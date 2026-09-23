# NEEC Rescoring Pass — Record, Part (b), Fourth Group: C1.4 Automation Resilience, C2.1 Freedom from Coercion and C3.2 Inflation Control Mechanisms

**Session 41 · 2026-09-23 · Scorer and engineer: Claude · Owner: Duke Johnson**
**Status: scratch (protocol 10.1). Parts (a), (b1), (b2) and (b3) are `NEEC_Rescoring_s37.md` to
`NEEC_Rescoring_s40.md`; this record continues the pass and edits none of them.** No corpus file, score or scoring
document changes until the pass ends. Its changes are then applied by generator with pinned inputs and restated in
place (protocol 10.2, 10.3; decisions D12, D14), and until then the published totals stand, provisional as
`README.md` says. Decisions taken here are Claude's under the owner's delegation (Handoff 35, section 2); each is
recorded with its reasons, and the owner may reverse any of them.
**Reproduce:** `python3 rescoring_s41.py` (harness check 84). The script holds every clause estimate below, checks the
group against the R4 audit's register and every verdict against D28, asserts that no clause departs from the audit's
A codes and that the two clauses left not estimated sit in units another clause already decides, computes every
figure in section 5 cumulatively with parts (a) to (b3), finds the criteria the pass so far leaves with no 1.0, and
checks that this record contains its generated tables verbatim.

---

## 1. What this group is

Handoff 40 orders C1.4 next, then C2.1 and C2.5. This group takes C1.4's two part (b) units (Fully Automated Luxury
Communism, Participatory Economics), C2.1's five (Degrowth, Fully Automated Luxury Communism, Participatory Economics,
CCO-PTF-CIP-SZH, Integral) and C3.2's four (Status Quo Market Capitalism, Nordic Social Democracy, Participatory
Economics, Integral), every one a published 1.0. C2.5's ten units follow as the next group (reading 3.1).

What the audit found silent: C1.4's Pass Threshold asks for "Poverty <8% and aggregate demand >85% baseline across all
three displacement scenarios"; Fully Automated Luxury Communism's text is silent on both clauses, Participatory
Economics' on demand. C2.1's second clause, "validated through revealed preference showing acceptance of initially
refused employment/living situations when alternatives exist", is silent on all five units, as it was on the three
part (a) re-estimated. C3.2's stress clause, "stress test inflation ≤5% (when external 8%)", is silent on all four,
and Status Quo's and Nordic Social Democracy's texts are also silent on "automatic adjustment preventing runaway
inflation".

None stands. All eleven become 0.5 (5.5 points). No failure count and no tier changes. CCO-PTF-CIP-SZH keeps first
place, 21.5 to 21.0; Participatory Economics and Integral share second at 16.5. After this group no entry scores 1.0
on C2.1, and a check this group adds finds C2.3, C2.4 and C3.1 already in that state: five criteria, each with at
least one 1.0 in the published corpus, are now cleared by no scored system (reading 3.5; section 6, item 1).

## 2. How a clause is recorded, and the rule

As in part (a), section 2: each clause is cleared, short, not shown, out of reach or moot; a 1.0 stands only if every
clause is cleared or moot, and otherwise becomes 0.5 (D28, protocol 2.3). A clause the audit coded A is carried as
cleared on the unit's own text ("as audited") unless the entry's or design's own sources contradict it; no clause in
this group needed that exception, and the script asserts so. Two clauses, Status Quo's and Nordic Social Democracy's
C3.2 clause 3, are marked "not estimated in this pass": each could not change its unit's verdict once clause 2 was
shown short. They stay not shown, and Report v2.0's clause-level Part I must estimate them. The script asserts that no
other silent clause is left unestimated.

## 3. Decisions and readings (under the delegation)

**3.1 The group's order.** C2.5 moves from third to after C3.2. Its ten units span all three scope classes and carry
four reach codes, and its clauses (no differential treatment, geographic mobility, voluntary association) need
readings that must be applied alike across all ten (protocol 5), so they are taken whole as the next group. C3.2's
four units need only readings already fixed or fixed here. The order after C2.5 is Handoff 40's. The change is
procedural and alters no score.

**3.2 C1.4 for designs.** (1) *Interpretations.* The Pass Threshold could be read as asking for levels, poverty under
8% and demand above 85% of baseline, under each of three stated displacement scenarios; or as satisfied by a mechanism
that decouples income and demand from employment "robust in the system's own design logic", the 1.0 anchor's wording.
(2) *Preponderance.* The threshold states figures under named scenarios, and the Measurement line calls for a "stress
test across automation scenarios"; anchors describe and thresholds govern (2.3(g)); part (b3)'s reading 3.1 already
reads C1.1's stress clause as asking for an estimate under the scenario, and part (b1)'s reading 3.5 holds that an
institution specified is not an estimate of the level it produces. (3) *Score* against the first reading: for a
design, an estimate at the three severities, from a run of its published model (part (b1), decision 3.2) or a
projection its sources state. (4) *Alternative rejected:* the anchor's design-logic test. Protocol 2.1 places at 0.5
performance that "holds only under favourable or untested conditions", so no unit is flagged on it, as in part (b3).
*A moot reading of the demand clause was weighed and rejected:* D28(e) moots a transition, scale-up or coordination the
document shows is not needed, and aggregate demand, the economy's total effective or planned consumption, is a level
every economy has; a non-market design's statement that consumption is maintained is a claim about that level, not a
showing that the clause cannot apply. The gap between C1.4's threshold and its Measurement line (section 6, item 3)
decides no unit here.

**3.3 C2.1, clause 2: a method clause.** (1) *Interpretations.* The clause could ask for observed behaviour, in a
population the entry serves, that bears out its self-reported autonomy; or it could be met by a design whose
specification removes survival compulsion, so that any acceptance is voluntary by construction. (2) *Preponderance.*
Protocol 2.3(d) makes it a method clause, satisfied by evidence at least as strong as the method named, and the
ordering 2.3(d) states (observed operation at least as strong as modelling) places a specification or a model below
observed behaviour. The Paper defines the method (section 7.3, Method 2 and its Validation Standard): self-reported
autonomy compared with observed indicators (more selective job changes, relocation for preference rather than
necessity, education continued without income pressure, business formation) and accepted as valid when the two
correlate at r > 0.65 across validation samples, consistently across age cohorts and cultural groups. (3) *Score*
against the first reading: observed behaviour of a population the entry serves, tested against its self-reported
autonomy. For a design, a component precedent's observed behaviour calibrates confidence in the component (protocol
4.1) and validates the clause only if it tests the rationale's self-reported share against behaviour. (4)
*Alternative rejected:* crediting a design's specified removal of survival compulsion as validation. Clause 1's
self-report claim already rests on that specification, and clause 2 exists to test it; crediting it would make the
clause a test that cannot fail (part (b1), reading 3.1). *Applied* to all five units, read alike with part (a)'s three
(Nordic Social Democracy, Market Socialism, Universal Basic Income), whose clause 2 was not shown. The closest
component evidence located, OpenResearch's randomised unconditional cash study, is set out in CCO-PTF-CIP-SZH's unit.

**3.4 C3.2, clause 2: the stress test.** (1) *For a configured national economy* the documented episode is the 2021-23
inflation shock: global inflation averaged 8.7% in 2022 (IMF), the clause's external 8%. The clause is read on headline
consumer price inflation for the whole economy (protocol 3.2), with a core measure as a sensitivity, and is short where
inflation stayed above 5% through the episode. (2) *Where the inflation came from does not change the reading.* The
clause asks that inflation be held to 5% in that environment, and inflation generated at home misses it no less than
inflation imported; economies that held inflation under 5% in the same months (Switzerland, 2.9% in October 2022)
show the bar was attainable. (3) *For a design*, part (b3)'s reading 3.1 applies: an estimate under a stated
external-inflation scenario, from a run of its published model or a projection its sources state; a structural claim
(no money supply; indicative prices iterated to balance) is not one. (4) *Integral is read alike with Fully Automated
Luxury Communism's clause 2 in part (a)*, not shown. A moot reading, that a system without currency has no price level
for external inflation to reach, is not open to it: the corpus's own review of Integral records that nodes procure
from traditional markets during transition, and part (a) did not read Fully Automated Luxury Communism's "price
instability becomes moot" as moot either. *Clause 3 for Status Quo and Nordic Social Democracy* is not estimated:
whether rate-setting by a monetary policy committee is "automatic adjustment" (the Requirement asks for "specific,
tested mechanisms"; the mechanisms listed include "rates adjust based on inflation data") is Report v2.0's question.

**3.5 Bands with no corpus unit, and a finding.** Part (b3)'s reading 3.5 is applied alike to every 1.0 band the pass
leaves with no corpus unit at its value: C2.1's (its example, Universal Basic Income, moved in part (a); its last
corpus 1.0s move here) and, found by a check this group adds, C2.3's and C2.4's (left empty by part (b1)) and C3.1's
(by part (b2)), besides C1.1's (part (b3)). When the pass is applied, each keeps its description, drops its example,
and records the change in `criteria.json`'s `source.corrections`. C3.2's 1.0 example, Participatory Economics, is a
seventh example the pass moves; its band keeps three corpus 1.0s (CCO-PTF-CIP-SZH, State Capitalism / China, State
Capitalism / Singapore), so a replacement exists. Part (b3) required the v2.0 documents to state that no scored system
clears C1.1; the same finding now covers five criteria (section 6, item 1).

## 4. The units

### 4.1 Summary (generated)

| Entry | Criterion | Clauses | Verdict | Flag |
|---|---|---|---|---|
| SQ | C3.2 | C S U | 1.0 → 0.5 |  |
| NSD | C3.2 | C S U | 1.0 → 0.5 |  |
| DG | C2.1 | C U | 1.0 → 0.5 |  |
| FALC | C1.4 | U U | 1.0 → 0.5 |  |
| FALC | C2.1 | C U | 1.0 → 0.5 |  |
| PE | C1.4 | C U | 1.0 → 0.5 |  |
| PE | C2.1 | C U | 1.0 → 0.5 |  |
| PE | C3.2 | C U C | 1.0 → 0.5 |  |
| CCO | C2.1 | C U | 1.0 → 0.5 |  |
| INT | C2.1 | C U | 1.0 → 0.5 |  |
| INT | C3.2 | C U C | 1.0 → 0.5 |  |

Clause statuses are listed in Appendix B's order: C cleared, S short, U not shown, R out of reach, M moot.

### 4.2 Clause by clause (generated)

#### SQ C3.2 Inflation Control Mechanisms: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Long-term inflation ≤3% | cleared | maintains long-term inflation around 2-3% target | as audited (the unit's own text) |
| 2 | stress test inflation ≤5% (when external 8%) | short | the 2021-23 shock is the documented stress episode, with global inflation averaging 8.7% in 2022: US consumer prices rose 7.0% over 2021, 8.5% in the year to March 2022 and 9.1% in the year to June 2022, the largest twelve-month rise since 1981; prices excluding food and energy rose 6.6% in the year to September 2022, so the bar is missed on the core measure as well (reading 3.4) | IMF, World Economic Outlook Update (July 2023); BLS, CPI news releases for March and June 2022; BLS, The Economics Daily, CPI 2021 in review (14 January 2022) and CPI to September 2022 |
| 3 | automatic adjustment preventing runaway inflation | not shown | not estimated in this pass; the verdict is fixed by clause 2 (whether rate-setting by the Federal Open Market Committee is automatic adjustment is left to Report v2.0) | — |

#### NSD C3.2 Inflation Control Mechanisms: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Long-term inflation ≤3% | cleared | Successfully maintained low inflation (2-3%) over decades | as audited (the unit's own text) |
| 2 | stress test inflation ≤5% (when external 8%) | short | in the same episode every Nordic economy ran HICP inflation above 5% in every month from May to October 2022; in October Denmark stood at 11.4%, Sweden 9.8%, Finland 8.4%, Norway 8.4% and Iceland 6.4%, against 10.6% in the euro area and 2.9% in Switzerland, which shows the 5% bar was attainable in that environment (reading 3.4) | Eurostat, euro indicators release 130/2022 (17 November 2022); IMF, World Economic Outlook Update (July 2023) |
| 3 | automatic adjustment preventing runaway inflation | not shown | not estimated in this pass; the verdict is fixed by clause 2 | — |

#### DG C2.1 Freedom from Coercion: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥70% report genuine autonomy in major life decisions | cleared | provide genuine autonomy in how to spend time | as audited (the unit's own text) |
| 2 | validated through revealed preference showing acceptance of initially refused employment/living situations when alternatives exist | not shown | universal basic services, reduced working hours and commons access are specified; no observed behaviour of a population the design serves, or of one a component serves, is compared with self-reported autonomy (reading 3.3) | Report v1.6, DG C2.1 |

#### FALC C1.4 Automation Resilience: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Poverty <8% | not shown | the rationale states the design's premise, an economy in which human labour is optional; no poverty level under a 30%, 50% or 70% displacement scenario is stated or cited, and none is located in the design's literature (reading 3.2) | Report v1.6, FALC C1.4 |
| 2 | aggregate demand >85% baseline | not shown | no level of aggregate demand under any displacement scenario is stated or cited (reading 3.2) | Report v1.6, FALC C1.4 |

#### FALC C2.1 Freedom from Coercion: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥70% report genuine autonomy in major life decisions | cleared | Post-scarcity eliminates economic coercion entirely | as audited (the unit's own text) |
| 2 | validated through revealed preference showing acceptance of initially refused employment/living situations when alternatives exist | not shown | the rationale rests on post-scarcity abundance, which has no implementation whose participants' behaviour could be observed; no behavioural validation is stated or located (reading 3.3) | Report v1.6, FALC C2.1 |

#### PE C1.4 Automation Resilience: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Poverty <8% | cleared | while maintaining consumption access | as audited (the unit's own text) |
| 2 | aggregate demand >85% baseline | not shown | remuneration by effort and sacrifice, with an average income for those who cannot work, is specified, and the rationale says the gains of automation could be distributed through reduced hours; no level of consumption or demand under a 30%, 50% or 70% displacement scenario is stated or cited, and none is located in the model's literature (reading 3.2) | Report v1.6, PE C1.4; Albert, Summarizing Participatory Economics, ZNetwork (31 August 2022) |

*Note:* the audit read the rationale's "consumption access" as its poverty clause; read as demand instead, it is a design statement, not a level under a stated scenario, so the verdict is the same.

#### PE C2.1 Freedom from Coercion: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥70% report genuine autonomy in major life decisions | cleared | eliminates both market and state coercion | as audited (the unit's own text) |
| 2 | validated through revealed preference showing acceptance of initially refused employment/living situations when alternatives exist | not shown | consumption councils and democratic planning are specified; no implementation of the model as specified is cited or located, so no participants' behaviour validates the self-reports (reading 3.3) | Report v1.6, PE C2.1 |

#### PE C3.2 Inflation Control Mechanisms: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Long-term inflation ≤3% | cleared | prevents systemic price instability | as audited (the unit's own text) |
| 2 | stress test inflation ≤5% (when external 8%) | not shown | facilitation boards adjusting indicative prices through the iteration process are specified; no estimate of inflation under an external 8% scenario is stated or cited, and the clause applies because the design keeps indicative prices (reading 3.4) | Report v1.6, PE C3.2 |
| 3 | automatic adjustment preventing runaway inflation | cleared | adjusting indicative prices to balance supply/demand | as audited (the unit's own text) |

#### CCO C2.1 Freedom from Coercion: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥70% report genuine autonomy in major life decisions | cleared | Modeling shows 75%+ report genuine autonomy | as audited (the unit's own text) |
| 2 | validated through revealed preference showing acceptance of initially refused employment/living situations when alternatives exist | not shown | no validation of the design's self-reported share by observed behaviour is stated or cited; the closest component evidence, OpenResearch's randomised study of $1,000 a month for three years to 1,000 low-income adults (control group $50 a month), found recipients' unemployment spells about a month longer with fewer applications, job seekers 5.5 points more likely to require interesting or meaningful work, and more moves of home and neighbourhood, which is behaviour of the kind the Paper's method names, but it reports no self-reported autonomy share and no correlation between self-report and behaviour (reading 3.3) | Report v1.6, CCO C2.1; Vivalt et al., The Employment Effects of a Guaranteed Income, NBER Working Paper 32719 (2024); OpenResearch, Key Findings: Employment (2024) |

*Note:* the pilot calibrates confidence in the unconditional component (protocol 4.1); it does not estimate the design. The rationale's 75% figure is stated neither by the design's published model, which computes no autonomy measure, nor by any research-hub document (section 6).

#### INT C2.1 Freedom from Coercion: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥70% report genuine autonomy in major life decisions | cleared | 70%+ genuine autonomy in major life decisions is plausible | as audited (the unit's own text) |
| 2 | validated through revealed preference showing acceptance of initially refused employment/living situations when alternatives exist | not shown | democratic governance, cooperative production and transparent reciprocity are specified; no implementation's observed behaviour is cited or located (reading 3.3) | Report v1.6, INT C2.1 |

#### INT C3.2 Inflation Control Mechanisms: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Long-term inflation ≤3% | cleared | there is no money supply to inflate | as audited (the unit's own text) |
| 2 | stress test inflation ≤5% (when external 8%) | not shown | the rationale's structural claim (no currency; demand matched to capacity by assessment) is not an estimate under an external 8% scenario; the corpus's own review of Integral records that nodes procure from traditional markets during transition and asserts that external inflation is isolated through sectoral boundaries, a mechanism the design does not specify and no source estimates; read alike with Fully Automated Luxury Communism's clause 2 in part (a) (reading 3.4) | Report v1.6, INT C3.2; Integral_NEEC_Review.md, C3.2; NEEC_Rescoring_s37.md, FALC C3.2 |
| 3 | automatic adjustment preventing runaway inflation | cleared | matched to capacity through COS | as audited (the unit's own text) |

## 5. What parts (a) and (b) so far change (generated)

| Entry | Published (rank) | After (a) | After (b1) | After (b2) | After (b3) | After this group (rank) | Change here | Failures | Tier | D28 units left | Floor if all fall |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| CCO | 24.5 (1) | 24.0 | 22.5 | 22.0 | 21.5 | 21.0 (1) | -0.5 | 0 | Potentially Adequate | 6 | 18.0 |
| PE | 20.5 (2) | 20.5 | 19.0 | 18.5 | 18.0 | 16.5 (2) | -1.5 | 1 | Potentially Adequate | 5 | 14.0 |
| NSD | 19.5 (3) | 17.0 | 16.0 | 15.5 | 15.0 | 14.5 (5) | -0.5 | 2 | Potentially Adequate | 3 | 13.0 |
| INT | 19.5 (3) | 19.0 | 18.0 | 17.5 | 17.5 | 16.5 (2) | -1.0 | 3 | Partially Adequate | 6 | 13.5 |
| DG | 19.0 (5) | 19.0 | 17.5 | 17.0 | 16.5 | 16.0 (4) | -0.5 | 2 | Potentially Adequate | 5 | 13.5 |
| MS | 16.5 (6) | 15.5 | 14.0 | 13.5 | 13.0 | 13.0 (8) | 0.0 | 2 | Potentially Adequate | 0 | 13.0 |
| MMT | 15.5 (7) | 14.0 | 13.0 | 12.5 | 12.0 | 12.0 (13) | 0.0 | 3 | Partially Adequate | 1 | 11.5 |
| UBI | 14.5 (8) | 13.0 | 12.5 | 12.0 | 11.5 | 11.5 (15) | 0.0 | 7 | Structurally Inadequate | 1 | 11.0 |
| MC | 14.5 (8) | 14.5 | 13.5 | 13.0 | 13.0 | 13.0 (8) | 0.0 | 3 | Partially Adequate | 2 | 12.0 |
| OS | 14.5 (8) | 14.0 | 14.0 | 14.0 | 14.0 | 14.0 (6) | 0.0 | 3 | Partially Adequate | 2 | 13.0 |
| SWF | 14.0 (11) | 14.0 | 14.0 | 13.5 | 13.5 | 13.5 (7) | 0.0 | 3 | Partially Adequate | 2 | 12.5 |
| SG | 14.0 (11) | 13.0 | 12.5 | 12.0 | 12.0 | 12.0 (13) | 0.0 | 4 | Partially Adequate | 0 | 12.0 |
| GEO | 13.5 (13) | 13.0 | 13.0 | 13.0 | 13.0 | 13.0 (8) | 0.0 | 2 | Potentially Adequate | 1 | 12.5 |
| UBS | 13.5 (13) | 13.5 | 13.0 | 12.5 | 12.5 | 12.5 (11) | 0.0 | 3 | Partially Adequate | 1 | 12.0 |
| IF | 13.5 (13) | 12.5 | 12.5 | 12.5 | 12.5 | 12.5 (11) | 0.0 | 5 | Partially Adequate | 2 | 11.5 |
| FALC | 13.0 (16) | 12.5 | 12.0 | 12.0 | 11.5 | 10.5 (16) | -1.0 | 10 | Structurally Inadequate | 3 | 9.0 |
| DE | 11.5 (17) | 11.0 | 10.5 | 10.5 | 10.5 | 10.5 (16) | 0.0 | 8 | Structurally Inadequate | 3 | 9.0 |
| SQ | 10.5 (18) | 10.0 | 10.0 | 10.0 | 10.0 | 9.5 (18) | -0.5 | 9 | Structurally Inadequate | 0 | 9.5 |
| CPS | 10.0 (19) | 8.5 | 8.5 | 8.5 | 8.0 | 8.0 (21) | 0.0 | 12 | Structurally Inadequate | 1 | 7.5 |
| SC | 10.0 (19) | 10.0 | 9.0 | 9.0 | 9.0 | 9.0 (20) | 0.0 | 9 | Structurally Inadequate | 1 | 8.5 |
| CN | 10.0 (19) | 10.0 | 10.0 | 9.5 | 9.5 | 9.5 (18) | 0.0 | 8 | Structurally Inadequate | 0 | 9.5 |
| QA | 9.0 (22) | 8.5 | 8.5 | 8.0 | 8.0 | 8.0 (21) | 0.0 | 10 | Structurally Inadequate | 0 | 8.0 |
| LM | 8.0 (23) | 6.5 | 6.5 | 6.5 | 6.5 | 6.5 (23) | 0.0 | 15 | Structurally Inadequate | 2 | 5.5 |

"D28 units left" counts the entry's units still to be re-estimated in part (b); "Floor if all fall" is the total if
every one of them became 0.5.

After this group the corpus has 18 dominance pairs against 18 after part (b3) (new: IF>SQ; lost: PE>CN), and its frontier holds 12 entries against 12 (NSD, MS, UBI, DG, FALC, PE, CCO, INT, MC, SWF, IF, OS). First place: CCO, 21.5 after part (b3), 21.0 now. Across parts (a) and (b1) to (b4), 98 units have been re-estimated: 6 stand and 92 become 0.5 (46.0 points).

Left for part (b): 47 D28 units (C2.5 10, C3.5 2, C4.1 8, C4.2 6, C4.3 6, C4.4 4, C4.5 3, C5.2 4, C5.4 2, C5.5 2).

After this group, the entries scoring 1.0 on this group's criteria are: C1.4, 2 (UBI, CCO); C2.1, 0; C3.2, 3 (CCO, CN, SG). Every criterion had a 1.0 in the published corpus; after the pass so far no entry scores 1.0 on 5 of them: C1.1 (emptied in part (b3)), C2.1 (emptied in part (b4)), C2.3 (emptied in part (b1)), C2.4 (emptied in part (b1)), C3.1 (emptied in part (b2)).

Flags added in this group: 0; removed: 0. Across the pass so far, 14 entries' flag registers change (CCO, CN, CPS, IF, LM, MC, NSD, OS, QA, SG, SQ, SWF, UBI, UBS).

Anchor examples citing a unit the pass moves: C1.1's 1.0 example, NSD (part (b3), to 0.5); C2.1's 1.0 example, UBI (part (a), to 0.5); C2.3's 1.0 example, DG (part (b1), to 0.5); C2.4's 1.0 example, PE (part (b1), to 0.5); C3.1's 1.0 example, UBI (part (b2), to 0.5); C3.2's 1.0 example, PE (part (b4), to 0.5); C5.1's 1.0 example, MS (part (b2), to 0.5). When the pass is applied, each band needs an example the corpus then scores at that value; C1.1's 1.0, C2.1's 1.0, C2.3's 1.0, C2.4's 1.0, C3.1's 1.0 bands have none left (reading 3.5; section 6).

## 6. Corrections found (not polish)

1. **Part (b3)'s record and Handoff 40: C1.1 was not the first criterion left with no 1.0.** `NEEC_Rescoring_s40.md`
   (reading 3.5 and section 6, item 3) and Handoff 40 (section 2.3(3)) call C1.1's 1.0 band the first left with no
   corpus unit at its value. Part (b1) had already left C2.3's and C2.4's 1.0 bands with none, and part (b2) C3.1's;
   the earlier scripts counted moved examples, not remaining units, and this group's script checks both. The earlier
   records are not edited (each part edits none of the others); this record corrects them. *Consequence:* part (b3)'s
   finding that "no scored system clears C1.1" becomes: after the pass so far, no scored system clears five criteria
   (C1.1, C2.1, C2.3, C2.4 and C3.1), although every criterion had at least one 1.0 in the published corpus, and three
   of the five are in Domain 2. Report v2.0's and Paper v2.0's comparative sections state this and why: for C1.1, no
   rationale estimated poverty under stress (part (b3), reading 3.1); for C2.1, none validated autonomy by revealed
   preference (reading 3.3); for C2.3 and C2.4, the outcome levels were institutions specified without an estimated
   level (part (b1), reading 3.5); for C3.1, no entry specifies an automatic rule raising support per covered person at
   least one for one with crisis severity (part (b2), reading 3.3).
2. **Report v1.6, CCO-PTF-CIP-SZH C2.1**, says "Modeling shows 75%+ report genuine autonomy". The design's published
   model (`harness.js` and `index.html` at `cd0ceec`) computes no autonomy or coercion measure, and no document of the
   research hub at `8e8a6ba` states the figure. It is carried as audited, since silence is not contradiction, but it is
   unsourced, in the same class as part (a)'s correction 3 (Universal Basic Income's C2.1 figure). Report v2.0 sources
   it or removes it.
3. **C1.4's Pass Threshold and Measurement line differ.** The threshold asks for poverty under 8% and demand above 85%
   of baseline across all three scenarios; the Measurement line asks for poverty under 5%, 7% and 10% and demand of
   90-110%, 85-110% and 80-110% at 30%, 50% and 70% displacement. The threshold governs (2.3): it is stricter than the
   Measurement line at 70% displacement, looser at 30% and 50%, and sets no upper bound on demand. Protocol 2.3 asks
   that such a gap be flagged rather than resolved silently; it decides no unit in this group. Paper v2.0 aligns the
   two lines or states which governs.
4. **Report v1.6, Status Quo and Nordic Social Democracy C3.2**, score 1.0 on long-run records, Status Quo's text
   expressly "during normal conditions", without the 2021-23 episode that tests the stress clause. Report v2.0 states
   that record against the clause.

*Polish, optional:* C2.1's clause 2 wording ("acceptance of initially refused employment/living situations when
alternatives exist") does not match the method the Paper itself sets out for it (section 7.3: self-reports correlated
with behavioural indicators). Paper v2.0 could align the wording; the Pass Threshold is scored as written.

## 7. Disclosure

CCO-PTF-CIP-SZH is the owner's design. Its C2.1 falls here on the same reading as the other four designs (reading 3.3).
The component evidence most favourable to it, a large randomised study of unconditional cash, was searched for and is
reported in its unit; it shows behaviour of the kind the method names but tests no self-reported share. Its one
unsourced figure is recorded as a correction (section 6, item 2). No simulation run is used in this group, because the
design's published model has no autonomy measure. The second pilot, with a replicator outside the Claude family, is the
independent test of these calls.

## 8. What remains

- **(b), continued:** the 47 D28 units of section 5's line "Left for part (b)", criterion by criterion; C2.5 next (10
  units, reading 3.1), then C3.5, C4.1-C4.5, C5.2, C5.4 and C5.5.
- **(c)** the 131 mechanism-class 0.5s against D29, Ostrom's C4.3 first; **(d)** D31's source for Ostrom's community
  land trusts; **(e)** the Islamic finance and Ostrom documents' quoted thresholds restated.

When the pass ends, its changes are applied by generator, and the corpus, CSV, `README.md` and Appendix A.4 are
regenerated; the changed flag registers are recomputed; the seven anchor examples the pass moves are replaced or, for
the five 1.0 bands left with no corpus unit, removed (reading 3.5); the protocol's statements about the corpus are
restated; and the claims and protocol verifiers and the five rescoring scripts get successors.

## 9. What this record does not show

It is one scorer's re-estimation, on evidence located in one session through web search, the entries' own rationales,
the corpus's review of Integral and the design's research-hub sources and published model. "Not shown" means no
evidence was located, not that the clause fails. Every unit in this group fell on a clause no rationale estimated: C1.4
under displacement, C2.1 by revealed preference, C3.2 under stress. A scoring document that supplies the estimate, at
the entry's evidentiary tier, reopens its unit. The two short clauses rest on official statistics for one episode; a
different stress episode could be argued, and the record names the one it uses. Whether these calls reproduce is what
the replication programme tests.
