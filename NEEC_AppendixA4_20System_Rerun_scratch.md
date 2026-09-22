# NEEC Appendix A.4: Full Re-Run for the 20-System, 26-Criterion Corpus

**SCRATCH DRAFT — Session 20.** Not yet inserted into the Paper. Paper
v1.4's published Appendix A.4 covers 15 systems (Session 12's re-run,
inserted in Session 13). This draft extends the same check to the
20-system corpus that became canonical in this session's insertion pass,
for use in the Step 5 (expanded) regeneration that produces Paper v2.0. It
follows the structure of Session 12's scratch document
(`NEEC_AppendixA4_Full_Rerun_scratch.md`).

**Method.** No weighting scheme is changed and no score is re-derived.
`run_a4_full_rerun_20.py` imports the scores, the four schemes, and the
helper functions from the unmodified canonical
`neec_weighting_robustness_analysis_v2.py`, and requires both of that
script's self-checks to pass first. Session 12 had to skip the
legacy-unchanged check because `baseline_weighting_script.py` was missing
at the time; the reconstructed file is now on the mount, so this run
includes it. No count is written into the script's logic: corpus size,
ties, and dominance pairs are all computed, so the script can be re-run
unchanged after the next insertion. All 19 of its checks pass, and its
captured output (`a4_rerun_20_raw_output.txt`) reproduces byte for byte
from any directory. Every table below was pasted from that output by a
script, not retyped.

**Two presentation conventions, new in this draft (proposed for Paper
v2.0).** First, rank positions stay ordinal, as in v1.4, but a position
whose weighted total equals another system's under the same scheme is now
marked "=", because the order inside a tie is only the canonical listing
order. The v1.4 table left such ties unmarked; for example, Market
Socialism and MMT + Job Guarantee both score 61.7% under Crisis-Risk.
Second, rank movements are computed with competition ranks (tied systems
share the better position), so a tie never produces an artificial
movement.

---

## Recap: the three alternative schemes (unchanged)

Each alternative multiplies one set of criteria K by a factor k and leaves
every other criterion at 1; the script checks that this holds.

- **Material-Security-Weighted:** K = Domain 1 (six criteria), k = 2;
  maximum 32.0.
- **Feasibility-Discounted:** K = Domain 5, k = 0.5; maximum 23.5.
- **Crisis-Risk-Weighted:** K = {C1.4, C4.2}, k = 3; maximum 30.0.

## What cannot change, by construction (reconfirmed, and now tested exhaustively)

1. **Adequacy tiers** depend only on which criteria score exactly 0.0, so
   no weighting can move them (table at the end).
2. **Formal dominance** survives any positive weighting (Theorem 5,
   Appendix A.2). Earlier runs illustrated this on a few spot-checked
   pairs. This run checks every strict-dominance pair in the corpus (all
   11) under all four schemes, and each keeps a strictly higher weighted
   total.

## A tool for reading the results: the single-factor identity

Because each alternative is single-factor, a system's weighted total is
its equal-weighted total plus (k − 1) times its sum over K. For two
systems a and b, with D the difference of their equal-weighted totals and
D_K the difference of their sums over K:

> weighted(a) − weighted(b) = D + (k − 1) · D_K

This is elementary algebra, not a new result, and the script confirms it
for all 400 ordered pairs under all three schemes. It explains every
movement below. In particular, a pair tied under equal weighting (D = 0)
stays tied under a scheme exactly when D_K = 0. Otherwise the tie breaks
toward the system that is stronger on K when k > 1 (Material-Security,
Crisis-Risk), and toward the system that is weaker on K when k < 1
(Feasibility-Discounted).

## Full ranking under each scheme, all 20 systems

| System | Equal | Material-Security x2 | Feasibility-Discounted x0.5 | Crisis-Risk x3 | Failures | Tier |
|---|---|---|---|---|---|---|
| CCO-PTF-CIP-SZH | 1 (94.2%) | 1 (93.8%) | 1 (94.7%) | 1 (95.0%) | 0 | Potentially Adequate |
| Participatory Economics | 2 (78.8%) | 2 (79.7%) | 2 (80.9%) | 2 (81.7%) | 1 | Potentially Adequate |
| Nordic Social Democracy | 3= (75.0%) | 3 (76.6%) | 5 (74.5%) | 5 (71.7%) | 2 | Potentially Adequate |
| Integral | 4= (75.0%) | 5 (70.3%) | 3 (77.7%) | 3 (75.0%) | 3 | Partially Adequate |
| Degrowth Economics | 5 (73.1%) | 4 (73.4%) | 4 (76.6%) | 4 (73.3%) | 2 | Potentially Adequate |
| Market Socialism | 6 (63.5%) | 6 (64.1%) | 6 (63.8%) | 6= (61.7%) | 2 | Potentially Adequate |
| MMT + Job Guarantee | 7 (59.6%) | 7 (59.4%) | 7 (59.6%) | 7= (61.7%) | 3 | Partially Adequate |
| Universal Basic Income | 8= (55.8%) | 9 (53.1%) | 8 (55.3%) | 8 (58.3%) | 7 | Structurally Inadequate |
| Mutual Credit / LETS | 9= (55.8%) | 10= (51.6%) | 10 (53.2%) | 10 (55.0%) | 3 | Partially Adequate |
| Sovereign Wealth Fund Statism | 10= (53.8%) | 11= (51.6%) | 11= (52.1%) | 13= (50.0%) | 3 | Partially Adequate |
| State Capitalism / Singapore | 11= (53.8%) | 8 (56.2%) | 12= (52.1%) | 14= (50.0%) | 4 | Partially Adequate |
| Georgism / Land Value Tax | 12= (51.9%) | 13 (48.4%) | 13 (51.1%) | 11= (51.7%) | 2 | Potentially Adequate |
| Universal Basic Services | 13= (51.9%) | 14 (46.9%) | 14 (50.0%) | 12= (51.7%) | 3 | Partially Adequate |
| Fully Automated Luxury Communism | 14 (50.0%) | 12 (50.0%) | 9 (54.3%) | 9 (56.7%) | 10 | Structurally Inadequate |
| Doughnut Economics | 15 (44.2%) | 18= (39.1%) | 15 (42.6%) | 15 (45.0%) | 8 | Structurally Inadequate |
| Status Quo Market Capitalism | 16 (40.4%) | 17= (39.1%) | 18= (36.2%) | 18 (35.0%) | 9 | Structurally Inadequate |
| Centrally Planned Socialism | 17= (38.5%) | 15= (40.6%) | 16 (40.4%) | 16 (40.0%) | 12 | Structurally Inadequate |
| Stakeholder Capitalism | 18= (38.5%) | 19 (37.5%) | 17 (37.2%) | 19 (33.3%) | 9 | Structurally Inadequate |
| State Capitalism / China | 19= (38.5%) | 16= (40.6%) | 19= (36.2%) | 17 (36.7%) | 8 | Structurally Inadequate |
| Libertarian Minarchism | 20 (30.8%) | 20 (25.0%) | 20 (27.7%) | 20 (26.7%) | 15 | Structurally Inadequate |

*Ranked by equal-weighted position. "=" marks a weighted total shared with
another system under that scheme. Percentages are each system's weighted
total divided by that scheme's maximum (26.0, 32.0, 23.5, and 30.0), so
they compare within a column, not across columns. The Failures and Tier
columns are the same under every scheme.*

## What moves, and what it means

**The top two and the bottom hold.** CCO-PTF-CIP-SZH and Participatory
Economics hold positions 1 and 2 under all four schemes, and Libertarian
Minarchism is last under all four, as in the 13- and 15-system checks.

**Nordic Social Democracy and Integral: unchanged from Session 12.** Tied
at 75.0% under equal weighting, Nordic leads under Material-Security
(76.6% vs. 70.3%), and Integral leads under Feasibility-Discounted (77.7%
vs. 74.5%) and Crisis-Risk (75.0% vs. 71.7%). Their percentages are
unchanged, and because none of the five systems inserted since Session 12
ranks above either of them under any scheme, so are their positions.

**Fully Automated Luxury Communism: the same caution, a larger number.**
FALC moves from equal-weighted position 14 to position 9 under both
Feasibility-Discounted and Crisis-Risk, where the 15-system run had 11 to
9. Its weighted percentages are unchanged (54.3% and 56.7%). The larger
movement comes from three newly inserted systems (Universal Basic
Services, Sovereign Wealth Fund Statism, and Singapore) that score above
FALC under equal weighting and below it under both schemes. The reasons
are also unchanged: Feasibility-Discounting relieves FALC's corpus-worst
Domain 5 (0.5/5), and Crisis-Risk triples two criteria FALC passes (C1.4
and C4.2). FALC keeps its 10 failures, and its tier, under every scheme.
As Session 12 put it, a rank rise for a system with 10 structural
failures shows which criteria a scheme emphasizes, not that the system is
adequate.

**The Sovereign Wealth Fund Statism / Singapore tie is the most
weighting-robust tie in the corpus.** Both systems score 14.0/26. The tie
survives Feasibility-Discounted, because their Domain 5 totals are equal
(3.5 each), and Crisis-Risk, because they score identically on C1.4 (0.5)
and C4.2 (0.0). It breaks only under Material-Security, where Singapore's
Domain 1 (4.0/6, against 2.5/6) puts it ahead, 18.00 to 16.50 (56.2% to
51.6%), and lifts Singapore from position 10 to 8. The corpus's other
ties behave differently. Session 12 found that the Universal Basic Income
/ Mutual Credit-LETS tie dissolves under all three alternatives, with UBI
ahead each time. The Georgism / Universal Basic Services tie (visible in
the Session 16 script output but not previously written up) breaks toward
Georgism under Material-Security and Feasibility-Discounted and survives
Crisis-Risk. Both SWF Statism and Singapore fall three positions under
Crisis-Risk (10 to 13) because both fail C4.2, the ecological criterion
that scheme triples; their shared tier (Partially Adequate) does not
move.

**The three-way tie at 10.0 separates under two schemes, in different
orders.** Centrally Planned Socialism and China have the same Domain 1
total (3.0), so their tie survives Material-Security, while Stakeholder
Capitalism (Domain 1: 2.0) falls behind both. Under
Feasibility-Discounted the three separate as Centrally Planned Socialism
(9.50), Stakeholder Capitalism (8.75), and China (8.50): halving Domain 5
costs China the most, because Domain 5 (3.0/5) is where China most
exceeds the other two. Under Crisis-Risk the order is Centrally Planned
Socialism (12.00), China (11.00), and Stakeholder Capitalism (10.00). The
order of China and Stakeholder Capitalism therefore depends entirely on
the scheme. All three remain Structurally Inadequate under every scheme,
with 12, 8, and 9 failures respectively.

**Four new scheme-specific ties.** Four pairs that differ under equal
weighting tie under one alternative: Status Quo Market Capitalism and
Doughnut Economics (39.1%), and Mutual Credit/LETS and SWF Statism
(51.6%), under Material-Security; Status Quo Market Capitalism and China
(36.2%) under Feasibility-Discounted; and Market Socialism and MMT + Job
Guarantee (61.7%) under Crisis-Risk. The last was already present, but
unmarked, in the 15-system table.

**Everything else moves by at most three positions, and nothing leaves
its tier.** Apart from FALC, the largest movements are SWF Statism and
Singapore under Crisis-Risk (above); every other system moves by at most
two positions under any scheme. Section 3 of the raw output lists every
movement.

## Dominance-pair spot check, extended, with one correction to Paper v1.4

| Pair | Dominance | Equal | Material-Security x2 | Feasibility-Discounted x0.5 | Crisis-Risk x3 |
|---|---|---|---|---|---|
| CCO-PTF-CIP-SZH vs. Status Quo Market Capitalism | **True** (guaranteed) | 24.50 > 10.50 | 30.00 > 12.50 | 22.25 > 8.50 | 28.50 > 10.50 |
| CCO-PTF-CIP-SZH vs. MMT + Job Guarantee | **True** (guaranteed) | 24.50 > 15.50 | 30.00 > 19.00 | 22.25 > 14.00 | 28.50 > 18.50 |
| CCO-PTF-CIP-SZH vs. Georgism / Land Value Tax | **True** (guaranteed) | 24.50 > 13.50 | 30.00 > 15.50 | 22.25 > 12.00 | 28.50 > 15.50 |
| Participatory Economics vs. Stakeholder Capitalism | False (non-dominated) | 20.50 > 10.00 | 25.50 > 12.00 | 19.00 > 8.75 | 24.50 > 10.00 |
| CCO-PTF-CIP-SZH vs. Nordic Social Democracy | False (non-dominated) | 24.50 > 19.50 | 30.00 > 24.50 | 22.25 > 17.50 | 28.50 > 21.50 |
| Mutual Credit / LETS vs. Georgism / Land Value Tax | False (non-dominated) | 14.50 > 13.50 | 16.50 > 15.50 | 12.50 > 12.00 | 16.50 > 15.50 |
| CCO-PTF-CIP-SZH vs. Doughnut Economics | **True** (guaranteed) | 24.50 > 11.50 | 30.00 > 12.50 | 22.25 > 10.00 | 28.50 > 13.50 |
| CCO-PTF-CIP-SZH vs. Universal Basic Services | **True** (guaranteed) | 24.50 > 13.50 | 30.00 > 15.00 | 22.25 > 11.75 | 28.50 > 15.50 |
| CCO-PTF-CIP-SZH vs. Sovereign Wealth Fund Statism | **True** (guaranteed) | 24.50 > 14.00 | 30.00 > 16.50 | 22.25 > 12.25 | 28.50 > 15.00 |
| CCO-PTF-CIP-SZH vs. State Capitalism / China | **True** (guaranteed) | 24.50 > 10.00 | 30.00 > 13.00 | 22.25 > 8.50 | 28.50 > 11.00 |
| CCO-PTF-CIP-SZH vs. State Capitalism / Singapore | **True** (guaranteed) | 24.50 > 14.00 | 30.00 > 18.00 | 22.25 > 12.25 | 28.50 > 15.00 |
| State Capitalism / Singapore vs. State Capitalism / China | **True** (guaranteed) | 14.00 > 10.00 | 18.00 > 13.00 | 12.25 > 8.50 | 15.00 > 11.00 |
| State Capitalism / Singapore vs. Sovereign Wealth Fund Statism | False (tie) | 14.00 = 14.00 | 18.00 > 16.50 | 12.25 = 12.25 | 15.00 = 15.00 |
| Universal Basic Services vs. Georgism / Land Value Tax | False (tie) | 13.50 = 13.50 | 15.00 < 15.50 | 11.75 < 12.00 | 15.50 = 15.50 |

**Correction to Paper v1.4 (a correction, not polish).** Paper v1.4's
Appendix A.4 table labels "Participatory Economics vs. Stakeholder
Capitalism" as **True** (guaranteed). It is not a dominance pair:
Stakeholder Capitalism outscores Participatory Economics on C4.5 (0.5 vs.
0.0), C5.2 (1.0 vs. 0.5), and C5.3 (1.0 vs. 0.5). The canonical script
has always printed "strict formal dominance: False" for this pair,
including in Session 12's raw output and in the transcript that Paper
v1.4's own Appendix L reproduces. The error therefore entered when
Session 12's scratch table was transcribed, and Session 13 carried it
into the Paper. The row's weighted comparisons are correct (Participatory
Economics leads under all four schemes), so only the label changes, but
the v1.4 prose around the table, which speaks of "the two False rows,"
needs the same fix: three of its six rows are non-dominated. No other
v1.4 label disagrees with the computation.

**The new rows.** CCO-PTF-CIP-SZH dominates all five systems inserted
since Session 12's run (Doughnut Economics, Universal Basic Services, SWF
Statism, China, and Singapore), and Singapore dominates China: six
further guaranteed pairs, each confirmed. The two tie rows are
non-dominated by construction and are included to show how each tie
behaves.

**An observation about the dominance structure (flagged; no score is
affected).** Of the 11 strict-dominance relations in the 20-system corpus,
10 run from CCO-PTF-CIP-SZH, and Singapore over China is the only one that
does not involve it (`verify_insertion_s20.py` checks this). Before this
session's insertion, all 7 relations ran from CCO-PTF-CIP-SZH. Because
CCO-PTF-CIP-SZH is the lead author's own framework, nearly all of the
corpus's formal dominance findings rest on one self-scored vector. The
Paper's self-referential-bias disclosure (Section 10.5) already names this
kind of risk; the observation strengthens the case for an independent
second-scorer replication of that system's vector (Appendix H.9, Step 6).

## Every equal-weighting tie, and how it behaves

| Tied pair (equal-weighted total) | Material-Security x2 | Feasibility-Discounted x0.5 | Crisis-Risk x3 |
|---|---|---|---|
| Nordic Social Democracy vs. Integral (19.5) | Nordic Social Democracy ahead (24.50 vs 22.50); D_K = +2.0 | Integral ahead (18.25 vs 17.50); D_K = +1.5 | Integral ahead (22.50 vs 21.50); D_K = -0.5 |
| Centrally Planned Socialism vs. Stakeholder Capitalism (10.0) | Centrally Planned Socialism ahead (13.00 vs 12.00); D_K = +1.0 | Centrally Planned Socialism ahead (9.50 vs 8.75); D_K = -1.5 | Centrally Planned Socialism ahead (12.00 vs 10.00); D_K = +1.0 |
| Centrally Planned Socialism vs. State Capitalism / China (10.0) | tie holds (13.00); D_K = 0 | Centrally Planned Socialism ahead (9.50 vs 8.50); D_K = -2.0 | Centrally Planned Socialism ahead (12.00 vs 11.00); D_K = +0.5 |
| Universal Basic Income vs. Mutual Credit / LETS (14.5) | Universal Basic Income ahead (17.00 vs 16.50); D_K = +0.5 | Universal Basic Income ahead (13.00 vs 12.50); D_K = -1.0 | Universal Basic Income ahead (17.50 vs 16.50); D_K = +0.5 |
| Stakeholder Capitalism vs. State Capitalism / China (10.0) | State Capitalism / China ahead (13.00 vs 12.00); D_K = -1.0 | Stakeholder Capitalism ahead (8.75 vs 8.50); D_K = -0.5 | State Capitalism / China ahead (11.00 vs 10.00); D_K = -0.5 |
| Georgism / Land Value Tax vs. Universal Basic Services (13.5) | Georgism / Land Value Tax ahead (15.50 vs 15.00); D_K = +0.5 | Georgism / Land Value Tax ahead (12.00 vs 11.75); D_K = -0.5 | tie holds (15.50); D_K = 0 |
| Sovereign Wealth Fund Statism vs. State Capitalism / Singapore (14.0) | State Capitalism / Singapore ahead (18.00 vs 16.50); D_K = -1.5 | tie holds (12.25); D_K = 0 | tie holds (15.00); D_K = 0 |

*D_K is the first-named system's sum over the scheme's weighted criteria
minus the second's. A tie survives exactly when D_K = 0.*

## Adequacy tier, all 20 systems (illustrative, not a test)

| System | Failures | Tier (invariant across all four schemes) |
|---|---|---|
| CCO-PTF-CIP-SZH | 0 | Potentially Adequate |
| Participatory Economics | 1 | Potentially Adequate |
| Nordic Social Democracy | 2 | Potentially Adequate |
| Market Socialism | 2 | Potentially Adequate |
| Degrowth Economics | 2 | Potentially Adequate |
| Georgism / Land Value Tax | 2 | Potentially Adequate |
| MMT + Job Guarantee | 3 | Partially Adequate |
| Integral | 3 | Partially Adequate |
| Mutual Credit / LETS | 3 | Partially Adequate |
| Universal Basic Services | 3 | Partially Adequate |
| Sovereign Wealth Fund Statism | 3 | Partially Adequate |
| State Capitalism / Singapore | 4 | Partially Adequate |
| Universal Basic Income | 7 | Structurally Inadequate |
| Doughnut Economics | 8 | Structurally Inadequate |
| State Capitalism / China | 8 | Structurally Inadequate |
| Status Quo Market Capitalism | 9 | Structurally Inadequate |
| Stakeholder Capitalism | 9 | Structurally Inadequate |
| Fully Automated Luxury Communism | 10 | Structurally Inadequate |
| Centrally Planned Socialism | 12 | Structurally Inadequate |
| Libertarian Minarchism | 15 | Structurally Inadequate |

Tier counts: 6 Potentially Adequate, 6 Partially Adequate, 8 Structurally
Inadequate.

## Conclusion

The conclusion of Section 10.9 and the published Appendix A.4 holds for 20
systems as it did for 13 and 15. Weighting changes the order among
roughly comparable, non-dominating systems: most visibly Nordic and
Integral, FALC's scheme-specific rise, and the direction in which each
equal-weighting tie breaks. It cannot change adequacy tiers or any
dominance relation, and this run confirms that for every relation the
corpus contains. The new systems add one qualification worth stating:
whether an equal-weighting tie survives an alternative scheme can be read
in advance from a single number per scheme (D_K), and the SWF Statism /
Singapore tie survives two of the three.

## Proposed for Paper v2.0 (decisions for the user)

1. Replace Appendix A.4's 15-system tables with these 20-system tables,
   or with the final corpus's if the Gulf, Islamic finance, and Ostrom
   entries are inserted first (the script needs no change).
2. Correct the Participatory Economics / Stakeholder Capitalism label and
   the "two False rows" wording.
3. Adopt the "=" tie marker and competition-rank movements.
4. Optionally add the single-factor identity as a short explanatory
   paragraph.
5. Decide whether the dominance-structure observation belongs in Section
   10.5 (self-referential bias), Section 11.3 (dominance), or both.

## Verification

- `run_a4_full_rerun_20.py`: 19/19 checks pass; captured output
  `a4_rerun_20_raw_output.txt`.
- `verify_insertion_s20.py`: confirms the canonical corpus these figures
  were computed from, including the dominance-structure observation.
- `run_all_checks.py`: re-runs both and compares each against its captured
  output.
