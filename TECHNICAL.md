# Technical notes

This is the technical companion to the [README](README.md). It covers the original result, the data, the rules,
the full set of test statistics and how to reproduce everything. Every table is also in
[results/FINDINGS.md](results/FINDINGS.md), and a review of the original paper's methods is in
[METHODS_REVIEW.md](METHODS_REVIEW.md).

## The original study

Kenneth J. Arrow, "Economic Welfare and the Allocation of Resources for Invention," in *The Rate and Direction of
Inventive Activity: Economic and Social Factors*, Princeton University Press for the NBER, 1962, pp. 609–626. The
paper is theory and reports no data. Its headline result (pp. 620–622 and footnote 7) is that for a cost-reducing
invention the incentive to invent is always larger for an outside inventor licensing to a competitive industry than
for a monopolist protected by entry barriers. For a non-drastic invention the monopolist's gain is bounded by
$`(c - c')\,x'_m`$, below the competitive inventor's $`(c - c')\,x_c`$. For a drastic invention the gap is the
pre-invention monopoly profit $`P`$. The ratio of the two incentives always exceeds one and tends to $`x_c / x_m`$
for minor inventions. I checked these statements against the NBER scan of the chapter.

## Headline results

| Test | Estimate (SE) | 95% CI | p | N |
|---|---|---|---|---|
| Log R&D intensity on CR4/10, 2017 | 0.037 (0.078) | −0.116 to 0.189 | 0.64 | 36 |
| Log R&D intensity on CR4/10, 2022 | 0.092 (0.085) | −0.075 to 0.260 | 0.28 | 29 |
| Change in log intensity on change in CR4/10, 2017 → 2022 | 0.232 (0.137) | −0.037 to 0.501 | 0.09 | 29 |
| Same, without the three defense industries | 0.016 (0.126) | −0.230 to 0.263 | 0.90 | 26 |

Arrow predicts a negative sign in every row. None of the estimates is negative and significant, and the only
positive estimates near significance depend on three defense industries.

## Data

All inputs are committed in `data/raw/` and were downloaded on November 1, 2026.

| File | Source | Used for |
|---|---|---|
| `nsf20311_tab032_berd2017.xlsx` | NCSES, BERD 2017, Table 32 | Domestic R&D paid for and performed by the company, $ millions |
| `nsf24335_tab031_berd2022.xlsx` | NCSES, BERD 2022, Table 31 | Same, 2022 |
| `nsf20311_tab008_berd2017_sales.xlsx` | NCSES, BERD 2017, Table 8 | Domestic sales of R&D performers or funders |
| `nsf24335_tab008_berd2022_sales.xlsx` | NCSES, BERD 2022, Table 8 | Same, 2022 |
| `EC1700SIZECONCEN.zip`, `EC2200SIZECONCEN.zip` | Census, Economic Census, concentration by largest firms | CR4, CR8, HHI (top 50 firms), shipments at 6-digit NAICS |
| `EC1731BASIC.zip`, `EC2231BASIC.zip` | Census, Economic Census, manufacturing summary statistics | Value added, payroll, fringe benefits, shipments |

The BERD files come from `ncses.nsf.gov/pubs/nsf20311` and `ncses.nsf.gov/pubs/nsf24335`; the Census files from
`www2.census.gov/programs-surveys/economic-census/data/{2017,2022}/sector00/` and `.../sector31/`.

## Method

These rules were fixed before looking at any result, except the defense-industry exclusion in the extension, which I
added after seeing the main within-industry estimate in order to find what drove it.

- **Industries.** The finest BERD manufacturing rows that partition NAICS 31–33 without overlap (36 rows; parent rows
  such as 325 or 334 are not used when their pieces are listed). BERD "other" rows are the parent minus the listed
  siblings. Rows suppressed with a "D" in either the R&D or the sales table are dropped (none in 2017; seven in 2022).
- **R&D intensity.** Company-funded, company-performed domestic R&D divided by domestic sales of R&D performers or
  funders, both in dollars, so the ratio is not affected by the tables' rounding to 0.1 point.
- **Concentration.** CR4, CR8 and HHI of each 6-digit NAICS industry, averaged within a BERD industry with
  shipment weights. Census cells with a noise or suppression flag are treated as missing.
- **Margin.** The Collins–Preston price-cost margin, (value added − payroll − fringe benefits) / shipments, averaged the
  same way, used as the Lerner index $`L`$.
- **Inference.** OLS with HC1 standard errors; sales-weighted WLS; Spearman correlation; leave-one-industry-out
  slopes; a version without pharmaceuticals (3254) and semiconductors (3344).
- **Extension.** Industries present in both years (29). The change in log intensity regressed on the change in CR4
  (and HHI), unweighted and weighted by average R&D, with a version that drops the three industries whose main buyer is
  the Defense Department (336414–15 and 336419, 336992, 334511). This last version is post hoc.
- **Classification caveat.** BERD files each company under its main industry, so a company can move between BERD
  industries from one survey to the next. BERD domestic sales for guided missiles rose from $18,895 million to
  $102,365 million and for navigation instruments fell from $76,530 million to $25,280 million, while Census
  shipments moved from $26,219 million to $36,732 million and from $51,591 million to $53,454 million
  (`census_shipments_musd` in the industry files). The within-industry changes therefore mix real changes in research
  effort with changes in which companies are counted, and the defense rows are the clearest case.

The cross-industry and within-industry equations are

```math
\begin{aligned}
\ln(\text{RDI}_j) &= a + b\,\text{CR4}_j/10 + e_j \\
\Delta\ln(\text{RDI}_j) &= \alpha + \beta\,\Delta\text{CR4}_j/10 + u_j
\end{aligned}
```

with $`H_0\!: b = 0`$ and $`H_0\!: \beta = 0`$ against Arrow's $`b, \beta < 0`$.

Arrow's minor-invention ratio, used as a teaching measure and as one test, follows from constant-elasticity demand
$`x = A p^{-\varepsilon}`$. The monopolist sets $`p_m = c\,\varepsilon / (\varepsilon - 1)`$, so its Lerner index is
$`L = 1/\varepsilon`$ and

```math
\frac{x_m}{x_c} = \left(\frac{p_m}{c}\right)^{-\varepsilon} = \left(\frac{1}{1 - L}\right)^{-1/L} = (1 - L)^{1/L}
```

which approaches $`e^{-1} \approx 0.37`$ as $`L \to 0`$. Per dollar of sales the monopolist's incentive is
$`(c - c')\,x_m / (p_m x_m) = (1 - L)(c - c')/c`$, so holding the proportional cost saving fixed, R&D intensity
should be proportional to $`1 - L`$, a slope of +1 on $`\ln(1 - L)`$.

## Full test statistics

Cross-industry (from `results/cross_section_tests.csv`), slope per 10 points of CR4 or CR8, per 1,000 HHI points,
or per unit of $`\ln(1 - L)`$:

| Specification | 2017 | 2022 |
|---|---|---|
| CR4, OLS | 0.037 (0.078), p = 0.64 | 0.092 (0.085), p = 0.28 |
| CR4, WLS by sales | 0.004 (0.086), p = 0.96 | −0.038 (0.136), p = 0.78 |
| CR8, OLS | 0.051 (0.086), p = 0.56 | 0.120 (0.092), p = 0.19 |
| HHI, OLS | −0.050 (0.197), p = 0.80 | 0.270 (0.197), p = 0.17 |
| $`\ln(1 - L)`$, OLS (Arrow: +1) | −0.99 (1.51), p = 0.51 | 0.44 (2.21), p = 0.84 |
| Spearman, CR4 | 0.10, p = 0.55 | 0.22, p = 0.25 |
| CR4, leave-one-out range | −0.010 to 0.070 | 0.045 to 0.129 |
| CR4, without pharma and semiconductors | 0.056 (0.074), p = 0.44 | 0.118 (0.080), p = 0.14 |

Within-industry, 2017 → 2022 (from `results/changes_tests.csv`):

| Specification | Estimate | p | N |
|---|---|---|---|
| ΔCR4/10, OLS | 0.232 (0.137) | 0.09 | 29 |
| ΔCR4/10, WLS by average R&D | 0.000 (0.091) | 1.00 | 29 |
| ΔHHI/100, OLS | 0.080 (0.028) | 0.004 | 28 |
| ΔCR4/10, without defense industries | 0.016 (0.126) | 0.90 | 26 |
| ΔHHI/100, without defense industries | 0.028 (0.027) | 0.30 | 25 |
| ΔCR4/10, outcome Δ ln R&D | 0.669 (0.331) | 0.04 | 29 |
| ΔCR4/10, outcome Δ ln sales | 0.437 (0.327) | 0.18 | 29 |
| Spearman, ΔCR4 | 0.17 | 0.39 | 29 |
| Leave-one-out range | 0.148 to 0.278 | | 28 |
| Mean Δ ln intensity, CR4 rose vs fell | 0.117 vs 0.023, difference 0.093 | 0.36 | 16 / 13 |

## Reproducing the results

```bash
pip install -r requirements.txt
python src/arrow_industries.py
python src/concentration_changes.py
```

Python 3.12 or later. Both scripts run offline from `data/raw/` and write to `results/`.

## Repository layout

| Path | What it is |
|---|---|
| `src/arrow_industries.py` | Builds the industry panel, cross-industry tests, CR4 bands, first figure |
| `src/concentration_changes.py` | Within-industry changes 2017 → 2022, names table, second figure |
| `results/industries_2017.csv`, `results/industries_2022.csv` | Industry-level data |
| `results/cross_section_tests.csv`, `results/cr4_bands.csv` | Cross-industry results |
| `results/changes_industries.csv`, `results/changes_tests.csv` | Within-industry results |

## Substitutions

Arrow's monopoly is a barrier to entry and his competitive case includes an outside inventor with full royalty
power; neither can be observed, so concentration stands in for the first and low concentration for the second. I
first planned a within-industry comparison of public companies' R&D (market leaders against smaller rivals, using
SEC XBRL data), the most direct way to set Arrow against Gilbert and Newbery. The SEC's servers refused every
automated request I sent on the day I collected the data, so the change-over-time design replaced it.

## References

- Arrow, K. J. (1962). Economic welfare and the allocation of resources for invention. In *The Rate and Direction
  of Inventive Activity*, Princeton University Press for the NBER, 609–626.
- Gilbert, R. J. & Newbery, D. M. G. (1982). Preemptive patenting and the persistence of monopoly. *American
  Economic Review* 72(3), 514–526.
- Reinganum, J. F. (1983). Uncertain innovation and the persistence of monopoly. *American Economic Review* 73(4),
  741–748.
- US Department of Justice and Federal Trade Commission (2023). *Merger Guidelines*.
