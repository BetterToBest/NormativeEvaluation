# NEEC Criteria Review, Session 44

**Status: proposal under Paper v1.4 Appendix I; nothing applied.** Session 44, 2026-09-23. Scorer and engineer:
Claude (Opus 5.5). Evidence tables: `criteria_review_s44.py`, output `criteria_review_s44_output.txt` (harness check
87). Inputs: `criteria.json` and `neec_corpus.json` in force at `s43`, and the findings of the seven rescoring records
(`NEEC_Rescoring_s37.md` to `_s43.md`).

## 1. Question and method

The owner asked whether the 26 criteria have gaps or redundancy, given the goal that any scorer, human or AI,
reproduce the same results. The review read every Pass Threshold, Requirement line and derivation, and asked three
things: (a) does each quantity enter the score once, at one bar; (b) would two careful scorers reading the same
evidence reach the same verdict; (c) does each norm N1–N14 have a criterion that measures its core, and is anything
a critical outside reviewer would expect missing. Proposals were chosen on those grounds only, not by their effect on
any system's rank; that effect is computed after adoption, as the rescoring pass computes its own.

## 2. Corrections: one quantity, more than one bar (K)

Paper v1.4 section 12.2 set the rule: a quantity scored in two criteria is a redundancy, and it moved the wealth Gini
from C1.5 to C1.2b on that ground. Five quantities still enter twice (output, section 2); on the corpus in force the
affected criterion pairs agree in 56.5–69.6% of entries against a 44.8% mean over all 325 pairs (section 3).

- **K1. Wealth Gini <0.35** is in C1.2b and again as C4.4's clause 1. Keep it in C1.2b; delete it from C4.4.
- **K2. Citizen proposals adopted** is in C2.4 at ≥35% and in C4.4 at ≥40%: one quantity, two bars. Keep it in C2.4
  (participation); delete it from C4.4, which then measures the distribution of political power by its accountability
  and removal clauses.
- **K3. Carbon reduction by 2030** is in C4.1 (35%) and C4.2 (35–45%). **K4. Resource use against regeneration** is in
  C4.1 (≤90%) and C4.2 (≤100%): two bars. Keep both in C4.2; C4.1 becomes fiscal and wealth sustainability across
  generations (debt path, wealth transfer). Rescoring reading 3.3 (s43) already records that C4.2 shares both clauses.
- **K5. Share of decisions free of coercion**: C2.1 requires ≥70% reporting genuine autonomy; C4.5 requires residual
  coercion below 10% of decisions. These are one construct at bars that disagree (70% autonomous admits up to 30%
  coerced). Keep it in C2.1; C4.5 keeps extraction and exit from exploitative relationships. (C4.5's exit clause is
  not a duplicate of C2.5, which concerns exit from the system itself, under N9.)
- **K6. Requirement figures that differ from the Pass Threshold** (protocol 2.3 asks these be flagged): C1.1 (95% vs
  90%, already known), **C1.2a ($70,000+ vs ≥$60,000)** and **C1.4 (poverty <5%, demand 90–110% vs <8%, >85%)**, the
  last two new. The Pass Threshold is operative; v2.0 should carry one figure per quantity, and the criteria
  generator should assert it.

No criterion is removed; K1–K5 remove clauses. Removing a clause from a conjunctive threshold can keep or raise a
score, never lower it, so only units the removed clause decided need re-checking, and the rescoring records name the
deciding clause of each unit they re-estimated.

## 3. Reproducibility (R)

- **R1. Dated clauses.** C4.1 and C4.2 bind "by 2030"; C1.4's scenarios are dated 2030 and 2040. After 2030 these can
  bind only a record. Restate each as a rate from a stated base year, or as consistency with a named, published
  pathway (rescoring reading 3.3 flagged this for C4.1).
- **R2. Place-bound measures.** C1.1's protocol names the US Census Supplemental Poverty Measure; C1.3 uses area median
  income, a US construct; C1.2a's Pass Threshold is a dollar figure with no price year or purchasing-power basis
  (its protocol adjusts for some contexts). The corpus includes China, Qatar and Singapore. Restate with
  internationally published measures at constant, purchasing-power-adjusted prices, or relative measures.
- **R3. Quantities nobody publishes.** When the pass is applied, seven criteria have no 1.0 (C1.1, C2.1, C2.3, C2.4,
  C3.1, C3.5, C4.1). In C2.1, C2.3, C2.4 (clause 2), C3.1 and C3.5 the clauses fix levels of quantities no statistical
  agency publishes: a revealed-preference autonomy share, 10+ weekly hours of creative engagement, a proposal-adoption
  share, a 72-hour response scaling 1:1 with output loss, diagnosis and correction shares. A criterion no system can
  clear separates only 0.0 from 0.5. For each, v2.0 should either tie the clause to a published indicator with a named
  source (time-use surveys for discretionary time, for example) or declare it aspirational and say so in the Paper.
- **R4. Instruments in place of outcomes.** C4.3's clause 2 (disadvantaged groups receive 150%+ proportional benefits)
  requires targeting, which a universalist system cannot show even where disparities close; C3.4 requires
  "democratic governance for changes"; C5.2 requires a written plan for both staged and rapid deployment. Instrument
  clauses credit designs that name the instrument; outcome clauses credit whatever works. Restate as outcomes, except
  where the norm itself names the instrument: C2.2's "unconditional" is N2's content and stays, disclosed as the one
  criterion that favours unconditional-provision designs by definition.
- **R5. 0.5 means two things.** Of 118 units re-estimated, 111 became 0.5, most because a clause was not shown (records s37–s43). A 0.5 now records
  either partial performance or silence. Keep the scale; publish beside each system's total the number of units that
  rest on a clause not shown (the D28 clause records already hold this). No score changes; a reader or replicator
  sees how much of each total rests on evidence and how much on its absence.
- **R6. "Racial and Gender Equity"** names axes salient in some societies. In Qatar the salient axis is citizenship;
  elsewhere caste, ethnicity or religion. Rename it Group Equity, with the axes declared per entry in the scope
  declaration (protocol 3.3).

## 4. Structure (S)

- **S1. Equal criteria are not equal norms.** Under equal criterion weighting the norms' implicit shares run from
  15.4% (N7, in eight criteria) to 1.9% (N11) (output, section 1). Paper 10.9 defends equal criterion weighting;
  v2.0 should also publish the norm weights it implies. The same table bears on Paper 10.5: N2 and N11, the norms
  closest to CCO-PTF's design, carry 7.1% and 1.9%.
- **S2. N6 is called a hard constraint and scored as one unit in 26.** Section 4's N6 text says ecological compliance is
  not traded against other goods; the aggregation trades it (a 0.0 on C4.2 costs one point). Either make it a gate
  or restate the text. Proposed: restate N6's sentence to describe the Applied scoring accurately, and add "N6 as a
  constraint" (a 0.0 on C4.2 caps the tier at Partially Adequate) to Appendix A.4's named schemes, so the constraint
  reading is reported without changing the headline.
- **S3. Two norms have no criterion measuring their core.** N13 (incentive alignment) is only the second parent of
  C2.3 and C3.2. N14 (scaling without extraction) maps only to C5.5, which measures cultural portability, not
  extraction. G1 and G3 below close these.

## 5. Gaps (G)

- **G1. Productive and innovative capacity** (from N13 + N1; proposed C3.6). Nothing tests whether a system can produce
  and improve what its other criteria assume it distributes; the distribution criteria can all be passed on
  projections that hold output fixed. This is the question comparative economics most often puts to alternative
  systems (allocation under dispersed information), and its absence is the first gap an outside reviewer would name.
  Defined on provisioning, not GDP growth, so it builds in no preference against Degrowth or Doughnut Economics. Draft
  clauses: real output per hour worked non-declining over 20 years; a functioning mechanism that directs investment to
  new products and processes; basic-needs provisioning maintained under the system's own working-time assumptions.
- **G2. Civil liberties and rule of law** (from N3 + N7; proposed C2.6). Domain 2 measures economic coercion,
  participation and exit, but not speech, association, due process, judicial independence or privacy. That is where
  the state-capitalist entries differ most from the rest, and where designs that route allocation through shared data
  systems raise questions. It would also be NEEC's most reproducible criterion: published expert indices score real
  economies, and designs are scored on stated guarantees and independent adjudication under protocol 4.1.
- **G3. N14 through clauses, not a new criterion.** Measure C4.2 on consumption-based accounting, so emissions and
  extraction moved abroad do not pass; extend C4.3 (renamed, R6) to non-citizen residents.
- **Considered and not proposed.** Health and education outcomes (access is already in C1.1's and C2.2's baskets;
  outcomes depend heavily on non-economic causes, and adding them would count poverty twice); care work (C4.3's gender
  axis, C2.2); financial stability (C3.1, C3.3's compound scenarios); corruption (C3.5, C4.4, and G2); privacy (G2);
  governance of automation (C1.4, N11). They are listed so a reviewer can see the question was asked.

## 6. Cost and sequencing

- **Package A** (K1–K6, R1–R6, S1–S2, G3): no criterion added; the count stays 26. It rewrites the thresholds of C1.1,
  C1.2a, C1.3, C1.4, C4.1, C4.2, C4.3, C4.4 and C4.5, and the indicators of the R3 criteria.
- **Package B** (G1, G2): 26 → 28 criteria, 46 new units (23 entries × 2), Domain 2 and Domain 3 maxima 5 → 6, every
  total restated. The tier bands (0–2, 3–5, 6+ failures) would be kept as integers and the choice disclosed, with
  Appendix A.4 reporting the proportional alternative.
- **Why now.** The pass paused at C4.2 and C4.4, two of the criteria Package A rewrites. Deciding first means those
  units are scored once, on the clauses v2.0 will carry.

## 7. Decisions

- **7.1 (under the delegation; flagged; the owner may reverse).** Package A is adopted for the v2.0 criteria, and the
  rescoring pass continues on the revised clauses: the pass's own rule that it changes no Pass Threshold (s43, reading
  3.3) is lifted for Package A only, because scoring C4.2 and C4.4 on clauses v2.0 will delete would be done twice.
  The restated criteria are written by generator (`build_criteria.py`) with the current `criteria.json` snapshotted
  and earlier checks pinned to the snapshot.
- **7.2 (the owner's decision).** Package B changes the framework's structure and every total, so it is not taken under
  the delegation. Recommendation: adopt both G1 and G2. If adopted, their 46 units are scored in the pass alongside
  the remaining D28 units, under the same protocol.
