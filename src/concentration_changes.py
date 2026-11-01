"""Within-industry version of the Arrow test: did R&D intensity fall where concentration rose?

The cross-industry comparison in arrow_industries.py is exposed to the oldest objection in this
literature: industries differ in technological opportunity (there is more left to discover in
drugs than in diesel), and that difference can swamp any effect of market structure. Comparing each
industry with itself between the 2017 and 2022 surveys differences out anything fixed about it.

Run src/arrow_industries.py first; this reads results/industries_2017.csv and industries_2022.csv.

Usage (from the repository root):
    python src/concentration_changes.py
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy import stats

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "results"

# Well-known companies in each industry, for the names table. The surveys do not name firms;
# these are the industry's leading US producers as commonly listed in company filings and the trade press.
LEADERS = {
    "3254": "Pfizer, Merck, Eli Lilly",
    "3344": "Intel, Texas Instruments, Micron",
    "333242": "Applied Materials, Lam Research, KLA",
    "3342": "Cisco, Motorola Solutions",
    "other 334": "Apple, Dell, HP",
    "334511": "RTX, L3Harris, Honeywell",
    "336411–13": "Boeing, GE Aerospace, RTX",
    "336414–15, 336419": "Lockheed Martin, Northrop Grumman",
    "336992": "General Dynamics, BAE Systems",
    "3361–63": "General Motors, Ford, Tesla",
    "324": "Marathon, Valero, Phillips 66",
    "312": "Altria, Coca-Cola, PepsiCo",
    "331": "Nucor, Steel Dynamics, Cleveland-Cliffs",
    "3391": "Medtronic, Stryker, Becton Dickinson",
    "334510, 334517": "GE HealthCare, Medtronic",
    "322": "International Paper, Smurfit Westrock",
    "321": "Weyerhaeuser, Louisiana-Pacific",
    "327": "Owens Corning, Corning",
}


# Industries whose main customer is the Defense Department (missiles and space, tanks, guidance systems).
DEFENSE = ["336414–15, 336419", "336992", "334511"]


def ols(y, x, w=None):
    X = sm.add_constant(x)
    model = sm.WLS(y, X, weights=w) if w is not None else sm.OLS(y, X)
    return model.fit(cov_type="HC1")


def main():
    a = pd.read_csv(OUT / "industries_2017.csv").set_index("berd_code")
    b = pd.read_csv(OUT / "industries_2022.csv").set_index("berd_code")
    keep = ["berd_label", "rd_musd", "berd_sales_musd", "rd_intensity", "cr4", "cr8", "hhi", "pcm"]
    d = a[keep].merge(b[keep], left_index=True, right_index=True, suffixes=("_17", "_22"))
    print(f"Loaded {len(a)} industries for 2017 and {len(b)} for 2022; {len(d)} appear in both")
    d["d_cr4"] = d.cr4_22 - d.cr4_17
    d["d_hhi"] = d.hhi_22 - d.hhi_17
    d["d_ln_intensity"] = np.log(d.rd_intensity_22 / d.rd_intensity_17)
    d["d_ln_rd"] = np.log(d.rd_musd_22 / d.rd_musd_17)
    d["d_ln_sales"] = np.log(d.berd_sales_musd_22 / d.berd_sales_musd_17)
    d["leaders"] = [LEADERS.get(c, "") for c in d.index]
    d.index.name = "berd_code"

    y = d.d_ln_intensity
    rows = []
    for name, x, w, how in [("d_cr4_per10", d.d_cr4 / 10, None, "OLS, HC1"),
                            ("d_cr4_per10", d.d_cr4 / 10, (d.rd_musd_17 + d.rd_musd_22) / 2,
                             "WLS by average R&D, HC1"),
                            ("d_hhi_per100", d.d_hhi / 100, None, "OLS, HC1")]:
        ok = x.notna()
        f = ols(y[ok], x[ok], None if w is None else w[ok])
        lo, hi = f.conf_int().iloc[1]
        rows.append({"regressor": name, "method": how, "n": int(ok.sum()), "slope": f.params.iloc[1],
                     "se": f.bse.iloc[1], "ci_low": lo, "ci_high": hi, "p": f.pvalues.iloc[1],
                     "r2": f.rsquared})
    # Splitting the change in intensity into its numerator and denominator.
    for part in ("d_ln_rd", "d_ln_sales"):
        f = ols(d[part], d.d_cr4 / 10)
        lo, hi = f.conf_int().iloc[1]
        rows.append({"regressor": "d_cr4_per10", "method": f"OLS, HC1, outcome {part}", "n": len(d),
                     "slope": f.params.iloc[1], "se": f.bse.iloc[1], "ci_low": lo, "ci_high": hi,
                     "p": f.pvalues.iloc[1], "r2": f.rsquared})
    # Without the three industries whose buyer is mainly the Defense Department.
    nd = d.drop(index=[c for c in DEFENSE if c in d.index])
    f = ols(nd.d_ln_intensity, nd.d_cr4 / 10)
    lo, hi = f.conf_int().iloc[1]
    rows.append({"regressor": "d_cr4_per10", "method": "OLS, HC1, without missiles, tanks and navigation instruments",
                 "n": len(nd), "slope": f.params.iloc[1], "se": f.bse.iloc[1], "ci_low": lo, "ci_high": hi,
                 "p": f.pvalues.iloc[1], "r2": f.rsquared})
    nh = nd.dropna(subset=["d_hhi"])
    f = ols(nh.d_ln_intensity, nh.d_hhi / 100)
    lo, hi = f.conf_int().iloc[1]
    rows.append({"regressor": "d_hhi_per100", "method": "OLS, HC1, without missiles, tanks and navigation instruments",
                 "n": len(nh), "slope": f.params.iloc[1], "se": f.bse.iloc[1], "ci_low": lo, "ci_high": hi,
                 "p": f.pvalues.iloc[1], "r2": f.rsquared})
    rho, p = stats.spearmanr(d.d_cr4, y)
    rows.append({"regressor": "d_cr4", "method": "Spearman rank correlation", "n": len(d), "slope": rho, "p": p})
    loo = [ols(y.drop(i), d.d_cr4.drop(i) / 10).params.iloc[1] for i in d.index]
    rows.append({"regressor": "d_cr4_per10", "method": "OLS, leave-one-industry-out min", "n": len(d) - 1, "slope": min(loo)})
    rows.append({"regressor": "d_cr4_per10", "method": "OLS, leave-one-industry-out max", "n": len(d) - 1, "slope": max(loo)})
    rose, fell = d[d.d_cr4 > 0], d[d.d_cr4 <= 0]
    rows.append({"regressor": "group means", "method": "mean change in log intensity, CR4 rose",
                 "n": len(rose), "slope": rose.d_ln_intensity.mean()})
    rows.append({"regressor": "group means", "method": "mean change in log intensity, CR4 fell or unchanged",
                 "n": len(fell), "slope": fell.d_ln_intensity.mean()})
    t = stats.ttest_ind(rose.d_ln_intensity, fell.d_ln_intensity, equal_var=False)
    rows.append({"regressor": "group means", "method": "difference, CR4 rose minus fell (Welch t-test)",
                 "n": len(d), "slope": rose.d_ln_intensity.mean() - fell.d_ln_intensity.mean(), "p": t.pvalue})
    res = pd.DataFrame(rows)
    res.to_csv(OUT / "changes_tests.csv", index=False, float_format="%.4f")

    cols = ["berd_label_17", "leaders", "cr4_17", "cr4_22", "d_cr4", "rd_intensity_17", "rd_intensity_22",
            "d_ln_intensity", "rd_musd_17", "rd_musd_22", "berd_sales_musd_17", "berd_sales_musd_22",
            "hhi_17", "hhi_22", "pcm_17", "pcm_22"]
    d.sort_values("d_cr4")[cols].rename(columns={"berd_label_17": "industry"}).to_csv(
        OUT / "changes_industries.csv", float_format="%.4f")

    fig, ax = plt.subplots(figsize=(7.4, 4.8))
    ax.scatter(d.d_cr4, d.d_ln_intensity, s=np.sqrt(d.rd_musd_22) * 3, color="#3b6ea5", alpha=0.65,
               edgecolor="white", linewidth=1.5)
    f = ols(y, d.d_cr4)
    xs = np.linspace(d.d_cr4.min(), d.d_cr4.max(), 50)
    ax.plot(xs, f.params.iloc[0] + f.params.iloc[1] * xs, color="#c0504d", lw=1.5)
    ax.axhline(0, color="#777777", lw=0.8)
    ax.axvline(0, color="#777777", lw=0.8)
    short = {"3254": "Pharmaceuticals", "3344": "Semiconductors", "336411–13": "Aircraft",
             "3361–63": "Motor vehicles", "324": "Petroleum refining", "334511": "Navigation instruments",
             "336414–15, 336419": "Missiles and space", "3342": "Communications equip.", "312": "Beverages & tobacco",
             "336992": "Tanks", "other 334": "Computers, other electronics"}
    for c, r in d.iterrows():
        if c in short:
            ax.annotate(short[c], (r.d_cr4, r.d_ln_intensity), fontsize=7.5, xytext=(4, 3),
                        textcoords="offset points", color="#333333")
    ax.set_xlabel("Change in four-firm concentration, 2017 to 2022 (points)")
    ax.set_ylabel("Change in log R&D intensity, 2017 to 2022")
    ax.set_title(f"Changes in concentration and R&D intensity, {len(d)} industries (line: OLS fit)", fontsize=10)
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(alpha=0.2, lw=0.6)
    fig.tight_layout()
    fig.savefig(OUT / "changes_scatter.png", dpi=160)
    plt.close(fig)
    print(res[["regressor", "method", "n", "slope", "se", "p"]].to_string(index=False))


if __name__ == "__main__":
    main()
