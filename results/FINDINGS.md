# Arrow (1962) on modern data: findings

## In plain English

Kenneth Arrow argued in 1962 that a monopolist protected from entry has a weaker reason to invent than a
competitive industry, because each improvement mostly replaces profit it already earns. If he was right, the more
concentrated American manufacturing industries should put a smaller share of their revenue into research.

- **They do not.** In 2017 and 2022, industries where the top four companies hold more of the market spend, if
  anything, slightly more of their sales on research. Chip-making machinery (Applied Materials, Lam Research, KLA)
  is highly concentrated and research-heavy; beverages and tobacco (Altria, Coca-Cola, PepsiCo) is concentrated and
  spends half a cent of each sales dollar.
- **The biggest research spenders sit in the middle.** Semiconductors (Intel, Texas Instruments, Micron) and
  pharmaceuticals (Pfizer, Merck, Eli Lilly) spend 22.6% and 15.3% of sales, with four-firm shares near 40%.
- **Changes over time tell the same story.** Where concentration rose between 2017 and 2022, research intensity did
  not fall. A positive association appears only because of three defense industries (Lockheed Martin, Northrop
  Grumman, RTX and others), where concentration and measured R&D intensity both rose; without them the slope is
  close to zero. The defense jumps partly reflect companies being refiled between survey industries.

A narrative tour is in the [README](../README.md); methods and every statistic are in
[TECHNICAL.md](../TECHNICAL.md).

## Key to the labels

*Code* is the NAICS code or code group used by the NSF Business Enterprise Research and Development Survey (BERD);
"other 333" means NAICS 333 minus the sibling rows listed separately. *R&D $M* is domestic R&D paid for and
performed by the companies, millions of dollars. *Sales $M* is domestic sales of R&D performers or funders.
*R&D %* is their ratio. *CR4* and *CR8* are the shares of shipments made by the 4 and 8 largest companies, and
*HHI* is the Herfindahl-Hirschman Index of the 50 largest, each averaged over 6-digit NAICS industries with shipment
weights. *PCM* is the price-cost margin, (value added − payroll − benefits) / shipments. *x_m/x_c* is Arrow's
minor-invention ratio of monopoly to competitive incentive under constant-elasticity demand, $`(1 - L)^{1/L}`$ with
$`L`$ = PCM. *NAICS-6* is the number of 6-digit Census industries averaged. In the test tables, *slope* is per 10
points of CR4 or CR8, per 1,000 (levels) or 100 (changes) HHI points, or per unit of $`\ln(1 - L)`$, with HC1
standard errors; *p* is two-sided.

### industries_2017.csv

| Code | Industry | R&D $M | Sales $M | R&D % | CR4 | CR8 | HHI | PCM | x_m/x_c | NAICS-6 |
|---|---|---|---|---|---|---|---|---|---|---|
| 311 | Food | 4,453 | 647,782 | 0.69 | 45.3 | 58.2 | 708 | 0.256 | 0.315 | 42 |
| 312 | Beverage and tobacco products | 968 | 150,683 | 0.64 | 67.2 | 75.1 | 1,152 | 0.551 | 0.234 | 7 |
| 313–16 | Textile, apparel, and leather products | 919 | 81,151 | 1.13 | 33.9 | 46.7 | 498 | 0.229 | 0.321 | 23 |
| 321 | Wood products | 170 | 27,589 | 0.62 | 32.4 | 43.0 | 388 | 0.237 | 0.319 | 14 |
| 322 | Paper | 1,292 | 166,833 | 0.77 | 50.8 | 64.2 | 902 | 0.301 | 0.304 | 11 |
| 323 | Printing and related support activities | 218 | 40,404 | 0.54 | 16.9 | 22.9 | 121 | 0.282 | 0.309 | 4 |
| 324 | Petroleum and coal products | 301 | 233,600 | 0.13 | 44.9 | 66.6 | 706 | 0.169 | 0.334 | 5 |
| 3251 | Basic chemicals | 2,393 | 158,316 | 1.51 | 45.6 | 58.4 | 452 | 0.363 | 0.289 | 7 |
| 3252 | Resin, synthetic rubber, and artificial synthetic fibers and filaments | 612 | 43,430 | 1.41 | 30.6 | 45.3 | 399 | 0.266 | 0.313 | 3 |
| 3253 | Pesticide, fertilizer, and other agricultural chemicals | 1,092 | 69,085 | 1.58 | 59.5 | 70.8 | 930 | 0.426 | 0.272 | 4 |
| 3254 | Pharmaceuticals and medicines | 55,229 | 466,391 | 11.84 | 43.0 | 57.6 | 644 | 0.570 | 0.228 | 4 |
| 3256 | Soap, cleaning compound, and toilet preparation | 2,488 | 98,208 | 2.53 | 54.4 | 64.7 | 1,381 | 0.503 | 0.249 | 4 |
| 3255, 3259 | Paint, coating, adhesive, and other chemicals | 1,471 | 66,428 | 2.21 | 32.8 | 46.7 | 447 | 0.347 | 0.293 | 7 |
| 326 | Plastics and rubber products | 3,637 | 187,102 | 1.94 | 26.0 | 35.6 | 324 | 0.292 | 0.307 | 16 |
| 327 | Nonmetallic mineral products | 1,303 | 45,621 | 2.86 | 35.3 | 46.5 | 545 | 0.351 | 0.292 | 18 |
| 331 | Primary metals | 741 | 91,446 | 0.81 | 44.8 | 62.0 | 728 | 0.246 | 0.317 | 18 |
| 332 | Fabricated metal products | 2,099 | 111,740 | 1.88 | 22.6 | 31.5 | 255 | 0.275 | 0.311 | 36 |
| 33311 | Agricultural implement | 1,511 | 46,786 | 3.23 | 55.7 | 66.5 |  | 0.255 | 0.315 | 2 |
| 333242 | Semiconductor machinery | 3,228 | 20,067 | 16.09 | 56.9 | 73.2 | 1,030 | 0.143 | 0.340 | 1 |
| 3336 | Engine, turbine, and power transmission equipment | 1,921 | 35,990 | 5.34 | 55.5 | 69.1 | 917 | 0.230 | 0.321 | 4 |
| other 333 | Other machinery | 5,596 | 220,238 | 2.54 | 31.2 | 42.3 | 397 | 0.281 | 0.309 | 32 |
| 3342 | Communications equipment | 10,972 | 88,593 | 12.38 | 43.8 | 60.1 | 557 | 0.284 | 0.308 | 3 |
| 3344 | Semiconductor and other electronic components | 27,859 | 171,921 | 16.20 | 38.5 | 52.1 | 323 | 0.271 | 0.311 | 6 |
| 334510, 334517 | Electromedical, electrotherapeutic, and irradiation apparatus | 2,545 | 22,449 | 11.34 | 38.1 | 49.7 | 354 | 0.381 | 0.284 | 2 |
| 334511 | Search, detection, navigation, guidance, aeronautical, and nautical system and instrument | 3,214 | 76,530 | 4.20 | 50.4 | 72.7 | 852 | 0.299 | 0.305 | 1 |
| other 3345 | Other measuring and controlling device | 4,329 | 69,039 | 6.27 | 29.1 | 41.0 | 325 | 0.307 | 0.303 | 6 |
| other 334 | Other computer and electronic products | 21,022 | 268,585 | 7.83 | 53.0 | 64.7 | 695 | 0.326 | 0.298 | 6 |
| 335 | Electrical equipment, appliances, and components | 4,110 | 113,434 | 3.62 | 45.2 | 60.2 | 625 | 0.283 | 0.309 | 18 |
| 3361–63 | Automobiles, bodies, trailers, and parts | 21,137 | 756,472 | 2.79 | 53.4 | 73.0 | 1,112 | 0.170 | 0.334 | 15 |
| 336411–13 | Aircraft, aircraft engine, and aircraft parts | 11,473 | 331,306 | 3.46 | 81.5 | 87.7 | 2,112 | 0.374 | 0.286 | 3 |
| 336414–15, 336419 | Guided missile, space vehicle, and related parts | 430 | 18,895 | 2.28 | 90.6 | 97.4 | 2,792 | 0.216 | 0.324 | 3 |
| 336992 | Military armored vehicle, tank, and tank component | 4 | 322 | 1.24 | 79.6 | 89.0 | 2,021 | 0.305 | 0.303 | 1 |
| other 336 | Other transportation | 1,585 | 66,100 | 2.40 | 55.6 | 67.1 | 713 | 0.235 | 0.320 | 5 |
| 337 | Furniture and related products | 419 | 43,772 | 0.96 | 35.1 | 43.4 | 519 | 0.272 | 0.311 | 12 |
| 3391 | Medical equipment and supplies | 13,348 | 309,223 | 4.32 | 32.8 | 47.5 | 402 | 0.405 | 0.278 | 5 |
| 3399 | Other miscellaneous manufacturing | 2,062 | 78,464 | 2.63 | 27.2 | 37.9 | 311 | 0.329 | 0.297 | 11 |

### industries_2022.csv

| Code | Industry | R&D $M | Sales $M | R&D % | CR4 | CR8 | HHI | PCM | x_m/x_c | NAICS-6 |
|---|---|---|---|---|---|---|---|---|---|---|
| 312 | Beverage and tobacco products | 660 | 133,830 | 0.49 | 62.9 | 72.3 | 734 | 0.522 | 0.243 | 7 |
| 321 | Wood products | 254 | 61,018 | 0.42 | 34.2 | 46.0 | 420 | 0.314 | 0.301 | 13 |
| 322 | Paper | 1,004 | 98,823 | 1.02 | 48.9 | 61.4 | 887 | 0.303 | 0.304 | 10 |
| 323 | Printing and related support activities | 164 | 29,296 | 0.56 | 14.1 | 19.7 | 95 | 0.309 | 0.302 | 4 |
| 324 | Petroleum and coal products | 856 | 399,161 | 0.21 | 51.6 | 71.2 | 848 | 0.184 | 0.331 | 5 |
| 3252 | Resin, synthetic rubber, and artificial synthetic fibers and filaments | 1,413 | 91,925 | 1.54 | 35.4 | 48.5 | 442 | 0.297 | 0.305 | 3 |
| 3254 | Pharmaceuticals and medicines | 104,720 | 685,744 | 15.27 | 38.0 | 52.9 | 528 | 0.568 | 0.228 | 4 |
| 3255, 3259 | Paint, coating, adhesive, and other chemicals | 1,195 | 67,008 | 1.78 | 33.1 | 46.6 | 485 | 0.332 | 0.297 | 7 |
| 326 | Plastics and rubber products | 3,251 | 253,088 | 1.28 | 25.7 | 35.8 | 313 | 0.305 | 0.303 | 16 |
| 327 | Nonmetallic mineral products | 1,435 | 66,532 | 2.16 | 37.0 | 48.1 | 541 | 0.352 | 0.291 | 18 |
| 331 | Primary metals | 1,099 | 160,761 | 0.68 | 49.7 | 65.2 | 845 | 0.273 | 0.311 | 18 |
| 332 | Fabricated metal products | 3,304 | 188,388 | 1.75 | 23.4 | 32.3 | 252 | 0.296 | 0.305 | 36 |
| 333242 | Semiconductor machinery | 5,390 | 32,885 | 16.39 | 60.7 | 78.2 | 1,153 | 0.153 | 0.338 | 1 |
| other 333 | Other machinery | 7,987 | 313,360 | 2.55 | 29.9 | 40.7 | 366 | 0.270 | 0.312 | 28 |
| 3342 | Communications equipment | 10,870 | 94,162 | 11.54 | 49.8 | 64.6 | 795 | 0.248 | 0.317 | 3 |
| 3344 | Semiconductor and other electronic components | 47,380 | 209,620 | 22.60 | 40.6 | 54.4 | 713 | 0.250 | 0.316 | 6 |
| 334510, 334517 | Electromedical, electrotherapeutic, and irradiation apparatus | 3,959 | 34,617 | 11.44 | 35.9 | 47.9 | 538 | 0.302 | 0.304 | 2 |
| 334511 | Search, detection, navigation, guidance, aeronautical, and nautical system and instruments | 2,170 | 25,280 | 8.58 | 57.9 | 78.2 | 1,200 | 0.297 | 0.305 | 1 |
| other 3345 | Other measuring and controlling devices | 3,976 | 61,566 | 6.46 | 27.4 | 39.9 | 307 | 0.323 | 0.299 | 6 |
| other 334 | Other computer and electronic products | 30,879 | 309,204 | 9.99 | 57.8 | 71.9 | 683 | 0.224 | 0.322 | 5 |
| 335 | Electrical equipment, appliances, and components | 6,657 | 190,989 | 3.49 | 48.4 | 62.6 | 568 | 0.319 | 0.300 | 16 |
| 3361–63 | Motor vehicles, bodies, trailers, and parts | 30,722 | 934,230 | 3.29 | 47.9 | 67.8 | 826 | 0.175 | 0.333 | 14 |
| 336411–13 | Aircraft, aircraft engine, and aircraft parts | 9,303 | 254,318 | 3.66 | 73.6 | 83.4 |  | 0.233 | 0.320 | 3 |
| 336414–15, 336419 | Guided missile, space vehicle, and related parts | 4,483 | 102,365 | 4.38 | 95.8 | 98.7 | 3,102 | 0.139 | 0.341 | 3 |
| 336992 | Military armored vehicle, tank, and tank components | 26 | 1,288 | 2.02 | 85.1 | 92.8 | 2,289 | 0.371 | 0.287 | 1 |
| other 336 | Other transportation | 1,935 | 85,180 | 2.27 | 55.5 | 67.8 | 749 | 0.225 | 0.322 | 5 |
| 337 | Furniture and related products | 405 | 38,358 | 1.06 | 32.7 | 41.2 | 417 | 0.287 | 0.308 | 11 |
| 3391 | Medical equipment and supplies | 20,112 | 439,882 | 4.57 | 32.9 | 46.3 | 351 | 0.375 | 0.286 | 5 |
| 3399 | Other miscellaneous manufacturing | 2,921 | 98,835 | 2.96 | 26.0 | 35.9 | 260 | 0.323 | 0.299 | 11 |

### cross_section_tests.csv

| year | regressor | method | n | slope | se | ci_low | ci_high | p | r2 |
|---|---|---|---|---|---|---|---|---|---|
| 2017 | cr4_per10 | OLS, HC1 | 36 | 0.037 | 0.078 | -0.116 | 0.189 | 0.638 | 0.003 |
| 2017 | cr4_per10 | WLS by R&D-performer sales, HC1 | 36 | 0.004 | 0.086 | -0.165 | 0.174 | 0.960 | 0.000 |
| 2017 | cr8_per10 | OLS, HC1 | 36 | 0.051 | 0.086 | -0.118 | 0.219 | 0.555 | 0.006 |
| 2017 | hhi_per1000 | OLS, HC1 | 35 | -0.050 | 0.197 | -0.435 | 0.335 | 0.800 | 0.001 |
| 2017 | log_one_minus_pcm | OLS, HC1 (Arrow predicts slope +1) | 36 | -0.995 | 1.508 | -3.950 | 1.961 | 0.509 | 0.020 |
| 2017 | cr4 | Spearman rank correlation | 36 | 0.104 |  |  |  | 0.547 |  |
| 2017 | cr4_per10 | OLS, leave-one-industry-out min | 35 | -0.010 |  |  |  |  |  |
| 2017 | cr4_per10 | OLS, leave-one-industry-out max | 35 | 0.070 |  |  |  |  |  |
| 2017 | cr4_per10 | OLS, HC1, without pharma (3254) and semiconductors (3344) | 34 | 0.056 | 0.074 | -0.088 | 0.201 | 0.445 | 0.009 |
| 2022 | cr4_per10 | OLS, HC1 | 29 | 0.092 | 0.085 | -0.075 | 0.260 | 0.280 | 0.021 |
| 2022 | cr4_per10 | WLS by R&D-performer sales, HC1 | 29 | -0.038 | 0.136 | -0.304 | 0.228 | 0.778 | 0.002 |
| 2022 | cr8_per10 | OLS, HC1 | 29 | 0.120 | 0.092 | -0.061 | 0.301 | 0.194 | 0.036 |
| 2022 | hhi_per1000 | OLS, HC1 | 28 | 0.270 | 0.197 | -0.115 | 0.656 | 0.169 | 0.019 |
| 2022 | log_one_minus_pcm | OLS, HC1 (Arrow predicts slope +1) | 29 | 0.445 | 2.205 | -3.877 | 4.767 | 0.840 | 0.003 |
| 2022 | cr4 | Spearman rank correlation | 29 | 0.219 |  |  |  | 0.253 |  |
| 2022 | cr4_per10 | OLS, leave-one-industry-out min | 28 | 0.045 |  |  |  |  |  |
| 2022 | cr4_per10 | OLS, leave-one-industry-out max | 28 | 0.129 |  |  |  |  |  |
| 2022 | cr4_per10 | OLS, HC1, without pharma (3254) and semiconductors (3344) | 27 | 0.118 | 0.080 | -0.039 | 0.276 | 0.141 | 0.042 |

### cr4_bands.csv

| cr4_band | year | industries | mean_rd_intensity | median_rd_intensity | pooled_rd_intensity | rd_musd |
|---|---|---|---|---|---|---|
| under 30% | 2017 | 5 | 2.65 | 1.94 | 2.54 | 12,345 |
| 30% to 50% | 2017 | 17 | 4.39 | 2.21 | 4.68 | 132,441 |
| 50% or more | 2017 | 14 | 3.88 | 2.66 | 3.39 | 71,365 |
| under 30% | 2022 | 6 | 2.59 | 2.15 | 2.29 | 21,603 |
| 30% to 50% | 2022 | 14 | 5.78 | 2.72 | 7.29 | 231,225 |
| 50% or more | 2022 | 9 | 5.33 | 3.66 | 4.15 | 55,702 |

### changes_tests.csv

| regressor | method | n | slope | se | ci_low | ci_high | p | r2 |
|---|---|---|---|---|---|---|---|---|
| d_cr4_per10 | OLS, HC1 | 29 | 0.232 | 0.137 | -0.037 | 0.501 | 0.091 | 0.109 |
| d_cr4_per10 | WLS by average R&D, HC1 | 29 | 0.000 | 0.091 | -0.178 | 0.178 | 0.999 | 0.000 |
| d_hhi_per100 | OLS, HC1 | 28 | 0.080 | 0.028 | 0.025 | 0.134 | 0.004 | 0.240 |
| d_cr4_per10 | OLS, HC1, outcome d_ln_rd | 29 | 0.669 | 0.331 | 0.020 | 1.317 | 0.043 | 0.192 |
| d_cr4_per10 | OLS, HC1, outcome d_ln_sales | 29 | 0.437 | 0.327 | -0.205 | 1.078 | 0.182 | 0.108 |
| d_cr4_per10 | OLS, HC1, without missiles, tanks and navigation instruments | 26 | 0.016 | 0.126 | -0.230 | 0.263 | 0.896 | 0.001 |
| d_hhi_per100 | OLS, HC1, without missiles, tanks and navigation instruments | 25 | 0.028 | 0.027 | -0.025 | 0.081 | 0.302 | 0.038 |
| d_cr4 | Spearman rank correlation | 29 | 0.167 |  |  |  | 0.387 |  |
| d_cr4_per10 | OLS, leave-one-industry-out min | 28 | 0.148 |  |  |  |  |  |
| d_cr4_per10 | OLS, leave-one-industry-out max | 28 | 0.278 |  |  |  |  |  |
| group means | mean change in log intensity, CR4 rose | 16 | 0.117 |  |  |  |  |  |
| group means | mean change in log intensity, CR4 fell or unchanged | 13 | 0.023 |  |  |  |  |  |
| group means | difference, CR4 rose minus fell (Welch t-test) | 29 | 0.093 |  |  |  | 0.358 |  |

### changes_industries.csv

| Code | Industry | Leading companies | CR4 2017 | CR4 2022 | ΔCR4 | R&D % 2017 | R&D % 2022 | Δ ln R&D % |
|---|---|---|---|---|---|---|---|---|
| 336411–13 | Aircraft, aircraft engine, and aircraft parts | Boeing, GE Aerospace, RTX | 81.5 | 73.6 | -7.9 | 3.46 | 3.66 | +0.055 |
| 3361–63 | Automobiles, bodies, trailers, and parts | General Motors, Ford, Tesla | 53.4 | 47.9 | -5.5 | 2.79 | 3.29 | +0.163 |
| 3254 | Pharmaceuticals and medicines | Pfizer, Merck, Eli Lilly | 43.0 | 38.0 | -5.0 | 11.84 | 15.27 | +0.254 |
| 312 | Beverage and tobacco products | Altria, Coca-Cola, PepsiCo | 67.2 | 62.9 | -4.3 | 0.64 | 0.49 | -0.264 |
| 323 | Printing and related support activities |  | 16.9 | 14.1 | -2.8 | 0.54 | 0.56 | +0.037 |
| 337 | Furniture and related products |  | 35.1 | 32.7 | -2.4 | 0.96 | 1.06 | +0.098 |
| 334510, 334517 | Electromedical, electrotherapeutic, and irradiation apparatus | GE HealthCare, Medtronic | 38.1 | 35.9 | -2.2 | 11.34 | 11.44 | +0.009 |
| 322 | Paper | International Paper, Smurfit Westrock | 50.8 | 48.9 | -2.0 | 0.77 | 1.02 | +0.272 |
| other 3345 | Other measuring and controlling device |  | 29.1 | 27.4 | -1.7 | 6.27 | 6.46 | +0.029 |
| 3399 | Other miscellaneous manufacturing |  | 27.2 | 26.0 | -1.3 | 2.63 | 2.96 | +0.117 |
| other 333 | Other machinery |  | 31.2 | 29.9 | -1.3 | 2.54 | 2.55 | +0.003 |
| 326 | Plastics and rubber products |  | 26.0 | 25.7 | -0.3 | 1.94 | 1.28 | -0.414 |
| other 336 | Other transportation |  | 55.6 | 55.5 | -0.1 | 2.40 | 2.27 | -0.054 |
| 3391 | Medical equipment and supplies | Medtronic, Stryker, Becton Dickinson | 32.8 | 32.9 | +0.2 | 4.32 | 4.57 | +0.058 |
| 3255, 3259 | Paint, coating, adhesive, and other chemicals |  | 32.8 | 33.1 | +0.4 | 2.21 | 1.78 | -0.216 |
| 332 | Fabricated metal products |  | 22.6 | 23.4 | +0.7 | 1.88 | 1.75 | -0.069 |
| 327 | Nonmetallic mineral products | Owens Corning, Corning | 35.3 | 37.0 | +1.7 | 2.86 | 2.16 | -0.281 |
| 321 | Wood products | Weyerhaeuser, Louisiana-Pacific | 32.4 | 34.2 | +1.8 | 0.62 | 0.42 | -0.392 |
| 3344 | Semiconductor and other electronic components | Intel, Texas Instruments, Micron | 38.5 | 40.6 | +2.1 | 16.20 | 22.60 | +0.333 |
| 335 | Electrical equipment, appliances, and components |  | 45.2 | 48.4 | +3.2 | 3.62 | 3.49 | -0.039 |
| 333242 | Semiconductor machinery | Applied Materials, Lam Research, KLA | 56.9 | 60.7 | +3.8 | 16.09 | 16.39 | +0.019 |
| other 334 | Other computer and electronic products | Apple, Dell, HP | 53.0 | 57.8 | +4.8 | 7.83 | 9.99 | +0.244 |
| 3252 | Resin, synthetic rubber, and artificial synthetic fibers and filaments |  | 30.6 | 35.4 | +4.9 | 1.41 | 1.54 | +0.087 |
| 331 | Primary metals | Nucor, Steel Dynamics, Cleveland-Cliffs | 44.8 | 49.7 | +4.9 | 0.81 | 0.68 | -0.170 |
| 336414–15, 336419 | Guided missile, space vehicle, and related parts | Lockheed Martin, Northrop Grumman | 90.6 | 95.8 | +5.2 | 2.28 | 4.38 | +0.655 |
| 336992 | Military armored vehicle, tank, and tank component | General Dynamics, BAE Systems | 79.6 | 85.1 | +5.5 | 1.24 | 2.02 | +0.485 |
| 3342 | Communications equipment | Cisco, Motorola Solutions | 43.8 | 49.8 | +5.9 | 12.38 | 11.54 | -0.070 |
| 324 | Petroleum and coal products | Marathon, Valero, Phillips 66 | 44.9 | 51.6 | +6.7 | 0.13 | 0.21 | +0.509 |
| 334511 | Search, detection, navigation, guidance, aeronautical, and nautical system and instrument | RTX, L3Harris, Honeywell | 50.4 | 57.9 | +7.5 | 4.20 | 8.58 | +0.715 |
