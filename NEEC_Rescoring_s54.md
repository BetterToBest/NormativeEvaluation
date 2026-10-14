# NEEC Rescoring Pass — Record, Stage 2, Group 2.3: C1.3 Housing Security (class M)

**Session 54 · 2026-10-14 · Scorer and engineer: Claude · Owner: Duke Johnson**
**Status: scratch (protocol 10.1). Parts (a) and (b) and groups 2.1 and 2.2 are `NEEC_Rescoring_s37.md` to
`NEEC_Rescoring_s53.md`; this record edits none of them.** No corpus file, score or scoring document changes until the
pass ends. Its changes are then applied by generator with pinned inputs and restated in place (protocol 10.2, 10.3;
decisions D12, D14), and until then the published totals stand, provisional as `README.md` says. Decisions taken here
are Claude's under the owner's delegation (Handoff 35, section 2); each is recorded with its reasons, and the owner may
reverse any of them.
**Reproduce:** `python3 rescoring_s54.py` (harness check 103). It is the second group written on the shared module
(`pass_common.py`, decision 52.5): the script holds the 20 readings and the group's own checks, and the module computes
the consequences cumulatively with every part before it. It recomputes the figures the readings derive, checks the
simulation runs' captured output by digest and every figure quoted from it, and checks that this record contains its
generated tables verbatim. The runs themselves: `node cco_c13_checks_s54.js path/to/harness.js path/to/index.html` on
a clone of `BetterToBest/compassionism-simulation` at `5a7a7b1` (about one minute); the harness does not rerun the
JavaScript, as with Sessions 38, 40, 51 and 53.

---

## 1. What this group is

The consequence triage (`triage_s52.py`, decision 52.7), rerun after group 2.2, put C1.3 first among the criteria still
to read: 20 units in play, five of them able to change an adequacy tier on their own. C1.3 is class M: v2.0 restated its
bar (codes K6, R2; `NEEC_Criteria_v2_s45.md`, section 4). The Pass Threshold has two clauses: "≥88% housing stability
over 5-year periods" and "housing costs ≤30% of disposable income at 80% of regional median household disposable
income". The second replaces Paper v1.4's "affordability at 80% AMI", a United States term, with a measure any national
survey can report (the OECD Affordable Housing Database, EU-SILC, national household surveys) and that a design can
project. Three units were re-estimated earlier and are not re-read: Nordic Social Democracy's (part (b1)), MMT + Job
Guarantee's and Singapore's (part (a)), all at 0.5. For class M every other unit is re-checked clause by clause against
Appendix V in the D28 form (section 7 of the criteria record): six published 1.0s, eleven 0.5s and three 0.0s.

**Outcome.** One entry clears C1.3: Centrally Planned Socialism, the 1.0 band's anchor, on the historical record
(reading 3.4), flagged. **Five units fall** from 1.0 to 0.5: Degrowth, Fully Automated Luxury Communism, Participatory
Economics, CCO-PTF-CIP-SZH and Integral. None of them estimates either clause, or, for CCO-PTF-CIP-SZH, shows either on
its published model (readings 3.2 and 3.3). Fifteen hold; none rises. Net −2.5 points; **no failure count and no tier
changes.** CCO-PTF-CIP-SZH keeps first place, 15.0 to 14.5; Participatory Economics and Integral share second at 14.0.

## 2. How a clause is recorded, and the rule

As in group 2.2, section 2, and decision 53.2: each clause is cleared, short, not shown, out of reach or moot. A unit is
1.0 only if both clauses are cleared (D28, protocol 2.3); 0.0 only on one of protocol 2.1's whole-criterion conditions,
stated as the unit's reason and never with a clause cleared; 0.5 otherwise. A clause-level gap never makes 0.0 (D28(f)).
"Not shown" means that no estimate or evidence of the clause's quantity was located, not that the clause fails; "short"
means the evidence located falls below it.

## 3. Decisions and readings (under the delegation)

**3.1 What the clauses ask (decision 54.1).** *Clause 1:* at least 88% of participants keep their housing over a 5-year
period without involuntary displacement, which the measurement field names as foreclosure, eviction or inability to
afford rent increases. A stability rate is shown by a 5-year measure, or by a bound: where the channels of displacement
the field names are closed to all but an identified share of the population, one minus that share is a lower bound on
the rate. An annual displacement rate *d* bounds the 5-year rate between 1 − 5*d* and 1 − *d*; it clears only if the
lower bound reaches 88%. *Clause 2:* housing is affordable to a household at 80% of the regional median household
disposable income when its housing costs (rent or mortgage payments plus utilities) are at most 30% of its disposable
income. The clause is about households at that income as a class, renters at market prices included, not about the
luckiest of them. Where a survey measures cost burden on pre-tax income (the United States), a burden on pre-tax income
is a larger burden on disposable income, so a shortfall on pre-tax income is a shortfall. For a design, "projected on
the same measure" (the field's words) means a stated cost or cost share; a description of housing as decommodified,
universal or affordable is not a projection. *Alternative:* read clause 2 as the median cost ratio of all households at
that income, owners with old mortgages included. Rejected for the comparative cases because it would measure the price
of housing bought long ago rather than the price a household at that income now faces, which is what the criterion's
"resistant to market volatility" concerns; no unit's verdict turns on it here, since no unit that is short on renters
would clear on the other reading with its clause 1 shown.

**3.2 The designs that state no figure.** Degrowth (community land trusts, cooperatives, rent control), Fully Automated
Luxury Communism (automated construction, universal provision), Participatory Economics (allocation by consumption
councils) and Integral (community-controlled allocation, cooperative ownership) were published at 1.0 on descriptions of
decommodified housing. None states a stability rate or a housing cost, and none cites a source that does. Protocol
2.3(b): silence is not clearance. Each falls to 0.5, both clauses not shown. Integral's rationale cites the criterion's
own benchmark, community land trusts' 0.46% foreclosure rate against 3.26% for conventional mortgages in 2008–2010, as
making 90%+ stability plausible. A crisis foreclosure rate among trust homeowners is evidence for one channel and one
tenure, not a 5-year stability rate for the population a comprehensive system serves (protocol 3.2), and clause 2 is
silent in any case. *Alternative:* credit a design whose named housing mechanism has a documented record (trusts,
cooperatives) with that record's rate. Rejected: no such record states either clause's quantity for a whole population,
and the rule for every design in the pass has been that a clause the design does not estimate cannot support a 1.0.

**3.3 CCO-PTF-CIP-SZH on its published model (decision 54.2; reading 3.10 of group 2.1).** The published 1.0 rests on
the papers' "PTF housing achieves 94% stability rates (validated through CLT data)" and "average cost reductions of 60%
compared to traditional rental markets" (`cco-ptf-integrated-framework.html`, sections 4 and 5). The model at the pin
frozen for v2.0 (`5a7a7b1`, v4.20; decision 52.9) is the design's published model, so it governs where it computes the
quantity (group 2.1, reading 3.2). It does not compute either: its documentation states that "the engine models no
housing tenure" (CONTRIBUTING.md, the extreme-poverty overlay), and it carries no housing-cost line (Public Trust Housing
scales the whole living-wage basket by 0.65). Its nearest measure is housing distress: a year in which an agent's cash
income and the savings it holds cannot cover the basket. A new runner, `cco_c13_checks_s54.js`, counts the agents who
pass a whole 5-year window with no such year (section 5). In the reference run, 78.5% to 86.4% do, depending on the
window, against 50.4% to 57.8% in the matched Baseline: the design's mechanisms add 22 to 35 points. In years 16 to 20,
83 of 500 seeds reach 88%. Inside Public Trust Housing, 93.6% to 96.8% pass every window, the papers' 94%; but Public
Trust Housing holds 20.1% of agents (the model's uptake setting, 20%, "a conservative housing transition rate"), and
outside it 74.7% to 83.7% pass. The papers' 60% cost reduction likewise applies to Public Trust Housing residents. The
design is a comprehensive system, so its participants are the population its sources serve, a whole society (protocol
3.2); a narrower population is a scope matter, not a flag (protocol 3.4). *Decision:* both clauses are not shown; the
unit is 0.5, not flagged. The distress measure is a proxy and is not read as short: it counts a shortfall of income as
displacement, which overstates instability, and counts no move for any other cause, which understates it. In the
Adverse Environment, which the criterion's "resistant to market volatility" bears on, 63.5% of agents pass years 16 to
20, against 23.2% in its matched Baseline. *Alternative:* credit the papers' 94%. Rejected: the model behind the
papers' figures is not published (CONTRIBUTING.md, NEEC note 1), and the published model gives 94% only to the fifth of
agents in Public Trust Housing. For version 2.1: a version of the model with housing tenure and a housing-cost line,
showing 88% of all agents stable over 5-year windows and housing costs at or under 30% of disposable income at 80% of
the median, would clear it (section 8).

**3.4 Centrally Planned Socialism on the historical record (decision 54.3).** The 1.0 band's anchor ("universal housing
provision through state allocation... homelessness essentially eliminated"). Protocol 4.1: a historical system is scored
from the record, collapse included. *Clause 2:* housing fees, communal services included, were about 2.5% of an average
worker's or employee's income in 1990 (Childress, Kutuzov and Haase 2001, section 3), and fees for maintenance and utilities had been
unchanged since 1928 (section 7); a household at 80% of the median paid of the order of 3%. After the
system ended, rents rose steeply, and the poorest Russian quintile's rent-to-income ratio reached 18.6% in 1995 (section
7, citing Bobyr and Lee 1997), still under 30%. Cleared. *Clause 1:* no 5-year stability rate is documented.
But the three channels the measurement names were closed to state tenants: there were no mortgages, rents did not rise,
and eviction was "virtually unheard of in public housing" (section 10). The exposed segment is the
workers' hostels, whose places went with the job: 6% of households in the 1989 census, with 5% in communal apartments
and 2% renting space (IMF, World Bank, OECD and EBRD, *A Study of the Soviet Economy*, 1991, chapter V.9, as the
publisher's catalogue quotes it; the chapter's text refused retrieval, HTTP 403). Counting every hostel household as
displaced within five years leaves 94% stable. Through the collapse, flats passed to their occupants, voluntarily and
practically free of charge (section 6); the post-Soviet evictions this session's searches located concern hostel
residents, after hostels were privatised (reports from Moscow and Dushanbe). Cleared, by a bound. *Decision:* 1.0 holds, flagged toward 0.5. The flag records what the bound does not
cover: it rests on the late-Soviet record, not on a measured rate; the deportations of the 1930s and 1940s were forced
displacement by the state on a large scale; and the configuration's other states (the Eastern Bloc, Cuba, North Korea) are not measured
here. *Alternative:* 0.5, not
shown, for want of a measured rate. Rejected: clause 1 asks for a rate at or above 88%, and a lower bound of 94% derived
from the record shows it for the system's mature form; the earlier period and the other states are carried by the flag.
The anchor holds.

**3.5 The configured national economies.** *Status Quo* (United States): 80% of the 2023 median household income
($80,610, pre-tax; US Census Bureau, P60-282) is $64,488, inside the $45,000 to $74,999 band, where 45% of renter
households pay 30% or more of pre-tax income on housing and utilities; half of all renter households, a record 22.6
million, are cost-burdened (Joint Center for Housing Studies, *The State of the Nation's Housing 2025*, 2023 data). On
disposable income, the clause's basis, the share is larger. Clause 2 is short. For clause 1 there is no national measure
of 5-year involuntary displacement; landlords filed 3.6 million eviction cases against 2.7 million households in 2018
(Eviction Lab), on about a third of households who rent. Not shown. The published rationale's "72% stability over 5
years" for market-rate rental has no located source; it coincides with the design papers' figure for CCO alone and is
replaced. 0.5, as published. *Stakeholder Capitalism:* the host economy's housing, with employer housing assistance:
clause 2 short, clause 1 not shown, as for Status Quo; 0.5. *China:* forced relocation of about 12.6 million households
in 2008–2012, pre-sale failure (more than 85% of homes sold before completion by 2022; mortgage boycotts at over 300
developments) and the historical exclusion of about 300 million migrant workers from city housing support; no 5-year
rate or cost share is reported: both not shown, 0.5. *Qatar:* for citizens housing is largely decommodified; for the
non-citizen majority, housing and residence depend on continuous employment with an employer who can cancel the visa;
neither clause has a figure for the configured population (protocol 3.2): 0.5; the citizens-only scenario (1.0) stays a
scenario. *Nordic Social Democracy and Singapore,* re-estimated in parts (b1) and (a), had clause 1 read as cleared on
their units' own text ("about 90% or more"; "far above the threshold for the resident population"). Under reading 3.1
an unsourced figure would be not shown. Neither verdict changes, since both units are 0.5 on a short clause 2; the
earlier parts are not edited, and Report v2.0 gives clause 1 for both as not shown.

**3.6 The mechanisms.** Universal Basic Income (the 0.5 band's anchor), Market Socialism (housing cooperatives within a
market allocation), Georgism (supply effects of the tax, no tenant stability; Estonia's land tax did not prevent the
Tallinn bubble), Islamic finance (diminishing partnership, a real housing product priced at market rates), Ostrom-style
commons (community land trusts counted in under D31, with the scenario counting them out at 0.0) and Universal Basic
Services (zero-rent social housing on a needs basis, never implemented at the scale proposed) each have a genuine
housing mechanism and no figure for either clause: 0.5, as published. Mutual Credit/LETS and Sovereign Wealth Fund
Statism have no housing channel of any kind; both clauses are out of reach and each stays 0.0 on that whole-criterion
reason. Libertarian Minarchism is the 0.0 band's anchor, pure market allocation with no stabilizing mechanism: 0.0.
*Doughnut Economics* is held at 0.5: housing is one of its twelve social-foundation dimensions, its City Portraits track
affordability, and one narrow policy output is located. The published scoring document says itself that the framework
has "no housing-specific mechanism of DE's own"; group 2.2 gave the framework's C1.2a 0.0 on the same kind of finding
("adopts none as its own"). *Decision:* hold, flagged toward 0.0. *Alternative:* 0.0, as consistency with C1.2a would
suggest (protocol 2.3(e)). Not adopted: the C1.2a unit was 0.0 as published and its flag ran toward 0.5, so the two
criteria's published readings already differ on whether the framework's diagnostic process counts; the pass re-checks
clauses and corrects inconsistencies of reading, and here the difference is one of evidence (a tracked housing
dimension and a policy output, against no wealth vehicle at all). The flag puts the question to the owner. Either way no
tier changes: the framework has eight failures.

## 4. The units

### 4.1 Summary (generated)

| Entry | Published | Clause 1 | Clause 2 | Verdict | Flag |
|---|---:|---|---|---:|---|
| SQ | 0.5 | not shown | short | 0.5 |  |
| CPS | 1.0 | cleared | cleared | 1.0 | toward 0.5: the clause is cleared by a bound on the late-Soviet record, not by a measured rate, and the bound does not cover the deportations of the 1930s and 1940s or the configuration's other states |
| MS | 0.5 | not shown | not shown | 0.5 |  |
| LM | 0.0 | not shown | not shown | 0.0 |  |
| UBI | 0.5 | not shown | not shown | 0.5 |  |
| DG | 1.0 | not shown | not shown | 0.5 |  |
| SC | 0.5 | not shown | short | 0.5 |  |
| FALC | 1.0 | not shown | not shown | 0.5 |  |
| PE | 1.0 | not shown | not shown | 0.5 |  |
| CCO | 1.0 | not shown | not shown | 0.5 |  |
| INT | 1.0 | not shown | not shown | 0.5 |  |
| GEO | 0.5 | not shown | not shown | 0.5 |  |
| MC | 0.0 | out of reach | out of reach | 0.0 |  |
| DE | 0.5 | not shown | not shown | 0.5 | toward 0.0, the reading of the framework's C1.2a: no housing mechanism of its own |
| UBS | 0.5 | not shown | not shown | 0.5 |  |
| SWF | 0.0 | out of reach | out of reach | 0.0 |  |
| CN | 0.5 | not shown | not shown | 0.5 |  |
| QA | 0.5 | not shown | not shown | 0.5 |  |
| IF | 0.5 | not shown | not shown | 0.5 |  |
| OS | 0.5 | not shown | not shown | 0.5 |  |

### 4.2 Clause by clause (generated)

#### SQ C1.3 Housing Security: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥88% housing stability over 5-year periods | not shown | no national measure of 5-year involuntary displacement exists; in 2018 landlords filed 3.6 million eviction cases against 2.7 million households, and renters, about a third of households, carry most of the exposure; the published 72%, for market-rate rental only, has no located source (reading 3.5) | Eviction Lab (Princeton University), national data update of 11 July 2022, figures for 2018; Report v1.6, System 1, C1.3 |
| 2 | housing costs ≤30% of disposable income at 80% of regional median household disposable income | short | 80% of the 2023 median household income ($80,610) is $64,488, inside the $45,000 to $74,999 band, where 45% of renter households pay 30% or more of pre-tax income on housing and utilities; on disposable income, the clause's basis, the share is larger; half of all renter households, a record 22.6 million, are cost-burdened | Joint Center for Housing Studies of Harvard University, The State of the Nation's Housing 2025 (2023 data; cost burden: 30% or more of pre-tax household income on housing and utilities), as summarised by the National Low Income Housing Coalition, Memo to Members, 30 June 2025; US Census Bureau, Income in the United States: 2023 (P60-282), real median household income $80,610, pre-tax money income |

*Note:* the published rationale's 72% is replaced by sourced figures; the verdict is unchanged.

#### CPS C1.3 Housing Security: 1.0 → 1.0

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥88% housing stability over 5-year periods | cleared | no 5-year rate is documented, but the three causes of displacement the measure names were closed to state tenants: no mortgages, rents and fees unchanged since 1928, and eviction 'virtually unheard of in public housing'; the exposed segment, workers' hostels whose places went with the job, held 6% of households in the 1989 census; counting every hostel household as displaced within five years leaves 94% stable; through the collapse, flats passed to their occupants practically free of charge (reading 3.4) | Childress, Kutuzov and Haase, A Decade of Housing Reform in Russia (Land Tenure Center, University of Wisconsin-Madison, draft of 26 July 2001; md5 babfbd70), sections 3, 6, 7 and 10; IMF, World Bank, OECD and EBRD, A Study of the Soviet Economy (1991), vol. 3, chapter V.9 Housing, citing the 1989 census (read from the publisher's catalogue excerpt; the chapter's text refused retrieval) |
| 2 | housing costs ≤30% of disposable income at 80% of regional median household disposable income | cleared | housing fees, communal services included, were about 2.5% of an average worker's or employee's income in 1990, so a household at 80% of the median paid of the order of 3%; after the system ended, the poorest Russian quintile's rent-to-income ratio reached 18.6% in 1995, still under 30% | Childress, Kutuzov and Haase, A Decade of Housing Reform in Russia (Land Tenure Center, University of Wisconsin-Madison, draft of 26 July 2001; md5 babfbd70), sections 3, 6, 7 and 10 |

*Flag (reading 3.4):* toward 0.5: the clause is cleared by a bound on the late-Soviet record, not by a measured rate, and the bound does not cover the deportations of the 1930s and 1940s or the configuration's other states.

*Note:* the 1.0 band's anchor example; it holds.

#### MS C1.3 Housing Security: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥88% housing stability over 5-year periods | not shown | housing cooperatives exist within the cooperative movement, but the market still allocates most housing; no stability rate, documented or designed, is stated, and no source the unit cites gives one | Report v1.6, System 4, C1.3 |
| 2 | housing costs ≤30% of disposable income at 80% of regional median household disposable income | not shown | no housing cost, and no share of income at 80% of the median, is stated or projected; cooperative housing is a minority tenure | Report v1.6, System 4, C1.3 |

#### LM C1.3 Housing Security: 0.0 → 0.0

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥88% housing stability over 5-year periods | not shown | pure market allocation with no stabilizing mechanism; no rate is stated | Report v1.6, System 5, C1.3 |
| 2 | housing costs ≤30% of disposable income at 80% of regional median household disposable income | not shown | no affordability instrument of any kind; housing costs are whatever the market sets | Report v1.6, System 5, C1.3 |

*0.0 (protocol 2.1):* no structural mechanism addresses the criterion: pure market allocation with no stabilizing mechanism (the 0.0 band's anchor).

#### UBI C1.3 Housing Security: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥88% housing stability over 5-year periods | not shown | stable income improves housing security for many; no stability rate, documented or designed, is stated, and no source the unit cites gives one | Report v1.6, System 7, C1.3 |
| 2 | housing costs ≤30% of disposable income at 80% of regional median household disposable income | not shown | the transfer raises income, but without housing policy landlords can capture it through rent increases; no housing cost, and no share of income at 80% of the median, is stated or projected | Report v1.6, System 7, C1.3; Paper v1.4, Appendix H.7 |

*Note:* the 0.5 band's anchor example; it holds.

#### DG C1.3 Housing Security: 1.0 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥88% housing stability over 5-year periods | not shown | community land trusts, housing cooperatives and rent controls are named as the design's housing mechanism; no stability rate, documented or designed, is stated, and no source the unit cites gives one | Report v1.6, System 8, C1.3 |
| 2 | housing costs ≤30% of disposable income at 80% of regional median household disposable income | not shown | no housing cost, and no share of income at 80% of the median, is stated or projected; the design names decommodification, not a cost | Report v1.6, System 8, C1.3 |

*Note:* published 1.0 read in the D28 form (silence is not clearance, protocol 2.3(b)): neither clause is estimated, so the unit falls to 0.5 (reading 3.2).

#### SC C1.3 Housing Security: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥88% housing stability over 5-year periods | not shown | the host economy's housing (Status Quo's) with some employer housing assistance; no national measure of 5-year displacement exists, as for Status Quo | Report v1.6, System 9, C1.3; Eviction Lab (Princeton University), national data update of 11 July 2022, figures for 2018 |
| 2 | housing costs ≤30% of disposable income at 80% of regional median household disposable income | short | housing remains market-allocated; at 80% of the US median, $64,488, 45% of renter households in the $45,000 to $74,999 band pay 30% or more of pre-tax income, and no source shows the reform changing it | Report v1.6, System 9, C1.3; Joint Center for Housing Studies of Harvard University, The State of the Nation's Housing 2025 (2023 data; cost burden: 30% or more of pre-tax household income on housing and utilities), as summarised by the National Low Income Housing Coalition, Memo to Members, 30 June 2025; US Census Bureau, Income in the United States: 2023 (P60-282), real median household income $80,610, pre-tax money income |

#### FALC C1.3 Housing Security: 1.0 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥88% housing stability over 5-year periods | not shown | automated construction and universal provision are projected to achieve complete housing security; no stability rate, documented or designed, is stated, and no source the unit cites gives one | Report v1.6, System 10, C1.3 |
| 2 | housing costs ≤30% of disposable income at 80% of regional median household disposable income | not shown | no housing cost, and no share of income at 80% of the median, is stated or projected; provision is described as universal, not costed | Report v1.6, System 10, C1.3 |

*Note:* published 1.0 read in the D28 form: neither clause is estimated, so the unit falls to 0.5 (reading 3.2).

#### PE C1.3 Housing Security: 1.0 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥88% housing stability over 5-year periods | not shown | housing is allocated by consumption councils on needs and effort and described as decommodified and stable; no stability rate, documented or designed, is stated, and no source the unit cites gives one | Report v1.6, System 11, C1.3 |
| 2 | housing costs ≤30% of disposable income at 80% of regional median household disposable income | not shown | no housing cost, and no share of income at 80% of the median, is stated or projected; allocation by effort rating sets no housing charge that can be read against income | Report v1.6, System 11, C1.3 |

*Note:* published 1.0 read in the D28 form: neither clause is estimated, so the unit falls to 0.5 (reading 3.2).

#### CCO C1.3 Housing Security: 1.0 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥88% housing stability over 5-year periods | not shown | the engine models no housing tenure, so it computes no stability rate; on its nearest measure, a year in which cash income and savings cannot cover the basket, 86.4% of agents pass years 16 to 20 with no such year (83 of 500 seeds at 88% or more) and 78.5% the weakest 5-year window, against 51.1% in the matched Baseline; inside Public Trust Housing, which holds 20.1% of agents, 93.6% to 96.8% pass every window, outside it 74.7% to 83.7%; the papers' 94% has no published model behind it (reading 3.3) | Compassionism Simulation at 5a7a7b1 (v4.20), harness.js (md5 fe6fa4a3) and index.html (md5 c333b632); cco_c13_checks_s54_output.txt; the simulation's CONTRIBUTING.md at 5a7a7b1 (md5 bba4ef73), the extreme-poverty overlay; research hub at 8e8a6ba, cco-ptf-integrated-framework.html (md5 10ab8364), sections 4 and 5; Report v1.6, System 12, C1.3 |
| 2 | housing costs ≤30% of disposable income at 80% of regional median household disposable income | not shown | the engine carries no housing-cost line (Public Trust Housing scales the whole basket by 0.65); the papers' average housing cost reduction of 60% against market rents applies to Public Trust Housing residents, 20.1% of agents in the reference run, and no cost share at 80% of the median is stated | Compassionism Simulation at 5a7a7b1 (v4.20), harness.js (md5 fe6fa4a3) and index.html (md5 c333b632); cco_c13_checks_s54_output.txt; the simulation's CONTRIBUTING.md at 5a7a7b1 (md5 bba4ef73), the extreme-poverty overlay; research hub at 8e8a6ba, cco-ptf-integrated-framework.html (md5 10ab8364), sections 4 and 5 |

*Note:* published 1.0 read in the D28 form: neither clause is shown on the published model, and its nearest measure falls short of 88% in every window for the population the design serves; Public Trust Housing residents clear it, a narrower population, which is a scope matter (protocol 3.4), not a flag.

#### INT C1.3 Housing Security: 1.0 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥88% housing stability over 5-year periods | not shown | community-controlled allocation and cooperative ownership; the rationale cites the criterion's own benchmark, community land trusts' foreclosure rate of 0.46% against 3.26% in 2008-2010, as making 90%+ plausible; a crisis foreclosure rate for trust homeowners is not a 5-year stability rate for the system's population, and no stability rate, documented or designed, is stated, and no source the unit cites gives one | Report v1.6, System 13, C1.3 |
| 2 | housing costs ≤30% of disposable income at 80% of regional median household disposable income | not shown | no housing cost, and no share of income at 80% of the median, is stated or projected | Report v1.6, System 13, C1.3 |

*Note:* published 1.0 read in the D28 form: neither clause is estimated, so the unit falls to 0.5 (reading 3.2).

#### GEO C1.3 Housing Security: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥88% housing stability over 5-year periods | not shown | the tax discourages land-banking and raises construction density, but addresses neither eviction nor rental stability; Estonia's land tax did not prevent the Tallinn housing bubble of about 2003 to 2008 | NEEC_Georgism_LVT_scoring_scratch.md, C1.3; Report v1.6, System 14, C1.3 |
| 2 | housing costs ≤30% of disposable income at 80% of regional median household disposable income | not shown | supply effects are measured in housing-unit growth, not in housing costs against income; no affordability figure for households at 80% of the median is located | NEEC_Georgism_LVT_scoring_scratch.md, C1.3 |

#### MC C1.3 Housing Security: 0.0 → 0.0

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥88% housing stability over 5-year periods | out of reach | no housing-specific design element, volatility buffer or stability outcome in any source reviewed (WIR, Sardex, LETS, time banking, Trueque, Grassroots Economics) | Report v1.6, System 15, C1.3 |
| 2 | housing costs ≤30% of disposable income at 80% of regional median household disposable income | out of reach | the instrument governs no housing cost | Report v1.6, System 15, C1.3 |

*0.0 (protocol 2.1):* no structural mechanism addresses the criterion: no housing channel of any kind.

#### DE C1.3 Housing Security: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥88% housing stability over 5-year periods | not shown | housing is one of the twelve social-foundation dimensions and City Portraits track it; the one located policy output (Portland's 'From Excess to Access') is narrow; no stability rate, documented or designed, is stated, and no source the unit cites gives one | NEEC_DoughnutEconomics_scoring_scratch.md, C1.3 |
| 2 | housing costs ≤30% of disposable income at 80% of regional median household disposable income | not shown | affordability is tracked as an indicator, not set by a mechanism of the framework's own | NEEC_DoughnutEconomics_scoring_scratch.md, C1.3 |

*Flag (reading 3.6):* toward 0.0, the reading of the framework's C1.2a: no housing mechanism of its own.

*Note:* held at 0.5 on the published reading, which credits the diagnostic process and its one policy output; the reading that gave the framework's C1.2a 0.0 (no vehicle of its own) would give 0.0 here, and is flagged.

#### UBS C1.3 Housing Security: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥88% housing stability over 5-year periods | not shown | zero-rent social housing on a needs basis, 1.5 million new units; Vienna's municipal and cooperative housing, the closest analogue, is durable at population scale; no stability rate, documented or designed, is stated, and no source the unit cites gives one | NEEC_UniversalBasicServices_scoring_scratch.md, C1.3 |
| 2 | housing costs ≤30% of disposable income at 80% of regional median household disposable income | not shown | zero rent clears the clause for the households the shelter sector houses, but that design has not been implemented at the scale proposed, Vienna charges modest rents and new cooperative entrants pay an upfront sum of the order of $38,000; no cost share at 80% of the median is stated for the economy | NEEC_UniversalBasicServices_scoring_scratch.md, C1.3 |

#### SWF C1.3 Housing Security: 0.0 → 0.0

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥88% housing stability over 5-year periods | out of reach | the fund touches neither exemplar's housing market, both ordinary private mortgage-based systems; no housing allocation, land trust or tenancy protection is located | NEEC_SovereignWealthFundStatism_scoring_scratch.md, C1.3 |
| 2 | housing costs ≤30% of disposable income at 80% of regional median household disposable income | out of reach | the mechanism governs no housing cost | NEEC_SovereignWealthFundStatism_scoring_scratch.md, C1.3 |

*0.0 (protocol 2.1):* no structural mechanism addresses the criterion: no housing channel of any kind.

#### CN C1.3 Housing Security: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥88% housing stability over 5-year periods | not shown | about 12.6 million households were moved as their dwellings were demolished in 2008-2012; by 2022 more than 85% of homes were sold before completion, and mortgage boycotts spread to over 300 stalled developments; about 300 million migrant workers were historically shut out of city housing support; no 5-year stability rate is reported | NEEC_StateCapitalism_China_scoring_scratch.md, C1.3 |
| 2 | housing costs ≤30% of disposable income at 80% of regional median household disposable income | not shown | ownership is broad and lightly leveraged (about 18% of owners with a mortgage in 2022), but no housing cost share for households at 80% of the median is located, for owners or for the migrant renters | NEEC_StateCapitalism_China_scoring_scratch.md, C1.3 |

#### QA C1.3 Housing Security: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥88% housing stability over 5-year periods | not shown | for citizens housing is largely decommodified (free plots, long-term loans); for non-citizens, the large majority of residents, housing and residence depend on continuous employment with a cooperating employer, who can cancel the visa; no 5-year rate is reported for either | NEEC_StateCapitalism_Qatar_scoring_scratch.md, C1.3 |
| 2 | housing costs ≤30% of disposable income at 80% of regional median household disposable income | not shown | low-wage workers are housed by the employer or paid a housing allowance of at least QAR 500 a month; no housing cost share at 80% of the median is located | NEEC_StateCapitalism_Qatar_scoring_scratch.md, C1.3 |

*Note:* the citizens-only scenario (1.0) stays a scenario (protocol 3.2).

#### IF C1.3 Housing Security: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥88% housing stability over 5-year periods | not shown | diminishing partnership (musharakah mutanaqisah) is a real housing product: the financier bears ownership risk and a markup price cannot grow after default; allocation remains market-based and no stability rate, documented or designed, is stated, and no source the unit cites gives one | NEEC_IslamicFinance_scoring_scratch.md, C1.3 |
| 2 | housing costs ≤30% of disposable income at 80% of regional median household disposable income | not shown | profit rates are competitive with conventional mortgages, not below them; no affordability floor, and no cost share at 80% of the median is stated | NEEC_IslamicFinance_scoring_scratch.md, C1.3 |

#### OS C1.3 Housing Security: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥88% housing stability over 5-year periods | not shown | community land trusts are the commons' housing form (counted in, decision D31, with a scenario counting them out); no 5-year stability series for commons-governed housing was retrieved | NEEC_Ostrom_Commons_scoring_scratch.md, C1.3; SCORING_PROTOCOL.md 3.2 |
| 2 | housing costs ≤30% of disposable income at 80% of regional median household disposable income | not shown | nothing in the mechanism targets households at 80% of the median; no cost share is stated | NEEC_Ostrom_Commons_scoring_scratch.md, C1.3 |

*Note:* the scope scenario counting community land trusts out (0.0) stands.

## 5. The simulation runs (from `cco_c13_checks_s54_output.txt`)

`node cco_c13_checks_s54.js` on `harness.js` (md5 `fe6fa4a3`) and `index.html` (md5 `c333b632`) at `5a7a7b1`; 500
seeds, 500 agents, 20 years. The runner reproduces `runScenario()`'s year-20 housing distress, median wealth and wealth
poverty on every seed of the four scenarios before any figure is read. An agent passes a 5-year window when it has no
year of housing distress in it.

| Scenario | Agents | Years 1-5 | Years 6-10 | Years 11-15 | Years 16-20 | Lowest window | Seeds at 88% or more, years 16-20 |
|---|---|---:|---:|---:|---:|---:|---:|
| Reference (Full Integration), 0% | all | 80.1% | 78.5% | 81.8% | 86.4% | 78.5% | 83 of 500 |
| Reference (Full Integration), 0% | in PTH | 93.9% | 93.6% | 95.2% | 96.8% | 93.6% | 500 of 500 |
| Reference (Full Integration), 0% | outside PTH | 76.7% | 74.7% | 78.4% | 83.7% | 74.7% | 1 of 500 |
| Baseline, matched (0%) | all | 57.8% | 51.5% | 50.4% | 51.1% | 50.4% | 0 of 500 |
| Adverse Environment, 2% | all | 77.6% | 72.4% | 68.4% | 63.5% | 63.5% | 0 of 500 |
| Adverse Environment, 2% | in PTH | 92.7% | 90.1% | 88.0% | 84.9% | 84.9% | 95 of 500 |
| Adverse Environment, 2% | outside PTH | 73.8% | 68.0% | 63.4% | 58.1% | 58.1% | 0 of 500 |
| Baseline, matched to Adverse (2%) | all | 53.8% | 41.8% | 32.0% | 23.2% | 23.2% | 0 of 500 |

In the reference run the share of agents in distress rises from 6.9% in year 1 to 19.3% in years 6 and 7 and falls to
9.6% in year 20 (the capture's last note).

## 6. What parts (a), (b) and groups 2.1 to 2.3 change (generated)

| Entry | Published (rank) | After group 2.2 (rank) | After group 2.3 (rank) | Change here | Failures | Tier |
|---|---:|---:|---:|---:|---:|---|
| CCO | 24.5 (1) | 15.0 (1) | 14.5 (1) | -0.5 | 0 | Potentially Adequate |
| PE | 20.5 (2) | 14.5 (2) | 14.0 (2) | -0.5 | 1 | Potentially Adequate |
| NSD | 19.5 (3) | 13.0 (5) | 13.0 (4) | 0.0 | 2 | Potentially Adequate |
| INT | 19.5 (3) | 14.5 (2) | 14.0 (2) | -0.5 | 3 | Partially Adequate |
| DG | 19.0 (5) | 13.5 (4) | 13.0 (4) | -0.5 | 2 | Potentially Adequate |
| MS | 16.5 (6) | 13.0 (5) | 13.0 (4) | 0.0 | 2 | Potentially Adequate |
| MMT | 15.5 (7) | 11.0 (14) | 11.0 (14) | 0.0 | 4 | Partially Adequate |
| UBI | 14.5 (8) | 11.0 (14) | 11.0 (14) | 0.0 | 7 | Structurally Inadequate |
| MC | 14.5 (8) | 12.5 (8) | 12.5 (8) | 0.0 | 3 | Partially Adequate |
| OS | 14.5 (8) | 13.0 (5) | 13.0 (4) | 0.0 | 3 | Partially Adequate |
| SWF | 14.0 (11) | 12.5 (8) | 12.5 (8) | 0.0 | 3 | Partially Adequate |
| SG | 14.0 (11) | 11.5 (12) | 11.5 (12) | 0.0 | 4 | Partially Adequate |
| GEO | 13.5 (13) | 12.5 (8) | 12.5 (8) | 0.0 | 2 | Potentially Adequate |
| UBS | 13.5 (13) | 12.0 (11) | 12.0 (11) | 0.0 | 3 | Partially Adequate |
| IF | 13.5 (13) | 11.5 (12) | 11.5 (12) | 0.0 | 5 | Partially Adequate |
| FALC | 13.0 (16) | 9.5 (16) | 9.0 (18) | -0.5 | 10 | Structurally Inadequate |
| DE | 11.5 (17) | 9.0 (19) | 9.0 (18) | 0.0 | 8 | Structurally Inadequate |
| SQ | 10.5 (18) | 9.5 (16) | 9.5 (16) | 0.0 | 9 | Structurally Inadequate |
| CPS | 10.0 (19) | 7.5 (22) | 7.5 (22) | 0.0 | 12 | Structurally Inadequate |
| SC | 10.0 (19) | 8.5 (20) | 8.5 (20) | 0.0 | 9 | Structurally Inadequate |
| CN | 10.0 (19) | 9.5 (16) | 9.5 (16) | 0.0 | 8 | Structurally Inadequate |
| QA | 9.0 (22) | 8.0 (21) | 8.0 (21) | 0.0 | 10 | Structurally Inadequate |
| LM | 8.0 (23) | 6.5 (23) | 6.5 (23) | 0.0 | 14 | Structurally Inadequate |

After this group the corpus has 18 dominance pairs against 20 after group 2.2 (new: none; lost: CCO>CPS, INT>CPS), and its frontier holds 15 entries against 14 (SQ, NSD, CPS, MS, LM, UBI, DG, FALC, PE, CCO, INT, MC, SWF, IF, OS). First place: CCO, 15.0 after group 2.2, 14.5 now, ahead of PE, INT at 14.0. Across the pass so far 195 units have been re-estimated, each counted once: 17 are at 1.0, 165 at 0.5 and 13 at 0.0; against their published scores 146 fell, 1 rose and 48 are unchanged (net -72.5 points).

| Entry | Published | (a) | (b1) | (b2) | (b3) | (b4) | (b5) | (b6) | (b7) | 48.3 | (b8) | (b9) | (2.1) | (2.2) | (2.3) | Now | Re-estimated | At 0.5 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| CCO | 24.5 | -0.5 | -1.5 | -0.5 | -0.5 | -0.5 | -0.5 | -1.0 | -0.5 | -0.5 | -0.5 | -1.0 | -1.5 | -0.5 | -0.5 | 14.5 | 22 | 20 |
| PE | 20.5 |  | -1.5 | -0.5 | -0.5 | -1.5 |  | -0.5 | -0.5 |  | -0.5 | -0.5 |  |  | -0.5 | 14.0 | 15 | 14 |
| NSD | 19.5 | -2.5 | -1.0 | -0.5 | -0.5 | -0.5 |  |  |  |  | -0.5 | -0.5 |  | -0.5 |  | 13.0 | 14 | 13 |
| INT | 19.5 | -0.5 | -1.0 | -0.5 |  | -1.0 | -0.5 | -1.0 | -0.5 |  |  |  |  |  | -0.5 | 14.0 | 14 | 11 |
| DG | 19.0 |  | -1.5 | -0.5 | -0.5 | -0.5 |  | -0.5 | -1.0 |  | -1.0 |  |  |  | -0.5 | 13.0 | 13 | 13 |
| MS | 16.5 | -1.0 | -1.5 | -0.5 | -0.5 |  |  |  | 0.5 |  |  |  |  | -0.5 |  | 13.0 | 10 | 8 |
| MMT | 15.5 | -1.5 | -1.0 | -0.5 | -0.5 |  |  |  |  |  | -0.5 |  |  | -0.5 |  | 11.0 | 9 | 8 |
| UBI | 14.5 | -1.5 | -0.5 | -0.5 | -0.5 |  |  |  |  |  | -0.5 |  |  |  |  | 11.0 | 10 | 8 |
| MC | 14.5 |  | -1.0 | -0.5 |  |  | -0.5 |  |  |  |  |  |  |  |  | 12.5 | 7 | 4 |
| OS | 14.5 | -0.5 |  |  |  |  | -0.5 | -0.5 |  |  |  |  |  |  |  | 13.0 | 6 | 4 |
| SWF | 14.0 |  |  | -0.5 |  |  | -0.5 | -0.5 |  |  |  |  |  |  |  | 12.5 | 6 | 4 |
| SG | 14.0 | -1.0 | -0.5 | -0.5 |  |  |  |  |  |  |  |  |  | -0.5 |  | 11.5 | 5 | 5 |
| GEO | 13.5 | -0.5 |  |  |  |  | -0.5 |  |  |  |  |  |  |  |  | 12.5 | 4 | 3 |
| UBS | 13.5 |  | -0.5 | -0.5 |  |  | -0.5 |  |  |  |  |  |  |  |  | 12.0 | 6 | 4 |
| IF | 13.5 | -1.0 |  |  |  |  | -0.5 |  |  |  |  | -0.5 |  |  |  | 11.5 | 6 | 6 |
| FALC | 13.0 | -0.5 | -0.5 |  | -0.5 | -1.0 |  | -0.5 | -0.5 |  |  |  |  |  | -0.5 | 9.0 | 10 | 8 |
| DE | 11.5 | -0.5 | -0.5 |  |  |  | -0.5 | -0.5 | -0.5 |  |  |  |  |  |  | 9.0 | 7 | 6 |
| SQ | 10.5 | -0.5 |  |  |  | -0.5 |  |  |  |  |  |  |  |  |  | 9.5 | 5 | 4 |
| CPS | 10.0 | -1.5 |  |  | -0.5 |  |  |  |  |  | -0.5 |  |  |  |  | 7.5 | 7 | 5 |
| SC | 10.0 |  | -1.0 |  |  |  |  |  |  |  |  | -0.5 |  |  |  | 8.5 | 5 | 5 |
| CN | 10.0 |  |  | -0.5 |  |  |  |  |  |  |  |  |  |  |  | 9.5 | 3 | 3 |
| QA | 9.0 | -0.5 |  | -0.5 |  |  |  |  |  |  |  |  |  |  |  | 8.0 | 4 | 4 |
| LM | 8.0 | -1.5 |  |  |  |  |  |  |  |  |  | -0.5 |  | 0.5 |  | 6.5 | 7 | 5 |

Anchor examples citing a unit the pass moves: C1.1's 1.0 example, NSD (part (b3)); C1.2a's 1.0 example, MS (part (2.2)); C1.2b's 1.0 example, CCO (part (2.1)); C1.4's 1.0 example, CCO (part (2.1)); C2.1's 1.0 example, UBI (part (a)); C2.3's 1.0 example, DG (part (b1)); C2.4's 1.0 example, PE (part (b1)); C2.5's 1.0 example, CCO (part (b5)); C3.1's 1.0 example, UBI (part (b2)); C3.2's 1.0 example, PE (part (b4)); C3.5's 1.0 example, CCO (part (b6)); C4.1's 1.0 example, DG (part (b6)); C4.2's 1.0 example, PE (part (b7)); C4.3's 1.0 example, CCO (part (b8)); C5.1's 1.0 example, MS (part (b2)); C5.2's 1.0 example, CCO (part (b9)); C5.4's 1.0 example, CCO (part (b9)); C5.5's 1.0 example, PE (part (b9)). Bands whose example the pass moves and which no corpus unit then scores at their value: C1.1's 1.0, C1.2a's 1.0, C2.1's 1.0, C2.3's 1.0, C2.4's 1.0, C3.1's 1.0, C3.5's 1.0, C4.1's 1.0, C4.2's 1.0, C4.3's 1.0.

C1.3's three anchor examples (Centrally Planned Socialism at 1.0, Universal Basic Income at 0.5, Libertarian Minarchism
at 0.0) all hold, so the anchors line is unchanged by this group.

## 7. Corrections found (not polish)

1. **Status Quo's C1.3 rationale** gives "72% stability over 5 years" for market-rate rental with no source; Report
   v2.0 gives the sourced figures of reading 3.5.
2. **CCO-PTF-CIP-SZH's C1.3 rationale** states the papers' 94% and 60% as the system's figures; the design's published
   model produces neither, and gives the 94% only to Public Trust Housing residents, a fifth of agents (reading 3.3).
   Report v2.0 gives the model's figures and the population they cover.
3. **Four design rationales** (Degrowth, Fully Automated Luxury Communism, Participatory Economics, Integral) score 1.0
   on descriptions; Report v2.0 states that neither clause is estimated (reading 3.2).

No score is corrected outside the D28 form: the five falls are the rule applied, and no published 0.5 or 0.0 is found
inconsistent with its peers' reading.

## 8. Notes for the simulation's maintainers (the owner's project; not NEEC corrections)

- The engine models no housing tenure and no housing-cost line, so C1.3's two quantities cannot be read from it. A
  tenure state (Public Trust Housing, market rent, ownership), a rent or housing-cost line within the basket and a
  displacement event would let the model report both clauses.
- Public Trust Housing's uptake is a fixed 20% of agents; the papers' 94% matches the model's figure for that fifth.
  The share of all agents is the figure the criterion reads.

## 9. Disclosure

CCO-PTF-CIP-SZH is the owner's design. It falls from 1.0 to 0.5 here on a reading of its own published model. Four other
designs fall on the same rule (silence is not clearance), so the design keeps first place, at 14.5 on the 26 published
criteria, ahead of Participatory Economics and Integral at 14.0. The reading of the clauses (3.1) and the runner's measure were
settled before the runner's figures were computed; the decision to read the proxy as not shown rather than short (3.3)
was taken after, and it is the reading less unfavourable to the design; neither changes the verdict. The runner's
table shows that the design's own housing mechanism, where it reaches, performs at the papers' figure. The only unit that holds 1.0 belongs
to a system the corpus ranks 22nd of 23 and that fails twelve criteria; its flag records the limits of its record.

## 10. What remains

- **Next group from the triage** (rerun after this group, `triage_s52_output.txt`): C3.5 Failure-Mode Transparency, the
  first class I group, after the evidence cache (W5).
- **For the criteria record's next amendment:** decisions 54.1 to 54.3, with 53.1 to 53.3, 52.11 and 52.12, in one run
  of the chain.
- **For Report v2.0:** section 7's corrections; the clause 1 readings of Nordic Social Democracy and Singapore
  (reading 3.5).

## 11. What this record does not show

No national survey in reach reports C1.3's 5-year stability rate, and US cost burdens are measured on pre-tax income;
the Soviet figures come from a secondary study and a census share quoted by the publisher, and the bound derived from
them covers the system's mature form only. "Not shown" means that no evidence was located, not that the clause fails;
most units here are 0.5 for that reason, and better data could raise some; Qatar's citizens-only reading stays a scenario. The model's figures are the model's: 500 single-adult agents, prices an input, no housing
tenure, and a distress proxy this record does not treat as displacement. The interpretation check (decisions 50.1 to
50.4) was not run; it is optional. The record is one scorer's re-estimation; whether its calls reproduce is what the
replication programme tests.
