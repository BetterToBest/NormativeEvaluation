# NEEC Rescoring Pass — Record, Stage 2, Group 2.6: C5.2 Staged Transition Pathways (class M)

**Session 58 · 2026-10-15 · Scorer and engineer: Claude · Owner: Duke Johnson**
**Status: scratch (protocol 10.1). Parts (a) and (b) and groups 2.1 to 2.5 are `NEEC_Rescoring_s37.md` to
`NEEC_Rescoring_s57.md`; this record edits none of them.** No corpus file, score or scoring document changes until the
pass ends. Its changes are then applied by generator with pinned inputs and restated in place (protocol 10.2, 10.3;
decisions D12, D14), and until then the published totals stand, provisional as `README.md` says. Decisions 58.1 and
58.2 are the owner's (the Project ledger, 2026-10-15); the others are Claude's under the owner's delegation (Handoff 35,
section 2; decision 57.2: score changes for entries other than CCO-PTF-CIP-SZH need no owner confirmation), each
recorded with its reasons, and the owner may reverse any of them.
**Reproduce:** `python3 rescoring_s58.py` (harness check 106). It holds the 16 readings and the group's own checks, and
checks the owner's part 58.1 (`owner_s58.py`), which `pass_common.py` applies as its own part between group 2.5 and this
group; the module computes the consequences cumulatively with every part before it. The script recomputes the spans and
stage counts the readings derive, checks the simulation runs' captured output by digest for the figures part 58.1
quotes, and checks that this record contains its generated tables verbatim.

---

## 1. What this group is

**The owner's answers first.** The owner answered the two ledger items Session 57 opened. On d37 (S57-3.9) the owner
reversed decision 57.7: CCO-PTF-CIP-SZH's C3.2 stays at 1.0 (decision 58.1, section 3.1). On d38 (S57-3.3) the owner
paused the decision until all of CCO-PTF-CIP-SZH's readings are in (decision 58.2). Decision 58.1 is applied as a part of
the pass of its own, "58.1", after group 2.5; group 2.5's script and record are unchanged.

**The group.** C5.2 is class M (R4). v2.0 keeps its five Session 44 clauses word for word, staged (≥4 phases), rapid
(≤36 months) deployment, specific milestones, resource requirements and risk mitigation, and places all five under the
scope "each shown feasible by precedent or component evidence"; its requirement reads "each shown feasible rather than
only planned". Part (b9) (`NEEC_Rescoring_s50.md`) read the seven published 1.0s (Status Quo, Nordic Social Democracy,
Libertarian Minarchism, MMT + Job Guarantee, Stakeholder Capitalism, CCO-PTF-CIP-SZH, Islamic Finance) and set the
reading of the scope (its reading 3.2(b)): each element is shown feasible by a deployment that took place, of the system
itself, of institutions of the same kind, or of the components the pathway deploys at the pace and scale it sets; a
plan, a simulation or a programme of another kind cited for its speed shows nothing. This group applies that reading to
the other 16 units: 13 published at 0.5 and three at 0.0 (Centrally Planned Socialism, Fully Automated Luxury Communism,
Integral). The triage put C5.2 first (`triage_s52_output.txt`, section 4): 16 units in play, four able to change an
adequacy tier on their own, and Participatory Economics' and Integral's each able to decide who is first.

**Outcome.** Two units rise and none falls. **Integral's rises from 0.0 to 0.5:** the design's own white paper (v0.1,
December 2025), published after the corpus scored it, states a staged pathway and a risk framework, so the published
0.0's reason no longer describes the design, and its risk-mitigation clause is cleared on the reading part (b9) gave
CCO-PTF-CIP-SZH's (reading 3.3). **Sovereign Wealth Fund Statism's rises from 0.5 to 1.0:** every clause is shown by
deployments of the mechanism itself, Norway's in stages and Timor-Leste's within a year after its post-conflict
independence (reading 3.4). Centrally Planned Socialism's and Fully Automated Luxury Communism's 0.0s hold, each on its
whole-criterion reason (reading 3.5), and the other twelve hold at 0.5 (reading 3.6); Georgism's staged clause, which
its published rationale credited, is now short on its precedent's own record. Integral's failure count falls from 3 to
2, so **Integral moves from Partially Adequate to Potentially Adequate**, and **first place is shared at 14.5** by
CCO-PTF-CIP-SZH (after decision 58.1) and Integral. Five flags. 38 clauses are not estimated, each in a 0.5 unit whose
verdict another clause fixes (section 2).

## 2. How a clause is recorded, and the rule

As in group 2.2, section 2, and decision 53.2: each clause is cleared, short, not shown, out of reach or moot. A unit is
1.0 only if all five clauses are cleared or moot (D28, protocol 2.3); 0.0 only on one of protocol 2.1's whole-criterion
conditions, stated as the unit's reason and never with a clause cleared; 0.5 otherwise. A clause-level gap never makes
0.0 (D28(f)). "Not shown" means that no deployment showing the element was located, not that the element is impossible;
"short" means the deployment located falls below the clause. **Clauses not estimated:** as part (b9) did (its section 2),
a clause may be marked "not estimated in this pass" only where another clause of the same unit, short or not shown,
fixes the verdict at 0.5. No clause of a 0.0 or a 1.0 unit is left unestimated; the script checks this. The 38 such
clauses are listed for Report v2.0's clause-level estimate (section 8).

## 3. Decisions and readings

**3.1 The owner's decisions (58.1, 58.2).** *58.1 (ledger d37, the owner's answer of 2026-10-15):* "The backing of the
currency by creative output as a community chest is an original design feature, however Claude measured from none to
all for data knowledge, and insists on using the cautious readings. Keep CCO at one until an empirical study shows that
it doesn't hold up in real world data." Decision 57.7 is reversed: CCO-PTF-CIP-SZH's C3.2 is 1.0. Under D28 a 1.0 needs
every clause cleared, so the unit (`owner_s58.py`) records clause 1 cleared on the owner's reading, that the design's
backing by creative output backs what the Source pays (at full backing the design's published model at v5.6.0 raises
prices 0.1% a year in the Reference environment, every seed under 3%; `cco_sim_v56_checks_s57_output.txt`), and clauses
2 and 3 carried as group 2.1 carried them on the design's own papers (the framework paper's 8% scenario; the dual-
currency paper's adjustment rules). It is flagged toward 0.5 on group 2.5's reading, so that the record keeps both. Its
reopening condition replaces C3.2's in `STATE.md`: an empirical study showing that the backing by creative output does
not hold in real-world data. Decision 57.6 (a clause clearing only at a backing share the design does not state is not
shown) stands for the design's other units, which wait on decision 58.2; the owner's reasoning here may bear on them
(C1.2a, which clears at full backing, is the nearest), and that is the owner's to take up under 58.2, not this session's.
*Consequence,* computed in the script's check [0]: CCO-PTF-CIP-SZH 14.0 → 14.5, no failure count changes, and it holds
first place alone before this group. *58.2 (ledger d38):* "Pause this decision for now, wait until all the CCO readings
are in and I'll push back on some of them all at once." S57-3.3 stays open, paused; the eight holds stand as the pass's
readings in the meantime.

**3.2 C5.2's scope, applied to the units at 0.5 and 0.0 (decision 58.3, a method choice).** Part (b9)'s reading 3.2(b)
governs. This group adds what applying it to the remaining units needed:
(a) *Force.* A deployment that rested on a seizure of power by force (revolution, civil war, a coup, occupation) is not a
precedent for either pathway. The criterion's rationale names revolution as what a staged pathway avoids ("Revolutions
typically produce chaos, reaction, and systems worse than what they replaced"), its 0.0 band names transitions that
"required non-gradual means (revolution, occupation)", and part (b9) cleared staged clauses only on stages a polity took
by its own procedures (Sweden's, Germany's, Malaysia's). Where the configuration an entry defines rests on a precondition
that came about only by force, its later orderly stages are component evidence for the components they deployed, not a
precedent for the configuration. *Alternative:* count a deployment by any means; it would raise Centrally Planned
Socialism's rapid clause (flagged, reading 3.5) and change no other verdict.
(b) *Staged.* At least four successive, dated stages of deployment of the system or of a component the entry names as
defining. A deployment under way but not carried through, and shown by its own record not to be on course, is short.
(c) *Rapid.* A deployment of the system or its defining components to operation within 36 months, in a crisis or
post-crisis context; the span counted is the deployment's, from its first public step to operation. A deployment that
scaled within the window and then collapsed shows the pace, not that the element is feasible: the criterion's own rapid
template ends in "stabilization".
(d) *Milestones, resources, risk mitigation,* as part (b9) read them: dated targets set and met in a precedent
(Malaysia's 50% target, measured at 48%); a documented statement of what a deployment took (Islamic Finance's unit is not
shown without one); mitigations of kinds in use elsewhere, as CCO-PTF-CIP-SZH's risk clause was cleared.
(e) *The entry's sources.* Each unit is read on the sources its published score cites and the design's own current
documents, as earlier parts read Integral on the design's own pages (parts (b5), (b8)); the scope then asks for
deployments, wherever located.
(f) *0.5 against 0.0.* Protocol 2.1's 0.0 needs no structural mechanism addressing the criterion, or a pathway closed
under the system's own logic. Under v2.0 a pathway sketched in stages whose first stage has deployments of its kind is a
genuine mechanism short of the threshold: 0.5. A unit with no pathway beyond an aspiration, or whose every transition
required force, or whose destination cannot be deployed at all, is 0.0, and only with no clause cleared.

**3.3 Integral, re-read on the design's white paper (decision 58.4, a correction).** The corpus scored Integral on a
review of an earlier document whose stated pathway was "starts small and expands" (`Integral_NEEC_Review.md`, C5.2); that
phrase is the 0.0 band's example, and the anchor's note says it is not a pathway. The design's author has since
published *INTEGRAL: Technical White Paper v0.1* (December 2025; 345 pages; PDF md5 a6defc9a, from integralcollective.io,
retrieved 2026-10-15). Its section 11, "Transition, Adoption, & Implementation", states a pathway: proto-nodes grown from
practices that exist (mutual aid networks, tool libraries, repair cafés, timebanks, community kitchens; 11.2); each of
the five systems formalised in three steps as participation grows (11.3); scaling through use (11.4); hybrid integration
with the market through interface cooperatives with caps on market exposure and sunset rules (11.5, 11.6); safeguards
against suppression (11.10); and an arc of four stages, "from marginal experiment, to supplementary alternative, to
essential support layer, and eventually to a dominant substrate", "inherently generational" (11.11). *Applied:* (1)
staged not shown: the stages are a plan with no dates; the first stage's kind is deployed widely, but no node operating
the design's systems is located: the project's site registers four communities, in its own Phase 1, the building of its
software; (2) rapid not shown: the paper sets direct implementation in a nation-state aside as "highly unlikely"; (3)
milestones not shown: its markers are "incremental and often unremarkable"; (4) resources not shown: none is stated;
(5) risk mitigation cleared: section 11.10's measures (no single point of failure, peer-to-peer and federated
infrastructure with replicated data, grounded in deployed technologies, decentralised identifiers, content-addressed
storage and federated messaging; no central treasury; commons assets that cannot be pledged or sold; legal compliance as
the default) are mitigations of kinds in use elsewhere, the reading part (b9) gave CCO-PTF-CIP-SZH's clause 5. With a
clause cleared, 0.0 cannot hold (decision 53.2); and the published 0.0's reason, that the source "provides no phased
timeline, legal framework, resource requirement, or institutional-coordination plan", no longer describes the design's
pathway in full. The unit rises to 0.5. **Flagged** toward 0.0: read on the reviewed document alone, setting aside a
design document published after the scoring, the 0.0 stands. It is a correction rather than polish: the score rests on
the design as its author now publishes it, which is how the pass reads every design. *Consequence:* Integral 14.0 → 14.5,
failures 3 → 2, tier Partially Adequate → Potentially Adequate; first place shared with CCO-PTF-CIP-SZH; Integral
dominates Doughnut Economics (a new pair). *Reopening:* a node operating the design's systems, toward the staged clause.

**3.4 Sovereign Wealth Fund Statism (decision 58.5, a correction).** The entry scores the mechanism, a state channelling a
large revenue stream into a permanently held fund whose returns support the public under a withdrawal rule, with
Norway's and Alaska's as exemplars and Timor-Leste's and New Zealand's as further cases (its scoring document, Overview).
Its published 0.5 rested on the absence of "a system-specific, phase-by-phase national implementation plan"; v2.0 asks
instead whether each element is shown feasible by precedent, and its own precedents show each. (1) *Staged:* Norway's
deployment ran in dated stages: the law (1990), the first capital transfer (1996), the investment manager and a 40%
equity share (1998), the fiscal rule tying transfers to the fund's expected real return (2001) (NBIM, *The history*;
the Ministry of Finance, *The Norwegian Fiscal Policy Framework*). (2) *Rapid:* Timor-Leste, independent in May 2002 after
the violence of 1999, consulted on its petroleum fund (comments due 30 November 2004), promulgated Law No. 9/2005 on
3 August 2005 and made the fund's first investments on 9 September 2005, ten months from the consultation's close, in a
post-conflict state, on Norway's model and with its advisers. (3) *Milestones:* dated targets set and met: a 40% equity
share decided in 1997 and reached in the first half of 1998; 60% decided in 2007 and reached in June 2009; the rule's
expected return revised from 4% to 3% in 2017. (4) *Resources:* documented: the revenue transferred (USD 79.6 million
from the Timor Gap Account at the first investment) and the institution to manage it, built in Timor-Leste with Norway's
assistance from 2002, about NOK 56 million to 2007, whose advisers Norad's review calls "instrumental to the
establishment of the petroleum fund and its operations". (5) *Risk mitigation:* investment abroad only, a spending rule
(Norway's expected real return; Timor-Leste's Estimated Sustainable Income, 3% of petroleum wealth), ethical guidelines
from 2004; Norway's fund has been kept under its rule and is worth more than four times mainland GDP. The unit is 1.0.
**Flagged** toward 0.5: read as requiring the pathway to be shown feasible where no large non-recurring revenue exists,
the resource clause is not shown, since New Zealand's budget-funded fund suspended its contributions from 2009 to 2017;
and Timor-Leste's parliament approved withdrawals above its rule in most years from 2008 (RSIS, 2018), so the risk clause
rests on Norway's record. C5.5 (cultural and economic adaptability) is the criterion that weighs the windfall
precondition; C5.2 asks whether the pathway's elements are shown deployable, and they are. *Consequence:* Sovereign Wealth
Fund Statism 12.5 → 13.0, no failure count or tier changes. It is the first C5.2 1.0 in the corpus whose clauses are
cleared rather than moot.

**3.5 The two 0.0s that hold (decision 58.6).** *Centrally Planned Socialism:* every transition to the configuration
located followed a seizure of power by force (Russia's revolution and civil war; China's civil war; occupation in Eastern
Europe; Czechoslovakia's coup of February 1948; Kornai, *The Socialist System*, chapter 2), and no gradual or democratic
transition to comprehensive central planning is located. Under reading 3.2(a) no clause is shown, and the unit holds at
0.0 on the 0.0 band's own reason. **Flagged** toward 0.5 on the alternative in 3.2(a), under which the Soviet and Eastern
European nationalisations, each within 36 months, clear the rapid clause. *Fully Automated Luxury Communism:* the
entry's destination rests on technologies not yet developed, together with a political transformation, and states no
pathway; no stage of it can be deployed before the technologies exist. No clause is shown; 0.0 holds on protocol 2.1's
first condition.

**3.6 The twelve that hold at 0.5 (decision 58.7).** Each states or has a pathway whose first stage is deployed in its
kind, short of the threshold (3.2(f)); the clause that fixes each verdict is in its table. *Participatory Economics* (read
closely, since it could decide first place): three levels against at least four, a theoretical possibility in the
entry's words, with no deployment of participatory planning of production at any level; its nearest components are
deployed at a municipality's and a state's scale (Porto Alegre's participatory budgeting from 1989; Kerala's People's
Campaign, which devolved 35 to 40% of a state's plan funds to local planning from August 1996); the staged clause is
short and no rapid pathway is stated. *Market Socialism* (the 0.5 band's anchor): cooperative development has grown in
stages at a region's scale (Mondragón), and the one economy-wide deployment, Yugoslavia's self-management, began from
capital nationalised after a revolution (3.2(a)). *Universal Basic Income:* no scaling of a partial payment in stages is
located; Alaska's dividend follows the fund's earnings. *Degrowth* and *Doughnut Economics:* first-stage experiments and
a first-stage methodology deployed in many places, no later stage and no rapid pathway. *Georgism:* its staged
precedent, the Australian Capital Territory's 20-year shift from conveyance duty to rates from 2012, ran in annual
steps, but a review for the Legislative Assembly's estimates committee (reported 3 July 2026) finds abolition by 2032
"extremely unlikely", the substitution having come to "a complete stop", with conveyance duty still about 10% of
own-source revenue in 2029-30; the clause its published rationale credited is short on the precedent's own record.
*Mutual Credit / LETS:* no deployment in dated stages; Argentina's barter networks scaled within months in 2001-2002 and
collapsed (3.2(c)); the register's flag toward 0.0 is kept. *Universal Basic Services:* staged cleared on Quebec's four
dated stages of universal childcare (1997 to 2000), the model for Canada's national programme from 2021, as part (b9)
cleared Stakeholder Capitalism's on one component's stages; rapid not shown for the package (Britain's health service,
legislated in 1946 and in force by July 1948, is one sector). *China:* the reform sequence from 1978 is a documented
staged transition, but from a party-state that came to power by revolution (3.2(a)). *Singapore:* documented stages of
components, and a political precondition secured by detentions without trial in 1963 that historians contest. *Qatar:*
staged national plans develop a configuration already in place; its precondition, resource rents per citizen, cannot be
deployed. *Ostrom-style Commons:* national programmes handed resources to commons over decades, none within 36 months;
the register's flag toward 0.0 is kept.

**3.7 Consequences (computed; section 5).** After decision 58.1 CCO-PTF-CIP-SZH is first alone at 14.5; after this
group first place is shared by CCO-PTF-CIP-SZH and Integral at 14.5, ahead of Participatory Economics at 14.0. Integral
changes tier, to Potentially Adequate; Sovereign Wealth Fund Statism rises to 13.0 and
shares fifth place. Seven entries are now Potentially Adequate. The corpus gains one dominance pair (Integral over
Doughnut Economics). C5.2's 0.0 band keeps Centrally Planned Socialism's example; its Integral example moves (section 5).

## 4. The units

### 4.1 Summary (generated)

Statuses by clause; "not estimated" marks a clause another clause's status fixes (section 2).

| Entry | Published | Staged | Rapid | Milestones | Resources | Risk | Verdict | Flag |
|---|---:|---|---|---|---|---|---:|---|
| CPS | 0.0 | not shown | not shown | not shown | not shown | not shown | 0.0 | toward 0.5 |
| MS | 0.5 | not shown | not shown | not estimated | not estimated | not estimated | 0.5 |  |
| UBI | 0.5 | not shown | not estimated | not estimated | not estimated | not estimated | 0.5 |  |
| DG | 0.5 | not shown | not shown | not estimated | not estimated | not estimated | 0.5 |  |
| FALC | 0.0 | not shown | not shown | not shown | not shown | not shown | 0.0 |  |
| PE | 0.5 | short | not shown | not estimated | not estimated | not estimated | 0.5 |  |
| INT | 0.0 | not shown | not shown | not shown | not shown | cleared | 0.5 | toward 0.0 |
| GEO | 0.5 | short | not shown | not estimated | not estimated | not estimated | 0.5 |  |
| MC | 0.5 | not shown | not shown | not estimated | not estimated | not estimated | 0.5 | toward 0.0 |
| DE | 0.5 | not shown | not shown | not estimated | not estimated | not estimated | 0.5 |  |
| UBS | 0.5 | cleared | not shown | not estimated | not estimated | not estimated | 0.5 |  |
| SWF | 0.5 | cleared | cleared | cleared | cleared | cleared | 1.0 | toward 0.5 |
| CN | 0.5 | not shown | not shown | not estimated | not estimated | not estimated | 0.5 |  |
| SG | 0.5 | not shown | not shown | not estimated | not estimated | not estimated | 0.5 |  |
| QA | 0.5 | not shown | not shown | not estimated | not estimated | not estimated | 0.5 |  |
| OS | 0.5 | not estimated | not shown | not estimated | not estimated | not estimated | 0.5 | toward 0.0 |

### 4.2 Clause by clause (generated)

#### CPS C5.2 Staged Transition Pathways: 0.0 → 0.0

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Staged (≥4 phases) | not shown | no gradual transition to comprehensive central planning in a stable context is located: every transition to the configuration followed a seizure of power by force, by revolution and civil war (Russia, 1917-1921; China, 1949), by occupation (Eastern Europe, 1945-1949) or by a coup (Czechoslovakia, February 1948); the later stages of each, the five-year plans and collectivisation, rest on it (readings 3.2(a), 3.5) | Report v1.6, System 3, C5.2; Kornai, The Socialist System: The Political Economy of Communism (Princeton, 1992), chapter 2, the revolutionary-transitional system |
| 2 | rapid (≤36 months) deployment | not shown | the configuration was imposed within 36 months more than once (Soviet collectivisation from 1929; the nationalisations in Eastern Europe after 1945), but each deployment rested on a seizure of power by force, which the criterion's rationale names as what a pathway is to avoid, and none was a deployment a polity could adopt by its own procedures (readings 3.2(a), 3.5) | Report v1.6, System 3, C5.2; Kornai, The Socialist System: The Political Economy of Communism (Princeton, 1992), chapter 2, the revolutionary-transitional system |
| 3 | specific milestones | not shown | the five-year plans set dated targets, but in deployments that rest on force; no milestone of a pathway the criterion credits is located (reading 3.5) | Report v1.6, System 3, C5.2; Kornai, The Socialist System: The Political Economy of Communism (Princeton, 1992), chapter 2, the revolutionary-transitional system |
| 4 | resource requirements | not shown | no statement of what a transition into the configuration takes, other than the seizure of power, is located (reading 3.5) | Report v1.6, System 3, C5.2 |
| 5 | risk mitigation | not shown | the entry's record shows rapid implementation 'invariably chaotic', and no mitigation of a transition's risks is stated or located (reading 3.5) | Report v1.6, System 3, C5.2 |

*0.0 (protocol 2.1):* every transition to the configuration located required non-gradual means, revolution, civil war, a coup or occupation (the 0.0 band's own example); no pathway the criterion credits exists to be shown feasible.

*Flag (reading 3.5):* toward 0.5: read as counting a deployment by any means, the rapid clause is cleared by the Soviet and Eastern European nationalisations, each within 36 months.

*Note:* the 0.0 band's anchor example; it holds.

#### MS C5.2 Staged Transition Pathways: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Staged (≥4 phases) | not shown | the entry's pathway is incremental cooperative development; its component has grown in stages at a region's scale (Mondragón from 1956), but no stage beyond a niche is located from a market economy, and the one economy-wide deployment of worker self-management in markets, Yugoslavia's (in stages from 1950 to 1976), began from capital nationalised after a revolution (readings 3.2(a), 3.6) | Report v1.6, System 4, C5.2 |
| 2 | rapid (≤36 months) deployment | not shown | the entry states no rapid pathway, and no deployment of a cooperative sector at an economy's scale within 36 months is located (reading 3.6) | Report v1.6, System 4, C5.2 |
| 3 | specific milestones | not shown | not estimated in this pass; the verdict is fixed by clause 1 and 2 | this unit's clause 1 and 2 |
| 4 | resource requirements | not shown | not estimated in this pass; the verdict is fixed by clause 1 and 2 | this unit's clause 1 and 2 |
| 5 | risk mitigation | not shown | not estimated in this pass; the verdict is fixed by clause 1 and 2 | this unit's clause 1 and 2 |

*Note:* the 0.5 band's anchor example; it holds: a pathway is sketched and its first stage has deployments of its kind, so the unit is not 0.0 (reading 3.2(f)).

#### UBI C5.2 Staged Transition Pathways: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Staged (≥4 phases) | not shown | the entry's pathway is to begin with a partial basic income and scale it upward; no such scaling in stages is located: the one long-running universal payment, Alaska's dividend (paid every year since 1982), follows the fund's earnings and the legislature's appropriation, not a schedule toward a full basic income (reading 3.6) | Report v1.6, System 7, C5.2; NEEC_SovereignWealthFundStatism_scoring_scratch.md, overview |
| 2 | rapid (≤36 months) deployment | not shown | not estimated in this pass; the verdict is fixed by clause 1 | this unit's clause 1 |
| 3 | specific milestones | not shown | not estimated in this pass; the verdict is fixed by clause 1 | this unit's clause 1 |
| 4 | resource requirements | not shown | not estimated in this pass; the verdict is fixed by clause 1 | this unit's clause 1 |
| 5 | risk mitigation | not shown | not estimated in this pass; the verdict is fixed by clause 1 | this unit's clause 1 |

*Note:* a pathway is sketched and its first stage, a universal payment, has been deployed, so the unit is not 0.0 (reading 3.2(f)); clause 2 is not estimated (section 8).

#### DG C5.2 Staged Transition Pathways: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Staged (≥4 phases) | not shown | the entry names municipal experiments, bioregional organisation and voluntary simplicity as pathways; no polity located has deployed a planned contraction of output in stages, and the experiments named are local (reading 3.6) | Report v1.6, System 8, C5.2 |
| 2 | rapid (≤36 months) deployment | not shown | the entry states no rapid pathway, and the transition it describes faces 'massive political and economic disruption'; none is located (reading 3.6) | Report v1.6, System 8, C5.2 |
| 3 | specific milestones | not shown | not estimated in this pass; the verdict is fixed by clause 1 and 2 | this unit's clause 1 and 2 |
| 4 | resource requirements | not shown | not estimated in this pass; the verdict is fixed by clause 1 and 2 | this unit's clause 1 and 2 |
| 5 | risk mitigation | not shown | not estimated in this pass; the verdict is fixed by clause 1 and 2 | this unit's clause 1 and 2 |

*Note:* a pathway is sketched and its first stage has deployments of its kind, so the unit is not 0.0 (reading 3.2(f)).

#### FALC C5.2 Staged Transition Pathways: 0.0 → 0.0

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Staged (≥4 phases) | not shown | no pathway is specified: the entry's destination rests on technologies not yet developed (general artificial intelligence, abundant clean energy and storage) together with a political transformation, and no stage of deployment of that destination is located or possible before they exist (reading 3.5) | Report v1.6, System 10, C5.2 |
| 2 | rapid (≤36 months) deployment | not shown | no rapid pathway is stated, and none can be deployed before the technologies exist (reading 3.5) | Report v1.6, System 10, C5.2 |
| 3 | specific milestones | not shown | no milestones are stated (reading 3.5) | Report v1.6, System 10, C5.2 |
| 4 | resource requirements | not shown | no resource requirements are stated (reading 3.5) | Report v1.6, System 10, C5.2 |
| 5 | risk mitigation | not shown | no risk mitigation for a transition is stated (reading 3.5) | Report v1.6, System 10, C5.2 |

*0.0 (protocol 2.1):* no structural mechanism addresses the criterion: 'fully automated' is a destination without a roadmap, whose defining condition cannot be deployed by any pathway until technologies not yet developed exist.

*Note:* one of the 0.0s the published C5.2 count names; it holds.

#### PE C5.2 Staged Transition Pathways: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Staged (≥4 phases) | short | three levels, municipal, regional and national, against at least four, stated as a theoretical possibility; no deployment of participatory planning of production is located at any level; its nearest components have deployments at the first levels' scale only: participatory budgeting of a share of municipal investment (Porto Alegre from 1989) and the Kerala People's Campaign, which devolved 35 to 40% of a state's plan funds to local planning from August 1996 (reading 3.6) | Report v1.6, System 11, C5.2; Isaac with Franke, Local Democracy and Development: The People's Campaign for Decentralized Planning in Kerala (LeftWord, 2000; Rowman and Littlefield, 2002) |
| 2 | rapid (≤36 months) deployment | not shown | the entry states no rapid pathway, and holds that coordination complexity makes partial implementation difficult and that planning needs critical mass; no deployment within 36 months is located (reading 3.6) | Report v1.6, System 11, C5.2 |
| 3 | specific milestones | not shown | not estimated in this pass; the verdict is fixed by clause 1 and 2 | this unit's clause 1 and 2 |
| 4 | resource requirements | not shown | not estimated in this pass; the verdict is fixed by clause 1 and 2 | this unit's clause 1 and 2 |
| 5 | risk mitigation | not shown | not estimated in this pass; the verdict is fixed by clause 1 and 2 | this unit's clause 1 and 2 |

*Note:* read closely, since with first place shared Participatory Economics' C5.2 could decide it; a pathway is sketched in levels and its first stage's components have deployments at municipal and state scale, so the unit holds at 0.5 and is not 0.0 (reading 3.2(f)).

#### INT C5.2 Staged Transition Pathways: 0.0 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Staged (≥4 phases) | not shown | the design's white paper, published after the corpus scored it, now states a staged pathway: proto-nodes grown from existing mutual aid networks, timebanks, tool libraries and repair cafés, each of the five systems formalised in three steps, and an arc of four stages, from marginal experiment to supplementary alternative, essential support layer and dominant substrate, 'inherently generational' and undated; its first stage's kind is deployed, but no node operating the design's systems is located: the project's site registers four communities in its own Phase 1, the building of its software (reading 3.3) | Joseph, INTEGRAL: Technical White Paper v0.1 (integralcollective.io, December 2025; PDF md5 a6defc9a, retrieved 2026-10-15), sections 11.1 to 11.4 and 11.11; integralcollective.io, home and community pages, retrieved 2026-10-15 |
| 2 | rapid (≤36 months) deployment | not shown | the white paper sets aside direct implementation in a nation-state as 'highly unlikely' and states no rapid pathway; none is located (reading 3.3) | Joseph, INTEGRAL: Technical White Paper v0.1 (integralcollective.io, December 2025; PDF md5 a6defc9a, retrieved 2026-10-15), section 11.1 |
| 3 | specific milestones | not shown | no milestones are stated: the transition's markers are 'incremental and often unremarkable' (reading 3.3) | Joseph, INTEGRAL: Technical White Paper v0.1 (integralcollective.io, December 2025; PDF md5 a6defc9a, retrieved 2026-10-15), section 11.11 |
| 4 | resource requirements | not shown | no resource requirements are stated; interface cooperatives take in external resources, without a figure (reading 3.3) | Joseph, INTEGRAL: Technical White Paper v0.1 (integralcollective.io, December 2025; PDF md5 a6defc9a, retrieved 2026-10-15), sections 11.5 and 11.6 |
| 5 | risk mitigation | cleared | section 11.10 specifies safeguards of kinds in use elsewhere: no single point of failure, peer-to-peer and federated infrastructure with replicated data, grounded in deployed technologies (decentralised identifiers, content-addressed storage, federated messaging); no central treasury; commons assets that cannot be pledged or sold; legal compliance as the default; and interface cooperatives with capped market exposure and sunset rules; component evidence in the sense of reading 3.2, as CCO-PTF-CIP-SZH's risk mitigation was cleared in part (b9) (reading 3.3) | Joseph, INTEGRAL: Technical White Paper v0.1 (integralcollective.io, December 2025; PDF md5 a6defc9a, retrieved 2026-10-15), sections 11.6 and 11.10 |

*Flag (reading 3.3):* toward 0.0: read on the source the corpus scored, the review's document, whose stated pathway is 'starts small and expands' (the 0.0 band's example), and setting aside a design document published after the scoring.

*Note:* re-read on the design's own white paper (v0.1, December 2025), as parts (b5) and (b8) read the design's own pages; the published 0.0's reason, that the source provides no phased pathway, no longer describes the design, and a clause is cleared, so 0.0 cannot hold (decision 53.2); read closely, since Integral's C5.2 could decide who is first.

#### GEO C5.2 Staged Transition Pathways: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Staged (≥4 phases) | short | the precedent the entry cites, the Australian Capital Territory's 20-year shift from conveyance duty to general rates, has run in annual budget steps since 2012 with published evaluations, but it is not shown to completion: a review for the Legislative Assembly's estimates committee finds abolition by the 2032 deadline 'extremely unlikely', the substitution having come to 'a complete stop', with conveyance duty still about 10% of own-source revenue in 2029-30 (reading 3.6) | NEEC_Georgism_LVT_scoring_scratch.md, C5.2; ACT Treasury, Tax Reform (treasury.act.gov.au/taxreform, retrieved 2026-10-15); Pegasus Economics' review for the Legislative Assembly's estimates committee, as reported in The Canberra Times, 3 July 2026 |
| 2 | rapid (≤36 months) deployment | not shown | no rapid pathway is located, and the one fast introduction, Britain's of 1910, is the entry's clearest failure case (reading 3.6) | NEEC_Georgism_LVT_scoring_scratch.md, C5.2; Report v1.6, System 14, C5.2 |
| 3 | specific milestones | not shown | not estimated in this pass; the verdict is fixed by clause 1 and 2 | this unit's clause 1 and 2 |
| 4 | resource requirements | not shown | not estimated in this pass; the verdict is fixed by clause 1 and 2 | this unit's clause 1 and 2 |
| 5 | risk mitigation | not shown | not estimated in this pass; the verdict is fixed by clause 1 and 2 | this unit's clause 1 and 2 |

*Note:* the staged clause, which the published rationale credited, is now short on the precedent's own record.

#### MC C5.2 Staged Transition Pathways: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Staged (≥4 phases) | not shown | no deployment in dated stages is located: classic LETS, WIR, Sardex and Grassroots Economics each started small and grew without a multi-phase design; the Credit Commons federation effort is a design, early-stage and untested at scale, and a plan shows nothing under the scope (reading 3.6) | NEEC_MutualCredit_LETS_scoring_scratch.md, C5.2 |
| 2 | rapid (≤36 months) deployment | not shown | Argentina's barter networks scaled within months in the 2001-2002 crisis and then collapsed: the pace is shown, not the feasibility of a deployment that reaches stable operation (reading 3.2(c)) | NEEC_MutualCredit_LETS_scoring_scratch.md, C5.2 and C3.1 |
| 3 | specific milestones | not shown | not estimated in this pass; the verdict is fixed by clause 1 and 2 | this unit's clause 1 and 2 |
| 4 | resource requirements | not shown | not estimated in this pass; the verdict is fixed by clause 1 and 2 | this unit's clause 1 and 2 |
| 5 | risk mitigation | not shown | not estimated in this pass; the verdict is fixed by clause 1 and 2 | this unit's clause 1 and 2 |

*Flag (reading 3.6):* toward 0.0: the register's flag, since the staged design effort has not been tested against the failure modes it is meant to solve.

*Note:* the mechanism has operated for decades in its networks (WIR since 1934), so the unit is not 0.0 (reading 3.2(f)); the register's flag toward 0.0 is kept.

#### DE C5.2 Staged Transition Pathways: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Staged (≥4 phases) | not shown | a first-stage methodology, the City Portrait process, has been followed in dozens of jurisdictions, but no stage beyond the initial portrait and strategy is specified or located (reading 3.6) | NEEC_DoughnutEconomics_scoring_scratch.md, C5.2 |
| 2 | rapid (≤36 months) deployment | not shown | no rapid pathway exists: Amsterdam's adoption in the pandemic reused an existing planning process (reading 3.6) | NEEC_DoughnutEconomics_scoring_scratch.md, C5.2 |
| 3 | specific milestones | not shown | not estimated in this pass; the verdict is fixed by clause 1 and 2 | this unit's clause 1 and 2 |
| 4 | resource requirements | not shown | not estimated in this pass; the verdict is fixed by clause 1 and 2 | this unit's clause 1 and 2 |
| 5 | risk mitigation | not shown | not estimated in this pass; the verdict is fixed by clause 1 and 2 | this unit's clause 1 and 2 |

*Note:* a first stage is deployed in many places, so the unit is not 0.0 (reading 3.2(f)).

#### UBS C5.2 Staged Transition Pathways: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Staged (≥4 phases) | cleared | component evidence: Quebec's universal childcare was deployed in four dated stages, to four-year-olds in 1997, three-year-olds in 1998, two-year-olds in 1999 and all children under five not in kindergarten in 2000, and was the model for Canada's national programme from 2021; the entry's pathway is sector by sector (reading 3.6) | NEEC_UniversalBasicServices_scoring_scratch.md, C5.2; Baker, Gruber and Milligan, Universal Child Care, Maternal Labor Supply, and Family Well-Being, NBER Working Paper 11832 (2005; Journal of Political Economy, 2008), as summarised in the NBER Digest, June 2006 |
| 2 | rapid (≤36 months) deployment | not shown | the entry states no rapid pathway; one sector has a precedent of rapid deployment (Britain's national health service, legislated in 1946 and in force by July 1948), but no deployment of the package of universal services within 36 months is located (reading 3.6) | NEEC_UniversalBasicServices_scoring_scratch.md, C5.2; the British National Insurance Act 1946 and National Health Service Act 1946, in force 5 July 1948 |
| 3 | specific milestones | not shown | not estimated in this pass; the verdict is fixed by clause 2 | this unit's clause 2 |
| 4 | resource requirements | not shown | not estimated in this pass; the verdict is fixed by clause 2 | this unit's clause 2 |
| 5 | risk mitigation | not shown | not estimated in this pass; the verdict is fixed by clause 2 | this unit's clause 2 |

*Note:* the staged clause is cleared on one sector's staged deployment, as part (b9) cleared Stakeholder Capitalism's on one component's; the rapid clause fixes the verdict.

#### SWF C5.2 Staged Transition Pathways: 0.5 → 1.0

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Staged (≥4 phases) | cleared | the mechanism's own deployment, in at least four dated stages in Norway: the fund's law (1990), its first capital transfer (1996), the investment manager and a 40% equity share (1998), and the fiscal rule tying spending to the fund's expected real return (2001) (reading 3.4) | Norges Bank Investment Management, The history (nbim.no, retrieved 2026-10-15); Ministry of Finance, The Norwegian Fiscal Policy Framework (regjeringen.no, retrieved 2026-10-15), and its press release of 16 February 2017 on the expected rate of return |
| 2 | rapid (≤36 months) deployment | cleared | a precedent of the same kind in a post-crisis context: Timor-Leste, independent in 2002 after the violence of 1999, put its petroleum fund out to public consultation (comments due 30 November 2004), promulgated its law on 3 August 2005 and made the fund's first investments on 9 September 2005, 10 months from the consultation's close (reading 3.4) | Timor-Leste, Petroleum Fund Law No. 9/2005, promulgated 3 August 2005; Petroleum Fund of Timor-Leste, Annual Report 2008 (first investments of 9 September 2005); La'o Hamutuk, the Ministry of Planning and Finance's public consultation on the fund (comments due 30 November 2004); NEEC_SovereignWealthFundStatism_scoring_scratch.md, C5.2 |
| 3 | specific milestones | cleared | dated targets were set and met: a 40% equity share decided in 1997 and reached in the first half of 1998; 60% decided in 2007 and reached in June 2009; the fiscal rule's expected return revised from 4% to 3% in 2017 (reading 3.4) | Norges Bank Investment Management, The history (nbim.no, retrieved 2026-10-15); Ministry of Finance, The Norwegian Fiscal Policy Framework (regjeringen.no, retrieved 2026-10-15), and its press release of 16 February 2017 on the expected rate of return |
| 4 | resource requirements | cleared | what the deployments took is documented: the capital, the revenue stream transferred into the fund (in Timor-Leste, USD 79.6 million from the Timor Gap Account at the first investment), and the institution to manage it, built in Timor-Leste with Norway's assistance from 2002, about NOK 56 million to 2007, whose advisers were 'instrumental to the establishment of the petroleum fund and its operations' (reading 3.4) | Timor-Leste, Petroleum Fund Law No. 9/2005, promulgated 3 August 2005; Petroleum Fund of Timor-Leste, Annual Report 2008 (first investments of 9 September 2005); La'o Hamutuk, the Ministry of Planning and Finance's public consultation on the fund (comments due 30 November 2004); Norad, Review of TIM 2010: Assistance in developing the management of the petroleum sector in Timor-Leste (2007), on Norway's assistance since 2002 (about NOK 56 million, 2002-2007) |
| 5 | risk mitigation | cleared | the deployments' mitigations operated: assets invested abroad only, a spending rule tying transfers to the expected real return (Norway) or to 3% of petroleum wealth (Timor-Leste), ethical guidelines from 2004; Norway's fund has been kept and has grown to more than four times mainland GDP under the rule, though Timor-Leste's parliament approved withdrawals above its rule in most years from 2008 (reading 3.4) | Norges Bank Investment Management, The history (nbim.no, retrieved 2026-10-15); Ministry of Finance, The Norwegian Fiscal Policy Framework (regjeringen.no, retrieved 2026-10-15), and its press release of 16 February 2017 on the expected rate of return; RSIS Commentary CO18026, Timor-Leste's Oil: Blessing or Curse? (15 February 2018); NEEC_SovereignWealthFundStatism_scoring_scratch.md, overview |

*Flag (reading 3.4):* toward 0.5: read as requiring the pathway to be shown feasible where no large non-recurring revenue exists, the resource clause is not shown (New Zealand's budget-funded fund suspended its contributions from 2009 to 2017), and Timor-Leste's repeated withdrawals above its rule leave the risk clause resting on Norway alone.

*Note:* every clause is shown by deployments of the mechanism itself, which the published 0.5, judged on the absence of a phase-by-phase plan, did not credit; under v2.0's scope a precedent, not a plan, is the test (part (b9), reading 3.2).

#### CN C5.2 Staged Transition Pathways: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Staged (≥4 phases) | not shown | the reform sequence is one of the best-documented staged transitions, local experiments first and national policy after, sector by sector from 1978, and Vietnam adapted it; but each runs from a party-state that came to power by revolution and civil war, which the entry names as defining, and no polity located has reached the configuration by stages from a pluralist starting point (readings 3.2(a), 3.6) | NEEC_StateCapitalism_China_scoring_scratch.md, C5.2 |
| 2 | rapid (≤36 months) deployment | not shown | no rapid pathway is stated or located (reading 3.6) | NEEC_StateCapitalism_China_scoring_scratch.md, C5.2 |
| 3 | specific milestones | not shown | not estimated in this pass; the verdict is fixed by clause 1 and 2 | this unit's clause 1 and 2 |
| 4 | resource requirements | not shown | not estimated in this pass; the verdict is fixed by clause 1 and 2 | this unit's clause 1 and 2 |
| 5 | risk mitigation | not shown | not estimated in this pass; the verdict is fixed by clause 1 and 2 | this unit's clause 1 and 2 |

*Note:* a staged sequence of the configuration's market components is real and replicated, so the unit is not 0.0 (reading 3.2(f)).

#### SG C5.2 Staged Transition Pathways: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Staged (≥4 phases) | not shown | parts of the model have documented, sequenced histories (Temasek's incorporation in 1974 from existing state holdings, the privatisation programme of 1985-1987, the transfer of administrative know-how to Suzhou), but they are stages of components, not four stages of the configuration, and its political precondition was secured by Operation Coldstore's detentions without trial in 1963, an episode whose purpose historians contest (reading 3.6) | NEEC_StateCapitalism_Singapore_scoring_scratch.md, C5.2 |
| 2 | rapid (≤36 months) deployment | not shown | no rapid pathway is stated or located; the pathway unfolded over decades in a city-state (reading 3.6) | NEEC_StateCapitalism_Singapore_scoring_scratch.md, C5.2 |
| 3 | specific milestones | not shown | not estimated in this pass; the verdict is fixed by clause 1 and 2 | this unit's clause 1 and 2 |
| 4 | resource requirements | not shown | not estimated in this pass; the verdict is fixed by clause 1 and 2 | this unit's clause 1 and 2 |
| 5 | risk mitigation | not shown | not estimated in this pass; the verdict is fixed by clause 1 and 2 | this unit's clause 1 and 2 |

*Note:* documented sequences and a demonstrated transfer method, so the unit is not 0.0 (reading 3.2(f)).

#### QA C5.2 Staged Transition Pathways: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Staged (≥4 phases) | not shown | Qatar's multi-phase plans (the National Vision 2030 and three national development strategies, the third for 2024-2030) develop a configuration already in place; they are not a pathway into it, and its precondition, large resource rents per citizen, cannot be deployed (reading 3.6) | NEEC_StateCapitalism_Qatar_scoring_scratch.md, C5.2 |
| 2 | rapid (≤36 months) deployment | not shown | no rapid pathway exists (reading 3.6) | NEEC_StateCapitalism_Qatar_scoring_scratch.md, C5.2 |
| 3 | specific milestones | not shown | not estimated in this pass; the verdict is fixed by clause 1 and 2 | this unit's clause 1 and 2 |
| 4 | resource requirements | not shown | not estimated in this pass; the verdict is fixed by clause 1 and 2 | this unit's clause 1 and 2 |
| 5 | risk mitigation | not shown | not estimated in this pass; the verdict is fixed by clause 1 and 2 | this unit's clause 1 and 2 |

*Note:* documented staged planning of the configuration itself, so the unit is not 0.0 (reading 3.2(f)).

#### OS C5.2 Staged Transition Pathways: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Staged (≥4 phases) | not shown | not estimated in this pass; the verdict is fixed by clause 2 | this unit's clause 2 |
| 2 | rapid (≤36 months) deployment | not shown | the framework declines to be a deployment plan; the national programmes that handed resources to commons did so over decades (Nepal's community forestry under the Forest Act 1993 and Regulation 1995, to more than 22,000 groups; India's Joint Forest Management), and no deployment within 36 months is located (reading 3.6) | NEEC_Ostrom_Commons_scoring_scratch.md, C5.2 |
| 3 | specific milestones | not shown | not estimated in this pass; the verdict is fixed by clause 2 | this unit's clause 2 |
| 4 | resource requirements | not shown | not estimated in this pass; the verdict is fixed by clause 2 | this unit's clause 2 |
| 5 | risk mitigation | not shown | not estimated in this pass; the verdict is fixed by clause 2 | this unit's clause 2 |

*Flag (reading 3.6):* toward 0.0: the register's flag, on the reading that the framework's own refusal to specify a pathway governs, and that national forestry statutes implement policy rather than the scored mechanism.

*Note:* national programmes deployed the mechanism in stages, so the unit is not 0.0 (reading 3.2(f)); clause 1, which those programmes bear on, is not estimated, since clause 2 fixes the verdict; the register's flag toward 0.0 is kept.

### 4.3 The owner's part 58.1 (generated)

#### CCO C3.2 Inflation Control Mechanisms: 0.5 → 1.0 (part 58.1)

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Long-term inflation ≤3% | cleared | on the owner's reading the design's backing of the currency by creative output, a community chest, is an original feature of the design and is read as backing what the Source pays; at full backing the design's published model raises prices 0.1% a year over 20 years in the Reference environment, in every seed under 3%; the dual-currency paper's own simulations give 0.95% a year; held until an empirical study shows that the backing does not hold in real-world data | the owner's decision 58.1 (ledger d37, 2026-10-15); Compassionism Simulation at d10ed6e (v5.6.0), the v5.6 release's engine; cco_sim_v56_checks_s57_output.txt, its Reference row at full backing (H1, a = 1); research hub at 8e8a6ba, dual-currency-inflation.html (md5 329235ce), sections 5.2 and 5.4 |
| 2 | stress test inflation ≤5% (when external 8%) | cleared | carried, as group 2.1 carried it, on the framework paper's 8% scenario, in which local inflation is held to 3.2% while national inflation reaches 8.1%; the design's published model carries no 8% scenario, so it does not contradict the figure | the owner's decision 58.1 (ledger d37, 2026-10-15); research hub at 8e8a6ba, cco-ptf-integrated-framework.html (md5 10ab8364), section 5.2 |
| 3 | automatic adjustment preventing runaway inflation | cleared | carried, as group 2.1 carried it, on the design's automatic parameter adjustment (the dual-currency paper's adjustment rules); with every dollar the Source pays backed by new output, the model shows no runaway inflation for an adjustment to prevent | the owner's decision 58.1 (ledger d37, 2026-10-15); research hub at 8e8a6ba, dual-currency-inflation.html (md5 329235ce), section 5.4; Compassionism Simulation at d10ed6e (v5.6.0), the v5.6 release's engine; cco_sim_v56_checks_s57_output.txt, its Reference row at full backing (H1, a = 1) |

*Flag (reading 3.1):* toward 0.5: group 2.5's reading (decision 57.7): the design states no backing share; on the model's main reading the programme raises prices 50.8% a year, no 8% scenario is modelled, and the one automatic adjustment modelled raises the payout with prices rather than restraining issuance.

*Note:* the owner's decision 58.1 restores the published 1.0 and supersedes group 2.5's unit (decision 57.7, S57-3.9); it reopens toward 0.5 on an empirical study showing that the backing by creative output does not hold in real-world data.

## 5. What parts (a), (b), groups 2.1 to 2.5, decision 58.1 and group 2.6 change (generated)

Totals on the published 26-criterion structure, with every re-estimate of the pass in force; ranks are by total.

| Entry | Published (rank) | After decision 58.1 (rank) | After group 2.6 (rank) | Change here | Failures | Tier |
|---|---:|---:|---:|---:|---:|---|
| CCO | 24.5 (1) | 14.5 (1) | 14.5 (1) | 0.0 | 0 | Potentially Adequate |
| PE | 20.5 (2) | 14.0 (2) | 14.0 (3) | 0.0 | 1 | Potentially Adequate |
| NSD | 19.5 (3) | 13.5 (4) | 13.5 (4) | 0.0 | 1 | Potentially Adequate |
| INT | 19.5 (3) | 14.0 (2) | 14.5 (1) | 0.5 | 2 | Potentially Adequate |
| DG | 19.0 (5) | 13.0 (5) | 13.0 (5) | 0.0 | 2 | Potentially Adequate |
| MS | 16.5 (6) | 13.0 (5) | 13.0 (5) | 0.0 | 2 | Potentially Adequate |
| MMT | 15.5 (7) | 11.0 (14) | 11.0 (14) | 0.0 | 4 | Partially Adequate |
| UBI | 14.5 (8) | 11.0 (14) | 11.0 (14) | 0.0 | 7 | Structurally Inadequate |
| MC | 14.5 (8) | 12.5 (8) | 12.5 (9) | 0.0 | 3 | Partially Adequate |
| OS | 14.5 (8) | 13.0 (5) | 13.0 (5) | 0.0 | 3 | Partially Adequate |
| SWF | 14.0 (11) | 12.5 (8) | 13.0 (5) | 0.5 | 3 | Partially Adequate |
| SG | 14.0 (11) | 11.5 (11) | 11.5 (11) | 0.0 | 4 | Partially Adequate |
| GEO | 13.5 (13) | 12.5 (8) | 12.5 (9) | 0.0 | 2 | Potentially Adequate |
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

After this group the corpus has 17 dominance pairs against 16 after decision 58.1 (new: INT>DE; lost: none), and its frontier holds 15 entries against 15 (SQ, NSD, CPS, MS, LM, UBI, DG, FALC, PE, CCO, INT, MC, SWF, IF, OS). First place is shared by CCO and INT at 14.5 (CCO 14.5, INT 14.0 after decision 58.1), ahead of PE at 14.0. Across the pass so far 231 units have been re-estimated, each counted once: 18 are at 1.0, 194 at 0.5 and 19 at 0.0; against their published scores 147 fell, 7 rose and 77 are unchanged (net -70.0 points).

**The score ledger:** each entry's published total, the change each part has made, and its total now.

| Entry | Published | (a) | (b1) | (b2) | (b3) | (b4) | (b5) | (b6) | (b7) | 48.3 | (b8) | (b9) | (2.1) | (2.2) | (2.3) | (2.4) | (2.5) | 58.1 | (2.6) | Now | Re-estimated | At 0.5 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| CCO | 24.5 | -0.5 | -1.5 | -0.5 | -0.5 | -0.5 | -0.5 | -1.0 | -0.5 | -0.5 | -0.5 | -1.0 | -1.5 | -0.5 | -0.5 |  | -0.5 | 0.5 |  | 14.5 | 22 | 20 |
| PE | 20.5 |  | -1.5 | -0.5 | -0.5 | -1.5 |  | -0.5 | -0.5 |  | -0.5 | -0.5 |  |  | -0.5 |  |  |  |  | 14.0 | 17 | 16 |
| NSD | 19.5 | -2.5 | -1.0 | -0.5 | -0.5 | -0.5 |  |  |  |  | -0.5 | -0.5 |  | -0.5 |  | 0.5 |  |  |  | 13.5 | 15 | 14 |
| INT | 19.5 | -0.5 | -1.0 | -0.5 |  | -1.0 | -0.5 | -1.0 | -0.5 |  |  |  |  |  | -0.5 |  |  |  | 0.5 | 14.5 | 15 | 12 |
| DG | 19.0 |  | -1.5 | -0.5 | -0.5 | -0.5 |  | -0.5 | -1.0 |  | -1.0 |  |  |  | -0.5 |  |  |  |  | 13.0 | 15 | 15 |
| MS | 16.5 | -1.0 | -1.5 | -0.5 | -0.5 |  |  |  | 0.5 |  |  |  |  | -0.5 |  |  |  |  |  | 13.0 | 12 | 10 |
| MMT | 15.5 | -1.5 | -1.0 | -0.5 | -0.5 |  |  |  |  |  | -0.5 |  |  | -0.5 |  |  |  |  |  | 11.0 | 10 | 8 |
| UBI | 14.5 | -1.5 | -0.5 | -0.5 | -0.5 |  |  |  |  |  | -0.5 |  |  |  |  |  |  |  |  | 11.0 | 12 | 9 |
| MC | 14.5 |  | -1.0 | -0.5 |  |  | -0.5 |  |  |  |  |  |  |  |  |  |  |  |  | 12.5 | 9 | 6 |
| OS | 14.5 | -0.5 |  |  |  |  | -0.5 | -0.5 |  |  |  |  |  |  |  |  |  |  |  | 13.0 | 8 | 6 |
| SWF | 14.0 |  |  | -0.5 |  |  | -0.5 | -0.5 |  |  |  |  |  |  |  |  |  |  | 0.5 | 13.0 | 8 | 5 |
| SG | 14.0 | -1.0 | -0.5 | -0.5 |  |  |  |  |  |  |  |  |  | -0.5 |  |  |  |  |  | 11.5 | 7 | 7 |
| GEO | 13.5 | -0.5 |  |  |  |  | -0.5 |  |  |  |  |  |  |  |  |  |  |  |  | 12.5 | 6 | 5 |
| UBS | 13.5 |  | -0.5 | -0.5 |  |  | -0.5 |  |  |  |  |  |  |  |  | -0.5 |  |  |  | 11.5 | 8 | 5 |
| IF | 13.5 | -1.0 |  |  |  |  | -0.5 |  |  |  |  | -0.5 |  |  |  |  |  |  |  | 11.5 | 7 | 7 |
| FALC | 13.0 | -0.5 | -0.5 |  | -0.5 | -1.0 |  | -0.5 | -0.5 |  |  |  |  |  | -0.5 |  |  |  |  | 9.0 | 12 | 9 |
| DE | 11.5 | -0.5 | -0.5 |  |  |  | -0.5 | -0.5 | -0.5 |  |  |  |  |  |  |  |  |  |  | 9.0 | 9 | 8 |
| SQ | 10.5 | -0.5 |  |  |  | -0.5 |  |  |  |  |  |  |  |  |  |  |  |  |  | 9.5 | 6 | 5 |
| CPS | 10.0 | -1.5 |  |  | -0.5 |  |  |  |  |  | -0.5 |  |  |  |  |  |  |  |  | 7.5 | 8 | 5 |
| SC | 10.0 |  | -1.0 |  |  |  |  |  |  |  |  | -0.5 |  |  |  | 0.5 |  |  |  | 9.0 | 6 | 6 |
| CN | 10.0 |  |  | -0.5 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 9.5 | 5 | 4 |
| QA | 9.0 | -0.5 |  | -0.5 |  |  |  |  |  |  |  |  |  |  |  | 0.5 |  |  |  | 8.5 | 6 | 6 |
| LM | 8.0 | -1.5 |  |  |  |  |  |  |  |  |  | -0.5 |  | 0.5 |  | 0.5 |  |  |  | 7.0 | 8 | 6 |

Anchor examples citing a unit the pass moves: C1.1's 1.0 example, NSD (part (b3)); C1.2a's 1.0 example, MS (part (2.2)); C1.2b's 1.0 example, CCO (part (2.5)); C1.4's 1.0 example, CCO (part (2.5)); C2.1's 1.0 example, UBI (part (a)); C2.3's 1.0 example, DG (part (b1)); C2.4's 1.0 example, PE (part (b1)); C2.5's 1.0 example, CCO (part (b5)); C3.1's 1.0 example, UBI (part (b2)); C3.2's 1.0 example, PE (part (b4)); C3.5's 1.0 example, CCO (part (b6)); C3.5's 0.0 example, LM (part (2.4)); C3.5's 0.0 example, SC (part (2.4)); C4.1's 1.0 example, DG (part (b6)); C4.2's 1.0 example, PE (part (b7)); C4.3's 1.0 example, CCO (part (b8)); C5.1's 1.0 example, MS (part (b2)); C5.2's 1.0 example, CCO (part (b9)); C5.2's 0.0 example, INT (part (2.6)); C5.4's 1.0 example, CCO (part (b9)); C5.5's 1.0 example, PE (part (b9)). Bands whose example the pass moves and which no corpus unit then scores at their value: C1.1's 1.0, C1.2a's 1.0, C2.1's 1.0, C2.3's 1.0, C2.4's 1.0, C3.1's 1.0, C3.5's 1.0, C4.1's 1.0, C4.2's 1.0, C4.3's 1.0.

## 6. Corrections found (not polish)

- **Integral's C5.2, 0.0 → 0.5 (decision 58.4):** the published reason no longer describes the design, whose own white
  paper states a staged pathway and clears risk mitigation on the reading the pass gave CCO-PTF-CIP-SZH's.
- **Sovereign Wealth Fund Statism's C5.2, 0.5 → 1.0 (decision 58.5):** v2.0's scope asks for precedent, not a plan, and
  the mechanism's own deployments show every element.
- **Georgism's staged clause (decision 58.7):** credited in the published rationale, short on the precedent's record of
  2026; the verdict is unchanged.
- **CCO-PTF-CIP-SZH's C3.2 (decision 58.1):** the owner's reversal of decision 57.7; recorded, not a finding of this group.

## 7. Disclosure

The readings are Claude's, under the owner's delegation. Integral's rise ties CCO-PTF-CIP-SZH, the owner's design, for
first place; the pass checked that the reading which raises Integral is the one it applied to the owner's design (its
risk clause in part (b9)), and that the reading which would hold Integral at 0.0 is recorded as a flag. No verdict here
favours the owner's design: none of its units is read in this group, and decision 58.1 is the owner's, recorded as given.
Sources were read in this session on 2026-10-15: Integral's white paper (PDF md5 a6defc9a) and site; NBIM's history and
the Norwegian Ministry of Finance's fiscal framework; Timor-Leste's Petroleum Fund Law, the Fund's 2008 annual report and
La'o Hamutuk's consultation notice (through search summaries); Norad's 2007 review; RSIS's 2018 commentary; the NBER
summary of Baker, Gruber and Milligan; the ACT Treasury's tax reform page and The Canberra Times' report of 3 July 2026;
Isaac and Franke on the Kerala campaign (publisher's summary). No evidence cache was built for this group (a class M
re-read; `STATE.md`, Next work); the figures used are held in `rescoring_s58.py`. The automated interpretation check
(Jev) was not run.

## 8. What remains

- **Clauses not estimated (38):** Market Socialism, Degrowth, Participatory Economics, Georgism, Mutual Credit / LETS,
  Doughnut Economics, China, Singapore and Qatar, clauses 3 to 5; Universal Basic Services, clauses 3 to 5; Universal
  Basic Income, clauses 2 to 5; Ostrom-style Commons, clauses 1, 3, 4 and 5. For Report v2.0's clause-level Part I.
- **Decision 58.2:** S57-3.3 paused at the owner's request until CCO-PTF-CIP-SZH's readings are all in.
- **Next group** by the triage, rerun after this group (`triage_s52_output.txt`).
- **The criteria record** at its next amendment carries reading 3.2 (decision 58.3) with the earlier method choices.

## 9. What this record does not show

It re-reads C5.2's clauses on the evidence located in this session. It does not show that any pathway would succeed: by
part (b9)'s reading, political and economic success are C5.1's and C5.4's questions. The precedents searched for are those
the entries' sources name and those the pass located; a deployment located elsewhere, of an Integral node, of a
participatory plan of production, or of a basic income scaled in stages, could reopen a unit. Sovereign Wealth Fund
Statism's 1.0 rests on precedents in states with large resource revenues and on Norway's governance; Integral's 0.5 rests
on a document published after the scoring, and its flag records the reading without it.
