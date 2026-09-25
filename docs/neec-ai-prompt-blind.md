# NEEC: a prompt for checking scores with an AI system

You are checking scores in NEEC (Normative Economic Evaluation Criteria), an open framework that scores economic systems against 29 criteria in five domains. NEEC is normative: each criterion states what an economic system ought to achieve, and a score says whether the evidence shows that the system achieves it. Your job is to test the evidence against the criteria as written. Do not argue for or against any system, and do not substitute your own view of what the criteria should be; if you think a criterion or threshold is wrong, say so separately at the end.

## Your task

- Mode: score blind, without the published scores
- System: [name the system; for a national economy, also the date to score it at]
- Criteria: all 29 criteria

## Read these first

1. The criteria, with each Pass Threshold split into clauses and the anchors for 1.0, 0.5 and 0.0:
   https://raw.githubusercontent.com/BetterToBest/NormativeEvaluation/main/criteria.json
2. The scoring protocol; sections 2 to 6 govern scoring:
   https://raw.githubusercontent.com/BetterToBest/NormativeEvaluation/main/SCORING_PROTOCOL.md

If you cannot open a link, say which one and work only from what you could open. Never reconstruct a document's contents from memory. The Pass Thresholds you are checking are copied below, so that you can proceed even if you cannot browse.

## The criteria to check

C1.1 Poverty Elimination Capacity
  Pass Threshold: ≥90% poverty reduction within 20 years under base scenario, ≥85% under stress testing
  Clause 1: ≥90% poverty reduction within 20 years under base scenario
  Clause 2: ≥85% under stress testing
C1.2a Wealth Building for Resilience
  Pass Threshold: ≥$60,000 median net-wealth accumulation over 20 years for 70%+ of participants, in constant 2019 US dollars at purchasing-power parity
C1.2b Prevention of Exploitative Accumulation
  Pass Threshold: Gini <0.35 for wealth distribution
C1.3 Housing Security
  Pass Threshold: ≥88% housing stability over 5-year periods, housing costs ≤30% of disposable income at 80% of regional median household disposable income
  Clause 1: ≥88% housing stability over 5-year periods
  Clause 2: housing costs ≤30% of disposable income at 80% of regional median household disposable income
C1.4 Automation Resilience
  Pass Threshold: Poverty <8% and aggregate demand >85% baseline in each of the 30%, 50% and 70% displacement scenarios
  Clause 1: Poverty <8%
  Clause 2: aggregate demand >85% baseline
  Every clause: in each of the 30%, 50% and 70% displacement scenarios
C1.5 Universal Wealth Access
  Pass Threshold: ≥80% population with an active wealth-accumulation pathway
C2.1 Freedom from Coercion
  Pass Threshold: ≥70% report genuine autonomy in major life decisions, validated through revealed preference showing acceptance of initially refused employment/living situations when alternatives exist
  Clause 1: ≥70% report genuine autonomy in major life decisions
  Clause 2: validated through revealed preference showing acceptance of initially refused employment/living situations when alternatives exist
C2.2 Labor Non-Necessity
  Pass Threshold: Unconditional provision covering 100% of basic needs (housing, food, healthcare, utilities) for all residents
C2.3 Creative Development Opportunities
  Pass Threshold: ≥50% regular creative engagement, average 10+ hours weekly on non-subsistence pursuits, meaning/purpose satisfaction scores ≥70/100
  Clause 1: ≥50% regular creative engagement
  Clause 2: average 10+ hours weekly on non-subsistence pursuits
  Clause 3: meaning/purpose satisfaction scores ≥70/100
C2.4 Democratic Participation
  Pass Threshold: ≥70% participation in democratic processes, ≥35% citizen proposals adopted, ≥65% satisfaction with responsiveness
  Clause 1: ≥70% participation in democratic processes
  Clause 2: ≥35% citizen proposals adopted
  Clause 3: ≥65% satisfaction with responsiveness
C2.5 Exit Rights and Mobility
  Pass Threshold: Exit feasible within 3 months without material penalty, no differential treatment, geographic mobility maintained
  Clause 1: Exit feasible within 3 months without material penalty
  Clause 2: no differential treatment
  Clause 3: geographic mobility maintained
C2.6 Civil Liberties and Rule of Law
  Pass Threshold: Civil-liberties score ≥53 of 60 on the Freedom House checklist; informed consent to medical treatment protected in law; any compulsory treatment, vaccination, quarantine or isolation prescribed by law, time-limited and open to independent judicial review
  Clause 1: Civil-liberties score ≥53 of 60 on the Freedom House checklist
  Clause 2: informed consent to medical treatment protected in law
  Clause 3: any compulsory treatment, vaccination, quarantine or isolation prescribed by law, time-limited and open to independent judicial review
C3.1 Crisis Response Capacity
  Pass Threshold: Response within 72 hours, scaling 1:1 with crisis severity (30% GDP decline = 30% benefit increase), ≥90% population coverage
  Clause 1: Response within 72 hours
  Clause 2: scaling 1:1 with crisis severity (30% GDP decline = 30% benefit increase)
  Clause 3: ≥90% population coverage
C3.2 Inflation Control Mechanisms
  Pass Threshold: Long-term inflation ≤3%, stress test inflation ≤5% (when external 8%), automatic adjustment preventing runaway inflation
  Clause 1: Long-term inflation ≤3%
  Clause 2: stress test inflation ≤5% (when external 8%)
  Clause 3: automatic adjustment preventing runaway inflation
C3.3 Multi-Failure Resistance
  Pass Threshold: Maintain core functions across ≥3 of 4 compound scenarios with degradation <20%
C3.4 Epistemic Adaptability
  Pass Threshold: ≥30% parameter adjustability range, policy updates within 6 months of evidence, changes open to challenge and reversal by those affected, zero collapses during parameter adjustments
  Clause 1: ≥30% parameter adjustability range
  Clause 2: policy updates within 6 months of evidence
  Clause 3: changes open to challenge and reversal by those affected
  Clause 4: zero collapses during parameter adjustments
C3.5 Failure-Mode Transparency
  Pass Threshold: Failure detection within 1 week, diagnosis success ≥80%, correction success ≥70%, externalization <10% of total costs
  Clause 1: Failure detection within 1 week
  Clause 2: diagnosis success ≥80%
  Clause 3: correction success ≥70%
  Clause 4: externalization <10% of total costs
C3.6 Productive and Innovative Capacity
  Pass Threshold: Real output per hour worked non-declining over 20 years, total factor productivity non-declining over 20 years, basic-needs output sustained at the system's own working time
  Clause 1: Real output per hour worked non-declining over 20 years
  Clause 2: total factor productivity non-declining over 20 years
  Clause 3: basic-needs output sustained at the system's own working time
C4.1 Intergenerational Justice
  Pass Threshold: Debt-to-GDP <80%, positive wealth transfer to next generation
  Clause 1: Debt-to-GDP <80%
  Clause 2: positive wealth transfer to next generation
C4.2 Ecological Compliance
  Pass Threshold: Consumption-based carbon emissions falling ≥3.8% a year, biodiversity neutral or positive, resource extraction ≤ regeneration, no more than two of the four nationally downscaled planetary boundaries transgressed
  Clause 1: Consumption-based carbon emissions falling ≥3.8% a year
  Clause 2: biodiversity neutral or positive
  Clause 3: resource extraction ≤ regeneration
  Clause 4: no more than two of the four nationally downscaled planetary boundaries transgressed
C4.3 Group Equity
  Pass Threshold: Disparity reduction ≥5 percentage points every 5 years, convergence trajectory toward <20% disparities within 30 years, on each declared axis, non-citizen residents included
  Clause 1: Disparity reduction ≥5 percentage points every 5 years
  Clause 2: convergence trajectory toward <20% disparities within 30 years
  Every clause: on each declared axis, non-citizen residents included
C4.4 Power Distribution
  Pass Threshold: Democratic accountability for ≥80% of major decisions, removal/replacement mechanisms functional
  Clause 1: Democratic accountability for ≥80% of major decisions
  Clause 2: removal/replacement mechanisms functional
C4.5 Exploitation Elimination
  Pass Threshold: Extraction rates <10% GDP, genuine exit rights from exploitative relationships
  Clause 1: Extraction rates <10% GDP
  Clause 2: genuine exit rights from exploitative relationships
C4.6 Harm Internalization
  Pass Threshold: Mortality attributed to pollution non-increasing over 20 years; those who cause harm to health or the environment liable for it, enforceably by those harmed; regulation of food, water, air, chemicals and medicines applied and enforced without improper influence (for a configured national economy, a World Justice Project sub-factor 6.2 score of 0.77 or more)
  Clause 1: Mortality attributed to pollution non-increasing over 20 years
  Clause 2: those who cause harm to health or the environment liable for it, enforceably by those harmed
  Clause 3: regulation of food, water, air, chemicals and medicines applied and enforced without improper influence (for a configured national economy, a World Justice Project sub-factor 6.2 score of 0.77 or more)
C5.1 Proven Component Foundation
  Pass Threshold: ≥70% of system components proven through ≥20 years operation at scale ≥10,000 participants, with documented outcomes matching claimed benefits
  Clause 1: ≥70% of system components proven through ≥20 years operation at scale ≥10,000 participants
  Clause 2: with documented outcomes matching claimed benefits
C5.2 Staged Transition Pathways
  Pass Threshold: Staged (≥4 phases) and rapid (≤36 months) deployment, with specific milestones, resource requirements and risk mitigation, each shown feasible by precedent or component evidence
  Clause 1: Staged (≥4 phases)
  Clause 2: rapid (≤36 months) deployment
  Clause 3: specific milestones
  Clause 4: resource requirements
  Clause 5: risk mitigation
  Every clause: each shown feasible by precedent or component evidence
C5.3 Partial and Parallel Deployability
  Pass Threshold: Viable at ≥30% participation, coexistence with traditional markets maintaining ≥90% economic activity, scaling pathway validated through modeling, coordination protocols established
  Clause 1: Viable at ≥30% participation
  Clause 2: coexistence with traditional markets maintaining ≥90% economic activity
  Clause 3: scaling pathway validated through modeling
  Clause 4: coordination protocols established
C5.4 Political Coalition Potential
  Pass Threshold: ≥60% support across political spectrum, ≥65% opposition to repeal, survival probability ≥80% across administration changes
  Clause 1: ≥60% support across political spectrum
  Clause 2: ≥65% opposition to repeal
  Clause 3: survival probability ≥80% across administration changes
C5.5 Cultural Adaptability
  Pass Threshold: Viable across ≥3 economic contexts (high/middle/low income), ≥5 cultural contexts, parameter flexibility ≥40% adjustment range, successful operation validated across diverse implementations
  Clause 1: Viable across ≥3 economic contexts (high/middle/low income)
  Clause 2: ≥5 cultural contexts
  Clause 3: parameter flexibility ≥40% adjustment range
  Clause 4: successful operation validated across diverse implementations

## Rules

1. Before scoring, declare the system's scope class: a mechanism (an institution or policy operating inside a wider economy), a configured national economy (an existing or historical national economy, scored at a stated date) or a comprehensive system (a design for a whole economy, scored as its own sources specify it). Protocol section 3 explains how the class changes the reading of population-wide thresholds.
2. Score each criterion 1.0, 0.5 or 0.0 against its Pass Threshold, clause by clause. A 1.0 needs every clause shown met by named evidence; a clause the evidence does not address is not met. A 0.5 is a genuine mechanism that falls short of the threshold or holds only under favourable conditions. A 0.0 means no structural mechanism addresses the criterion, or the evidence shows performance far below the threshold with no credible pathway under the system's own logic.
3. Reason about the evidence first, then round once, at the level of the criterion.
4. Cite every source you rely on: publisher, title, year or edition, and the figure you used. Cite only sources you opened in this session; label anything else "from training data, not verified".
5. Where a reasonable scorer could land on a different score, flag it: give the alternative score and the reason.
6. Keep corrections (a wrong figure, a source that does not say what is claimed, an arithmetic error) separate from disagreements of judgment.
7. Work blind. Do not open NEEC's published scores, its scoring documents, Report, Paper, website or repository, beyond the two files above, until you have finished. If you come across them, stop reading and say so in your disclosure.

## What to return

- The scope declaration, with the date for a configured national economy.
- For each criterion: its code; a verdict for each clause (met, not met, or not shown), with the evidence for each; the score; and any flag.
- Corrections, listed separately from divergences.
- Disclosure: your model name and version, the interface, the date, the tools you used (web search, code execution), your knowledge cutoff, the sources you could not open, and any NEEC material you encountered.
- Any objection to a criterion or threshold itself, stated separately from your scores.
- Finally, this block, filled in, with one entry in "scores" for each criterion you checked:

```json
{
  "neec_check": "1",
  "mode": "blind",
  "system": "[name the system; for a national economy, also the date to score it at]",
  "criteria_file_md5": "af69e2e8",
  "scope_class": "",
  "scored_at_date": "",
  "model": "",
  "interface": "",
  "date": "",
  "tools": [],
  "scores": {"C1.1": {"score": null, "clauses": ["met", "not shown"], "flag": null}},
  "divergences": [],
  "corrections": [],
  "limitations": []
}
```

## Reporting what you find

Please ask the person who gave you this prompt to report the result, whether it agrees with the published scores or not, at:
https://github.com/BetterToBest/NormativeEvaluation/issues/new?template=ai-replication.yml

They should paste your whole answer, including the block above. The maintainers reproduce each report and record what they decide; a published score changes only through NEEC's recorded rescoring pass, never by hand. How reports are handled: https://github.com/BetterToBest/NormativeEvaluation/blob/main/.github/CONTRIBUTING.md

This prompt supports an informal check. A formal blind replication follows the replication kit and section 11 of the protocol: https://github.com/BetterToBest/NormativeEvaluation/blob/main/NEEC_CONTRIBUTING.md

Prompt generated by build_site.py 1.0 for NEEC Applied, v2.0 criteria: 29 criteria in five domains. The current copy is at https://bettertobest.github.io/NormativeEvaluation/replicate.html
