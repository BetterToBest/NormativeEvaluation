# NEEC Rescoring Pass — Record, Stage 2, Group 2.4: C3.5 Failure-Mode Transparency (class I)

**Session 56 · 2026-10-14 · Scorer and engineer: Claude · Owner: Duke Johnson**
**Status: scratch (protocol 10.1). Parts (a) and (b) and groups 2.1 to 2.3 are `NEEC_Rescoring_s37.md` to
`NEEC_Rescoring_s54.md`; this record edits none of them.** No corpus file, score or scoring document changes until the
pass ends. Its changes are then applied by generator with pinned inputs and restated in place (protocol 10.2, 10.3;
decisions D12, D14), and until then the published totals stand, provisional as `README.md` says. Decisions taken here
are Claude's under the owner's delegation (Handoff 35, section 2); each is recorded with its reasons, and the owner may
reverse any of them.
**Reproduce:** `python3 rescoring_s56.py` (harness check 104). It is the third group written on the shared module
(`pass_common.py`, decision 52.5): the script holds the 20 readings and the group's own checks, and the module computes
the consequences cumulatively with every part before it. It checks every file this session added to the evidence cache
by digest, finds every passage the readings quote in its file, recomputes each clause 4 status from the IMF rows, and
checks that this record contains its generated tables verbatim. `python3 rescoring_s56.py --fetch` rebuilds the added
files from the network; the harness does not fetch.

---

## 1. What this group is

The consequence triage (`triage_s52.py`, decision 52.7), rerun after group 2.3, put C3.5 first among the criteria still
to read: 20 units in play, four of them able to change an adequacy tier on their own. C3.5 is class I: v2.0 keeps its
clauses and bar ("Failure detection within 1 week, diagnosis success ≥80%, correction success ≥70%, externalization <10%
of total costs") and names an indicator for each (`NEEC_Criteria_v2_s45.md`, section 4): clauses 1 and 2 are
aspirational (section 5 of that record: no agency publishes them); clause 3 is the supreme audit institution's published
share of recommendations implemented; clause 4 is the IMF's implicit fossil fuel subsidies as a share of GDP, "the
published lower bound of externalization, with GDP standing for total costs". Three units were re-estimated earlier and
are not re-read: Centrally Planned Socialism's (part (a)) and CCO-PTF-CIP-SZH's and Integral's (part (b6)), all at 0.5.
The other 20 are read clause by clause in the D28 form, from the evidence cache Session 55 built (`evidence_cache_s55.py`,
`evidence_cache/C3.5/`) and the sources this session added to it (section 5): thirteen published 0.5s and seven 0.0s.

**Outcome.** No unit can reach 1.0: no source the corpus cites, and none the cache holds, reports clause 2's diagnosis
share for any entry. **Four units rise** from 0.0 to 0.5: Nordic Social Democracy and Stakeholder Capitalism, whose
published 0.0s the measures v2.0 names do not bear out (reading 3.4); Qatar, whose clause 4 clears on the IMF's figure
(reading 3.6); and Libertarian Minarchism, a correction (reading 3.3). **One falls**, Universal Basic Services, from 0.5
to 0.0, a correction: its published score credits the host economy's scrutiny, which the reach rule does not credit to a
mechanism (reading 3.5). Fifteen hold, three of them at 0.0 (MMT + Job Guarantee, Universal Basic Income, State
Capitalism / China). Net +1.5 points; five failure counts change and **no tier changes**. CCO-PTF-CIP-SZH keeps first
place at 14.5; Participatory Economics and Integral share second at 14.0. Seven units are flagged.

## 2. How a clause is recorded, and the rule

As in groups 2.2 and 2.3 and decision 53.2: each clause is cleared, short, not shown, out of reach or moot. A unit is
1.0 only if every clause is cleared (D28, protocol 2.3); 0.0 only on one of protocol 2.1's whole-criterion conditions,
stated as the unit's reason and never with a clause cleared; 0.5 otherwise. A clause-level gap never makes 0.0 (D28(f)).
"Not shown" means that no estimate or evidence of the clause's quantity was located, not that the clause fails; "short"
means the evidence located falls below it. For a mechanism a clause whose quantity it does not govern even when
generalised is out of reach, and the host economy's figure is not credited to it (protocol 3.2, D28(c)).

## 3. Decisions and readings (under the delegation)

**3.1 What the clauses ask (decision 56.1).** *Clause 1:* the time from a failure's occurrence to its official
identification, shown from the dated record (an official inquiry, audit or evaluation) of the entry's most consequential
failure in its scoring window, which the scoring document must name; for a design, from its monitoring rule. A scoring
document that names no such record leaves the clause not shown; a design's statement that failures are "visible" is not a
monitoring rule. *Clause 2:* shown only by a diagnostic record or an independent evaluation that reports the share of
failures whose cause is established; none is cited by any unit. *Clause 3:* the supreme audit institution's own
published share of its recommendations implemented, on its stated basis; a figure on another basis (a share of the
issues an audit office chose to require immediate action on) is not shown, and for a configuration of several countries
one country's figure does not show the configuration. The bar is "≥70%", so a rate of 70% clears it. *Clause 4:* the
IMF's implicit subsidies in total, as a share of GDP, for 2022, the latest year the 2023 update estimates (later years are
projections). The figure clears the clause under 10% and is short at 10% or more. For a design, a projected share; none
is stated. *Alternatives:* (a) read the IMF figure strictly as a lower bound, which can show a shortfall but never a
clearance. Rejected: v2.0 names it as the clause's indicator, and on that reading no entry could ever clear clause 4 on
the measure the criteria name for it. The reading matters only where a flag runs toward 0.0 (readings 3.4 and 3.6), and
those flags carry it. (b) read only the IMF's environmental components (global warming and local air pollution), since
the measure speaks of "unpriced environmental costs". Rejected: the indicators field names "implicit subsidies, % of
GDP", the total; the two readings give the same status for every entry except China (9.59% against 10.95%), whose flag
carries it (reading 3.6).

**3.2 The evidence.** The cache of Session 55 holds the 20 published rationales by location and digest and the landing
pages of the IMF, INTOSAI and the UK National Audit Office; it does not hold country figures. This session added six
files (section 5): the IMF's country rows for the nine countries the configured national economies cover, from the IMF's
own Climate Change Indicators Dashboard, which serves the 2023 update's dataset; GAO's four-year implementation rate,
from Government Executive's report of GAO's fiscal 2024 Performance and Accountability Report (gao.gov refuses this
container, HTTP 403, as in Session 55); China's National Audit Office's rectification reports for 2023 to 2025, from
Xinhua and China Daily; and Riksrevisionen's annual report for 2020. Not reached: Singapore's Auditor-General's Office
(HTTP 403), Qatar's State Audit Bureau (no answer), and any implementation rate for Denmark, Finland, Iceland or Norway.
Five rationales (Degrowth, Fully Automated Luxury Communism, Market Socialism, Participatory Economics, Status Quo) are
one line long and cite nothing; their clauses are read from what they say.

**3.3 Libertarian Minarchism, 0.0 → 0.5 (decision 56.2, a correction).** The published 0.0, the 0.0 band's anchor, reads
"Market externalities maximally hidden ... No mechanism for making systemic failures legible." Protocol 2.1's 0.0 needs no
structural mechanism addressing the criterion. The design's markets make a firm's failure visible to its owners and
creditors through losses and bankruptcy, and correct it by exit; its diffuse and ecological costs stay externalized,
left to claims by identifiable victims. That is the 0.5 band's own description ("Some failures are visible (often
internally, e.g., to firm members) while others ... remain externalized"), which Market Socialism's unit, the band's
anchor, holds for worker-members. It is the same correction decision 53.3 made to the design's C1.2a: a published 0.0
that rests on partial coverage, not absence. All four clauses are not shown; 0.5, flagged toward 0.0 (the anchor's
reading, that visibility to owners does not answer a criterion about systemic failure). The failure count falls from
14 to 13; the design stays last.

**3.4 What the named indicators show for the United States and the Nordic countries (decision 56.3).** *Status Quo:*
clause 3 is GAO's four-year rate, 70% in fiscal 2024 (75% in fiscal 2023, against GAO's goal of 80%), at the bar:
cleared. Clause 4: implicit subsidies of 3.23% of GDP in 2022: cleared. The published rationale's "market failures are
systematically externalized" is not borne out on the measure v2.0 names, but clauses 1 and 2 are not shown, so the unit
holds at 0.5. *Nordic Social Democracy, 0.0 → 0.5.* The published 0.0 rests on clause 4 alone ("still systematically
externalizes environmental costs ... consumption-based emissions show continued ecological overshoot"). On the named
measure the five countries' implicit subsidies were 0.05% (Finland) to 0.58% (Denmark) of GDP in 2022; the clause
clears. One clause short would not have made 0.0 in any case (D28(f)); with that clause cleared, nothing in the record
meets protocol 2.1's conditions for the criterion as a whole. Clause 3 is not shown for the configuration: Sweden's
audit office reported in 2020 that agencies had acted on nearly 85% of its annual-audit recommendations within a year,
but no rate for the other four was located. 0.5, not flagged: consumption-based emissions are C4.2's measure, not C3.5's
(the criteria record, C4.6's "distinguishes" field), and the doubt they raise is about one clause. Failures fall from 2 to 1.
*Stakeholder Capitalism, 0.0 → 0.5.* The reform keeps the host economy's institutions, as group 2.3 read its housing
(Status Quo's), so clauses 3 and 4 clear on Status Quo's figures. Its own addition, ESG self-reporting with minimal
enforcement, does not remove them. With two clauses cleared protocol 2.1's 0.0 does not hold (decision 53.2). 0.5,
flagged toward 0.0: the published reading, the 0.0 band's second anchor ("Systemic failures ... obscured behind public
relations"), joined to alternative (a) of 3.1. Failures fall from 9 to 8.

**3.5 Universal Basic Services, 0.5 → 0.0 (decision 56.4, a correction), and the other income and employment
mechanisms.** UBS is a mechanism (decision D17). Its scoring document finds "no purpose-built, systematic mechanism ...
for surfacing failures across the UBS system as a whole; every instance of transparency identified here comes from
ordinary journalistic and academic scrutiny of specific implementations, not a built-in feature of UBS itself", and
scores 0.5 on that scrutiny. Protocol 3.2 credits a mechanism only where the mechanism does the work; the host economy's
press and universities do not. With nothing of its own left, protocol 2.1's first condition holds: no structural
mechanism addresses the criterion. This is the reading the corpus already gives Universal Basic Income and MMT + Job
Guarantee, both 0.0 as published and held here on that reason (a cash transfer and a job guarantee have no channel that
detects, diagnoses or corrects failures or prices costs). It parallels decision 53.3's correction of MMT's C1.2a, whose
0.5 credited the host's markets. Flagged toward 0.5: public provision brings each service within public audit and
democratic accountability, which could be read as a channel the mechanism itself creates. That reading is argument, not
the scoring document's finding (protocol 4.3), so it is a flag, not the score. Failures rise from 3 to 4; the tier holds.

**3.6 The three state capitalisms (decision 56.5).** *China holds at 0.0.* Clause 1 is short on the records its scoring
document names: the State Council found that Zhengzhou officials had deliberately withheld reports of up to 139 dead or
missing in the 2021 floods, and the epidemic's first warning was met by a police reprimand; identification and correction
took months. Clause 4 is short: implicit subsidies of 10.95% of GDP in 2022. Clause 3 is not shown on GAO's basis. The
National Audit Office reports 92% to 98% of the issues requiring immediate action rectified within the year (reports of
2023 to 2025), but in the 2024 audit those were 2,186 of 4,238 issues, and about 51% of all of them were resolved by the
December report, the rest placed on roadmaps. The 0.0 rests on protocol 2.1's second condition: the configuration treats
public disclosure of its signature failures as illegitimate (the epidemic warning punished as false information, a
censorship directive during the floods, the labour-protest monitor dissolved), and no clause the record shows is met.
The published flag toward 0.5 stands and gains alternative (b) of 3.1, under which clause 4 would clear (9.59%) and the
0.0 could not hold. *Qatar, 0.0 → 0.5.* The published 0.0 rounded a continuous estimate of 0.2 to 0.35. Clause 1 is
short: the ILO found no categorical count of fatal occupational injuries possible, and unexplained and heat-related deaths
of workers are not classified as work-related. Clause 4 clears: implicit subsidies of 7.31% of GDP in 2022 (its explicit
subsidies, 11.67%, undercharge supply costs and are a different quantity). With a clause cleared, protocol 2.1's 0.0 does
not hold (decision 53.2). Flagged toward 0.0: the published reading (deaths left unexplained, a worker detained after
raising concerns) joined to alternative (a). Failures fall from 10 to 9. *Singapore holds at 0.5:* clause 4 clears
(3.03%); its audit office's rate was not reached; the published flag toward 0.0 stands, joined to alternative (a), without
which it could not be reached. The contrast the scoring documents draw between China and the other two (documented
concealment of signature failure modes, against gaps in measurement) is what separates China's 0.0 here; the IMF figure
confirms the externalization China's rationale names.

**3.7 The designs and the other mechanisms hold at 0.5.** Market Socialism (the 0.5 band's anchor), Degrowth, Fully
Automated Luxury Communism, Participatory Economics and Doughnut Economics each name a channel that makes some failures
visible (members, communities, crashes, planning iterations, City Portraits) and state no monitoring rule, diagnostic or
correction share, or projected externalization: each clause not shown. Georgism, Mutual Credit, Sovereign Wealth Fund
Statism and Islamic Finance each have a channel of their own (published valuations with an appeal, a shared ledger, a
fund's disclosure and ethics council, a reserve-disclosure regime), and clause 4 is out of reach for each. Islamic
Finance's published flag toward 0.0 stands. Ostrom-style commons governance specifies the corpus's fullest detection,
sanctioning and conflict-resolution apparatus (principles 4 to 6) but states no time, share or projection. Its published
scope scenario, which read externalization against the governed resource and gave 1.0, no longer reaches 1.0: clauses 2
and 3 are not shown in either frame (D28; protocol 2.3(b)).

**What does not change.** No entry's tier changes. Of the four units the triage marked as tier-capable (falls of Market
Socialism, Degrowth, Georgism and Islamic Finance to 0.0), none falls: each has a channel of its own, and no clause-level
gap makes 0.0.

## 4. The units

### 4.1 Summary (generated)

| Entry | Published | Clause 1 | Clause 2 | Clause 3 | Clause 4 | Verdict | Flag |
|---|---:|---|---|---|---|---:|---|
| SQ | 0.5 | not shown | not shown | cleared | cleared | 0.5 |  |
| NSD | 0.0 | not shown | not shown | not shown | cleared | 0.5 |  |
| MS | 0.5 | not shown | not shown | not shown | not shown | 0.5 |  |
| LM | 0.0 | not shown | not shown | not shown | not shown | 0.5 | toward 0.0 |
| MMT | 0.0 | not shown | not shown | out of reach | out of reach | 0.0 |  |
| UBI | 0.0 | not shown | not shown | out of reach | out of reach | 0.0 |  |
| DG | 0.5 | not shown | not shown | not shown | not shown | 0.5 |  |
| SC | 0.0 | not shown | not shown | cleared | cleared | 0.5 | toward 0.0 |
| FALC | 0.5 | not shown | not shown | not shown | not shown | 0.5 |  |
| PE | 0.5 | not shown | not shown | not shown | not shown | 0.5 |  |
| GEO | 0.5 | not shown | not shown | not shown | out of reach | 0.5 |  |
| MC | 0.5 | not shown | not shown | not shown | out of reach | 0.5 |  |
| DE | 0.5 | not shown | not shown | not shown | not shown | 0.5 |  |
| UBS | 0.5 | not shown | not shown | out of reach | out of reach | 0.0 | toward 0.5 |
| SWF | 0.5 | not shown | not shown | not shown | out of reach | 0.5 |  |
| CN | 0.0 | short | not shown | not shown | short | 0.0 | toward 0.5 |
| SG | 0.5 | not shown | not shown | not shown | cleared | 0.5 | toward 0.0 |
| QA | 0.0 | short | not shown | not shown | cleared | 0.5 | toward 0.0 |
| IF | 0.5 | not shown | not shown | not shown | out of reach | 0.5 | toward 0.0 |
| OS | 0.5 | not shown | not shown | not shown | not shown | 0.5 |  |

### 4.2 Clause by clause (generated)

#### SQ C3.5 Failure-Mode Transparency: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Failure detection within 1 week | not shown | the scoring document names no dated record of the entry's most consequential failure, which the measure requires; the rationale names the 2008 crisis without its inquiry | Report v1.6, System 1, C3.5 |
| 2 | diagnosis success ≥80% | not shown | aspirational: no diagnostic record or independent evaluation reporting the share of failures whose cause is established is cited | Report v1.6, System 1, C3.5 |
| 3 | correction success ≥70% | cleared | the four-year rate at which agencies implemented GAO's recommendations was 70% in fiscal 2024 (75% in fiscal 2023), at the bar | GAO Performance and Accountability Report, fiscal 2024, as reported by Government Executive (evidence_cache/C3.5/gao_fy2024_govexec.txt) |
| 4 | externalization <10% of total costs | cleared | implicit fossil fuel subsidies were 3.23% of GDP in 2022, under 10% | IMF Fossil Fuel Subsidies Data, 2023 Update, implicit subsidies, 2022 (evidence_cache/C3.5/imf_ffs_rows_s56.json) |

*Note:* the published rationale's externalization finding is not borne out on the measure v2.0 names; the verdict is unchanged because clauses 1 and 2 are not shown (reading 3.4).

#### NSD C3.5 Failure-Mode Transparency: 0.0 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Failure detection within 1 week | not shown | the scoring document names no dated record of the entry's most consequential failure, which the measure requires | Report v1.6, System 2, C3.5 |
| 2 | diagnosis success ≥80% | not shown | aspirational: no diagnostic record or independent evaluation reporting the share of failures whose cause is established is cited | Report v1.6, System 2, C3.5 |
| 3 | correction success ≥70% | not shown | Sweden's Riksrevisionen reported in 2020 that agencies had acted on nearly 85% of its annual-audit recommendations within a year; no rate was located for Denmark, Finland, Iceland or Norway | Riksrevisionen, annual report for 2020 (evidence_cache/C3.5/riksrevisionen_ar2020.txt) |
| 4 | externalization <10% of total costs | cleared | implicit fossil fuel subsidies were 0.05% (Finland) to 0.58% (Denmark) of GDP in 2022 in each of the five countries, under 10% | IMF Fossil Fuel Subsidies Data, 2023 Update, implicit subsidies, 2022 (evidence_cache/C3.5/imf_ffs_rows_s56.json) |

*Note:* published 0.0 on clause 4 alone (environmental costs systematically externalized); on the measure v2.0 names the configuration clears that clause, so 2.1's 0.0 conditions do not hold for the criterion as a whole and the unit rises to 0.5 (reading 3.4).

#### MS C3.5 Failure-Mode Transparency: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Failure detection within 1 week | not shown | worker ownership makes firm failures visible to members immediately; no monitoring rule stating how soon a failure is identified is specified or cited | Report v1.6, System 4, C3.5 |
| 2 | diagnosis success ≥80% | not shown | aspirational: no diagnostic record or independent evaluation reporting the share of failures whose cause is established is cited | Report v1.6, System 4, C3.5 |
| 3 | correction success ≥70% | not shown | no correction record, and no share of identified failures corrected, is stated or cited | Report v1.6, System 4, C3.5 |
| 4 | externalization <10% of total costs | not shown | market externalities (environmental costs) remain hidden, as the rationale says; no externalized cost is projected as a share of total costs | Report v1.6, System 4, C3.5 |

*Note:* the 0.5 band's anchor example; it holds.

#### LM C3.5 Failure-Mode Transparency: 0.0 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Failure detection within 1 week | not shown | losses and bankruptcy make a firm's failure visible to its owners and creditors; no monitoring rule stating how soon a failure is identified is specified or cited | Report v1.6, System 5, C3.5 |
| 2 | diagnosis success ≥80% | not shown | aspirational: no diagnostic record or independent evaluation reporting the share of failures whose cause is established is cited | Report v1.6, System 5, C3.5 |
| 3 | correction success ≥70% | not shown | no audit institution or correction record for systemic failures is specified; no correction record, and no share of identified failures corrected, is stated or cited | Report v1.6, System 5, C3.5 |
| 4 | externalization <10% of total costs | not shown | market externalities are left to claims by identifiable victims; no externalized cost is projected as a share of total costs | Report v1.6, System 5, C3.5 |

*Flag (reading 3.3):* toward 0.0, the anchor's reading: no mechanism makes systemic failures legible, and failures visible only to a firm's owners do not answer the criterion.

*Note:* published 0.0 (the 0.0 band's anchor) read under protocol 2.1: firm failures visible to owners and diffuse costs externalized is the 0.5 band's description, which Market Socialism's unit holds; a correction, as decision 53.3 raised the design's C1.2a (reading 3.3).

#### MMT C3.5 Failure-Mode Transparency: 0.0 → 0.0

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Failure detection within 1 week | not shown | the Job Guarantee's enrolment shows unemployment, not the failure of any institution; no monitoring rule stating how soon a failure is identified is specified or cited | Report v1.6, System 6, C3.5 |
| 2 | diagnosis success ≥80% | not shown | aspirational: no diagnostic record or independent evaluation reporting the share of failures whose cause is established is cited | Report v1.6, System 6, C3.5 |
| 3 | correction success ≥70% | out of reach | the mechanism does not govern the economy's audit institution; the host's rate is not credited to it (protocol 3.2) | Report v1.6, System 6, C3.5; SCORING_PROTOCOL.md 3.2 |
| 4 | externalization <10% of total costs | out of reach | the mechanism prices no fuel use and governs no other externalized cost; the host's figure is not credited to it (protocol 3.2) | Report v1.6, System 6, C3.5; SCORING_PROTOCOL.md 3.2 |

*0.0 (protocol 2.1):* no structural mechanism addresses the criterion: a job guarantee and functional-finance budgeting have no channel that detects, diagnoses or corrects failures or prices externalized costs, and the host economy's are not the mechanism's.

#### UBI C3.5 Failure-Mode Transparency: 0.0 → 0.0

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Failure detection within 1 week | not shown | no monitoring rule stating how soon a failure is identified is specified or cited | Report v1.6, System 7, C3.5 |
| 2 | diagnosis success ≥80% | not shown | aspirational: no diagnostic record or independent evaluation reporting the share of failures whose cause is established is cited | Report v1.6, System 7, C3.5 |
| 3 | correction success ≥70% | out of reach | the mechanism does not govern the economy's audit institution; the host's rate is not credited to it (protocol 3.2) | Report v1.6, System 7, C3.5; SCORING_PROTOCOL.md 3.2 |
| 4 | externalization <10% of total costs | out of reach | the mechanism prices no fuel use and governs no other externalized cost; the host's figure is not credited to it (protocol 3.2) | Report v1.6, System 7, C3.5; SCORING_PROTOCOL.md 3.2 |

*0.0 (protocol 2.1):* no structural mechanism addresses the criterion: a cash transfer has no channel that detects, diagnoses or corrects failures or prices externalized costs, and the host economy's are not the mechanism's.

#### DG C3.5 Failure-Mode Transparency: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Failure detection within 1 week | not shown | localized systems make failures visible to communities; no monitoring rule stating how soon a failure is identified is specified or cited | Report v1.6, System 8, C3.5 |
| 2 | diagnosis success ≥80% | not shown | aspirational: no diagnostic record or independent evaluation reporting the share of failures whose cause is established is cited | Report v1.6, System 8, C3.5 |
| 3 | correction success ≥70% | not shown | no correction record, and no share of identified failures corrected, is stated or cited | Report v1.6, System 8, C3.5 |
| 4 | externalization <10% of total costs | not shown | ecological impacts still require technical monitoring, as the rationale says; no externalized cost is projected as a share of total costs | Report v1.6, System 8, C3.5 |

#### SC C3.5 Failure-Mode Transparency: 0.0 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Failure detection within 1 week | not shown | ESG metrics are self-reported with minimal enforcement; the scoring document names no dated record of the entry's most consequential failure, which the measure requires | Report v1.6, System 9, C3.5 |
| 2 | diagnosis success ≥80% | not shown | aspirational: no diagnostic record or independent evaluation reporting the share of failures whose cause is established is cited | Report v1.6, System 9, C3.5 |
| 3 | correction success ≥70% | cleared | the reform keeps the host economy's institutions, Status Quo's as group 2.3 read them: agencies implemented 70% of GAO's recommendations within four years in fiscal 2024 | Report v1.6, System 9, C3.5; GAO Performance and Accountability Report, fiscal 2024, as reported by Government Executive (evidence_cache/C3.5/gao_fy2024_govexec.txt) |
| 4 | externalization <10% of total costs | cleared | on the same host economy, implicit fossil fuel subsidies were 3.23% of GDP in 2022, under 10% | IMF Fossil Fuel Subsidies Data, 2023 Update, implicit subsidies, 2022 (evidence_cache/C3.5/imf_ffs_rows_s56.json) |

*Flag (reading 3.4):* toward 0.0, the anchor's reading: ESG self-reporting obscures systemic failures behind public relations, with clause 4 read as a lower bound that can show only a shortfall (decision 56.1, alternative).

*Note:* published 0.0 (the 0.0 band's second anchor); with clauses 3 and 4 cleared on the host economy the reform keeps, 2.1's 0.0 conditions do not hold for the criterion as a whole, and the unit rises to 0.5, as Status Quo's holds (reading 3.4).

#### FALC C3.5 Failure-Mode Transparency: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Failure detection within 1 week | not shown | technical failures are highly visible (systems crash, production halts); no monitoring rule stating how soon a failure is identified is specified or cited | Report v1.6, System 10, C3.5 |
| 2 | diagnosis success ≥80% | not shown | aspirational: no diagnostic record or independent evaluation reporting the share of failures whose cause is established is cited | Report v1.6, System 10, C3.5 |
| 3 | correction success ≥70% | not shown | no correction record, and no share of identified failures corrected, is stated or cited | Report v1.6, System 10, C3.5 |
| 4 | externalization <10% of total costs | not shown | no externalized cost is projected as a share of total costs | Report v1.6, System 10, C3.5 |

#### PE C3.5 Failure-Mode Transparency: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Failure detection within 1 week | not shown | production and consumption imbalances are visible through the planning iterations; no monitoring rule stating how soon a failure is identified is specified or cited | Report v1.6, System 11, C3.5 |
| 2 | diagnosis success ≥80% | not shown | aspirational: no diagnostic record or independent evaluation reporting the share of failures whose cause is established is cited | Report v1.6, System 11, C3.5 |
| 3 | correction success ≥70% | not shown | no correction record, and no share of identified failures corrected, is stated or cited | Report v1.6, System 11, C3.5 |
| 4 | externalization <10% of total costs | not shown | no externalized cost is projected as a share of total costs | Report v1.6, System 11, C3.5 |

#### GEO C3.5 Failure-Mode Transparency: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Failure detection within 1 week | not shown | where well implemented, mass-valuation results are published with a correction channel for landowners (Estonia); no monitoring rule stating how soon a failure is identified is specified or cited | NEEC_Georgism_LVT_scoring_scratch.md, C3.5 |
| 2 | diagnosis success ≥80% | not shown | aspirational: no diagnostic record or independent evaluation reporting the share of failures whose cause is established is cited | NEEC_Georgism_LVT_scoring_scratch.md, C3.5 |
| 3 | correction success ≥70% | not shown | the valuation's appeal channel corrects parcel errors, but no share corrected is stated; the economy's audit institution is not the mechanism's | NEEC_Georgism_LVT_scoring_scratch.md, C3.5; SCORING_PROTOCOL.md 3.2 |
| 4 | externalization <10% of total costs | out of reach | the mechanism prices no fuel use and governs no other externalized cost; the host's figure is not credited to it (protocol 3.2) | NEEC_Georgism_LVT_scoring_scratch.md, C3.5; SCORING_PROTOCOL.md 3.2 |

#### MC C3.5 Failure-Mode Transparency: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Failure detection within 1 week | not shown | balances are visible to members in a shared ledger; the Redes de Trueque's counterfeiting and voucher inflation went undetected long enough to cause collapse; no monitoring rule stating how soon a failure is identified is specified or cited | NEEC_MutualCredit_LETS_scoring_scratch.md, C3.5 |
| 2 | diagnosis success ≥80% | not shown | aspirational: no diagnostic record or independent evaluation reporting the share of failures whose cause is established is cited | NEEC_MutualCredit_LETS_scoring_scratch.md, C3.5 |
| 3 | correction success ≥70% | not shown | no correction record, and no share of identified failures corrected, is stated or cited | NEEC_MutualCredit_LETS_scoring_scratch.md, C3.5 |
| 4 | externalization <10% of total costs | out of reach | the mechanism prices no fuel use and governs no other externalized cost; the host's figure is not credited to it (protocol 3.2) | NEEC_MutualCredit_LETS_scoring_scratch.md, C3.5; SCORING_PROTOCOL.md 3.2 |

#### DE C3.5 Failure-Mode Transparency: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Failure detection within 1 week | not shown | City Portraits surface shortfalls and overshoots publicly, but on a reporting cycle, not within a week of a failure; no dated record is named | NEEC_DoughnutEconomics_scoring_scratch.md, C3.5 |
| 2 | diagnosis success ≥80% | not shown | aspirational: no diagnostic record or independent evaluation reporting the share of failures whose cause is established is cited | NEEC_DoughnutEconomics_scoring_scratch.md, C3.5 |
| 3 | correction success ≥70% | not shown | correction is left to each jurisdiction's political process; an assessment found Amsterdam's implementation 'incipient and limited'; no share corrected is stated | NEEC_DoughnutEconomics_scoring_scratch.md, C3.5 |
| 4 | externalization <10% of total costs | not shown | the framework reports ecological overshoot but prices none of it; no externalized cost is projected as a share of total costs | NEEC_DoughnutEconomics_scoring_scratch.md, C3.5 |

#### UBS C3.5 Failure-Mode Transparency: 0.5 → 0.0

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Failure detection within 1 week | not shown | the transparency the published score credits is ordinary journalistic and academic scrutiny of specific implementations; no monitoring rule stating how soon a failure is identified is specified or cited | NEEC_UniversalBasicServices_scoring_scratch.md, C3.5 |
| 2 | diagnosis success ≥80% | not shown | aspirational: no diagnostic record or independent evaluation reporting the share of failures whose cause is established is cited | NEEC_UniversalBasicServices_scoring_scratch.md, C3.5 |
| 3 | correction success ≥70% | out of reach | the mechanism does not govern the economy's audit institution; the host's rate is not credited to it (protocol 3.2) | NEEC_UniversalBasicServices_scoring_scratch.md, C3.5; SCORING_PROTOCOL.md 3.2 |
| 4 | externalization <10% of total costs | out of reach | the mechanism prices no fuel use and governs no other externalized cost; the host's figure is not credited to it (protocol 3.2) | NEEC_UniversalBasicServices_scoring_scratch.md, C3.5; SCORING_PROTOCOL.md 3.2 |

*0.0 (protocol 2.1):* no structural mechanism addresses the criterion: the scoring document finds no purpose-built mechanism and credits only the host economy's ordinary scrutiny, which is not the mechanism's (protocol 3.2), as for Universal Basic Income and MMT + Job Guarantee.

*Flag (reading 3.5):* toward 0.5: public provision brings each service within public audit and democratic accountability, a channel the mechanism itself creates.

*Note:* published 0.5 on the host economy's scrutiny; a correction (reading 3.5).

#### SWF C3.5 Failure-Mode Transparency: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Failure detection within 1 week | not shown | Norway's fund scores 100 of 100 on the Truman scoreboard, with a Council on Ethics since 2004; funds such as Russia's and Iran's score about 5 of 10 on the Linaburg-Maduell index; no monitoring rule stating how soon a failure is identified is specified or cited | NEEC_SovereignWealthFundStatism_scoring_scratch.md, C3.5 |
| 2 | diagnosis success ≥80% | not shown | aspirational: no diagnostic record or independent evaluation reporting the share of failures whose cause is established is cited | NEEC_SovereignWealthFundStatism_scoring_scratch.md, C3.5 |
| 3 | correction success ≥70% | not shown | over 180 disclosed exclusion decisions by 2025 are corrections of the fund's own holdings; no share of identified failures corrected is stated | NEEC_SovereignWealthFundStatism_scoring_scratch.md, C3.5 |
| 4 | externalization <10% of total costs | out of reach | the mechanism prices no fuel use and governs no other externalized cost; the host's figure is not credited to it (protocol 3.2) | NEEC_SovereignWealthFundStatism_scoring_scratch.md, C3.5; SCORING_PROTOCOL.md 3.2 |

#### CN C3.5 Failure-Mode Transparency: 0.0 → 0.0

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Failure detection within 1 week | short | on the dated records the scoring document names, the Henan floods (a State Council investigation found reports of up to 139 dead or missing deliberately withheld) and the epidemic's onset (a doctor's warning met by a police reprimand), identification and correction took months, not a week | NEEC_StateCapitalism_China_scoring_scratch.md, C3.5 |
| 2 | diagnosis success ≥80% | not shown | aspirational: no diagnostic record or independent evaluation reporting the share of failures whose cause is established is cited | NEEC_StateCapitalism_China_scoring_scratch.md, C3.5 |
| 3 | correction success ≥70% | not shown | the National Audit Office reports 92% to 98% of the issues requiring immediate action rectified within the year (2023 to 2025); of all 4,238 issues in the 2024 audit, about 51% were resolved by the December report, the rest on roadmaps; no rate on GAO's basis, recommendations implemented within a stated period, is published | National Audit Office of China, rectification reports to the NPC Standing Committee, 2023 to 2025, as reported by Xinhua and China Daily (evidence_cache/C3.5/cnao_rectification_2023.txt, _2024.txt, _2025.txt) |
| 4 | externalization <10% of total costs | short | implicit fossil fuel subsidies were 10.95% of GDP in 2022, over 10% | IMF Fossil Fuel Subsidies Data, 2023 Update, implicit subsidies, 2022 (evidence_cache/C3.5/imf_ffs_rows_s56.json) |

*0.0 (protocol 2.1):* the configuration treats public disclosure of its signature failures as illegitimate (the epidemic warning punished as false information, a censorship directive during the floods, the labour-protest monitor dissolved), and on every clause the record shows it falls short.

*Flag (reading 3.6):* toward 0.5, the published flag: the Centrally Planned Socialism precedent, and the central investigations and the audit office's rectification reports weighted as a correction channel; and on the environmental components alone (global warming and local air pollution, 9.59% of GDP) clause 4 would clear (decision 56.1, alternative (b)).

*Note:* the published 0.0 and its flag hold; v2.0's clause 4 figure confirms the externalization the rationale names.

#### SG C3.5 Failure-Mode Transparency: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Failure detection within 1 week | not shown | official data are extensive and the dormitory outbreak's case data were public; the scoring document names no dated record of the entry's most consequential failure, which the measure requires | NEEC_StateCapitalism_Singapore_scoring_scratch.md, C3.5 |
| 2 | diagnosis success ≥80% | not shown | aspirational: no diagnostic record or independent evaluation reporting the share of failures whose cause is established is cited | NEEC_StateCapitalism_Singapore_scoring_scratch.md, C3.5 |
| 3 | correction success ≥70% | not shown | the Auditor-General's Office publishes no recommendation-implementation rate that was located (its site refuses this container) | NEEC_StateCapitalism_Singapore_scoring_scratch.md, C3.5 |
| 4 | externalization <10% of total costs | cleared | implicit fossil fuel subsidies were 3.03% of GDP in 2022, under 10% | IMF Fossil Fuel Subsidies Data, 2023 Update, implicit subsidies, 2022 (evidence_cache/C3.5/imf_ffs_rows_s56.json) |

*Flag (reading 3.6):* toward 0.0, the published flag: POFMA orders, the absence of any poverty line and non-public state-enterprise data read as active suppression, with clause 4 read as a lower bound that can show only a shortfall (decision 56.1, alternative).

#### QA C3.5 Failure-Mode Transparency: 0.0 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Failure detection within 1 week | short | the ILO's report on 2020 found no categorical count of fatal occupational injuries possible, and the authorities do not classify unexplained or heat-related deaths of workers as work-related: failures are left unidentified, not identified within a week | NEEC_StateCapitalism_Qatar_scoring_scratch.md, C3.5 |
| 2 | diagnosis success ≥80% | not shown | aspirational: no diagnostic record or independent evaluation reporting the share of failures whose cause is established is cited | NEEC_StateCapitalism_Qatar_scoring_scratch.md, C3.5 |
| 3 | correction success ≥70% | not shown | no recommendation-implementation rate of the State Audit Bureau was located (its site did not answer this container) | NEEC_StateCapitalism_Qatar_scoring_scratch.md, C3.5 |
| 4 | externalization <10% of total costs | cleared | implicit fossil fuel subsidies were 7.31% of GDP in 2022, under 10% (explicit subsidies, undercharging for supply costs, are a different quantity) | IMF Fossil Fuel Subsidies Data, 2023 Update, implicit subsidies, 2022 (evidence_cache/C3.5/imf_ffs_rows_s56.json) |

*Flag (reading 3.6):* toward 0.0, the published reading: deaths left unexplained and a worker detained after raising concerns, with clause 4 read as a lower bound that can show only a shortfall (decision 56.1, alternative).

*Note:* published 0.0 on a continuous estimate of 0.2 to 0.35; with clause 4 cleared on the measure v2.0 names, 2.1's 0.0 conditions do not hold for the criterion as a whole (decision 53.2), and the unit rises to 0.5 (reading 3.6).

#### IF C3.5 Failure-Mode Transparency: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Failure detection within 1 week | not shown | the disclosure regime on profit-equalisation and investment-risk reserves is largely observed (IFSB WP-10), but account holders are in some cases not informed of the bank's practices (IMF WP 15/120); no monitoring rule stating how soon a failure is identified is specified or cited | NEEC_IslamicFinance_scoring_scratch.md, C3.5 |
| 2 | diagnosis success ≥80% | not shown | aspirational: no diagnostic record or independent evaluation reporting the share of failures whose cause is established is cited | NEEC_IslamicFinance_scoring_scratch.md, C3.5 |
| 3 | correction success ≥70% | not shown | no correction record, and no share of identified failures corrected, is stated or cited | NEEC_IslamicFinance_scoring_scratch.md, C3.5 |
| 4 | externalization <10% of total costs | out of reach | the mechanism prices no fuel use and governs no other externalized cost; the host's figure is not credited to it (protocol 3.2) | NEEC_IslamicFinance_scoring_scratch.md, C3.5; SCORING_PROTOCOL.md 3.2 |

*Flag (reading 3.7):* toward 0.0, the published flag: return-smoothing read as active suppression of the mechanism's own central failure mode.

#### OS C3.5 Failure-Mode Transparency: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Failure detection within 1 week | not shown | principles 4 to 6 specify monitors accountable to the appropriators, graduated sanctions and cheap conflict resolution, at a scale where deviations are visible within days; no monitoring rule states a time | NEEC_Ostrom_Commons_scoring_scratch.md, C3.5 |
| 2 | diagnosis success ≥80% | not shown | aspirational: no diagnostic record or independent evaluation reporting the share of failures whose cause is established is cited | NEEC_Ostrom_Commons_scoring_scratch.md, C3.5 |
| 3 | correction success ≥70% | not shown | sanctions and conflict resolution are a correction apparatus, but no share of identified failures corrected is stated | NEEC_Ostrom_Commons_scoring_scratch.md, C3.5 |
| 4 | externalization <10% of total costs | not shown | principle 1's boundaries make costs borne by non-members a designed-in possibility (Stern, International Journal of the Commons, 2011); no share is stated | NEEC_Ostrom_Commons_scoring_scratch.md, C3.5 |

*Note:* the scope scenario reading externalization against the governed resource no longer reaches 1.0: clauses 2 and 3 are not shown in either frame (reading 3.7).

## 5. The sources added to the evidence cache

Each file was fetched on 2026-10-14 by `python3 rescoring_s56.py --fetch`; the text files hold the article text from 1,500 characters before the passage quoted to 1,500 after, with the raw page's md5 in their first lines. The script checks each file's md5 and finds each quoted passage in it. Session 55's files and index are unchanged.

| File (`evidence_cache/C3.5/`) | Clause | Source | md5 |
|---|---|---|---|
| `imf_ffs_rows_s56.json` | 4 | IMF Fossil Fuel Subsidies Data: 2023 Update (Black, Liu, Parry and Vernon), the country rows served by the IMF Climate Change Indicators Dashboard (climatedata.imf.org, dataset 'Fossil Fuel Subsidies Table'), percent of GDP | `dbd31b4b` |
| `gao_fy2024_govexec.txt` | 3 | Government Executive, 'GAO saved the federal government $67.5 billion in fiscal 2024' (November 2024), reporting GAO's Performance and Accountability Report for fiscal 2024 (GAO-25-900570; gao.gov refuses this container) | `357aecca` |
| `cnao_rectification_2023.txt` | 3 | China Daily (NPC site), 'Majority of auditing problems from 2022 have been rectified', 27 December 2023 | `2740055a` |
| `cnao_rectification_2024.txt` | 3 | China Daily (NPC site), Xinhua, 'Audit report shows China fixed 94 pct of fiscal irregularities', 23 December 2024 | `f47c55e4` |
| `cnao_rectification_2025.txt` | 3 | China Daily (NPC site), 'Audit: China fixes bulk of fiscal problems tied to 2024 budget', 23 December 2025 | `cdbda9e5` |
| `riksrevisionen_ar2020.txt` | 3 | Riksrevisionens årsredovisning för 2020 (Redogörelse 2020/21:RR4, riksdagen.se), the Auditor General's foreword | `3e9c1d11` |

## 6. What parts (a), (b) and groups 2.1 to 2.4 change (generated)

| Entry | Published (rank) | After group 2.3 (rank) | After group 2.4 (rank) | Change here | Failures | Tier |
|---|---:|---:|---:|---:|---:|---|
| CCO | 24.5 (1) | 14.5 (1) | 14.5 (1) | 0.0 | 0 | Potentially Adequate |
| PE | 20.5 (2) | 14.0 (2) | 14.0 (2) | 0.0 | 1 | Potentially Adequate |
| NSD | 19.5 (3) | 13.0 (4) | 13.5 (4) | 0.5 | 1 | Potentially Adequate |
| INT | 19.5 (3) | 14.0 (2) | 14.0 (2) | 0.0 | 3 | Partially Adequate |
| DG | 19.0 (5) | 13.0 (4) | 13.0 (5) | 0.0 | 2 | Potentially Adequate |
| MS | 16.5 (6) | 13.0 (4) | 13.0 (5) | 0.0 | 2 | Potentially Adequate |
| MMT | 15.5 (7) | 11.0 (14) | 11.0 (14) | 0.0 | 4 | Partially Adequate |
| UBI | 14.5 (8) | 11.0 (14) | 11.0 (14) | 0.0 | 7 | Structurally Inadequate |
| MC | 14.5 (8) | 12.5 (8) | 12.5 (8) | 0.0 | 3 | Partially Adequate |
| OS | 14.5 (8) | 13.0 (4) | 13.0 (5) | 0.0 | 3 | Partially Adequate |
| SWF | 14.0 (11) | 12.5 (8) | 12.5 (8) | 0.0 | 3 | Partially Adequate |
| SG | 14.0 (11) | 11.5 (12) | 11.5 (11) | 0.0 | 4 | Partially Adequate |
| GEO | 13.5 (13) | 12.5 (8) | 12.5 (8) | 0.0 | 2 | Potentially Adequate |
| UBS | 13.5 (13) | 12.0 (11) | 11.5 (11) | -0.5 | 4 | Partially Adequate |
| IF | 13.5 (13) | 11.5 (12) | 11.5 (11) | 0.0 | 5 | Partially Adequate |
| FALC | 13.0 (16) | 9.0 (18) | 9.0 (18) | 0.0 | 10 | Structurally Inadequate |
| DE | 11.5 (17) | 9.0 (18) | 9.0 (18) | 0.0 | 8 | Structurally Inadequate |
| SQ | 10.5 (18) | 9.5 (16) | 9.5 (16) | 0.0 | 9 | Structurally Inadequate |
| CPS | 10.0 (19) | 7.5 (22) | 7.5 (22) | 0.0 | 12 | Structurally Inadequate |
| SC | 10.0 (19) | 8.5 (20) | 9.0 (18) | 0.5 | 8 | Structurally Inadequate |
| CN | 10.0 (19) | 9.5 (16) | 9.5 (16) | 0.0 | 8 | Structurally Inadequate |
| QA | 9.0 (22) | 8.0 (21) | 8.5 (21) | 0.5 | 9 | Structurally Inadequate |
| LM | 8.0 (23) | 6.5 (23) | 7.0 (23) | 0.5 | 13 | Structurally Inadequate |

After this group the corpus has 16 dominance pairs against 18 after group 2.3 (new: none; lost: UBS>DE, CN>QA), and its frontier holds 15 entries against 15 (SQ, NSD, CPS, MS, LM, UBI, DG, FALC, PE, CCO, INT, MC, SWF, IF, OS). First place: CCO, 14.5 after group 2.3, 14.5 now, ahead of PE, INT at 14.0. Across the pass so far 215 units have been re-estimated, each counted once: 17 are at 1.0, 181 at 0.5 and 17 at 0.0; against their published scores 147 fell, 5 rose and 63 are unchanged (net -71.0 points).

| Entry | Published | (a) | (b1) | (b2) | (b3) | (b4) | (b5) | (b6) | (b7) | 48.3 | (b8) | (b9) | (2.1) | (2.2) | (2.3) | (2.4) | Now | Re-estimated | At 0.5 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| CCO | 24.5 | -0.5 | -1.5 | -0.5 | -0.5 | -0.5 | -0.5 | -1.0 | -0.5 | -0.5 | -0.5 | -1.0 | -1.5 | -0.5 | -0.5 |  | 14.5 | 22 | 20 |
| PE | 20.5 |  | -1.5 | -0.5 | -0.5 | -1.5 |  | -0.5 | -0.5 |  | -0.5 | -0.5 |  |  | -0.5 |  | 14.0 | 16 | 15 |
| NSD | 19.5 | -2.5 | -1.0 | -0.5 | -0.5 | -0.5 |  |  |  |  | -0.5 | -0.5 |  | -0.5 |  | 0.5 | 13.5 | 15 | 14 |
| INT | 19.5 | -0.5 | -1.0 | -0.5 |  | -1.0 | -0.5 | -1.0 | -0.5 |  |  |  |  |  | -0.5 |  | 14.0 | 14 | 11 |
| DG | 19.0 |  | -1.5 | -0.5 | -0.5 | -0.5 |  | -0.5 | -1.0 |  | -1.0 |  |  |  | -0.5 |  | 13.0 | 14 | 14 |
| MS | 16.5 | -1.0 | -1.5 | -0.5 | -0.5 |  |  |  | 0.5 |  |  |  |  | -0.5 |  |  | 13.0 | 11 | 9 |
| MMT | 15.5 | -1.5 | -1.0 | -0.5 | -0.5 |  |  |  |  |  | -0.5 |  |  | -0.5 |  |  | 11.0 | 10 | 8 |
| UBI | 14.5 | -1.5 | -0.5 | -0.5 | -0.5 |  |  |  |  |  | -0.5 |  |  |  |  |  | 11.0 | 11 | 8 |
| MC | 14.5 |  | -1.0 | -0.5 |  |  | -0.5 |  |  |  |  |  |  |  |  |  | 12.5 | 8 | 5 |
| OS | 14.5 | -0.5 |  |  |  |  | -0.5 | -0.5 |  |  |  |  |  |  |  |  | 13.0 | 7 | 5 |
| SWF | 14.0 |  |  | -0.5 |  |  | -0.5 | -0.5 |  |  |  |  |  |  |  |  | 12.5 | 7 | 5 |
| SG | 14.0 | -1.0 | -0.5 | -0.5 |  |  |  |  |  |  |  |  |  | -0.5 |  |  | 11.5 | 6 | 6 |
| GEO | 13.5 | -0.5 |  |  |  |  | -0.5 |  |  |  |  |  |  |  |  |  | 12.5 | 5 | 4 |
| UBS | 13.5 |  | -0.5 | -0.5 |  |  | -0.5 |  |  |  |  |  |  |  |  | -0.5 | 11.5 | 7 | 4 |
| IF | 13.5 | -1.0 |  |  |  |  | -0.5 |  |  |  |  | -0.5 |  |  |  |  | 11.5 | 7 | 7 |
| FALC | 13.0 | -0.5 | -0.5 |  | -0.5 | -1.0 |  | -0.5 | -0.5 |  |  |  |  |  | -0.5 |  | 9.0 | 11 | 9 |
| DE | 11.5 | -0.5 | -0.5 |  |  |  | -0.5 | -0.5 | -0.5 |  |  |  |  |  |  |  | 9.0 | 8 | 7 |
| SQ | 10.5 | -0.5 |  |  |  | -0.5 |  |  |  |  |  |  |  |  |  |  | 9.5 | 6 | 5 |
| CPS | 10.0 | -1.5 |  |  | -0.5 |  |  |  |  |  | -0.5 |  |  |  |  |  | 7.5 | 7 | 5 |
| SC | 10.0 |  | -1.0 |  |  |  |  |  |  |  |  | -0.5 |  |  |  | 0.5 | 9.0 | 6 | 6 |
| CN | 10.0 |  |  | -0.5 |  |  |  |  |  |  |  |  |  |  |  |  | 9.5 | 4 | 3 |
| QA | 9.0 | -0.5 |  | -0.5 |  |  |  |  |  |  |  |  |  |  |  | 0.5 | 8.5 | 5 | 5 |
| LM | 8.0 | -1.5 |  |  |  |  |  |  |  |  |  | -0.5 |  | 0.5 |  | 0.5 | 7.0 | 8 | 6 |

Anchor examples citing a unit the pass moves: C1.1's 1.0 example, NSD (part (b3)); C1.2a's 1.0 example, MS (part (2.2)); C1.2b's 1.0 example, CCO (part (2.1)); C1.4's 1.0 example, CCO (part (2.1)); C2.1's 1.0 example, UBI (part (a)); C2.3's 1.0 example, DG (part (b1)); C2.4's 1.0 example, PE (part (b1)); C2.5's 1.0 example, CCO (part (b5)); C3.1's 1.0 example, UBI (part (b2)); C3.2's 1.0 example, PE (part (b4)); C3.5's 1.0 example, CCO (part (b6)); C3.5's 0.0 example, LM (part (2.4)); C3.5's 0.0 example, SC (part (2.4)); C4.1's 1.0 example, DG (part (b6)); C4.2's 1.0 example, PE (part (b7)); C4.3's 1.0 example, CCO (part (b8)); C5.1's 1.0 example, MS (part (b2)); C5.2's 1.0 example, CCO (part (b9)); C5.4's 1.0 example, CCO (part (b9)); C5.5's 1.0 example, PE (part (b9)). Bands whose example the pass moves and which no corpus unit then scores at their value: C1.1's 1.0, C1.2a's 1.0, C2.1's 1.0, C2.3's 1.0, C2.4's 1.0, C3.1's 1.0, C3.5's 1.0, C4.1's 1.0, C4.2's 1.0, C4.3's 1.0.

C3.5's published anchors: CCO-PTF-CIP-SZH at 1.0 (moved to 0.5 by part (b6)), Market Socialism at 0.5 (holds), and Libertarian Minarchism and Stakeholder Capitalism at 0.0, both of which rise here. The 0.0 band is not left empty: China, MMT + Job Guarantee, Universal Basic Income and Universal Basic Services are at 0.0 after this group. Stage 3's restatement of the criterion's anchors takes its 0.0 examples from those units, as C1.1's and C1.2a's 1.0 bands drop theirs.

## 7. Corrections found (not polish)

1. **Libertarian Minarchism's C3.5, 0.0 → 0.5** (reading 3.3): the published 0.0 rests on partial coverage, the 0.5
   band's description, not on protocol 2.1's absence of a mechanism. Flagged toward 0.0.
2. **Universal Basic Services' C3.5, 0.5 → 0.0** (reading 3.5): the published 0.5 credits the host economy's scrutiny,
   which the reach rule does not credit to a mechanism, and the scoring document finds no mechanism of the entry's own.
   Flagged toward 0.5.
3. **Status Quo's and Nordic Social Democracy's C3.5 rationales** state that the economies "systematically externalize"
   environmental costs. On the measure v2.0 names, implicit fossil fuel subsidies were 3.23% of GDP in the United States
   and 0.05% to 0.58% in the Nordic countries in 2022, under the clause's 10%. Report v2.0 gives the figures.
4. **Five one-line rationales** (Degrowth, Fully Automated Luxury Communism, Market Socialism, Participatory Economics,
   Status Quo) cite nothing; Report v2.0's Part I, written from the per-unit rationales (decision 52.8), states each
   clause as this record does.
5. **Ostrom-style commons governance's scope scenario** (C3.5 at 1.0 when externalization is read against the governed
   resource) is stated in its scoring document before D28; under D28 the scenario gives 0.5, since clauses 2 and 3 are
   not shown in either frame. The scenario's table in Report v2.0 says so.

The rises of Nordic Social Democracy, Stakeholder Capitalism and Qatar are not corrections: each follows from the
indicator v2.0 names for clause 4 (or, for Stakeholder Capitalism, clauses 3 and 4), which the published scores
predate.

## 8. Disclosure

CCO-PTF-CIP-SZH is the owner's design. Its C3.5 unit was read in part (b6) and is not re-read here; this group changes
none of its scores. First place is unchanged at 14.5, half a point ahead of Participatory Economics and Integral, whose
C3.5 units hold at 0.5 (Participatory Economics) or were read earlier (Integral). Every reading here was made before
the consequences table was computed. The decision on clause 4's two alternatives (3.1) was taken after the IMF figures
were seen. Alternative (b) decides only China's status; the reading adopted (total implicit subsidies) is the one the
indicators field names, and the one less favourable to China. Alternative (a) would leave clause 4 not shown wherever
the figure is under 10%, which would let the flags of Stakeholder Capitalism, Singapore and Qatar toward 0.0 be
reached; it is carried in those flags.

## 9. What remains

- **Next group from the triage** (rerun after this group, `triage_s52_output.txt`): C5.2 Staged Transition Pathways,
  class M (16 units in play, 4 tier-capable), a judgment re-read with no cache needed; its 16 units at 0.5 or 0.0 were
  planned in reading 3.2 of `NEEC_Rescoring_s50.md`. C1.4 Automation Resilience, class I, moves to second (3
  tier-capable, from 4): this group's changes to failure counts reordered the two. The units that could change no
  failure count, tier or rank on their own are now seven: CCO C4.5, CN C2.5, CPS C2.5, IF C4.5, SG C2.5, SQ C2.5 and
  UBS C4.5.
- **`evidence_cache_s55.py`'s check [2]** compares the units in play *now* with its index, so it reports a failure once
  group 2.4 is part of the pass (no C3.5 unit is in play any more); its digest checks still pass. It is not a harness
  check and is not edited here. The C1.4 cache script should read the state before its group (`pc.Pass(upto=...)`).
- **For the criteria record's next amendment:** decisions 56.1 to 56.5, with 54.1 to 54.3, 53.1 to 53.3, 52.11 and
  52.12, in one run of the chain; C3.5's anchors (section 6).
- **For Report v2.0:** section 7's corrections; the clause 3 and 4 figures of reading 3.4 and 3.6.
- **Sources a later session could add:** the Nordic audit offices' and Singapore's Auditor-General's implementation rates
  (clause 3), and GAO's report itself (gao.gov refuses this container). None would change a verdict here, since
  clause 2 is not shown for any national economy, but China's and Qatar's flags turn partly on clause 3.

## 10. What this record does not show

No source located reports clause 2's diagnosis share for any entry, so C3.5 can at present separate only 0.0 from 0.5, as
the criteria record's section 5 foresaw. The IMF's implicit subsidies are a modelled estimate (the IMF's own lower bound
on the costs it counts), not an accounting of every externalized cost; GAO's figure is read from a press report of its
Performance and Accountability Report, and China's from Xinhua's and China Daily's reports of the audit office's
statements. "Not shown" means that no evidence was located, not that the clause fails. The interpretation check
(decisions 50.1 to 50.4) was not run; it is optional. The record is one scorer's re-estimation; whether its calls
reproduce is what the replication programme tests.
