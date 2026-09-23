# NEEC Rescoring Pass — Record, Part (b), Third Group: C1.1 Poverty Elimination Capacity

**Session 40 · 2026-09-23 · Scorer and engineer: Claude · Owner: Duke Johnson**
**Status: scratch (protocol 10.1). Parts (a), (b1) and (b2) are `NEEC_Rescoring_s37.md`, `NEEC_Rescoring_s38.md` and
`NEEC_Rescoring_s39.md`; this record continues the pass and edits none of them.** No corpus file, score or scoring
document changes until the pass ends. Its changes are then applied by generator with pinned inputs and restated in
place (protocol 10.2, 10.3; decisions D12, D14), and until then the published totals stand, provisional as
`README.md` says. Decisions taken here are Claude's under the owner's delegation (Handoff 35, section 2); each is
recorded with its reasons, and the owner may reverse any of them.
**Reproduce:** `python3 rescoring_s40.py` (harness check 83). The script holds every clause estimate below, checks the
group against the R4 audit's register and every verdict against D28, lists and asserts the one departure from the
audit's codes, checks the pinned simulation runs this record quotes, computes every figure in section 5 cumulatively
with parts (a), (b1) and (b2), and checks that this record contains its generated tables verbatim. The simulation runs
are `cco_simulation_checks_s40.js` and its captured output (section 7).

---

## 1. What this group is

Handoff 39 orders C1.1 next: its nine part (b) units (Nordic Social Democracy, Centrally Planned Socialism, Market
Socialism, MMT + Job Guarantee, UBI, Degrowth, Fully Automated Luxury Communism, Participatory Economics and
CCO-PTF-CIP-SZH), every one a published 1.0. The Pass Threshold has two clauses: "≥90% poverty reduction within 20
years under base scenario" and "≥85% under stress testing". The audit coded the first addressed and the second silent
on all nine units: no rationale says anything about poverty under stress, although protocol 2.1 asks a pass to hold
"where the criterion specifies one, under stress". CCO-PTF-CIP-SZH's base clause is also tested, against the design's
own published model, as Handoff 39 directs under part (b1)'s decision 3.2.

None stands. All nine become 0.5 (4.5 points). No failure count and no tier changes. CCO-PTF-CIP-SZH keeps first place,
22.0 to 21.5. After this group no entry in the corpus scores 1.0 on C1.1 (reading 3.5).

## 2. How a clause is recorded, and the rule

As in part (a), section 2: each clause is cleared, short, not shown, out of reach or moot; a 1.0 stands only if every
clause is cleared or moot, and otherwise becomes 0.5 (D28, protocol 2.3). A clause the audit coded A is carried as
cleared on the unit's own text ("as audited"). This group departs from that once, and the script asserts it and that
no other A clause departs: CCO-PTF-CIP-SZH's base clause, where the design's own published model contradicts the text's
98% (reading 3.3), an own-source exception of the kind part (a), section 2, defines. The stress clause was coded
silent everywhere, so estimating it is no departure.

## 3. Decisions and readings (under the delegation)

**3.1 C1.1, clause 2: what shows "≥85% under stress testing".** (1) *Interpretations.* The clause could be read as
asking for an estimate of poverty reduction under an adverse scenario, at the entry's evidentiary tier; or as satisfied
wherever the entry's mechanism is specified to keep operating in a downturn, the base estimate being carried into
stress. (2) *Preponderance.* The clause states a figure, 85%, distinct from the base clause's 90%, which presupposes an
estimate made under stress; protocol 2.1 places at 0.5 performance that "holds only under favourable or untested
conditions"; and part (b1)'s reading 3.5 already holds, for designs, that an institution specified is not an estimate
of the level it produces. (3) *Score* against the first reading, at the tier of protocol 4.1: for a real-world or
historical entry, the documented poverty outcome through a documented severe downturn in an implementation the entry
counts, on C1.1's own measure (reading 3.2); for a design, an estimate of the level under a stated adverse scenario,
from a run of its published model (part (b1), decision 3.2) or a projection its sources state. (4) *Alternative
rejected:* carrying the base estimate into stress wherever a mechanism is specified to operate automatically in a
downturn (MMT + Job Guarantee's countercyclical enrolment; UBI's unconditional payment). Protocol 2.1's text decides
this, so no unit is flagged on it; and the one crisis-tested precedent of such a component located, Argentina's Plan
Jefes y Jefas, moved its participants only part of the way (MMT's unit).

**3.2 C1.1's measure.** C1.1's Measurement line defines absolute poverty as the "inability to afford basic necessities
(housing, food, healthcare, utilities) using regional cost-of-living adjusted baskets". Where a stress record reports a
relative measure and absolute indicators separately, and the two diverge, the absolute indicators govern. This decides
one unit. In Finland's 1991-93 depression relative poverty fell slightly, partly because the median, and so the
relative line, fell; social-assistance receipt doubled and poverty rose in real terms (Uusitalo 2000). The reading is
Nordic Social Democracy's flag, toward 1.0: its own 94-96% figure states no measure and appears to be relative, and on
that measure poverty held.

**3.3 CCO-PTF-CIP-SZH, clause 1: which of the design's own sources governs.** The rationale's "98% poverty elimination
in modeling" is the stated outcome in the design's parameter file (`data/optimal-parameters.json`, v1.0.0, 2025-09-18)
and its two modelling papers on the research hub. The parameters the file names for that outcome (a Basic Unit of
$1,200 a month, octave 6, 78% participation, 20% PTH uptake) are the Compassionism Simulation's own Full Integration
reference settings. The model that produced 98% is not published in runnable form (the hub holds the papers and the
parameter file, no code); the simulation is published, versioned and reproduced (part (b1), decision 3.2). Run at those
settings for 20 years on 100 seeds, it reduces wealth poverty by 78.5% and BLEI poverty by 82.1% against its paired
Baseline, and no seed reaches 90% on either (section 7). *Decision:* the published model governs, because it is the
design's current, reproducible specification and it is run at the very settings the file credits with 98%; the engine
itself carries the papers' headline median wealth, $82,000, as a target constant (`CFG.TARGET_WEALTH`), not an output.
*Measures:* neither of the engine's headcounts is C1.1's basket measure (wealth poverty counts net wealth below
$25,000; BLEI poverty counts under 30 days of runway against basic daily costs), and the modelling paper measured
poverty below 60% of median income. The engine's two are read as the model's own nearest measures, as it presents
them, with its lowest tier (BLEI Crisis, under 7 days) as a sensitivity: 87.4%, still short. *Baseline:* reduction is
taken against the paired Baseline at year 20, the model's own counterfactual and the reading more favourable to the
design; against year 0, C1.1's measurement protocol, wealth poverty falls 59.3% and BLEI poverty rises. *Alternative:*
the papers' figures credited at the modelling tier (protocol 4.1). It is the unit's flag, toward 1.0.

**3.4 CCO-PTF-CIP-SZH, clause 2: the stress run.** Within the engine's own parameters, as part (b1)'s decision 3.2
requires: the reference settings with the engine's adverse channels switched on singly and together (recessions; AI
automation; recessions, automation and 2% inflation), each paired with the Baseline as `index.html` pairs it
(recessions and automation mirrored, Baseline inflation fixed at 3% CPI); and the engine's own shipped Stress Test
preset, which also lowers participation to 40% and the Basic Unit to $900. `harness.js` runs every trajectory with
recessions off (its own scope note), so the two recession functions are read verbatim from `index.html` at the same
commit and appended unchanged; both files are pinned by digest, and the runner is asserted to reproduce
`runScenario()` exactly on all 100 seeds when recessions are off. *The governing figure* is the combined run at the
reference settings (56.4% and 60.0%), since the Stress Test preset also weakens the design's own parameters (31.0% and
32.6%). Both are short of 85%, as are recessions alone (77.8% and 81.6%) and automation alone (69.4% and 72.3%).

**3.5 After this group no entry scores 1.0 on C1.1.** C1.1's 1.0 anchor cites Nordic Social Democracy, which this group
moves to 0.5, and no corpus unit is left at 1.0 to replace it. `criteria_schema.json` requires no minimum number of
examples in a band. *Decision:* when the pass is applied, the 1.0 band keeps its description, drops its example, and
records the change in the file's `source.corrections`. *Alternative rejected:* a hypothetical example, because every
anchor example is checked against a published corpus score (`build_criteria.py`). That a criterion of the framework is
now cleared by no scored system is itself a finding the Report v2.0 and Paper v2.0 must state (section 6).

## 4. The units

### 4.1 Summary (generated)

| Entry | Criterion | Clauses | Verdict | Flag |
|---|---|---|---|---|
| NSD | C1.1 | C U | 1.0 → 0.5 | alternative 1.0 |
| CPS | C1.1 | C S | 1.0 → 0.5 |  |
| MS | C1.1 | C U | 1.0 → 0.5 |  |
| MMT | C1.1 | C U | 1.0 → 0.5 |  |
| UBI | C1.1 | C U | 1.0 → 0.5 |  |
| DG | C1.1 | C U | 1.0 → 0.5 |  |
| FALC | C1.1 | C U | 1.0 → 0.5 |  |
| PE | C1.1 | C U | 1.0 → 0.5 |  |
| CCO | C1.1 | S S | 1.0 → 0.5 | alternative 1.0 |

Clause statuses are listed in Appendix B's order: C cleared, S short, U not shown, R out of reach, M moot.

### 4.2 Clause by clause (generated)

#### NSD C1.1 Poverty Elimination Capacity: 1.0 → 0.5 — flagged as contestable

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥90% poverty reduction within 20 years under base scenario | cleared | Achieves 94-96% poverty elimination | as audited (the unit's own text) |
| 2 | ≥85% under stress testing | not shown | Finland's 1991-93 depression is the documented stress episode (GDP down about 10% in three years, unemployment from about 3% to 16%): relative poverty did not rise and fell slightly, partly because the median and so the line fell, while social-assistance receipt doubled, the lowest decile's real income fell and in real terms poverty increased; C1.1 measures absolute poverty against a basket of necessities, and no reduction rate on that measure is located for the stress years (readings 3.1, 3.2) | Uusitalo, Social policy in a deep economic recession and after: the case of Finland, ISSA Research Conference, Helsinki (2000); Uusitalo, Economic Crisis and Social Policy in Finland in the 1990s, SPRC Discussion Paper 70, UNSW (1996) |

*Flag:* alternative 1.0: on the relative measure, which the unit's own 94-96% figure appears to use, poverty held through the deepest downturn a Nordic economy has had, as transfers absorbed the fall in factor incomes.

*Note:* Report v1.6's 94-96% is unsourced and does not state its measure; it is C1.1's 1.0 anchor example (section 6).

#### CPS C1.1 Poverty Elimination Capacity: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥90% poverty reduction within 20 years under base scenario | cleared | near-universal elimination of absolute poverty | as audited (the unit's own text) |
| 2 | ≥85% under stress testing | short | Cuba's Special Period (1990-95), after the loss of Soviet support, is a documented stress episode in a centrally planned economy with universal rationing: per capita daily energy intake fell from 2,899 to 1,863 kcal and average adult weight by 4-5 kg, a neuropathy outbreak, possibly due to vitamin deficiencies, affected about 50,000 people in 1992-93, and the decline in infant mortality reversed in 1990-93; a special rationing system shielded children, elderly people and pregnant women from the outbreak, but a basic necessity, food, fell short for the adult population at large | Franco, Ordunez, Caballero and Cooper, CMAJ 178(8) (2008); Franco et al., American Journal of Epidemiology 166 (2007) |

#### MS C1.1 Poverty Elimination Capacity: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥90% poverty reduction within 20 years under base scenario | cleared | demonstrate poverty elimination capacity | as audited (the unit's own text) |
| 2 | ≥85% under stress testing | not shown | the documented stress episode is Spain's 2008-13 crisis: Fagor Electrodomesticos, the group's founding cooperative, failed in 2013 with about 5,700 employees; the group's mechanisms (relocation, early retirement, Lagun-Aro) covered its 1,898 members, of whom 417 were relocated within two months with solutions aimed at 1,000-1,200, while non-member employees of its subsidiaries were outside them; no poverty-reduction figure under stress is located for members or for the wider workforce (reading 3.1) | The Local (14 November 2013); CECOP, relaying Mondragon Corporation (2014); Learning from the Bankruptcy of Fagor Electrodomesticos, reflections at the 2015 CIRIEC conference |

#### MMT C1.1 Poverty Elimination Capacity: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥90% poverty reduction within 20 years under base scenario | cleared | Near-universal poverty elimination achievable | as audited (the unit's own text) |
| 2 | ≥85% under stress testing | not shown | no estimate of poverty reduction under stress is stated or cited; the guarantee is specified as countercyclical, which is a mechanism, not an estimate of the level (reading 3.1); the one crisis-tested precedent of the component, Argentina's Plan Jefes y Jefas in the 2002 crisis, in which poverty rose from 37% to 58%, cut the share of participants falling into indigence from an estimated 40% to 30% | Report v1.6, MMT C1.1 and C3.1; Galasso and Ravallion, World Bank Economic Review 18(3) (2004) |

*Note:* Jefes targeted unemployed heads of households with dependents, so it calibrates confidence in the component (protocol 4.1) rather than estimating the design.

#### UBI C1.1 Poverty Elimination Capacity: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥90% poverty reduction within 20 years under base scenario | cleared | would achieve 95%+ elimination | as audited (the unit's own text) |
| 2 | ≥85% under stress testing | not shown | no estimate under stress is stated or cited; the payment is specified as unconditional and fixed, part (b2) found no rule raising it with crisis severity, and Alaska's dividend, the long-running precedent, is set on an annual cycle (reading 3.1) | Report v1.6, UBI C1.1; NEEC_Rescoring_s39.md, UBI C3.1; NEEC_Rescoring_s38.md, UBI C3.4 |

#### DG C1.1 Poverty Elimination Capacity: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥90% poverty reduction within 20 years under base scenario | cleared | could eliminate poverty | as audited (the unit's own text) |
| 2 | ≥85% under stress testing | not shown | the rationale names instruments (wealth caps, maximum income ratios, universal basic services) that could eliminate poverty; no stress scenario or estimate is stated or cited (reading 3.1) | Report v1.6, DG C1.1 |

#### FALC C1.1 Poverty Elimination Capacity: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥90% poverty reduction within 20 years under base scenario | cleared | Theoretical capacity for 100% poverty elimination | as audited (the unit's own text) |
| 2 | ≥85% under stress testing | not shown | the rationale conditions its figure on technological assumptions proving correct; no scenario in which they fall short, this entry's stress case, is estimated (reading 3.1) | Report v1.6, FALC C1.1 |

#### PE C1.1 Poverty Elimination Capacity: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥90% poverty reduction within 20 years under base scenario | cleared | would eliminate poverty | as audited (the unit's own text) |
| 2 | ≥85% under stress testing | not shown | remuneration by effort and sacrifice and universal access to consumption councils are specified; no stress scenario or estimate is stated or cited (reading 3.1) | Report v1.6, PE C1.1 |

#### CCO C1.1 Poverty Elimination Capacity: 1.0 → 0.5 — flagged as contestable

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥90% poverty reduction within 20 years under base scenario | short | on the design's own published model (reference preset, 20 years, 100 seeds), wealth poverty falls 78.5% and BLEI poverty 82.1% against the paired Baseline, and no seed reaches 90% on either; against year 0 wealth poverty falls 59.3% and BLEI poverty rises; the engine's lowest tier, BLEI Crisis, gives 87.4%; the rationale's 98% is the design's parameter file's stated outcome for a Basic Unit of $1,200, octave 6, 78% participation and 20% PTH uptake, the engine's own reference settings; the model that produced it is not published in runnable form, the modelling paper measures poverty below 60% of median income, and the engine carries the papers' headline median wealth, $82,000, as a target (reading 3.3) | compassionism-simulation at cd0ceec (v4.15), harness.js and index.html; cco_simulation_checks_s40_output.txt; research-hub at 8e8a6ba (2026-09-21), data/optimal-parameters.json (v1.0.0, 2025-09-18), economic-modeling-simulation.html and cco-ptf-integrated-framework.html |
| 2 | ≥85% under stress testing | short | with the engine's adverse channels on at the reference settings (recessions, AI automation and 2% inflation, paired with the Baseline as the engine pairs them) the reductions are 56.4% and 60.0%; recessions alone give 77.8% and 81.6%, automation alone 69.4% and 72.3%, and the engine's own Stress Test preset 31.0% and 32.6%; at most 4 of 100 seeds reach 85% on a documented measure in any stress run (reading 3.4) | compassionism-simulation at cd0ceec (v4.15), harness.js and index.html; cco_simulation_checks_s40_output.txt |

*Flag:* alternative 1.0: the design's hub papers' modelled figures credited at the modelling tier instead of the published engine: 98% reduction in the base case, and poverty below 3% in 87% of recession scenarios.

*Note:* neither of the engine's headcounts is C1.1's basket measure; they are read as the model presents them. The unit reopens if a later version of the simulation reaches 90% in the reference run and 85% in the stress run on its documented measures, or if the model behind the papers' figures is published and reproduces them.

## 5. What parts (a) and (b) so far change (generated)

| Entry | Published (rank) | After (a) | After (b1) | After (b2) | After this group (rank) | Change here | Failures | Tier | D28 units left | Floor if all fall |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| CCO | 24.5 (1) | 24.0 | 22.5 | 22.0 | 21.5 (1) | -0.5 | 0 | Potentially Adequate | 7 | 18.0 |
| PE | 20.5 (2) | 20.5 | 19.0 | 18.5 | 18.0 (2) | -0.5 | 1 | Potentially Adequate | 8 | 14.0 |
| NSD | 19.5 (3) | 17.0 | 16.0 | 15.5 | 15.0 (5) | -0.5 | 2 | Potentially Adequate | 4 | 13.0 |
| INT | 19.5 (3) | 19.0 | 18.0 | 17.5 | 17.5 (3) | 0.0 | 3 | Partially Adequate | 8 | 13.5 |
| DG | 19.0 (5) | 19.0 | 17.5 | 17.0 | 16.5 (4) | -0.5 | 2 | Potentially Adequate | 6 | 13.5 |
| MS | 16.5 (6) | 15.5 | 14.0 | 13.5 | 13.0 (8) | -0.5 | 2 | Potentially Adequate | 0 | 13.0 |
| MMT | 15.5 (7) | 14.0 | 13.0 | 12.5 | 12.0 (13) | -0.5 | 3 | Partially Adequate | 1 | 11.5 |
| UBI | 14.5 (8) | 13.0 | 12.5 | 12.0 | 11.5 (15) | -0.5 | 7 | Structurally Inadequate | 1 | 11.0 |
| MC | 14.5 (8) | 14.5 | 13.5 | 13.0 | 13.0 (8) | 0.0 | 3 | Partially Adequate | 2 | 12.0 |
| OS | 14.5 (8) | 14.0 | 14.0 | 14.0 | 14.0 (6) | 0.0 | 3 | Partially Adequate | 2 | 13.0 |
| SWF | 14.0 (11) | 14.0 | 14.0 | 13.5 | 13.5 (7) | 0.0 | 3 | Partially Adequate | 2 | 12.5 |
| SG | 14.0 (11) | 13.0 | 12.5 | 12.0 | 12.0 (13) | 0.0 | 4 | Partially Adequate | 0 | 12.0 |
| GEO | 13.5 (13) | 13.0 | 13.0 | 13.0 | 13.0 (8) | 0.0 | 2 | Potentially Adequate | 1 | 12.5 |
| UBS | 13.5 (13) | 13.5 | 13.0 | 12.5 | 12.5 (11) | 0.0 | 3 | Partially Adequate | 1 | 12.0 |
| IF | 13.5 (13) | 12.5 | 12.5 | 12.5 | 12.5 (11) | 0.0 | 5 | Partially Adequate | 2 | 11.5 |
| FALC | 13.0 (16) | 12.5 | 12.0 | 12.0 | 11.5 (15) | -0.5 | 10 | Structurally Inadequate | 5 | 9.0 |
| DE | 11.5 (17) | 11.0 | 10.5 | 10.5 | 10.5 (17) | 0.0 | 8 | Structurally Inadequate | 3 | 9.0 |
| SQ | 10.5 (18) | 10.0 | 10.0 | 10.0 | 10.0 (18) | 0.0 | 9 | Structurally Inadequate | 1 | 9.5 |
| CPS | 10.0 (19) | 8.5 | 8.5 | 8.5 | 8.0 (21) | -0.5 | 12 | Structurally Inadequate | 1 | 7.5 |
| SC | 10.0 (19) | 10.0 | 9.0 | 9.0 | 9.0 (20) | 0.0 | 9 | Structurally Inadequate | 1 | 8.5 |
| CN | 10.0 (19) | 10.0 | 10.0 | 9.5 | 9.5 (19) | 0.0 | 8 | Structurally Inadequate | 0 | 9.5 |
| QA | 9.0 (22) | 8.5 | 8.5 | 8.0 | 8.0 (21) | 0.0 | 10 | Structurally Inadequate | 0 | 8.0 |
| LM | 8.0 (23) | 6.5 | 6.5 | 6.5 | 6.5 (23) | 0.0 | 15 | Structurally Inadequate | 2 | 5.5 |

"D28 units left" counts the entry's units still to be re-estimated in part (b); "Floor if all fall" is the total if
every one of them became 0.5.

After this group the corpus has 18 dominance pairs against 18 after part (b2) (new: none; lost: none), and its frontier holds 12 entries against 12 (NSD, MS, UBI, DG, FALC, PE, CCO, INT, MC, SWF, IF, OS). First place: CCO, 22.0 after part (b2), 21.5 now. Across parts (a), (b1), (b2) and (b3), 87 units have been re-estimated: 6 stand and 81 become 0.5 (40.5 points). No entry now scores 1.0 on C1.1.

Left for part (b): 58 D28 units (C1.4 2, C2.1 5, C2.5 10, C3.2 4, C3.5 2, C4.1 8, C4.2 6, C4.3 6, C4.4 4, C4.5 3, C5.2 4, C5.4 2, C5.5 2).

Flags added in this group: 2; removed: 0. Across the pass so far, 14 entries' flag registers change (CCO, CN, CPS, IF, LM, MC, NSD, OS, QA, SG, SQ, SWF, UBI, UBS).

Anchor examples citing a unit the pass moves: C1.1's 1.0 example, NSD (part (b3), to 0.5); C2.1's 1.0 example, UBI (part (a), to 0.5); C2.3's 1.0 example, DG (part (b1), to 0.5); C2.4's 1.0 example, PE (part (b1), to 0.5); C3.1's 1.0 example, UBI (part (b2), to 0.5); C5.1's 1.0 example, MS (part (b2), to 0.5). When the pass is applied, each band needs an example the corpus then scores at that value; C1.1's 1.0 band has none left (reading 3.5).

## 6. Corrections found (not polish)

1. **Report v1.6, Nordic Social Democracy C1.1**, says the model "achieves 94-96% poverty elimination". The figure has
   no source and does not state its measure; C1.1's calculation is a reduction rate against a baseline, on absolute
   poverty (reading 3.2). The same sentence is C1.1's 1.0 anchor example (item 3). Report v2.0 states the measure and
   the source, or restates the claim.
2. **Report v1.6, CCO-PTF-CIP-SZH C1.1**, says the design "achieves 98% poverty elimination in modeling". The design's
   published model, at the settings its own parameter file credits with 98%, gives 78.5% (wealth poverty) and 82.1%
   (BLEI poverty) against its paired Baseline (reading 3.3). Report v2.0 cites the published model and its figures,
   or names the model that produced 98% and where it can be run.
3. **Anchor examples.** C1.1's 1.0 example (Nordic Social Democracy) is a sixth example the pass moves (section 5),
   and the first whose band is left with no corpus unit at that value. Handling: reading 3.5.
4. **A finding the v2.0 documents must state:** after the pass as it now stands, no scored system clears C1.1, the
   first criterion of the first domain. Report v2.0's and Paper v2.0's comparative sections say so, and say why: no
   rationale in the corpus estimated poverty reduction under stress.

*For the simulation's maintainers (not a NEEC correction):* the headline 98% and $82,000 of the research hub's
modelling papers and parameter file are not reproduced by the current engine at the same parameters; the engine's
Baseline counterfactual deteriorates from 37.7% to 71.4% wealth poverty and from 2.7% to 70.5% BLEI poverty over 20
years, which flatters any reduction measured against it; and neither engine headcount is an income or basket measure.
The owner decides what the simulation does with these.

*Polish, optional:* the unit texts' "within 20 years" could be read against the measurement protocol's 5-year
tracking; section 7's second table gives the reference run at each interval.

## 7. The simulation runs (generated from `cco_simulation_checks_s40_output.txt`)

Engine: `harness.js` at `BetterToBest/compassionism-simulation` commit `cd0ceec` (v4.15), md5 `035d1be8…`, with
`updateRecession` and `buildRecessionPath` appended verbatim from `index.html` at the same commit, md5 `1c8273b1…`.
The run reproduces the documented seed-42 reference regression (median BLEI 1965 d, wealth poverty 16.6%, Gini 0.534,
System Stability 88.5%) and Session 38's run 1 (Baseline 71.4% and 70.5%; reference 15.3% and 12.6%) before either
table is trusted. N = 100 seeds (1-100), 500 agents, 20 years; figures are seed means. The last column counts seeds
whose own reduction against their paired Baseline clears the clause the row tests: 90% for the base scenario, 85% for
the stress runs.

| Scenario | Measure | Year 0 | Paired Baseline, yr 20 | Scenario, yr 20 | Reduction vs paired Baseline | Reduction vs year 0 | Seeds clearing the clause vs Baseline |
|---|---|---:|---:|---:|---:|---:|---:|
| A. Reference (Full Integration), no stress | Wealth poverty | 37.7% | 71.4% | 15.3% | 78.5% | 59.3% | 0 of 100 at 90% |
| A. Reference (Full Integration), no stress | BLEI poverty | 2.7% | 70.5% | 12.6% | 82.1% | none (rises from year 0) | 0 of 100 at 90% |
| A. Reference (Full Integration), no stress | BLEI Crisis (sensitivity) | 0.0% | 45.3% | 5.7% | 87.4% | none (rises from year 0) | 13 of 100 at 90% |
| B1. Reference, recessions on | Wealth poverty | 37.7% | 72.8% | 16.1% | 77.8% | 57.1% | 0 of 100 at 85% |
| B1. Reference, recessions on | BLEI poverty | 2.7% | 71.9% | 13.2% | 81.6% | none (rises from year 0) | 4 of 100 at 85% |
| B1. Reference, recessions on | BLEI Crisis (sensitivity) | 0.0% | 45.4% | 5.8% | 87.3% | none (rises from year 0) | 83 of 100 at 85% |
| B2. Reference, AI automation on | Wealth poverty | 37.7% | 80.8% | 24.7% | 69.4% | 34.4% | 0 of 100 at 85% |
| B2. Reference, AI automation on | BLEI poverty | 2.7% | 80.1% | 22.2% | 72.3% | none (rises from year 0) | 0 of 100 at 85% |
| B2. Reference, AI automation on | BLEI Crisis (sensitivity) | 0.0% | 70.5% | 9.3% | 86.9% | none (rises from year 0) | 84 of 100 at 85% |
| B3. Reference, recessions + automation + 2% inflation | Wealth poverty | 37.7% | 81.8% | 35.7% | 56.4% | 5.3% | 0 of 100 at 85% |
| B3. Reference, recessions + automation + 2% inflation | BLEI poverty | 2.7% | 81.1% | 32.4% | 60.0% | none (rises from year 0) | 0 of 100 at 85% |
| B3. Reference, recessions + automation + 2% inflation | BLEI Crisis (sensitivity) | 0.0% | 70.9% | 11.1% | 84.4% | none (rises from year 0) | 30 of 100 at 85% |
| C. The engine's Stress Test preset | Wealth poverty | 37.7% | 81.8% | 56.5% | 31.0% | none (rises from year 0) | 0 of 100 at 85% |
| C. The engine's Stress Test preset | BLEI poverty | 6.7% | 81.1% | 54.6% | 32.6% | none (rises from year 0) | 0 of 100 at 85% |
| C. The engine's Stress Test preset | BLEI Crisis (sensitivity) | 0.0% | 70.9% | 35.8% | 49.5% | none (rises from year 0) | 0 of 100 at 85% |

The reference run at the measurement protocol's 5-year intervals:

| Measure | Year 0 | Year 5 | Year 10 | Year 15 | Year 20 | Paired Baseline, yr 5 / 10 / 15 / 20 |
|---|---:|---:|---:|---:|---:|---|
| Wealth poverty | 37.7% | 26.6% | 23.9% | 19.9% | 15.3% | 53.9% / 62.3% / 67.4% / 71.4% |
| BLEI poverty | 2.7% | 19.6% | 19.9% | 16.7% | 12.6% | 48.9% / 59.8% / 65.9% / 70.5% |
| BLEI Crisis (sensitivity) | 0.0% | 7.1% | 7.4% | 6.7% | 5.7% | 44.9% / 50.2% / 48.5% / 45.3% |

To rerun: clone `BetterToBest/compassionism-simulation`, check out `cd0ceec`, and run
`node cco_simulation_checks_s40.js path/to/harness.js path/to/index.html`. The harness does not rerun the JavaScript
(the simulation's source is not in this repository); `rescoring_s40.py` checks the captured output's two digests, its
reference run and its own checks, and that this record quotes both tables verbatim.

## 8. Disclosure

CCO-PTF-CIP-SZH is the owner's design. Its C1.1 falls here on both clauses, on the design's own published model run at
the settings the design's own parameter file credits with 98%. The reading that decides its base clause (3.3) prefers
a published, reproducible model over a figure whose model cannot be run; the same preference would apply to any entry
whose rationale cites modelling. The alternative, crediting the papers' figures, is carried as the unit's flag. The
owner told the scorer that the simulation is being calibrated and that v4.16 is in development; the unit reopens if a
later version reaches 90% in the reference run and 85% in the stress run on its documented measures, or if the model
behind the papers' figures is published and reproduces them. The second pilot, with a replicator outside the Claude
family, is the independent test of these calls.

## 9. What remains

- **(b), continued:** the 58 D28 units of section 5's line "Left for part (b)", criterion by criterion; C1.4 next (2
  units), then C2.1, C2.5, C3.2, C3.5, C4.1-C4.5, C5.2, C5.4 and C5.5.
- **(c)** the 131 mechanism-class 0.5s against D29, Ostrom's C4.3 first; **(d)** D31's source for Ostrom's community
  land trusts; **(e)** the Islamic finance and Ostrom documents' quoted thresholds restated.

When the pass ends, its changes are applied by generator, and the corpus, CSV, `README.md` and Appendix A.4 are
regenerated; the changed flag registers are recomputed, the six anchor examples are replaced or, for C1.1's 1.0 band,
removed (reading 3.5), the protocol's statements about the corpus are restated, and the claims and protocol verifiers
and the four rescoring scripts get successors.

## 10. What this record does not show

It is one scorer's re-estimation, on evidence located in one session through web search, the entries' own rationales,
the design's research-hub sources and the design's published model. "Not shown" means no evidence was located, not
that the clause fails. The stress clause fell for every unit chiefly because no rationale in the corpus estimated
poverty under stress; a scoring document that does so, on C1.1's measure, reopens its unit. The simulation's figures
are the model's, at the modelling tier, on measures that are not C1.1's own. Whether these calls reproduce is what the
replication programme tests.
