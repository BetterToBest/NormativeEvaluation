# NEEC Rescoring Pass — Record, Stage 2, Group 2.7: C1.4 Automation Resilience (class I)

**Session 60 · 2026-10-15 · Scorer and engineer: Claude · Owner: Duke Johnson**
**Status: scratch (protocol 10.1). Parts (a) and (b), groups 2.1 to 2.6 and part 58.1 are `NEEC_Rescoring_s37.md` to
`NEEC_Rescoring_s58.md` and `owner_s58.py`; this record edits none of them.** No corpus file, score or scoring document
changes until the pass ends. Its changes are then applied by generator with pinned inputs and restated in place
(protocol 10.2, 10.3; decisions D12, D14), and until then the published totals stand, provisional as `README.md` says.
Decisions taken here are Claude's under the owner's delegation (Handoff 35, section 2; decision 57.2: only
CCO-PTF-CIP-SZH's score changes wait on the owner, and none is made here); each is recorded with its reasons, and the
owner may reverse any of them.
**Reproduce:** `python3 rescoring_s60.py` (harness check 107). It is the second class I group, written on the shared
module (`pass_common.py`, decision 52.5): the script holds the 20 readings and the group's own checks, and the module
computes the consequences cumulatively with every part before it. It checks every cache file the readings use by digest,
finds every passage quoted in its file, locates each unit's published rationale where the cache's index puts it, and
checks that this record contains its generated tables verbatim. It reads no network.

---

## 1. What this group is

The consequence triage (`triage_s52.py`, decision 52.7), rerun after group 2.6, put C1.4 first among the criteria still
to read: 20 units in play, four of them able to change an adequacy tier on their own, and Integral's able to change who
is first. C1.4 is class I: v2.0 keeps its clauses and bar ("Poverty <8% and aggregate demand >85% baseline in each of
the 30%, 50% and 70% displacement scenarios") and names its measure (`criteria.json`; `NEEC_Criteria_v2_s45.md`): in
each of three scenarios displacing 30%, 50% or 70% of baseline paid working hours, poverty on the Societal Poverty Line
as in C1.1, and aggregate demand as real final consumption expenditure against the pre-displacement baseline; for a
design, its own model of the three scenarios. Three units were re-estimated earlier and are not re-read: Fully Automated
Luxury Communism's and Participatory Economics' (part (b4), each 1.0 to 0.5) and CCO-PTF-CIP-SZH's (group 2.5, 0.5 on
the simulation at v5.6.0). The other 20 are read clause by clause in the D28 form, from the evidence cache Session 59
built (`evidence_cache_s59.py`, `evidence_cache/C1.4/`) and two extracts this session added to it (section 5): one
published 1.0, fourteen 0.5s and five 0.0s.

**Outcome.** No unit's sources state either clause's quantity in any of the three scenarios, so none can be 1.0, and
after this group no entry is at 1.0 on C1.4. **One unit falls**, Universal Basic Income, from 1.0 to 0.5, a correction:
its published 1.0 rests on the design's logic, and silence is not clearance (reading 3.2). Nineteen hold, five of them at
0.0 (Status Quo, Libertarian Minarchism, Stakeholder Capitalism, Doughnut Economics, Islamic Finance). Net −0.5 points;
no failure count, tier or rank but Universal Basic Income's changes. **Integral holds at 0.5** on the design's own white
paper (reading 3.5), so first place stays shared by CCO-PTF-CIP-SZH and Integral at 14.5. Five units are flagged; no
flag could change a tier.

## 2. How a clause is recorded, and the rule

As in groups 2.2 to 2.6 and decision 53.2: each clause is cleared, short, not shown, out of reach or moot. A unit is 1.0
only if every clause is cleared (D28, protocol 2.3); 0.0 only on one of protocol 2.1's whole-criterion conditions, stated
as the unit's reason and never with a clause cleared; 0.5 otherwise. A clause-level gap never makes 0.0 (D28(f)). "Not
shown" means that no estimate of the clause's quantity was located, not that the clause fails; "short" means the
evidence located falls below it. For a mechanism, a clause whose quantity it does not govern even when generalised is
out of reach, and the host economy's figure is not credited to it (protocol 3.2, D28(c)).

## 3. Decisions and readings (under the delegation)

**3.1 What the clauses ask (decision 60.1).** Each clause is a level in each of three scenarios, and v2.0 names the
measure: poverty on the Societal Poverty Line and real final consumption expenditure against the pre-displacement
baseline, with 30%, 50% and 70% of baseline paid working hours displaced. No economy has been observed at those
displacements, so a clause is shown only by a model of the scenarios: for a design its own model, as the indicators
field says; for a configured national economy or a mechanism, a published model of the economy under them. A
rationale's judgement that a system "can maintain 30% displacement" or "cannot sustain 50-70%" is not an estimate, and
a design's statement that its mechanism scales with automation is not a level under a stated scenario: both leave the
clause not shown (protocol 2.3(b)). The demand clause's measure is final consumption expenditure in total, which the
World Bank's source note for the series v2.0 names defines across households and general government (section 5), so
consumption provided in kind by the state counts toward it. The cache holds the measure's sources (the World Bank's PIP
methodology page and the final consumption series' pages), not any model; it holds no country's poverty or consumption
figure because no scenario figure exists to compare it with. *Alternative weighed:* read a configuration's clause 1 as
short where its poverty on the Societal Poverty Line already exceeds 8% before any displacement. Not adopted: displacement
in a scenario is set against the configuration's response to it, which no source models, and the reading would separate
no 0.5 from a 0.0, since a clause-level gap never makes 0.0 (D28(f)). C1.1's group reads the baseline figures.

**3.2 Universal Basic Income, 1.0 → 0.5 (decision 60.2, a correction).** The published 1.0 reads the transfer as
"scales naturally with automation (fewer employed = more UBI funding available from automation productivity)". The
transfer is the 1.0 band's "explicit mechanism decoupling income/demand from employment", but the band's second half,
"robust ... across displacement severities", is asserted, not shown: no level of poverty or consumption under any of the
three scenarios is stated or cited, and the funding claim (that automation's productivity yields the revenue) is not
modelled. Under D28 a clause not estimated cannot support a 1.0 (protocol 2.3(b)). This is the reading parts (b4) and
group 2.5 gave Fully Automated Luxury Communism's, Participatory Economics' and CCO-PTF-CIP-SZH's published 1.0s, each to
0.5 on the same ground; applying it to Universal Basic Income completes it. Universal Basic Income's total falls from
11.0 to 10.5 on the published structure; it stays Structurally Inadequate with seven failures.

**3.3 The 0.5s held (decision 60.3).** Fourteen units hold at 0.5: each names a genuine mechanism that carries some
income or demand through displacement and is not shown to survive the higher severities, the 0.5 band's description.
Nordic Social Democracy is the band's anchor; Centrally Planned Socialism (employment guaranteed regardless of
productivity), Market Socialism (cooperatives sharing hours and gains), MMT + Job Guarantee, Degrowth (work-sharing),
Georgism (a land-value dividend), Mutual Credit (exchange without wages), Universal Basic Services (in-kind provision),
Sovereign Wealth Fund Statism (a revenue base independent of wages), China (state-directed employment and investment),
Singapore (a time-limited jobseeker payment, training and reserves), Qatar (a rent-funded citizen buffer) and Ostrom-style
commons (an employment-independent share of the governed resource) each name one. Two readings are recorded with them.
*Universal Basic Services:* its rationale finds "no mechanism at all for the aggregate-demand side" because the services
pay no cash. On the measure v2.0 names, government final consumption is part of final consumption expenditure, so the
services count toward it; the finding is not borne out, and the verdict is unchanged because neither clause is shown.
*Qatar:* non-citizens are most of the population protocol 3.2 counts, and the buffer covers citizens; a mechanism
covering part of the relevant population is the 0.5 band in protocol 2.1, and the rationale's continuous estimate (0.35
to 0.6) is consistent with it. Ostrom's published flag toward 0.0 is kept (reading 3.6).

**3.4 The 0.0s held, and the peer question between Status Quo and Singapore (decision 60.4).** Status Quo (the 0.0
band's anchor), Libertarian Minarchism, Stakeholder Capitalism, Doughnut Economics and Islamic Finance hold at 0.0, each
on protocol 2.1's first condition: no structural mechanism addresses the criterion. Libertarian Minarchism removes the
safety nets that exist; Doughnut Economics names automation and supplies no provision (its scoring document contrasts it
with the 0.5s); Islamic Finance's mechanism governs neither quantity (reading 3.6). Status Quo and Stakeholder Capitalism
raise a peer question the published scores leave open. Status Quo's rationale says "no mechanism exists"; the
configuration has unemployment insurance, a buffer time-limited and conditional on job search, as Singapore's Jobseeker
Support is (six months, up to S$6,000). Singapore's scoring document holds 0.5 on that payment together with training
and reserve-funded wage subsidies, and places itself "above Status Quo's 0.0, which rests on the absence of any such
lever". The United States also has training programmes and used fiscal capacity in 2020; the distinction is not
established. Two readings are open: insurance against cyclical job loss is not a mechanism for paid work becoming
optional, which holds Status Quo at 0.0 and would take Singapore to 0.0; or any buffer of that kind is the 0.5 band's,
which would raise Status Quo and Stakeholder Capitalism (which keeps the host economy's institutions, as group 2.4 read
it) to 0.5. This group holds all three published scores and flags each toward the other reading: neither reading is
shown better, the published anchor is Status Quo's, and no flag can change a tier (Status Quo would have 8 failures,
Stakeholder Capitalism 7, Singapore 5). Report v2.0 states the question.

**3.5 Integral, held at 0.5 on its white paper (decision 60.5).** Integral's unit can decide who is first, so it was
re-read on the design's own *Technical White Paper v0.1* (December 2025; PDF md5 a6defc9a, the copy group 2.6 read),
which the corpus's rationale predates. The rationale's question was whether essentials are provided unconditionally as
automation reduces contribution opportunities. The paper answers it in part: the access value of a good weighs "fairness
and community need, ensuring that essentials remain accessible regardless of age or ability"; "fewer labor hours are
needed to maintain stable access to essentials" as automation and open design reduce labour; and its section 11.8 offers
"contribution pathways without gatekeeping" to the unemployed. But access "emerges from participation", and the
reference code refuses a redemption on an "insufficient ITC balance". The paper states no level of poverty or consumption
under any displacement scenario and asks "critical readers willing to stress-test the logic". The mechanism is genuine
(production planned on needs assessed through CDS, not on purchasing power, so demand does not require employment), and
neither clause is shown: 0.5, not flagged. A reading toward 1.0 would need the design's own model of the three
scenarios; a reading toward 0.0 would need the mechanism to be absent, which the paper does not support.

**3.6 Islamic Finance and Ostrom-style commons: the published flags kept.** Islamic Finance's mechanism changes how
credit is priced; it governs neither household income nor final consumption, so both clauses are out of reach (protocol
3.2), and the unit is 0.0 on the absence of a mechanism, as its scoring document holds. Its flag toward 0.5, crediting
profit-and-loss-sharing accounts as a non-wage income channel, is kept. Ostrom-style commons' flag toward 0.0, on a
bounded subsistence base for a minority, is kept.

**3.7 The evidence.** The cache of Session 59 holds the 20 published rationales by location and digest and the measure's
sources: the World Bank's PIP methodology page (the Societal Poverty Line) and the World Development Indicators pages for
final consumption expenditure in current and constant US dollars. The OECD national accounts page refused the container
(HTTP 403). This session added the World Bank's source note for the constant-price series, which defines its coverage,
and five passages of Integral's white paper (section 5). Ten rationales are the Report v1.6's one-paragraph entries
(Status Quo, Nordic Social Democracy, Centrally Planned Socialism, Market Socialism, Libertarian Minarchism, MMT + Job
Guarantee, Universal Basic Income, Degrowth, Stakeholder Capitalism and Integral). None cites a source: the index's
"citation strings" for three of them are the bold label "STRUCTURAL FAILURE.", not citations. They are read from what
they say.

## 4. The units

### 4.1 Summary (generated)

| Entry | Published | Clause 1 | Clause 2 | Verdict | Flag |
|---|---:|---|---|---:|---|
| SQ | 0.0 | not shown | not shown | 0.0 | toward 0.5 |
| NSD | 0.5 | not shown | not shown | 0.5 |  |
| CPS | 0.5 | not shown | not shown | 0.5 |  |
| MS | 0.5 | not shown | not shown | 0.5 |  |
| LM | 0.0 | not shown | not shown | 0.0 |  |
| MMT | 0.5 | not shown | not shown | 0.5 |  |
| UBI | 1.0 | not shown | not shown | 0.5 |  |
| DG | 0.5 | not shown | not shown | 0.5 |  |
| SC | 0.0 | not shown | not shown | 0.0 | toward 0.5 |
| INT | 0.5 | not shown | not shown | 0.5 |  |
| GEO | 0.5 | not shown | not shown | 0.5 |  |
| MC | 0.5 | not shown | not shown | 0.5 |  |
| DE | 0.0 | not shown | not shown | 0.0 |  |
| UBS | 0.5 | not shown | not shown | 0.5 |  |
| SWF | 0.5 | not shown | not shown | 0.5 |  |
| CN | 0.5 | not shown | not shown | 0.5 |  |
| SG | 0.5 | not shown | not shown | 0.5 | toward 0.0 |
| QA | 0.5 | not shown | not shown | 0.5 |  |
| IF | 0.0 | out of reach | out of reach | 0.0 | toward 0.5 |
| OS | 0.5 | not shown | not shown | 0.5 | toward 0.0 |

### 4.2 Clause by clause (generated)

#### SQ C1.4 Automation Resilience: 0.0 → 0.0

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Poverty <8% | not shown | the rationale asserts a deflationary spiral at 30% displacement without a model; no model or estimate of poverty on the Societal Poverty Line under a 30%, 50% or 70% displacement of paid hours is stated or cited, and none was located | Report v1.6, System 1, C1.4 |
| 2 | aggregate demand >85% baseline | not shown | no model or estimate of real final consumption expenditure against a pre-displacement baseline in any of the three scenarios is stated or cited, and none was located | Report v1.6, System 1, C1.4 |

*0.0 (protocol 2.1):* no structural mechanism addresses the criterion: income and demand run through paid work, and the configuration's support for the unemployed is insurance against cyclical job loss, not a provision for paid work becoming optional; the 0.0 band's anchor.

*Flag (reading 3.4):* toward 0.5: the configuration's unemployment insurance is a time-limited buffer of the kind Singapore's Jobseeker Support is, and Singapore's unit holds 0.5 on it with training and fiscal capacity, which this configuration also has.

#### NSD C1.4 Automation Resilience: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Poverty <8% | not shown | generous unemployment benefits and retraining are a buffer; the rationale says the configuration cannot sustain 50-70% displacement, without a model; no model or estimate of poverty on the Societal Poverty Line under a 30%, 50% or 70% displacement of paid hours is stated or cited, and none was located | Report v1.6, System 2, C1.4 |
| 2 | aggregate demand >85% baseline | not shown | no model or estimate of real final consumption expenditure against a pre-displacement baseline in any of the three scenarios is stated or cited, and none was located | Report v1.6, System 2, C1.4 |

*Note:* the 0.5 band's anchor example; it holds.

#### CPS C1.4 Automation Resilience: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Poverty <8% | not shown | employment guaranteed regardless of productivity separates income from market demand for labour; no model or estimate of poverty on the Societal Poverty Line under a 30%, 50% or 70% displacement of paid hours is stated or cited, and none was located | Report v1.6, System 3, C1.4 |
| 2 | aggregate demand >85% baseline | not shown | no model or estimate of real final consumption expenditure against a pre-displacement baseline in any of the three scenarios is stated or cited, and none was located | Report v1.6, System 3, C1.4 |

#### MS C1.4 Automation Resilience: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Poverty <8% | not shown | cooperatives can reduce hours rather than shed members and distribute automation's gains to them, under competitive pressure to automate; no model or estimate of poverty on the Societal Poverty Line under a 30%, 50% or 70% displacement of paid hours is stated or cited, and none was located | Report v1.6, System 4, C1.4 |
| 2 | aggregate demand >85% baseline | not shown | no model or estimate of real final consumption expenditure against a pre-displacement baseline in any of the three scenarios is stated or cited, and none was located | Report v1.6, System 4, C1.4 |

#### LM C1.4 Automation Resilience: 0.0 → 0.0

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Poverty <8% | not shown | no model or estimate of poverty on the Societal Poverty Line under a 30%, 50% or 70% displacement of paid hours is stated or cited, and none was located | Report v1.6, System 5, C1.4 |
| 2 | aggregate demand >85% baseline | not shown | no model or estimate of real final consumption expenditure against a pre-displacement baseline in any of the three scenarios is stated or cited, and none was located | Report v1.6, System 5, C1.4 |

*0.0 (protocol 2.1):* no structural mechanism addresses the criterion: the design removes the safety nets that exist and leaves income and demand to paid work alone.

#### MMT C1.4 Automation Resilience: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Poverty <8% | not shown | the Job Guarantee keeps income tied to (guaranteed) work; the rationale's 'can maintain 30% displacement but fails at 50-70%' is a judgement, not an estimate; no model or estimate of poverty on the Societal Poverty Line under a 30%, 50% or 70% displacement of paid hours is stated or cited, and none was located | Report v1.6, System 6, C1.4 |
| 2 | aggregate demand >85% baseline | not shown | no model or estimate of real final consumption expenditure against a pre-displacement baseline in any of the three scenarios is stated or cited, and none was located | Report v1.6, System 6, C1.4 |

#### UBI C1.4 Automation Resilience: 1.0 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Poverty <8% | not shown | an unconditional transfer is an explicit mechanism decoupling income from employment; the rationale's 'scales naturally with automation' is a design statement, not a level of poverty under a stated scenario; no model or estimate of poverty on the Societal Poverty Line under a 30%, 50% or 70% displacement of paid hours is stated or cited, and none was located | Report v1.6, System 7, C1.4 |
| 2 | aggregate demand >85% baseline | not shown | unconditional transfers sustain household spending, as the rationale says; no model or estimate of real final consumption expenditure against a pre-displacement baseline in any of the three scenarios is stated or cited, and none was located | Report v1.6, System 7, C1.4 |

*Note:* published 1.0 on the design's logic; under D28 silence is not clearance (protocol 2.3(b)), as parts (b4) and group 2.5 read Fully Automated Luxury Communism's, Participatory Economics' and CCO-PTF-CIP-SZH's 1.0s; a correction (reading 3.2).

#### DG C1.4 Automation Resilience: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Poverty <8% | not shown | reduced hours and work-sharing could absorb displacement; no mechanism for income as labour becomes optional is specified; no model or estimate of poverty on the Societal Poverty Line under a 30%, 50% or 70% displacement of paid hours is stated or cited, and none was located | Report v1.6, System 8, C1.4 |
| 2 | aggregate demand >85% baseline | not shown | no model or estimate of real final consumption expenditure against a pre-displacement baseline in any of the three scenarios is stated or cited, and none was located | Report v1.6, System 8, C1.4 |

#### SC C1.4 Automation Resilience: 0.0 → 0.0

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Poverty <8% | not shown | no model or estimate of poverty on the Societal Poverty Line under a 30%, 50% or 70% displacement of paid hours is stated or cited, and none was located | Report v1.6, System 9, C1.4 |
| 2 | aggregate demand >85% baseline | not shown | no model or estimate of real final consumption expenditure against a pre-displacement baseline in any of the three scenarios is stated or cited, and none was located | Report v1.6, System 9, C1.4 |

*0.0 (protocol 2.1):* no structural mechanism addresses the criterion: stakeholder governance leaves firms automating to stay competitive and adds nothing for income distribution or demand as automation advances; the 0.0 band's description.

*Flag (reading 3.4):* toward 0.5, on the host economy the reform keeps, as Status Quo's flag: the configuration's unemployment insurance is a time-limited buffer of the kind Singapore's Jobseeker Support is, and Singapore's unit holds 0.5 on it with training and fiscal capacity, which this configuration also has.

#### INT C1.4 Automation Resilience: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Poverty <8% | not shown | the white paper states that essentials remain accessible 'regardless of age or ability' and that automation lowers the labour needed for them, but access still 'emerges from participation' and redemption needs an ITC balance; it states no level of poverty under any displacement scenario and invites readers to stress-test it; no model or estimate of poverty on the Societal Poverty Line under a 30%, 50% or 70% displacement of paid hours is stated or cited, and none was located | Report v1.6, System 13, C1.4; Joseph, INTEGRAL: Technical White Paper v0.1 (December 2025; PDF md5 a6defc9a), sections 3, 6 and 11.8 and the closing invitation (evidence_cache/C1.4/integral_wp_v01_extract.txt) |
| 2 | aggregate demand >85% baseline | not shown | production planned on needs assessed through CDS, not on purchasing power, so demand does not require employment; no model or estimate of real final consumption expenditure against a pre-displacement baseline in any of the three scenarios is stated or cited, and none was located | Report v1.6, System 13, C1.4; Joseph, INTEGRAL: Technical White Paper v0.1 (December 2025; PDF md5 a6defc9a), sections 3, 6 and 11.8 and the closing invitation (evidence_cache/C1.4/integral_wp_v01_extract.txt) |

*Note:* read on the design's own white paper as group 2.6 read C5.2; it answers the rationale's question only in part (reading 3.5).

#### GEO C1.4 Automation Resilience: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Poverty <8% | not shown | an LVT-funded dividend would capture automation's surplus to the extent it capitalises into land values, an assumption less secure for AI-era capital; no model or estimate of poverty on the Societal Poverty Line under a 30%, 50% or 70% displacement of paid hours is stated or cited, and none was located | NEEC_Georgism_LVT_scoring_scratch.md, C1.4 |
| 2 | aggregate demand >85% baseline | not shown | no model or estimate of real final consumption expenditure against a pre-displacement baseline in any of the three scenarios is stated or cited, and none was located | NEEC_Georgism_LVT_scoring_scratch.md, C1.4 |

#### MC C1.4 Automation Resilience: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Poverty <8% | not shown | mutual credit sustains exchange without wage income, but a displaced member needs something other members want; no model or estimate of poverty on the Societal Poverty Line under a 30%, 50% or 70% displacement of paid hours is stated or cited, and none was located | NEEC_MutualCredit_LETS_scoring_scratch.md, C1.4 |
| 2 | aggregate demand >85% baseline | not shown | no model or estimate of real final consumption expenditure against a pre-displacement baseline in any of the three scenarios is stated or cited, and none was located | NEEC_MutualCredit_LETS_scoring_scratch.md, C1.4 |

#### DE C1.4 Automation Resilience: 0.0 → 0.0

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Poverty <8% | not shown | the social foundation is a measurement target, not a provision; no model or estimate of poverty on the Societal Poverty Line under a 30%, 50% or 70% displacement of paid hours is stated or cited, and none was located | NEEC_DoughnutEconomics_scoring_scratch.md, C1.4 |
| 2 | aggregate demand >85% baseline | not shown | no model or estimate of real final consumption expenditure against a pre-displacement baseline in any of the three scenarios is stated or cited, and none was located | NEEC_DoughnutEconomics_scoring_scratch.md, C1.4 |

*0.0 (protocol 2.1):* no structural mechanism addresses the criterion: automation is named as a concern and met with no income-distribution, contribution-recognition or demand-maintenance mechanism in the framework or its implementations.

#### UBS C1.4 Automation Resilience: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Poverty <8% | not shown | free provision of housing, food, healthcare, education, transport and information lowers the wage income needed to avoid poverty; no model or estimate of poverty on the Societal Poverty Line under a 30%, 50% or 70% displacement of paid hours is stated or cited, and none was located | NEEC_UniversalBasicServices_scoring_scratch.md, C1.4 |
| 2 | aggregate demand >85% baseline | not shown | the rationale finds no mechanism for demand because the services pay no cash; on the measure v2.0 names, final consumption expenditure includes general government's, so the services themselves count toward it; no model or estimate of real final consumption expenditure against a pre-displacement baseline in any of the three scenarios is stated or cited, and none was located | NEEC_UniversalBasicServices_scoring_scratch.md, C1.4; World Bank WDI, NE.CON.TOTL.KD, source note (evidence_cache/C1.4/wb_fce_kd_metadata.txt) |

*Note:* the rationale's demand-side finding is not borne out on the measure; the verdict is unchanged because neither clause is shown (reading 3.3).

#### SWF C1.4 Automation Resilience: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Poverty <8% | not shown | the fund's revenue does not erode with the wage base, but no payout scales with displacement (Norway's budget transfer; Alaska's fixed dividend); no model or estimate of poverty on the Societal Poverty Line under a 30%, 50% or 70% displacement of paid hours is stated or cited, and none was located | NEEC_SovereignWealthFundStatism_scoring_scratch.md, C1.4 |
| 2 | aggregate demand >85% baseline | not shown | no model or estimate of real final consumption expenditure against a pre-displacement baseline in any of the three scenarios is stated or cited, and none was located | NEEC_SovereignWealthFundStatism_scoring_scratch.md, C1.4 |

#### CN C1.4 Automation Resilience: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Poverty <8% | not shown | the state directs state-owned employers to absorb workers and has begun retraining for AI displacement; dibao reaches under 3% of the population; no model or estimate of poverty on the Societal Poverty Line under a 30%, 50% or 70% displacement of paid hours is stated or cited, and none was located | NEEC_StateCapitalism_China_scoring_scratch.md, C1.4 |
| 2 | aggregate demand >85% baseline | not shown | directed investment can sustain demand, as the rationale says (C3.1); no model or estimate of real final consumption expenditure against a pre-displacement baseline in any of the three scenarios is stated or cited, and none was located | NEEC_StateCapitalism_China_scoring_scratch.md, C1.4 |

#### SG C1.4 Automation Resilience: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Poverty <8% | not shown | Jobseeker Support pays up to S$6,000 over six months, conditional on job search, with training and reserve-funded wage subsidies; no model or estimate of poverty on the Societal Poverty Line under a 30%, 50% or 70% displacement of paid hours is stated or cited, and none was located | NEEC_StateCapitalism_Singapore_scoring_scratch.md, C1.4 |
| 2 | aggregate demand >85% baseline | not shown | no model or estimate of real final consumption expenditure against a pre-displacement baseline in any of the three scenarios is stated or cited, and none was located | NEEC_StateCapitalism_Singapore_scoring_scratch.md, C1.4 |

*Flag (reading 3.4):* toward 0.0: a six-month conditional payment is insurance against cyclical job loss, as Status Quo's unemployment insurance is, and the foreign-workforce margin is an exclusion, not a decoupling.

#### QA C1.4 Automation Resilience: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Poverty <8% | not shown | citizens' incomes rest on a hydrocarbon rent automation would not touch, through state jobs; non-citizens, most of the population the protocol counts (3.2), have no mechanism beyond departure; no model or estimate of poverty on the Societal Poverty Line under a 30%, 50% or 70% displacement of paid hours is stated or cited, and none was located | NEEC_StateCapitalism_Qatar_scoring_scratch.md, C1.4; SCORING_PROTOCOL.md 3.2 |
| 2 | aggregate demand >85% baseline | not shown | no model or estimate of real final consumption expenditure against a pre-displacement baseline in any of the three scenarios is stated or cited, and none was located | NEEC_StateCapitalism_Qatar_scoring_scratch.md, C1.4 |

*Note:* a buffer covering part of the relevant population is the 0.5 band (protocol 2.1).

#### IF C1.4 Automation Resilience: 0.0 → 0.0

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Poverty <8% | out of reach | the mechanism prices and structures credit; it governs neither household income nor final consumption, and the host economy's are not credited to it (protocol 3.2) | NEEC_IslamicFinance_scoring_scratch.md, C1.4; SCORING_PROTOCOL.md 3.2 |
| 2 | aggregate demand >85% baseline | out of reach | the mechanism prices and structures credit; it governs neither household income nor final consumption, and the host economy's are not credited to it (protocol 3.2) | NEEC_IslamicFinance_scoring_scratch.md, C1.4; SCORING_PROTOCOL.md 3.2 |

*0.0 (protocol 2.1):* no structural mechanism addresses the criterion: changing how credit is priced leaves distribution running through wage labour, as for Status Quo.

*Flag (reading 3.6):* toward 0.5, the published flag: profit-and-loss-sharing investment accounts read as a non-wage income channel that persists under displacement.

#### OS C1.4 Automation Resilience: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Poverty <8% | not shown | a commons share is not conditioned on employment and its non-wage income is observed, for members of a bounded resource; no model or estimate of poverty on the Societal Poverty Line under a 30%, 50% or 70% displacement of paid hours is stated or cited, and none was located | NEEC_Ostrom_Commons_scoring_scratch.md, C1.4 |
| 2 | aggregate demand >85% baseline | not shown | no aggregate-demand mechanism, as the rationale says; no model or estimate of real final consumption expenditure against a pre-displacement baseline in any of the three scenarios is stated or cited, and none was located | NEEC_Ostrom_Commons_scoring_scratch.md, C1.4 |

*Flag (reading 3.6):* toward 0.0, the published flag: a bounded subsistence base for a minority cannot hold poverty under 8% economy-wide at 70% displacement.

## 5. The sources added to the evidence cache

Both files were written on 2026-10-15. `wb_fce_kd_metadata.txt` holds the name, source and source note of the World
Bank's NE.CON.TOTL.KD series, from the World Bank's indicator API, with the raw response's md5 in its first lines.
`integral_wp_v01_extract.txt` holds five passages of the white paper's text (`pdftotext -layout`), each headed by its line
range, with the PDF's md5 (a6defc9a, the copy `NEEC_Rescoring_s58.md` read). The script checks each file's md5 and finds
each quoted passage in it. Session 59's files and index are unchanged; the script checks Session 59's extracts against
the index's digests and each unit's rationale against the index's location.

## 6. What parts (a), (b), groups 2.1 to 2.7 and part 58.1 change (generated)

| Entry | Published (rank) | After group 2.6 (rank) | After group 2.7 (rank) | Change here | Failures | Tier |
|---|---:|---:|---:|---:|---:|---|
| CCO | 24.5 (1) | 14.5 (1) | 14.5 (1) | 0.0 | 0 | Potentially Adequate |
| PE | 20.5 (2) | 14.0 (3) | 14.0 (3) | 0.0 | 1 | Potentially Adequate |
| NSD | 19.5 (3) | 13.5 (4) | 13.5 (4) | 0.0 | 1 | Potentially Adequate |
| INT | 19.5 (3) | 14.5 (1) | 14.5 (1) | 0.0 | 2 | Potentially Adequate |
| DG | 19.0 (5) | 13.0 (5) | 13.0 (5) | 0.0 | 2 | Potentially Adequate |
| MS | 16.5 (6) | 13.0 (5) | 13.0 (5) | 0.0 | 2 | Potentially Adequate |
| MMT | 15.5 (7) | 11.0 (14) | 11.0 (14) | 0.0 | 4 | Partially Adequate |
| UBI | 14.5 (8) | 11.0 (14) | 10.5 (15) | -0.5 | 7 | Structurally Inadequate |
| MC | 14.5 (8) | 12.5 (9) | 12.5 (9) | 0.0 | 3 | Partially Adequate |
| OS | 14.5 (8) | 13.0 (5) | 13.0 (5) | 0.0 | 3 | Partially Adequate |
| SWF | 14.0 (11) | 13.0 (5) | 13.0 (5) | 0.0 | 3 | Partially Adequate |
| SG | 14.0 (11) | 11.5 (11) | 11.5 (11) | 0.0 | 4 | Partially Adequate |
| GEO | 13.5 (13) | 12.5 (9) | 12.5 (9) | 0.0 | 2 | Potentially Adequate |
| UBS | 13.5 (13) | 11.5 (11) | 11.5 (11) | 0.0 | 4 | Partially Adequate |
| IF | 13.5 (13) | 11.5 (11) | 11.5 (11) | 0.0 | 5 | Partially Adequate |
| FALC | 13.0 (16) | 9.0 (18) | 9.0 (18) | 0.0 | 10 | Structurally Inadequate |
| DE | 11.5 (17) | 9.0 (18) | 9.0 (18) | 0.0 | 8 | Structurally Inadequate |
| SQ | 10.5 (18) | 9.5 (16) | 9.5 (16) | 0.0 | 9 | Structurally Inadequate |
| CPS | 10.0 (19) | 7.5 (22) | 7.5 (22) | 0.0 | 12 | Structurally Inadequate |
| SC | 10.0 (19) | 9.0 (18) | 9.0 (18) | 0.0 | 8 | Structurally Inadequate |
| CN | 10.0 (19) | 9.5 (16) | 9.5 (16) | 0.0 | 8 | Structurally Inadequate |
| QA | 9.0 (22) | 8.5 (21) | 8.5 (21) | 0.0 | 9 | Structurally Inadequate |
| LM | 8.0 (23) | 7.0 (23) | 7.0 (23) | 0.0 | 13 | Structurally Inadequate |

| Entry | Published | (a) | (b1) | (b2) | (b3) | (b4) | (b5) | (b6) | (b7) | 48.3 | (b8) | (b9) | (2.1) | (2.2) | (2.3) | (2.4) | (2.5) | 58.1 | (2.6) | (2.7) | Now | Re-estimated | At 0.5 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| CCO | 24.5 | -0.5 | -1.5 | -0.5 | -0.5 | -0.5 | -0.5 | -1.0 | -0.5 | -0.5 | -0.5 | -1.0 | -1.5 | -0.5 | -0.5 |  | -0.5 | 0.5 |  |  | 14.5 | 22 | 20 |
| PE | 20.5 |  | -1.5 | -0.5 | -0.5 | -1.5 |  | -0.5 | -0.5 |  | -0.5 | -0.5 |  |  | -0.5 |  |  |  |  |  | 14.0 | 17 | 16 |
| NSD | 19.5 | -2.5 | -1.0 | -0.5 | -0.5 | -0.5 |  |  |  |  | -0.5 | -0.5 |  | -0.5 |  | 0.5 |  |  |  |  | 13.5 | 16 | 15 |
| INT | 19.5 | -0.5 | -1.0 | -0.5 |  | -1.0 | -0.5 | -1.0 | -0.5 |  |  |  |  |  | -0.5 |  |  |  | 0.5 |  | 14.5 | 16 | 13 |
| DG | 19.0 |  | -1.5 | -0.5 | -0.5 | -0.5 |  | -0.5 | -1.0 |  | -1.0 |  |  |  | -0.5 |  |  |  |  |  | 13.0 | 16 | 16 |
| MS | 16.5 | -1.0 | -1.5 | -0.5 | -0.5 |  |  |  | 0.5 |  |  |  |  | -0.5 |  |  |  |  |  |  | 13.0 | 13 | 11 |
| MMT | 15.5 | -1.5 | -1.0 | -0.5 | -0.5 |  |  |  |  |  | -0.5 |  |  | -0.5 |  |  |  |  |  |  | 11.0 | 11 | 9 |
| UBI | 14.5 | -1.5 | -0.5 | -0.5 | -0.5 |  |  |  |  |  | -0.5 |  |  |  |  |  |  |  |  | -0.5 | 10.5 | 13 | 10 |
| MC | 14.5 |  | -1.0 | -0.5 |  |  | -0.5 |  |  |  |  |  |  |  |  |  |  |  |  |  | 12.5 | 10 | 7 |
| OS | 14.5 | -0.5 |  |  |  |  | -0.5 | -0.5 |  |  |  |  |  |  |  |  |  |  |  |  | 13.0 | 9 | 7 |
| SWF | 14.0 |  |  | -0.5 |  |  | -0.5 | -0.5 |  |  |  |  |  |  |  |  |  |  | 0.5 |  | 13.0 | 9 | 6 |
| SG | 14.0 | -1.0 | -0.5 | -0.5 |  |  |  |  |  |  |  |  |  | -0.5 |  |  |  |  |  |  | 11.5 | 8 | 8 |
| GEO | 13.5 | -0.5 |  |  |  |  | -0.5 |  |  |  |  |  |  |  |  |  |  |  |  |  | 12.5 | 7 | 6 |
| UBS | 13.5 |  | -0.5 | -0.5 |  |  | -0.5 |  |  |  |  |  |  |  |  | -0.5 |  |  |  |  | 11.5 | 9 | 6 |
| IF | 13.5 | -1.0 |  |  |  |  | -0.5 |  |  |  |  | -0.5 |  |  |  |  |  |  |  |  | 11.5 | 8 | 7 |
| FALC | 13.0 | -0.5 | -0.5 |  | -0.5 | -1.0 |  | -0.5 | -0.5 |  |  |  |  |  | -0.5 |  |  |  |  |  | 9.0 | 12 | 9 |
| DE | 11.5 | -0.5 | -0.5 |  |  |  | -0.5 | -0.5 | -0.5 |  |  |  |  |  |  |  |  |  |  |  | 9.0 | 10 | 8 |
| SQ | 10.5 | -0.5 |  |  |  | -0.5 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 9.5 | 7 | 5 |
| CPS | 10.0 | -1.5 |  |  | -0.5 |  |  |  |  |  | -0.5 |  |  |  |  |  |  |  |  |  | 7.5 | 9 | 6 |
| SC | 10.0 |  | -1.0 |  |  |  |  |  |  |  |  | -0.5 |  |  |  | 0.5 |  |  |  |  | 9.0 | 7 | 6 |
| CN | 10.0 |  |  | -0.5 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 9.5 | 6 | 5 |
| QA | 9.0 | -0.5 |  | -0.5 |  |  |  |  |  |  |  |  |  |  |  | 0.5 |  |  |  |  | 8.5 | 7 | 7 |
| LM | 8.0 | -1.5 |  |  |  |  |  |  |  |  |  | -0.5 |  | 0.5 |  | 0.5 |  |  |  |  | 7.0 | 9 | 6 |

After this group the corpus has 17 dominance pairs against 17 after group 2.6 (new: none; lost: none), and its frontier holds 15 entries against 15 (SQ, NSD, CPS, MS, LM, UBI, DG, FALC, PE, CCO, INT, MC, SWF, IF, OS). First place is shared by CCO and INT at 14.5 (CCO 14.5, INT 14.5 after group 2.6), ahead of PE at 14.0. Across the pass so far 251 units have been re-estimated, each counted once: 18 are at 1.0, 209 at 0.5 and 24 at 0.0; against their published scores 148 fell, 7 rose and 96 are unchanged (net -70.5 points).

Anchor examples citing a unit the pass moves: C1.1's 1.0 example, NSD (part (b3)); C1.2a's 1.0 example, MS (part (2.2)); C1.2b's 1.0 example, CCO (part (2.5)); C1.4's 1.0 example, CCO (part (2.5)); C2.1's 1.0 example, UBI (part (a)); C2.3's 1.0 example, DG (part (b1)); C2.4's 1.0 example, PE (part (b1)); C2.5's 1.0 example, CCO (part (b5)); C3.1's 1.0 example, UBI (part (b2)); C3.2's 1.0 example, PE (part (b4)); C3.5's 1.0 example, CCO (part (b6)); C3.5's 0.0 example, LM (part (2.4)); C3.5's 0.0 example, SC (part (2.4)); C4.1's 1.0 example, DG (part (b6)); C4.2's 1.0 example, PE (part (b7)); C4.3's 1.0 example, CCO (part (b8)); C5.1's 1.0 example, MS (part (b2)); C5.2's 1.0 example, CCO (part (b9)); C5.2's 0.0 example, INT (part (2.6)); C5.4's 1.0 example, CCO (part (b9)); C5.5's 1.0 example, PE (part (b9)). Bands whose example the pass moves and which no corpus unit then scores at their value: C1.1's 1.0, C1.2a's 1.0, C1.4's 1.0, C2.1's 1.0, C2.3's 1.0, C2.4's 1.0, C3.1's 1.0, C3.5's 1.0, C4.1's 1.0, C4.2's 1.0, C4.3's 1.0.

C1.4's published anchors: CCO-PTF-CIP-SZH at 1.0 (moved to 0.5 by group 2.5), Nordic Social Democracy at 0.5 (holds) and
Status Quo at 0.0 (holds, flagged toward 0.5). After this group no corpus unit is at 1.0 on C1.4; stage 3's restatement
of the criterion's anchors drops the 1.0 band's example, as C1.1's and C1.2a's were dropped.

## 7. Corrections found (not polish)

1. **Universal Basic Income's C1.4, 1.0 → 0.5** (reading 3.2): a published 1.0 resting on the design's logic, with no
   level under any scenario stated, as part (b4) and group 2.5 found for the three other 1.0s.
2. **Universal Basic Services' C1.4 rationale** finds no demand-side mechanism because the services pay no cash; on the
   measure v2.0 names, government final consumption counts toward demand (reading 3.3). Report v2.0 says so; the verdict
   is unchanged.
3. **Status Quo's C1.4 rationale** says that "no mechanism exists"; the configuration has unemployment insurance, and
   Singapore's 0.5 rests on a buffer of the same kind (reading 3.4). Report v2.0 states the peer question and both flags.
4. **Integral's C1.4 rationale** asks whether essentials are unconditional; the white paper, published after the corpus
   scored the design, answers it in part (reading 3.5). Report v2.0 cites the paper.

## 8. Disclosure

CCO-PTF-CIP-SZH is the owner's design. Its C1.4 unit was read in group 2.5 and is not re-read here; this group changes
none of its scores. First place stays shared at 14.5 by CCO-PTF-CIP-SZH and Integral: Integral's unit, which alone could
have changed that, holds at 0.5 on reading 3.5, which was made on the white paper's text before the consequences were
computed. Every reading here was made before the consequences table was computed. The peer question of reading 3.4 was
found while reading; holding all three published scores is the course that moves no score on an open question, and the
flags carry both readings.

## 9. What remains

- **Next group from the triage** (rerun after this group, `triage_s52_output.txt`): C4.3 Group Equity, class M (16 units
  in play, 4 tier-capable), a judgment re-read with no cache needed; part (b8) planned its readings 3.2 to 3.5. Then
  C3.1, C4.2, C1.1, C4.1, C2.1, C2.4, C2.3, C4.4, C4.5, C2.5 and C3.4. The units that alone could change who is first are
  now seven (NSD C2.5, PE C2.5, PE C4.5, CCO C4.5, INT C1.1, INT C3.4, INT C4.3); the units that could change no failure
  count, tier or rank on their own are still seven.
- **`evidence_cache_s59.py`'s check [2]** compares the units in play *now* with its index, so it reports a failure once
  this group is part of the pass; its digest checks still pass. It is not a harness check and is not edited here.
- **For the criteria record's next amendment:** decision 60.1 (what C1.4's clauses ask; final consumption counts
  government's), with the method choices listed in `STATE.md`; C1.4's anchors (section 6).
- **For Report v2.0:** section 7's corrections and the peer question of reading 3.4.
- **Sources a later session could add:** any published model of an economy under a 30%, 50% or 70% displacement of paid
  hours. None was located; one would be the first evidence that could show either clause for any entry.

## 10. What this record does not show

No source located models any entry's poverty or final consumption under the three displacement scenarios, so C1.4 can at
present separate only 0.0 from 0.5, as for C3.5's clause 2. "Not shown" means that no estimate was located, not that
the clause fails. The cache holds no OECD page (HTTP 403). The white paper is read in five passages chosen by searching
its text for automation, essentials, unemployment and contribution; it is 345 pages and a later version may say more.
The interpretation check (decisions 50.1 to 50.4) was not run; it is optional. The record is one scorer's re-estimation;
whether its calls reproduce is what the replication programme tests.
