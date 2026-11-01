# Methods review of Arrow (1962)

**Paper.** Kenneth J. Arrow, "Economic Welfare and the Allocation of Resources for Invention," in Universities-National
Bureau Committee for Economic Research, *The Rate and Direction of Inventive Activity: Economic and Social Factors*,
Princeton University Press for the National Bureau of Economic Research, 1962, pp. 609–626 (with a comment by
C. J. Hitch, pp. 625–626).

**Statistical focus.** The comparison of the incentive to invent a cost-reducing process under competition and under
monopoly (pp. 619–622, including footnote 7), and in particular the result that the ratio of the competitive to the
monopoly incentive is always above one and is approximately $`x_c / x_m`$ for a minor invention. Secondarily, the
claim that a free-enterprise economy underinvests in invention because of risk, inappropriability and indivisibility
(pp. 609–619).

**Review standard.** Internal consistency of the formal results, explicitness of assumptions, and the testability of
the predictions. Because the paper reports no data, the usual empirical checklist (sampling, standard errors, data
availability) is applied only to say what does not apply and why.

**What was read.** The full text of the chapter as scanned by the NBER (chapter c2144, nber.org/chapters/c2144),
including footnotes and Hitch's comment. The scan's text layer has optical character recognition errors in several
equations; where an equation was unclear I relied on its surrounding prose and on the consistency of the algebra, and
I flag those places below.

---

## Methods summary

**Research design.** A welfare-theoretic essay in two parts. The first part (pp. 609–619) argues verbally, from
the theory of competitive equilibrium under uncertainty, that invention is subject to all three classical sources of
market failure: indivisibility, inappropriability and uncertainty. The second part (pp. 619–622) is a formal
partial-equilibrium model comparing the payoff from a cost-reducing invention to an outside inventor who licenses it
to a competitive industry with the payoff to a monopolist protected by entry barriers. The last section (pp. 623–625)
discusses non-market ways of financing research.

**Sampling strategy, sample size, inclusion and exclusion criteria.** Not applicable. There is no sample. The model
has one industry, one inventor and one invention.

**Independent and dependent variables.** In the formal model the exogenous variables are pre-invention unit cost
$`c`$, post-invention unit cost $`c'`$, and the industry demand curve (assumed downward sloping, with downward-sloping
marginal revenue). The outcome is the incentive to invent, defined as the increase in profit (or royalty income) the
invention brings.

**Statistical methods.** None. The results are proved by comparing integrals of the marginal revenue curve and, in
footnote 7, by differentiating the incentive gap and ratio with respect to $`c'`$ and applying L'Hôpital's rule.

**Reported effect sizes, confidence intervals, p-values.** None are reported, and none could be, since there are no
estimates. The "statistics" of the paper are its formal results, listed in the table below.

**Missing data treatment.** Not applicable.

**Stated limitations.** Arrow states several. The appropriability problem is set aside in the formal comparison
("The difficulty of appropriating the information will be ignored," p. 619). Monopoly is defined as barriers to
entry, and a temporary monopoly that does not block new entrants is treated as closer to competition (p. 619). He
notes that the only argument for monopoly's superiority is greater appropriability, which would have to be weighed
against the disincentive he derives (p. 622). In footnote 3 he concedes that the claim that risky activities should
be undertaken whenever expected return exceeds the market rate "depends on some unstated assumptions."

## Statistics extraction table

| Statistic | Value and unit | Source location | What it measures | What it does not establish |
|---|---|---|---|---|
| Competitive inventor's incentive, drastic invention ($`p'_m < c`$) | $`P'`$, the post-invention monopoly profit, in money per period | p. 620 | Royalty income when the inventor can set the royalty so the competitive price equals the post-invention monopoly price | That inventors can in practice set such a royalty; licensing frictions are assumed away |
| Competitive inventor's incentive, non-drastic invention ($`p'_m > c`$) | $`x_c (c - c')`$, money per period | p. 620 | Cost saving on the full competitive output, captured through a royalty of $`c - c'`$ per unit | Anything about invention under imperfect appropriability, which is set aside |
| Monopolist's incentive | $`P' - P`$, money per period | p. 620 | Gain in monopoly profit from the lower cost | Behavior of a monopolist facing a threat of entry, which the model excludes by definition |
| Upper bound on the monopolist's incentive | $`P' - P < (c - c')\, x'_m`$ | p. 621 | Cost saving on the post-invention monopoly output, derived from declining marginal revenue | How large the gap is for any real demand curve |
| Maximum gap between the two incentives | $`P`$, the pre-invention monopoly profit | p. 621 and footnote 7, pp. 621–622 | The "replacement" of existing profit, reached for drastic inventions | That monopolists invest less in absolute amounts in any actual industry |
| Ratio of competitive to monopoly incentive | Always greater than 1; decreasing as $`c'`$ falls; approximately $`x_c / x_m`$ for minor inventions | p. 621 and footnote 7, p. 622 | Relative incentive, which for small cost reductions equals the ratio of competitive to monopoly output | A numerical value; for linear demand the ratio is 2, but that case is not worked in the paper |
| Realized social benefit versus competitive incentive | Realized social benefit $`\ge`$ competitive incentive, equal for non-drastic inventions | p. 622 | Inventor captures all realized benefit of moderate inventions but not of radical ones, suggesting a bias against major inventions | The size of underinvestment, or the potential (first-best) benefit, which is larger still |
| Sources of underinvestment | Three: risk, limited appropriability, increasing returns in use | p. 619 | Qualitative direction of the market failure, stronger for basic research | Magnitude; Arrow points to Griliches (1958) on hybrid corn as the kind of rate-of-return study that could measure it (p. 623, footnote 8) |
| Cost of developing a new military aircraft or missile (Hitch's comment) | $0.5 billion to $2.0 billion | p. 625 | Hitch's figure for why the Air Force moved competition to the design stage | It is not Arrow's figure and no source is given |

## Interpretation notes

- The formal result is a comparison of incentives, not of investment levels. It shows the monopolist's private gain
  from a given invention is smaller. Turning this into a prediction about R&D spending requires added assumptions
  about the cost of invention and about how many inventions are available, which the paper does not supply.
- "Monopoly" in the paper means barriers to entry, and "competition" means a competitive industry plus an outside
  inventor with full royalty power. Empirical tests that equate monopoly with high concentration and competition with
  low concentration substitute a structural proxy for the paper's institutional definition.
- The paper treats only process (cost-reducing) inventions formally. It remarks that the product case is "not very
  different" (p. 619) without a derivation.
- The result is conditional on the monopolist not facing an entrant who could obtain the invention. Gilbert and
  Newbery (1982, *American Economic Review* 72(3): 514–526) show that when an entrant could win the invention, the
  incumbent's incentive can exceed the entrant's. Reinganum (1983, *American Economic Review* 73(4): 741–748) shows
  that with uncertain invention the incumbent can again invest less. These are extensions under different
  assumptions, not corrections of Arrow's algebra.
- A reporting slip in the text: p. 621 states that for minor inventions the ratio is approximately $`x_c / x_m`$,
  "i.e., the ratio of monopoly to competitive output." The symbols give competitive to monopoly output, and footnote 7
  confirms $`x_c / x'_m`$. The words appear reversed. The algebra is not affected.
- The sentence on p. 621 that the ratio "decreases steadily with c'" is ambiguous on its own; footnote 7 makes clear
  that the ratio falls as $`c'`$ falls, so larger inventions bring the two incentives closer in ratio while the
  absolute gap grows.

## Unanswered questions

- How large is the gap for plausible demand curves? The paper gives no worked example or calibration.
- Does the result survive when the competitive inventor cannot set an arbitrary royalty, for example when the
  invention is imitated or when patents are narrow? Arrow sets appropriability aside for the formal comparison.
- How should the model be read for industries between the two extremes, oligopolies with some entry barriers, which
  is where most real industries sit?
- How does the replacement effect interact with the size of firms' research programs? Arrow's own first part argues
  that large firms with many projects can act as their own insurers (p. 616), which pushes in the opposite direction.

## Items requiring expert verification

- The equations on pp. 620–622 are partly unreadable in the scanned text layer (for example the integral expression
  for $`P' - P`$ and the derivative formulas in footnote 7). The reconstruction used here, the standard one in later
  textbook treatments, should be checked against a clean print copy.
- Whether the volume should be cited with Richard R. Nelson as editor. The NBER book page credits the
  Universities-National Bureau Committee for Economic Research and the Committee on Economic Growth of the Social
  Science Research Council, with Nelson writing the introduction; many later citations list Nelson as editor.
- Arrow's affiliation is printed as The RAND Corporation. He spent most of his career at Stanford, and a historian
  of the period would be better placed to say how his appointments were arranged in 1960–62.

## How the modern rerun relates

The rerun in this repository does not reproduce anything in the paper, because the paper has no data. It tests
two predictions that later writers drew from Arrow's comparison, using public US data for 2017 and 2022. The
results are summarized in [results/FINDINGS.md](results/FINDINGS.md).
