# NEEC Rescoring Pass — Record, Part (b), First Group: C3.4, C5.3, C2.4, C1.3 and C2.3

**Session 38 · 2026-09-22 · Scorer and engineer: Claude · Owner: Duke Johnson**
**Status: scratch (protocol 10.1). Part (a) is `NEEC_Rescoring_s37.md`; this record continues the pass and does not
edit it.** No corpus file, score or scoring document changes until the pass ends. Its changes are then applied by
generator with pinned inputs and restated in place (protocol 10.2, 10.3; decisions D12, D14), and until then the
published totals stand, provisional as `README.md` says. Decisions taken here are Claude's under the owner's
delegation (Handoff 35, section 2); each is recorded with its reasons, and the owner may reverse any of them.
**Reproduce:** `python3 rescoring_s38.py` (harness check 81). The script holds every clause estimate below, checks
the group against the R4 audit's register and every verdict against D28, computes every figure in sections 5 and 6
cumulatively with part (a), and checks that this record contains its generated tables verbatim. The simulation runs
of section 5 come from `node cco_simulation_checks_s38.js`, run on the Compassionism Simulation's own engine at a
pinned commit (3.2).

---

## 1. What this group is

Part (b) re-estimates the 101 units of D28's population that part (a) did not, criterion by criterion, so that one
criterion's clauses are read alike across the corpus (protocol 5). Handoff 37 orders the criteria whose clause
readings part (a) fixed first. This group is all of their part (b) units: C3.4 (10), C5.3 (6), C2.4 (6), C1.3 (1)
and C2.3 (6), 29 in all. Section 3.4 of part (a) supplies the readings of C3.4's clauses 2 and 4, C2.4, C1.3's
clause 2 and C2.3's clause 1; section 3 below adds five readings the group needed.

Two stand: Market Socialism's C3.4, on Mondragon's record, and Universal Basic Services' C5.3, on Canada's childcare
expansion, flagged with 0.5 as its alternative. Twenty-seven become 0.5 (13.5 points). No failure count and no tier
changes.

## 2. How a clause is recorded, and the rule

As in part (a), section 2: each clause is cleared, short, not shown, out of reach or moot; a 1.0 stands only if
every clause is cleared or moot, and otherwise becomes 0.5 (D28, protocol 2.3). A clause the audit coded A is
carried as cleared on the unit's own text ("as audited") unless the entry's or design's own sources contradict it;
no clause in this group needed that exception, and the script asserts so. "Not estimated in this pass" marks a
clause that could not change the verdict once another was shown short or not shown.

## 3. Decisions and readings (under the delegation)

**3.1 C3.4, clause 4, for a design with no implementation record.** "Zero collapses during parameter adjustments"
asks for a record. For a design, silence is not clearance (2.3(b)) and modelling can stand for observation
(2.3(d)). *Reading:* the clause is shown only by modelling adjustments made during operation, in a model able to
represent a way an adjustment could cause a collapse. Sensitivity runs at fixed settings show the range of stable
settings, which is clause 1's subject, not transitions between them. *Alternative rejected:* accepting fixed-setting
sensitivity analysis would clear the clause for any design with a sensitivity table, by a test that cannot fail.
*Applied:* Degrowth and Participatory Economics have neither a record nor such modelling (not shown). CCO-PTF-CIP-SZH
has a published model, run in 3.2: it shows no collapse but cannot represent one, so the clause is not shown and the
unit is flagged with 1.0 as its alternative.

**3.2 A design's published model may be run by the scorer.** Protocol 4.1 makes a design's own specification the
evidence for what it specifies; a published simulation is that specification in executable form, and running it is
reproduction rather than the scorer's argument (4.3). *Conditions:* the model is pinned to a commit and a file
digest; the engine is not changed (the script only exposes functions the file already defines); the run first
reproduces the model's own documented reference figures; the settings are the model's published ones, varied only as
the design itself specifies or as the clause asks; the script and its output are kept in this repository; and the
runs count at the modelling tier (4.1). *Applied:* the Compassionism Simulation's engine, `harness.js` at
`BetterToBest/compassionism-simulation` commit `cd0ceec` (v4.15), md5 `035d1be82ab497e76a234615a04c0ce9`, which its
own CONTRIBUTING.md confirms reproduces `index.html` v4.15. *Limitation:* the harness here cannot rerun the
JavaScript, since the simulation's source is not in this repository; `rescoring_s38.py` checks the captured output's
engine digest and reference run and that this record quotes its tables verbatim, and anyone can rerun it against a
clone at `cd0ceec`. The owner told the scorer in this session that the simulation and its research are being
calibrated and updated, with the open goal of finding parameter configurations that deliver the best welfare outcomes
across all points at once. That is why every run is pinned: a later version can reopen a unit, as section 9 says.

**3.3 C5.3, clause 4: coordination.** The clause is moot (D28(e)) only where the entry's own text establishes that
coordination across jurisdictions is not needed, as Mutual Credit's does. Doughnut Economics is adopted city by city,
but its ecological ceiling is planetary, so its text does not establish that; the moot reading does not transfer, and
no protocol was located (not shown). Intergovernmental agreements that coordinate a component's deployment across
jurisdictions are coordination protocols: Universal Basic Services' childcare sector scaled from Quebec to Canada
under bilateral agreements with every province and territory (cleared). That unit is flagged with 0.5 as its
alternative, because the protocols cover one sector, not the seven-sector package.

**3.4 C5.3, clause 3, is a method clause.** "Scaling pathway validated through modeling" is satisfied by evidence at
least as strong as modelling (2.3(d)), and observed scaling is. Observed operation from sub-national to national
scale clears it (UBS's childcare, as audited). Observed operation only to a regional federation (Mondragon) or a
single city-state (Singapore), with no modelled pathway beyond it, leaves it not shown; a scale ceiling in the entry's
own evidence makes it short (Mutual Credit).

**3.5 Outcome clauses of C2.3 and C2.4 for designs.** Weekly creative engagement, meaning or purpose satisfaction,
the share of citizen proposals adopted and satisfaction with responsiveness are outcome levels. A design's
specification of an institution — assemblies, councils, a digital portal, reduced hours — is not an estimate of the
level, and a projected relative increase with no base level is not one either. Without a modelled or component-
calibrated estimate the clause is not shown (4.1). *Applied* to Market Socialism (on its components), Degrowth,
Fully Automated Luxury Communism, Participatory Economics, CCO-PTF-CIP-SZH and Integral.

**3.6 A question about CCO-PTF-CIP-SZH's C5.3, raised and resolved.** Its rationale says the system is viable at 30%
participation, while the simulation's documents call 55% the minimum viable or critical participation rate (the
research-hub copy of the simulation's README, v3.3; the reference-configuration table in CONTRIBUTING.md; the in-app
sensitivity guidance). The unit's clauses are all addressed, so it is outside D28's population. The engine settles
it: the 55% constant is read only to issue a warning, no dynamic changes there, and at 30% participation wealth
poverty is below the baseline in 100 of 100 seeds, with results varying smoothly across 30% to 78% (section 5, run
1). The rationale is supported and the unit stays at 1.0, outside the pass. The inconsistency in the simulation's own
documents is a note for its maintainers (section 7), not a NEEC correction.

**3.7 D31: MMT + Job Guarantee's C2.4 stays out of reach.** Participation, the adoption of citizen proposals and
satisfaction with responsiveness are properties of the political system, and no source was located in the
job-guarantee literature that places democratic institutions inside the guarantee's design. Session 35's reach coding
is confirmed; the unit is 0.5.

## 4. The units

### 4.1 Summary (generated)

| Entry | Criterion | Clauses | Verdict | Flag |
|---|---|---|---|---|
| NSD | C1.3 | C S | 1.0 → 0.5 |  |
| NSD | C3.4 | C C C S | 1.0 → 0.5 |  |
| MS | C2.3 | U C U | 1.0 → 0.5 |  |
| MS | C2.4 | C U U | 1.0 → 0.5 |  |
| MS | C3.4 | C C C C | 1.0 → 1.0 |  |
| MS | C5.3 | C C U U | 1.0 → 0.5 |  |
| MMT | C2.4 | R R R | 1.0 → 0.5 |  |
| MMT | C3.4 | C U U U | 1.0 → 0.5 |  |
| UBI | C3.4 | C S C U | 1.0 → 0.5 |  |
| DG | C2.3 | U C U | 1.0 → 0.5 |  |
| DG | C2.4 | C U U | 1.0 → 0.5 |  |
| DG | C3.4 | C C C U | 1.0 → 0.5 |  |
| SC | C3.4 | C U S U | 1.0 → 0.5 |  |
| SC | C5.3 | C C U U | 1.0 → 0.5 |  |
| FALC | C2.3 | C C U | 1.0 → 0.5 |  |
| PE | C2.3 | U C U | 1.0 → 0.5 |  |
| PE | C2.4 | C U U | 1.0 → 0.5 |  |
| PE | C3.4 | C C C U | 1.0 → 0.5 |  |
| CCO | C2.3 | U C U | 1.0 → 0.5 |  |
| CCO | C2.4 | C U U | 1.0 → 0.5 |  |
| CCO | C3.4 | C C C U | 1.0 → 0.5 | alternative 1.0 |
| INT | C2.3 | C C U | 1.0 → 0.5 |  |
| INT | C2.4 | C U U | 1.0 → 0.5 |  |
| MC | C3.4 | C U U C | 1.0 → 0.5 |  |
| MC | C5.3 | C C S M | 1.0 → 0.5 |  |
| DE | C5.3 | C C C U | 1.0 → 0.5 |  |
| UBS | C3.4 | C S U U | 1.0 → 0.5 |  |
| UBS | C5.3 | C C C C | 1.0 → 1.0 | alternative 0.5 |
| SG | C5.3 | C C U C | 1.0 → 0.5 |  |

Clause statuses are listed in Appendix B's order: C cleared, S short, U not shown, R out of reach, M moot.

### 4.2 Clause by clause (generated)

#### NSD C1.3 Housing Security: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥88% housing stability over 5-year periods | cleared | about 90% or more housing stability | as audited (the unit's own text) |
| 2 | maintaining affordability at 80% area median income | short | housing cost overburden (housing costs above 40% of disposable income) in 2024: Denmark 14.6% and Sweden 10.6%, among the highest rates in the EU; in Denmark's lowest income quintile, whose incomes fall below 80% of the median, the rate ranges from 44.6% to 60.4% across the EU-SILC series | Eurostat, Living conditions in Europe: housing (2024 data, ilc_lvho07a); Eurostat ilc_lvho07b, via DBnomics |

#### NSD C3.4 Epistemic Adaptability: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥30% parameter adjustability range | cleared | willing to adjust parameters based on research and outcomes | as audited (the unit's own text) |
| 2 | policy updates within 6 months of evidence | cleared | frequent policy experimentation and evaluation | as audited (the unit's own text) |
| 3 | democratic governance for changes | cleared | parameter changes are enacted by elected parliaments (the national turnouts of part (a), NSD C2.4) | IDEA Voter Turnout Database; Valmyndigheten, 2022 results |
| 4 | zero collapses during parameter adjustments | short | the financial liberalisation of the 1980s led to systemic banking crises in Finland, Norway and Sweden, among the deepest in advanced economies since the Second World War, with Finland's output falling nearly 15%; Denmark, whose supervision was tightened, avoided a systemic crisis | Honkapohja, Bank of Finland Research Discussion Paper 36/2012; Anderson, Federal Reserve Bank of St. Louis Economic Synopses 2009, no. 10 |

*Note:* the liberalisation changed the configuration's own credit parameters (lending ceilings, interest and capital controls), which is what clause 4 asks about; the welfare state's functions continued, but the clause asks for zero collapses, and a systemic banking crisis is one.

#### MS C2.3 Creative Development Opportunities: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥50% regular creative engagement | not shown | Mondragon's training and education time bears on opportunity; no weekly creative-engagement figure located (reading 3.5) | — |
| 2 | average 10+ hours weekly on non-subsistence pursuits | cleared | sabbaticals and education time | as audited (the unit's own text) |
| 3 | meaning/purpose satisfaction scores ≥70/100 | not shown | not estimated in this pass; the verdict is fixed by another clause | — |

#### MS C2.4 Democratic Participation: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥70% participation in democratic processes | cleared | 75-85% participation in cooperative governance | as audited (the unit's own text) |
| 2 | ≥35% citizen proposals adopted | not shown | no adoption share of member-initiated proposals located for Mondragon or other cooperative networks | — |
| 3 | ≥65% satisfaction with responsiveness | not shown | not estimated in this pass; the verdict is fixed by another clause | — |

#### MS C3.4 Epistemic Adaptability: 1.0 → 1.0

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥30% parameter adjustability range | cleared | the pay-ratio cap, a core distributive parameter, moved from 1:3 at founding to 1:4.5 in the 1970s and 1:6 in 1988, a 100% range | Co-operative News, Co-operative approaches to pay (thenews.coop) |
| 2 | policy updates within 6 months of evidence | cleared | democratic governance enables rapid adaptation to evidence | as audited (the unit's own text) |
| 3 | democratic governance for changes | cleared | the pay-ratio changes were decided at the cooperatives' General Assemblies | Co-operative News (thenews.coop); Report v1.6, MS C3.4 |
| 4 | zero collapses during parameter adjustments | cleared | stated search: no collapse caused by a parameter adjustment located; Fagor Electrodomesticos, the founding cooperative, failed in 2013 after heavy losses in the euro-area and Spanish real-estate crises, carrying debt from its 2005 Brandt acquisition, causes that clear it of an adjustment | Fortune (27 November 2013); The Local (14 November 2013); Mondragon Annual Report 2013 |

*Note:* clause 2 rests on the unit's own text, as part (a)'s convention carries an addressed clause; Report v2.0's clause-level Part I should time an update against the evidence that called for it.

#### MS C5.3 Partial and Parallel Deployability: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Viable at ≥30% participation | cleared | cooperatives function well in mixed economies | as audited (the unit's own text) |
| 2 | coexistence with traditional markets maintaining ≥90% economic activity | cleared | can coexist with traditional firms | as audited (the unit's own text) |
| 3 | scaling pathway validated through modeling | not shown | no modelling of a scaling pathway cited; observed cooperative scale peaks at a regional federation (Mondragon: about 70,000 workers in 92 cooperatives), short of the national stage the Measurement line describes (reading 3.4) | Reasons to Be Cheerful, via DailyGood (2026); criteria.json C5.3 (measurement) |
| 4 | coordination protocols established | not shown | not estimated in this pass; the verdict is fixed by another clause | — |

#### MMT C2.4 Democratic Participation: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥70% participation in democratic processes | out of reach | participation in democratic processes is a property of the political system; no source located in the job-guarantee literature places democratic institutions inside the guarantee's design (D31) | Session 35 reach reason, confirmed |
| 2 | ≥35% citizen proposals adopted | out of reach | the adoption of citizen proposals is a property of the political system | Session 35 reach reason, confirmed |
| 3 | ≥65% satisfaction with responsiveness | out of reach | satisfaction with responsiveness is a property of the political system | Session 35 reach reason, confirmed |

#### MMT C3.4 Epistemic Adaptability: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥30% parameter adjustability range | cleared | adjust job guarantee wage, spending levels and taxation | as audited (the unit's own text) |
| 2 | policy updates within 6 months of evidence | not shown | spending and taxation are adjusted through the legislative budget, and no update timed against the evidence that called for it was located; the one national precedent, Argentina's Jefes de Hogar, paid a fixed 150 pesos per beneficiary under decree 565/2002, the sum still stated in a 2003 amendment bill, while the programme was extended by statute to 2007 | Decreto 565/2002; Camara de Diputados bill 2938-D-03 (2003); Ley 26204; CELS, Plan Jefes y Jefas |
| 3 | democratic governance for changes | not shown | not estimated in this pass; the verdict is fixed by another clause | — |
| 4 | zero collapses during parameter adjustments | not shown | not estimated in this pass; the verdict is fixed by another clause | — |

#### UBI C3.4 Epistemic Adaptability: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥30% parameter adjustability range | cleared | simple parameter adjustment (benefit level, taxation rates) | as audited (the unit's own text) |
| 2 | policy updates within 6 months of evidence | short | the longest-running precedent, Alaska's dividend, is set once a year; since the 2017 Supreme Court ruling it competes for annual funding like other programmes; the 2018 percent-of-market-value law came in the third budget year of the deficit that prompted the 2016 veto: annual cycles fall short | Alaska Public Media (6 May 2022); Anchorage Daily News (4 October 2018; 11 October 2022); Petroleum News (13 May 2018) |
| 3 | democratic governance for changes | cleared | changes enacted by the legislature and governor and tested in the state Supreme Court | Courthouse News (2017); Alaska Public Media (6 May 2022) |
| 4 | zero collapses during parameter adjustments | not shown | not estimated in this pass; the verdict is fixed by another clause | — |

#### DG C2.3 Creative Development Opportunities: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥50% regular creative engagement | not shown | the design reduces working hours to 20 a week and programmes community culture; no estimate of weekly creative engagement (reading 3.5) | — |
| 2 | average 10+ hours weekly on non-subsistence pursuits | cleared | prioritises creative and social time | as audited (the unit's own text) |
| 3 | meaning/purpose satisfaction scores ≥70/100 | not shown | no meaning or purpose satisfaction estimate in the design's sources | — |

#### DG C2.4 Democratic Participation: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥70% participation in democratic processes | cleared | participatory democracy core principle | as audited (the unit's own text) |
| 2 | ≥35% citizen proposals adopted | not shown | the design specifies assemblies and consensus processes, not an estimate of the share of citizen proposals adopted; none located (reading 3.5) | — |
| 3 | ≥65% satisfaction with responsiveness | not shown | not estimated in this pass; the verdict is fixed by another clause | — |

#### DG C3.4 Epistemic Adaptability: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥30% parameter adjustability range | cleared | democratic governance allows evidence-based adjustments | as audited (the unit's own text) |
| 2 | policy updates within 6 months of evidence | cleared | decentralised experimentation enables rapid learning and adaptation | as audited (the unit's own text) |
| 3 | democratic governance for changes | cleared | democratic governance allows evidence-based adjustments | as audited (the unit's own text) |
| 4 | zero collapses during parameter adjustments | not shown | no implementation record, and no modelling of adjustments to the design's parameters in operation located in its sources (reading 3.1) | — |

#### SC C3.4 Epistemic Adaptability: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥30% parameter adjustability range | cleared | easier to adjust metrics and targets than restructure the system | as audited (the unit's own text) |
| 2 | policy updates within 6 months of evidence | not shown | not estimated in this pass; the verdict is fixed by another clause | — |
| 3 | democratic governance for changes | short | firms' metrics and targets are changed by boards under one-share-one-vote; the entry's own scoring records plutocratic control and token stakeholder voice: governed, not democratic (as Islamic finance's C3.4 in part (a)) | Report v1.6, SC C2.4 and C4.4 |
| 4 | zero collapses during parameter adjustments | not shown | not estimated in this pass; the verdict is fixed by another clause | — |

#### SC C5.3 Partial and Parallel Deployability: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Viable at ≥30% participation | cleared | partial deployment proven viable through existing examples | as audited (the unit's own text) |
| 2 | coexistence with traditional markets maintaining ≥90% economic activity | cleared | stakeholder firms coexist easily with traditional corporations | as audited (the unit's own text) |
| 3 | scaling pathway validated through modeling | not shown | the unit cites existing examples (B Corps competing in the same markets); no modelled or observed pathway from pilots to national scale located (reading 3.4) | Report v1.6, SC C5.3 |
| 4 | coordination protocols established | not shown | not estimated in this pass; the verdict is fixed by another clause | — |

#### FALC C2.3 Creative Development Opportunities: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥50% regular creative engagement | cleared | humans pursue art, science, philosophy and relationships | as audited (the unit's own text) |
| 2 | average 10+ hours weekly on non-subsistence pursuits | cleared | unlimited time and resources for creative pursuits | as audited (the unit's own text) |
| 3 | meaning/purpose satisfaction scores ≥70/100 | not shown | no meaning or purpose satisfaction estimate; the design's sources state the aim, not a level (reading 3.5) | — |

#### PE C2.3 Creative Development Opportunities: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥50% regular creative engagement | not shown | no estimate of weekly creative engagement (reading 3.5) | — |
| 2 | average 10+ hours weekly on non-subsistence pursuits | cleared | reduced hours (20-30 a week) leave substantial time for self-directed pursuits | as audited (the unit's own text) |
| 3 | meaning/purpose satisfaction scores ≥70/100 | not shown | not estimated in this pass; the verdict is fixed by another clause | — |

#### PE C2.4 Democratic Participation: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥70% participation in democratic processes | cleared | everyone participates in planning affecting them | as audited (the unit's own text) |
| 2 | ≥35% citizen proposals adopted | not shown | the plan is assembled from council proposals revised through iteration until feasible; no estimate of the share adopted, and no implementation (reading 3.5) | Report v1.6, PE C2.4 |
| 3 | ≥65% satisfaction with responsiveness | not shown | not estimated in this pass; the verdict is fixed by another clause | — |

#### PE C3.4 Epistemic Adaptability: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥30% parameter adjustability range | cleared | councils adjust proposals based on feedback | as audited (the unit's own text) |
| 2 | policy updates within 6 months of evidence | cleared | democratic structure enables rapid evidence-based changes | as audited (the unit's own text) |
| 3 | democratic governance for changes | cleared | democratic structure enables rapid evidence-based changes | as audited (the unit's own text) |
| 4 | zero collapses during parameter adjustments | not shown | no implementation record, and no modelling of adjustments to the design's parameters in operation located (reading 3.1) | — |

#### CCO C2.3 Creative Development Opportunities: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥50% regular creative engagement | not shown | the design projects relative increases for its case studies (60% more cultural-event participation; 32% more creative output), not a level of weekly engagement (reading 3.5) | research-hub at 8e8a6ba (2026-09-21), cultural-value-integration.html (section 6) |
| 2 | average 10+ hours weekly on non-subsistence pursuits | cleared | time and resources for non-subsistence activities | as audited (the unit's own text) |
| 3 | meaning/purpose satisfaction scores ≥70/100 | not shown | no meaning or purpose satisfaction estimate located in the design's documents | — |

#### CCO C2.4 Democratic Participation: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥70% participation in democratic processes | cleared | as audited; the design's documents give 15-25% as the portal's pilot success metric and model participation rising from 55% to 85% at maturity | research-hub at 8e8a6ba (2026-09-21), citizens-internet-portal.html; integrated-digital-governance.html |
| 2 | ≥35% citizen proposals adopted | not shown | any citizen may submit proposals above a signature threshold, and binding changes need a 60-67% supermajority with a geographic distribution requirement; no estimate of the share adopted (reading 3.5) | research-hub at 8e8a6ba (2026-09-21), citizens-internet-portal.html |
| 3 | ≥65% satisfaction with responsiveness | not shown | satisfaction with democratic processes is named as a metric, with no estimate | research-hub at 8e8a6ba (2026-09-21), risk-mitigation-framework.html |

#### CCO C3.4 Epistemic Adaptability: 1.0 → 0.5 — flagged as contestable

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥30% parameter adjustability range | cleared | octave caps, basic amounts (5-20% of GDP per capita), conversion multipliers and the phi-rate adjustable | as audited (the unit's own text) |
| 2 | policy updates within 6 months of evidence | cleared | the design's crisis protocol schedules parameter recalibration within one to six months, and monthly cost-of-living adjustments in an inflation surge | research-hub at 8e8a6ba (2026-09-21), integrated-implementation-roadmap.html (Appendix G) |
| 3 | democratic governance for changes | cleared | CIP enables democratic parameter adjustment | as audited (the unit's own text) |
| 4 | zero collapses during parameter adjustments | not shown | the design's own engine was run by the scorer with the Basic Unit stepped by 0.7 to 1.3 from year 10: no collapse; but prices are an exogenous input and agents do not respond to the change, so no adjustment could cause a collapse in the model, and the run cannot show the clause (readings 3.1, 3.2) | compassionism-simulation at cd0ceec (v4.15), harness.js; cco_simulation_checks_s38_output.txt |

*Flag:* alternative 1.0: the design's modelled stability across adjustments accepted at the modelling tier without requiring a channel by which an adjustment could fail.

*Note:* reopens if the simulation adds an endogenous price or behavioural channel and the adjustment run is repeated.

#### INT C2.3 Creative Development Opportunities: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥50% regular creative engagement | cleared | could exceed the 35-55% range; the comparison it rests on is unsourced (part (a), correction 3) | as audited (the unit's own text) |
| 2 | average 10+ hours weekly on non-subsistence pursuits | cleared | space for arts, culture and personal development | as audited (the unit's own text) |
| 3 | meaning/purpose satisfaction scores ≥70/100 | not shown | no meaning or purpose satisfaction estimate (reading 3.5) | — |

#### INT C2.4 Democratic Participation: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥70% participation in democratic processes | cleared | plausibly match or exceed the best documented cooperative precedents | as audited (the unit's own text) |
| 2 | ≥35% citizen proposals adopted | not shown | weighted consensus and objection mapping specified; no estimate of the share of proposals adopted (reading 3.5) | — |
| 3 | ≥65% satisfaction with responsiveness | not shown | not estimated in this pass; the verdict is fixed by another clause | — |

#### MC C3.4 Epistemic Adaptability: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥30% parameter adjustability range | cleared | clearing and settlement mechanisms adapted over nine decades | as audited (the unit's own text) |
| 2 | policy updates within 6 months of evidence | not shown | the adaptations the unit cites run over decades (WIR) and years (the Credit Commons redesign, documented through 2024-2025); no update timed against the evidence that called for it located | NEEC_MutualCredit_LETS_scoring_scratch.md, C3.4 |
| 3 | democratic governance for changes | not shown | not estimated in this pass; the verdict is fixed by another clause | — |
| 4 | zero collapses during parameter adjustments | cleared | nine decades of continuous operation | as audited (the unit's own text) |

#### MC C5.3 Partial and Parallel Deployability: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Viable at ≥30% participation | cleared | can begin with as few as a handful of participants | as audited (the unit's own text) |
| 2 | coexistence with traditional markets maintaining ≥90% economic activity | cleared | operates alongside conventional currency | as audited (the unit's own text) |
| 3 | scaling pathway validated through modeling | short | the entry's own document records a practical trust ceiling of 100-200 members per LETS node and WIR's centralisation under scale; the federated redesign meant to pass them is not yet validated | NEEC_MutualCredit_LETS_scoring_scratch.md, C3.4 and sources |
| 4 | coordination protocols established | moot | no case of adoption requiring or attempting multi-jurisdiction coordination | as audited (the unit's own text) |

#### DE C5.3 Partial and Parallel Deployability: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Viable at ≥30% participation | cleared | adopted piecemeal by voluntarily participating jurisdictions | as audited (the unit's own text) |
| 2 | coexistence with traditional markets maintaining ≥90% economic activity | cleared | coexists with the ordinary market economy | as audited (the unit's own text) |
| 3 | scaling pathway validated through modeling | cleared | the scaling record is concrete and dated | as audited (the unit's own text) |
| 4 | coordination protocols established | not shown | no inter-jurisdictional coordination protocol located in the entry's document; cities adopt the framework independently, but its ecological ceiling is planetary, so the text does not establish that coordination is unneeded and Mutual Credit's moot reading does not transfer (reading 3.3) | NEEC_DoughnutEconomics_scoring_scratch.md, C5.3 |

#### UBS C3.4 Epistemic Adaptability: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥30% parameter adjustability range | cleared | the framework's authors revising scope, framing and emphasis | as audited (the unit's own text) |
| 2 | policy updates within 6 months of evidence | short | the unit's own record is revision by the framework's authors at intervals of one to three years (2017, 2019, 2020, 2023): cycles longer than six months, as for Doughnut Economics in part (a) | NEEC_UniversalBasicServices_scoring_scratch.md, C3.4 |
| 3 | democratic governance for changes | not shown | not estimated in this pass; the verdict is fixed by another clause | — |
| 4 | zero collapses during parameter adjustments | not shown | not estimated in this pass; the verdict is fixed by another clause | — |

#### UBS C5.3 Partial and Parallel Deployability: 1.0 → 1.0 — flagged as contestable

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Viable at ≥30% participation | cleared | each of its sectors adopted independently | as audited (the unit's own text) |
| 2 | coexistence with traditional markets maintaining ≥90% economic activity | cleared | Quebec's universal low-fee childcare raised mothers' employment by nearly 70,000 (3.8% of women's employment) and provincial GDP by about 1.7% in 2008: market activity grew | Fortin, Godbout and St-Cerny (2012), Universite de Sherbrooke Working Paper 2012/02 |
| 3 | scaling pathway validated through modeling | cleared | universal childcare scaled from Quebec to all of Canada | as audited (the unit's own text) |
| 4 | coordination protocols established | cleared | Canada-wide Early Learning and Child Care agreements signed by the federal government with every province and territory by March 2022, including an asymmetrical agreement with Quebec (reading 3.3) | Employment and Social Development Canada, Question Period Notes (June 2022; June 2023) |

*Flag:* alternative 0.5: coordination protocols shown for one sector, childcare, and none for the seven-sector package.

#### SG C5.3 Partial and Parallel Deployability: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Viable at ≥30% participation | cleared | the state's share can be dialled down | as audited (the unit's own text) |
| 2 | coexistence with traditional markets maintaining ≥90% economic activity | cleared | coexists with private and foreign firms by design | as audited (the unit's own text) |
| 3 | scaling pathway validated through modeling | not shown | the record is of one city-state; the entry's own text says components transplanted abroad worked less well (China's Housing Provident Fund; the Temasek model's limited influence); no modelled pathway (reading 3.4) | NEEC_StateCapitalism_Singapore_scoring_scratch.md, C5.3 |
| 4 | coordination protocols established | cleared | enterprises operate on an equal basis with local and foreign businesses | as audited (the unit's own text) |

## 5. The simulation runs (generated from `cco_simulation_checks_s38_output.txt`)

The engine first reproduces the simulation's documented seed-42 reference run (median BLEI 1,965 days, wealth poverty
16.6%, Gini 0.534, System Stability 88.5%). Run 1 varies only the CCO participation rate in the Full Integration
reference preset; the baseline has no systems enabled.

| Configuration | Wealth poverty | BLEI poverty | System Stability |
|---|---:|---:|---:|
| Baseline (no systems) | 71.4% | 70.5% | 98.5% |
| Full Integration, participation 30% | 26.9% | 24.2% | 88.3% |
| Full Integration, participation 45% | 23.2% | 20.6% | 88.4% |
| Full Integration, participation 55% | 20.9% | 18.1% | 88.6% |
| Full Integration, participation 78% (reference) | 15.3% | 12.6% | 88.7% |

Run 2 steps the monthly Basic Unit amount by the factor shown from the start of year 10 and holds it, comparing each
seed with the unadjusted run.

| Step | Final wealth poverty, adjusted | Final wealth poverty, unadjusted | Largest one-year excess rise |
|---|---:|---:|---:|
| x0.7 | 16.0% | 15.3% | 1.4 points |
| x0.8 | 15.8% | 15.3% | 1.4 points |
| x1.2 | 14.9% | 15.3% | 1.6 points |
| x1.3 | 14.7% | 15.3% | 1.6 points |

No collapse follows any step: final wealth poverty moves by under one point, and the largest single-year excess rise
is the same size for increases as for cuts, which marks it as path noise rather than an effect of the cut. The run
cannot fail, though. Prices are an exogenous input (`inflRate`, damped by PTF and PTH adoption) and agents do not
respond to the level of the Basic Unit, so the engine has no channel through which an adjustment could cause a
collapse. The simulation's own CONTRIBUTING.md states the standard this record applies: "A regression guard that has
never been seen to fail is a claim, not a guard."

## 6. What parts (a) and (b) so far change (generated)

| Entry | Published (rank) | After part (a) (rank) | After this group (rank) | Change here | Failures | Tier | D28 units left | C5.1 clause 2 | Floor if all fall |
|---|---:|---:|---:|---:|---:|---|---:|---:|---:|
| CCO | 24.5 (1) | 24.0 (1) | 22.5 (1) | -1.5 | 0 | Potentially Adequate | 8 | 1 | 18.0 |
| PE | 20.5 (2) | 20.5 (2) | 19.0 (2) | -1.5 | 1 | Potentially Adequate | 10 | 0 | 14.0 |
| NSD | 19.5 (3) | 17.0 (5) | 16.0 (5) | -1.0 | 2 | Potentially Adequate | 5 | 1 | 13.0 |
| INT | 19.5 (3) | 19.0 (3) | 18.0 (3) | -1.0 | 3 | Partially Adequate | 9 | 0 | 13.5 |
| DG | 19.0 (5) | 19.0 (3) | 17.5 (4) | -1.5 | 2 | Potentially Adequate | 8 | 0 | 13.5 |
| MS | 16.5 (6) | 15.5 (6) | 14.0 (6) | -1.5 | 2 | Potentially Adequate | 1 | 1 | 13.0 |
| MMT | 15.5 (7) | 14.0 (8) | 13.0 (10) | -1.0 | 3 | Partially Adequate | 3 | 0 | 11.5 |
| UBI | 14.5 (8) | 13.0 (12) | 12.5 (13) | -0.5 | 7 | Structurally Inadequate | 3 | 1 | 10.5 |
| MC | 14.5 (8) | 14.5 (7) | 13.5 (9) | -1.0 | 3 | Partially Adequate | 2 | 1 | 12.0 |
| OS | 14.5 (8) | 14.0 (8) | 14.0 (6) | 0.0 | 3 | Partially Adequate | 2 | 1 | 12.5 |
| SWF | 14.0 (11) | 14.0 (8) | 14.0 (6) | 0.0 | 3 | Partially Adequate | 2 | 1 | 12.5 |
| SG | 14.0 (11) | 13.0 (12) | 12.5 (13) | -0.5 | 4 | Partially Adequate | 0 | 1 | 12.0 |
| GEO | 13.5 (13) | 13.0 (12) | 13.0 (10) | 0.0 | 2 | Potentially Adequate | 1 | 0 | 12.5 |
| UBS | 13.5 (13) | 13.5 (11) | 13.0 (10) | -0.5 | 3 | Partially Adequate | 1 | 1 | 12.0 |
| IF | 13.5 (13) | 12.5 (15) | 12.5 (13) | 0.0 | 5 | Partially Adequate | 2 | 0 | 11.5 |
| FALC | 13.0 (16) | 12.5 (15) | 12.0 (16) | -0.5 | 10 | Structurally Inadequate | 6 | 0 | 9.0 |
| DE | 11.5 (17) | 11.0 (17) | 10.5 (17) | -0.5 | 8 | Structurally Inadequate | 3 | 0 | 9.0 |
| SQ | 10.5 (18) | 10.0 (18) | 10.0 (18) | 0.0 | 9 | Structurally Inadequate | 1 | 0 | 9.5 |
| CPS | 10.0 (19) | 8.5 (21) | 8.5 (21) | 0.0 | 12 | Structurally Inadequate | 2 | 0 | 7.5 |
| SC | 10.0 (19) | 10.0 (18) | 9.0 (20) | -1.0 | 9 | Structurally Inadequate | 1 | 0 | 8.5 |
| CN | 10.0 (19) | 10.0 (18) | 10.0 (18) | 0.0 | 8 | Structurally Inadequate | 0 | 1 | 9.5 |
| QA | 9.0 (22) | 8.5 (21) | 8.5 (21) | 0.0 | 10 | Structurally Inadequate | 0 | 1 | 8.0 |
| LM | 8.0 (23) | 6.5 (23) | 6.5 (23) | 0.0 | 15 | Structurally Inadequate | 2 | 0 | 5.5 |

"D28 units left" counts the entry's units still to be re-estimated in part (b); "C5.1 clause 2" counts its C5.1 1.0s
whose second clause part (b) must still test; "Floor if all fall" is the total if every one of them became 0.5.

After this group the corpus has 14 dominance pairs against 15 after part (a) (new: IF>SC; lost: CCO>MS, CCO>SWF), and its frontier holds 13 entries against 11 (NSD, MS, MMT, UBI, DG, FALC, PE, CCO, INT, MC, SWF, IF, OS). First place: CCO, 24.0 after part (a), 22.5 now.

Left for part (b): 72 D28 units (C1.1 9, C1.4 2, C2.1 5, C2.5 10, C3.1 5, C3.2 4, C3.5 2, C4.1 8, C4.2 6, C4.3 6, C4.4 4, C4.5 3, C5.2 4, C5.4 2, C5.5 2) and C5.1's second clause on 11 1.0s (NSD, MS, UBI, CCO, MC, UBS, SWF, CN, SG, QA, OS).

Cumulatively, parts (a) and (b) have re-estimated 62 units: four stand and 58 become 0.5 (29.0 points). CCO-PTF-CIP-
SZH keeps first place at 22.5; Participatory Economics is second at 19.0 and Integral third at 18.0. No failure
count and no tier changes. Two flags are added in this group (CCO-PTF-CIP-SZH C3.4, toward 1.0; Universal Basic
Services C5.3, toward 0.5); with part (a)'s eight changes, ten entries' flag registers change, and their
enumerations and joint readings are recomputed when the pass is applied.

## 7. Corrections found (not polish)

1. **Handoff 37, section 8, item 3** gives the part (b) units of the fixed-reading criteria as C3.4 11, C5.3 8,
   C2.4 6, C1.3 3 and C2.3 6. They are 10, 6, 6, 1 and 6 (C1.3's 3 counts part (a)'s two units as well). The totals
   it states, 101 units and eleven C5.1 1.0s, are right.
2. **Integral's C2.3** compares its projection with "the 35-55% range already achieved by Nordic and cooperative
   systems". That range rests on figures part (a) found unsourced (its correction 3). Report v2.0 states a sourced
   comparison or none.
3. **For the simulation's maintainers (not a NEEC correction).** Three places describe a 55% participation threshold
   below which network effects collapse (the research-hub copy of the README, v3.3; the reference-configuration table
   in CONTRIBUTING.md; the in-app sensitivity guidance). In the engine, `CCO_MIN_PARTICIPATION` is read only to issue a
   warning, and the only 55% gate in the dynamics is the SZH synergy term, which applies to zone coherence, not to
   participation. Either the threshold is built into the dynamics or it is described as a heuristic.

*Polish, optional:* Report v2.0's CCO-PTF-CIP-SZH C5.3 can cite run 1 for "viable at 30%+" instead of asserting it.

## 8. Disclosure

CCO-PTF-CIP-SZH is the owner's design. This group reads three of its units on its own documents and model, and all
three fall (C2.3, C2.4, C3.4), one flagged toward 1.0. A fourth question (C5.3, 3.6) was resolved in the design's
favour by its own engine. It keeps first place (24.0 to 22.5). The runs of 3.2 use the owner's published engine at a
pinned commit; the decision to run a design's model applies to any entry that publishes one, and no other entry in
the corpus does. The second pilot, with a replicator outside the Claude family, is the independent test of these
calls.

## 9. What remains

- **(b), continued:** the 72 D28 units of section 6's last line, criterion by criterion, and C5.1's second clause on
  its eleven 1.0s outside D28's population; then C3.1, deciding its step-versus-scaling question (part (a), 3.4).
- **(c)** the 131 mechanism-class 0.5s against D29, Ostrom's C4.3 first; **(d)** D31's source for Ostrom's
  community land trusts; **(e)** the Islamic finance and Ostrom documents' quoted thresholds restated.

**Reopening conditions.** Nordic Social Democracy's C2.3 (part (a)): Eurostat's database was again not reachable in
this session (a fetch of its cultural-participation article returned the site's main page). CCO-PTF-CIP-SZH's C3.4:
reopens if the simulation adds an endogenous price or behavioural channel and run 2 is repeated on the new version.

When the pass ends, its changes are applied by generator, and the corpus, CSV, `README.md` and Appendix A.4 are
regenerated; the changed flag registers are recomputed, the protocol's statements about the corpus are restated, and
the claims and protocol verifiers get successors.

## 10. What this record does not show

It is one scorer's re-estimation, on evidence located in one session through web search, the entries' own scoring
documents, and the CCO design's own documents and engine. "Not shown" means no evidence was located, not that the
clause fails. Several units fall on clauses no design in the corpus estimates (3.5), which is what D28's rule
requires, not a finding that the designs would fail them. Where the evidence or the reading is divided, the unit is
flagged in the direction a careful second scorer could take: one toward 1.0 and one toward 0.5. Whether these calls
reproduce is what the replication programme tests.
