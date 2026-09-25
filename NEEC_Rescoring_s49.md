# NEEC Rescoring Pass — Record, Part (b), Eighth Group: C4.3 Group Equity and C4.5 Exploitation Elimination, on the v2.0 Clauses

**Session 49 · 2026-09-25 · Scorer and engineer: Claude · Owner: Duke Johnson**
**Status: scratch (protocol 10.1). Parts (a) to (b7) are `NEEC_Rescoring_s37.md` to `NEEC_Rescoring_s47.md`, and
`NEEC_Rescoring_s48.md` re-read C4.4 on decision 48.3; this record continues the pass and edits none of them.** No
corpus file, score or scoring document changes until the pass ends. Its changes are then applied by generator with
pinned inputs and restated in place (protocol 10.2, 10.3; decisions D12, D14), and until then the published totals
stand, provisional as `README.md` says. Decisions taken here are Claude's under the owner's delegation (Handoff 35,
section 2); each is recorded with its reasons, and the owner may reverse any of them.
**Reproduce:** `python3 rescoring_s49.py` (harness check 95). The script holds every clause estimate below on the
v2.0 clauses (`criteria.json`), maps each to the Session 44 clause the R4 audit coded, checks the group against the
audit's register and against part (a), re-reads the audit's A codes on C4.3 and carries them on C4.5, computes
Nordic Social Democracy's C4.3 clause 1 from the Eurostat figures it holds, computes every figure in section 5
cumulatively with parts (a) to (b7) and decision 48.3 on the published 26-criterion structure, and checks that this
record contains its generated tables verbatim.

---

## 1. What this group is

Handoff 48 set C4.3 and C4.5 next, on the v2.0 clauses as part (b7) was. C4.3's part (b) units are Nordic Social
Democracy, Centrally Planned Socialism, MMT + Job Guarantee, Universal Basic Income, Degrowth Economics and
Participatory Economics; its seventh published 1.0, CCO-PTF-CIP-SZH's, is outside D28's population because the audit
coded every clause A, and is re-checked here as class M (reading 3.8). C4.5's part (b) units are Degrowth, Fully
Automated Luxury Communism and Integral; its other three published 1.0s, Centrally Planned Socialism, Libertarian
Minarchism and Universal Basic Income, fell in part (a) and are re-read here on the v2.0 clauses (reading 3.7).

**The v2.0 clauses.** C4.3 (class M) keeps "Disparity reduction ≥5 percentage points every 5 years" and "convergence
trajectory toward <20% disparities within 30 years" verbatim and deletes "disadvantaged groups receive 150%+
proportional benefits", which its measurement now counts as evidence for the trajectory, not a separate test. It
adds a scope, "on each declared axis, non-citizen residents included", and a measure: the gap between the median
household incomes of the least and most advantaged groups on each axis declared in the entry's scope, as a
percentage of the most advantaged group's median, from national household surveys. C4.5 (class D) keeps "Extraction
rates <10% GDP" and "genuine exit rights from exploitative relationships" verbatim and deletes "residual coercion
<10% of decisions", which v2.0 measures once, in C2.1 (K5).

**What the audit found,** on the Session 44 clauses: on C4.3, Centrally Planned Socialism was silent on the rate,
MMT + Job Guarantee on convergence, and Universal Basic Income, Degrowth and Participatory Economics on both; every
unit was silent on the 150% clause except MMT's and CCO-PTF-CIP-SZH's. On C4.5, every part (b) unit was silent on exit
rights, and Degrowth on coercion as well.

**Outcome.** *C4.3:* all seven become 0.5 (3.5 points, CCO-PTF-CIP-SZH's included). Nordic Social Democracy is short
on the rate: on its immigrant axis, in each of the four countries a gap above 20% falls by less than 5 points in five
years (reading 3.4). No design or mechanism projects the gaps (reading 3.3), and no series by nationality exists for
the Soviet-type record (reading 3.5). **C4.3 joins the criteria no scored system clears, which are now nine.**
*C4.5:* Fully Automated Luxury Communism and Integral stand, Integral flagged; Degrowth becomes 0.5, flagged, on exit
rights (reading 3.6). *Part (a)'s units:* all three stay 0.5. Net −4.0 points; no failure count and no tier changes.
CCO-PTF-CIP-SZH keeps first place, 18.5 to 18.0; Participatory Economics is second at 15.0; Integral is third at 14.5.
Two dominance pairs are added (CCO-PTF-CIP-SZH over Degrowth, Integral over Centrally Planned Socialism), and
Degrowth leaves the frontier, which falls from 13 entries to 12.

## 2. How a clause is recorded, and the rule

As in part (a), section 2: each clause is cleared, short, not shown, out of reach or moot; a 1.0 stands only if every
clause is cleared or moot, and otherwise becomes 0.5 (D28, protocol 2.3). The clauses are v2.0's, in their Pass
Threshold's order (`criteria.json`; protocol draft.9, Appendix B). Each is mapped to the Session 44 clause it
continues and inherits that clause's audit code: C4.3's two from the Session 44 clauses 1 and 3, C4.5's from clauses 1
and 2. A clause the audit coded A on C4.5, which v2.0 keeps verbatim and places under no new scope, is carried as
cleared on the unit's own text ("as audited"); none of the design's own sources contradicts it. On C4.3 every A code
is read again against the clause with its scope and measure (reading 3.2); none is carried. Every clause is estimated:
none is left "not estimated in this pass". One clause is out of reach, Universal Basic Income's C4.5 clause 1, as the
audit coded it and part (a) confirmed.

## 3. Decisions and readings (under the delegation)

**3.1 The group, and the structure its totals are on.** The units are listed by criterion in the audit register's
order, then CCO-PTF-CIP-SZH's C4.3 (reading 3.8), then part (a)'s re-read units. The consequences in section 5 are
computed, as in every earlier group, on the published 26-criterion structure with the pass's re-estimates in force,
decision 48.3's re-reading of C4.4 included. v2.0's three new criteria have no scored units yet, so totals on 29
criteria wait for stage 2's new units; the verdicts here are on v2.0's clauses and carry over unchanged.

**3.2 C4.3's scope and measure, and the audit's codes.** (1) *Interpretations.* v2.0 keeps C4.3's two remaining
clauses word for word, so an A code on them could (a) be carried as audited, as on any verbatim clause, or (b) be read
again against the clause with its new scope and measure, as part (b7)'s reading 3.2 reads A codes on restated clauses
and as `rescoring_s48.py` re-read every C4.4 unit when decision 48.3 defined clause 1's measure. (2) *Preponderance:*
(b). The words are the same, but what they test is not: the audit read "disparity reduction" against a clause with no
axis and no measure, and v2.0 asks for a fall in a stated quantity, the gap between groups' median household incomes,
on every axis the entry's society makes salient, non-citizen residents included. Session 48 found that carrying a
code "as audited" on a clause whose measure had changed shielded one unit from the test applied to another
(`NEEC_Rescoring_s48.md`, correction 1). (3) *Score* against (b): a phrase is carried where it claims that the gap on a
declared axis falls at the rate, or converges; a policy, a commitment, a remuneration rule, access to a benefit, or an
outcome on another measure (labour force participation, a gender equality index, trafficking vulnerability) is not
such a claim, and the clause is estimated. (4) *Applied:* none of the nine A codes on C4.3's two clauses is carried
(seven in the part (b) units, two in CCO-PTF-CIP-SZH's). *Alternative recorded:* reading (a) would carry seven
clauses as cleared, and Nordic Social Democracy's, MMT + Job Guarantee's, Universal Basic Income's, Degrowth's and
Participatory Economics' C4.3 would still fall on their silent clauses; it would change the verdicts of none of the
part (b) units, and would keep CCO-PTF-CIP-SZH's at 1.0 on phrases that do not name the measure.

**3.3 C4.3 for designs and mechanisms: a projection on the measure.** Part (b1)'s reading 3.5 holds that a design's
specification of an institution is not an estimate of the level it produces, and part (b7)'s reading 3.3 that a
clause's measure is what a design must project. C4.3's clauses are a rate and a trajectory of a measured gap, so for
a design or a mechanism each is shown by a modelled or component-calibrated projection of the gap between groups'
median household incomes on each declared axis. *Applied:* none of the five has one. MMT + Job Guarantee's
proponents argue that it would effectively eliminate the racial unemployment gap and set an economy-wide floor on
compensation (Paul, Darity and Hamilton, 2018), which is a claim about unemployment, not household income. A basic
income narrows percentage gaps once, when it is introduced; that is a level shift, not a reduction every five years,
and no projection of the gaps under one was located. Degrowth's decolonial and feminist-economic aims are goals.
Participatory Economics' remuneration by effort, sacrifice and need ties income to them, but the gaps that result
between groups turn on hours, need allowances and household composition, which no source estimates. *Reopening:* a
projection, from a published model or calibrated components, of the gap on each axis a design declares.

**3.4 C4.3 for Nordic Social Democracy: the immigrant axis.** (1) *The axis.* The entry's scope declaration, written
for v1, declares no axes. Its own C4.3 text names "immigrant and minority communities", so immigrant background is a
declared axis, and v2.0's scope brings non-citizen residents into it. It is read by country of birth and by
citizenship, the two breakdowns the countries' household surveys publish. (2) *The source.* EU-SILC, the national
household survey of each of the four countries, as Eurostat publishes it: median equivalised net income of those
born in (or citizens of) a country outside the EU-27 and the reporting country, against natives (or nationals), who
have the higher median in every edition (ilc_di16, ilc_di15; editions 2016 to 2025, data updated 2026-09-17). (3) *The
rate.* The samples of non-EU-born residents are small and single editions move by several points, so the rate is
measured two ways, and a gap is short only if it fails both: the change between the three-year means of 2018–2020 and
2023–2025, and the least-squares trend over the ten editions, per five years. (4) *Applied:* in each country a gap
above 20% falls by less than 5 points on both measures (Denmark, Finland and Norway by citizenship; Sweden by country
of birth), so clause 1 is short on any reading of how four countries combine. Sweden's citizenship gap does fall
faster than 5 points, and Denmark's and Norway's country-of-birth gaps are below 20%. The gender axis, where the
audited phrase lies, decides nothing: the unit is short on the axis its own text names. *Clause 2:* on the ten-edition
trends every immigrant-axis gap above 20% reaches 20% by 2040 except Denmark's by citizenship, whose trend rises
while its three-year mean falls; series this noisy do not establish a trajectory, so it is not shown. *Reopening:* a
national register series, which has no sampling error, showing each gap above 20% falling 5 points in five years.

| Country | Axis | Gap 2018-2020 | Gap 2023-2025 | Change | Ten-edition trend per 5 years | Breaks |
|---|---|---:|---:|---:|---:|---|
| Denmark | country of birth | 18.6% | 13.5% | -5.1 | -3.9 | 2020 |
| Finland | country of birth | 21.0% | 19.4% | -1.6 | -1.9 | — |
| Sweden | country of birth | 31.6% | 27.4% | -4.2 | -2.4 | — |
| Norway | country of birth | 23.9% | 18.8% | -5.2 | -2.5 | 2021, 2023 |
| Denmark | citizenship | 24.7% | 20.5% | -4.2 | +0.9 | 2020 |
| Finland | citizenship | 25.2% | 21.7% | -3.5 | -3.4 | — |
| Sweden | citizenship | 43.0% | 31.4% | -11.6 | -8.7 | — |
| Norway | citizenship | 27.0% | 25.5% | -1.4 | -3.1 | 2021, 2023 |

**3.5 C4.3 for Centrally Planned Socialism: no series exists.** The Soviet statistics office did not publish the size
distribution of household income from the 1920s until 1989, and then by republic only for 1988 and 1990 (Alexeev and
Gaddy, 1993, section 1): two years, not five, and no earlier point. No source can therefore show a gap between
nationalities' median household incomes falling 5 points in five years, or project its convergence; the 1988
distributions show the southern republics' per capita household incomes well below the northern ones'. The entry's
audited phrase on clause 2, women's high labour force participation, education and leadership roles, is an outcome
on another measure (reading 3.2). Both clauses are not shown. *Reopening:* a reconstructed series of household income
by nationality or republic for any Soviet-type economy.

**3.6 C4.5, clause 2: "genuine exit rights from exploitative relationships".** (1) *Interpretations.* The clause
could ask for (a) the formal right to leave a relationship; (b) the capacity to leave or refuse one without losing
access to subsistence, because the system provides a floor independent of the relationship or an assured
alternative on terms it sets; or (c) the capacity to refuse all participation in the economy without penalty.
(2) *Preponderance:* (b). "Genuine" excludes (a): part (a) held that formal freedom of contract without a subsistence
floor is not genuine exit (Libertarian Minarchism's C4.5) and cleared Universal Basic Income's clause on its cash
floor. The Measurement line reads "capacity to refuse participation without penalty" beside the three extractive
relationships it names (labour and capital, tenants and landlords, borrowers and lenders), so the participation is in
those relationships; reading (c) is C2.2's question, labour non-necessity, which v2.0 measures separately. The clause
is a capacity, like C4.4's removal clause, so a design shows it by a mechanism its own sources specify, of a kind
that functions where it is in use (part (b7), reading 3.5). (3) *Score* against (b): shown where the system's
sources specify, for each kind of extractive relationship it contains, a floor or an assured alternative on which a
person can leave it without losing subsistence. (4) *Applied:* **Fully Automated Luxury Communism** cleared: its
universal material provision, housing included, makes labour optional rather than a survival requirement.
**Integral** cleared and **flagged**: it has no employer, landlord or creditor, a participant can leave a team or
node and have contribution recognised in another, basic needs are accessible below standard contribution thresholds
with need-based adjustments, and a participant can leave the federation without penalty (part (b5)); under reading
(c), or if a floor must be independent of all contribution, "below standard contribution thresholds" does not show it
(alternative 0.5). **Degrowth** not shown and **flagged**: its universal basic services secure housing, healthcare,
education and transport, but for employment the entry specifies reduced hours and work-sharing, not an income floor
or an assured alternative, and its own C2.2 rationale says the design does not fully decouple survival from
employment; its C2.1 rationale says the services "eliminate survival coercion", and read so the clause would be
cleared (alternative 1.0). **Libertarian Minarchism** (part (a), re-read) not shown: formal freedom of contract only.
**Centrally Planned Socialism** (part (a), re-read) short: exit from employment was penalised, the 1977 Constitution
making conscientious work every able-bodied citizen's duty and the RSFSR's 1961 decree punishing the avoidance of
socially useful work.

**3.7 Part (a)'s C4.5 units, re-read on v2.0.** Part (a) scored Centrally Planned Socialism's, Libertarian
Minarchism's and Universal Basic Income's C4.5 on the Session 44 clauses. v2.0 deletes the coercion clause, and C4.5 is
class D, so each can keep its verdict or rise (`NEEC_Criteria_v2_s45.md`, section 7). *Applied:* none rises.
Centrally Planned Socialism's extraction clause is verbatim and stays short, and its exit clause, not estimated in
part (a), is short (reading 3.6). Libertarian Minarchism's deleted coercion clause was its short one, but neither
kept clause is shown. Universal Basic Income's deleted coercion clause was also its short one, but its extraction
clause is out of reach. All three stay 0.5, and the first two keep part (a)'s flags toward 0.0.

**3.8 CCO-PTF-CIP-SZH's C4.3, re-checked as class M now.** Its C4.3 is the one published C4.3 1.0 outside D28's
population, because the audit coded all three of its Session 44 clauses A. C4.3 is class M, so every C4.3 unit is
re-checked against Appendix V in stage 2 whatever its D28 status. Leaving the owner's design as the only C4.3 1.0 not
read on readings 3.2 and 3.3 while its six D28 peers fall on them would repeat the uneven application that Session 48
corrected. It is therefore re-checked here, with the same readings and the same search. Its first audited phrase,
"Universal provision addresses disparities without stigma", is word for word the phrase this group re-reads for
Universal Basic Income. Its 150% benefit flow is evidence for a trajectory, and it states no gap or rate. Its third
phrase, trafficking vulnerability eliminated, is an outcome on another measure. The design's published model (the
Compassionism Simulation at `cd0ceec`, whose engine digest the pass pins) represents no groups, and no page of the
research hub at `8e8a6ba` projects a gap between groups' incomes. Both clauses are not shown, and the unit becomes
0.5. C4.3's 1.0 anchor cites CCO-PTF-CIP-SZH, so when the pass is applied the band loses its example, the ninth
(part (b4), reading 3.5).

## 4. The units

### 4.1 Summary (generated)

| Entry | Criterion | Clauses | Verdict | Flag |
|---|---|---|---|---|
| NSD | C4.3 | S U | 1.0 → 0.5 |  |
| CPS | C4.3 | U U | 1.0 → 0.5 |  |
| MMT | C4.3 | U U | 1.0 → 0.5 |  |
| UBI | C4.3 | U U | 1.0 → 0.5 |  |
| DG | C4.3 | U U | 1.0 → 0.5 |  |
| PE | C4.3 | U U | 1.0 → 0.5 |  |
| CCO | C4.3 | U U | 1.0 (class M) → 0.5 |  |
| DG | C4.5 | C U | 1.0 → 0.5 | alternative 1.0 |
| FALC | C4.5 | C C | 1.0 → 1.0 |  |
| INT | C4.5 | C C | 1.0 → 1.0 | alternative 0.5 |
| CPS | C4.5 | S S | 0.5 (part (a)) → 0.5 | alternative 0.0 |
| LM | C4.5 | U U | 0.5 (part (a)) → 0.5 | alternative 0.0 |
| UBI | C4.5 | R C | 0.5 (part (a)) → 0.5 |  |

### 4.2 Clause by clause (generated)

#### NSD C4.3 Group Equity: 1.0 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Disparity reduction ≥5 percentage points every 5 years | short | the entry's own text names immigrant and minority communities, so immigrant background is a declared axis, read by country of birth and by citizenship (non-EU against natives or nationals); in each of the four countries a gap above 20% falls by less than 5 points in five years on both measures: Denmark by citizenship, 20.5% against 24.7% (-4.2), trend +0.9; Finland by citizenship, 21.7% against 25.2% (-3.5), trend -3.4; Sweden by country of birth, 27.4% against 31.6% (-4.2), trend -2.4; Norway by citizenship, 25.5% against 27.0% (-1.4), trend -3.1 (three-year means, 2023-2025 against 2018-2020; the trend is the least-squares fit over the ten editions, per five years) (reading 3.4) | Eurostat, EU-SILC, ilc_di16 (median equivalised net income by group of country of birth) and ilc_di15 (by group of citizenship), population aged 18 or over, national currency, editions 2016 to 2025, data updated 2026-09-17, retrieved 2026-09-25 (JSON md5 2b786488 and 9f69c948); Report v1.6, NSD C4.3 |
| 2 | convergence trajectory toward <20% disparities within 30 years | not shown | the audited phrase, the strongest performance on gender equity globally, claims the gender axis, not the immigrant axis the entry's text declares; on the ten-edition trends the immigrant-axis gaps above 20% reach 20% by 2040 except Denmark's by citizenship, whose trend rises (+0.9 points per five years) although its three-year mean fell; series this noisy do not establish a convergence trajectory (reading 3.4) | Eurostat, EU-SILC, ilc_di16 (median equivalised net income by group of country of birth) and ilc_di15 (by group of citizenship), population aged 18 or over, national currency, editions 2016 to 2025, data updated 2026-09-17, retrieved 2026-09-25 (JSON md5 2b786488 and 9f69c948) |

*Note:* the audit coded both clauses A; both are re-read against the scope and measure v2.0 adds (reading 3.2).

#### CPS C4.3 Group Equity: 1.0 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Disparity reduction ≥5 percentage points every 5 years | not shown | the rationale is silent on the rate, as the audit found; the Soviet statistics office did not publish the size distribution of household income from the 1920s until 1989, and then by republic only for 1988 and 1990, two years apart, so no source can show a gap between nationalities' median household incomes falling 5 points in five years; the 1988 distributions show the southern republics' per capita household incomes well below the northern ones' (reading 3.5) | Alexeev and Gaddy, Income Distribution in the U.S.S.R. in the 1980s, Review of Income and Wealth 39(1) (1993), section 1 and Tables 1 and 2 (Goskomstat budget surveys; PDF md5 6e1b8367); Report v1.6, CPS C4.3 |
| 2 | convergence trajectory toward <20% disparities within 30 years | not shown | the audited phrase, women's high labour force participation, education and leadership roles, is an outcome on another measure, not a trajectory of household income gaps; for the same reason no series by nationality exists from which a convergence could be projected (readings 3.2 and 3.5) | Alexeev and Gaddy, Income Distribution in the U.S.S.R. in the 1980s, Review of Income and Wealth 39(1) (1993), section 1 and Tables 1 and 2 (Goskomstat budget surveys; PDF md5 6e1b8367); Report v1.6, CPS C4.3 |

#### MMT C4.3 Group Equity: 1.0 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Disparity reduction ≥5 percentage points every 5 years | not shown | the audited phrase, eliminating discrimination in hiring through the government as employer of last resort, is a process; the programme's proponents argue that it would effectively eliminate the racial unemployment gap and set an economy-wide floor on compensation, but a gap in unemployment is not a gap in median household income, and no projection of the gap between groups' median household incomes on any declared axis is stated, modelled or located, so neither the rate nor the convergence is shown (reading 3.3) | Paul, Darity and Hamilton, The Federal Job Guarantee: A Policy to Achieve Permanent Full Employment (Center on Budget and Policy Priorities, 2018); Report v1.6, MMT C4.3 |
| 2 | convergence trajectory toward <20% disparities within 30 years | not shown | the rationale's care and community-service jobs address gendered devaluation of labour, a mechanism; no projection of the gap between groups' median household incomes on any declared axis is stated, modelled or located, so neither the rate nor the convergence is shown (reading 3.3) | Paul, Darity and Hamilton (2018); Report v1.6, MMT C4.3 |

#### UBI C4.3 Group Equity: 1.0 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Disparity reduction ≥5 percentage points every 5 years | not shown | the audited phrase, universal provision that addresses disparities without stigma, describes access to the benefit, not a fall in a gap; a flat payment narrows percentage gaps once, when it is introduced, which is not a reduction every five years; no projection of the gap between groups' median household incomes on any declared axis is stated, modelled or located, so neither the rate nor the convergence is shown (reading 3.3) | Report v1.6, UBI C4.3 |
| 2 | convergence trajectory toward <20% disparities within 30 years | not shown | care work made viable without market employment is a mechanism; no projection of the gap between groups' median household incomes on any declared axis is stated, modelled or located, so neither the rate nor the convergence is shown (reading 3.3) | Report v1.6, UBI C4.3 |

#### DG C4.3 Group Equity: 1.0 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Disparity reduction ≥5 percentage points every 5 years | not shown | the audited phrase, explicitly confronting structural inequalities, is a commitment; decolonial and feminist-economic aims and care valued equally with production are goals and means, and no projection of the gap between groups' median household incomes on any declared axis is stated, modelled or located, so neither the rate nor the convergence is shown (reading 3.3) | Report v1.6, DG C4.3 |
| 2 | convergence trajectory toward <20% disparities within 30 years | not shown | as for clause 1: no projection of the gap between groups' median household incomes on any declared axis is stated, modelled or located, so neither the rate nor the convergence is shown (reading 3.3) | Report v1.6, DG C4.3 |

#### PE C4.3 Group Equity: 1.0 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Disparity reduction ≥5 percentage points every 5 years | not shown | the audited phrase, effort-based remuneration that addresses the devaluation of care work, is a remuneration rule: it ties income to effort, sacrifice and need, but the gaps that would result between groups depend on hours, need allowances and household composition, and no projection of the gap between groups' median household incomes on any declared axis is stated, modelled or located, so neither the rate nor the convergence is shown (reading 3.3) | Report v1.6, PE C4.3 |
| 2 | convergence trajectory toward <20% disparities within 30 years | not shown | balanced job complexes and democratic participation are institutions, not an estimate of the gap's path; no projection of the gap between groups' median household incomes on any declared axis is stated, modelled or located, so neither the rate nor the convergence is shown (reading 3.3) | Report v1.6, PE C4.3 |

#### CCO C4.3 Group Equity: 1.0 (class M) → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Disparity reduction ≥5 percentage points every 5 years | not shown | the audited phrase, universal provision that addresses disparities without stigma, is the phrase re-read for Universal Basic Income: access to the benefit, not a fall in a gap; targeting disadvantaged communities first, with 150%+ proportional benefits during rollout, is a benefit flow, which v2.0's measurement counts as evidence for the trajectory, not a separate test, and it states no gap or rate; the design's published model represents no groups, and its research hub projects no gap; no projection of the gap between groups' median household incomes on any declared axis is stated, modelled or located, so neither the rate nor the convergence is shown (reading 3.3) | Report v1.6, CCO C4.3; Compassionism Simulation at cd0ceec, harness.js (md5 035d1be8) and index.html (md5 1c8273b1), searched 2026-09-25; research hub at 8e8a6ba, searched 2026-09-25 |
| 2 | convergence trajectory toward <20% disparities within 30 years | not shown | the audited phrase, trafficking vulnerability eliminated through unconditional security, is an outcome on another measure, not the path of a household income gap, and aesthetic multipliers that value historically devalued creative work are a mechanism; no projection of the gap between groups' median household incomes on any declared axis is stated, modelled or located, so neither the rate nor the convergence is shown (reading 3.3) | Report v1.6, CCO C4.3; Compassionism Simulation at cd0ceec, harness.js (md5 035d1be8) and index.html (md5 1c8273b1), searched 2026-09-25; research hub at 8e8a6ba, searched 2026-09-25 |

*Note:* the one C4.3 1.0 outside D28's population (the audit coded every clause A); C4.3 is class M, so it is re-checked here on readings 3.2 and 3.3 with the rest of C4.3 rather than left for stage 2 (reading 3.8).

#### DG C4.5 Exploitation Elimination: 1.0 → 0.5 — flagged as contestable

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Extraction rates <10% GDP | cleared | removes profit motive for extraction | as audited (the unit's own text) |
| 2 | genuine exit rights from exploitative relationships | not shown | universal basic services secure housing, healthcare, education and transport, but for employment the entry specifies reduced hours and work-sharing, not an income floor or an assured alternative, and its own C2.2 rationale says the design does not fully decouple survival from employment, so exit from an employment relationship without penalty is not shown (reading 3.6) | Report v1.6, DG C1.1, C2.1, C2.2 and C4.5 |

*Flag:* alternative 1.0: read as the entry's C2.1 rationale reads its universal basic services, as eliminating survival coercion, exit from employment would be genuine; the services it names cover housing, healthcare, education and transport, not food or income, and its C2.2 rationale says survival is not fully decoupled from employment (reading 3.6).

#### FALC C4.5 Exploitation Elimination: 1.0 → 1.0

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Extraction rates <10% GDP | cleared | Eliminates labor exploitation | as audited (the unit's own text) |
| 2 | genuine exit rights from exploitative relationships | cleared | the design provides universal material provision, housing included, through automated production and makes labour an optional hobby rather than a survival requirement, so no one depends on an employment, tenancy or credit relationship for subsistence (reading 3.6) | Report v1.6, FALC C1.1, C1.3 and C2.2 |

#### INT C4.5 Exploitation Elimination: 1.0 → 1.0 — flagged as contestable

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Extraction rates <10% GDP | cleared | removes employer-employee extraction | as audited (the unit's own text) |
| 2 | genuine exit rights from exploitative relationships | cleared | the design has no employer, landlord or creditor: housing is community-controlled, production cooperative, and ITC credits cannot be borrowed, lent or accrue interest; a participant can leave a team or a node, contribution in one node is recognised for access in another, basic needs are accessible below standard contribution thresholds with a need-based adjustment for caregiving and health constraints, and a participant can leave the federation without penalty (reading 3.6) | Report v1.6, INT C4.5; integralcollective.io, The System: ITC (modules ITC-5, ITC-6 and ITC-7), accessed 2026-09-25 (page md5 e5e589fa); NEEC_Rescoring_s42.md, INT C2.5 |

*Flag:* alternative 0.5: read as requiring that a participant able to contribute who declines all contribution keep access to basic needs, the design does not show the clause: basic needs are accessible below standard contribution thresholds, which the design's sources do not say is no contribution at all (reading 3.6).

#### CPS C4.5 Exploitation Elimination: 0.5 (part (a)) → 0.5 — flagged as contestable

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Extraction rates <10% GDP | short | surplus appropriated by the state rather than private owners: extraction continued, to another appropriator, with nothing placing it below 10% of GDP, as part (a) found | Report v1.6, CPS C4.5; rescoring_s37.py, CPS C4.5 |
| 2 | genuine exit rights from exploitative relationships | short | exit from employment was penalised: the 1977 Constitution made conscientious work the duty of every able-bodied citizen and declared evasion of socially useful work incompatible with socialist society, and the RSFSR's decree of 4 May 1961 on persons avoiding socially useful work punished it (reading 3.6) | Constitution of the USSR (1977), article 60; Decree of the Presidium of the Supreme Soviet of the RSFSR of 4 May 1961 |

*Flag:* alternative 0.0: state appropriation read as structural, load-bearing extraction, the 0.0 band's own test (part (a)).

*Note:* part (a)'s unit re-read on v2.0's clauses: clause 1 is verbatim and stays short, and clause 2, left not estimated in part (a), is short; it stays 0.5.

#### LM C4.5 Exploitation Elimination: 0.5 (part (a)) → 0.5 — flagged as contestable

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Extraction rates <10% GDP | not shown | no mechanism limits private extraction, as part (a) found: the entry treats voluntary exchange as non-exploitative by definition | Report v1.6, LM C4.5; rescoring_s37.py, LM C4.5 |
| 2 | genuine exit rights from exploitative relationships | not shown | formal freedom of contract with no subsistence floor and no assured alternative: exit is not shown to be genuine (reading 3.6) | Report v1.6, LM C4.5; rescoring_s37.py, LM C4.5 |

*Flag:* alternative 0.0: the design treats voluntary exchange as non-exploitative by definition: the 0.0 condition of excluding the criterion's concern as illegitimate (protocol 2.1; part (a)).

*Note:* part (a)'s unit re-read on v2.0's clauses: its short clause, residual coercion, is deleted, and neither kept clause is shown; it stays 0.5.

#### UBI C4.5 Exploitation Elimination: 0.5 (part (a)) → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Extraction rates <10% GDP | out of reach | the economy-wide extraction share is not governed by an income transfer | Session 35 reach reason, confirmed in part (a) |
| 2 | genuine exit rights from exploitative relationships | cleared | an exit option from exploitative work | as audited (the unit's own text) |

*Note:* part (a)'s unit re-read on v2.0's clauses: its short clause, residual coercion, is deleted, but clause 1 is out of reach, so it stays 0.5.

## 5. What parts (a) and (b) so far change (generated)

| Entry | Published (rank) | After 48.3 (rank) | After this group (rank) | Change here | Failures | Tier | D28 units left | Floor if all fall |
|---|---:|---:|---:|---:|---:|---|---:|---:|
| CCO | 24.5 (1) | 18.5 (1) | 18.0 (1) | -0.5 | 0 | Potentially Adequate | 1 | 17.5 |
| PE | 20.5 (2) | 15.5 (2) | 15.0 (2) | -0.5 | 1 | Potentially Adequate | 1 | 14.5 |
| NSD | 19.5 (3) | 14.5 (3) | 14.0 (4) | -0.5 | 2 | Potentially Adequate | 2 | 13.0 |
| INT | 19.5 (3) | 14.5 (3) | 14.5 (3) | 0.0 | 3 | Partially Adequate | 0 | 14.5 |
| DG | 19.0 (5) | 14.5 (3) | 13.5 (5) | -1.0 | 2 | Potentially Adequate | 0 | 13.5 |
| MS | 16.5 (6) | 13.5 (6) | 13.5 (5) | 0.0 | 2 | Potentially Adequate | 0 | 13.5 |
| MMT | 15.5 (7) | 12.0 (11) | 11.5 (14) | -0.5 | 3 | Partially Adequate | 0 | 11.5 |
| UBI | 14.5 (8) | 11.5 (15) | 11.0 (15) | -0.5 | 7 | Structurally Inadequate | 0 | 11.0 |
| MC | 14.5 (8) | 12.5 (8) | 12.5 (8) | 0.0 | 3 | Partially Adequate | 1 | 12.0 |
| OS | 14.5 (8) | 13.0 (7) | 13.0 (7) | 0.0 | 3 | Partially Adequate | 0 | 13.0 |
| SWF | 14.0 (11) | 12.5 (8) | 12.5 (8) | 0.0 | 3 | Partially Adequate | 0 | 12.5 |
| SG | 14.0 (11) | 12.0 (11) | 12.0 (11) | 0.0 | 4 | Partially Adequate | 0 | 12.0 |
| GEO | 13.5 (13) | 12.5 (8) | 12.5 (8) | 0.0 | 2 | Potentially Adequate | 0 | 12.5 |
| UBS | 13.5 (13) | 12.0 (11) | 12.0 (11) | 0.0 | 3 | Partially Adequate | 0 | 12.0 |
| IF | 13.5 (13) | 12.0 (11) | 12.0 (11) | 0.0 | 5 | Partially Adequate | 1 | 11.5 |
| FALC | 13.0 (16) | 9.5 (16) | 9.5 (16) | 0.0 | 10 | Structurally Inadequate | 0 | 9.5 |
| DE | 11.5 (17) | 9.0 (19) | 9.0 (19) | 0.0 | 8 | Structurally Inadequate | 0 | 9.0 |
| SQ | 10.5 (18) | 9.5 (16) | 9.5 (16) | 0.0 | 9 | Structurally Inadequate | 0 | 9.5 |
| CPS | 10.0 (19) | 8.0 (21) | 7.5 (22) | -0.5 | 12 | Structurally Inadequate | 0 | 7.5 |
| SC | 10.0 (19) | 9.0 (19) | 9.0 (19) | 0.0 | 9 | Structurally Inadequate | 1 | 8.5 |
| CN | 10.0 (19) | 9.5 (16) | 9.5 (16) | 0.0 | 8 | Structurally Inadequate | 0 | 9.5 |
| QA | 9.0 (22) | 8.0 (21) | 8.0 (21) | 0.0 | 10 | Structurally Inadequate | 0 | 8.0 |
| LM | 8.0 (23) | 6.5 (23) | 6.5 (23) | 0.0 | 15 | Structurally Inadequate | 1 | 6.0 |

After this group the corpus has 23 dominance pairs against 21 after 48.3 (new: CCO>DG, INT>CPS; lost: none), and its frontier holds 12 entries against 13 (NSD, MS, LM, UBI, FALC, PE, CCO, INT, MC, SWF, IF, OS). First place: CCO, 18.5 after 48.3, 18.0 now. Across the pass so far 138 units have been re-estimated, each counted once: 12 stand and 126 are at 0.5 (63.0 points).

Left for part (b): 8 D28 units (C5.2 4, C5.4 2, C5.5 2), which finish it.

Flags added in this group: 2; removed: 0. Flags added by the pass so far: 20 (against 18 before this group); removed: 7. Across the pass so far, 16 entries' flag registers change (CCO, CN, CPS, DG, IF, INT, LM, MC, NSD, OS, QA, SG, SQ, SWF, UBI, UBS).

After this group no entry scores 1.0 on C4.3 (7 published), and C4.5 keeps 2 (FALC, INT; 6 published). Every criterion had a 1.0 in the published corpus; after the pass so far no entry scores 1.0 on 9 of them: C1.1 (emptied in part (b3)), C2.1 (emptied in part (b4)), C2.3 (emptied in part (b1)), C2.4 (emptied in part (b1)), C3.1 (emptied in part (b2)), C3.5 (emptied in part (b6)), C4.1 (emptied in part (b6)), C4.2 (emptied in part (b7)), C4.3 (emptied in part (b8)).

Anchor examples citing a unit the pass moves: C1.1's 1.0 example, NSD (part (b3)); C2.1's 1.0 example, UBI (part (a)); C2.3's 1.0 example, DG (part (b1)); C2.4's 1.0 example, PE (part (b1)); C2.5's 1.0 example, CCO (part (b5)); C3.1's 1.0 example, UBI (part (b2)); C3.2's 1.0 example, PE (part (b4)); C3.5's 1.0 example, CCO (part (b6)); C4.1's 1.0 example, DG (part (b6)); C4.2's 1.0 example, PE (part (b7)); C4.3's 1.0 example, CCO (part (b8)); C5.1's 1.0 example, MS (part (b2)). Bands whose example the pass moves and which no corpus unit then scores at their value: C1.1's 1.0, C2.1's 1.0, C2.3's 1.0, C2.4's 1.0, C3.1's 1.0, C3.5's 1.0, C4.1's 1.0, C4.2's 1.0, C4.3's 1.0.

**The score ledger** (published total, each part's change, the total now; 26 criteria; the column (b8) is this record,
CCO-PTF-CIP-SZH's C4.3 included):

| Entry | Published | (a) | (b1) | (b2) | (b3) | (b4) | (b5) | (b6) | (b7) | 48.3 | (b8) | Now | Re-estimated | At 0.5 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| CCO | 24.5 | -0.5 | -1.5 | -0.5 | -0.5 | -0.5 | -0.5 | -1.0 | -0.5 | -0.5 | -0.5 | 18.0 | 14 | 13 |
| PE | 20.5 |  | -1.5 | -0.5 | -0.5 | -1.5 |  | -0.5 | -0.5 |  | -0.5 | 15.0 | 12 | 11 |
| NSD | 19.5 | -2.5 | -1.0 | -0.5 | -0.5 | -0.5 |  |  |  |  | -0.5 | 14.0 | 11 | 11 |
| INT | 19.5 | -0.5 | -1.0 | -0.5 |  | -1.0 | -0.5 | -1.0 | -0.5 |  |  | 14.5 | 12 | 10 |
| DG | 19.0 |  | -1.5 | -0.5 | -0.5 | -0.5 |  | -0.5 | -1.0 |  | -1.0 | 13.5 | 11 | 11 |
| MS | 16.5 | -1.0 | -1.5 | -0.5 | -0.5 |  |  |  | 0.5 |  |  | 13.5 | 8 | 6 |
| MMT | 15.5 | -1.5 | -1.0 | -0.5 | -0.5 |  |  |  |  |  | -0.5 | 11.5 | 8 | 8 |
| UBI | 14.5 | -1.5 | -0.5 | -0.5 | -0.5 |  |  |  |  |  | -0.5 | 11.0 | 8 | 7 |
| MC | 14.5 |  | -1.0 | -0.5 |  |  | -0.5 |  |  |  |  | 12.5 | 4 | 4 |
| OS | 14.5 | -0.5 |  |  |  |  | -0.5 | -0.5 |  |  |  | 13.0 | 4 | 3 |
| SWF | 14.0 |  |  | -0.5 |  |  | -0.5 | -0.5 |  |  |  | 12.5 | 4 | 3 |
| SG | 14.0 | -1.0 | -0.5 | -0.5 |  |  |  |  |  |  |  | 12.0 | 4 | 4 |
| GEO | 13.5 | -0.5 |  |  |  |  | -0.5 |  |  |  |  | 12.5 | 2 | 2 |
| UBS | 13.5 |  | -0.5 | -0.5 |  |  | -0.5 |  |  |  |  | 12.0 | 4 | 3 |
| IF | 13.5 | -1.0 |  |  |  |  | -0.5 |  |  |  |  | 12.0 | 3 | 3 |
| FALC | 13.0 | -0.5 | -0.5 |  | -0.5 | -1.0 |  | -0.5 | -0.5 |  |  | 9.5 | 8 | 7 |
| DE | 11.5 | -0.5 | -0.5 |  |  |  | -0.5 | -0.5 | -0.5 |  |  | 9.0 | 5 | 5 |
| SQ | 10.5 | -0.5 |  |  |  | -0.5 |  |  |  |  |  | 9.5 | 2 | 2 |
| CPS | 10.0 | -1.5 |  |  | -0.5 |  |  |  |  |  | -0.5 | 7.5 | 5 | 5 |
| SC | 10.0 |  | -1.0 |  |  |  |  |  |  |  |  | 9.0 | 2 | 2 |
| CN | 10.0 |  |  | -0.5 |  |  |  |  |  |  |  | 9.5 | 1 | 1 |
| QA | 9.0 | -0.5 |  | -0.5 |  |  |  |  |  |  |  | 8.0 | 2 | 2 |
| LM | 8.0 | -1.5 |  |  |  |  |  |  |  |  |  | 6.5 | 4 | 3 |

## 6. Corrections found (not polish)

None new. One recorded before is restated because this group bears on it: C4.5's 1.0 anchor cites Participatory
Economics, which the corpus scores 0.0 on C4.5, with a rationale that is Degrowth's (Handoff 30, item 5). Degrowth's
C4.5 falls here, so the band's text cannot simply be re-attributed; when the pass is applied, the band needs an
example the corpus then scores 1.0 on C4.5 (Fully Automated Luxury Communism or Integral).

## 7. Disclosure

The owner designed CCO-PTF-CIP-SZH. Its C4.3 falls here, from 1.0 to 0.5, on the readings that lower the six D28
units, and it is re-checked now rather than in stage 2 so that no unit of the owner's design is read more leniently
than its peers (reading 3.8). It keeps first place, at 18.0 on the 26 published criteria. Two flags are added, one
in each direction: Integral's C4.5 toward 0.5 and Degrowth's toward 1.0. Neither concerns the owner's design, and
Integral's would leave it at 14.0, level with Nordic Social Democracy.

## 8. What remains

Part (b) has 8 D28 units left: C5.2 (Nordic Social Democracy, Libertarian Minarchism, Stakeholder Capitalism, Islamic
Finance), C5.4 (Nordic Social Democracy, CCO-PTF-CIP-SZH) and C5.5 (Participatory Economics, Mutual Credit); they
finish it. The class M re-checks follow in stage 2. C4.3's other 16 units (its thirteen 0.5s and three 0.0s) are read on
readings 3.2 to 3.5, the four configured national economies whose C4.3 this group does not read (Status Quo, China,
Singapore, Qatar) on national household survey series as in reading 3.4. C4.4's seventeen units follow decision 48.3, and C4.1's four part (b6) units (FALC, PE, INT, SWF) turn on its debt clause.
C4.5's 0.5s and 0.0s are class D: a 0.5 whose only unshown clause was residual coercion rises.

## 9. What this record does not show

It re-estimates clauses on the evidence located in this session; it does not score the three new criteria, and it
changes no published figure. The Nordic figures are survey estimates with sampling error, which is why the rate is
measured two ways (reading 3.4); a register series could reopen the unit. The design sources searched are those
named in each clause's source; a projection published elsewhere could reopen a unit (readings 3.3, 3.5).
