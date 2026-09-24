# NEEC Rescoring Pass — Record, Part (b), Sixth Group: C3.5 Failure-Mode Transparency and C4.1 Intergenerational Justice

**Session 43 · 2026-09-23 · Scorer and engineer: Claude · Owner: Duke Johnson**
**Status: scratch (protocol 10.1). Parts (a) and (b1) to (b5) are `NEEC_Rescoring_s37.md` to
`NEEC_Rescoring_s42.md`; this record continues the pass and edits none of them.** No corpus file, score or scoring
document changes until the pass ends. Its changes are then applied by generator with pinned inputs and restated in
place (protocol 10.2, 10.3; decisions D12, D14), and until then the published totals stand, provisional as
`README.md` says. Decisions taken here are Claude's under the owner's delegation (Handoff 35, section 2); each is
recorded with its reasons, and the owner may reverse any of them.
**Reproduce:** `python3 rescoring_s43.py` (harness check 86). The script holds every clause estimate below, checks the
group against the R4 audit's register and every verdict against D28, asserts that no clause departs from the audit's A
codes and that the audit's four out-of-reach codes stand, asserts that the four clauses left not estimated sit in units
another clause already decides, computes every figure in section 5 cumulatively with parts (a) to (b5), and checks that
this record contains its generated tables verbatim.

---

## 1. What this group is

Handoff 42 orders C3.5 next and proposes taking it with C4.1 in the same session (reading 3.1). C3.5's two part (b)
units are CCO-PTF-CIP-SZH and Integral; its third published 1.0, Centrally Planned Socialism, fell in part (a). C4.1's
eight are Degrowth Economics, Fully Automated Luxury Communism, Participatory Economics, CCO-PTF-CIP-SZH, Integral,
Doughnut Economics, Sovereign Wealth Fund Statism and Ostrom-Style Commons Governance: all eight of its published 1.0s,
across two scope classes.

What the audit found: C3.5's Pass Threshold is "Failure detection within 1 week, diagnosis success ≥80%, correction
success ≥70%, externalization <10% of total costs". Its third and fourth clauses were silent on CCO-PTF-CIP-SZH, and its
second and third on Integral. C4.1's is "35% carbon reduction by 2030, resource use ≤90% regeneration, debt-to-GDP <80%,
positive wealth transfer to next generation". No unit's text addressed the debt clause: it was silent on seven units and
coded out of reach for Ostrom. The carbon clause was silent on four and out of reach for the fund and for Ostrom; the
resource clause was silent on CCO-PTF-CIP-SZH and out of reach for the fund; the transfer clause was silent on
Participatory Economics and Doughnut Economics.

No unit stands. All ten become 0.5 (5.0 points). No failure count and no tier changes. CCO-PTF-CIP-SZH keeps first
place, 20.5 to 19.5, falling on four quantities its sources do not estimate (a correction share, an externalised share,
resource use against regeneration, a debt ratio) with no departure from the audit's codes. Participatory Economics is
second at 16.0, Degrowth third at 15.5, Integral fourth at 15.0. The dominance pairs and the frontier do not change.
Degrowth, the one unit with a single silent clause, falls on it and is flagged toward 1.0 (reading 3.5). **C3.5 and
C4.1 join the criteria no scored system clears, which are now seven** (reading 3.8).

## 2. How a clause is recorded, and the rule

As in part (a), section 2: each clause is cleared, short, not shown, out of reach or moot; a 1.0 stands only if every
clause is cleared or moot, and otherwise becomes 0.5 (D28, protocol 2.3). A clause the audit coded A is carried as
cleared on the unit's own text ("as audited") unless the entry's or design's own sources contradict it. No clause in
this group needs that exception, and the script asserts that none departs. Four clauses are marked "not estimated in
this pass": the debt clause of Fully Automated Luxury Communism, Participatory Economics and Integral, whose units a
silent carbon clause already fixes, and of Sovereign Wealth Fund Statism, whose unit two out-of-reach clauses fix. They
stay not shown, and Report v2.0's clause-level Part I must estimate them. The audit's four out-of-reach codes are
confirmed by a search for a source under D31 (reading 3.6).

## 3. Decisions and readings (under the delegation)

**3.1 The group.** Handoff 42 proposed C3.5 with C4.1 because both are small and because their clauses are outcome
levels, which part (b1)'s reading 3.5 governs for designs: a detection time, a diagnosed share, a corrected share and an
externalised share; an emissions cut, resource use against regeneration, a debt ratio and a transfer. Taken together
they need the same two readings, what estimates such a level for a design with no implementation, and when a model can
show it. The units are listed in the audit register's order.

**3.2 C3.5's clauses for designs.** (1) *Interpretations.* The four clauses could be read (a) as outcome levels, or (b)
as satisfied by the specification of institutions that detect, diagnose and correct failures and account for costs.
(2) *Preponderance.* The Measurement line names quantities ("time from failure occurrence to identification", "% of
failures with identified causes", "% of identified failures successfully addressed"), and part (b1)'s reading 3.5 holds,
for C2.3 and C2.4, that a design's specification of an institution is not an estimate of the level. (3) *Score* against
(a): a clause is shown by a modelled or component-calibrated estimate, and a model that does not represent failures
cannot show any of the four (part (b1), reading 3.1; part (b5), reading 3.1). A clause the audit coded A is carried as
audited, as throughout the pass. (4) *Applied:* CCO-PTF-CIP-SZH's published model represents no detection, diagnosis or
correction of failures, and its documents specify monitoring institutions but no correction share and no externalised
share. The one quantitative lead, the CIP paper's probabilities that corruption is detected (0.75) and that it ends in
conviction (0.62), is an illustrative input to an expected-cost calculation for one class of failure: it neither clears
clause 3 (it is below the bar in any case) nor contradicts clauses 1 and 2, since neither probability is a detection time
or a diagnosis share. Integral's FRS specifies seven modules, from signal intake and diagnostic analysis to
recommendations routed to CDS and longitudinal memory, and states no rate; the corpus's review sets a mechanism beside
each bar, not an estimate (section 6).

**3.3 C4.1, clause 1: the date.** The clause asks for "35% carbon reduction by 2030". (1) *Interpretations.* It could be
read (a) as a calendar deadline, or (b) as a rate: a reduction path at least as steep as the one the Measurement line
derives for 1.5°C ("must decline 35-45% by 2030"). (2) Read as a deadline, no design unimplemented in 2026 can clear it,
a test that cannot be passed (the mirror of the test that cannot fail which part (b1)'s reading 3.1 rejects); read as a
rate, it needs a stated path and a base year. (3) *Left open,* since no verdict turns on it: the two units whose texts
claim a reduction (Degrowth, CCO-PTF-CIP-SZH) are carried as audited, none of the four units whose texts are silent has
an emissions estimate on either reading, and the fund's and Ostrom's clauses are out of reach. For a design, a boundary
to respect, a monitoring system or a pricing mechanism is not a reduction estimated (part (b1), reading 3.5).
(4) *Flagged for Paper v2.0, not applied:* after 2030 the clause can be read as a deadline only against a configured
economy's record. Restating it as a rate from a stated base year would change a Pass Threshold, which the pass does not
do (protocol 2.3); it is recorded here, and meanwhile as evidence that will date (protocol 4.5).

**3.4 C4.1, clause 3 for designs.** (1) *Interpretations.* The clause could be shown (a) by a stated fiscal balance, or
(b) by a level of the debt ratio under the design. (2) *Preponderance:* the clause names the ratio, and a flow (a
break-even date, a surplus) does not fix a ratio without a starting level and a path. (3) *Score* against (b): the
clause is shown by a modelled or component-calibrated estimate of the ratio under the design. The existing public debt
of the economy a comprehensive system serves belongs to the population it serves (protocol 3.2), and a remedy its sources
do not specify is not credited (D29(c)). (4) *Applied:* CCO-PTF-CIP-SZH's break-even by year 6 and surplus by year 10
are flows (not shown); Doughnut Economics commits to no fiscal rule (not shown); Degrowth, reading 3.5. *Left open,*
since no verdict turns on it: whether a debt-to-GDP clause applies to a post-monetary design (Integral), whose unit
clause 1 already fixes.

**3.5 Degrowth Economics, clause 3: the one unit that could have stood.** Its other three clauses are carried as
audited; only the debt clause was silent, so the unit turned on it, and the degrowth literature's own modelling was
searched for an estimate. Two stock-flow-consistent models were located. In LowGrow SFC's Sustainable Prosperity
scenario for Canada (Jackson and Victor 2020), a post-growth path with net zero by 2040, stabilised GDP, higher
transfers and shorter hours, public debt of about 55% of GDP in 2017 rises slowly but steadily to more than 80% by 2067,
because GDP stabilises while government keeps borrowing and carbon-tax revenue falls to zero; in the model's growth
scenarios it peaks around 66% and ends near 60%. EUROGREEN's degrowth scenario for France (D'Alessandro et al. 2020)
reports the deficit rather than the debt level: below 3% of GDP until 2040, then rising steeply as GDP contracts, even
with a wealth tax the authors introduce to offset the rising deficit and debt ratios. A 2023 paper arguing for Modern
Monetary Theory in a degrowth transition records that modellers of no-growth and degrowth scenarios commonly treat the
rising debt ratio as a problem. *Score:* short. In the one model reporting the level, the ratio crosses 80% within its
horizon and keeps rising, and the degrowth model's deficit rises steeply once GDP contracts. *Flag,* alternative 1.0:
read at the horizon of the threshold's own carbon clause, or at mid-century, the one modelled level located is below
80%; and neither model is the corpus entry's degrowth as such (LowGrow SFC is post-growth; EUROGREEN reports no debt
level). *Reopening:* a degrowth model or source holding the debt ratio below 80% over its horizon, for instance through
the wealth tax EUROGREEN introduces or a stated fiscal rule, would reopen the unit, which would then stand.

**3.6 D31: the four out-of-reach codes are confirmed.** *Sovereign Wealth Fund Statism.* The fund's ethics-based
exclusions (coal, tar sands, the highest-emitting oil-sands producers) govern what it holds, while the extraction rate
is set by the state's petroleum licensing, which the entry's own document records expanding in 2026. Neither the entry's
document nor the fund designs it scores place the economy's emissions or its extraction rate inside the fund, so
clauses 1 and 2 stay out of reach and the unit is 0.5; clause 3 is not estimated. *Ostrom-style commons governance.*
The transfer of the design to global commons is disputed within the mechanism's own literature: Ostrom's 2009 World
Bank paper finds solutions much easier to craft for smaller-scale common-pool resources than for the global commons, and
Stern (2011) concludes that design principle 7 must be rewritten for them, both cited in the entry's own document. D31
scores such an extension out. The carbon storage the entry credits is resource use at or below regeneration, clause 2's
subject, and public debt lies outside every design principle. Counting either extension in would not change either unit:
Ostrom's clause 3 would still be out of reach, and no emissions path or extraction rate attributable to the fund was
located. The document's flag on Ostrom's C4.1, whose alternative was 0.5, is removed.

**3.7 CCO-PTF-CIP-SZH, C4.1: the rationale's premise and the design's carbon figures.** The rationale grounds clause 1
in "CCO funding through carbon tax". No research-hub source located names a carbon tax as CCO's funding: the
digital-governance paper funds the system through a $54.1 billion implementation budget and reaches break-even through
conversion fees, PTF rental revenues and reduced social-service costs. The design's own carbon figures are a roadmap
target (Appendix D) of 15-20% in year 1, 35-45% in year 3, 50-65% in year 5 and 70-80% in year 7, in a table beside
resource figures that does not say whose footprint it covers, and a modelled 45% below baseline trajectory over 20 years
(the modelling paper, section 9.1). Neither is dated to 2030 or names a base year, and they differ in pace. Neither
contradicts the rationale's undated range, so clause 1 is carried as audited and the range is disclosed (protocol 4.3).
The unit falls on clauses 2 and 3, which the design does not estimate. *Reopening:* design estimates of resource use
against regeneration and of the debt ratio under the design.

**3.8 After this group no entry scores 1.0 on C3.5 or C4.1.** C3.5's 1.0 anchor cites CCO-PTF-CIP-SZH; C4.1's cites
Degrowth. Under part (b4)'s reading 3.5, a band with no corpus unit at its value loses its example when the pass is
applied, and seven 1.0 bands now have none (section 5). Part (b4)'s finding that no scored system clears five criteria
becomes seven. As before, it states what the evidence located shows, not that the thresholds cannot be met: both
criteria here fall on outcome levels no design source estimates, on reach, or, for Degrowth, on its own literature's
modelled debt path. Report v2.0 and the v2.0 site state the finding with its reasons. Twenty-seven units remain, so the
count may change again.

## 4. The units

### 4.1 Summary (generated)

| Entry | Criterion | Clauses | Verdict | Flag |
|---|---|---|---|---|
| DG | C4.1 | C C S C | 1.0 → 0.5 | alternative 1.0 |
| FALC | C4.1 | U C U C | 1.0 → 0.5 |  |
| PE | C4.1 | U C U U | 1.0 → 0.5 |  |
| CCO | C3.5 | C C U U | 1.0 → 0.5 |  |
| CCO | C4.1 | C U U C | 1.0 → 0.5 |  |
| INT | C3.5 | C U U C | 1.0 → 0.5 |  |
| INT | C4.1 | U C U C | 1.0 → 0.5 |  |
| DE | C4.1 | U C U U | 1.0 → 0.5 |  |
| SWF | C4.1 | R R U C | 1.0 → 0.5 |  |
| OS | C4.1 | R C R C | 1.0 → 0.5 |  |

Clause statuses are listed in Appendix B's order: C cleared, S short, U not shown, R out of reach, M moot.

### 4.2 Clause by clause (generated)

#### DG C4.1 Intergenerational Justice: 1.0 → 0.5 — flagged as contestable

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | 35% carbon reduction by 2030 | cleared | Absolute reduction in resource extraction and emissions | as audited (the unit's own text) |
| 2 | resource use ≤90% regeneration | cleared | Absolute reduction in resource extraction | as audited (the unit's own text) |
| 3 | debt-to-GDP <80% | short | the two stock-flow-consistent models of the post-growth and degrowth literature located both show the public debt ratio worsening once growth ends: in LowGrow SFC's Sustainable Prosperity scenario for Canada, public debt of about 55% of GDP in 2017 rises slowly but steadily to more than 80% of GDP by 2067, as GDP stabilises while government keeps borrowing and carbon-tax revenue falls to zero, against a peak of about 66% in the growth scenarios; EUROGREEN's degrowth scenario for France reports the deficit, not the debt level, below 3% of GDP until 2040 and rising steeply after 2040 as GDP contracts, even with a wealth tax introduced to offset the rising deficit and debt ratios; so the modelled ratio crosses 80% within the modelled horizon and does not stabilise (reading 3.5) | Jackson and Victor, The Transition to a Sustainable Prosperity, Ecological Economics 177 (2020) 106787, section 5.3 and Fig. 11; D'Alessandro, Cieplinski, Distefano and Dittmer, Feasible alternatives to green growth, Nature Sustainability 3 (2020) 329-335, Fig. 3d and Methods; How to pay for saving the world: Modern Monetary Theory for a degrowth transition, Ecological Economics (2023) |
| 4 | positive wealth transfer to next generation | cleared | preservation for future generations | as audited (the unit's own text) |

*Flag:* alternative 1.0: read at the horizon of the threshold's own carbon clause (2030), or at mid-century, the one modelled debt level located is below 80%, since LowGrow SFC's ratio crosses the bar only late in its fifty-year run; and LowGrow SFC models a post-growth rather than a degrowth design, while the degrowth model located reports no debt level (reading 3.5).

#### FALC C4.1 Intergenerational Justice: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | 35% carbon reduction by 2030 | not shown | the rationale says renewable energy and circular economy principles would preserve resources; the design's premise, energy abundance from renewables, is stated without an emissions path, and its reviewers describe the case as conditional on renewable and other technologies advancing faster than climate and ecological breakdown; no carbon reduction by 2030, or on any dated path, is stated or cited, and none is located (reading 3.3) | Report v1.6, FALC C4.1; Bastani, Fully Automated Luxury Communism (2019); Mariqueo-Russell and Read, Fully automated luxury barbarism, Radical Philosophy (2019) |
| 2 | resource use ≤90% regeneration | cleared | circular economy principles would preserve resources | as audited (the unit's own text) |
| 3 | debt-to-GDP <80% | not shown | not estimated in this pass; the verdict is fixed by clause 1 | — |
| 4 | positive wealth transfer to next generation | cleared | eliminates the need to exploit the future | as audited (the unit's own text) |

#### PE C4.1 Intergenerational Justice: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | 35% carbon reduction by 2030 | not shown | the model's pollution damage revealing mechanism prices pollution inside the annual planning procedure and, under the model's assumptions, reduces it to efficient levels with the polluter paying and victims compensated; an efficient level is not a stated reduction, and no carbon path by 2030 or on any dated path is stated or cited for the model, which has no implementation (reading 3.3) | Report v1.6, PE C4.1; Hahnel, Participatory Economics and the Next System (2017); Hahnel, Wanted: A Pollution Damage Revealing Mechanism, Review of Radical Political Economics (2017) |
| 2 | resource use ≤90% regeneration | cleared | can incorporate long-term ecological preservation | as audited (the unit's own text) |
| 3 | debt-to-GDP <80% | not shown | not estimated in this pass; the verdict is fixed by clauses 1 and 4 | — |
| 4 | positive wealth transfer to next generation | not shown | the rationale says future generations are represented through explicit councils; the model's literature states intergenerational equity and efficiency as goals that imply environmental sustainability and specifies long-run investment planning, but no council representing future generations is located in it, and no transfer to the next generation is estimated (reading 3.3; section 6) | Report v1.6, PE C4.1; Hahnel, A Participatory Economy (2022); Hahnel and Kerkhoff, Integrating Investment and Annual Planning, Review of Radical Political Economics 52:2 (2020) |

#### CCO C3.5 Failure-Mode Transparency: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Failure detection within 1 week | cleared | Failures legible and diagnosable | as audited (the unit's own text) |
| 2 | diagnosis success ≥80% | cleared | Failures legible and diagnosable | as audited (the unit's own text) |
| 3 | correction success ≥70% | not shown | the design specifies monitoring institutions (real-time anomaly detection, AI risk models whose lowest alert level triggers enhanced monitoring with weekly human review, democratic review of major security changes, and a CIP dashboard) but states no share of identified failures successfully corrected; the nearest figure, the CIP paper's conviction probability of 0.62 for detected corruption, is an illustrative input to an expected-cost calculation for one class of failure, and below the bar in any case; the published model represents no detection, diagnosis or correction of failures (reading 3.2) | research hub at 8e8a6ba: risk-mitigation-framework.html, sections 4.3, 10 and 12; citizens-internet-portal.html, section 8.2; harness.js and index.html at cd0ceec (searched) |
| 4 | externalization <10% of total costs | not shown | no share of total costs externalised is stated or estimated; the rationale's grounds (flows visible on a ledger, member monitoring, a dashboard) concern the visibility of the system's own operations, not costs borne outside it; no design source located prices an environmental cost (none names a carbon tax), and the dashboard lists carbon emissions, energy use and waste reduction as metrics to display, not costs internalised (reading 3.2) | Report v1.6, CCO C3.5; research hub at 8e8a6ba: integrated-implementation-roadmap.html, Real-Time Dashboard Metrics; economic-modeling-simulation.html, section 9.1 |

*Note:* clauses 1 and 2 are carried as audited: the CIP paper's detection probability of 0.75 for corruption is neither a detection time nor a diagnosis share, and it covers one class of failure, so it does not contradict the rationale (section 7).

#### CCO C4.1 Intergenerational Justice: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | 35% carbon reduction by 2030 | cleared | 35-45% trajectory achievable | as audited (the unit's own text) |
| 2 | resource use ≤90% regeneration | not shown | no comparison of resource use with regeneration is stated; the roadmap's resource table projects 60-90% reductions in the paper, energy and water use it lists (50 million reams, 500 GWh and 2 billion gallons a year) without saying whose use they are, and the implementation framework names regeneration among the environmental-health dimensions to monitor; the published model represents no resource flows (reading 3.3) | research hub at 8e8a6ba: integrated-implementation-roadmap.html, Appendix D; universal-implementation-framework.html (environmental health); harness.js and index.html at cd0ceec (searched) |
| 3 | debt-to-GDP <80% | not shown | the design states a five-year implementation budget of $54.1 billion, fiscal break-even by year 6 through conversion fees, PTF rental revenues and reduced social-service costs, and a projected annual surplus of $89 billion by year 10; that is a fiscal flow, not a debt level, no debt-to-GDP ratio under the design is stated for any economy it serves, and the published model has no public-finance side (reading 3.4) | research hub at 8e8a6ba: integrated-digital-governance.html, section 6.3; harness.js and index.html at cd0ceec (searched) |
| 4 | positive wealth transfer to next generation | cleared | Positive intergenerational wealth transfer | as audited (the unit's own text) |

*Note:* clause 1 is carried as audited, although no research-hub source names a carbon tax as CCO's funding, as the rationale does (section 6); the design's own carbon figures are a roadmap target of 35-45% by year 3, in a table that does not say whose footprint it covers, and a modelled 45% below baseline trajectory over 20 years, neither dated to 2030 (reading 3.7).

#### INT C3.5 Failure-Mode Transparency: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Failure detection within 1 week | cleared | triggers alarms | as audited (the unit's own text) |
| 2 | diagnosis success ≥80% | not shown | FRS-2 analyses incoming signals against expected ranges, stated principles and prior baselines, and FRS-4 routes recommendations stating the observed problem and its likely cause to CDS; no share of failures whose cause is correctly identified is stated or modelled, the system has no implementation, and the corpus's own review sets a mechanism (system-dynamics modelling and historical comparison) beside the bar, not an estimate (reading 3.2) | integralcollective.io, accessed 2026-09-23, The System: FRS (modules FRS-1 to FRS-7); Integral_NEEC_Review.md, C3.5 |
| 3 | correction success ≥70% | not shown | recommendations go to democratic deliberation in CDS, and FRS-6 keeps time series to evaluate whether past decisions achieved their stated outcomes; no share of identified failures successfully corrected is stated or modelled, and the review sets democratic deliberation and adaptive implementation beside the bar, not a level (reading 3.2) | integralcollective.io, accessed 2026-09-23, The System: FRS (modules FRS-4 to FRS-6); Integral_NEEC_Review.md, C3.5 |
| 4 | externalization <10% of total costs | cleared | tendency to externalize costs | as audited (the unit's own text) |

#### INT C4.1 Intergenerational Justice: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | 35% carbon reduction by 2030 | not shown | the design treats ecological sustainability as a structural requirement, with FRS monitoring ecological thresholds and OAD assessing ecological and lifecycle impacts; no emissions path is stated or modelled, and the corpus's own review reaches a plausible 35%+ reduction by 2030 by inference from the post-growth design, not from a design source (reading 3.3) | Report v1.6, INT C4.1; Integral_NEEC_Review.md, C4.1; integralcollective.io, accessed 2026-09-23, The System: FRS; White Paper v0.1, contents (OAD-3, OAD-4) |
| 2 | resource use ≤90% regeneration | cleared | Ecological sustainability is treated as | as audited (the unit's own text) |
| 3 | debt-to-GDP <80% | not shown | not estimated in this pass; the verdict is fixed by clause 1 (whether a debt-to-GDP clause applies to a post-monetary design is left to Report v2.0, reading 3.4) | — |
| 4 | positive wealth transfer to next generation | cleared | enables intergenerational transfer of knowledge | as audited (the unit's own text) |

#### DE C4.1 Intergenerational Justice: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | 35% carbon reduction by 2030 | not shown | the ecological ceiling includes climate change among nine planetary boundaries, a boundary the economy should respect rather than a reduction the framework delivers; by the entry's own scope decision the framework commits to no redistributive, ownership or monetary mechanism, and emission cuts in the jurisdictions that adopt it are those jurisdictions' own policies, not credited to a comprehensive system whose sources do not specify them; its authors' 2025 update finds that overshoot must reverse at nearly twice its current rate to safeguard Earth-system stability by 2050, a finding about the world, not a reduction achieved (reading 3.3) | NEEC_DoughnutEconomics_scoring_scratch.md, scope decision and C4.1; Raworth, Doughnut Economics (2017); Fanning and Raworth, Nature (2025); protocol 3.2 and D29(c) |
| 2 | resource use ≤90% regeneration | cleared | an intergenerational-preservation device | as audited (the unit's own text) |
| 3 | debt-to-GDP <80% | not shown | by the same scope decision the framework commits to no fiscal rule or monetary mechanism, and no debt path under it is stated or located (reading 3.4) | NEEC_DoughnutEconomics_scoring_scratch.md, scope decision |
| 4 | positive wealth transfer to next generation | not shown | the ecological ceiling preserves Earth-system conditions for future generations as a goalpost; no transfer of wealth or assets to the next generation is estimated for the framework or its adopters (reading 3.3) | NEEC_DoughnutEconomics_scoring_scratch.md, C4.1 |

#### SWF C4.1 Intergenerational Justice: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | 35% carbon reduction by 2030 | out of reach | economy-wide carbon emissions are not governed by the fund; the audit's code is confirmed, since the fund's ethics-based exclusions reach coal, tar sands and the highest-emitting oil-sands producers in its own portfolio while the state that owns it continues to license new oil and gas production, so the fund's climate rules govern what it holds, not the economy's emissions, and neither the entry's document nor the fund designs it scores place an emissions trajectory inside the fund (reading 3.6) | r4_audit_s35.py, REACH; reading 3.6; NEEC_SovereignWealthFundStatism_scoring_scratch.md, C4.1 and C4.2 |
| 2 | resource use ≤90% regeneration | out of reach | the rate of resource extraction is not governed by the fund, which invests its proceeds; the audit's code is confirmed, since the extraction rate is set by the state's petroleum licensing, which the entry's own document records expanding in 2026, not by the fund or its spending rule (reading 3.6) | r4_audit_s35.py, REACH; reading 3.6; NEEC_SovereignWealthFundStatism_scoring_scratch.md, C4.2 |
| 3 | debt-to-GDP <80% | not shown | not estimated in this pass; the verdict is fixed by clauses 1 and 2 | — |
| 4 | positive wealth transfer to next generation | cleared | explicitly-designed intergenerational wealth-transfer mechanism | as audited (the unit's own text) |

*Note:* Qatar's C4.1 flag (alternative 1.0) names this unit as its precedent; when the pass is applied and the flag registers are recomputed, that flag's basis needs restating (section 6).

#### OS C4.1 Intergenerational Justice: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | 35% carbon reduction by 2030 | out of reach | economy-wide carbon reduction is not governed by resource-commons institutions; the audit's code is confirmed under D31, since the transfer of the design to global commons is disputed within the mechanism's own literature: Ostrom's 2009 World Bank paper finds solutions much easier to craft for smaller-scale common-pool resources than for the global commons, and Stern (2011) concludes that design principle 7 must be rewritten for them; the carbon storage the entry credits is resource use at or below regeneration, clause 2's subject (reading 3.6) | r4_audit_s35.py, REACH; reading 3.6; NEEC_Ostrom_Commons_scoring_scratch.md, C4.1 and C4.2 (Ostrom, World Bank, 2009; Stern, International Journal of the Commons, 2011) |
| 2 | resource use ≤90% regeneration | cleared | Resource use at or below regeneration is the mechanism | as audited (the unit's own text) |
| 3 | debt-to-GDP <80% | out of reach | public debt is not governed by commons institutions; the audit's code is confirmed, since the entry's own flag records that the mechanism does not address the debt-to-GDP clause, and none of the design principles concerns public finance (reading 3.6) | r4_audit_s35.py, REACH; reading 3.6; NEEC_Ostrom_Commons_scoring_scratch.md, C4.1 |
| 4 | positive wealth transfer to next generation | cleared | Positive intergenerational transfer is not a projection | as audited (the unit's own text) |

*Note:* the document's flag, whose alternative was 0.5, is removed: the unit is 0.5 on reach.

## 5. What parts (a) and (b) so far change (generated)

| Entry | Published (rank) | After (b5) (rank) | After this group (rank) | Change here | Failures | Tier | D28 units left | Floor if all fall |
|---|---:|---:|---:|---:|---:|---|---:|---:|
| CCO | 24.5 (1) | 20.5 (1) | 19.5 (1) | -1.0 | 0 | Potentially Adequate | 3 | 18.0 |
| PE | 20.5 (2) | 16.5 (2) | 16.0 (2) | -0.5 | 1 | Potentially Adequate | 4 | 14.0 |
| NSD | 19.5 (3) | 14.5 (5) | 14.5 (5) | 0.0 | 2 | Potentially Adequate | 3 | 13.0 |
| INT | 19.5 (3) | 16.0 (3) | 15.0 (4) | -1.0 | 3 | Partially Adequate | 3 | 13.5 |
| DG | 19.0 (5) | 16.0 (3) | 15.5 (3) | -0.5 | 2 | Potentially Adequate | 4 | 13.5 |
| MS | 16.5 (6) | 13.0 (7) | 13.0 (6) | 0.0 | 2 | Potentially Adequate | 0 | 13.0 |
| MMT | 15.5 (7) | 12.0 (11) | 12.0 (11) | 0.0 | 3 | Partially Adequate | 1 | 11.5 |
| UBI | 14.5 (8) | 11.5 (15) | 11.5 (15) | 0.0 | 7 | Structurally Inadequate | 1 | 11.0 |
| MC | 14.5 (8) | 12.5 (9) | 12.5 (8) | 0.0 | 3 | Partially Adequate | 1 | 12.0 |
| OS | 14.5 (8) | 13.5 (6) | 13.0 (6) | -0.5 | 3 | Partially Adequate | 0 | 13.0 |
| SWF | 14.0 (11) | 13.0 (7) | 12.5 (8) | -0.5 | 3 | Partially Adequate | 0 | 12.5 |
| SG | 14.0 (11) | 12.0 (11) | 12.0 (11) | 0.0 | 4 | Partially Adequate | 0 | 12.0 |
| GEO | 13.5 (13) | 12.5 (9) | 12.5 (8) | 0.0 | 2 | Potentially Adequate | 0 | 12.5 |
| UBS | 13.5 (13) | 12.0 (11) | 12.0 (11) | 0.0 | 3 | Partially Adequate | 0 | 12.0 |
| IF | 13.5 (13) | 12.0 (11) | 12.0 (11) | 0.0 | 5 | Partially Adequate | 1 | 11.5 |
| FALC | 13.0 (16) | 10.5 (16) | 10.0 (16) | -0.5 | 10 | Structurally Inadequate | 2 | 9.0 |
| DE | 11.5 (17) | 10.0 (17) | 9.5 (17) | -0.5 | 8 | Structurally Inadequate | 1 | 9.0 |
| SQ | 10.5 (18) | 9.5 (18) | 9.5 (17) | 0.0 | 9 | Structurally Inadequate | 0 | 9.5 |
| CPS | 10.0 (19) | 8.0 (21) | 8.0 (21) | 0.0 | 12 | Structurally Inadequate | 1 | 7.5 |
| SC | 10.0 (19) | 9.0 (20) | 9.0 (20) | 0.0 | 9 | Structurally Inadequate | 1 | 8.5 |
| CN | 10.0 (19) | 9.5 (18) | 9.5 (17) | 0.0 | 8 | Structurally Inadequate | 0 | 9.5 |
| QA | 9.0 (22) | 8.0 (21) | 8.0 (21) | 0.0 | 10 | Structurally Inadequate | 0 | 8.0 |
| LM | 8.0 (23) | 6.5 (23) | 6.5 (23) | 0.0 | 15 | Structurally Inadequate | 1 | 6.0 |

"After (b5)" is the total after parts (a) to (b5), whose intermediate columns are in `NEEC_Rescoring_s37.md` to
`NEEC_Rescoring_s42.md`; "D28 units left" counts the entry's units still to be re-estimated in part (b); "Floor if all
fall" is the total if every one of them became 0.5.

After this group the corpus has 18 dominance pairs against 18 after part (b5) (new: none; lost: none), and its frontier holds 13 entries against 13 (NSD, MS, LM, UBI, DG, FALC, PE, CCO, INT, MC, SWF, IF, OS). First place: CCO, 20.5 after part (b5), 19.5 now. Across parts (a) and (b1) to (b6), 118 units have been re-estimated: 7 stand and 111 become 0.5 (55.5 points).

Left for part (b): 27 D28 units (C4.2 6, C4.3 6, C4.4 4, C4.5 3, C5.2 4, C5.4 2, C5.5 2).

After this group, the entries scoring 1.0 on this group's criteria are: C3.5, 0; C4.1, 0, against 3 published and 8 published. Every criterion had a 1.0 in the published corpus; after the pass so far no entry scores 1.0 on 7 of them: C1.1 (emptied in part (b3)), C2.1 (emptied in part (b4)), C2.3 (emptied in part (b1)), C2.4 (emptied in part (b1)), C3.1 (emptied in part (b2)), C3.5 (emptied in part (b6)), C4.1 (emptied in part (b6)).

Flags added in this group: 1; removed: 1. Across the pass so far, 15 entries' flag registers change (CCO, CN, CPS, DG, IF, LM, MC, NSD, OS, QA, SG, SQ, SWF, UBI, UBS).

Anchor examples citing a unit the pass moves: C1.1's 1.0 example, NSD (part (b3), to 0.5); C2.1's 1.0 example, UBI (part (a), to 0.5); C2.3's 1.0 example, DG (part (b1), to 0.5); C2.4's 1.0 example, PE (part (b1), to 0.5); C2.5's 1.0 example, CCO (part (b5), to 0.5); C3.1's 1.0 example, UBI (part (b2), to 0.5); C3.2's 1.0 example, PE (part (b4), to 0.5); C3.5's 1.0 example, CCO (part (b6), to 0.5); C4.1's 1.0 example, DG (part (b6), to 0.5); C5.1's 1.0 example, MS (part (b2), to 0.5). When the pass is applied, each band needs an example the corpus then scores at that value; C1.1's 1.0, C2.1's 1.0, C2.3's 1.0, C2.4's 1.0, C3.1's 1.0, C3.5's 1.0, C4.1's 1.0 bands have none left (part (b4), reading 3.5; reading 3.8 here); C2.5's 1.0 band keeps one (LM, flagged; part (b5), reading 3.7).

## 6. Corrections found (not polish)

1. **Report v1.6, CCO-PTF-CIP-SZH C4.1,** says "CCO funding through carbon tax". No research-hub source located names a
   carbon tax as CCO's funding (reading 3.7). Report v2.0 states the design's funding as its documents give it, and both
   of its carbon figures with their scope and horizon.
2. **`Integral_NEEC_Review.md`, C3.5 and C4.1.** Its C3.5 "Estimated Performance" sets a mechanism beside each bar
   ("Correction success ≥70%: Democratic deliberation and adaptive implementation"), which is not an estimate
   (protocol 2.2); its C4.1 "plausible 35%+ carbon reduction by 2030" is inferred from the post-growth design, not taken
   from a design source. The review is a corpus document and is not edited here; Report v2.0 states Integral's C3.5 and
   C4.1 on the design's own sources, as the units do.
3. **Report v1.6, Participatory Economics C4.1,** says "Future generations represented through explicit councils". No
   such council was located in the model's literature searched (Hahnel 2017, 2020, 2022), which states
   intergenerational equity as a goal and specifies long-run investment planning. Report v2.0 cites a source for the
   councils or restates the sentence.
4. **Qatar's C4.1 flag** (alternative 1.0) names Sovereign Wealth Fund Statism's C4.1 as its precedent. That unit
   becomes 0.5 here. When the pass is applied and the flag registers are recomputed, the flag's basis must be restated;
   whether it survives on Qatar's own evidence is outside this group.

*Polish, optional:* C3.5's fourth clause, "externalization <10% of total costs", does not say whose total costs; the
Measurement line's "No systematic externalization (environmental, social costs not hidden)" suggests the economy's.
Paper v2.0 could name the base.

## 7. Disclosure

CCO-PTF-CIP-SZH is the owner's design. It falls here on both criteria, 1.0 points in all, on the same readings that
govern every unit and with no departure from the audit's codes: its sources state no correction share, no externalised
share, no resource use against regeneration and no debt ratio under the design. No simulation run is used, because the
design's published model represents none of these quantities (emissions, resource flows, public finance and the handling
of failures are all absent from `harness.js` and `index.html` at `cd0ceec`); its documents decide the units.

*Notes for the design's maintainers* (the owner's project, not NEEC corrections; they add to Handoff 40, section 12):
(a) the published model represents no emissions, resource flows, public finance or failure handling, so C3.5 and C4.1
rest on documents alone; (b) the carbon figures differ across documents (the roadmap's Appendix D schedule, 35-45% by
year 3; the modelling paper's 45% below baseline trajectory over 20 years), Appendix D does not say whose footprint it
covers, and no hub document carries the carbon tax the NEEC Report names; (c) the fiscal claims are flows (break-even by
year 6, an $89 billion annual surplus by year 10) with no debt path and no stated base economy.

## 8. What remains

- **(b), continued:** the 27 D28 units of section 5's line "Left for part (b)", criterion by criterion; C4.2 next (6),
  which shares C4.1's carbon and regeneration clauses and so readings 3.3 and 3.6, then C4.3, C4.4, C4.5, C5.2, C5.4 and
  C5.5.
- **(c)** the 131 mechanism-class 0.5s against D29, Ostrom's C4.3 first; **(d)** D31's source for Ostrom's community
  land trusts; **(e)** the Islamic finance and Ostrom documents' quoted thresholds restated.

When the pass ends, its changes are applied by generator, and the corpus, CSV, `README.md` and Appendix A.4 are
regenerated; the changed flag registers are recomputed (Qatar's C4.1 among them, section 6); the ten anchor examples the
pass moves are replaced or, for the seven 1.0 bands left with no corpus unit, removed (part (b4), reading 3.5; reading
3.8 here); the protocol's statements about the corpus are restated; and the claims and protocol verifiers and the seven
rescoring scripts get successors.

## 9. What this record does not show

It is one scorer's re-estimation, on evidence located in one session through web search, the entries' own rationales
and scoring documents, the corpus's review of Integral, the design's research-hub sources and published model, and
Integral's published system description (its v0.1 white paper exists as a PDF too large for the fetch tool, so its
summary page and system pages were read). "Not shown" means no evidence was located, not that the clause fails. Seven
units fall on clauses no source estimates, two on reach, and one, Degrowth, on its own literature's modelled debt path,
under a flagged reading. Whether these calls reproduce is what the replication programme tests.
