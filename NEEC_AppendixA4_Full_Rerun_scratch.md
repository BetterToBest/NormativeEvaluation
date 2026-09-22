# NEEC Appendix A.4: Full Re-Run for the 15-System, 26-Criterion Corpus

**SCRATCH DRAFT — Session 12.** Not yet inserted into `NEEC_Paper_v1_3.md`.
Per the project's scratch-before-insert discipline, this sits for review
before folding into Appendix A.4 proper. This is the item Paper Section
12.5 explicitly flagged as outstanding ("a full re-run of Appendix A.4...
recomputing every system's weighted total and rank position under all
three schemes on the 26-criterion basis remains a candidate for a future
revision") and Session 11's own handoff listed as Remaining Scope item 2.

**Method, stated plainly.** No new weighting scheme is proposed and no
score is re-derived. This document runs the three named alternative
schemes Appendix A.4 already defines (Material-Security-Weighted,
Feasibility-Discounted, Crisis-Risk-Weighted), unchanged, against the
complete 15-system corpus already canonical in `neec_scores.csv` /
`neec_weighting_robustness_analysis_v2.py` — the same computation that
script's own `run_full_report()` function already assembles, driven here
via a standalone script (`run_a4_full_rerun.py`, included with this
draft) so the output could be captured and written up without depending
on the currently-missing `baseline_weighting_script.py` (see the
Verification section below for how that dependency was avoided, and
Appendix Note at the end of this document for a related finding).

---

## Recap: what the three schemes represent (unchanged from existing Appendix A.4)

- **Material-Security-Weighted** (Domain 1 criteria ×2, all others ×1):
  material security as prerequisite to everything else NEEC measures.
- **Feasibility-Discounted** (Domain 5 criteria ×0.5, all others ×1):
  theoretical/normative adequacy (Domains 1-4) should dominate the
  assessment, buildability secondary.
- **Crisis-Risk-Weighted** (C1.4 Automation Resilience and C4.2
  Ecological Compliance ×3, all others ×1): these two — already NEEC's
  most historically-discussed discriminating criteria — represent the
  most consequential near-term structural risks.

D1_CRITS now has 6 members (C1.1, C1.2a, C1.2b, C1.3, C1.4, C1.5) rather
than 5, so Material-Security-Weighted's own maximum grows from 30.0 to
32.0 accordingly — this is the correct, intended behavior (doubling a
now-6-criterion domain weights more total points than doubling a
5-criterion one), not a bug, exactly as the v2 script's own comments
already note.

## What still can't change, by construction (reconfirmed, not re-tested)

Two of NEEC's three primary comparative tools remain mathematically
invariant to any positive reweighting for the full 15-system corpus, for
the identical reasons Appendix A.4 already states for the 13-system one:

1. **Adequacy tier membership** depends only on which criteria score
   exactly 0.0 — a fact about raw, unweighted scores no weighting scheme
   touches. All 15 systems' tier assignments below are identical under
   all four schemes, because they must be. This is illustrated, not
   tested, by the table in the next section.
2. **Formal dominance relations** are also weight-independent by
   Appendix A.2's own Theorem 5, which already covers *any* positive
   weights, not just the four specifically named here. Every dominance
   claim already published in Section 11.3 is guaranteed to survive
   every scheme below and any other positive reweighting whatsoever.

## Full ranking under each scheme, all 15 systems

| System | Equal (baseline) | Material-Security ×2 | Feasibility-Discounted ×0.5 | Crisis-Risk ×3 |
|---|---|---|---|---|
| CCO-PTF-CIP-SZH | 1 (94.2%) | 1 (93.8%) | 1 (94.7%) | 1 (95.0%) |
| Participatory Economics | 2 (78.8%) | 2 (79.7%) | 2 (80.9%) | 2 (81.7%) |
| Nordic Social Democracy | 3 (75.0%) | 3 (76.6%) | 5 (74.5%) | 5 (71.7%) |
| Integral | 4 (75.0%) | 5 (70.3%) | 3 (77.7%) | 3 (75.0%) |
| Degrowth Economics | 5 (73.1%) | 4 (73.4%) | 4 (76.6%) | 4 (73.3%) |
| Market Socialism | 6 (63.5%) | 6 (64.1%) | 6 (63.8%) | 6 (61.7%) |
| MMT + Job Guarantee | 7 (59.6%) | 7 (59.4%) | 7 (59.6%) | 7 (61.7%) |
| Universal Basic Income | 8 (55.8%) | 8 (53.1%) | 8 (55.3%) | 8 (58.3%) |
| Mutual Credit / LETS | 9 (55.8%) | 9 (51.6%) | 10 (53.2%) | 10 (55.0%) |
| Georgism / Land Value Tax | 10 (51.9%) | 11 (48.4%) | 11 (51.1%) | 11 (51.7%) |
| Fully Automated Luxury Communism | 11 (50.0%) | 10 (50.0%) | 9 (54.3%) | 9 (56.7%) |
| Status Quo Market Capitalism | 12 (40.4%) | 13 (39.1%) | 14 (36.2%) | 13 (35.0%) |
| Centrally Planned Socialism | 13 (38.5%) | 12 (40.6%) | 12 (40.4%) | 12 (40.0%) |
| Stakeholder Capitalism | 14 (38.5%) | 14 (37.5%) | 13 (37.2%) | 14 (33.3%) |
| Libertarian Minarchism | 15 (30.8%) | 15 (25.0%) | 15 (27.7%) | 15 (26.7%) |

*Ranked by equal-weighted position. Percentages are each system's
weighted total ÷ that scheme's own maximum possible (26.0 / 32.0 / 23.5 /
30.0 respectively) — not comparable in absolute value across columns,
only in rank order within a column.*

## What moves, and what it means

**CCO-PTF-CIP-SZH and Participatory Economics hold ranks 1 and 2 under
all four schemes**, exactly as they did in the original 13-system
check — now confirmed to generalize to the full 15-system corpus rather
than being an artifact of the smaller set. Both retain a wide enough gap
over the next-ranked system under every scheme tested that none of the
three alternative weightings comes close to closing it.

**The Nordic/Integral swap, now with exact figures.** Section 12.5
reported this spot-check only directionally ("both...still place Integral
ahead of Nordic"). The full re-run gives the precise numbers: Nordic
leads under Material-Security-Weighted (76.6% vs. 70.3%) — Nordic's
proven, multi-decade wealth-building infrastructure (C1.2a=1.0) pulls
ahead when Domain 1 is doubled, while Integral's own C1.2a=0.0 costs it
proportionally more under this scheme than under equal weighting.
Integral leads under both Feasibility-Discounted (77.7% vs. 74.5%) and
Crisis-Risk-Weighted (75.0% vs. 71.7%) — discounting Domain 5 removes
most of Nordic's implementation-proof advantage directly, and tripling
C4.2 rewards Integral's full ecological-compliance Pass against Nordic's
own Partial. This is unchanged in kind from the pre-retrofit finding
(Section 12.5); this pass supplies the numbers rather than a new
direction.

**A genuinely new finding: Fully Automated Luxury Communism is the
second-largest mover, in the same two schemes, for an unrelated
reason — and it is a caution, not an endorsement.** FALC rises from
equal-rank 11 to rank 9 under both Feasibility-Discounted and
Crisis-Risk-Weighted. FALC's own Domain 5 score (0.5/5, the single worst
Implementation Viability score in the corpus) is exactly what
Feasibility-Discounting relieves it of; and FALC scores a full 1.0 Pass
on *both* of the criteria Crisis-Risk-Weighting triples (C1.4, C4.2) —
a real, if narrow, alignment between FALC's specific strengths and
exactly what these two schemes reward. FALC remains Structurally
Inadequate (10 failures) under every scheme, since tier membership
cannot move — this is precisely the "formal rank movement is not the
same as merit" caution Section 11.3 already states for dominance and
applies here just as directly to scalar rank: a 2-position rise for a
system with 10 structural failures says something about which two
criteria a scheme happens to emphasize, not about the system's overall
adequacy.

**A second genuinely new finding: the Universal Basic Income / Mutual
Credit-LETS percentage tie is specific to equal weighting and dissolves
under every alternative scheme tested — while the tier gap it sits
beside never does.** Both score exactly 14.5/26 (55.8%) under equal
weighting, landing on opposite sides of the Structurally-Inadequate/
Partially-Adequate boundary (7 failures vs. 3) — already flagged
repeatedly (Report Part II; Paper Section 11.1) as one of the corpus's
sharpest illustrations of tier-vs-percentage divergence. This pass adds
a specific, previously unstated qualifier: the *percentage* half of that
illustration is itself a feature of equal weighting specifically. Under
Material-Security-Weighted, UBI (53.1%) pulls ahead of Mutual Credit/LETS
(51.6%); under Feasibility-Discounted, 55.3% vs. 53.2%; under
Crisis-Risk-Weighted, 58.3% vs. 55.0% — UBI leads under all three
alternatives, driven mainly by UBI's own C1.4=1.0 (a full automation-
resilience Pass) against Mutual Credit/LETS's C1.4=0.5, which every
scheme other than equal weighting rewards more heavily one way or
another (directly under Crisis-Risk-Weighted; indirectly under the other
two, since UBI's Domain 1 profile is otherwise stronger). The tier gap
between the two — the actually load-bearing part of the finding, per
Section 10.3's own argument for why NEEC treats percentage as its least
important comparative tool — does not move, because it cannot.
Georgism / Land Value Tax shows the same qualitative pattern one rank
below Mutual Credit/LETS under every scheme: its own equal-weighted
51.9% (rank 10) falls to a consistent rank 11 under all three
alternatives, without ever threatening its Potentially Adequate tier
membership (2 failures throughout).

**Everything else moves by at most one or two rank positions**, and stays
within the same adequacy tier its occupant already belonged to — the
same pattern the pre-retrofit check found, now confirmed across a wider
corpus that includes two systems (Georgism, Mutual Credit/LETS) added
after Appendix A.4 was first written and one (Integral) whose full
criterion-level vector wasn't available until the retrofit supplied it.

## Dominance-pair spot check, extended for the 15-system corpus

As before, this table is **confirmatory for genuine dominance pairs
only** — Theorem 5 already proves the weighted-total inequality holds
for *any* positive weighting wherever strict dominance holds, so a pair
marked `strict formal dominance: True` below could not have come out any
other way without contradicting an already-proven theorem. Pairs marked
`False` are non-dominated; their weighted-total comparison is a genuine,
unguaranteed empirical observation, included for context, not as a
second dominance test.

| Pair | Dominance | Equal | Material-Security ×2 | Feasibility-Disc. ×0.5 | Crisis-Risk ×3 |
|---|---|---|---|---|---|
| CCO-PTF vs. Status Quo Capitalism | **True** (guaranteed) | 24.50 > 10.50 | 30.00 > 12.50 | 22.25 > 8.50 | 28.50 > 10.50 |
| CCO-PTF vs. MMT + Job Guarantee | **True** (guaranteed) | 24.50 > 15.50 | 30.00 > 19.00 | 22.25 > 14.00 | 28.50 > 18.50 |
| CCO-PTF vs. Georgism / LVT | **True** (guaranteed) | 24.50 > 13.50 | 30.00 > 15.50 | 22.25 > 12.00 | 28.50 > 15.50 |
| Participatory Econ vs. Stakeholder Cap. | **True** (guaranteed) | 20.50 > 10.00 | 25.50 > 12.00 | 19.00 > 8.75 | 24.50 > 10.00 |
| CCO-PTF vs. Nordic Social Democracy | False (non-dominated) | 24.50 > 19.50 | 30.00 > 24.50 | 22.25 > 17.50 | 28.50 > 21.50 |
| Mutual Credit/LETS vs. Georgism / LVT | False (non-dominated) | 14.50 > 13.50 | 16.50 > 15.50 | 12.50 > 12.00 | 16.50 > 15.50 |

The two new **guaranteed** pairs (CCO-PTF vs. MMT+JG; CCO-PTF vs.
Georgism/LVT) did not exist as dominance relations before this project's
own retrofit and Session 6 addition respectively — MMT+JG only fell
under strict dominance once the retrofit's more conservative C1.2b=0.0
removed its prior escape route (Section 11.3's own already-published
finding), and Georgism was scored directly under the v2 structure from
its first evaluation, so it was never checked against an alternative
weighting scheme until this pass. Both behave exactly as Theorem 5
requires.

The **non-dominated** Mutual Credit/LETS-vs-Georgism pair is worth a
second look precisely because it is *not* guaranteed: Mutual Credit/LETS's
weighted total exceeds Georgism's under every one of the four schemes
tested, despite the two systems occupying different, non-adjacent
adequacy tiers in the *opposite* direction (Georgism: 2 failures,
Potentially Adequate; Mutual Credit/LETS: 3 failures, Partially
Adequate) — the identical percentage-vs-tier tension already documented
for this pair under equal weighting (Report System 15's own "note on the
adequacy-tier result") turns out to hold under every alternative scheme
checked too, not merely the one weighting convention under which it was
first noticed.

## Adequacy tier confirmation, all 15 systems (illustrative, not a test)

| System | Failures | Tier (invariant across all 4 schemes) |
|---|---|---|
| CCO-PTF-CIP-SZH | 0 | Potentially Adequate |
| Participatory Economics | 1 | Potentially Adequate |
| Nordic Social Democracy | 2 | Potentially Adequate |
| Degrowth Economics | 2 | Potentially Adequate |
| Market Socialism | 2 | Potentially Adequate |
| Georgism / Land Value Tax | 2 | Potentially Adequate |
| Integral | 3 | Partially Adequate |
| MMT + Job Guarantee | 3 | Partially Adequate |
| Mutual Credit / LETS | 3 | Partially Adequate |
| Universal Basic Income | 7 | Structurally Inadequate |
| Status Quo Market Capitalism | 9 | Structurally Inadequate |
| Stakeholder Capitalism | 9 | Structurally Inadequate |
| Fully Automated Luxury Communism | 10 | Structurally Inadequate |
| Centrally Planned Socialism | 12 | Structurally Inadequate |
| Libertarian Minarchism | 15 | Structurally Inadequate |

## Conclusion

The reading Section 10.9 and the original Appendix A.4 already argued for
on normative grounds holds, empirically, across the full corpus: equal
weighting affects which of several non-dominating, roughly-comparable
systems ranks marginally ahead of another (most visibly Nordic vs.
Integral, and, newly documented here, FALC's scheme-specific rise and the
UBI/Mutual-Credit-LETS percentage tie's dependence on the equal-weighting
convention specifically) — but it cannot affect adequacy classification
or any already-established dominance relation, by construction rather
than by luck, for 15 systems exactly as it could not for 13. NEEC's
headline comparative claims do not depend on the equal-weighting choice;
the claims that do depend on it are, again, exactly the ones this project
has always treated as its least important output (Section 10.3).

---

## Verification

`run_a4_full_rerun.py` (included alongside this draft) imports
`SCORES`/`PUBLISHED`/`SCHEMES`/`weighted_total`/`max_possible`/
`failure_count`/`tier`/`dominates` directly from an unmodified copy of
`neec_weighting_robustness_analysis_v2.py` and requires
`verify_transcription()` to pass (it does — all 15 systems' 26-criterion
vectors sum to their published domain/overall totals exactly) before
computing anything. It deliberately does **not** call that script's own
`verify_unchanged_from_legacy()`, since `baseline_weighting_script.py`
remains absent from the project mount — this is a pre-existing, separately
tracked gap (Session 9-11 handoffs' own Remaining Scope item 8), not a
gap this pass introduces, and `verify_unchanged_from_legacy()` tests
something orthogonal to weighting robustness (whether Step 1c touched
only the wealth criteria — already independently confirmed clean in
Sessions 8-10 when that file was available). All figures in every table
above were produced by, and can be independently reproduced from, that
script's fresh output.

**Appendix note: `baseline_weighting_script.py` reconstructed this
session.** Both dependent scripts that need this file
(`verify_unchanged_from_legacy()` and `step1c_retrofit.py`) require only
two things from it: a `SCORES` dict giving each of the 13 pre-retrofit
systems' full 25-criterion vector (legacy, unsplit C1.2/C1.5), and a
`PUBLISHED` dict exposing each system's legacy Total. Both are fully
recoverable from already-published, cross-referenced sources: every
legacy C1.2/C1.5 value is stated identically in both
`NEEC_Step1c_Retrofit_C1.2ab_C1.5.md`'s own "Legacy text" citation at the
start of each system's subsection and `neec_scores_csv_builder_v2.py`'s
own per-row `revision_note` strings; every other criterion is,
by Step 1c's own design, unchanged from the current canonical `SCORES`
dict. A reconstruction built this way (`baseline_weighting_script.py`,
included with this session's outputs) was checked against
`PUBLISHED_LEGACY_25` (already present in
`neec_weighting_robustness_analysis_v2.py`) and matches all 13 systems'
legacy totals exactly; separately, running both previously-blocked
scripts against it reproduces every already-published Step 1c figure
(the old/new comparison table, the tier-change flag, the final ranking)
exactly. This is disclosed as a reconstruction of the file's *data*, not
a recovery of its original text — treat it as provisional until whoever
has access to the original file can confirm it (or replace it if the
original resurfaces), but it is not blocking: every number it produces
was already independently checkable before it existed, and now is,
mechanically, again.
