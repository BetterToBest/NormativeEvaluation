# NEEC Rescoring Pass — Record, Stage 2, Group 2.8: C4.3 Group Equity (class M)

**Session 61 · 2026-10-15 · Scorer and engineer: Claude · Owner: Duke Johnson**
**Status: scratch (protocol 10.1). Parts (a) and (b), groups 2.1 to 2.7 and part 58.1 are `NEEC_Rescoring_s37.md` to
`NEEC_Rescoring_s60.md` and `owner_s58.py`; this record edits none of them.** No corpus file, score or scoring document
changes until the pass ends. Its changes are then applied by generator with pinned inputs and restated in place
(protocol 10.2, 10.3; decisions D12, D14), and until then the published totals stand, provisional as `README.md` says.
Decisions taken here are Claude's under the owner's delegation (Handoff 35, section 2; decision 57.2: only
CCO-PTF-CIP-SZH's score changes wait on the owner, and none is made here); each is recorded with its reasons, and the
owner may reverse any of them.
**Reproduce:** `python3 rescoring_s61.py` (harness check 108). It is written on the shared module (`pass_common.py`,
decision 52.5): the script holds the 16 readings and the group's own checks, and the module computes the consequences
cumulatively with every part before it. It checks the three files this group added to the evidence cache
(`evidence_cache/C4.3/`) by digest, finds every passage quoted in its file, recomputes from them every gap the readings
quote, locates each unit's published rationale, and checks that this record contains its generated tables verbatim. It
reads no network.

---

## 1. What this group is

The consequence triage (`triage_s52.py`, decision 52.7), rerun after group 2.7, put C4.3 first among the criteria still
to read: 16 units in play, four of them able to change an adequacy tier on their own (Integral, Market Socialism,
Georgism, Islamic Finance), and Integral's able to change who is first. C4.3 is class M: v2.0 keeps two of its clauses
word for word ("Disparity reduction ≥5 percentage points every 5 years", "convergence trajectory toward <20% disparities
within 30 years"), places them under the scope "on each declared axis, non-citizen residents included", and names the
measure: the gap between the median household incomes, and wealth where published, of the least and most advantaged
groups on each declared axis, as a percentage of the most advantaged group's median, from national household surveys
(`criteria.json`; `NEEC_Criteria_v2_s45.md`). Part (b8) (`NEEC_Rescoring_s49.md`) read the seven published 1.0s, each to
0.5, and set the readings this group applies: an A code on a restated clause is read again (its 3.2); a design or a
mechanism shows a clause only by a projection of the gap on the measure (its 3.3); a configured national economy is read
on its national household survey (its 3.4 and 3.5). This group reads the other 16: thirteen 0.5s and three 0.0s, the
four configured national economies (Status Quo, China, Singapore, Qatar) on their surveys, as `NEEC_Rescoring_s51.md`,
section 11, planned.

**Outcome.** No unit shows either clause, so none is 1.0, and C4.3 stays among the criteria no scored system clears.
**One unit falls**, Status Quo, from 0.5 to 0.0, a correction: on the measure the gap between the least and most
advantaged groups on its declared axis is above 50% and wider than in 2002, and the Black-white gap has stayed between
35% and 45% for 53 years (reading 3.3). Fifteen hold, three of them at 0.0 (Libertarian Minarchism, China, Qatar).
Singapore's two clauses are short on its 2025 household survey, where the Malay gap widened; it holds at 0.5 on a
group-directed mechanism in force (reading 3.4). **Integral holds at 0.5** on the design's own white paper (reading 3.7),
so first place stays shared by CCO-PTF-CIP-SZH and Integral at 14.5. Net −0.5 points; Status Quo gains a failure (nine to
ten) and no tier changes. Nine units are flagged; two of the flags, published ones kept here (Georgism and Islamic
Finance toward 0.0), could each change a tier.

## 2. How a clause is recorded, and the rule

As in groups 2.2 to 2.7 and decision 53.2: each clause is cleared, short, not shown, out of reach or moot. A unit is 1.0
only if every clause is cleared (D28, protocol 2.3); 0.0 only on one of protocol 2.1's whole-criterion conditions, stated
as the unit's reason and never with a clause cleared; 0.5 otherwise. A clause-level gap never makes 0.0 (D28(f)). "Not
shown" means that no estimate of the clause's quantity was located, not that the clause fails; "short" means the
evidence located falls below it. Both clauses must hold on each declared axis, so one axis short makes the clause short.
For a mechanism, the host economy's gaps are not credited to it (protocol 3.2).

## 3. Decisions and readings (under the delegation)

**3.1 What the clauses ask.** As part (b8) read them: a rate (the fall in each gap, in points per five years) and a
trajectory (whether the trend reaches 20% within 30 years), on the measure v2.0 names, on each axis the entry declares
or its own text names (part (b8), reading 3.4(1)). A configured national economy is read on its household survey, by
the two measures of the rate part (b8) used for Nordic Social Democracy where a series allows (the change between the
three-year means of 2018–2020 and 2023–2025, and the least-squares trend over the ten editions 2016–2025, per five
years); a design or a mechanism by a projection of the gap from a model or calibrated components (part (b8), reading
3.3). No such projection exists for any of the twelve designs and mechanisms read here.

**3.2 0.0 and 0.5 on C4.3 (decision 61.1, a method choice).** (1) *The question.* A class M re-read may lower a 0.5 or
raise a 0.0 (decision 53.2), so the line between them must be drawn the same way for every unit. C4.3's band texts
overlap: the 0.5 band names "formal equality without reparative mechanisms", the 0.0 band "formally neutral policy in a
context of large documented disparities, with no active correction". (2) *Interpretations.* (a) Any formal equality is
0.5; (b) formal neutrality is 0.0 wherever disparities exist; (c) protocol 2.1's three conditions, read on C4.3's measure.
(3) *Preponderance:* (c). The band texts describe and protocol 2.1 governs (protocol 2.3(g)). Read on C4.3, its
conditions are: *no structural mechanism addresses the criterion* — nothing in the system bears on a gap between
groups, neither a group-directed measure (a quota, a targeted benefit, an enforced anti-discrimination rule, a
monitoring rule that amends allocations) nor a flow whose form narrows percentage gaps (a universal flat transfer or
provision, an income floor, care work remunerated); *the system excludes the concern* — its own logic rules out
correction, or it allocates rights and benefits to the most advantaged group; *far below the threshold with no credible
pathway* — on the measure, over a long series, a gap far above 20% that does not narrow, with nothing in the system's
own logic that would close it. A unit meeting none is 0.5: a genuine mechanism, or for a design not deployed, formal
equality with no context of its own in which disparities are documented. Reading (a) would hold Status Quo at 0.5 on
its anti-discrimination law against its own measured record; reading (b) would lower every formally neutral mechanism,
Islamic Finance's among them, on disparities not measured on C4.3's measure. (4) *Applied:* in readings 3.3 to 3.7.

**3.3 Status Quo, 0.5 → 0.0 (decision 61.2, a correction).** (1) *The axis.* The entry's text declares race, citing the
Black-white wealth gap, and gender. The Census Bureau's Current Population Survey publishes median household income by
race and Hispanic origin of householder every year (Table H-5; section 5). On that axis the least advantaged group is
Black households and the most advantaged Asian households, whose median exceeds the white non-Hispanic median in every
year from 2002 to 2025. (2) *The rate.* The gap between Black and Asian households is 52.1% in 2023–2025 against 52.6% in
2018–2020 (−0.5), with a ten-edition trend of +0.2 points per five years; it was 44.8% in 2002 and is 52.5% in 2025. The
gap the entry's own text draws, Black against white non-Hispanic households, is 37.9% against 40.2% (−2.3), trend −2.3;
both measures fall short of 5 points on both comparisons. (3) *The trajectory.* The Black-white non-Hispanic gap has stayed
between 34.8% and 44.7% in all 53 editions since 1972 (42.5% in 1972, 38.0% in 2025); the Black-Asian gap has widened.
Neither reaches 20% within 30 years at its long-run rate. Wealth, which the measure adds where published, was not read:
income decides both clauses. (4) *The 0.0 condition.* Performance on the measure is far below the threshold, a rate near
zero against 5 points and a gap above 50% against 20%, and the system shows no credible pathway under its own logic: its
correction is formal anti-discrimination law, in force since 1964, under which the gap has not left its band, and its
group-directed remedies are being withdrawn (race-conscious admissions ended by *Students for Fair Admissions v.
Harvard*, 2023; federal contractors' affirmative action, Executive Order 11246, revoked by Executive Order 14173 in
January 2025). (5) *Why this is a correction.* The published 0.5 rests on "some progress over decades"; on the measure
v2.0 names there is none on the Black-white comparison since 2002 and a widening on the least-to-most comparison. It
also resolves the inconsistency logged since Handoff 30 (item 4): the 0.0 band's example, Status Quo, was published at
0.5. *Flag:* toward 0.5, counting anti-discrimination law as a correction of partial reach and the Hispanic gap against
white non-Hispanic households, which narrows about 2 points in five years (26.6% to 24.5% on the three-year means).
*Consequence:* Status Quo's total falls from 9.5 to 9.0 on the published structure and its failures from nine to ten; it
stays Structurally Inadequate.

**3.4 Singapore holds at 0.5, its clauses short.** (1) *The source.* The General Household Survey 2025 (June 2026),
Table 6.1, gives the median monthly household market income of resident households by the ethnic group of the household
reference person, for 2020 and 2025 (section 5). (2) *The clauses.* Malay households have the lowest median and Indian
households the highest; the gap is 35.9% in 2025 against 32.1% in 2020. Per household member, against Chinese
households, it is 43.6% against 41.7%. The gap widened, so clause 1 is short; a gap widening over the one interval the
survey gives is not on a trajectory, and the decade before (the census, 2010 to 2020) saw Malay per-member incomes grow
fastest, so the two intervals point opposite ways and clause 2 is short. (3) *Why not 0.0.* The system has a
group-directed mechanism in force: the Tertiary Tuition Fee Subsidy for Malays, government-funded and means-tested since
1991, which the Ministry of Education described in May 2026 as complementing the national schemes for Malay students
from lower- and middle-income households; and its first anti-discrimination statute, the Workplace Fairness Act, from
2025. The record is mixed over 15 years, not a long series that does not narrow. Status Quo's measured record is 53
editions with its group-directed remedies being withdrawn; Singapore's is two intervals with a group-directed remedy in
force. *Flag:* the published flag toward 0.0 is kept, now on the measure. Wider resident and non-resident gaps (the
two-tier labour regime) are outside the survey, which covers residents; the entry's C4.5 reads them.

**3.5 China and Qatar hold at 0.0.** *China.* No national household survey publishes median household income by ethnic
group: the National Bureau of Statistics publishes by urban and rural residence and by region. Neither clause can be
measured on the ethnic axis, as part (b8) found for the Soviet-type record (its reading 3.5). The 0.0 holds on the
published reason, now stated as protocol 2.1's second condition: state coercion targeting the minorities most affected,
which the UN human rights office found may constitute crimes against humanity, and an assimilationist ethnic law of
2026, a harm beyond the formal neutrality of the 0.0 band. The published flag's 0.5 side (the preferential policies) is
kept; its 1.0 side, on the Centrally Planned Socialism precedent, lapses, since that unit fell to 0.5 in part (b8).
*Qatar.* The Planning and Statistics Authority's 2012/13 household survey, as the press reported it, gives average
monthly household income of QR 72,700 for Qatari and QR 24,400 for non-Qatari households, a gap of 66.4% on means, with
workers in collective housing outside the survey; one survey gives no rate, and the 2017/18 survey was not read (the
authority's site did not answer the container). The 0.0 holds on protocol 2.1's second condition: rights and rent-funded
benefits are allocated by nationality to the most advantaged legal group, and v2.0's scope counts the non-citizen
residents, most of the population, whom the allocation excludes.

**3.6 The designs and mechanisms (decision 61.3).** Twelve units are designs or mechanisms; none has a projection of the
gap, so both clauses are not shown in each (part (b8), reading 3.3). Libertarian Minarchism holds at 0.0: its own logic
confines the state to protecting rights and rules out any corrective flow (protocol 2.1, the second condition). The
other eleven hold at 0.5, each on a mechanism that bears on a gap (reading 3.2): Market Socialism (democratic governance
and pay compression), Stakeholder Capitalism (group-directed diversity programmes), Fully Automated Luxury Communism
(universal abundance), Georgism (a flat Citizen's Dividend), Mutual Credit (care work valued), Doughnut Economics (gender
equality a dimension of the social foundation), Universal Basic Services (universal provision without means-testing),
Sovereign Wealth Fund Statism (a flat dividend), Ostrom-style commons (quotas inside the mechanism, collective tenure),
Islamic Finance (formal equality of contract terms; see below) and Integral (reading 3.7). *Flags.* A published flag's
1.0 side lapses wherever it stood (Georgism, Mutual Credit, Sovereign Wealth Fund Statism, Universal Basic Services):
1.0 now needs a projection on each declared axis, which no source gives. Universal Basic Services' flag pointed only to
1.0, so it carries none now. The published 0.0 sides are kept: Georgism (assessment bias), Mutual Credit (participation
gap), Sovereign Wealth Fund Statism (a persistent Native gap), Islamic Finance and Ostrom-style commons. Stakeholder
Capitalism is flagged now, toward 0.0: it operates in the economy whose gap reading 3.3 finds far below the bar, and
corporate diversity programmes have been withdrawn widely since 2024. *Islamic Finance* (tier-capable): the scored object
is the contract set, whose terms are the same whoever signs, the 0.5 band's "formal equality without reparative
mechanisms"; the documented gaps are in women's uptake of Islamic microfinance and wealth management in Malaysia, which
are participation, not the measure, and inheritance rules lie outside the scope the owner confirmed (Session 22, D5).
The 0.0 condition is not met on the measure, so the unit holds; its published flag is kept, and it alone could move the
entry to Structurally Inadequate. *Market Socialism* (tier-capable) carries no flag: its mechanism is genuine and its
reach unclear, the 0.5 band's second description.

**3.7 Integral holds at 0.5 on its white paper (decision 61.4).** The published 0.5 is the band's example: democratic
architecture prevents new privilege but "no explicit reparative mechanisms are discussed". The white paper (v0.1,
December 2025), which groups 2.6 and 2.7 read, adds a group-directed monitoring mechanism: the contribution system is
checked so that "no person or demographic group is structurally disadvantaged", its rules carry "protected-category
adjustments", the deliberation system's analysis has a fairness layer of "distributional effects", and a review module
amends a decision when "access inequity" is detected (section 5). It also says that "equity is not enforced through
redistribution", it states no rule addressing a historical disparity, and the design's income is non-monetary
contribution credit, so no gap on the measure is projected. Neither clause is shown; the mechanism keeps the unit off
0.0. The white paper was read on these passages before the consequences were computed; Integral's C4.3 could have
decided who is first, and it does not.

**3.8 What the group does not decide (decision 61.5, a method choice).** The gender axis, which several rationales
name, is not read on a national survey for any unit: household income by the householder's sex compares household
types (lone mothers against lone fathers, for instance) rather than women and men, and for each unit read here another
axis decides the clause or no survey exists. Wealth gaps are not read for the same reason: income decides each clause
read. Report v2.0 states both.

## 4. The units

### 4.1 Summary (generated)

| Entry | Published | Rate | Convergence | Verdict | Flag |
|---|---:|---|---|---:|---|
| SQ | 0.5 | short | short | 0.0 | toward 0.5 |
| MS | 0.5 | not shown | not shown | 0.5 |  |
| LM | 0.0 | not shown | not shown | 0.0 |  |
| SC | 0.5 | not shown | not shown | 0.5 | toward 0.0 |
| FALC | 0.5 | not shown | not shown | 0.5 |  |
| INT | 0.5 | not shown | not shown | 0.5 |  |
| GEO | 0.5 | not shown | not shown | 0.5 | toward 0.0 |
| MC | 0.5 | not shown | not shown | 0.5 | toward 0.0 |
| DE | 0.5 | not shown | not shown | 0.5 |  |
| UBS | 0.5 | not shown | not shown | 0.5 |  |
| SWF | 0.5 | not shown | not shown | 0.5 | toward 0.0 |
| CN | 0.0 | not shown | not shown | 0.0 | toward 0.5 |
| SG | 0.5 | short | short | 0.5 | toward 0.0 |
| QA | 0.0 | not shown | not shown | 0.0 |  |
| IF | 0.5 | not shown | not shown | 0.5 | toward 0.0 |
| OS | 0.5 | not shown | not shown | 0.5 | toward 0.0 |

### 4.2 Clause by clause (generated)

#### SQ C4.3 Group Equity: 0.5 → 0.0

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Disparity reduction ≥5 percentage points every 5 years | short | on the race and Hispanic origin axis the entry's text declares, the least advantaged group is Black households and the most advantaged Asian households, whose median exceeds the white non-Hispanic median in every year 2002-2025; the gap is 52.1% in 2023-2025 against 52.6% in 2018-2020 (-0.5), trend +0.2 per five years over the ten editions, and 52.5% in 2025 against 44.8% in 2002; the gap against white non-Hispanic households, the comparison the entry's own text draws, is 37.9% against 40.2% (-2.3), trend -2.3 (reading 3.3) | U.S. Census Bureau, CPS ASEC, Table H-5, median household income by race and Hispanic origin of householder, 1967 to 2025 (xlsx md5 9086455a, retrieved 2026-10-15; evidence_cache/C4.3/us_census_h05_extract.txt); Report v1.6, SQ C4.3 |
| 2 | convergence trajectory toward <20% disparities within 30 years | short | no trajectory toward 20%: the Black-white non-Hispanic gap has stayed between 34.8% and 44.7% in all 53 editions since 1972 (42.5% in 1972, 38.0% in 2025), and the Black-Asian gap widened by 7.7 points from 2002 to 2025; at the long-run rate the 20% level is not reached within 30 years on either comparison (reading 3.3) | U.S. Census Bureau, CPS ASEC, Table H-5, median household income by race and Hispanic origin of householder, 1967 to 2025 (xlsx md5 9086455a, retrieved 2026-10-15; evidence_cache/C4.3/us_census_h05_extract.txt); Executive Order 14173 of 21 January 2025, revoking Executive Order 11246 (federal contractors' affirmative action); Students for Fair Admissions v. Harvard, 600 U.S. 181 (2023) |

*0.0 (protocol 2.1):* the best evidence shows performance far below the threshold with no credible pathway under the system's own logic (protocol 2.1): on the measure v2.0 names the gap between the least and most advantaged groups is above 50% and wider than in 2002, the Black-white gap has not left the band of 35% to 45% in 53 years, and the system's group-directed remedies are being withdrawn (race-conscious admissions in 2023, federal contractors' affirmative action in 2025); the 0.0 band's own example.

*Flag (reading 3.3):* toward 0.5: counting anti-discrimination law as a correction with partial reach, and the Hispanic gap against white non-Hispanic households, which narrows about 2 points in five years from 29% to 24%, as the axis on which the system shows some movement.

*Note:* a correction (reading 3.3): the published 0.5 rests on 'some progress over decades', which the measure does not show; it resolves the inconsistency logged since Handoff 30, the 0.0 band's example published at 0.5.

#### MS C4.3 Group Equity: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Disparity reduction ≥5 percentage points every 5 years | not shown | the cooperative structure's equity effects are mixed by the entry's own account (some cooperatives prioritise equity, others replicate societal biases); pay compression within a firm bears on gaps between groups but is not a projection of them; no projection of the gap between groups' median household incomes on any axis, from a model or calibrated components, is stated or located, so neither the rate nor the convergence is shown (part (b8), reading 3.3) | Report v1.6, MS C4.3 |
| 2 | convergence trajectory toward <20% disparities within 30 years | not shown | as for clause 1: no projection of the gap's path is stated or located (part (b8), reading 3.3) | Report v1.6, MS C4.3 |

*Note:* 0.5 holds: a genuine mechanism (democratic governance and pay compression) with unclear reach, the 0.5 band's second description (reading 3.2).

#### LM C4.3 Group Equity: 0.0 → 0.0

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Disparity reduction ≥5 percentage points every 5 years | not shown | formal equality before the law only: the minimal state's functions exclude any corrective measure, and no mechanism bears on a gap between groups; no projection of the gap between groups' median household incomes on any axis, from a model or calibrated components, is stated or located, so neither the rate nor the convergence is shown (part (b8), reading 3.3) | Report v1.6, LM C4.3 |
| 2 | convergence trajectory toward <20% disparities within 30 years | not shown | as for clause 1: no projection of the gap's path is stated or located (part (b8), reading 3.3) | Report v1.6, LM C4.3 |

*0.0 (protocol 2.1):* the system excludes the criterion's concern (protocol 2.1): its own logic confines the state to protecting rights and rules out any corrective flow, so historical disparities persist unchallenged, as its rationale says.

#### SC C4.3 Group Equity: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Disparity reduction ≥5 percentage points every 5 years | not shown | diversity initiatives and hiring targets are group-directed but address representation, not household income gaps, and the host economy's gaps are not credited to the mechanism (protocol 3.2); no projection of the gap between groups' median household incomes on any axis, from a model or calibrated components, is stated or located, so neither the rate nor the convergence is shown (part (b8), reading 3.3) | Report v1.6, SC C4.3 |
| 2 | convergence trajectory toward <20% disparities within 30 years | not shown | as for clause 1: no projection of the gap's path is stated or located (part (b8), reading 3.3) | Report v1.6, SC C4.3 |

*Flag (reading 3.6):* toward 0.0: the mechanism operates in the economy whose gap reading 3.3 finds far below the bar, and corporate diversity programmes have been withdrawn widely since 2024, so its correction may lack a credible pathway.

*Note:* 0.5 holds: a group-directed mechanism of partial reach (reading 3.2); flagged now.

#### FALC C4.3 Group Equity: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Disparity reduction ≥5 percentage points every 5 years | not shown | universal abundance narrows material gaps by its form, but governance and historical inequities are unaddressed by the entry's account; no projection of the gap between groups' median household incomes on any axis, from a model or calibrated components, is stated or located, so neither the rate nor the convergence is shown (part (b8), reading 3.3) | Report v1.6, FALC C4.3 |
| 2 | convergence trajectory toward <20% disparities within 30 years | not shown | as for clause 1: no projection of the gap's path is stated or located (part (b8), reading 3.3) | Report v1.6, FALC C4.3 |

*Note:* 0.5 holds (reading 3.2).

#### INT C4.3 Group Equity: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Disparity reduction ≥5 percentage points every 5 years | not shown | the white paper, published after the corpus scored the design, adds what the review's document lacked: the contribution system is checked so that 'no person or demographic group is structurally disadvantaged', its rules carry 'protected-category adjustments', the deliberation system's analysis has a fairness layer of distributional effects, and detected access inequity amends a decision; but 'equity is not enforced through redistribution', no rule addresses a historical disparity, and the design's income is non-monetary contribution credit; no projection of the gap between groups' median household incomes on any axis, from a model or calibrated components, is stated or located, so neither the rate nor the convergence is shown (part (b8), reading 3.3) | Joseph, INTEGRAL: Technical White Paper v0.1 (December 2025; PDF md5 a6defc9a), section 4.3, the contribution loop, and CDS's participant weights, Module 3's fairness layer and its review module (evidence_cache/C4.3/integral_wp_v01_c43_extract.txt); Report v1.6, INT C4.3 |
| 2 | convergence trajectory toward <20% disparities within 30 years | not shown | as for clause 1: no projection of the gap's path is stated or located (part (b8), reading 3.3) | Joseph, INTEGRAL: Technical White Paper v0.1 (December 2025; PDF md5 a6defc9a), section 4.3, the contribution loop, and CDS's participant weights, Module 3's fairness layer and its review module (evidence_cache/C4.3/integral_wp_v01_c43_extract.txt) |

*Note:* read on the design's own white paper (v0.1, December 2025), as groups 2.6 and 2.7 read it; 0.5 holds, the band's example, now with a group-directed monitoring mechanism the published rationale did not have; read closely, since Integral's C4.3 could decide who is first (reading 3.7).

#### GEO C4.3 Group Equity: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Disparity reduction ≥5 percentage points every 5 years | not shown | the Citizen's Dividend is universal and flat, which narrows percentage gaps once, by its form; land assessment carries a documented racial bias in current U.S. practice, which no Georgist proposal located corrects; no projection of the gap between groups' median household incomes on any axis, from a model or calibrated components, is stated or located, so neither the rate nor the convergence is shown (part (b8), reading 3.3) | Report v1.6, GEO C4.3 |
| 2 | convergence trajectory toward <20% disparities within 30 years | not shown | as for clause 1: no projection of the gap's path is stated or located (part (b8), reading 3.3) | Report v1.6, GEO C4.3 |

*Flag (reading 3.6):* toward 0.0: weighting the documented assessment bias, which land-only valuation could amplify, as a mechanism that replicates disparity; the published flag's 1.0 side lapses: 1.0 now needs a projection of the gap on each declared axis, which no source gives (reading 3.6).

*Note:* 0.5 holds (reading 3.2); the published flag's 0.0 side kept.

#### MC C4.3 Group Equity: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Disparity reduction ≥5 percentage points every 5 years | not shown | time banking values care work, which bears on the gender axis, and Grassroots Economics reaches low-income non-white communities, but a long-running UK scheme's membership was overwhelmingly white in a diverse area; no projection of the gap between groups' median household incomes on any axis, from a model or calibrated components, is stated or located, so neither the rate nor the convergence is shown (part (b8), reading 3.3) | Report v1.6, MC C4.3 |
| 2 | convergence trajectory toward <20% disparities within 30 years | not shown | as for clause 1: no projection of the gap's path is stated or located (part (b8), reading 3.3) | Report v1.6, MC C4.3 |

*Flag (reading 3.6):* toward 0.0: weighting the documented participation gap as evidence that formally open schemes replicate exclusion; the published flag's 1.0 side lapses: 1.0 now needs a projection of the gap on each declared axis, which no source gives (reading 3.6).

*Note:* 0.5 holds (reading 3.2); the published flag's 0.0 side kept.

#### DE C4.3 Group Equity: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Disparity reduction ≥5 percentage points every 5 years | not shown | gender equality is one of the social foundation's twelve dimensions and unpaid care work is engaged directly, which bears on the gender axis; no reparative mechanism for racial disparities is located; no projection of the gap between groups' median household incomes on any axis, from a model or calibrated components, is stated or located, so neither the rate nor the convergence is shown (part (b8), reading 3.3) | NEEC_DoughnutEconomics_scoring_scratch.md, C4.3 |
| 2 | convergence trajectory toward <20% disparities within 30 years | not shown | as for clause 1: no projection of the gap's path is stated or located (part (b8), reading 3.3) | NEEC_DoughnutEconomics_scoring_scratch.md, C4.3 |

*Note:* 0.5 holds (reading 3.2).

#### UBS C4.3 Group Equity: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Disparity reduction ≥5 percentage points every 5 years | not shown | universal non-means-tested provision removes a documented channel of racially disparate stigma, and Quebec's universal childcare raised mothers' employment, which bears on the gender axis; no reparative mechanism and a documented rollout-equity concern in the closest precedent; no projection of the gap between groups' median household incomes on any axis, from a model or calibrated components, is stated or located, so neither the rate nor the convergence is shown (part (b8), reading 3.3) | NEEC_UniversalBasicServices_scoring_scratch.md, C4.3 |
| 2 | convergence trajectory toward <20% disparities within 30 years | not shown | as for clause 1: no projection of the gap's path is stated or located (part (b8), reading 3.3) | NEEC_UniversalBasicServices_scoring_scratch.md, C4.3 |

*Note:* 0.5 holds (reading 3.2); the published flag, toward 1.0 only, lapses: 1.0 now needs a projection of the gap on each declared axis (reading 3.6).

#### SWF C4.3 Group Equity: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Disparity reduction ≥5 percentage points every 5 years | not shown | Alaska's dividend, flat per resident, reduces poverty proportionally more for rural Alaska Natives, but the Native-non-Native poverty ratio, about 2.5, has not closed over the dividend's forty years, and the host economy's gaps are not credited to the mechanism (protocol 3.2); no projection of the gap between groups' median household incomes on any axis, from a model or calibrated components, is stated or located, so neither the rate nor the convergence is shown (part (b8), reading 3.3) | NEEC_SovereignWealthFundStatism_scoring_scratch.md, C4.3 |
| 2 | convergence trajectory toward <20% disparities within 30 years | not shown | as for clause 1: no projection of the gap's path is stated or located (part (b8), reading 3.3) | NEEC_SovereignWealthFundStatism_scoring_scratch.md, C4.3 |

*Flag (reading 3.6):* toward 0.0: weighting the persistent gap and the documented adverse correlate over the disproportionate proportional benefit; the published flag's 1.0 side lapses: 1.0 now needs a projection of the gap on each declared axis, which no source gives (reading 3.6).

*Note:* 0.5 holds (reading 3.2); the published flag's 0.0 side kept.

#### CN C4.3 Group Equity: 0.0 → 0.0

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Disparity reduction ≥5 percentage points every 5 years | not shown | no national household survey publishes median household income by ethnic group (the National Bureau of Statistics publishes by urban and rural residence and by region), so no gap on the ethnic axis can be measured, as for Centrally Planned Socialism (part (b8), reading 3.5) (reading 3.5) | NEEC_StateCapitalism_China_scoring_scratch.md, C4.3 |
| 2 | convergence trajectory toward <20% disparities within 30 years | not shown | no series exists from which a convergence on the ethnic axis could be projected; top-level gender representation has fallen since 2022 (reading 3.5) | NEEC_StateCapitalism_China_scoring_scratch.md, C4.3 |

*0.0 (protocol 2.1):* the system excludes the criterion's concern for the minorities most affected (protocol 2.1): coercive state action targeting them, which the UN human rights office found may constitute crimes against humanity, and an assimilationist ethnic law of 2026, a harm beyond the formal neutrality of the 0.0 band.

*Flag (reading 3.5):* toward 0.5: weighting the preferential policies (examination bonus points, the one-child exemption) as a disproportionate-benefit mechanism; the published flag's 1.0 side, on the Centrally Planned Socialism precedent, lapses, since that unit fell to 0.5 in part (b8).

*Note:* 0.0 holds.

#### SG C4.3 Group Equity: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Disparity reduction ≥5 percentage points every 5 years | short | on the ethnic axis the entry's text declares, Malay households have the lowest median household market income and Indian households the highest: the gap is 35.9% in 2025 against 32.1% in 2020, +3.8 points in five years; per household member, against Chinese households, the highest, 43.6% against 41.7% (+1.9); the gap widened, so clause 1 is short (reading 3.4) | Department of Statistics Singapore, General Household Survey 2025 (June 2026), Table 6.1, median monthly household market income by ethnic group of the household reference person, resident households (evidence_cache/C4.3/sg_ghs2025_table6_1.txt); Ministry of Education, parliamentary reply of 7 May 2026 on the Tertiary Tuition Fee Subsidy for Malays (introduced 1991, government-funded, administered by Yayasan MENDAKI, means-tested), retrieved 2026-10-15; NEEC_StateCapitalism_Singapore_scoring_scratch.md, C4.3 |
| 2 | convergence trajectory toward <20% disparities within 30 years | short | a gap that widened over the one five-year interval the survey gives is not on a trajectory toward 20%; the entry's own record has Malay per-member incomes growing fastest from 2010 to 2020 (census), so the decade before ran the other way, and two intervals with opposite signs establish no trajectory (reading 3.4) | Department of Statistics Singapore, General Household Survey 2025 (June 2026), Table 6.1, median monthly household market income by ethnic group of the household reference person, resident households (evidence_cache/C4.3/sg_ghs2025_table6_1.txt); NEEC_StateCapitalism_Singapore_scoring_scratch.md, C4.3 |

*Flag (reading 3.4):* toward 0.0: on the measure the Malay gap widened from 2020 to 2025 while the system's transfers, though progressive, are not reparative; the 0.0 band read literally.

*Note:* 0.5 holds: a group-directed, government-funded mechanism in force (the Tertiary Tuition Fee Subsidy for Malays, means-tested, since 1991), the 2025 Workplace Fairness Act, and a mixed record over 15 years (reading 3.4); the published flag toward 0.0 kept, now on the measure.

#### QA C4.3 Group Equity: 0.0 → 0.0

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Disparity reduction ≥5 percentage points every 5 years | not shown | the 2012/13 household survey reports average monthly household income of QR 72,700 for Qatari households and QR 24,400 for non-Qatari households, a gap of 66.4% on means, with workers in collective housing outside the survey; one survey gives no rate (reading 3.5) | Planning and Statistics Authority, Household Income and Expenditure Survey 2012/13, as reported by The Peninsula (18 June 2014) and Doha News (average monthly household income, Qatari QR 72,700, non-Qatari QR 24,400); psa.gov.qa did not answer the container, so the 2017/18 survey was not read; NEEC_StateCapitalism_Qatar_scoring_scratch.md, C4.3 |
| 2 | convergence trajectory toward <20% disparities within 30 years | not shown | no series is located from which a convergence on the citizenship axis could be projected (reading 3.5) | Planning and Statistics Authority, Household Income and Expenditure Survey 2012/13, as reported by The Peninsula (18 June 2014) and Doha News (average monthly household income, Qatari QR 72,700, non-Qatari QR 24,400); psa.gov.qa did not answer the container, so the 2017/18 survey was not read |

*0.0 (protocol 2.1):* the system excludes the criterion's concern (protocol 2.1): rights and rent-funded benefits are allocated by nationality to the most advantaged legal group, the reverse of the flow the criterion asks for, and v2.0's scope counts the non-citizen residents, most of the population, whom the allocation excludes.

*Note:* 0.0 holds.

#### IF C4.3 Group Equity: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Disparity reduction ≥5 percentage points every 5 years | not shown | the contracts' terms are the same whoever signs, formal equality without a reparative mechanism; the documented gaps are in participation (women's uptake of Islamic microfinance and wealth management in Malaysia), not on the measure; the host economy's gaps are not credited to the mechanism (protocol 3.2); no projection of the gap between groups' median household incomes on any axis, from a model or calibrated components, is stated or located, so neither the rate nor the convergence is shown (part (b8), reading 3.3) | NEEC_IslamicFinance_scoring_scratch.md, C4.3 |
| 2 | convergence trajectory toward <20% disparities within 30 years | not shown | as for clause 1: no projection of the gap's path is stated or located (part (b8), reading 3.3) | NEEC_IslamicFinance_scoring_scratch.md, C4.3 |

*Flag (reading 3.6):* toward 0.0: folding inheritance rules into the mechanism, or weighting the participation gap as evidence that formally neutral contracts replicate disparity.

*Note:* 0.5 holds on the owner-confirmed scope (Session 22, D5) and the 0.5 band's 'formal equality without reparative mechanisms' (reading 3.2); the published flag kept; it alone could change the entry's tier.

#### OS C4.3 Group Equity: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Disparity reduction ≥5 percentage points every 5 years | not shown | participatory exclusion of women, Indigenous and landless users is documented across settings, and so are working remedies inside the mechanism (India's Joint Forest Management quotas) and collective tenure for some 370 million Indigenous people; no projection of the gap between groups' median household incomes on any axis, from a model or calibrated components, is stated or located, so neither the rate nor the convergence is shown (part (b8), reading 3.3) | NEEC_Ostrom_Commons_scoring_scratch.md, C4.3 |
| 2 | convergence trajectory toward <20% disparities within 30 years | not shown | as for clause 1: no projection of the gap's path is stated or located (part (b8), reading 3.3) | NEEC_Ostrom_Commons_scoring_scratch.md, C4.3 |

*Flag (reading 3.6):* toward 0.0: reading participatory exclusion as a structural property of bounded, locally governed institutions and the quotas as an external correction.

*Note:* 0.5 holds (reading 3.2); the published flag kept.

## 5. The sources added to the evidence cache

All three files were written on 2026-10-15 in `evidence_cache/C4.3/`. `us_census_h05_extract.txt` holds the median
household income in current dollars of seven series of the Census Bureau's Table H-5 (white alone not Hispanic, white not
Hispanic, Black alone, Black, Asian alone, Asian and Pacific Islander, Hispanic), every year the table gives, with the
xlsx's md5 (9086455a); where a year is listed twice the table's later estimate, listed first, is used.
`sg_ghs2025_table6_1.txt` holds lines 2621 to 2680 of the General Household Survey 2025's text (`pdftotext -layout`;
PDF md5 051185ee): the section on household income by ethnic group and Table 6.1. `integral_wp_v01_c43_extract.txt`
holds five passages of Integral's white paper (PDF md5 a6defc9a, the copy groups 2.6 and 2.7 read), each headed by its
line range. The script checks each file by digest, finds each quoted passage, and recomputes every gap the readings
quote. Not cached, and named in the units: the Ministry of Education's parliamentary reply of 7 May 2026 on the
Tertiary Tuition Fee Subsidy; Executive Order 14173; the Qatar survey's press reports.

## 6. What parts (a), (b), groups 2.1 to 2.8 and part 58.1 change (generated)

| Entry | Published (rank) | After group 2.7 (rank) | After group 2.8 (rank) | Change here | Failures | Tier |
|---|---:|---:|---:|---:|---:|---|
| CCO | 24.5 (1) | 14.5 (1) | 14.5 (1) | 0.0 | 0 | Potentially Adequate |
| PE | 20.5 (2) | 14.0 (3) | 14.0 (3) | 0.0 | 1 | Potentially Adequate |
| NSD | 19.5 (3) | 13.5 (4) | 13.5 (4) | 0.0 | 1 | Potentially Adequate |
| INT | 19.5 (3) | 14.5 (1) | 14.5 (1) | 0.0 | 2 | Potentially Adequate |
| DG | 19.0 (5) | 13.0 (5) | 13.0 (5) | 0.0 | 2 | Potentially Adequate |
| MS | 16.5 (6) | 13.0 (5) | 13.0 (5) | 0.0 | 2 | Potentially Adequate |
| MMT | 15.5 (7) | 11.0 (14) | 11.0 (14) | 0.0 | 4 | Partially Adequate |
| UBI | 14.5 (8) | 10.5 (15) | 10.5 (15) | 0.0 | 7 | Structurally Inadequate |
| MC | 14.5 (8) | 12.5 (9) | 12.5 (9) | 0.0 | 3 | Partially Adequate |
| OS | 14.5 (8) | 13.0 (5) | 13.0 (5) | 0.0 | 3 | Partially Adequate |
| SWF | 14.0 (11) | 13.0 (5) | 13.0 (5) | 0.0 | 3 | Partially Adequate |
| SG | 14.0 (11) | 11.5 (11) | 11.5 (11) | 0.0 | 4 | Partially Adequate |
| GEO | 13.5 (13) | 12.5 (9) | 12.5 (9) | 0.0 | 2 | Potentially Adequate |
| UBS | 13.5 (13) | 11.5 (11) | 11.5 (11) | 0.0 | 4 | Partially Adequate |
| IF | 13.5 (13) | 11.5 (11) | 11.5 (11) | 0.0 | 5 | Partially Adequate |
| FALC | 13.0 (16) | 9.0 (18) | 9.0 (17) | 0.0 | 10 | Structurally Inadequate |
| DE | 11.5 (17) | 9.0 (18) | 9.0 (17) | 0.0 | 8 | Structurally Inadequate |
| SQ | 10.5 (18) | 9.5 (16) | 9.0 (17) | -0.5 | 10 | Structurally Inadequate |
| CPS | 10.0 (19) | 7.5 (22) | 7.5 (22) | 0.0 | 12 | Structurally Inadequate |
| SC | 10.0 (19) | 9.0 (18) | 9.0 (17) | 0.0 | 8 | Structurally Inadequate |
| CN | 10.0 (19) | 9.5 (16) | 9.5 (16) | 0.0 | 8 | Structurally Inadequate |
| QA | 9.0 (22) | 8.5 (21) | 8.5 (21) | 0.0 | 9 | Structurally Inadequate |
| LM | 8.0 (23) | 7.0 (23) | 7.0 (23) | 0.0 | 13 | Structurally Inadequate |

After this group the corpus has 17 dominance pairs against 17 after group 2.7 (new: none; lost: none), and its frontier holds 15 entries against 15 (SQ, NSD, CPS, MS, LM, UBI, DG, FALC, PE, CCO, INT, MC, SWF, IF, OS). First place is shared by CCO and INT at 14.5 (CCO 14.5, INT 14.5 after group 2.7), ahead of PE at 14.0. Across the pass so far 267 units have been re-estimated, each counted once: 18 are at 1.0, 221 at 0.5 and 28 at 0.0; against their published scores 149 fell, 7 rose and 111 are unchanged (net -71.0 points).

| Entry | Published | (a) | (b1) | (b2) | (b3) | (b4) | (b5) | (b6) | (b7) | 48.3 | (b8) | (b9) | (2.1) | (2.2) | (2.3) | (2.4) | (2.5) | 58.1 | (2.6) | (2.7) | (2.8) | Now | Re-estimated | At 0.5 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| CCO | 24.5 | -0.5 | -1.5 | -0.5 | -0.5 | -0.5 | -0.5 | -1.0 | -0.5 | -0.5 | -0.5 | -1.0 | -1.5 | -0.5 | -0.5 |  | -0.5 | 0.5 |  |  |  | 14.5 | 22 | 20 |
| PE | 20.5 |  | -1.5 | -0.5 | -0.5 | -1.5 |  | -0.5 | -0.5 |  | -0.5 | -0.5 |  |  | -0.5 |  |  |  |  |  |  | 14.0 | 17 | 16 |
| NSD | 19.5 | -2.5 | -1.0 | -0.5 | -0.5 | -0.5 |  |  |  |  | -0.5 | -0.5 |  | -0.5 |  | 0.5 |  |  |  |  |  | 13.5 | 16 | 15 |
| INT | 19.5 | -0.5 | -1.0 | -0.5 |  | -1.0 | -0.5 | -1.0 | -0.5 |  |  |  |  |  | -0.5 |  |  |  | 0.5 |  |  | 14.5 | 17 | 14 |
| DG | 19.0 |  | -1.5 | -0.5 | -0.5 | -0.5 |  | -0.5 | -1.0 |  | -1.0 |  |  |  | -0.5 |  |  |  |  |  |  | 13.0 | 16 | 16 |
| MS | 16.5 | -1.0 | -1.5 | -0.5 | -0.5 |  |  |  | 0.5 |  |  |  |  | -0.5 |  |  |  |  |  |  |  | 13.0 | 14 | 12 |
| MMT | 15.5 | -1.5 | -1.0 | -0.5 | -0.5 |  |  |  |  |  | -0.5 |  |  | -0.5 |  |  |  |  |  |  |  | 11.0 | 11 | 9 |
| UBI | 14.5 | -1.5 | -0.5 | -0.5 | -0.5 |  |  |  |  |  | -0.5 |  |  |  |  |  |  |  |  | -0.5 |  | 10.5 | 13 | 10 |
| MC | 14.5 |  | -1.0 | -0.5 |  |  | -0.5 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 12.5 | 11 | 8 |
| OS | 14.5 | -0.5 |  |  |  |  | -0.5 | -0.5 |  |  |  |  |  |  |  |  |  |  |  |  |  | 13.0 | 10 | 8 |
| SWF | 14.0 |  |  | -0.5 |  |  | -0.5 | -0.5 |  |  |  |  |  |  |  |  |  |  | 0.5 |  |  | 13.0 | 10 | 7 |
| SG | 14.0 | -1.0 | -0.5 | -0.5 |  |  |  |  |  |  |  |  |  | -0.5 |  |  |  |  |  |  |  | 11.5 | 9 | 9 |
| GEO | 13.5 | -0.5 |  |  |  |  | -0.5 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 12.5 | 8 | 7 |
| UBS | 13.5 |  | -0.5 | -0.5 |  |  | -0.5 |  |  |  |  |  |  |  |  | -0.5 |  |  |  |  |  | 11.5 | 10 | 7 |
| IF | 13.5 | -1.0 |  |  |  |  | -0.5 |  |  |  |  | -0.5 |  |  |  |  |  |  |  |  |  | 11.5 | 9 | 8 |
| FALC | 13.0 | -0.5 | -0.5 |  | -0.5 | -1.0 |  | -0.5 | -0.5 |  |  |  |  |  | -0.5 |  |  |  |  |  |  | 9.0 | 13 | 10 |
| DE | 11.5 | -0.5 | -0.5 |  |  |  | -0.5 | -0.5 | -0.5 |  |  |  |  |  |  |  |  |  |  |  |  | 9.0 | 11 | 9 |
| SQ | 10.5 | -0.5 |  |  |  | -0.5 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | -0.5 | 9.0 | 8 | 5 |
| CPS | 10.0 | -1.5 |  |  | -0.5 |  |  |  |  |  | -0.5 |  |  |  |  |  |  |  |  |  |  | 7.5 | 9 | 6 |
| SC | 10.0 |  | -1.0 |  |  |  |  |  |  |  |  | -0.5 |  |  |  | 0.5 |  |  |  |  |  | 9.0 | 8 | 7 |
| CN | 10.0 |  |  | -0.5 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 9.5 | 7 | 5 |
| QA | 9.0 | -0.5 |  | -0.5 |  |  |  |  |  |  |  |  |  |  |  | 0.5 |  |  |  |  |  | 8.5 | 8 | 7 |
| LM | 8.0 | -1.5 |  |  |  |  |  |  |  |  |  | -0.5 |  | 0.5 |  | 0.5 |  |  |  |  |  | 7.0 | 10 | 6 |

Anchor examples citing a unit the pass moves: C1.1's 1.0 example, NSD (part (b3)); C1.2a's 1.0 example, MS (part (2.2)); C1.2b's 1.0 example, CCO (part (2.5)); C1.4's 1.0 example, CCO (part (2.5)); C2.1's 1.0 example, UBI (part (a)); C2.3's 1.0 example, DG (part (b1)); C2.4's 1.0 example, PE (part (b1)); C2.5's 1.0 example, CCO (part (b5)); C3.1's 1.0 example, UBI (part (b2)); C3.2's 1.0 example, PE (part (b4)); C3.5's 1.0 example, CCO (part (b6)); C3.5's 0.0 example, LM (part (2.4)); C3.5's 0.0 example, SC (part (2.4)); C4.1's 1.0 example, DG (part (b6)); C4.2's 1.0 example, PE (part (b7)); C4.3's 1.0 example, CCO (part (b8)); C5.1's 1.0 example, MS (part (b2)); C5.2's 1.0 example, CCO (part (b9)); C5.2's 0.0 example, INT (part (2.6)); C5.4's 1.0 example, CCO (part (b9)); C5.5's 1.0 example, PE (part (b9)). Bands whose example the pass moves and which no corpus unit then scores at their value: C1.1's 1.0, C1.2a's 1.0, C1.4's 1.0, C2.1's 1.0, C2.3's 1.0, C2.4's 1.0, C3.1's 1.0, C3.5's 1.0, C4.1's 1.0, C4.2's 1.0, C4.3's 1.0.

C4.3's published anchors: CCO-PTF-CIP-SZH at 1.0 (moved to 0.5 by part (b8)), Integral at 0.5 (holds) and Status Quo at
0.0 (published 0.5; now 0.0, so the example and the unit agree). After this group no corpus unit is at 1.0 on C4.3;
stage 3's restatement of the criterion's anchors drops the 1.0 band's example, as part (b8) recorded.

## 7. Corrections found (not polish)

1. **Status Quo's C4.3, 0.5 → 0.0** (reading 3.3): the published 0.5 rests on "some progress over decades", which the
   measure does not show; the 0.0 band's example now agrees with its unit.
2. **Integral's C4.3 rationale** finds no discussion of whether contribution weighting accounts for disadvantage; the
   white paper, published after the corpus scored the design, names protected-category adjustments (reading 3.7).
   Report v2.0 cites the paper; the verdict is unchanged.
3. **Singapore's C4.3 rationale** reads ethnic income by census decade; on the 2025 survey the Malay gap widened from 2020
   (reading 3.4). Report v2.0 states the survey's figures; the verdict is unchanged.

## 8. Disclosure

CCO-PTF-CIP-SZH is the owner's design. Its C4.3 unit was read in part (b8) and is not re-read here; this group changes
none of its scores. First place stays shared at 14.5 by CCO-PTF-CIP-SZH and Integral: Integral's unit, which alone could
have changed that, holds at 0.5 on reading 3.7, which was made on the white paper's text before the consequences were
computed. Every reading here was made before the consequences table was computed. Status Quo's fall follows from the
Census series; the line of reading 3.2 was drawn so that it applies alike to the deployed economies (Status Quo,
Singapore) and to the formally neutral mechanism (Islamic Finance), and the record states for each why it falls or holds.

## 9. What remains

- **Next group from the triage** (rerun after this group, `triage_s52_output.txt`): C3.1 Crisis Response Capacity, class I (16 units in play, 3 tier-capable), which needs its
  evidence cache first; then C1.1, C4.2, C4.1, C2.1, C2.3, C2.4, C4.4, C4.5, C2.5 and C3.4. The units that alone could
  change who is first are now six (NSD C2.5, PE C2.5, PE C4.5, CCO C4.5, INT C1.1, INT C3.4); the units that could
  change no failure count, tier or rank on their own are six (CCO C4.5, CN C2.5, CPS C2.5, IF C4.5, SG C2.5, UBS C4.5).
- **For the criteria record's next amendment:** decision 61.1 (0.0 and 0.5 on C4.3 under protocol 2.1), with the method
  choices listed in `STATE.md`; C4.3's anchors (section 6).
- **For Report v2.0:** section 7's corrections; the gender and wealth axes not read (reading 3.8); the flags.
- **Sources a later session could add:** Qatar's 2017/18 household survey by nationality; a published projection of any
  design's or mechanism's group income gaps, which would be the first evidence that could show either clause for one.

## 10. What this record does not show

No source projects any design's or mechanism's gap between groups, so for them C4.3 can at present separate only 0.0
from 0.5. "Not shown" means that no estimate was located, not that the clause fails. The United States and Singapore
are read on one income concept each (money income before taxes; household market income before transfers), and neither
is equivalised, as the measure does not ask. Qatar is read on press reports of a 2012/13 survey. The white paper is read
in five passages chosen by searching its text for equity, demographic groups, protected categories and marginalisation;
it is 345 pages and a later version may say more. The interpretation check (decisions 50.1 to 50.4) was not run; it is
optional. The record is one scorer's re-estimation; whether its calls reproduce is what the replication programme tests.
