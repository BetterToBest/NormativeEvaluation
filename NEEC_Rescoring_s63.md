# NEEC Rescoring Pass — Record, Stage 2, Group 2.9: C3.1 Crisis Response Capacity (class I)

**Session 63 · 2026-10-15 · Scorer and engineer: Claude · Owner: Duke Johnson**
**Status: scratch (protocol 10.1). Parts (a) and (b), groups 2.1 to 2.8 and part 58.1 are `NEEC_Rescoring_s37.md` to
`NEEC_Rescoring_s61.md` and `owner_s58.py`; this record edits none of them.** No corpus file, score or scoring document
changes until the pass ends. Its changes are then applied by generator with pinned inputs and restated in place
(protocol 10.2, 10.3; decisions D12, D14), and until then the published totals stand, provisional as `README.md` says.
Decisions taken here are Claude's under the owner's delegation (Handoff 35, section 2; decision 57.2: only
CCO-PTF-CIP-SZH's score changes wait on the owner, and none is made here); each is recorded with its reasons, and the
owner may reverse any of them.
**Reproduce:** `python3 rescoring_s63.py` (harness check 109). It is the third class I group, written on the shared
module (`pass_common.py`, decision 52.5): the script holds the 16 readings and the group's own checks, and the module
computes the consequences cumulatively with every part before it. It checks every cache file the readings use by digest,
finds every passage quoted in its file, recomputes every figure the readings quote, locates each unit's published
rationale where Session 62's index puts it and checks that it is unchanged, and checks that this record contains its
generated tables verbatim. It reads no network.

---

## 1. What this group is

The consequence triage (`triage_s52.py`, decision 52.7), rerun after group 2.8, put C3.1 first among the criteria still
to read: 16 units in play, three of them able to change an adequacy tier on their own. C3.1 is class I: v2.0 keeps its
three clauses and bar ("Response within 72 hours", "scaling 1:1 with crisis severity (30% GDP decline = 30% benefit
increase)", "≥90% population coverage") and names its measure (`criteria.json`; `NEEC_Criteria_v2_s45.md`): days from a
shock's trigger, the first official data showing it, to the first increased payment, with no legislative delay; the
percentage change in social benefits received by households (national accounts item D.62) against the percentage fall in
real GDP in that shock; and the share of the population covered by at least one social protection cash benefit (the ILO's
SDG indicator 1.3.1). For a design the clauses are read from its rules; for a configured national economy clause 1 is
read from the dated record of its response to its most recent major shock. Seven units were re-estimated earlier and are
not re-read: Nordic Social Democracy's and CCO-PTF-CIP-SZH's (part (a)) and MMT + Job Guarantee's, Universal Basic
Income's, Degrowth's, Participatory Economics' and Integral's (part (b2)), each from 1.0 to 0.5. The other 16 are read
clause by clause in the D28 form, from the evidence cache Session 62 built (`evidence_cache_s62.py`,
`evidence_cache/C3.1/`) and ten data files this session added to it (section 5): fourteen published 0.5s and two 0.0s.

**Outcome.** No unit clears all three clauses, so none can be 1.0, and after this group no entry is at 1.0 on C3.1.
**One unit rises**, Status Quo, from 0.0 to 0.5, a correction: on the measure v2.0 names its scaling clause is cleared
(the United States' social benefits rose 35.5% in 2020 against a 2.1% fall in real GDP) and its coverage is 11 points
short, and a unit with a cleared clause is not 0.0 under D28(f) and protocol 2.1 (reading 3.2). Fifteen hold, one of
them at 0.0 (Libertarian Minarchism). Net +0.5 points; Status Quo's rank moves from 17th to 16th, and no failure count
of another entry, no tier and no first place changes: first place stays shared by CCO-PTF-CIP-SZH and Integral at 14.5.
Three units are flagged toward 0.0 (Status Quo, Doughnut Economics, Qatar); no flag could change a tier.

## 2. How a clause is recorded, and the rule

As in groups 2.2 to 2.8 and decision 53.2: each clause is cleared, short, not shown, out of reach or moot. A unit is 1.0
only if every clause is cleared (D28, protocol 2.3); 0.0 only on one of protocol 2.1's whole-criterion conditions, stated
as the unit's reason and never with a clause cleared; 0.5 otherwise. A clause-level gap never makes 0.0 (D28(f)). "Not
shown" means that no estimate of the clause's quantity was located, not that the clause fails; "short" means the
evidence located falls below it. For a mechanism, a clause whose quantity it does not govern even when generalised is
out of reach, and the host economy's figure is not credited to it (protocol 3.2, D28(c)).

## 3. Decisions and readings (under the delegation)

**3.1 What the clauses ask, and what the measure counts (decision 63.1).** Clause 1 counts days from the first official
data showing a shock to the first increased payment, "no legislative delay (automatic activation based on triggers)": a
response that needs an Act is not within the clause, however fast the Act. Clause 2 compares two percentages, the change
in social benefits received by households and the fall in real GDP, and v2.0's text does not say that the increase must be
automatic: a discretionary increase counts toward it, and clause 1 is where automatism is tested. Clause 3 is the ILO's
coverage estimate. *Alternative weighed:* read clause 2 only on benefits that rise by rule. Not adopted: it adds a
condition v2.0 does not state, and it would make clause 2 repeat clause 1; the effect is the same on every verdict here,
since no unit that shows clause 2 shows clause 1. *The measure's sources.* The national accounts series for the
United States is the Bureau of Economic Analysis's government social benefits to persons (through FRED), which includes
Medicare and Medicaid; SNA item D.62 excludes benefits in kind, so the series is a proxy whose base is larger than
D.62's and which understates D.62's percentage rise. For the other economies no D.62 series was located (the OECD and
Eurostat pages carry no figures, section 5). The coverage figures are the ILO's SDG 1.3.1 estimates, read through the
UN Statistics Division's SDG API (series SI_COV_BENFTS), which serves the indicator the ILO's own pages (HTTP 403)
would. A design's coverage is read from its rules; a rule that pays every resident (the Georgist dividend, universal
services) is universal in form but is not a stated share, so the clause is "not shown" (reading 3.4).

**3.2 Status Quo, 0.0 → 0.5 (decision 63.2, a correction; flagged toward 0.0).** The published 0.0 rests on "three to six
months of legislative debate" (the Report's rationale, from the criterion's own comparison text) and on "no automatic
stabilizers scaling with crisis severity". On the measure, for the configuration's most recent major shock: clause 1 is
short, since the response was legislated and the increase in payments came in the weeks after the data (weekly initial
claims 273,000 in the week to 14 March 2020 and 2,914,000 in the week to 21 March; the Senate passed the CARES Act on 25
March, the House the next day, and the President signed it on 27 March, six days after the week of the jump; the monthly
series of benefits paid rose 2.7% in March and 97.8% in April). Clause 2 is cleared: government social benefits to
persons rose 35.5% from 2019 to 2020 against a 2.1% fall in real GDP, 17 times the fall. Clause 3 is short: 78.8% of the
population were covered in 2023 by at least one benefit. So the delay the rationale describes is not what the 2020
record shows (the Act was signed within a week of the jump, not months), clause 2 is cleared, and coverage is 11 points
from the bar. Under D28(f) and protocol 2.1 a unit with a cleared clause is not 0.0, and the evidence does not show a
response that is absent or far below the threshold with no pathway: it is the 0.5 band's "some crisis-responsive
capacity exists but is not automatic". The reading is a correction of the published score on the measure v2.0 names, as
group 2.8 corrected Status Quo's C4.3 downward on its measure. *Flag toward 0.0:* the 0.0 band read literally, response
that "requires legislative/political action": every increase in 2020 came by Act of Congress and the configuration's
rules raise no payment with the shock; the published rationale's months of delay refers to the response to the 2008
recession, which this record does not re-read. The flag could not change a tier (at 0.5 Status Quo has nine failures and at 0.0 ten; it is Structurally
Inadequate on either).

**3.3 The configured economies held: China, Singapore, Qatar (decision 63.3).** *China* holds at 0.5: the 2008 package was
decided on 5 November and announced on 9 November, without legislative delay, but it was discretionary and infrastructure-heavy,
no dated first payment to households is located, and coverage is 75.6% in 2021 (63.0% in 2015), 14 points short and rising
about 2 points a year. *Singapore* holds at 0.5: coverage is cleared (100% in 2019, 2020 and 2023), the response of 2020
was among the fastest and largest in the corpus, but each budget needed Parliament, so clause 1 is short, and no D.62 series
was located for clause 2. *Qatar* holds at 0.5 on the speed and size of a response that faces no legislative delay (the
emir holds legislative authority) and is flagged toward 0.0: coverage is 4.1% in 2022 (4.0% in 2018), 86 points short,
because non-citizens, most of the population, are outside social assistance and pensions, and on that figure the
allocation by nationality offers no pathway to the clause. The flag is not adopted as the verdict because the response
itself is fast and large and the 0.0 band describes a response that needs months of legislation or is opposed to
stabilization; it could not change a tier.

**3.4 The 0.5s held for designs and mechanisms (decision 63.4).** Eleven units hold at 0.5 and each names a genuine
capacity that is not shown at the clauses' levels, the 0.5 band's description. Three are mechanisms at the level of the
firm or bank, the band's own wording ("firm/local-level rather than system-wide"): Market Socialism (the band's anchor
example), Stakeholder Capitalism (the entry's text is the same, and the host economy's stabilizers are not credited to
it) and Islamic Finance (bank-level resilience, as its scoring document finds). Mutual Credit has the strongest evidence
for a firm-level stabilizer in the corpus (WIR's countercyclical circulation) and its coverage is far short. Georgism's
dividend is automatic, so it needs no legislation, but nothing raises it in a downturn, so its scaling is short.
Centrally Planned Socialism and Fully Automated Luxury Communism name a capacity to mobilise or respond without payment
rules; Universal Basic Services provides services that are in operation permanently, which the criterion's benefits
clause does not count (D.62 excludes benefits in kind); Sovereign Wealth Fund Statism's Norwegian escape clause is
statutory and was used at record scale, but it took roughly two months from the onset to the Revised Budget, and
Norway's 99.3% coverage is the welfare state's, not the fund's (protocol 3.2). Ostrom-style commons (reading 3.6) is
the eleventh. *Doughnut Economics* holds at 0.5 on its scoring document's finding of a real, rapid, local-level response
(Amsterdam's adoption in April 2020), and is flagged toward 0.0: the response is a framing and not a payment, and the
design supplies no mechanism that addresses any of the three clauses, the first condition of protocol 2.1, on which group
2.7 held the same design at 0.0 for C1.4.

**3.5 Libertarian Minarchism holds at 0.0 (decision 63.5).** The design is "ideologically opposed to stabilization
mechanisms": no unemployment insurance, no disaster relief, no crisis intervention. No clause is cleared and the design
has no mechanism that addresses the criterion: protocol 2.1's whole-criterion condition. It is the 0.0 band's anchor
example, and after this group the only unit scoring 0.0 on C3.1.

**3.6 Ostrom-style commons: the scope scenario kept.** The scoring document reports, as a scenario and not a flag (decision
D18(b)), that reading clause 3 against the population the institution governs raises the unit to 1.0. That applies the
threshold to a population other than the one the declared population rule fixes, and it would still leave clause 1
(no day count located) and clause 2 (no change in benefits against output) not shown, so the scenario would not raise
the unit under D28 even if adopted. The published treatment stands.

**3.7 The evidence.** Session 62's cache holds the 16 published rationales by location and digest and the pages of the
sources the measure names (the IMF fiscal-measures page, the Eurostat and World Bank pages for national accounts, the
World Bank and UN SDG pages for coverage). None of them carries a figure, and the ILO database refused the container
(HTTP 403). This session added the figures (section 5). Six rationales are the Report v1.6's one-paragraph entries
(Status Quo, Centrally Planned Socialism, Market Socialism, Libertarian Minarchism, Stakeholder Capitalism and Fully
Automated Luxury Communism); none cites a source, so they are read from what they say.

## 4. The units

### 4.1 Summary (generated)

| Entry | Published | Response time | Scaling | Coverage | Verdict | Flag |
|---|---:|---|---|---|---:|---|
| SQ | 0.0 | short | cleared | short | 0.5 | toward 0.0 |
| CPS | 0.5 | not shown | not shown | not shown | 0.5 |  |
| MS | 0.5 | not shown | out of reach | out of reach | 0.5 |  |
| LM | 0.0 | short | short | short | 0.0 |  |
| SC | 0.5 | not shown | out of reach | out of reach | 0.5 |  |
| FALC | 0.5 | not shown | not shown | not shown | 0.5 |  |
| GEO | 0.5 | not shown | short | not shown | 0.5 |  |
| MC | 0.5 | not shown | out of reach | short | 0.5 |  |
| DE | 0.5 | not shown | out of reach | out of reach | 0.5 | toward 0.0 |
| UBS | 0.5 | not shown | not shown | not shown | 0.5 |  |
| SWF | 0.5 | short | not shown | not shown | 0.5 |  |
| CN | 0.5 | not shown | not shown | short | 0.5 |  |
| SG | 0.5 | short | not shown | cleared | 0.5 |  |
| QA | 0.5 | not shown | not shown | short | 0.5 | toward 0.0 |
| IF | 0.5 | not shown | out of reach | out of reach | 0.5 |  |
| OS | 0.5 | not shown | not shown | short | 0.5 |  |

### 4.2 Clause by clause (generated)

#### SQ C3.1 Crisis Response Capacity: 0.0 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Response within 72 hours | short | the response was legislated, not triggered by rule: the weekly initial-claims series rose from 273,000 (week to 14 March 2020) to 2,914,000 (week to 21 March), the Senate passed the CARES Act on 25 March and the House on 26 March, and the President signed it on 27 March, six days after the week the claims jumped; the monthly series of benefits paid rose +2.7% in March and +97.8% in April (3,151.2, 3,235.1, 6,397.7 billion at annual rates in February, March and April), so the first large increase in payments came in April; not 72 hours, and not free of legislation (reading 3.2) | FRED: A063RC1 (monthly, seasonally adjusted annual rates) and ICSA (initial claims, weekly), retrieved 2026-10-15 (evidence_cache/C3.1/fred_benefits_monthly.csv, fred_claims_weekly.csv); evidence_cache/C3.1/cares_act_wikipedia_lead.txt (the Act's date of signature); Report v1.6, SQ C3.1 |
| 2 | scaling 1:1 with crisis severity (30% GDP decline = 30% benefit increase) | cleared | in 2020 government social benefits to persons rose 35.5% (3,090.8 to 4,187.5 billion dollars) while real GDP fell 2.1% (20,715.7 to 20,284.5 billion, chained 2017 dollars), 17.0 times the fall, far above 1:1; the series is the national accounts' government social benefits to persons, which includes Medicare and Medicaid; SNA item D.62 excludes benefits in kind, so the series is a proxy for it, and a proxy whose base is larger than D.62's, so that it understates the percentage rise in D.62; the increase was legislated, which clause 1 and not this clause counts (reading 3.2) | U.S. Bureau of Economic Analysis through FRED: A063RC1A027NBEA (government social benefits to persons, billions of dollars, annual) and GDPCA (real gross domestic product, billions of chained 2017 dollars, annual), retrieved 2026-10-15 (evidence_cache/C3.1/fred_benefits_annual.csv, fred_realgdp_annual.csv) |
| 3 | ≥90% population coverage | short | 78.8% of the population covered by at least one benefit in 2023 (76.1% in 2015), against 90%: short, by 11 points (reading 3.2) | UN Statistics Division, SDG indicator database, series SI_COV_BENFTS (SDG 1.3.1, population covered by at least one social protection benefit), source ILO - Social Security Inquiry Database, estimated data, both sexes (evidence_cache/C3.1/sdg131_840.json) |

*Flag (reading 3.2):* toward 0.0: reading the 0.0 band literally, response that 'requires legislative/political action': every increase in 2020 came by Act of Congress, the configuration's rules raise no payment with the shock, and the published rationale's months of delay refers to the response to the 2008 recession, which this record does not re-read.

*Note:* a correction (reading 3.2): the published 0.0 rests on 'three to six months of legislative debate', which the 2020 record does not show (the Act was signed six days after the week of the claims jump), and on no automatic stabilizers scaling with severity; on the measure v2.0 names clause 2 is cleared and clause 3 is 11 points short, and under D28(f) and protocol 2.1 a unit with a cleared clause is not 0.0; the 0.0 band's own example, now held by Libertarian Minarchism alone.

#### CPS C3.1 Crisis Response Capacity: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Response within 72 hours | not shown | the command economy could mobilise resources rapidly in WWII and disasters, by the entry's own account, without legislative delay; no payment rule, trigger or day count is stated; the unit is a mechanism or a design whose rules state no payment that rises with a shock, no trigger and no number of days | Report v1.6, CPS C3.1 |
| 2 | scaling 1:1 with crisis severity (30% GDP decline = 30% benefit increase) | not shown | chronic shortages meant perpetual intervention, not a payment that scales with a shock; no estimate of benefits against a fall in output is stated or located | Report v1.6, CPS C3.1 |
| 3 | ≥90% population coverage | not shown | employment is guaranteed by design, but no share of the population covered by a cash benefit is stated or located | Report v1.6, CPS C3.1 |

*Note:* 0.5 holds: a genuine capacity to mobilise without legislative delay, not shown at the clauses' levels, the 0.5 band's description (reading 3.4).

#### MS C3.1 Crisis Response Capacity: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Response within 72 hours | not shown | cooperatives retain workers in a recession (layoff rates four to five times lower, by the entry); no payment, trigger or day count at the level of the system | Report v1.6, MS C3.1 |
| 2 | scaling 1:1 with crisis severity (30% GDP decline = 30% benefit increase) | out of reach | firm-level resilience governs no social benefit; the entry's own finding is that it 'doesn't translate to system-level response' | Report v1.6, MS C3.1 |
| 3 | ≥90% population coverage | out of reach | a firm-level mechanism reaches the members of the firms that adopt it, not the population; the economy's coverage is not credited to it (protocol 3.2) | Report v1.6, MS C3.1 |

*Note:* 0.5 holds: the 0.5 band's own anchor example, 'firm-level resilience doesn't translate to system-level response' (reading 3.4).

#### LM C3.1 Crisis Response Capacity: 0.0 → 0.0

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Response within 72 hours | short | the design's functions exclude any crisis payment: no unemployment insurance, no disaster relief, no crisis intervention | Report v1.6, LM C3.1 |
| 2 | scaling 1:1 with crisis severity (30% GDP decline = 30% benefit increase) | short | no benefit exists to scale; markets are 'expected to self-correct while populations suffer' | Report v1.6, LM C3.1 |
| 3 | ≥90% population coverage | short | no cash benefit is paid, so coverage by one is nil by the design's rules | Report v1.6, LM C3.1 |

*0.0 (protocol 2.1):* the system is ideologically opposed to the criterion (the 0.0 band's second description) and has no mechanism that addresses it (protocol 2.1): the minimal state's functions rule out every stabilizing flow.

*Note:* 0.0 holds; the 0.0 band's example, 'ideologically opposed to stabilization mechanisms' (reading 3.5).

#### SC C3.1 Crisis Response Capacity: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Response within 72 hours | not shown | stakeholder commitment could mean retaining workers rather than laying them off; no payment, trigger or day count at the level of the system; the host economy's institutions are not credited to the mechanism (protocol 3.2) | Report v1.6, SC C3.1 |
| 2 | scaling 1:1 with crisis severity (30% GDP decline = 30% benefit increase) | out of reach | firm-level improvements govern no social benefit; the entry's own finding is that they do not translate to system-level crisis response; the host economy's institutions are not credited to the mechanism (protocol 3.2) | Report v1.6, SC C3.1 |
| 3 | ≥90% population coverage | out of reach | a firm-level mechanism does not reach the population; the host economy's institutions are not credited to the mechanism (protocol 3.2) | Report v1.6, SC C3.1 |

*Note:* 0.5 holds, as Market Socialism's, the entry's text being the same (reading 3.4).

#### FALC C3.1 Crisis Response Capacity: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Response within 72 hours | not shown | automated production could respond rapidly to a crisis, by the entry; no payment, trigger or day count is stated | Report v1.6, FALC C3.1 |
| 2 | scaling 1:1 with crisis severity (30% GDP decline = 30% benefit increase) | not shown | universal provision is not a benefit that scales with a fall in output; the entry's concern is technical failure, not scaling | Report v1.6, FALC C3.1 |
| 3 | ≥90% population coverage | not shown | abundance is meant for everyone, but no share of the population covered by a cash benefit is stated | Report v1.6, FALC C3.1 |

*Note:* 0.5 holds (reading 3.4).

#### GEO C3.1 Crisis Response Capacity: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Response within 72 hours | not shown | the Citizen's Dividend would be an automatic annual or more frequent payment that continues without a fresh legislative vote, as Alaska's does, so it needs no legislative delay; no payment rises with the shock, so no response time can be counted | NEEC_Georgism_LVT_scoring_scratch.md, C3.1 |
| 2 | scaling 1:1 with crisis severity (30% GDP decline = 30% benefit increase) | short | nothing in the design raises the dividend in a downturn; land-value revenue is prized for its stability across the cycle, so the payment does not scale with the fall in output | NEEC_Georgism_LVT_scoring_scratch.md, C3.1 |
| 3 | ≥90% population coverage | not shown | a universal flat payment reaches every resident in form, but no source states a share of the population covered | NEEC_Georgism_LVT_scoring_scratch.md, C3.1 |

*Note:* 0.5 holds: automatic continuity is real, automatic crisis-scaling is not part of the design (reading 3.4).

#### MC C3.1 Crisis Response Capacity: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Response within 72 hours | not shown | WIR credit circulation moves countercyclically (a 2009 study), Sardex was founded in response to the credit crunch, and Argentina's Redes de Trueque grew to several million participants in 2001 and 2002; no day count between a shock and a response is located | NEEC_MutualCredit_LETS_scoring_scratch.md, C3.1 |
| 2 | scaling 1:1 with crisis severity (30% GDP decline = 30% benefit increase) | out of reach | mutual credit is not a social benefit; the countercyclical credit is a liquidity buffer for member firms | NEEC_MutualCredit_LETS_scoring_scratch.md, C3.1 |
| 3 | ≥90% population coverage | short | self-selected networks of businesses, and a mobilisation that was 'neither universal nor centrally triggered'; far below 90% of the population | NEEC_MutualCredit_LETS_scoring_scratch.md, C3.1 |

*Note:* 0.5 holds: the strongest peer-reviewed evidence in the corpus for a firm-level stabilizer, the 0.5 band's description (reading 3.4).

#### DE C3.1 Crisis Response Capacity: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Response within 72 hours | not shown | the model has no trigger-based disbursement; Amsterdam adopted it as a recovery strategy in April 2020, within weeks of the pandemic's onset, a response in policy framing and not a payment | NEEC_DoughnutEconomics_scoring_scratch.md, C3.1 |
| 2 | scaling 1:1 with crisis severity (30% GDP decline = 30% benefit increase) | out of reach | the model governs no benefit that could scale with a fall in output | NEEC_DoughnutEconomics_scoring_scratch.md, C3.1 |
| 3 | ≥90% population coverage | out of reach | the model governs no cash benefit, so the share of a population covered by one is not a quantity it fixes | NEEC_DoughnutEconomics_scoring_scratch.md, C3.1 |

*Flag (reading 3.4):* toward 0.0: counting a single city's recovery framing as a crisis-response capacity at all, when the design supplies no mechanism that addresses any of the three clauses (protocol 2.1's first condition, as group 2.7 read it for the same design on C1.4).

*Note:* 0.5 holds on its scoring document's finding of a real, rapid, local-level response (the 0.5 band's 'local-level rather than system-wide'), flagged toward 0.0 (reading 3.4).

#### UBS C3.1 Crisis Response Capacity: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Response within 72 hours | not shown | services that run as a universal default need no activation in a crisis, since the 'trigger' fired when the service became universal; no payment rises with the shock, so no response time is counted | NEEC_UniversalBasicServices_scoring_scratch.md, C3.1 |
| 2 | scaling 1:1 with crisis severity (30% GDP decline = 30% benefit increase) | not shown | there is no automatic benefit-scaling mechanism; government final consumption in kind is outside D.62, which counts benefits in cash | NEEC_UniversalBasicServices_scoring_scratch.md, C3.1 |
| 3 | ≥90% population coverage | not shown | universal provision covers every resident in form; no source states the share covered by a cash benefit | NEEC_UniversalBasicServices_scoring_scratch.md, C3.1 |

*Note:* 0.5 holds: a structural advantage of a different kind (permanent operation), with indirect evidence from the pandemic's essential-worker designations (reading 3.4).

#### SWF C3.1 Crisis Response Capacity: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Response within 72 hours | short | Norway's fiscal rule has a statutory escape clause for withdrawals 'to counteract economic setbacks', used at record scale in 2020; the response took roughly two months from the pandemic's onset to the Revised Budget of May 2020, set in a budget, not by a payment rule | NEEC_SovereignWealthFundStatism_scoring_scratch.md, C3.1 |
| 2 | scaling 1:1 with crisis severity (30% GDP decline = 30% benefit increase) | not shown | a 382-billion-kroner withdrawal (4.2% of the fund) scales at the level of the national budget, not at the household level, and no change in benefits against a fall in output is stated | NEEC_SovereignWealthFundStatism_scoring_scratch.md, C3.1 |
| 3 | ≥90% population coverage | not shown | Norway's welfare state covers 99.3% of its population in 2023 on the ILO's measure, but that is the host economy's, not the fund's (protocol 3.2); no share is stated for the fund's own payment (UN Statistics Division, SDG indicator database, series SI_COV_BENFTS (SDG 1.3.1, population covered by at least one social protection benefit), source ILO - Social Security Inquiry Database, estimated data, both sexes (evidence_cache/C3.1/sdg131_578.json)) | NEEC_SovereignWealthFundStatism_scoring_scratch.md, C3.1 |

*Note:* 0.5 holds: real, rule-supported, demonstrated countercyclical capacity, budget-cycle in speed (reading 3.4).

#### CN C3.1 Crisis Response Capacity: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Response within 72 hours | not shown | the State Council decided on its 4-trillion-yuan stimulus on 5 November 2008 and announced it on 9 November, without legislative delay, but the package was infrastructure-heavy and discretionary; no dated first payment to households is located for either shock | NEEC_StateCapitalism_China_scoring_scratch.md, C3.1 |
| 2 | scaling 1:1 with crisis severity (30% GDP decline = 30% benefit increase) | not shown | no series of household benefits against real GDP is located for the 2008 or the 2020 shock | NEEC_StateCapitalism_China_scoring_scratch.md, C3.1 |
| 3 | ≥90% population coverage | short | 75.6% of the population covered by at least one benefit in 2021 (63.0% in 2015, 70.8% in 2019), against 90%: short, and rising 12.6 points in six years | UN Statistics Division, SDG indicator database, series SI_COV_BENFTS (SDG 1.3.1, population covered by at least one social protection benefit), source ILO - Social Security Inquiry Database, estimated data, both sexes (evidence_cache/C3.1/sdg131_156.json) |

*Note:* 0.5 holds: fast, large, discretionary mobilisation without legislative delay, neither automatic nor household-level, and 14 points short on coverage (reading 3.3).

#### SG C3.1 Crisis Response Capacity: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Response within 72 hours | short | three budget packages in about two months in 2020, each needing a budget in Parliament and, for reserve draws, the President's assent; wage support covered local workers; discretionary, so not within 72 hours or free of legislation | NEEC_StateCapitalism_Singapore_scoring_scratch.md, C3.1 |
| 2 | scaling 1:1 with crisis severity (30% GDP decline = 30% benefit increase) | not shown | the Jobs Support Scheme raised its wage subsidy from 25% to 75%, a subsidy to employers, not a change in household benefits against a fall in real GDP (5.4% in 2020); no D.62 series is located | NEEC_StateCapitalism_Singapore_scoring_scratch.md, C3.1 |
| 3 | ≥90% population coverage | cleared | 100.0% of the population covered by at least one benefit in 2019, 2020 and 2023 on the ILO's measure | UN Statistics Division, SDG indicator database, series SI_COV_BENFTS (SDG 1.3.1, population covered by at least one social protection benefit), source ILO - Social Security Inquiry Database, estimated data, both sexes (evidence_cache/C3.1/sdg131_702.json) |

*Note:* 0.5 holds: coverage cleared, the response among the fastest and largest in the corpus but discretionary (reading 3.3).

#### QA C3.1 Crisis Response Capacity: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Response within 72 hours | not shown | the QR 75 billion package of March 2020 and the suspension of customs duties came without legislative delay, because the emir holds legislative authority, but they are discretionary and mostly to firms and banks; no dated first payment to households is located | NEEC_StateCapitalism_Qatar_scoring_scratch.md, C3.1 |
| 2 | scaling 1:1 with crisis severity (30% GDP decline = 30% benefit increase) | not shown | no series of household benefits against real GDP is located; the 2026 record shows spending falling 3.7% in the first quarter | NEEC_StateCapitalism_Qatar_scoring_scratch.md, C3.1 |
| 3 | ≥90% population coverage | short | 4.1% of the population covered by at least one benefit in 2022 (4.0% in 2018), against 90%: non-citizens, most of the population, are outside social assistance and pensions | UN Statistics Division, SDG indicator database, series SI_COV_BENFTS (SDG 1.3.1, population covered by at least one social protection benefit), source ILO - Social Security Inquiry Database, estimated data, both sexes (evidence_cache/C3.1/sdg131_634.json) |

*Flag (reading 3.3):* toward 0.0: reading coverage at 4% of the population, 86 points below the bar, with benefits allocated by nationality, as a system whose own logic offers no pathway to the clause (protocol 2.1).

*Note:* 0.5 holds on the speed and size of the discretionary response, flagged toward 0.0 on coverage (reading 3.3).

#### IF C3.1 Crisis Response Capacity: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Response within 72 hours | not shown | the resilience is a property of banks' business model, not a trigger-based payment; no day count is located | NEEC_IslamicFinance_scoring_scratch.md, C3.1 |
| 2 | scaling 1:1 with crisis severity (30% GDP decline = 30% benefit increase) | out of reach | the mechanism governs no social benefit; the host economy's institutions are not credited to the mechanism (protocol 3.2) | NEEC_IslamicFinance_scoring_scratch.md, C3.1 |
| 3 | ≥90% population coverage | out of reach | a bank-level property does not reach the population; the host economy's institutions are not credited to the mechanism (protocol 3.2) | NEEC_IslamicFinance_scoring_scratch.md, C3.1 |

*Note:* 0.5 holds: the 0.5 band's 'firm-level rather than system-wide', as its scoring document finds; its H.7 home is Market Socialism's (reading 3.4).

#### OS C3.1 Crisis Response Capacity: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Response within 72 hours | not shown | the Taos Valley acequias' rule changes in scarcity so that every member has enough to survive, automatic and rule-based, no legislation, centuries old; no day count from a trigger is located | NEEC_Ostrom_Commons_scoring_scratch.md, C3.1 |
| 2 | scaling 1:1 with crisis severity (30% GDP decline = 30% benefit increase) | not shown | the scarcity rule scales access to the resource with severity, within the resource the commons governs; no change in benefits against a fall in real GDP is stated | NEEC_Ostrom_Commons_scoring_scratch.md, C3.1 |
| 3 | ≥90% population coverage | short | 90% of a population is unreachable for a bounded local institution, and it provides no crisis instrument outside the resource it governs | NEEC_Ostrom_Commons_scoring_scratch.md, C3.1 |

*Note:* 0.5 holds; the scoring document's scope scenario (D18(b): coverage read against the population the institution governs, which would raise the unit to 1.0) is a scenario and not a flag, and is kept as published (reading 3.6).

## 5. The sources added to the evidence cache

Written on 2026-10-15 by `evidence_cache_s63.py` (which holds each file's md5 and fetches with `--fetch`). The four FRED
files are the Bureau of Economic Analysis's series A063RC1A027NBEA (government social benefits to persons, annual),
GDPCA (real GDP, annual), A063RC1 (benefits, monthly, October 2019 to December 2020) and the Department of Labor's ICSA
(weekly initial claims, 15 February to 10 May 2020). The five `sdg131_<area>.json` files are the UN Statistics Division's
SDG API's responses for series SI_COV_BENFTS, areas 840 (United States), 156 (China), 702 (Singapore), 634 (Qatar) and
578 (Norway), whose source field reads "ILO - Social Security Inquiry Database". `cares_act_wikipedia_lead.txt` is the
first 1,400 characters of the English Wikipedia article on the CARES Act (the date of signature and of the votes); the
article is a secondary source, used only for those dates. The script checks each file's md5 and finds each quoted passage.
The OECD national accounts pages were not tried, and the ILO's own pages are not needed. Session 62's files and index are
unchanged. No D.62 series for China, Singapore, Qatar or Norway, and no dated first payment of a household benefit for
China, Singapore or Qatar, was located; clauses 1 and 2 for those economies are therefore "not shown" or rest on the
rationale's own dates.

## 6. What parts (a), (b), groups 2.1 to 2.8 and part 58.1 change (generated)

| Entry | Published (rank) | After group 2.8 (rank) | After group 2.9 (rank) | Change here | Failures | Tier |
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
| FALC | 13.0 (16) | 9.0 (17) | 9.0 (18) | 0.0 | 10 | Structurally Inadequate |
| DE | 11.5 (17) | 9.0 (17) | 9.0 (18) | 0.0 | 8 | Structurally Inadequate |
| SQ | 10.5 (18) | 9.0 (17) | 9.5 (16) | 0.5 | 9 | Structurally Inadequate |
| CPS | 10.0 (19) | 7.5 (22) | 7.5 (22) | 0.0 | 12 | Structurally Inadequate |
| SC | 10.0 (19) | 9.0 (17) | 9.0 (18) | 0.0 | 8 | Structurally Inadequate |
| CN | 10.0 (19) | 9.5 (16) | 9.5 (16) | 0.0 | 8 | Structurally Inadequate |
| QA | 9.0 (22) | 8.5 (21) | 8.5 (21) | 0.0 | 9 | Structurally Inadequate |
| LM | 8.0 (23) | 7.0 (23) | 7.0 (23) | 0.0 | 13 | Structurally Inadequate |

After this group the corpus has 17 dominance pairs against 17 after group 2.8 (new: none; lost: none), and its frontier holds 15 entries against 15 (SQ, NSD, CPS, MS, LM, UBI, DG, FALC, PE, CCO, INT, MC, SWF, IF, OS). First place is shared by CCO and INT at 14.5 (CCO 14.5, INT 14.5 after group 2.8), ahead of PE at 14.0. Across the pass so far 283 units have been re-estimated, each counted once: 18 are at 1.0, 236 at 0.5 and 29 at 0.0; against their published scores 149 fell, 8 rose and 126 are unchanged (net -70.5 points).

Anchor examples citing a unit the pass moves: C1.1's 1.0 example, NSD (part (b3)); C1.2a's 1.0 example, MS (part (2.2)); C1.2b's 1.0 example, CCO (part (2.5)); C1.4's 1.0 example, CCO (part (2.5)); C2.1's 1.0 example, UBI (part (a)); C2.3's 1.0 example, DG (part (b1)); C2.4's 1.0 example, PE (part (b1)); C2.5's 1.0 example, CCO (part (b5)); C3.1's 1.0 example, UBI (part (b2)); C3.1's 0.0 example, SQ (part (2.9)); C3.2's 1.0 example, PE (part (b4)); C3.5's 1.0 example, CCO (part (b6)); C3.5's 0.0 example, LM (part (2.4)); C3.5's 0.0 example, SC (part (2.4)); C4.1's 1.0 example, DG (part (b6)); C4.2's 1.0 example, PE (part (b7)); C4.3's 1.0 example, CCO (part (b8)); C5.1's 1.0 example, MS (part (b2)); C5.2's 1.0 example, CCO (part (b9)); C5.2's 0.0 example, INT (part (2.6)); C5.4's 1.0 example, CCO (part (b9)); C5.5's 1.0 example, PE (part (b9)). Bands whose example the pass moves and which no corpus unit then scores at their value: C1.1's 1.0, C1.2a's 1.0, C1.4's 1.0, C2.1's 1.0, C2.3's 1.0, C2.4's 1.0, C3.1's 1.0, C3.5's 1.0, C4.1's 1.0, C4.2's 1.0, C4.3's 1.0.

C3.1's published anchors: Universal Basic Income at 1.0 (moved to 0.5 by part (b2)), Market Socialism at 0.5 (holds) and
Status Quo at 0.0 (moved to 0.5 by this group, flagged toward 0.0); Libertarian Minarchism, cited at 0.0 in the band's
text, holds. After this group no corpus unit is at 1.0 on C3.1; stage 3's restatement of the criterion's anchors drops the
1.0 band's example and replaces the 0.0 band's Status Quo example with Libertarian Minarchism, as C1.1's and C1.2a's 1.0
examples were dropped.

| Entry | Published | (a) | (b1) | (b2) | (b3) | (b4) | (b5) | (b6) | (b7) | 48.3 | (b8) | (b9) | (2.1) | (2.2) | (2.3) | (2.4) | (2.5) | 58.1 | (2.6) | (2.7) | (2.8) | (2.9) | Now | Re-estimated | At 0.5 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| CCO | 24.5 | -0.5 | -1.5 | -0.5 | -0.5 | -0.5 | -0.5 | -1.0 | -0.5 | -0.5 | -0.5 | -1.0 | -1.5 | -0.5 | -0.5 |  | -0.5 | 0.5 |  |  |  |  | 14.5 | 22 | 20 |
| PE | 20.5 |  | -1.5 | -0.5 | -0.5 | -1.5 |  | -0.5 | -0.5 |  | -0.5 | -0.5 |  |  | -0.5 |  |  |  |  |  |  |  | 14.0 | 17 | 16 |
| NSD | 19.5 | -2.5 | -1.0 | -0.5 | -0.5 | -0.5 |  |  |  |  | -0.5 | -0.5 |  | -0.5 |  | 0.5 |  |  |  |  |  |  | 13.5 | 16 | 15 |
| INT | 19.5 | -0.5 | -1.0 | -0.5 |  | -1.0 | -0.5 | -1.0 | -0.5 |  |  |  |  |  | -0.5 |  |  |  | 0.5 |  |  |  | 14.5 | 17 | 14 |
| DG | 19.0 |  | -1.5 | -0.5 | -0.5 | -0.5 |  | -0.5 | -1.0 |  | -1.0 |  |  |  | -0.5 |  |  |  |  |  |  |  | 13.0 | 16 | 16 |
| MS | 16.5 | -1.0 | -1.5 | -0.5 | -0.5 |  |  |  | 0.5 |  |  |  |  | -0.5 |  |  |  |  |  |  |  |  | 13.0 | 15 | 13 |
| MMT | 15.5 | -1.5 | -1.0 | -0.5 | -0.5 |  |  |  |  |  | -0.5 |  |  | -0.5 |  |  |  |  |  |  |  |  | 11.0 | 11 | 9 |
| UBI | 14.5 | -1.5 | -0.5 | -0.5 | -0.5 |  |  |  |  |  | -0.5 |  |  |  |  |  |  |  |  | -0.5 |  |  | 10.5 | 13 | 10 |
| MC | 14.5 |  | -1.0 | -0.5 |  |  | -0.5 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 12.5 | 12 | 9 |
| OS | 14.5 | -0.5 |  |  |  |  | -0.5 | -0.5 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 13.0 | 11 | 9 |
| SWF | 14.0 |  |  | -0.5 |  |  | -0.5 | -0.5 |  |  |  |  |  |  |  |  |  |  | 0.5 |  |  |  | 13.0 | 11 | 8 |
| SG | 14.0 | -1.0 | -0.5 | -0.5 |  |  |  |  |  |  |  |  |  | -0.5 |  |  |  |  |  |  |  |  | 11.5 | 10 | 10 |
| GEO | 13.5 | -0.5 |  |  |  |  | -0.5 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 12.5 | 9 | 8 |
| UBS | 13.5 |  | -0.5 | -0.5 |  |  | -0.5 |  |  |  |  |  |  |  |  | -0.5 |  |  |  |  |  |  | 11.5 | 11 | 8 |
| IF | 13.5 | -1.0 |  |  |  |  | -0.5 |  |  |  |  | -0.5 |  |  |  |  |  |  |  |  |  |  | 11.5 | 10 | 9 |
| FALC | 13.0 | -0.5 | -0.5 |  | -0.5 | -1.0 |  | -0.5 | -0.5 |  |  |  |  |  | -0.5 |  |  |  |  |  |  |  | 9.0 | 14 | 11 |
| DE | 11.5 | -0.5 | -0.5 |  |  |  | -0.5 | -0.5 | -0.5 |  |  |  |  |  |  |  |  |  |  |  |  |  | 9.0 | 12 | 10 |
| SQ | 10.5 | -0.5 |  |  |  | -0.5 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | -0.5 | 0.5 | 9.5 | 9 | 6 |
| CPS | 10.0 | -1.5 |  |  | -0.5 |  |  |  |  |  | -0.5 |  |  |  |  |  |  |  |  |  |  |  | 7.5 | 10 | 7 |
| SC | 10.0 |  | -1.0 |  |  |  |  |  |  |  |  | -0.5 |  |  |  | 0.5 |  |  |  |  |  |  | 9.0 | 9 | 8 |
| CN | 10.0 |  |  | -0.5 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 9.5 | 8 | 6 |
| QA | 9.0 | -0.5 |  | -0.5 |  |  |  |  |  |  |  |  |  |  |  | 0.5 |  |  |  |  |  |  | 8.5 | 9 | 8 |
| LM | 8.0 | -1.5 |  |  |  |  |  |  |  |  |  | -0.5 |  | 0.5 |  | 0.5 |  |  |  |  |  |  | 7.0 | 11 | 6 |

## 7. Corrections found (not polish)

1. **Status Quo's C3.1, 0.0 → 0.5** (reading 3.2): the published 0.0 rests on months of legislative delay and no scaling;
   on the measure v2.0 names, scaling is cleared and the Act was signed within a week of the claims jump. Flagged toward
   0.0.
2. **Status Quo's C3.1 rationale** describes "3-6 months of legislative debate" as the characteristic delay; for the 2020
   shock the dated record shows days (reading 3.2). Report v2.0 states the measure's reading and both flags.
3. **The criterion's measure for clause 2 does not distinguish automatic from discretionary increases** (reading 3.1); an
   economy can clear clause 2 by legislated transfers, which clause 1 then counts against. Report v2.0 and the criteria
   record's next amendment state it.
4. **Qatar's and Doughnut Economics' C3.1** are flagged toward 0.0 (readings 3.3 and 3.4); neither flag could change a
   tier.

## 8. Disclosure

CCO-PTF-CIP-SZH is the owner's design. Its C3.1 unit was read in part (a) and is not re-read; this group changes none of
its scores. First place stays shared at 14.5 by CCO-PTF-CIP-SZH and Integral; Integral's C3.1 unit was read in part (b2).
Every reading here was made before the consequences table was computed. The session ran on Sonnet 5.5, not on the Opus
5.5 at high that `STATE.md`'s routing assigns judgment groups; the owner may wish to have the readings that carry
judgment (Status Quo's correction, the two flags and Libertarian Minarchism's hold) read again in an Opus session.

## 9. What remains

- **Next group from the triage** (rerun after this group, `triage_s52_output.txt`): C4.2 Ecological Compliance, class M
  (16 units in play, 3 tier-capable), a judgment re-read with no cache needed. Then C1.1, C4.1, C2.1, C2.4, C2.3, C4.4,
  C4.5, C2.5 and C3.4. The units that alone could change who is first are six (NSD C2.5, PE C2.5, PE C4.5, CCO C4.5,
  INT C1.1, INT C3.4); the units that could change no failure count, tier or rank on their own are seven.
- **`evidence_cache_s62.py`'s check [2]** compares the units in play *now* with its index, so it reports a failure once
  this group is part of the pass; its digest checks still pass. It is not a harness check and is not edited here.
- **For the criteria record's next amendment:** decision 63.1 (what clause 2 counts), and C3.1's anchors (section 6).
- **For Report v2.0:** section 7's corrections.
- **Sources a later session could add:** a D.62 series for China, Singapore and Qatar from their statistics offices;
  the IMF's country-by-country fiscal-measures database, which is script-rendered and was not read; dated first
  payments of the 2020 household measures of the three economies.

## 10. What this record does not show

C3.1's clause 1 is read for one economy (the United States) from the weekly claims, the monthly benefits series and the
date of an Act, not from the IMF's database, which the container could read only as a page; the first increased payment
is therefore dated to the month, not the day. Clause 2 is computed for one economy only, on a proxy for D.62. The ILO's
coverage figures are estimates (nature "E"), and Singapore's 100% and Norway's 99.3% are the ILO's, not checked against
national sources. "Not shown" means that no estimate was located, not that the clause fails. The interpretation check
(decisions 50.1 to 50.4) was not run; it is optional. The record is one scorer's re-estimation; whether its calls
reproduce is what the replication programme tests.
