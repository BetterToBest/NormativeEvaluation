# NEEC Rescoring Pass — Record, Stage 2, Group 2.1: CCO-PTF-CIP-SZH's Modelled Units on the Design's Published Model, v4.20

**Session 51 · 2026-09-26 · Scorer and engineer: Claude · Owner: Duke Johnson**
**Status: scratch (protocol 10.1). Parts (a) and (b) are `NEEC_Rescoring_s37.md` to `NEEC_Rescoring_s50.md`, and
`NEEC_Rescoring_s48.md` re-read C4.4 on decision 48.3; this record begins stage 2 and edits none of them.** No corpus
file, score or scoring document changes until the pass ends. Its changes are then applied by generator with pinned
inputs and restated in place (protocol 10.2, 10.3; decisions D12, D14), and until then the published totals stand,
provisional as `README.md` says. Decisions taken here are Claude's under the owner's delegation (Handoff 35, section 2);
each is recorded with its reasons, and the owner may reverse any of them.
**Reproduce:** `python3 rescoring_s51.py` (harness check 99). It holds every clause estimate below on the v2.0 clauses
(`criteria.json`), scans the rationale of every published 1.0 for figures from an entry's own modelling (reading 3.2),
checks the simulation runs' captured output (its digest, its sixteen checks, and every figure this record quotes),
carries or departs from the audit's A codes with a reason for each, checks the design's other re-estimated units against
v4.20 (reading 3.9), computes every figure in section 6 cumulatively with parts (a) and (b) and decision 48.3 on the
published 26-criterion structure, and checks that this record contains its generated tables and the runs' tables
verbatim. The runs themselves: `node cco_simulation_checks_s51.js path/to/harness.js path/to/index.html` on a clone of
`BetterToBest/compassionism-simulation` at `5a7a7b1`; the harness does not rerun the JavaScript (the simulation's
source is not in this repository), as with Sessions 38 and 40.

---

## 1. What this group is

On 2026-09-26 the owner told the scorer that version 4.20 of the Compassionism Simulation, CCO-PTF-CIP-SZH's published
model, is live, with features that could alter some of the design's NEEC scores. The pass had read the model at
`cd0ceec` (v4.15) since part (b1) and pinned every run to it; Handoff 40 recorded that a new version reopens the
design's units only through the reopening conditions their records state. Between v4.15 and v4.20 the simulation
answered the ten notes Handoff 40 (section 12) left for its maintainers (section 9 below) and changed what it models:

- **v4.16:** an opt-in Baseline run at the scenario's own inflation (the shipped Baseline runs at 3% CPI).
- **v4.17:** income and basket poverty measures (cash income below 60% of the scenario's median, with and without the
  in-kind value of cost relief; cash income below the living-wage basket, net and gross of cost relief), each reported
  against year 0 and against the Baseline; recessions in `harness.js`; an **Adverse Environment** preset, the reference
  settings under recessions, AI automation and 2% inflation; and four disclosures: the papers' 98% and $82,000 are not
  produced by the engine, the 55% participation threshold is not a dynamic, the SZH synergy is gated on a proxy, and
  prices are an exogenous input.
- **v4.18:** an extreme-poverty overlay built on a housing-distress measure.
- **v4.19:** automatic stabilizers on the Research Hub's crisis protocols, off in every preset; CCO's cost relief
  scales with the Basic Unit (unchanged at the $1,200 reference).
- **v4.20:** `automationRisk` recalibrated to Frey and Osborne's employment-weighted distribution (high-risk weight 0.47
  to 0.63) and sampled by inverse CDF, which moved the seed-42 regression once (1,965 to 1,975 days, $559,223 to
  $570,661, Gini 0.534 to 0.518, wealth poverty 16.6% to 15.8%); continuous integration and a source-parity check
  between `index.html` and `harness.js`.

**What this group does.** It moves the pass's pin to v4.20 (reading 3.1). It scans the rationale of every published
1.0 for a figure that rests on the entry's own modelling (reading 3.2): 27 rationales name modelling, a simulation, a
stress test or a projection, and 9 rest on a figure from the entry's own model, all of them CCO-PTF-CIP-SZH's. The pass
re-estimated four of the nine (C1.1, C2.1, C4.2, C4.4); the other five, **C1.2b, C1.4, C3.2, C3.3 and C5.3**, are read
here on the published model and the design's sources, and C1.1, class I, is re-checked on v2.0's indicator, the
Societal Poverty Line (readings 3.3 and 3.4). Every other unit of the design the pass re-estimated is checked against
v4.20 (reading 3.9).

**Outcome.** **C1.2b, C1.4 and C3.3 fall from 1.0 to 0.5**: the published model puts the wealth Gini at 0.518, cannot
run C1.4's displacement scenarios and shows poverty above 8% at its nearest one, and runs one of C3.3's four compound
scenarios, in which the nearest measure to housing stability degrades by 28.8%; the three rationales' figures are the
modelling paper's Gini of 0.28, which the design's own BLEI paper says the simulation does not reproduce, and two
figures located in no design source (readings 3.5 to 3.7). **C3.2 and C5.3 stand**: the model computes neither prices
nor aggregate participation, and the design's papers state the figures (reading 3.8). **C1.1 stays 0.5** on the
Societal Poverty Line, on which the reference run's poverty rises from 9.0% to 11.5%, and part (b3)'s flag toward 1.0
is removed (readings 3.3, 3.4). None of the other fourteen units reopens; C3.4's condition, an endogenous price or
behavioural channel, is not met. Net −1.5 points; no failure count and no tier changes. **CCO-PTF-CIP-SZH keeps first
place, 17.0 to 15.5**; Participatory Economics and Integral share second at 14.5. The group also records Paper v1.4
Appendix G's Run Record #4, which v4.20's automation recalibration triggers (section 8).

## 2. How a clause is recorded, and the rule

As in part (a), section 2: each clause is cleared, short, not shown, out of reach or moot; a 1.0 stands only if every
clause is cleared or moot, and otherwise becomes 0.5 (D28, protocol 2.3); a clause-level gap never makes 0.0 (D28(f)).
The clauses are v2.0's (`criteria.json`; protocol draft.9, Appendix B). C1.1, C1.4, C3.2 and C5.3 keep their Session 44
clauses verbatim, each mapped to the clause the R4 audit coded. C1.2b and C3.3 have one clause each; the audit covered
multi-clause thresholds only, so they are outside D28's population and have no audit codes. On C3.2 and C5.3 (class U)
every A code is carried as cleared on the unit's own text, as in parts (b7) to (b9); on C1.4 (class I) both A codes
are departed from, each with its reason (reading 3.6). No clause is left not estimated, and none is out of reach.

## 3. Decisions and readings (under the delegation)

**3.1 The pin moves to v4.20.** *Decision:* from this group the pass reads the Compassionism Simulation at commit
`5a7a7b1`, `harness.js` md5 `fe6fa4a3…` and `index.html` md5 `c333b632…` (`META.VERSION` 4.20). On 2026-09-26 the
simulation's site served both files byte for byte. Earlier records keep `cd0ceec` (v4.15) as the evidence of their
date, and their reopening conditions are checked against v4.20 here (reading 3.9); `session_check.py` now notes the
simulation's HEAD against the new pin. The run script executes `harness.js` itself, not a re-implementation. It checks
v4.20's documented seed-42 regression, reproduces `runScenario()` exactly on all 500 seeds of all eight scenarios it
uses, and reproduces the automation sweep and headline figures v4.20's release notes print for seeds 1 to 500 before
any table is read (section 5). v4.17 moved the two recession functions into `harness.js`, and they are the page's
character for character, so nothing is appended to the engine as Session 40 had to. *Reason:* the owner announced
the version; the pin's purpose, that every NEEC figure can be rerun on a stated engine, is kept by pinning the new one.
N is 500 seeds here, against Session 40's 100, to match the simulation's own documented runs.

**3.2 Which units the model bears on.** *Interpretations.* (i) Only the reopening conditions recorded for units the
pass re-estimated; or (ii) those, and every published 1.0 whose rationale rests on a figure from the entry's own
modelling, since part (b3)'s reading 3.3 decided that "the published model governs" the design's C1.1, and that "the
same preference would apply to any entry whose rationale cites modelling". *Preponderance:* (ii). Under (i) the pass
would read the modelling paper's 98% against the published engine while crediting, unread, the Gini figure the same
paper reports in its results. *Applied:* every published 1.0's rationale, from the text the
R4 audit read, is scanned for modelling, simulation, stress testing or projection. The scan finds 27 and classifies
each (generated):

| Why the word appears | Units |
|---|---|
| a figure from the design's own modelling | CCO C1.1, CCO C1.2b, CCO C1.4, CCO C2.1, CCO C3.2, CCO C3.3, CCO C4.2, CCO C4.4, CCO C5.3 (9) |
| the word names the system or its framework, not a model's output | NSD C5.4, DE C2.5, CN C5.1, SG C5.1, SG C5.3, IF C5.2 (6) |
| the text contrasts an observed record with projection or modelling | GEO C3.4, GEO C5.3, MC C3.4, MC C5.3, DE C5.3, SWF C5.3, IF C5.3, OS C4.1 (8) |
| the stress test is a real-world episode | CN C3.2 (1) |
| the entry's revision of its own model is the clause's evidence, not a modelled figure | DE C3.4, UBS C3.4 (2) |
| the estimates are NEEC's own review of a design that publishes no model | INT C3.3 (1) |

The nine that rest on the entry's own modelled figures are all CCO-PTF-CIP-SZH's; no other entry cites a model of its
own. Integral's C3.3 rests on four compound-scenario estimates made by NEEC's own review of a design that publishes no
model; three of the four are under 20% (`Integral_NEEC_Review.md`), which clears ≥3 of 4, and there is nothing further
to read them against. Of the nine, the pass has re-estimated C1.1 (part (b3)), C2.1 (part (b4)), C4.2 (part (b7)) and
C4.4 (part (b7) and decision 48.3). The other five are read here. *Rule, applied alike:* where the published model
computes the quantity a rationale's figure states, the model governs, as part (b3) decided; where it does not, the
design's sources are read at the modelling tier (protocol 4.1), and a figure that no source of the design states is
not evidence, as part (b4) found for the design's C2.1 figure. C1.2b and C3.3 are class W and single-clause, outside
D28's population. "No verdict can change" describes what the v2.0 revision does to class W units; it does not shield a unit
from the entry's own evidence. Part (b2) likewise read C5.1's eleven 1.0s outside D28.

**3.3 C1.1, re-checked as class I: the Societal Poverty Line.** C1.1 is class I: v2.0 names its indicator, "poverty
headcount at the Societal Poverty Line (2021 PPP)", and its calculation, the reduction "against the rate at the stated
base year (the adoption year for a design)". Part (b3)'s record read the engine's two headcounts, net wealth under
$25,000 and under 30 days of runway, a different measure, so the unit is re-checked (`NEEC_Criteria_v2_s45.md`,
section 7). The World Bank's line in 2021 PPP dollars is max($3.00, $1.30 + 50% of the median) a day (Foster et al.,
Policy Research Working Paper 11137, June 2025, section 3.4.1). The run applies it to the engine's own per-agent cash
income (wage income after the income shock plus CCO conversion proceeds), for 365 days, in the engine's dollars.
Two things about the engine matter: its agents are single adults with no taxes or transfers, so the engine needs no
equivalence scale, and the United States is the PPP numeraire. A variant counts the in-kind value of cost relief as
income. *Result:* in the reference run poverty on the line is 9.0% at adoption and 11.5% at year 20, 27.9% higher;
with in-kind relief 8.4%, 6.8% lower. The line rises with the median, which Full Integration doubles ($39,966 to $79,370), and
low-wage participants and non-participants stay below it; the engine's documentation describes the same behaviour for
its own relative measure. The largest reduction on any measure is net basket poverty's (85.0% against year 0, 87.9%
against the paired Baseline). *Stress:* the Adverse Environment governs, the preset the engine's documentation names
for stress criteria ("a stress criterion that means 'does the reference design hold up under adverse conditions'
should be tested against Adverse Environment"); the Stress Test preset also weakens the settings, as part (b3)'s
reading 3.4 found. No measure falls 85% there against either comparator (largest 57.9%). Both clauses stay short; the
unit stays 0.5.

**3.4 C1.1's flag toward 1.0 is removed.** Part (b3) flagged the unit toward 1.0: "the design's hub papers' modelled
figures credited at the modelling tier instead of the published engine". The flag rested on a measure gap. Neither of
the engine's headcounts was the papers' measure, poverty below 60% of median income, so the papers' 98% could not be
tested on its own terms. v4.17 closed the gap, and on the papers' own measure the engine shows no reduction: 15.3% at
adoption, 18.1% at year 20, and 16.4% in the paired Baseline. Its documentation also states that "the 98% / $82,000
headline is not produced by this engine" and that "the model behind 98% is not in this repository". A careful second
scorer could no longer defensibly credit a figure that the design's published model contradicts on the figure's own
measure and at its own settings, and that the model's maintainers disclaim (protocol 6.1). *Decision:* the flag is
removed. The reopening conditions stay: the unit reopens if the model behind 98% is published and reproduces it, or if
a later version reaches 90% in the reference run and 85% in the Adverse Environment on the Societal Poverty Line.
*Alternative rejected:* keeping the flag on protocol 4.1's modelling tier alone. That tier credits a design's modelled
figures; it does not credit them against the design's own published model at the same settings.

**3.5 C1.2b: the wealth Gini.** The rationale reads "wealth Gini is projected under 0.35", carried from the design's
C4.4 rationale. The projection is the modelling paper's: integrated CCO-PTF system, "Gini coefficient reduction:
0.45 → 0.28 (median)" (section 5.1), from the unpublished model behind the papers' 98%. The published model computes the
quantity. At year 20 of the reference run the Gini is 0.518 on the engine's EDC-adjusted net wealth, the figure it
reports, and 0.510 on net wealth with negative holdings at zero; no seed of 500 is below 0.35, and the Gini falls from
0.601 at adoption. The design's own BLEI paper says the same at the pin: its design target, "0.25 in the simulation's
own `CFG.TARGET_GINI` constant", "is not, however, what the simulation actually measures", which "measures EDC-adjusted
Gini at 0.518 (v4.4), more than double either stated target", "a large, honestly-disclosed gap between design target
and measured output" (section 9). *Decision:* short; the unit is 0.5. Not 0.0: conversion limits, expiring units and
distributed acre equity are structural mechanisms of the kind C1.2b's measurement names, and they lower the Gini. No
flag: the design's own sources concede the gap.

**3.6 C1.4: the design's own model of the scenarios, and Appendix G.** v2.0's C1.4 asks for poverty under 8% on the
Societal Poverty Line and aggregate demand above 85% of baseline "in each of the 30%, 50% and 70% displacement
scenarios", and names as a design's indicator "its own model of the three scenarios". The rationale reads: "Stress
testing shows the system maintains poverty <5% and aggregate demand 90-110% baseline across 30%, 50%, 70% job
displacement scenarios". Those figures are Paper v1.4's own C1.4 measurement text for its 30% scenario ("maintain
poverty <5%, aggregate demand 90-110% baseline"), restated as a result. No design source states them: the modelling
paper's unemployment shock (joblessness to 12%) reports system stability in 94% of scenarios, and the framework paper
lists a scenario of 20% unemployment with a 45% fall in traditional employment but reports no result for it; no source
reports poverty or demand under a displacement of 30% or more. The published model cannot run the scenarios. Its
automation channel slows each agent's wage growth by at most 0.10 times the agent's automation risk a year, reaching
the cap in year 13, and displaces no hours: the mismatch Paper v1.4's
Appendix G.2 records, unchanged at v4.20. Its nearest scenario, High Automation, is milder than the 30% scenario. There,
at year 25, poverty on the Societal Poverty Line is 18.0% (10.6% with in-kind relief), against 12.1% without
automation; no seed is below 8%; aggregate wage income falls to 46.2% of the automation-off run and aggregate cash
income to 47.8%. *Decision:* both clauses are not shown and the unit is 0.5; the audit's two A codes are departed from,
each with its reason. Not 0.0: the Basic Unit does not depend on employment, a mechanism of the kind C1.4 asks for.
*Alternative rejected:* reading "cannot be evaluated" (Appendix G.6) as leaving the rationale's figures standing. G.6
says a comparison cannot be made; it does not make an unsourced figure evidence. Appendix G found the same in kind at
v3.9 to v4.2 and changed no score only because no score was then read from simulation output.

**3.7 C3.3: the one compound scenario the model runs.** C3.3 asks that core functions be maintained across at least
three of four compound scenarios with degradation under 20%. Its functions are poverty (the share above C1.1's line),
housing stability (C1.3's rate), essential-service capacity and democratic-function capacity; degradation is "each
function's fall from its pre-shock level, as a share of that level". *Reading:* in a 20-year run whose shocks recur
from year 1, the pre-shock level is the same run's level without the shocks, the paired run on the same population;
year 0 precedes adoption and would count the design's own effect as recovery. The published model runs one compound
scenario, the Adverse Environment, milder than C3.3's recession-and-automation scenario (30% GDP decline, 15%
unemployment, 40% business closures). At year 20 the share above the Societal Poverty Line is 4.4% lower than without
the shocks, under 20%. The share not in housing distress, the engine's nearest measure to housing stability, is 28.8%
lower. Essential services and democratic functions are not modelled, and neither are the other three compound
scenarios. The design's papers report single-shock tests (a recession of 8% of GDP, a 6% inflation surge, unemployment
of 12%, a climate crisis; cyber attacks at 97% of transaction capacity for two to three days) and no compound scenario
or degradation figure. The rationale's "Degradation <15% in all scenarios" is located in no design source. *Decision:*
not shown; the unit is 0.5. Not 0.0: the distributed architecture is a mechanism of the kind C3.3 asks for. The verdict
does not turn on the housing measure: three of the four scenarios are unshown whatever the one modelled shows.

**3.8 C3.2 and C5.3: the model is silent, and they stand.** C3.2's figures are the design's modelling. The dual-currency
inflation paper, a formal model with its calibration and numerical simulations, gives 0.95% a year in its baseline
scenario and a 95% interval of 0.6% to 1.4% over 10,000 runs (sections 5.2 and 5.4). The framework paper's 8% scenario
holds local inflation to 3.2% while national inflation reaches 8.1% (section 5.2). The published model computes no
price: inflation is an input rate there, and its documentation says that "as long as prices are exogenous, the model
assumes the framework is non-inflationary rather than testing it". It neither supports nor contradicts the figures.
C5.3's figures are likewise the framework paper's (viability at 30% participation; merchant revenue at 98-102% of
pre-implementation levels; sections 5.2 and 5.3) and the modelling paper's phased rollout (section 10.1). The published
model reads no aggregate participation (v4.17 relabelled its 55% threshold a design reference, and outcomes change
smoothly through it), and it computes neither economic activity nor a scaling path. *Decision:* both units stand, the
audit's A codes carried as class U requires. *Alternative rejected:* discounting every figure from the design's
unpublished models, because some of them are contradicted by the published one. That would treat silence as
contradiction. The inflation paper's model is a different model, stated with its equations, and nothing located
contradicts it.

**3.9 The design's other re-estimated units, against v4.20.** Fourteen other units of the design were re-estimated in
parts (a) and (b). For each, the table gives what its record read from the model, or its reopening condition, and what
v4.20 changes (generated):

| Unit | Part | Verdict | What the record read from the model, or its reopening condition | At v4.20 | Outcome |
|---|---|---|---|---|---|
| CCO C2.3 | (b1) | 0.5 | no estimate of the level of creative engagement or of meaning scores was located | computes neither | stands |
| CCO C2.4 | (b1) | 0.5 | no estimate of the share of proposals adopted or of satisfaction with responsiveness | the CIP democratic rate is an input (65%), not an output; computes neither | stands |
| CCO C3.4 | (b1) | 0.5 (flagged) | reopens if the simulation adds an endogenous price or behavioural channel and the adjustment run is repeated | prices remain an exogenous input rate, damped only by realised PTF and PTH membership (Known Limitations, v4.17); no behavioural response is added, and v4.19's rule scaling cost relief with the Basic Unit is mechanical: not met | stands |
| CCO C5.1 | (b2) | 0.5 | the components' records decide; no model is read | does not bear | stands |
| CCO C2.1 | (b4) | 0.5 | the model computes no autonomy or coercion measure | still none | stands |
| CCO C2.5 | (b5) | 0.5 | the model does not simulate an exit from Public Trust Housing | Public Trust Housing membership is still fixed at construction | stands |
| CCO C3.5 | (b6) | 0.5 | no share of failures diagnosed or corrected, and no externalised cost, in the model | still none | stands |
| CCO C4.1 | (b6) | 0.5 | no resource use against regeneration and no debt ratio in the model | still none; v4.19 states that the engine has no budget constraint | stands |
| CCO C4.2 | (b7) | 0.5 | the model represents neither emissions nor biodiversity | still neither | stands |
| CCO C4.4 | 48.3 | 0.5 | no simulation run is used: the model represents no governance of decisions | still none | stands |
| CCO C4.3 | (b8) | 0.5 | the model represents no groups | agents still carry no group attribute | stands |
| CCO C5.2 | (b9) | 0.5 (flagged) | the model represents no deployment pathway | still none: the population is fixed from year 0 | stands |
| CCO C5.4 | (b9) | 0.5 | no projection of opposition to repeal or of survival across administrations | still none | stands |
| CCO C3.1 | (a) | 0.5 | clause 3 (coverage) not shown: participation is opt-in | v4.19 adds automatic stabilizers built on the Research Hub's crisis protocols, off in every preset (the hub's x1.20 rule, a shock-neutral default of x1.35 and a scaled option of +2.8% per 1% of income lost); clause 2 on the design's stated rules is unchanged (the roadmap's fixed 20%); CCO participants, who receive Basic Units, are 77.9% of the reference population, and emergency enrollment extends cost relief, not a cash benefit, at a placeholder 50% take-up: clause 3 still fixes 0.5 | stands |

C3.1 is the one on which v4.20 has new content: the Research Hub's recession protocol, built as an opt-in lever.
Clause 2 is read "for a design, from its rules". The design's stated rule is the roadmap's fixed 20% on a GDP decline
of more than 2% for two quarters. The simulation's shock-neutral default (×1.35) is also fixed, and its scaled option
(+2.8% per 1% of income lost) is a lever of the model, off in every preset, whose trigger reads income, since the
engine has no GDP. Clause 3 (≥90% coverage, the share receiving at least one cash benefit) fixes the verdict whatever
clause 2 reads: participants, who receive Basic Units, are 77.9% of the reference population.

**3.10 Stage 2's order.** Handoff 50 set stage 2 to begin with the class M re-checks (C5.2's sixteen units first). The
owner's notice of v4.20 bears on the design's units, and reading 3.2 found five published 1.0s that rest on the
design's modelling. *Decision:* this group comes first; the class M re-checks follow unchanged (section 11). When the
class M re-checks reach the design's C1.2a and C1.3, and the class I re-checks its C3.1, they read the model at this
pin: v4.20 reports median wealth (C1.2a) and housing distress (C1.3), neither of them yet on v2.0's measures.

## 4. The units

### 4.1 Summary (generated)

| Entry | Criterion | Class | Clauses | Verdict | Flag |
|---|---|---|---|---|---|
| CCO | C1.1 | I | S S | 0.5 (part (b3)) → 0.5 | removed (part (b3)'s, toward 1.0) |
| CCO | C1.2b | W | S | 1.0 → 0.5 |  |
| CCO | C1.4 | I | U U | 1.0 → 0.5 |  |
| CCO | C3.2 | U | C C C | 1.0 → 1.0 |  |
| CCO | C3.3 | W | U | 1.0 → 0.5 |  |
| CCO | C5.3 | U | C C C C | 1.0 → 1.0 |  |

### 4.2 Clause by clause (generated)

#### CCO C1.1 Poverty Elimination Capacity: 0.5 (part (b3)) → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥90% poverty reduction within 20 years under base scenario | short | on the design's published model at v4.20, at the Full Integration settings its parameter file credits with 98% (500 seeds, 20 years), poverty on the Societal Poverty Line, v2.0's indicator, computed from the engine's own cash incomes, is 9.0% at adoption and 11.5% at year 20, 27.9% higher, and 8.4% (6.8% lower) with the in-kind value of cost relief counted as income; on the modelling paper's own measure, income below 60% of the median, it rises from 15.3% to 18.1%; the largest reduction on any measure the engine reports is net basket poverty's, 85.0% against year 0 and 87.9% against the paired Baseline, on which 2 of 500 seeds reach 90% against year 0; the simulation's own documentation states that the papers' 98% is not produced by the engine and that the model behind it is not in its repository (readings 3.3 and 3.4) | Compassionism Simulation at 5a7a7b1 (v4.20), harness.js (md5 fe6fa4a3) and index.html (md5 c333b632); cco_simulation_checks_s51_output.txt; Foster, Jolliffe, Lara Ibarra, Lakner and Tetteh-Baah, Global Poverty Revisited Using 2021 PPPs and New Data on Consumption, World Bank Policy Research Working Paper 11137 (June 2025), section 3.4.1 (PDF md5 1128f547); the simulation's CONTRIBUTING.md at 5a7a7b1 (md5 bba4ef73), v4.17 Release Notes (NEEC note 1) |
| 2 | ≥85% under stress testing | short | in the Adverse Environment, the preset the engine's documentation names for stress criteria (recessions, AI automation and 2% inflation at the reference settings), no measure falls 85% against either comparator: the largest reduction is BLEI poverty's, 57.9% against the paired Baseline; poverty on the Societal Poverty Line rises from 9.0% to 15.4%, 71.7% above its level at adoption, and is 10.5% below the Baseline's; no seed reaches 85% against year 0 on any measure, and the Stress Test preset, which also weakens the settings, gives less (reading 3.3) | Compassionism Simulation at 5a7a7b1 (v4.20), harness.js (md5 fe6fa4a3) and index.html (md5 c333b632); cco_simulation_checks_s51_output.txt; the simulation's CONTRIBUTING.md at 5a7a7b1 (md5 bba4ef73), v4.17 Release Notes (NEEC notes 5 and 6) |

*Note:* part (b3)'s unit re-checked as class I: its record read the engine's two headcounts, not v2.0's indicator, so it is re-read on the Societal Poverty Line (reading 3.3); both clauses stay short and the unit stays 0.5. Part (b3)'s flag toward 1.0, the papers' figures credited at the modelling tier, is removed: the engine now carries the papers' own measure and shows no reduction on it (reading 3.4). The unit reopens if the model behind the papers' 98% is published and reproduces it, or if a later version of the simulation reaches 90% in the reference run and 85% in the Adverse Environment on the Societal Poverty Line.

#### CCO C1.2b Prevention of Exploitative Accumulation: 1.0 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Gini <0.35 for wealth distribution | short | on the design's published model at v4.20, at the reference settings (500 seeds), the wealth Gini at year 20 is 0.518 on the engine's EDC-adjusted net wealth, the figure it reports, and 0.510 on net wealth with negative holdings counted as zero; no seed is below 0.35 on either; the Gini falls from 0.601 at adoption, so the design's mechanisms narrow the distribution, but not to the bar; the rationale's projection under 0.35 is the modelling paper's 0.28 (the median of its runs), from a model not published in runnable form, and the design's BLEI paper states that the simulation measures 0.518 (N = 5,000, v4.4), more than double its stated target of 0.25 (the engine's TARGET_GINI constant), a gap it calls large and honestly disclosed (reading 3.5) | Compassionism Simulation at 5a7a7b1 (v4.20), harness.js (md5 fe6fa4a3) and index.html (md5 c333b632); cco_simulation_checks_s51_output.txt; research hub at 8e8a6ba, economic-modeling-simulation.html (md5 86dda39b), section 5.1; research hub at 8e8a6ba, basic-living-economic-index.html (md5 0d1481fb), section 9 |

*Note:* C1.2b is class W and single-clause, outside D28's population; it is re-read because its rationale's figure is a modelled projection and the design's published model computes the quantity (reading 3.2). The design's mechanisms (conversion limits, expiring units, distributed acre equity) are genuine and lower the Gini from its level at adoption, so the unit is 0.5, not 0.0.

#### CCO C1.4 Automation Resilience: 1.0 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Poverty <8% | not shown | the rationale's figures (poverty below 5% and aggregate demand at 90-110% of baseline across the 30%, 50% and 70% scenarios) are Paper v1.4's own C1.4 measurement text for its 30% scenario, restated as a result, and no design source states them; v2.0 names the design's own model of the three scenarios as the indicator, and the published model cannot run them: its automation channel slows each agent's wage growth by at most 0.10 times the agent's automation risk a year and displaces no hours (Appendix G's standing mismatch); at its closest analogue, High Automation over 25 years, milder than the 30% scenario, poverty on the Societal Poverty Line is 15.1% at year 20 and 18.0% at year 25 (9.4% and 10.6% with in-kind relief counted as income), against 11.5% and 12.1% with automation off, and no seed is below 8% (reading 3.6) | Compassionism Simulation at 5a7a7b1 (v4.20), harness.js (md5 fe6fa4a3) and index.html (md5 c333b632); cco_simulation_checks_s51_output.txt; NEEC_Paper_v1_4.md, Appendix G (G.2, G.7); Report v1.6, CCO C1.4; NEEC_Paper_v1_4.md, section 6 (C1.4 measurement) |
| 2 | aggregate demand >85% baseline | not shown | the published model computes no final consumption; Appendix G's proxy, aggregate wage income, falls to 46.2% of the automation-off run by year 25, and aggregate cash income, which adds CCO conversion proceeds, to 47.8% (reading 3.6) | Compassionism Simulation at 5a7a7b1 (v4.20), harness.js (md5 fe6fa4a3) and index.html (md5 c333b632); cco_simulation_checks_s51_output.txt; NEEC_Paper_v1_4.md, Appendix G (G.2, G.7) |

*Note:* the audit coded both clauses A on the rationale's figures; they are located in no design source, and the design's own model contradicts them at its nearest scenario, so both A codes are departed from (reading 3.6). Paper v1.4's Appendix G found the same in kind at v3.9 to v4.2 and changed no score, because no score was then read from simulation output; C1.4 is class I, and v2.0 names the design's own model as its indicator.

#### CCO C3.2 Inflation Control Mechanisms: 1.0 → 1.0

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Long-term inflation ≤3% | cleared | inflation contained ≤3% long-term | as audited (the unit's own text) |
| 2 | stress test inflation ≤5% (when external 8%) | cleared | ≤5% during external 8% shock | as audited (the unit's own text) |
| 3 | automatic adjustment preventing runaway inflation | cleared | automatic parameter adjustment | as audited (the unit's own text) |

*Note:* re-read under reading 3.2 and carried (reading 3.8): the rationale's figures are the design's modelling, the dual-currency inflation paper's numerical simulations (0.95% a year overall in its baseline scenario, a 95% interval of 0.6% to 1.4% across 10,000 runs; research hub at 8e8a6ba, dual-currency-inflation.html (md5 329235ce), sections 5.2 and 5.4) and the framework paper's 8% scenario (local inflation held to 3.2% while national inflation reaches 8.1%; research hub at 8e8a6ba, cco-ptf-integrated-framework.html (md5 10ab8364), section 5.2); the published model computes no price, since inflation is an input rate there, and its documentation states that it assumes rather than tests that the framework is non-inflationary (the simulation's CONTRIBUTING.md at 5a7a7b1 (md5 bba4ef73), Model Architecture Feedback), so it neither supports nor contradicts them.

#### CCO C3.3 Multi-Failure Resistance: 1.0 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Maintain core functions across ≥3 of 4 compound scenarios with degradation <20% | not shown | the design's published model runs one compound scenario, the Adverse Environment (recessions, AI automation and 2% inflation at the reference settings), milder than C3.3's recession-and-automation scenario (a 30% GDP decline, 15% unemployment and 40% business closures); in it, at year 20, the share above the Societal Poverty Line is 4.4% lower than in the paired run without the shocks, under 20%, but the share not in housing distress, the engine's nearest measure to housing stability, is 28.8% lower, and essential-service and democratic-function capacity are not modelled; the other three compound scenarios are not modelled; the design's papers report single-shock stress tests (a recession of 8% of GDP, a 6% inflation surge, unemployment of 12%, a climate crisis, a cyber attack) and no compound scenario or degradation figure; the rationale's degradation under 15% in all scenarios is located in no design source (reading 3.7) | Compassionism Simulation at 5a7a7b1 (v4.20), harness.js (md5 fe6fa4a3) and index.html (md5 c333b632); cco_simulation_checks_s51_output.txt; research hub at 8e8a6ba, economic-modeling-simulation.html (md5 86dda39b), section 5.3; research hub at 8e8a6ba, cco-ptf-integrated-framework.html (md5 10ab8364), sections 4.3 and 5.3 |

*Note:* C3.3 is class W and single-clause, outside D28's population; it is re-read because its rationale's figure is a stress-test result from the design's modelling (reading 3.2). The design's distributed architecture is a genuine mechanism, so the unit is 0.5, not 0.0.

#### CCO C5.3 Partial and Parallel Deployability: 1.0 → 1.0

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Viable at ≥30% participation | cleared | Viable at 30%+ participation | as audited (the unit's own text) |
| 2 | coexistence with traditional markets maintaining ≥90% economic activity | cleared | Can coexist with traditional markets | as audited (the unit's own text) |
| 3 | scaling pathway validated through modeling | cleared | Scaling pathway validated through modeling | as audited (the unit's own text) |
| 4 | coordination protocols established | cleared | Inter-jurisdictional coordination protocols specified | as audited (the unit's own text) |

*Note:* re-read under reading 3.2 and carried (reading 3.8): the rationale's figures are the design's modelling (the framework paper: viability at 30% participation, merchant revenue at 98-102% of pre-implementation levels; research hub at 8e8a6ba, cco-ptf-integrated-framework.html (md5 10ab8364), sections 5.2 and 5.3; the modelling paper's pilot, regional and national phases, research hub at 8e8a6ba, economic-modeling-simulation.html (md5 86dda39b), section 10.1); the published model reads no aggregate participation, its 55% threshold being a run warning since v4.17, and computes neither economic activity nor a scaling path, so it neither supports nor contradicts them.

## 5. The simulation runs (from `cco_simulation_checks_s51_output.txt`)

Engine: `harness.js` at `BetterToBest/compassionism-simulation` commit `5a7a7b1` (v4.20), md5 `fe6fa4a3…`, and the
presets and recession functions of `index.html` at the same commit, md5 `c333b632…`. Before any table is read, the run
checks three things. It reproduces v4.20's seed-42 regression (median BLEI 1,975 days, BLEI poverty 13.2%, median
wealth $570,661, wealth poverty 15.8%, Gini 0.518, System Stability 88.8%). Its runner reproduces `runScenario()` on
all 500 seeds of all eight scenarios, on eleven outputs. And it reproduces the automation sweep and the refreshed
headline of v4.20's release notes (Full Integration 15.27% wealth and 12.43% BLEI poverty; High Automation 29.16% and
26.65%; Adverse Environment 38.42% and 34.92%; wealth poverty 78.6% below the shipped Baseline). N = 500 seeds (1 to
500), 500 agents; figures are seed means. "Paired Baseline" is the Baseline the engine pairs with a scenario:
recessions and automation mirrored, inflation at the shipped 3% CPI.

C1.1: poverty reduction on the engine's measures and the Societal Poverty Line.

| Scenario | Measure | Year 0 | Year 20 | Reduction vs year 0 | Seeds clearing the clause vs year 0 | Paired Baseline (3% CPI), yr 20 | Reduction vs paired Baseline |
|---|---|---:|---:|---:|---:|---:|---:|
| Reference (Full Integration) | Societal Poverty Line, cash income | 9.0% | 11.5% | none (27.9% higher) | 0 of 500 at 90% | 9.6% | none (19.2% higher) |
| Reference (Full Integration) | Societal Poverty Line, incl. in-kind relief | 9.0% | 8.4% | 6.8% | 0 of 500 at 90% | 9.6% | 13.2% |
| Reference (Full Integration) | Relative income poverty (60% of median), cash | 15.3% | 18.1% | none (18.6% higher) | 0 of 500 at 90% | 16.4% | none (10.7% higher) |
| Reference (Full Integration) | Relative income poverty, incl. in-kind relief | 15.3% | 14.7% | 3.4% | 0 of 500 at 90% | 16.4% | 9.9% |
| Reference (Full Integration) | Basket poverty, net | 66.3% | 9.9% | 85.0% | 2 of 500 at 90% | 81.9% | 87.9% |
| Reference (Full Integration) | Basket poverty, gross | 66.3% | 19.7% | 70.2% | 0 of 500 at 90% | 81.9% | 75.9% |
| Reference (Full Integration) | Wealth poverty | 37.8% | 15.3% | 59.6% | 0 of 500 at 90% | 71.5% | 78.6% |
| Reference (Full Integration) | BLEI poverty | 10.3% | 12.4% | none (20.5% higher) | 0 of 500 at 90% | 70.5% | 82.4% |
| Reference (Full Integration) | Extreme poverty (per 10,000) | 22.0 | 13.1 | 40.3% | 0 of 500 at 90% | 73.1 | 82.0% |
| Stress: Adverse Environment | Societal Poverty Line, cash income | 9.0% | 15.4% | none (71.7% higher) | 0 of 500 at 85% | 17.2% | 10.5% |
| Stress: Adverse Environment | Societal Poverty Line, incl. in-kind relief | 9.0% | 9.3% | none (3.3% higher) | 0 of 500 at 85% | 17.2% | 46.2% |
| Stress: Adverse Environment | Relative income poverty (60% of median), cash | 15.3% | 21.8% | none (42.6% higher) | 0 of 500 at 85% | 23.6% | 7.8% |
| Stress: Adverse Environment | Relative income poverty, incl. in-kind relief | 15.3% | 14.9% | 2.6% | 0 of 500 at 85% | 23.6% | 37.1% |
| Stress: Adverse Environment | Basket poverty, net | 66.3% | 58.1% | 12.4% | 0 of 500 at 85% | 95.8% | 39.4% |
| Stress: Adverse Environment | Basket poverty, gross | 66.3% | 76.6% | none (15.4% higher) | 0 of 500 at 85% | 95.8% | 20.1% |
| Stress: Adverse Environment | Wealth poverty | 37.8% | 38.4% | none (1.6% higher) | 0 of 500 at 85% | 83.6% | 54.0% |
| Stress: Adverse Environment | BLEI poverty | 10.3% | 34.9% | none (238.5% higher) | 0 of 500 at 85% | 82.9% | 57.9% |
| Stress: Adverse Environment | Extreme poverty (per 10,000) | 22.0 | 38.0 | none (72.9% higher) | 0 of 500 at 85% | 85.1 | 55.3% |
| Stress: the Stress Test preset | Societal Poverty Line, cash income | 9.0% | 17.7% | none (97.1% higher) | 0 of 500 at 85% | 17.2% | none (2.8% higher) |
| Stress: the Stress Test preset | Societal Poverty Line, incl. in-kind relief | 9.0% | 14.4% | none (60.5% higher) | 0 of 500 at 85% | 17.2% | 16.3% |
| Stress: the Stress Test preset | Relative income poverty (60% of median), cash | 15.3% | 24.2% | none (58.4% higher) | 0 of 500 at 85% | 23.6% | none (2.4% higher) |
| Stress: the Stress Test preset | Relative income poverty, incl. in-kind relief | 15.3% | 20.7% | none (35.5% higher) | 0 of 500 at 85% | 23.6% | 12.4% |
| Stress: the Stress Test preset | Basket poverty, net | 66.3% | 79.7% | none (20.2% higher) | 0 of 500 at 85% | 95.8% | 16.8% |
| Stress: the Stress Test preset | Basket poverty, gross | 66.3% | 86.1% | none (29.8% higher) | 0 of 500 at 85% | 95.8% | 10.2% |
| Stress: the Stress Test preset | Wealth poverty | 37.8% | 61.2% | none (61.9% higher) | 0 of 500 at 85% | 83.6% | 26.8% |
| Stress: the Stress Test preset | BLEI poverty | 10.3% | 59.1% | none (473.2% higher) | 0 of 500 at 85% | 82.9% | 28.7% |
| Stress: the Stress Test preset | Extreme poverty (per 10,000) | 22.0 | 61.6 | none (180.0% higher) | 0 of 500 at 85% | 85.1 | 27.6% |

The reference run at C1.1's 5-year intervals:

| Measure | Year 0 | Year 5 | Year 10 | Year 15 | Year 20 |
|---|---:|---:|---:|---:|---:|
| Societal Poverty Line, cash income | 9.0% | 8.6% | 9.5% | 10.5% | 11.5% |
| Societal Poverty Line, incl. in-kind relief | 9.0% | 5.8% | 6.5% | 7.3% | 8.4% |
| Relative income poverty (60% of median), cash | 15.3% | 15.1% | 16.3% | 17.4% | 18.1% |
| Basket poverty, net | 66.3% | 30.8% | 21.2% | 14.5% | 9.9% |
| Wealth poverty | 37.8% | 26.8% | 24.0% | 20.1% | 15.3% |

C1.2b: the wealth Gini.

| Scenario | Gini | Year 0 | Year 10 | Year 20 | Seeds below 0.35 at year 20 |
|---|---|---:|---:|---:|---:|
| Reference (Full Integration) | EDC-adjusted (the engine's KPI) | 0.702 | 0.573 | 0.518 | 0 of 500 |
| Reference (Full Integration) | net wealth, negatives at zero | 0.601 | 0.557 | 0.510 | 0 of 500 |
| Baseline (3% CPI) | EDC-adjusted (the engine's KPI) | 0.746 | 0.812 | 0.857 | 0 of 500 |
| Baseline (3% CPI) | net wealth, negatives at zero | 0.601 | 0.793 | 0.849 | 0 of 500 |

C1.4, Appendix G's protocol: Full Integration with automation off and High Automation, both 25 years.

| Year | Full Integration, automation off: SPL poverty (cash / in-kind) | High Automation: SPL poverty (cash / in-kind) | Wealth poverty, off / on | Basket poverty (net), off / on | Aggregate wage income, on / off | Aggregate cash income, on / off |
|---:|---:|---:|---:|---:|---:|---:|
| 5 | 8.6% / 5.8% | 8.6% / 5.8% | 26.8% / 26.8% | 30.8% / 30.8% | 100.0% | 100.0% |
| 10 | 9.5% / 6.5% | 9.6% / 6.6% | 24.0% / 25.4% | 21.2% / 26.4% | 90.2% | 90.7% |
| 15 | 10.5% / 7.3% | 11.9% / 7.9% | 20.1% / 25.7% | 14.5% / 32.2% | 70.9% | 72.0% |
| 20 | 11.5% / 8.4% | 15.1% / 9.4% | 15.3% / 27.1% | 9.9% / 40.9% | 56.2% | 57.7% |
| 25 | 12.1% / 9.4% | 18.0% / 10.6% | 10.9% / 29.2% | 6.8% / 48.6% | 46.2% | 47.8% |

C3.3: the Adverse Environment against the paired run without shocks, at the reference settings.

| Core function (share of the population) | Year | Full Integration, no shock | Adverse Environment | Degradation |
|---|---:|---:|---:|---:|
| above the Societal Poverty Line (cash income) | 10 | 90.5% | 90.3% | 0.2% |
| above the Societal Poverty Line (cash income) | 20 | 88.5% | 84.6% | 4.4% |
| above the SPL, incl. in-kind relief | 10 | 93.5% | 93.4% | 0.1% |
| above the SPL, incl. in-kind relief | 20 | 91.6% | 90.7% | 1.0% |
| above the wealth-poverty line | 10 | 76.0% | 68.8% | 9.4% |
| above the wealth-poverty line | 20 | 84.7% | 61.6% | 27.3% |
| out of basket poverty (net) | 10 | 78.8% | 63.3% | 19.7% |
| out of basket poverty (net) | 20 | 90.1% | 41.9% | 53.5% |
| not in housing distress (the nearest measure to housing stability) | 10 | 82.3% | 73.4% | 10.8% |
| not in housing distress (the nearest measure to housing stability) | 20 | 90.4% | 64.4% | 28.8% |

To rerun: clone `BetterToBest/compassionism-simulation`, check out `5a7a7b1`, and run
`node cco_simulation_checks_s51.js path/to/harness.js path/to/index.html` (about one minute); the output is
byte-identical to the capture (md5 `b4f481e7…`).

## 6. What parts (a), (b) and group 2.1 change (generated)

Computed on the published 26-criterion structure with every re-estimate of parts (a) and (b), decision 48.3 and this
group in force. No corpus file changes until the pass is applied.

| Entry | Published (rank) | After part (b) (rank) | After group 2.1 (rank) | Change here | Failures | Tier |
|---|---:|---:|---:|---:|---:|---|
| CCO | 24.5 (1) | 17.0 (1) | 15.5 (1) | -1.5 | 0 | Potentially Adequate |
| PE | 20.5 (2) | 14.5 (2) | 14.5 (2) | 0.0 | 1 | Potentially Adequate |
| NSD | 19.5 (3) | 13.5 (4) | 13.5 (4) | 0.0 | 2 | Potentially Adequate |
| INT | 19.5 (3) | 14.5 (2) | 14.5 (2) | 0.0 | 3 | Partially Adequate |
| DG | 19.0 (5) | 13.5 (4) | 13.5 (4) | 0.0 | 2 | Potentially Adequate |
| MS | 16.5 (6) | 13.5 (4) | 13.5 (4) | 0.0 | 2 | Potentially Adequate |
| MMT | 15.5 (7) | 11.5 (13) | 11.5 (13) | 0.0 | 3 | Partially Adequate |
| UBI | 14.5 (8) | 11.0 (15) | 11.0 (15) | 0.0 | 7 | Structurally Inadequate |
| MC | 14.5 (8) | 12.5 (8) | 12.5 (8) | 0.0 | 3 | Partially Adequate |
| OS | 14.5 (8) | 13.0 (7) | 13.0 (7) | 0.0 | 3 | Partially Adequate |
| SWF | 14.0 (11) | 12.5 (8) | 12.5 (8) | 0.0 | 3 | Partially Adequate |
| SG | 14.0 (11) | 12.0 (11) | 12.0 (11) | 0.0 | 4 | Partially Adequate |
| GEO | 13.5 (13) | 12.5 (8) | 12.5 (8) | 0.0 | 2 | Potentially Adequate |
| UBS | 13.5 (13) | 12.0 (11) | 12.0 (11) | 0.0 | 3 | Partially Adequate |
| IF | 13.5 (13) | 11.5 (13) | 11.5 (13) | 0.0 | 5 | Partially Adequate |
| FALC | 13.0 (16) | 9.5 (16) | 9.5 (16) | 0.0 | 10 | Structurally Inadequate |
| DE | 11.5 (17) | 9.0 (19) | 9.0 (19) | 0.0 | 8 | Structurally Inadequate |
| SQ | 10.5 (18) | 9.5 (16) | 9.5 (16) | 0.0 | 9 | Structurally Inadequate |
| CPS | 10.0 (19) | 7.5 (22) | 7.5 (22) | 0.0 | 12 | Structurally Inadequate |
| SC | 10.0 (19) | 8.5 (20) | 8.5 (20) | 0.0 | 9 | Structurally Inadequate |
| CN | 10.0 (19) | 9.5 (16) | 9.5 (16) | 0.0 | 8 | Structurally Inadequate |
| QA | 9.0 (22) | 8.0 (21) | 8.0 (21) | 0.0 | 10 | Structurally Inadequate |
| LM | 8.0 (23) | 6.0 (23) | 6.0 (23) | 0.0 | 15 | Structurally Inadequate |

After this group the corpus has 21 dominance pairs against 22 after part (b) (new: none; lost: CCO>DG), and its frontier holds 14 entries against 13 (SQ, NSD, MS, LM, UBI, DG, FALC, PE, CCO, INT, MC, SWF, IF, OS). First place: CCO, 17.0 after part (b), 15.5 now, ahead of PE, INT at 14.5. Across the pass so far 152 units have been re-estimated, each counted once: 16 stand and 136 are at 0.5 (68.0 points).

Flags added in this group: none; removed: 1 (CCO C1.1, the flag toward 1.0 that part (b3) added; reading 3.4). Flags added by the pass so far: 22 (against 23 before this group); removed from the published registers: 7. CCO-PTF-CIP-SZH's published register holds no flag; the pass's flags on it are now on C3.4, C5.2 (before this group: C1.1, C3.4, C5.2).

After this group C1.1 keeps 0 scores of 1.0 (none); C1.2b keeps 4 scores of 1.0 (DG, PE, INT, MC); C1.4 keeps 1 score of 1.0 (UBI); C3.2 keeps 3 scores of 1.0 (CCO, CN, SG); C3.3 keeps 3 scores of 1.0 (DG, PE, INT); C5.3 keeps 7 scores of 1.0 (SQ, CCO, GEO, UBS, SWF, IF, OS). After parts (a), (b) and this group no entry scores 1.0 on 9 criteria: C1.1 (emptied in part (b3)), C2.1 (emptied in part (b4)), C2.3 (emptied in part (b1)), C2.4 (emptied in part (b1)), C3.1 (emptied in part (b2)), C3.5 (emptied in part (b6)), C4.1 (emptied in part (b6)), C4.2 (emptied in part (b7)), C4.3 (emptied in part (b8)).

Anchor examples citing a unit the pass moves: C1.1's 1.0 example, NSD (part (b3)); C1.2b's 1.0 example, CCO (part (2.1)); C1.4's 1.0 example, CCO (part (2.1)); C2.1's 1.0 example, UBI (part (a)); C2.3's 1.0 example, DG (part (b1)); C2.4's 1.0 example, PE (part (b1)); C2.5's 1.0 example, CCO (part (b5)); C3.1's 1.0 example, UBI (part (b2)); C3.2's 1.0 example, PE (part (b4)); C3.5's 1.0 example, CCO (part (b6)); C4.1's 1.0 example, DG (part (b6)); C4.2's 1.0 example, PE (part (b7)); C4.3's 1.0 example, CCO (part (b8)); C5.1's 1.0 example, MS (part (b2)); C5.2's 1.0 example, CCO (part (b9)); C5.4's 1.0 example, CCO (part (b9)); C5.5's 1.0 example, PE (part (b9)). Bands whose example the pass moves and which no corpus unit then scores at their value: C1.1's 1.0, C2.1's 1.0, C2.3's 1.0, C2.4's 1.0, C3.1's 1.0, C3.5's 1.0, C4.1's 1.0, C4.2's 1.0, C4.3's 1.0.

**The score ledger.** Each entry's published total, each part's change, and its total now. "Re-estimated" counts the
entry's units in the pass, each once; "At 0.5" counts those now at 0.5.

| Entry | Published | (a) | (b1) | (b2) | (b3) | (b4) | (b5) | (b6) | (b7) | 48.3 | (b8) | (b9) | (2.1) | Now | Re-estimated | At 0.5 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| CCO | 24.5 | -0.5 | -1.5 | -0.5 | -0.5 | -0.5 | -0.5 | -1.0 | -0.5 | -0.5 | -0.5 | -1.0 | -1.5 | 15.5 | 20 | 18 |
| PE | 20.5 |  | -1.5 | -0.5 | -0.5 | -1.5 |  | -0.5 | -0.5 |  | -0.5 | -0.5 |  | 14.5 | 13 | 12 |
| NSD | 19.5 | -2.5 | -1.0 | -0.5 | -0.5 | -0.5 |  |  |  |  | -0.5 | -0.5 |  | 13.5 | 13 | 12 |
| INT | 19.5 | -0.5 | -1.0 | -0.5 |  | -1.0 | -0.5 | -1.0 | -0.5 |  |  |  |  | 14.5 | 12 | 10 |
| DG | 19.0 |  | -1.5 | -0.5 | -0.5 | -0.5 |  | -0.5 | -1.0 |  | -1.0 |  |  | 13.5 | 11 | 11 |
| MS | 16.5 | -1.0 | -1.5 | -0.5 | -0.5 |  |  |  | 0.5 |  |  |  |  | 13.5 | 8 | 6 |
| MMT | 15.5 | -1.5 | -1.0 | -0.5 | -0.5 |  |  |  |  |  | -0.5 |  |  | 11.5 | 8 | 8 |
| UBI | 14.5 | -1.5 | -0.5 | -0.5 | -0.5 |  |  |  |  |  | -0.5 |  |  | 11.0 | 8 | 7 |
| MC | 14.5 |  | -1.0 | -0.5 |  |  | -0.5 |  |  |  |  |  |  | 12.5 | 5 | 4 |
| OS | 14.5 | -0.5 |  |  |  |  | -0.5 | -0.5 |  |  |  |  |  | 13.0 | 4 | 3 |
| SWF | 14.0 |  |  | -0.5 |  |  | -0.5 | -0.5 |  |  |  |  |  | 12.5 | 4 | 3 |
| SG | 14.0 | -1.0 | -0.5 | -0.5 |  |  |  |  |  |  |  |  |  | 12.0 | 4 | 4 |
| GEO | 13.5 | -0.5 |  |  |  |  | -0.5 |  |  |  |  |  |  | 12.5 | 2 | 2 |
| UBS | 13.5 |  | -0.5 | -0.5 |  |  | -0.5 |  |  |  |  |  |  | 12.0 | 4 | 3 |
| IF | 13.5 | -1.0 |  |  |  |  | -0.5 |  |  |  |  | -0.5 |  | 11.5 | 4 | 4 |
| FALC | 13.0 | -0.5 | -0.5 |  | -0.5 | -1.0 |  | -0.5 | -0.5 |  |  |  |  | 9.5 | 8 | 7 |
| DE | 11.5 | -0.5 | -0.5 |  |  |  | -0.5 | -0.5 | -0.5 |  |  |  |  | 9.0 | 5 | 5 |
| SQ | 10.5 | -0.5 |  |  |  | -0.5 |  |  |  |  |  |  |  | 9.5 | 3 | 2 |
| CPS | 10.0 | -1.5 |  |  | -0.5 |  |  |  |  |  | -0.5 |  |  | 7.5 | 5 | 5 |
| SC | 10.0 |  | -1.0 |  |  |  |  |  |  |  |  | -0.5 |  | 8.5 | 3 | 3 |
| CN | 10.0 |  |  | -0.5 |  |  |  |  |  |  |  |  |  | 9.5 | 1 | 1 |
| QA | 9.0 | -0.5 |  | -0.5 |  |  |  |  |  |  |  |  |  | 8.0 | 2 | 2 |
| LM | 8.0 | -1.5 |  |  |  |  |  |  |  |  |  | -0.5 |  | 6.0 | 5 | 4 |

## 7. Corrections found (not polish)

1. **CCO-PTF-CIP-SZH's C1.4 rationale** states as a stress-testing result Paper v1.4's own C1.4 measurement figures for
   the 30% scenario (poverty under 5%, aggregate demand at 90-110% of baseline). No design source states them, and the
   design's published model contradicts them at its nearest scenario (reading 3.6). Report v2.0 cites the model's
   figures.
2. **Its C3.3 rationale's** "Degradation <15% in all scenarios" is located in no design source; the design's papers
   report single-shock tests only (reading 3.7).
3. **Its C1.2b and C4.4 rationales'** "wealth Gini projected under 0.35" is the modelling paper's 0.28, which the
   design's BLEI paper states the published simulation does not reproduce: it measures 0.518 (reading 3.5). Report v2.0
   gives the published model's figure.
4. **Anchor examples.** C1.2b's and C1.4's 1.0 examples cite CCO-PTF-CIP-SZH (section 6). When the pass is applied
   they are replaced with units still at 1.0 (Integral and three others on C1.2b; Universal Basic Income on C1.4), as
   part (b3)'s reading 3.5 set for moved examples; neither band is left empty.
5. **Paper v1.4 Appendix G.2** describes C1.4's stress test as "maintain poverty <5% and aggregate demand 90-110%
   baseline" at 30%, 50% and 70% "of the population" displaced. v2.0's clause is poverty under 8% and aggregate demand
   above 85% of baseline, in scenarios displacing 30%, 50% and 70% of baseline paid working hours. Paper v2.0's
   Appendix G states v2.0's clause (section 8).

## 8. Paper v1.4 Appendix G.7, Run Record #4 (for Paper v2.0)

Appendix G.7 is append-only; Run #4 was to be logged "once the simulation's next substantive update (automation
mechanics, wage growth, or poverty/Gini calculation) ships". v4.20 recalibrated the automation mechanics, and v4.17 and
v4.18 changed the poverty calculations. The text below is for Paper v2.0's Appendix G, after Run #3, which it does not
edit.

**Run #4 — v4.20, September 2026 (Session 51).** *Trigger:* v4.20 recalibrated `automationRisk` (high-risk weight 0.47
to 0.63, matched to Frey and Osborne's employment-weighted mean of 0.592, and sampled by inverse CDF so that the weight
moves no other draw); v4.17 and v4.18 added income, basket and extreme-poverty measures. *Method:* literal execution of
the simulation's own `harness.js` under Node.js, pinned by digest, not a re-implementation. The protocol's Step 4
preference for the tool's own output is met more directly than a CSV export would meet it: the runner reproduces
`runScenario()` exactly and the release notes' N = 500 figures (`cco_simulation_checks_s51.js`). 500 seeds, Full
Integration with automation off and High Automation (the page's `hiAI` preset), 25 years.
*Constants and dead code (Steps 2 and 3):* `AI_DISPLACEMENT_YEAR_1/2` = 5 and 15, `AI_DISPLACEMENT_RATE_1/2` = 0.012
and 0.022, and the cap `Math.min(0.10, popAIDisp)` are unchanged. The cap is reached in year 13 (0-indexed), and the
year-15 branch starts at 0.142, above it, so **`AI_DISPLACEMENT_RATE_2` still moves no output** (Runs #1 to #3:
*still open*). `SZH_PTF_BONUS` is still defined and read by no formula (Run #2: *still open*). The SZH synergy is still
gated on the coherence slider, now disclosed in the model as a proxy (v4.17: *changed*, disclosed).
*Framing (G.2):* the model still has no displacement-fraction lever. Automation remains a wage-growth drag of at most
0.10 times each agent's risk a year, and no agent loses hours (*still open*). *Results (Step 4, seed means):* poverty
on the Societal Poverty Line, v2.0's C1.4 measure, at years 20 and 25 is 11.5% and 12.1% without automation, and 15.1%
and 18.0% with it (9.4% and 10.6% counting in-kind relief); no seed is below 8% at year 25. Wealth poverty is 27.1%
and 29.2% with automation, against 15.3% and 10.9% without. Aggregate wage income with automation falls to 56.2% of
the automation-off run at year 20 and 46.2% at year 25; aggregate cash income, with conversion proceeds, to 57.7% and
47.8% (Run #2: 40.7% to 41.0% at year 25, with v4.1's uniform risk draw). *Status against C1.4 (Step 5):* unchanged in kind. The
model cannot produce the 30%, 50% or 70% scenarios. At its closest analogue, milder than the 30% scenario, poverty
exceeds 8% on every measure it reports and on the Societal Poverty Line, and the demand proxy is far below 85% of
baseline. *Changed in consequence:* the rescoring pass now reads a design's own model as C1.4's indicator (v2.0), and
CCO-PTF-CIP-SZH's C1.4 is re-estimated at 0.5 (`NEEC_Rescoring_s51.md`, reading 3.6). *Still recommended:* a lever
that displaces hours, so the scenarios can be run; the Acre-Equity ablation of Run #2, still outstanding.

## 9. Notes for the simulation's maintainers (the owner's project; not NEEC corrections)

Handoff 40's ten notes, at v4.20: **answered** — 2 (income and basket measures, v4.17; extreme poverty, v4.18), 3 and
4 (explained: the wage-to-basket calibration, and a measurement effect plus a transient; reported against year 0), 5
(recessions in `harness.js`), 6 (the Adverse Environment preset), 7 (relabelled a design reference), 8 (the parity
fix), 10 (each release states its regression); **open, as decisions logged for the owner** — 1 (the papers' 98% and
$82,000, now disclosed as not produced by the engine) and 9 (an endogenous price channel, logged, not built). Three
further notes, for whoever works on v4.21:

1. **A Societal Poverty Line headcount**, max($3.00, $1.30 + half the median) a day in 2021 PPP, would report NEEC
   v2.0's C1.1 measure directly. On the engine's cash incomes it rises from 9.0% at adoption to 11.5% at year 20 in the
   reference run (section 5).
2. **A lever that displaces hours** (a share of paid working hours removed, with no assumption about timing) would let
   the model run C1.4's 30%, 50% and 70% scenarios, which its wage-growth drag cannot reach (section 8).
3. **A compound-scenario report** for C3.3's four scenarios, with the degradation of each core function against the
   same run without the shocks, would test the design's multi-failure claim. The engine now runs one of the four.

## 10. Disclosure

CCO-PTF-CIP-SZH is the owner's design, and this group is about it alone. That follows from the scan: of 27 rationales
that name modelling, only the design's nine rest on the entry's own modelled figures, because only the design publishes
a model of its own. Publishing the model is to the design's credit, and its maintainers' disclosures made several of
these readings possible (v4.17's, and the BLEI paper's on the Gini). The group is not a penalty for publishing. Every
reading here would apply to any entry with a model of its own: where the model computes a rationale's figure, it
governs, and a figure no source states is not evidence. Three of the design's units fall from 1.0 to 0.5, two stand,
and C1.1 loses its flag toward 1.0. It keeps first place, at 15.5 on the 26 published criteria. The owner told the
scorer that v4.20 has features that could alter the design's scores. None raises a score here. The stabilizers bear on
C3.1, whose verdict is fixed by coverage, and the new poverty measures show on C1.1's own line what the older ones
showed.

## 11. What remains

- **Stage 2's class M re-checks**, in Handoff 50's order: C5.2's sixteen units at 0.5 or 0.0 on part (b9)'s reading
  3.2 (they can rise); C4.3's other sixteen units on part (b8)'s readings 3.2 to 3.5, with Status Quo, China, Singapore
  and Qatar on national household survey series; C4.4's seventeen units on decision 48.3; C4.1's four part (b6) units
  (FALC, PE, INT, SWF) on its debt clause; then every other unit of C1.2a, C1.3, C3.4, C4.1, C4.2, C4.3 and C5.2 not
  yet read on v2.0 (Handoff 47, section 7), the design's C1.2a and C1.3 among them (reading 3.10).
- **Then** the class D rises (25 units at 0.5), the class I re-checks (the 42 units of the configured national
  economies, and any other unit whose record cites a different measure), and the 69 new units.
- **(c)** the 131 mechanism-class 0.5s against D29; **(d)** D31's source for Ostrom's community land trusts; **(e)** the
  Islamic finance and Ostrom documents' quoted thresholds restated.
- **For Report v2.0:** section 7's corrections; the clauses earlier groups left not estimated; and the flags of parts
  (b9) and 50.6.

## 12. What this record does not show

It re-estimates six units on the design's published model and sources as they stood on 2026-09-26. The model's figures
are the model's, at the modelling tier: 500 single-adult agents with no taxes or transfers, prices set as an input,
and automation as a wage-growth drag. The Societal Poverty Line computed here is the scorer's application of the
World Bank's formula to the engine's incomes, not a figure the simulation reports. "Not shown" means that no evidence
was located, not that the clause fails. A published model behind the papers' figures, a displacement lever, or a
compound-scenario report could reopen C1.1, C1.4 or C3.3 (sections 3.4, 8 and 9). A later version that computes prices
could bear on C3.2 and C3.4. The interpretation check (decisions 50.1 to 50.4) was not run on this group, whose
readings turn on the published model's computed figures, not on how a text is read. The record is one scorer's
re-estimation; whether its calls reproduce is what the replication programme tests.
