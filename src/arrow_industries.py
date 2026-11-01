"""Arrow (1962) across US manufacturing: do concentrated industries spend less on R&D?

Arrow's replacement effect predicts that an industry shielded from entry has a weaker incentive
to invent than a competitive one. This script pairs company-funded R&D intensity from the NSF
Business Enterprise Research and Development Survey (BERD, 2017 and 2022) with Census Economic
Census concentration (CR4, CR8, HHI) and price-cost margins for the same years, aggregated from
6-digit NAICS industries up to the BERD industry groups, and tests the sign of the relationship.

Inputs (all committed in data/raw/):
    nsf20311_tab032_berd2017.xlsx, nsf24335_tab031_berd2022.xlsx   NSF BERD R&D (Tables 32 / 31)
    nsf20311_tab008_berd2017_sales.xlsx, nsf24335_tab008_...       NSF BERD sales (Table 8)
    EC1700SIZECONCEN.zip, EC2200SIZECONCEN.zip                      Census concentration
    EC1731BASIC.zip, EC2231BASIC.zip                                Census manufacturing statistics

Usage (from the repository root):
    python src/arrow_industries.py
"""

import warnings
import zipfile
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy import stats

# The NSF workbooks lack a default style, which openpyxl reports on every read; it is harmless.
warnings.filterwarnings("ignore", message="Workbook contains no default style")

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw"
OUT = ROOT / "results"

BERD_FILES = {2017: "nsf20311_tab032_berd2017.xlsx", 2022: "nsf24335_tab031_berd2022.xlsx"}
SALES_FILES = {2017: "nsf20311_tab008_berd2017_sales.xlsx", 2022: "nsf24335_tab008_berd2022_sales.xlsx"}

# The finest BERD manufacturing rows, which together partition NAICS 31-33 without double counting.
# Parent rows (325, 333, 334, 3345, 336, 3364, 339) are not used because their pieces are listed.
LEAVES = ["311", "312", "313–16", "321", "322", "323", "324", "3251", "3252", "3253", "3254",
          "3256", "3255, 3259", "326", "327", "331", "332", "33311", "333242", "3336",
          "other 333", "3342", "3344", "334510, 334517", "334511", "other 3345", "other 334",
          "335", "3361–63", "336411–13", "336414–15, 336419", "336992", "other 336", "337",
          "3391", "3399"]

# What BERD's "other" rows leave out: the sibling rows listed in the same table (BERD table notes).
OTHER_EXCLUDES = {
    "other 333": ["33311", "333242", "3336"],
    "other 3345": ["334510", "334517", "334511"],
    "other 334": ["3342", "3344", "3345"],
    "other 336": ["3361", "3362", "3363", "3364", "336992"],
}

# Bands for the summary table. 50% is the four-firm level the 1968 DOJ merger guidelines and much of
# the structure-conduct literature treated as "highly concentrated"; 30% splits the rest roughly in half.
CR4_BANDS = [0, 30, 50, 101]


def naics_prefixes(code):
    """Turn a BERD NAICS label ('3361–63', '334510, 334517', 'other 333') into include/exclude prefixes."""
    if code.startswith("other "):
        return [code.split()[1]], OTHER_EXCLUDES[code]
    include = []
    for part in code.split(","):
        part = part.strip()
        if "–" in part:
            start, end = part.split("–")
            stem = start[: len(start) - len(end)]
            include += [stem + str(k).zfill(len(end)) for k in range(int(start[-len(end):]), int(end) + 1)]
        else:
            include.append(part)
    return include, []


def berd_rows(path, value_col):
    """Leaf-industry rows of one BERD table: {code: (label, value)}; 'D' (suppressed) becomes NaN."""
    df = pd.read_excel(path, header=None, engine="openpyxl")
    rows = {}
    for r in df.itertuples(index=False):
        label, code = r[0], r[1]
        if isinstance(code, (int, float)) and not pd.isna(code):
            code = str(int(code))  # Excel stores plain codes such as 3254 as numbers
        if isinstance(code, str) and " ".join(code.split()) in LEAVES:
            code = " ".join(code.split())
            rows.setdefault(code, (str(label).strip(), pd.to_numeric(r[value_col], errors="coerce")))
    return rows


def load_berd(year):
    """BERD company-funded domestic R&D and domestic sales of R&D performers or funders, by industry."""
    rd = berd_rows(RAW / BERD_FILES[year], 2)       # column 2: domestic R&D, $ millions
    sales = berd_rows(RAW / SALES_FILES[year], 4)   # column 4: domestic sales of performers or funders
    out = pd.DataFrame([{"berd_code": c, "berd_label": rd[c][0], "rd_musd": rd[c][1],
                         "berd_sales_musd": sales.get(c, ("", np.nan))[1]} for c in LEAVES if c in rd])
    suppressed = out[out.rd_musd.isna() | out.berd_sales_musd.isna()].berd_code.tolist()
    out = out.dropna(subset=["rd_musd", "berd_sales_musd"])
    out = out[out.rd_musd > 0]
    # Computed from dollars rather than the table's percentage, which is rounded to 0.1 point.
    out["rd_intensity"] = out.rd_musd / out.berd_sales_musd * 100
    print(f"BERD {year}: {len(LEAVES)} leaf industries defined, {len(out)} kept, "
          f"{len(suppressed)} suppressed (D) and dropped: {', '.join(suppressed) or 'none'}")
    return out.reset_index(drop=True)


def read_dat(zip_name):
    with zipfile.ZipFile(RAW / zip_name) as z:
        name = [n for n in z.namelist() if n.endswith(".dat")][0]
        with z.open(name) as f:
            df = pd.read_csv(f, sep="|", dtype=str, keep_default_na=False)
    df.columns = [c.lstrip("#") for c in df.columns]
    return df


def num(df, col):
    v = pd.to_numeric(df[col], errors="coerce")
    flag = f"{col}_F"
    return v.where(df[flag].isin(["", "0"])) if flag in df else v


def load_census(year):
    """6-digit manufacturing CR4, CR8, HHI, shipments and price-cost margin for one Census year."""
    yy = str(year)[2:]
    code = f"NAICS{year}"
    con = read_dat(f"EC{yy}00SIZECONCEN.zip")
    con = con[(con.GEOTYPE == "01") & (con.TYPOP == "00") & con[code].str.fullmatch(r"3[1-3]\d{4}")]
    con = con.assign(val_pct=num(con, "VAL_PCT"), hhi=num(con, "HHI"), rcptot=num(con, "RCPTOT"))
    by = {c: con[con.CONCENFI == c].set_index(code) for c in ("001", "604", "608", "650")}
    out = pd.DataFrame({"shipments_k": by["001"].rcptot, "cr4": by["604"].val_pct,
                        "cr8": by["608"].val_pct, "hhi": by["650"].hhi})
    basic = read_dat(f"EC{yy}31BASIC.zip")
    basic = basic[(basic.GEOTYPE == "01") & basic[code].str.fullmatch(r"3[1-3]\d{4}")]
    basic = basic.drop_duplicates(code).set_index(code)
    # Collins-Preston price-cost margin: (value added - payroll - fringe benefits) / shipments.
    pcm = (num(basic, "VALADD") - num(basic, "PAYANN") - num(basic, "BENEFIT")) / num(basic, "RCPTOT")
    out = out.join(pcm.rename("pcm"))
    n0 = len(out)
    out = out.dropna(subset=["cr4", "shipments_k"])
    print(f"Census {year}: {n0} six-digit manufacturing industries, {len(out)} with CR4 and shipments, "
          f"{out.hhi.notna().sum()} with HHI, {out.pcm.notna().sum()} with a price-cost margin")
    return out


def aggregate(census, berd):
    """Shipment-weighted average of 6-digit Census measures inside each BERD industry group."""
    rows = []
    for b in berd.itertuples(index=False):
        inc, exc = naics_prefixes(b.berd_code)
        idx = census.index.to_series()
        mask = idx.apply(lambda n: any(n.startswith(p) for p in inc) and not any(n.startswith(p) for p in exc))
        sub = census[mask.values]
        w = sub.shipments_k
        row = b._asdict()
        row["n_naics6"] = len(sub)
        row["census_shipments_musd"] = w.sum() / 1000
        for m in ("cr4", "cr8", "hhi", "pcm"):
            ok = sub[m].notna()
            row[m] = np.average(sub.loc[ok, m], weights=w[ok]) if ok.any() else np.nan
        top = sub.sort_values("shipments_k", ascending=False).head(1)
        row["largest_naics6"] = top.index[0] if len(top) else ""
        rows.append(row)
    out = pd.DataFrame(rows)
    # Arrow's ratio for a minor process invention, monopoly incentive / competitive incentive,
    # x_m / x_c = (1 - L)^(1/L) for constant-elasticity demand with Lerner index L = pcm.
    out["arrow_ratio"] = (1 - out.pcm) ** (1 / out.pcm)
    return out


def ols(y, x, w=None):
    X = sm.add_constant(x)
    model = sm.WLS(y, X, weights=w) if w is not None else sm.OLS(y, X)
    return model.fit(cov_type="HC1")


def tests(ind, year):
    """Slope of log R&D intensity on concentration and on the margin, several ways."""
    y = np.log(ind.rd_intensity)
    rows = []
    specs = [("cr4_per10", ind.cr4 / 10, None, "OLS, HC1"),
             ("cr4_per10", ind.cr4 / 10, ind.berd_sales_musd, "WLS by R&D-performer sales, HC1"),
             ("cr8_per10", ind.cr8 / 10, None, "OLS, HC1"),
             ("hhi_per1000", ind.hhi / 1000, None, "OLS, HC1"),
             ("log_one_minus_pcm", np.log(1 - ind.pcm), None, "OLS, HC1 (Arrow predicts slope +1)")]
    for name, x, w, how in specs:
        ok = x.notna() & y.notna()
        f = ols(y[ok], x[ok], None if w is None else w[ok])
        lo, hi = f.conf_int().iloc[1]
        rows.append({"year": year, "regressor": name, "method": how, "n": int(ok.sum()),
                     "slope": f.params.iloc[1], "se": f.bse.iloc[1], "ci_low": lo, "ci_high": hi,
                     "p": f.pvalues.iloc[1], "r2": f.rsquared})
    rho, p = stats.spearmanr(ind.cr4, ind.rd_intensity)
    rows.append({"year": year, "regressor": "cr4", "method": "Spearman rank correlation",
                 "n": len(ind), "slope": rho, "p": p})
    # Leave-one-industry-out range of the main slope.
    loo = []
    for i in ind.index:
        d = ind.drop(i)
        loo.append(ols(np.log(d.rd_intensity), d.cr4 / 10).params.iloc[1])
    rows.append({"year": year, "regressor": "cr4_per10", "method": "OLS, leave-one-industry-out min",
                 "n": len(ind) - 1, "slope": min(loo)})
    rows.append({"year": year, "regressor": "cr4_per10", "method": "OLS, leave-one-industry-out max",
                 "n": len(ind) - 1, "slope": max(loo)})
    # Without the two industries the literature singles out for technological opportunity.
    d = ind[~ind.berd_code.isin(["3254", "3344"])]
    f = ols(np.log(d.rd_intensity), d.cr4 / 10)
    lo, hi = f.conf_int().iloc[1]
    rows.append({"year": year, "regressor": "cr4_per10", "method": "OLS, HC1, without pharma (3254) and semiconductors (3344)",
                 "n": len(d), "slope": f.params.iloc[1], "se": f.bse.iloc[1], "ci_low": lo, "ci_high": hi,
                 "p": f.pvalues.iloc[1], "r2": f.rsquared})
    return pd.DataFrame(rows)


def bands(ind, year):
    b = pd.cut(ind.cr4, CR4_BANDS, right=False, labels=["under 30%", "30% to 50%", "50% or more"])
    g = ind.groupby(b, observed=False)
    out = pd.DataFrame({
        "year": year,
        "industries": g.size(),
        "mean_rd_intensity": g.rd_intensity.mean(),
        "median_rd_intensity": g.rd_intensity.median(),
        "pooled_rd_intensity": g.rd_musd.sum() / g.berd_sales_musd.sum() * 100,
        "rd_musd": g.rd_musd.sum(),
    })
    out.index.name = "cr4_band"
    return out.reset_index()


def figure(both):
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.6), sharey=True)
    short = {"3254": "Pharmaceuticals", "3344": "Semiconductors", "333242": "Chip-making machinery",
             "336411–13": "Aircraft", "312": "Beverages & tobacco",
             "324": "Petroleum refining", "3361–63": "Motor vehicles"}
    for ax, (year, ind) in zip(axes, both.items()):
        ax.scatter(ind.cr4, ind.rd_intensity, s=np.sqrt(ind.berd_sales_musd) * 0.9,
                   color="#3b6ea5", alpha=0.65, edgecolor="white", linewidth=1.5)
        f = ols(np.log(ind.rd_intensity), ind.cr4)
        xs = np.linspace(ind.cr4.min(), ind.cr4.max(), 50)
        ax.plot(xs, np.exp(f.params.iloc[0] + f.params.iloc[1] * xs), color="#c0504d", lw=1.5)
        for r in ind.itertuples():
            if r.berd_code in short:
                ax.annotate(short[r.berd_code], (r.cr4, r.rd_intensity), fontsize=7.5,
                            xytext=(4, 3), textcoords="offset points", color="#333333")
        ax.set_yscale("log")
        ax.set_title(f"{year}: {len(ind)} manufacturing industries", fontsize=10)
        ax.set_xlabel("Four-firm concentration ratio (shipment-weighted, %)")
        ax.grid(alpha=0.2, lw=0.6)
        ax.spines[["top", "right"]].set_visible(False)
    axes[0].set_ylabel("Company-funded R&D, % of domestic sales (log scale)")
    fig.suptitle("R&D intensity does not fall as concentration rises (line: OLS fit of log intensity on CR4)",
                 fontsize=11)
    fig.tight_layout()
    fig.savefig(OUT / "rd_vs_concentration.png", dpi=160)
    plt.close(fig)


def main():
    OUT.mkdir(exist_ok=True)
    both, all_tests, all_bands = {}, [], []
    for year in (2017, 2022):
        berd = load_berd(year)
        census = load_census(year)
        ind = aggregate(census, berd)
        empty = ind[ind.n_naics6 == 0].berd_code.tolist()
        ind = ind[ind.n_naics6 > 0].dropna(subset=["cr4"]).reset_index(drop=True)
        print(f"  {year}: {len(ind)} BERD industries matched to Census; dropped with no 6-digit match: {empty or 'none'}")
        ind.to_csv(OUT / f"industries_{year}.csv", index=False, float_format="%.4f")
        all_tests.append(tests(ind, year))
        all_bands.append(bands(ind, year))
        both[year] = ind
    t = pd.concat(all_tests, ignore_index=True)
    t.to_csv(OUT / "cross_section_tests.csv", index=False, float_format="%.4f")
    bd = pd.concat(all_bands, ignore_index=True)
    bd.to_csv(OUT / "cr4_bands.csv", index=False, float_format="%.3f")
    figure(both)
    print(t[["year", "regressor", "method", "n", "slope", "se", "p"]].to_string(index=False))
    print(bd.to_string(index=False))


if __name__ == "__main__":
    main()
