# NEEC Rescoring Pass — Record, Part (a): The 33 Stated-Shortfall 1.0s

**Session 37 · 2026-09-22 · Scorer and engineer: Claude · Owner: Duke Johnson**
**Status: scratch (protocol 10.1). Part (a) is complete; parts (b) to (e) follow in later sessions.** No corpus
file, score or scoring document changes until the pass ends. Its changes are then applied by generator with
pinned inputs and restated in place (protocol 10.2, 10.3; decisions D12, D14), and until then the published
totals stand, provisional as `README.md` says. Decisions taken here are Claude's under the owner's delegation
(Handoff 35, section 2); each is recorded with its reasons, and the owner may reverse any of them.
**Reproduce:** `python3 rescoring_s37.py` (harness check 80). The script holds every clause estimate below,
checks the population against the R4 audit's register and every verdict against decision D28, computes every
figure in section 5, and checks that this record contains its generated tables verbatim.

---

## 1. What part (a) is

The R4 audit (`NEEC_R4_MultiClause_Audit_s35.md`) found that 134 of the corpus's 167 multi-clause 1.0s do not
show every clause of their Pass Threshold cleared, and that 33 of those contain a clause their own text says falls
short. Its section 7 orders the rescoring pass: these 33 first, each re-estimated on the clause its text says falls
short and on every clause it leaves unshown, on cited evidence — for designs, their own specification, held to
protocol 4.1's evidentiary tier. A stated shortfall is tested, not assumed: where the evidence clears the clause,
the 1.0 stands. Two of the 33 do.

## 2. How a clause is recorded, and the rule

| Status | Meaning |
|---|---|
| cleared | shown on evidence at or above the clause's bar |
| short | the evidence shows the clause below its bar |
| not shown | no estimate on evidence located (silence is not clearance, D28(b)) |
| out of reach | a quantity the mechanism does not govern even when generalised (D28(c)) |
| moot | the clause cannot apply to the entry (D28(e)); none arises in part (a) |

**The rule (D28, protocol 2.3).** A 1.0 stands only if every clause is cleared or moot; otherwise it becomes 0.5.
An out-of-reach clause holds the criterion at 0.5 at most.

A clause the audit coded A is carried as cleared on the unit's own text ("as audited"), since part (a)
re-estimates what the text says falls short and what it leaves unshown. The exception is a clause whose entry's
or design's own sources contradict the text: there the sources govern (CCO-PTF-CIP-SZH C3.1, clause 3).
"Not estimated in this pass" marks a clause that could not change the verdict once another clause was shown
short. It stays not shown, and Report v2.0's clause-level Part I must estimate it.

## 3. Decisions and readings (under the delegation)

**3.1 Part (a) scores 1.0 or 0.5, never 0.0.** D28 moves a 1.0 that does not stand to 0.5 (audit record, 5;
protocol 2.3(f)). Two units, read on evidence, arguably meet one of protocol 2.1's whole-criterion 0.0 conditions:
Libertarian Minarchism's C4.5 (the design treats voluntary exchange as non-exploitative by definition, excluding
the criterion's concern as illegitimate) and Centrally Planned Socialism's C4.5 (state appropriation as structural,
load-bearing extraction, the 0.0 band's own test). Each is scored 0.5 and flagged with 0.0 as its alternative
(protocol 6.1), which carries the question into the joint readings and tier robustness. *Alternative rejected:*
scoring 0.0 directly would change two failure counts through a pass whose rule is clause-level and whose bound
says it cannot (2.3(f)), and it would re-read only the corpus's 1.0s, not its 0.5s, for 0.0 conditions.

**3.2 D31: MMT + Job Guarantee's environmental work is inside the mechanism.** The rationale credits Green New
Deal proposals, and Session 35's audit coded all four of C4.2's clauses out of reach, reading the Green New Deal
as an adjacent programme. D31 asks for a source in the mechanism's own literature. The job guarantee's leading
designer pairs it with environmental work in the design itself: Tcherneva (2007, Levy Economics Institute Working
Paper 517) weighs the guarantee's environmental merits against a basic income's, and Tcherneva (2021) presents the
guarantee as the social arm of the Green New Deal, creating jobs that answer environmental and social needs. The
work is scored in and the clauses are within reach. None is shown cleared ("theoretically compatible with absolute
emissions reductions" is not a 35–45% cut by 2030), so the unit is 0.5 — not the 0.0 that a reach reading leaving
no mechanism in scope would have raised. *Scope scenario:* counting the environmental work out leaves no mechanism
addressing C4.2 (0.0, one failure more).

**3.3 D31: MMT + Job Guarantee's social housing stays outside.** No source located in the job-guarantee
literature pairs a housing programme with the guarantee in its design, so the out-of-reach reading of C1.3's
affordability clause stands. Counting housing in would not change the score, since C1.3's first clause is not
shown either way.

**3.4 Readings fixed in part (a), to be applied alike in part (b)** (protocol 5: one criterion's clauses are read
alike across the corpus).

- *C1.3, clause 2 (affordability at 80% of area median income).* For a configured national economy, read against
  the whole population, renters and non-residents included (protocol 3.2). A documented rent shock in the segment
  that houses them is a failure to maintain affordability there.
- *C2.3, clause 1.* "Regular" is weekly, as the Measurement line says. Annual participation is an upper bound,
  not an estimate.
- *C2.4.* National-election turnout is participation in a democratic process (clause 1). Clause 2 is the
  adoption share of citizen-initiated proposals that reached the deciding body.
- *C3.1, clause 2.* Tested first at the threshold's own example: a 30% GDP decline must raise support per
  covered person by at least 30%, automatically. Widening coverage at fixed benefit levels is clause 3's subject,
  not clause 2's. Whether a fixed step that exceeds the example also "scales" is left open — the threshold says
  "scaling 1:1", while the Paper's rationale for the criterion says "increasing support by 50%+ during downturns".
  Neither unit here turns on it, and part (b) decides it by protocol 4.2 with the units that do.
- *C3.4, clause 2.* "Evidence" dates from the formal assessment or advice that calls for the change; scheduled
  review cycles longer than six months fall short. The alternative, dating from the market evidence, is flagged
  where it decides a unit (Sovereign Wealth Fund Statism).
- *C3.4, clause 4.* Cleared by a stated search of the record that locates no collapse caused by a parameter
  adjustment (the Georgism precedent). Documented failures that no source attributes to, or clears of, an
  adjustment leave the clause not shown, and the unit is flagged (Ostrom-style commons governance).
- *C5.1, clause 2.* The entry's documented outcomes against the benefits its own sources claim for it. Where the
  corpus's own scoring of the entry records outcomes short of those claims, the clause is not shown. Part (b)
  applies this reading to the eleven C5.1 1.0s outside part (a) (audit record, 7).
- *C5.2.* Judged on the plans' content — phases, timeline, milestones, resources and risk mitigation — as the
  anchor's note asks ("judge this on specificity"). Whether the plans would work is C5.1's and C5.4's question.

## 4. The units

### 4.1 Summary (generated)

| Entry | Criterion | Clauses | Verdict | Flag |
|---|---|---|---|---|
| SQ | C5.1 | C U | 1.0 → 0.5 | alternative 1.0 |
| NSD | C2.1 | U U | 1.0 → 0.5 |  |
| NSD | C2.3 | U C U | 1.0 → 0.5 |  |
| NSD | C2.4 | C S U | 1.0 → 0.5 |  |
| NSD | C3.1 | C S U | 1.0 → 0.5 |  |
| NSD | C4.4 | S S U C | 1.0 → 0.5 |  |
| CPS | C3.2 | S U S | 1.0 → 0.5 |  |
| CPS | C3.5 | C U S U | 1.0 → 0.5 |  |
| CPS | C4.5 | S U U | 1.0 → 0.5 | alternative 0.0 |
| MS | C2.1 | S U | 1.0 → 0.5 |  |
| MS | C4.4 | S U C U | 1.0 → 0.5 |  |
| LM | C2.3 | S U U | 1.0 → 0.5 |  |
| LM | C2.4 | S U U | 1.0 → 0.5 |  |
| LM | C4.5 | U U S | 1.0 → 0.5 | alternative 0.0 |
| MMT | C1.3 | U R | 1.0 → 0.5 |  |
| MMT | C4.2 | U U U U | 1.0 → 0.5 |  |
| MMT | C5.2 | S U U U U | 1.0 → 0.5 |  |
| UBI | C2.1 | U U | 1.0 → 0.5 |  |
| UBI | C4.5 | R C S | 1.0 → 0.5 |  |
| UBI | C5.3 | C C U U | 1.0 → 0.5 |  |
| FALC | C3.2 | C U S | 1.0 → 0.5 |  |
| CCO | C3.1 | C S U | 1.0 → 0.5 |  |
| CCO | C5.2 | C C C C C | 1.0 → 1.0 |  |
| INT | C5.3 | C C U U | 1.0 → 0.5 |  |
| GEO | C3.4 | C S C C | 1.0 → 0.5 |  |
| DE | C3.4 | C S S U | 1.0 → 0.5 |  |
| SWF | C3.4 | C C C C | 1.0 → 1.0 | alternative 0.5 |
| SG | C1.3 | C S | 1.0 → 0.5 |  |
| SG | C3.4 | C S S C | 1.0 → 0.5 |  |
| QA | C5.3 | C C S U | 1.0 → 0.5 |  |
| IF | C3.4 | C S S C | 1.0 → 0.5 |  |
| IF | C5.1 | C S | 1.0 → 0.5 |  |
| OS | C3.4 | C C C U | 1.0 → 0.5 | alternative 1.0 |

Clause statuses are listed in Appendix B's order: C cleared, S short, U not shown, R out of reach.

### 4.2 Clause by clause (generated)

#### SQ C5.1 Proven Component Foundation: 1.0 → 0.5 — flagged as contestable

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥70% of system components proven through ≥20 years operation at scale ≥10,000 participants | cleared | operated for centuries; its components in continuous national-scale operation far beyond 20 years | as audited (the unit's own text) |
| 2 | with documented outcomes matching claimed benefits | not shown | the rationale claims longevity, not a match of outcomes to claimed benefits, and concedes the record does not validate adequacy for contemporary challenges; the corpus's own scoring of this entry records outcomes short of the broad-prosperity benefits its defenders claim (C1.1 0.5; C1.2b, C1.4, C4.4 0.0) | Report v1.6, SQ C5.1; neec_corpus.json (SQ) |

*Flag:* alternative 1.0: outcomes matched component by component against narrow claimed functions (price stability, growth) rather than the system's broad claims.

#### NSD C2.1 Freedom from Coercion: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥70% report genuine autonomy in major life decisions | not shown | no standardized autonomy figure; the rationale says coercion is reduced significantly, and Nordic unemployment insurance carries availability and activation conditions, which the criterion's Requirement counts as bureaucratic control | Report v1.6, NSD C2.1; criteria.json C2.1 (requirement) |
| 2 | validated through revealed preference showing acceptance of initially refused employment/living situations when alternatives exist | not shown | no revealed-preference study of acceptance under a guaranteed alternative located | — |

#### NSD C2.3 Creative Development Opportunities: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥50% regular creative engagement | not shown | the Measurement line asks for weekly engagement; the figures located are annual (74% Denmark, 68% Sweden, 63% Finland took part in at least one artistic activity in a year), an upper bound only; the rationale's 35-45% is unsourced; EU-SILC table ilc_scp07 (2015, 2022) holds the weekly shares | Special Eurobarometer 399 (2013), via NZ Ministry of Social Development, Social Report |
| 2 | average 10+ hours weekly on non-subsistence pursuits | cleared | about 1,380 hours worked a year against 1,780 in the US leave well over 10 hours a week | as audited (the unit's own text) |
| 3 | meaning/purpose satisfaction scores ≥70/100 | not shown | not located in this pass (EU-SILC well-being module: things one does are worthwhile) | — |

*Note:* returns to 1.0 only if ilc_scp07 shows at least 50% engaging weekly and the well-being module at least 7.0 of 10.

#### NSD C2.4 Democratic Participation: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥70% participation in democratic processes | cleared | latest national turnouts: Sweden 84.2% (2022), Denmark 84.16% (2022), Iceland 80.1% (2021), Norway 77.2% (2021), Finland 68.5% (2023); four of five at or above 70% (the rationale's 65-75% understated it) | IDEA Voter Turnout Database; Valmyndigheten, 2022 results; Nordregio (2024) |
| 2 | ≥35% citizen proposals adopted | short | by September 2020, 36 Finnish citizens' initiatives had reached Parliament and two became law (same-sex marriage; the Maternity Act): about 6% | Yle News (September 2020) |
| 3 | ≥65% satisfaction with responsiveness | not shown | not estimated in this pass; the verdict is fixed by clause 2 | — |

#### NSD C3.1 Crisis Response Capacity: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Response within 72 hours | cleared | benefits automatically increase in downturns without legislative delay | as audited (the unit's own text) |
| 2 | scaling 1:1 with crisis severity (30% GDP decline = 30% benefit increase) | short | support rises by widening coverage at fixed replacement rates; no automatic rise in support per covered person at the threshold's own example (30% decline, 30% increase); the rationale says the stabilizers scale moderately | Report v1.6, NSD C3.1; criteria.json C3.1 (pass threshold, measurement) |
| 3 | ≥90% population coverage | not shown | not estimated in this pass | — |

#### NSD C4.4 Power Distribution: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Gini <0.35 for wealth | short | wealth Gini 0.65-0.75, the entry's own figure, on which its C1.2b (the same wealth-Gini test) is already scored 0.5 | Report v1.6, NSD C1.2b and C4.4; Paper v1.4, 12.3 |
| 2 | ≥40% citizen proposals adopted | short | about 6% of the Finnish citizens' initiatives that reached Parliament were adopted (see C2.4) | Yle News (September 2020) |
| 3 | democratic accountability for ≥80% of major decisions | not shown | not estimated in this pass | — |
| 4 | removal/replacement mechanisms functional | cleared | parliamentary removal functions: Sweden's prime minister lost a confidence vote on 21 June 2021 | Riksdag confidence vote, 21 June 2021 |

#### CPS C3.2 Inflation Control Mechanisms: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Long-term inflation ≤3% | short | official prices held by decree while excess demand appeared as queues, rationing and black markets (the entry's shortage inflation): repressed and hidden inflation, not price stability | Report v1.6, CPS C3.2; Kornai, Economics of Shortage (1980); Nuti, Contributions to Political Economy 5 (1986) |
| 2 | stress test inflation ≤5% (when external 8%) | not shown | no stress record separable from the system's end | — |
| 3 | automatic adjustment preventing runaway inflation | short | no automatic adjustment: the monetary overhang was released as open inflation when prices were freed at the system's end | Nuti (1986); Report v1.6, CPS C3.5 |

#### CPS C3.5 Failure-Mode Transparency: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Failure detection within 1 week | cleared | failures (shortages, queues, poverty) were highly visible | as audited (the unit's own text) |
| 2 | diagnosis success ≥80% | not shown | not shown | — |
| 3 | correction success ≥70% | short | correction came through eventual collapse and reform, in every Soviet-type economy: a failure replicated across independent implementations (D29(a)) | Report v1.6, CPS C3.5 |
| 4 | externalization <10% of total costs | not shown | not estimated in this pass | — |

#### CPS C4.5 Exploitation Elimination: 1.0 → 0.5 — flagged as contestable

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Extraction rates <10% GDP | short | surplus appropriated by the state rather than private owners: extraction continued, to another appropriator, with nothing placing it below 10% of GDP | Report v1.6, CPS C4.5 |
| 2 | genuine exit rights from exploitative relationships | not shown | not estimated in this pass | — |
| 3 | residual coercion <10% of decisions | not shown | not estimated in this pass | — |

*Flag:* alternative 0.0: state appropriation read as structural, load-bearing extraction, the 0.0 band's own test.

#### MS C2.1 Freedom from Coercion: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥70% report genuine autonomy in major life decisions | short | the rationale concedes survival-linked compulsion persists (compete or close replaces work or starve); no autonomy survey located | Report v1.6, MS C2.1 |
| 2 | validated through revealed preference showing acceptance of initially refused employment/living situations when alternatives exist | not shown | no revealed-preference validation located | — |

#### MS C4.4 Power Distribution: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Gini <0.35 for wealth | short | wealth Gini 0.40-0.50 for cooperative systems, the Paper's own figure, above 0.35 | Paper v1.4, 12.3 (C1.2b current performance) |
| 2 | ≥40% citizen proposals adopted | not shown | not estimated in this pass | — |
| 3 | democratic accountability for ≥80% of major decisions | cleared | economic power distributed through democratic ownership | as audited (the unit's own text) |
| 4 | removal/replacement mechanisms functional | not shown | not estimated in this pass | — |

#### LM C2.3 Creative Development Opportunities: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥50% regular creative engagement | short | the rationale says the freedom applies only to economically secure minorities | Report v1.6, LM C2.3 |
| 2 | average 10+ hours weekly on non-subsistence pursuits | not shown | claimed only for those with capital; not shown for the population | — |
| 3 | meaning/purpose satisfaction scores ≥70/100 | not shown | not estimated in this pass | — |

#### LM C2.4 Democratic Participation: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥70% participation in democratic processes | short | economic democracy is entirely absent (the rationale), and the criterion's Requirement counts it as much as political democracy | Report v1.6, LM C2.4; criteria.json C2.4 (requirement) |
| 2 | ≥35% citizen proposals adopted | not shown | not estimated in this pass | — |
| 3 | ≥65% satisfaction with responsiveness | not shown | not estimated in this pass | — |

#### LM C4.5 Exploitation Elimination: 1.0 → 0.5 — flagged as contestable

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Extraction rates <10% GDP | not shown | no mechanism limits private extraction | — |
| 2 | genuine exit rights from exploitative relationships | not shown | formal freedom of contract; exit without a subsistence floor is not shown to be genuine | — |
| 3 | residual coercion <10% of decisions | short | the rationale concedes the design ignores economic coercion and power asymmetries | Report v1.6, LM C4.5 |

*Flag:* alternative 0.0: the design treats voluntary exchange as non-exploitative by definition: the 0.0 condition of excluding the criterion's concern as illegitimate (protocol 2.1).

#### MMT C1.3 Housing Security: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥88% housing stability over 5-year periods | not shown | the job guarantee would substantially improve housing security: an improvement, not a stability rate | Report v1.6, MMT C1.3 |
| 2 | maintaining affordability at 80% area median income | out of reach | affordability is set by housing policy and land markets; no source located in the job-guarantee literature that pairs a housing programme with the guarantee in its design (D31) | Session 35 reach reason, confirmed |

*Note:* a scope scenario counting social housing in does not change the score: clause 1 stays not shown.

#### MMT C4.2 Ecological Compliance: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Absolute carbon reductions 35-45% by 2030 | not shown | within reach under D31 (the guarantee's own literature pairs it with environmental work); theoretically compatible with absolute reductions is not a 35-45% cut by 2030 | Tcherneva, Levy WP 517 (2007); Tcherneva, La garantie d'emploi: l'arme sociale du Green New Deal (2021) |
| 2 | biodiversity neutral or positive | not shown | within reach under D31; no estimate | — |
| 3 | resource extraction ≤ regeneration | not shown | within reach under D31; no estimate | — |
| 4 | ≥7 of 9 planetary boundaries respected | not shown | within reach under D31; no estimate | — |

*Note:* supersedes Session 35's out-of-reach coding of all four clauses; a scope scenario counting the environmental work out leaves no mechanism addressing C4.2 (0.0, one failure more).

#### MMT C5.2 Staged Transition Pathways: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | staged (≥4 phases) | short | three stages (pilot, regional, national) against at least four; no four-phase plan located in the blueprint literature, which sets out structure, funding and administration | Report v1.6, MMT C5.2; Tcherneva, Levy WP 902 (2018) |
| 2 | rapid (≤36 months) deployment | not shown | no deployment plan of 36 months or less located | — |
| 3 | specific milestones | not shown | not shown | — |
| 4 | resource requirements | not shown | not shown | — |
| 5 | risk mitigation | not shown | not shown | — |

#### UBI C2.1 Freedom from Coercion: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥70% report genuine autonomy in major life decisions | not shown | 65-75% report increased autonomy: straddles the bar, measures an increase rather than genuine autonomy, and is unsourced | Report v1.6, UBI C2.1 |
| 2 | validated through revealed preference showing acceptance of initially refused employment/living situations when alternatives exist | not shown | no revealed-preference validation cited | — |

#### UBI C4.5 Exploitation Elimination: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Extraction rates <10% GDP | out of reach | the economy-wide extraction share is not governed by an income transfer | Session 35 reach reason, confirmed |
| 2 | genuine exit rights from exploitative relationships | cleared | an exit option from exploitative work | as audited (the unit's own text) |
| 3 | residual coercion <10% of decisions | short | eliminates most desperate exploitation: reduced, not below 10% of decisions | Report v1.6, UBI C4.5 |

#### UBI C5.3 Partial and Parallel Deployability: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Viable at ≥30% participation | cleared | implementable at municipal, state or national scale | as audited (the unit's own text) |
| 2 | coexistence with traditional markets maintaining ≥90% economic activity | cleared | Alaska shows coexistence with the market economy | as audited (the unit's own text) |
| 3 | scaling pathway validated through modeling | not shown | a gradual rollout is asserted; no scaling pathway validated through modelling cited | Report v1.6, UBI C5.3 |
| 4 | coordination protocols established | not shown | not estimated in this pass | — |

#### FALC C3.2 Inflation Control Mechanisms: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Long-term inflation ≤3% | cleared | post-scarcity abundance claimed to remove inflation (a design's projection) | as audited (the unit's own text) |
| 2 | stress test inflation ≤5% (when external 8%) | not shown | not shown | — |
| 3 | automatic adjustment preventing runaway inflation | short | assumes the problem away through technology: no mechanism of its own, which D26 places in the 0.5 band | Report v1.6, FALC C3.2; criteria.json C3.2 (D26) |

#### CCO C3.1 Crisis Response Capacity: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Response within 72 hours | cleared | the design's Recession Protocol acts at 0-72 hours | research-hub at 8e8a6ba (2026-09-21), integrated-implementation-roadmap.html, Appendix G |
| 2 | scaling 1:1 with crisis severity (30% GDP decline = 30% benefit increase) | short | the design raises Basic Units by a fixed 20% on a trigger of a GDP decline above 2% for two quarters, later steps discretionary: below the threshold's own example (30% decline, 30% increase); the Report's 50% is in no published CCO document located | research-hub at 8e8a6ba (2026-09-21), integrated-implementation-roadmap.html, Appendix G |
| 3 | ≥90% population coverage | not shown | re-read on the design's own sources: participation is opt-in and the rollout plan targets 60% opt-in; coverage of 90% of the affected population is not shown | compassionate-meritocracy-plan, index.html (3-Month Plan for the USA) |

*Note:* correction for Report v2.0: the design's figure is 20%, not 50%.

#### CCO C5.2 Staged Transition Pathways: 1.0 → 1.0

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | staged (≥4 phases) | cleared | seven phases over seven years | research-hub at 8e8a6ba (2026-09-21), integrated-implementation-roadmap.html |
| 2 | rapid (≤36 months) deployment | cleared | a three-month national launch plan | compassionate-meritocracy-plan, index.html |
| 3 | specific milestones | cleared | phase timelines, success metrics and a KPI appendix; a sprint timeline | research-hub at 8e8a6ba (2026-09-21), integrated-implementation-roadmap.html (Appendix I); compassionate-meritocracy-plan |
| 4 | resource requirements | cleared | USD 500 billion over five years for PTFs; a Resource Requirements section | research-hub at 8e8a6ba (2026-09-21), integrated-implementation-roadmap.html (Appendix A); compassionate-meritocracy-plan |
| 5 | risk mitigation | cleared | a Risk Assessment and Mitigation section; a Risk Mitigation Framework paper (31 August 2025) | compassionate-meritocracy-plan; research-hub at 8e8a6ba (2026-09-21), risk-mitigation-framework.html |

*Note:* the plans' specification is what C5.2 judges (its anchor note); their feasibility is scored at C5.1 and C5.4; the documents are the owner's (self-referential disclosure).

#### INT C5.3 Partial and Parallel Deployability: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Viable at ≥30% participation | cleared | the federated structure starts with a handful of people | as audited (the unit's own text) |
| 2 | coexistence with traditional markets maintaining ≥90% economic activity | cleared | nodes coexist with traditional markets | as audited (the unit's own text) |
| 3 | scaling pathway validated through modeling | not shown | starting small is supported by design; no modelling of the scaling pathway cited | Report v1.6, INT C5.3 |
| 4 | coordination protocols established | not shown | not estimated in this pass | — |

#### GEO C3.4 Epistemic Adaptability: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥30% parameter adjustability range | cleared | rates, valuation methods and phase-ins adjusted across jurisdictions | as audited (the unit's own text) |
| 2 | policy updates within 6 months of evidence | short | multi-year cycles, not updates within six months: Estonia's national revaluations in 2001 and then 2022; the ACT's transition review about every four years; Denmark's 2024 reform phased in to 2028 | NEEC_Georgism_LVT_scoring_scratch.md, C3.4 |
| 3 | democratic governance for changes | cleared | changes through ordinary democratic process | as audited (the unit's own text) |
| 4 | zero collapses during parameter adjustments | cleared | no collapse caused by an adjustment located | as audited (the unit's own text) |

#### DE C3.4 Epistemic Adaptability: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥30% parameter adjustability range | cleared | the global model and city portraits revised on new data | as audited (the unit's own text) |
| 2 | policy updates within 6 months of evidence | short | scheduled cycles longer than six months: the global monitor annually, Amsterdam biennially | NEEC_DoughnutEconomics_scoring_scratch.md, C3.4 |
| 3 | democratic governance for changes | short | the framework's own revisions are made by its authors and DEAL, not governed democratically; only city applications pass through councils | NEEC_DoughnutEconomics_scoring_scratch.md, C3.4 |
| 4 | zero collapses during parameter adjustments | not shown | not shown either way | — |

#### SWF C3.4 Epistemic Adaptability: 1.0 → 1.0 — flagged as contestable

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥30% parameter adjustability range | cleared | the strategic equity share moved from 40% (1998) to 60% (decided June 2007) to 70% (2017): a core parameter moved by half its value; the expected return in the fiscal rule from 4% to 3% (2017) | Norges Bank, Matsen speech (1 December 2016); Ministry of Finance press release (16 February 2017) |
| 2 | policy updates within 6 months of evidence | cleared | the 2017 decisions came on 16 February, eleven weeks after Norges Bank's recommendation of 1 December 2016 | NBIM letter to the Ministry (1 December 2016); Ministry of Finance (16 February 2017) |
| 3 | democratic governance for changes | cleared | a democratically enacted change | as audited (the unit's own text) |
| 4 | zero collapses during parameter adjustments | cleared | the new equity share held through 2008-2009 without collapse | as audited (the unit's own text) |

*Flag:* alternative 0.5: evidence dated from the market evidence of lower expected returns rather than from the formal assessment, which makes the expected-return revision slow.

#### SG C1.3 Housing Security: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥88% housing stability over 5-year periods | cleared | a documented stability rate far above the threshold for the resident population | as audited (the unit's own text) |
| 2 | maintaining affordability at 80% area median income | short | not maintained for the rental segment, which houses most non-residents: private rents up 29.7% in 2022 after 9.9% in 2021, HDB rents up about 28.5% in 2022, foreigners about 65% of renters; the configured-economy population rule counts them (protocol 3.2) | URA via Malay Mail (27 January 2023); Vulcan Post (2023), citing URA and PropertyGuru |

#### SG C3.4 Epistemic Adaptability: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥30% parameter adjustability range | cleared | repeated recalibration: divestment, climate targets, a carbon tax | as audited (the unit's own text) |
| 2 | policy updates within 6 months of evidence | short | some evidence-based proposals slow or refused: unemployment support long resisted until 2025; an official poverty line refused | NEEC_StateCapitalism_Singapore_scoring_scratch.md, C3.4 |
| 3 | democratic governance for changes | short | governed democratically but under a dominant-party supermajority | NEEC_StateCapitalism_Singapore_scoring_scratch.md, C3.4 |
| 4 | zero collapses during parameter adjustments | cleared | no collapse from recalibration | as audited (the unit's own text) |

#### QA C5.3 Partial and Parallel Deployability: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Viable at ≥30% participation | cleared | the distributive core serves citizens, 9-13% of residents | as audited (the unit's own text) |
| 2 | coexistence with traditional markets maintaining ≥90% economic activity | cleared | runs in parallel with a market economy | as audited (the unit's own text) |
| 3 | scaling pathway validated through modeling | short | no validated scaling pathway exists (the entry's own flag) | NEEC_StateCapitalism_Qatar_scoring_scratch.md, C5.3 |
| 4 | coordination protocols established | not shown | not estimated in this pass | — |

#### IF C3.4 Epistemic Adaptability: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥30% parameter adjustability range | cleared | product sets re-engineered and frameworks revised | as audited (the unit's own text) |
| 2 | policy updates within 6 months of evidence | short | after the 2012 tightening of bay' al-inah the industry re-engineered within a few years | NEEC_IslamicFinance_scoring_scratch.md, C3.4 |
| 3 | democratic governance for changes | short | changes set by Shariah Advisory Councils of appointed scholars and by central banks: governed, not democratic (the document's quotation drops democratic) | NEEC_IslamicFinance_scoring_scratch.md, C3.4; audit record, 4 |
| 4 | zero collapses during parameter adjustments | cleared | no destabilisation | as audited (the unit's own text) |

#### IF C5.1 Proven Component Foundation: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥70% of system components proven through ≥20 years operation at scale ≥10,000 participants | cleared | every named contract in commercial use at scale since 1983 | as audited (the unit's own text) |
| 2 | with documented outcomes matching claimed benefits | short | the design promises profit-and-loss sharing; debt-like sale contracts dominate (tawarruq 46% of Malaysian Islamic financing by 2019), and the document leaves the match to its other criteria | NEEC_IslamicFinance_scoring_scratch.md, C3.4 and C5.1 |

#### OS C3.4 Epistemic Adaptability: 1.0 → 0.5 — flagged as contestable

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥30% parameter adjustability range | cleared | principle 3 is a procedure for changing the rules | as audited (the unit's own text) |
| 2 | policy updates within 6 months of evidence | cleared | in-period adjustment faster than six months (the acequia scarcity rule) | as audited (the unit's own text) |
| 3 | democratic governance for changes | cleared | rule changes governed by those affected | as audited (the unit's own text) |
| 4 | zero collapses during parameter adjustments | not shown | the founding literature records outright failures and fragile appropriator-designed institutions; no analysis located attributing them to, or clearing them of, a rule adjustment | Ostrom, Governing the Commons (1990), ch. 5 (Turkish inshore fisheries, California groundwater basins, Sri Lankan and Nova Scotian fisheries) |

*Flag:* alternative 1.0: read as for Georgism: no collapse caused by an adjustment located.

## 5. What part (a) changes (generated)

| Entry | Total now (rank) | After part (a) (rank) | Change | Failures | Tier | Left for part (b) | Bound after part (b) |
|---|---:|---:|---:|---:|---|---:|---:|
| CCO | 24.5 (1) | 24.0 (1) | -0.5 | 0 | Potentially Adequate | 11 | 18.5 |
| PE | 20.5 (2) | 20.5 (2) | 0.0 | 1 | Potentially Adequate | 13 | 14.0 |
| NSD | 19.5 (3) | 17.0 (5) | -2.5 | 2 | Potentially Adequate | 7 | 13.5 |
| INT | 19.5 (3) | 19.0 (3) | -0.5 | 3 | Partially Adequate | 11 | 13.5 |
| DG | 19.0 (5) | 19.0 (3) | 0.0 | 2 | Potentially Adequate | 11 | 13.5 |
| MS | 16.5 (6) | 15.5 (6) | -1.0 | 2 | Potentially Adequate | 5 | 13.0 |
| MMT | 15.5 (7) | 14.0 (8) | -1.5 | 3 | Partially Adequate | 5 | 11.5 |
| UBI | 14.5 (8) | 13.0 (12) | -1.5 | 7 | Structurally Inadequate | 4 | 11.0 |
| MC | 14.5 (8) | 14.5 (7) | 0.0 | 3 | Partially Adequate | 4 | 12.5 |
| OS | 14.5 (8) | 14.0 (8) | -0.5 | 3 | Partially Adequate | 2 | 13.0 |
| SWF | 14.0 (11) | 14.0 (8) | 0.0 | 3 | Partially Adequate | 2 | 13.0 |
| SG | 14.0 (11) | 13.0 (12) | -1.0 | 4 | Partially Adequate | 1 | 12.5 |
| GEO | 13.5 (13) | 13.0 (12) | -0.5 | 2 | Potentially Adequate | 1 | 12.5 |
| UBS | 13.5 (13) | 13.5 (11) | 0.0 | 3 | Partially Adequate | 3 | 12.0 |
| IF | 13.5 (13) | 12.5 (15) | -1.0 | 5 | Partially Adequate | 2 | 11.5 |
| FALC | 13.0 (16) | 12.5 (15) | -0.5 | 10 | Structurally Inadequate | 7 | 9.0 |
| DE | 11.5 (17) | 11.0 (17) | -0.5 | 8 | Structurally Inadequate | 4 | 9.0 |
| SQ | 10.5 (18) | 10.0 (18) | -0.5 | 9 | Structurally Inadequate | 1 | 9.5 |
| CPS | 10.0 (19) | 8.5 (21) | -1.5 | 12 | Structurally Inadequate | 2 | 7.5 |
| SC | 10.0 (19) | 10.0 (18) | 0.0 | 9 | Structurally Inadequate | 3 | 8.5 |
| CN | 10.0 (19) | 10.0 (18) | 0.0 | 8 | Structurally Inadequate | 0 | 10.0 |
| QA | 9.0 (22) | 8.5 (21) | -0.5 | 10 | Structurally Inadequate | 0 | 8.5 |
| LM | 8.0 (23) | 6.5 (23) | -1.5 | 15 | Structurally Inadequate | 2 | 5.5 |

"Left for part (b)" counts the entry's units still to be re-estimated under D28; "Bound after part (b)" is the
entry's total if every one of them fell, the audit's textual bound updated for part (a).

After part (a) the corpus has 15 dominance pairs against 14 (new: CCO>CPS, CCO>LM, CN>QA; lost: CCO>MMT, IF>SC), and its frontier holds 11 entries against 12 (NSD, MMT, UBI, DG, FALC, PE, CCO, INT, MC, IF, OS). First place: CCO, 24.5 to 24.0.

No failure count and no tier changes. The largest falls are Nordic Social Democracy's (2.5 points; it rested on
figures its own sources contradict or do not support) and Centrally Planned Socialism's, Libertarian Minarchism's,
MMT + Job Guarantee's and Universal Basic Income's (1.5 each). The flag registers of eight entries change: five
flags are added (Status Quo C5.1, Centrally Planned Socialism C4.5, Libertarian Minarchism C4.5, Sovereign Wealth
Fund Statism C3.4, Ostrom C3.4) and three removed, because their alternative, 0.5, is now the score (Singapore
C3.4, Qatar C5.3, Islamic finance C3.4). The enumerations and joint readings of those eight entries are recomputed
when the pass is applied.

## 6. Corrections found (not polish)

1. **Report v1.6, CCO-PTF-CIP-SZH C3.1** says the system "automatically increases by 50% during crises". No
   published CCO document located gives 50%. The design's own roadmap specifies a fixed 20% increase in Basic
   Units within 72 hours, on a trigger of a GDP decline above 2% for two quarters (Integrated Implementation
   Roadmap, Appendix G). Report v2.0 carries the design's figure.
2. **Report v1.6, Nordic Social Democracy C2.4** gives "65-75% voter turnout". The latest national elections
   had turnouts from 77.2% to 84.2% in four of the five countries, and 68.5% in Finland.
3. **Unsourced figures.** Nordic Social Democracy's C2.3 ("35-45% regular creative engagement") and Universal
   Basic Income's C2.1 ("Pilots show 65-75% report increased autonomy") name no source. Report v2.0 states sourced
   figures or none.
4. **C5.2's definition embeds one entry's design.** Its definition in `criteria.json`, carried from Paper v1.4,
   includes CCO-PTF-CIP-SZH's own phase and month schedules and the line "CCO-PTF modeling: Both pathways
   validated through simulation". The Pass Threshold is unaffected. *Decision:* the entry-specific text moves out
   of the definition when Paper v2.0 renders the criteria from `criteria.json` (D19, Step 5); nothing changes
   before then.

## 7. Disclosure

CCO-PTF-CIP-SZH is the owner's design. In part (a), one of its units stands on its own documents (C5.2), one falls
on them (C3.1, where they also correct the Report against CCO), and it keeps first place (24.5 to 24.0). The
documents read are the owner's published plans, in `BetterToBest/research-hub` at commit 8e8a6ba (2026-09-21) and
`BetterToBest/compassionate-meritocracy-plan`. Protocol 4.1 makes a design's own specification the evidence for
what it specifies, and C5.2 asks what the plans specify, not whether they would work. The second pilot, with a
replicator outside the Claude family, is the independent test of exactly this.

## 8. What remains

- **(b)** the other 101 units, criterion by criterion, and C5.1's second clause on its eleven 1.0s outside part (a);
- **(c)** the 131 mechanism-class 0.5s against D29, Ostrom's C4.3 first;
- **(d)** D31's source for Ostrom's community land trusts;
- **(e)** the Islamic finance and Ostrom documents' quoted thresholds restated to the definitions (audit record, 4).

**Reopening condition.** Nordic Social Democracy's C2.3 returns to 1.0 only if Eurostat's EU-SILC table
`ilc_scp07` shows at least 50% of residents practising an artistic activity weekly and the EU-SILC well-being
module shows a rating of at least 7.0 of 10 for the worth of what people do. This session's environment could
not reach Eurostat's database, so a session that can should read both.

When the pass ends, its changes are applied by generator, and the corpus, CSV, `README.md` and Appendix A.4 are
regenerated. The eight changed flag registers are then recomputed, the protocol's statements about the corpus
are restated, and the claims and protocol verifiers get successors.

## 9. What this record does not show

It is one scorer's re-estimation, on evidence located in one session through web search and the design's own
repositories. "Not shown" means no evidence was located, not that the clause fails. Where the evidence or the
reading is divided, the unit is flagged in the direction a careful second scorer could take: two toward 1.0, one
toward 0.5 and two toward 0.0. Whether these calls reproduce is what the replication programme tests.
