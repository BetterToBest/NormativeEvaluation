#!/usr/bin/env python3
"""
adjudicate_s83.py -- NEEC: the adjudication of the outside review's verdict disagreements (Session 83, ledger S65)
================================================================================================================
The outside blind review (run r1) read all 667 units; its reader's verdict differs from NEEC's on 177
(compare_outside.py, NEEC_OutsideReview_Result_s82.md). Session 83 adjudicated every one on the sources, by one rule for
every entry (NEEC_Adjudication_s83.md, section 2): the protocol as written, the unit's pack, the reader's stated estimates
and sources, Jev's clause choices and NEEC's record. An adjudication holds NEEC's verdict, adopts the reader's, or reaches a
third reading. This file holds the result, in the form of the pass's units, as a layer over the owner's decisions of
Session 79 (final_pass.adjudicated_state(); apply_adjudication_s83.py writes the v2 files from it).

  OUTCOMES   one line per disagreement (177): unit, outcome, NEEC's verdict, the reader's, the verdict that now stands,
             and the reason in one sentence. Outcomes: hold, adopt, third (applied under the delegation, decision 57.2);
             owner (a CCO-PTF-CIP-SZH unit or an owner-decided cell whose adjudicated reading differs: not applied, put to
             the owner, published either way); stands (an owner-decided cell on which the adjudication finds no fact the
             owner's decision did not weigh).
  UNITS      the units this layer writes: kind 'change' (a verdict moves), 'revision' (a clause's reading is corrected, the
             verdict holds) or 'flag' (a held verdict gains the reader's reading, or another, as its close call). Each is a
             whole unit: verdict, clauses (status, estimate, source), flag, note, zero.
  OWNER      the four adjudicated readings that go to the owner, each with the unit it would write; never applied here.

No main; nothing is printed. Deterministic.
"""

TAG = "adjudication s83"
SESSION = 83
RECORD = "NEEC_Adjudication_s83.md"
DATE = "2026-10-20"
LABEL = "the adjudication of the outside review (Session 83)"

# unit | outcome | NEEC | reader | stands | reason (one sentence; the record, section 4, gives each in full)
OUTCOMES_TEXT = """
CCO|C1.2a|stands|1.0|0.5|1.0|the reader's not shown repeats the reading before decision 79.1 (no backing) and adds no fact the decision did not weigh; stage B held 0.5
CCO|C2.2|owner|1.0|0.5|1.0|the design's text pays citizens and legal residents aged 18 or more, and its own model leaves adults below their cost of living
CCO|C2.5|stands|1.0|0.5|1.0|the reader's short clause 1 (the Acre Equity haircut) is the question decision 79.2 decided
CCO|C3.4|stands|1.0|0.5|1.0|the reader's clause 4 rests on stability across participation levels and crisis scenarios, not on parameter adjustments, the reading decision 79.3 decided
CCO|C4.3|hold|0.5|0.0|0.5|a universal floor is a mechanism (the 0.5 band's formal equality); the reader reads Universal Basic Income at 0.5 on the same pattern
CCO|C5.1|hold|0.5|0.0|0.5|three of five components have twenty-year precedents (WIR, Alaska's dividend, land trusts): the 0.5 band, not 0.0's no comparable record
CCO|C5.2|hold|0.5|1.0|0.5|the reader cleared every clause on the plans' existence without the scope the threshold sets: each shown feasible by precedent or component evidence
CCO|C5.3|owner|1.0|0.5|1.0|the design's modelling paper (minimum viable participation 55%), its BLEI paper (self-funding at 60-65%) and its model's run warning outweigh the framework paper's 30%
NSD|C2.5|hold|0.5|1.0|0.5|benefits conditioned on availability for work are differential treatment, which the reader itself reads so for Status Quo
NSD|C2.6|hold|0.5|1.0|0.5|Sweden's quarantine has no time limit and its area closure cannot be appealed to a court (Smittskyddslag 3:9, 3:10, 8:1); the reader does not engage the text
NSD|C3.3|hold|0.5|1.0|0.5|the reader's 1.0 rests on projection for two of the four scenarios, where a configured economy is read on documented outcomes (4.1)
NSD|C3.4|hold|0.5|1.0|0.5|the reader's clause 4 window (2000-2026) leaves out the banking crises that followed the 1980s liberalisation in Finland, Norway and Sweden
NSD|C4.1|hold|0.5|1.0|0.5|a configuration of four economies clears only where each does (Finland 88.4% of GDP in 2025); the reader's aggregate is the reading NEEC already flags
NSD|C4.6|hold|0.5|1.0|0.5|the reader's cited liability cases could not be traced and do not match the known record; the clause stays not shown, flagged toward 1.0
NSD|C5.1|hold|0.5|1.0|0.5|a judgement NEEC already flags toward 1.0; on the Societal Poverty Line the headcount rose in all four economies from 2005
NSD|C5.3|hold|0.5|0.0|0.5|NEEC's reading is the 0.5 band's own text (components adopted piecemeal); 0.0 needs a system that cannot function at all at partial adoption
DG|C1.2a|hold|0.5|0.0|0.5|land trusts and cooperatives are a collective vehicle; the design rejects growth, not resilience, so 0.0's exclusion of the concern is not shown
DG|C1.2b|adopt|1.0|0.5|0.5|no source estimates the wealth distribution: caps on the top and commons do not bound a Gini, and the design keeps private property and markets
DG|C3.3|adopt|1.0|0.5|0.5|no source estimates the degradation of any core function under the compound scenarios; a design feature named by the 1.0 band is not an estimate
DG|C3.4|owner|1.0|0.5|1.0|decision 79.4's rule needs clauses 1 to 3 cleared; clauses 1 and 2 rest on the published rationale's words, which no source estimates
DG|C4.2|hold|0.5|1.0|0.5|degrowth's own scenario researchers write that its scenarios have not yet been explored for biodiversity (Otero et al.), so clause 2 is not shown
DG|C5.3|hold|0.5|0.0|0.5|local components function (transition towns, eco-villages): the 0.5 band
DG|C5.4|hold|0.0|0.5|0.0|the 0.0 band's rhetorical repulsion: the name is chosen as a provocation, and the reader's own estimate (15-30% support) is far below 60%; flagged toward 0.5
PE|C1.3|hold|0.5|1.0|0.5|no stability rate is stated, and housing in the design is consumption debited against an effort-rated budget, not free
PE|C1.5|hold|0.5|0.0|0.5|universal council access to the collective mechanism the reader itself credits at 0.5 on C1.2a
PE|C2.5|hold|0.5|0.0|0.5|the design allows a consumption allowance for those who do not want to work (Hahnel and Wright, 2016), against the reader's clause 2
PE|C3.3|adopt|1.0|0.5|0.5|no source estimates the degradation of any core function under the compound scenarios; distributed decision-making is a feature, not an estimate
PE|C3.4|owner|1.0|0.5|1.0|decision 79.4's rule needs clauses 1 to 3 cleared; clause 2 rests on the published rationale's words, which no source estimates
PE|C4.1|hold|0.5|1.0|0.5|councils and federations carry the year's differences as debt, with no rule bounding them (Hahnel and Wright, 2016); Jev reads both clauses not shown
PE|C5.1|hold|0.5|0.0|0.5|participatory budgeting and worker councils have records; the 0.5 band, as for CCO-PTF-CIP-SZH and Integral
PE|C5.3|hold|0.5|0.0|0.5|the 0.5 band: participatory institutions function at partial adoption
INT|C1.2b|adopt|1.0|0.5|0.5|the design removes accumulation inside its network but grows in parallel with market and state systems, and no source estimates the distribution; Jev reads it not shown
INT|C1.5|hold|0.0|0.5|0.0|the reader's own estimate (0% with a pathway) is 2.1's no mechanism
INT|C3.2|hold|0.5|1.0|0.5|clause 2's basis is corrected (the white paper does specify a one-way monetary boundary, section 11.6), but no source estimates inflation under an external 8% while nodes buy from markets; flagged toward 1.0
INT|C3.3|adopt|1.0|0.5|0.5|the 1.0 cites a review's estimate of degradation under 25%, which does not show under 20%, and the white paper gives none; Jev reads it not shown
INT|C3.4|stands|1.0|0.5|1.0|clauses 1 to 3 are cleared on the white paper's text (the reader missed the drought example and Modules 1 and 10); clause 4 is decision 79.4's
INT|C5.1|hold|0.5|0.0|0.5|cooperatives, land trusts and deliberation platforms have records; the white paper concedes the integration layer is untested: the 0.5 band
INT|C5.3|hold|0.5|1.0|0.5|clause 4 is now cleared on the white paper's protocols, but 'derived from empirical system modeling' describes how thresholds will be set, not a model validating the scaling path
MMT|C1.2a|hold|0.0|0.5|0.0|income only: no structural mechanism addresses wealth building (Session 53's line); the reader applies no 0.0 test
SG|C1.2a|hold|0.5|1.0|0.5|the reader counts citizens and permanent residents; the protocol counts everyone who lives and works there (3.2), and Work Permit holders have no vehicle
CPS|C1.2a|hold|0.0|0.5|0.0|the households' deposits were frozen and erased in 1992 (4.1, collapse included); the reader's own estimate is far below
UBI|C1.2a|hold|0.0|0.5|0.0|income only: no structural mechanism addresses wealth building; the reader applies no 0.0 test
FALC|C1.2a|hold|0.0|0.5|0.0|no vehicle is specified; the reader's own estimate says the design replaces individual wealth building
GEO|C1.2a|hold|0.0|0.5|0.0|the dividend is income; lower taxes raise the host's saving, which reach does not credit
DE|C1.2a|hold|0.0|0.5|0.0|the framework adopts no vehicle of its own
OS|C1.2a|hold|0.0|0.5|0.0|use-rights, not assets; the reader's own estimate agrees
CPS|C1.2b|hold|0.5|1.0|0.5|the reader's 0.30-0.35 straddles the bar and is attributed to works on income and on post-Soviet wealth; NEEC's contestable flag stands
DE|C1.2b|hold|0.0|0.5|0.0|the framework adopts no mechanism of its own, as on C1.2a
UBS|C1.2b|hold|0.0|0.5|0.0|the reader's own estimate finds no anti-concentration mechanism
QA|C1.2b|hold|0.5|0.0|0.5|commentary on UBS's figures puts Qatar's wealth Gini near 48 (2023), short but not far below; the citizens' allocation covers part of the population
IF|C1.2b|hold|0.0|0.5|0.0|zakat is outside the mechanism on the scoring document's scope decision (D31); the reader's 0.5 is the flagged scope scenario
SC|C1.2b|hold|0.0|0.5|0.0|the reader's own estimate finds no structural cap; it applies no 0.0 test
FALC|C1.2b|third|0.0|1.0|0.5|NEEC's 0.0 rests on unresolved risk, which 2.1 places at 0.5; the reader's 1.0 has no estimate of the distribution
MC|C1.2b|adopt|1.0|0.5|0.5|out of reach: mutual credit governs exchange balances, not the holdings of land, capital and savings that set a wealth Gini
SQ|C1.1|hold|0.5|0.0|0.5|NEEC's flag already names 0.0; the reader reads the Nordic economies' rising headcounts at 0.5 on the same pattern
DE|C1.1|hold|0.0|0.5|0.0|NEEC's flag already names 0.5; the reader applies no 0.0 test
OS|C1.1|hold|0.5|0.0|0.5|reach caps at 0.5 and never makes 0.0 alone (D28(c)); commons sustain resource-dependent households' livelihoods
FALC|C1.3|hold|0.5|1.0|0.5|no stability rate is stated (Session 54's rule, the 1.0 band's own words)
MC|C1.3|hold|0.0|0.5|0.0|no housing channel; the reader's own estimate agrees
UBS|C1.3|hold|0.5|1.0|0.5|no stability rate is stated; Vienna's analogue gives none
SWF|C1.3|hold|0.0|0.5|0.0|no housing channel; the reader's own estimate agrees
IF|C1.4|hold|0.0|0.5|0.0|NEEC's flag already names 0.5; the reader's own estimate finds no decoupling mechanism
CPS|C1.4|hold|0.5|0.0|0.5|guaranteed employment is a buffer that separates income from market demand for labour (the 0.5 band)
MC|C1.4|hold|0.5|0.0|0.5|mutual credit sustains exchange without wage income and arose in mass unemployment (Comox Valley, 1983; Argentina, 2001-02)
DE|C1.4|hold|0.0|0.5|0.0|automation named and met with no mechanism; the reader applies no 0.0 test
QA|C1.4|hold|0.5|0.0|0.5|rent-funded state jobs cover the citizens, about a tenth of residents: 2.1's partial population; now flagged toward 0.0
OS|C1.5|hold|0.0|0.5|0.0|exclusion is constitutive (principle 1) and reach is under a third, with no route to 80%; the reader concedes both
LM|C1.5|adopt|0.0|0.5|0.5|the published 0.0 asserts that only those born with capital have access, with no figure; market pathways are open without prior wealth, gated by income, as for Status Quo
UBI|C1.5|hold|0.0|0.5|0.0|the reader's own estimate (0% through the mechanism) is 2.1's no mechanism
DE|C1.5|hold|0.0|0.5|0.0|no asset mechanism, as on C1.2a
UBS|C1.5|hold|0.0|0.5|0.0|the reader's own estimate (0% through the mechanism) is 2.1's no mechanism
CN|C2.1|hold|0.0|0.5|0.0|state-mandated labour transfers: the 0.0 band's substitution of one coercion for another; flag stands
QA|C2.1|hold|0.0|0.5|0.0|survival compulsion maximised for the non-citizen majority by design; flag stands
LM|C2.1|hold|0.0|0.5|0.0|the reader's own estimate (survival compulsion remains) is the 0.0 band's economic coercion by design
DE|C2.1|hold|0.0|0.5|0.0|the published whole-criterion finding stands; the reader applies no 0.0 test
IF|C2.1|hold|0.5|0.0|0.5|the bar on compounding a defaulted debt reduces one channel of coercion; reach caps at 0.5, never 0.0 alone
OS|C2.2|hold|0.0|0.5|0.0|principle 2 ties appropriation to contribution; the reader's own estimate finds no provision
MMT|C2.2|hold|0.0|0.5|0.0|the 0.0 band names an ideological commitment to full employment; the job requires work
UBI|C2.2|adopt|1.0|0.5|0.5|the threshold asks for 100% of basic needs, not only unconditionality: the level is a free parameter in the literature, and rents can absorb the payment (NEEC's own C1.3)
GEO|C2.2|hold|0.5|0.0|0.5|an unconditional dividend from land rent is a real, partial baseline (the 0.5 band)
MC|C2.2|hold|0.5|0.0|0.5|credit before contribution, repaid by supplying goods, is the 0.5 band's ongoing contribution; now flagged toward 0.0
DE|C2.2|hold|0.0|0.5|0.0|no baseline is provided in the framework or its applications
UBS|C2.2|hold|0.5|1.0|0.5|shelter and food are allocated by need as costed; generalisation applies those rules economy-wide, it does not make them universal
CN|C2.2|hold|0.0|0.5|0.0|means-tested floors read as no baseline for every configured economy (Status Quo, Singapore, which the reader also reads at 0.0)
QA|C2.2|hold|0.0|0.5|0.0|the citizens' baseline is conditional and the non-citizen majority has none, as for Status Quo and Singapore
IF|C2.2|hold|0.0|0.5|0.0|the reader's own estimate finds no provision
CPS|C2.3|hold|0.0|0.5|0.0|socialist realism obligatory and prior censorship: the 0.0 band's own case; flag stands
OS|C2.3|hold|0.5|0.0|0.5|reach caps at 0.5; the reader reads every other mechanism at 0.5 on the same pattern
CN|C2.4|hold|0.0|0.5|0.0|the reader's own estimates (about 0% participation and proposals) and its 0.0 for the Soviet economy and Qatar
LM|C2.4|hold|0.5|0.0|0.5|formal democratic rights exist: the 0.5 band
FALC|C2.4|hold|0.0|0.5|0.0|governance is left unspecified: 2.1's no structural mechanism
MS|C2.5|hold|0.5|1.0|0.5|private firms only at small scale, passing to their workers (Schweickart): differential treatment the reader does not engage
MMT|C2.5|hold|0.5|1.0|0.5|the literature divides on whether the job replaces benefits (4.2); NEEC's flag already names 1.0
FALC|C2.5|hold|0.5|1.0|0.5|the sources state no terms of exit; silence is not clearance
UBS|C2.5|hold|0.5|1.0|0.5|portability of locally allocated housing is not stated; NEEC's flag already names 1.0
CN|C2.5|hold|0.5|0.0|0.5|most residents may emigrate and hukou has been eased; NEEC's flag already names 0.0
MC|C2.5|hold|0.5|1.0|0.5|a leaver forfeits a credit balance earned by supplying goods (kept short by decision 79.2's note)
LM|C2.6|hold|0.5|1.0|0.5|NEEC's estimate of 50-56 straddles the bar of 53; the reader's 54 lies inside it; flag stands
MMT|C2.6|hold|0.5|0.0|0.5|reach caps at 0.5: a mechanism does not govern the host's civil liberties
DE|C2.6|hold|0.5|0.0|0.5|the reader scores silence as 0 of 60; the framework presupposes the host's democracy
DE|C3.1|hold|0.0|0.5|0.0|no stabilisation instrument adopted; NEEC's flag already names 0.5
QA|C3.1|hold|0.0|0.5|0.0|cash-benefit coverage 4.1%, withheld by design; the reader's own clauses are all short
SC|C3.1|hold|0.5|0.0|0.5|the reform keeps its host's stabilisers and clause 2 is cleared on the 2020 record, so 0.0 is barred
GEO|C3.1|hold|0.5|0.0|0.5|the universal dividend clears clause 3, so 0.0 is barred
OS|C3.1|hold|0.5|0.0|0.5|a mechanism that pays no benefit holds at 0.5 by reach (Session 74's rule)
CN|C3.2|hold|1.0|0.5|1.0|2.0% in 2022 against about 8% abroad, long-run within 3%, and rule-based reserve and price-range schemes; flag stands
SG|C3.2|adopt|1.0|0.5|0.5|headline inflation was 6.1% in 2022, above the stress bar of 5%, the measure the pass applied to Status Quo
SQ|C3.3|adopt|0.0|0.5|0.5|the published 'fails catastrophically' is contradicted on the criterion's own poverty measure: the headcount fell in 2009 and 2020-21
LM|C3.4|hold|0.5|0.0|0.5|clause 3 is cleared on independent courts, so 0.0 is barred; NEEC's flag already names 0.0
SWF|C3.4|hold|1.0|0.5|1.0|eleven weeks from recommendation to decision (2017); clause 3 re-read on v2.0's wording is cleared; flag stands
OS|C3.4|stands|1.0|0.5|1.0|the reader clears clauses 1 to 3 and, shown the argument, clause 4 too (stage B); decision 79.4 stands
MS|C3.4|hold|1.0|0.5|1.0|Mondragon's 2009 crisis decisions by members are consistent with clause 2, though no source dates one within six months; now flagged toward 0.5
LM|C3.5|hold|0.5|0.0|0.5|NEEC's flag already names 0.0; the reader itself clears clause 4
UBS|C3.5|hold|0.0|0.5|0.0|no channel of the mechanism's own; NEEC's flag already names 0.5
CN|C3.5|hold|0.0|0.5|0.0|failure information actively suppressed (the Henan floods, the epidemic warning); flag stands
CPS|C3.5|adopt|0.5|0.0|0.0|failure information actively suppressed (Kyshtym 1957, the 1932-33 famine, Chernobyl's first days), the ground of China's 0.0
MMT|C3.5|hold|0.0|0.5|0.0|no channel; the reader marks the reach clauses moot, which they are not
UBI|C3.5|hold|0.0|0.5|0.0|no channel; the reader's own estimates agree
CPS|C3.6|hold|0.5|0.0|0.5|D28(f) holds a configured economy at 0.5 with clause 1 cleared (Session 77); flag stands
LM|C3.6|hold|0.5|1.0|0.5|no economy's record is of the design, which removes the state's part in education and research; working time not stated
CPS|C4.1|hold|0.5|1.0|0.5|the deficit of 10-13% of GDP in 1989 puts the debt on a path above the bar; NEEC's flag already names the reader's level reading
SC|C4.1|hold|0.5|0.0|0.5|clause 2 is cleared on the host's figures, so 0.0 is barred
MS|C4.2|hold|0.5|0.0|0.5|NEEC's flag already names 0.0
SC|C4.2|hold|0.0|0.5|0.0|voluntary metrics on a host far below every clause; NEEC's flag already names 0.5
SWF|C4.2|hold|0.5|0.0|0.5|out of reach: 0.5, never 0.0 on reach alone (Session 73's class reading)
IF|C4.2|hold|0.5|0.0|0.5|out of reach (Session 73's class reading)
MMT|C4.2|hold|0.5|0.0|0.5|within reach (a green job guarantee) but not estimated
UBI|C4.2|hold|0.5|0.0|0.5|out of reach (Session 73's class reading)
GEO|C4.2|hold|0.5|0.0|0.5|out of reach (Session 73's class reading)
MC|C4.2|hold|0.5|0.0|0.5|out of reach (Session 73's class reading)
SQ|C4.3|hold|0.0|0.5|0.0|the Black-white gap has stayed between 35% and 45% since 1972; the reader's own clauses are short; flag stands
GEO|C4.3|hold|0.5|0.0|0.5|a universal flat dividend, read as for Universal Basic Income and CCO-PTF-CIP-SZH; NEEC's flag already names 0.0
CN|C4.3|hold|0.0|0.5|0.0|coercive action against the minorities most affected (OHCHR, 2022); flag stands
OS|C4.3|hold|0.5|0.0|0.5|quotas and collective tenure work inside the mechanism; NEEC's flag already names 0.0
UBI|C4.4|hold|0.5|0.0|0.5|out of reach (Session 73's class reading); NEEC's flag already names 0.0
DE|C4.4|hold|0.0|0.5|0.0|no ownership or removal design adopted; NEEC's flag already names 0.5
SG|C4.4|hold|0.0|0.5|0.0|an electoral autocracy throughout 2014-2025; the reader's own clauses are short; flag stands
MS|C4.4|hold|1.0|0.5|1.0|cleared on decision 48.3's measure through worker-members' election and dismissal of the council; now flagged toward 0.5 for the design's other variants
MC|C4.4|hold|0.5|0.0|0.5|out of reach (Session 73's class reading)
CPS|C4.5|hold|0.5|0.0|0.5|state housing at nominal rents and no interest-bearing consumer debt remove two relationship types for most households (reading 4.5.3); flag stands
LM|C4.5|adopt|0.5|0.0|0.0|every relationship type in place, exit only the formal right to quit, no floor: reading 4.5.3's 0.0 line, as Status Quo
SC|C4.5|hold|0.0|0.5|0.0|reading 4.5.3's 0.0 line, as Status Quo; NEEC's flag already names 0.5
DE|C4.5|hold|0.0|0.5|0.0|names directions and commits to none; NEEC's flag already names 0.5
SWF|C4.5|hold|0.0|0.5|0.0|the fund removes no extractive relationship; NEEC's flag already names 0.5
SG|C4.5|hold|0.5|0.0|0.5|77.2% of resident households pay no private landlord (reading 4.5.3's 0.5 condition); flag stands
UBI|C4.6|hold|0.5|0.0|0.5|out of reach (Session 76's class reading)
SC|C4.6|hold|0.5|0.0|0.5|the reform keeps its host's liability law and regulators, as C3.1 reads it
SWF|C4.6|hold|0.5|0.0|0.5|out of reach (Session 76's class reading)
UBI|C5.1|hold|1.0|0.5|1.0|Alaska's dividend outcomes are documented; NEEC's flag already names 0.5
SWF|C5.1|hold|0.5|1.0|0.5|outcomes are mixed (Timor-Leste's over-withdrawal; Alaska's dividend in 2025); NEEC's flag already names 1.0
SG|C5.1|hold|0.5|1.0|0.5|NEEC's flag already names 1.0
FALC|C5.1|adopt|0.0|0.5|0.5|NEEC's own text (components proven individually, not integrated) is the 0.5 band, as for Participatory Economics, Integral and CCO-PTF-CIP-SZH
MC|C5.2|hold|0.5|0.0|0.5|NEEC's flag already names 0.0
SWF|C5.2|hold|1.0|0.5|1.0|the threshold's precedent route: Norway's four dated stages and Timor-Leste's ten months; flag stands
IF|C5.2|hold|0.5|0.0|0.5|Malaysia's staged build and Iran's conversion are precedents; the reader's 0.0 misses them
SQ|C5.2|hold|1.0|0.5|1.0|the existing system needs no transition: moot (2.3(e))
SC|C5.2|hold|0.5|0.0|0.5|clause 1 is cleared on Germany's staged codetermination, so 0.0 is barred
FALC|C5.2|hold|0.0|0.5|0.0|the destination rests on technologies not yet developed; now flagged toward 0.5 for the sketched political route
DE|C5.2|hold|0.5|0.0|0.5|the City Portrait method, a first stage followed in dozens of places: a sketched pathway
CN|C5.2|hold|0.5|1.0|0.5|the reader reads China's own development phases, not a transition to the configuration
SG|C5.2|hold|0.5|1.0|0.5|the reader reads Singapore's own development phases, not a transition to the configuration
UBS|C5.3|hold|1.0|0.5|1.0|scaling observed (Quebec's childcare to all of Canada, 2.3(d)) and the 2022 federal-provincial agreements; flag stands
SQ|C5.3|hold|1.0|0.5|1.0|the reader's short clause 2 treats the traditional market as needing to coexist with itself
UBI|C5.3|adopt|0.5|1.0|1.0|read as Georgism and Sovereign Wealth Fund Statism are: scaling observed at national scale (Iran since 2010, 2.3(d)) and coordination not needed by a single jurisdiction (2.3(e))
GEO|C5.3|hold|1.0|0.5|1.0|single jurisdictions adopt alone (coordination moot, 2.3(e)) and operation is observed from city to nation
SWF|C5.3|hold|1.0|0.5|1.0|every fund operates alone (coordination moot) and operation is observed at national scale
CN|C5.3|hold|0.5|1.0|0.5|the reader moots every clause for a configured economy yet reads Nordic Social Democracy at 0.0 and Singapore at 0.5
QA|C5.3|hold|0.5|1.0|0.5|the reader moots every clause, against its own readings of the other configured economies
SWF|C5.4|hold|0.5|1.0|0.5|the dividend has been paid every year since 1982, but its statutory formula has been overridden since 2016; now flagged toward 1.0
SC|C5.4|adopt|0.0|0.5|0.5|the published 0.0 has no figure; business support and the anti-ESG backlash are the 0.5 band's appeal to part of the spectrum against resistance from another
MC|C5.5|hold|1.0|0.5|1.0|WIR, Sardex and Grassroots Economics operate; NEEC's flag already names 0.5
QA|C5.5|hold|0.0|0.5|0.0|the 0.0 band's precondition: rents very large relative to the citizen body, which the configuration cannot produce
IF|C5.5|hold|1.0|0.5|1.0|three income bands and six cultural settings; now flagged toward 0.5, as Mutual Credit is, for want of a documented range
CPS|C5.5|hold|0.5|0.0|0.5|operated in six or more cultural settings (clause 2 cleared), so 0.0 is barred; now flagged toward 0.0 (D29(a))
MS|C5.5|adopt|0.0|0.5|0.5|the published 0.0 calls wider scaling 'uncertain', which is the 0.5 band, not 0.0's no credible generalisation
UBI|C5.5|adopt|0.0|0.5|0.5|the published 0.0 asserts cultural resistance with no figure; transfers of the kind have operated across income levels and cultures
SC|C5.5|hold|0.0|0.5|0.0|stakeholder commitments are not reflected in practice (Bebchuk and Tallarita, 2020); now flagged toward 0.5
"""
OUTCOMES = {}
for _ln in OUTCOMES_TEXT.strip().splitlines():
    _u, _cid, _o, _n, _r, _s, _why = _ln.split("|", 6)
    OUTCOMES[(_u, _cid)] = dict(outcome=_o, neec=float(_n), reader=float(_r), stands=float(_s), why=_why)

V1 = "Report v1.6"
OR = "the outside review r1, the reader's reading (outside_review_r1/results/reader.jsonl.gz)"
TAB = "Tabatabai, The Basic Income Road to Reforming Iran's Price Subsidies, Basic Income Studies (doi 10.2202/1932-0183.1172)"
SPL = "World Bank SI.POV.SOPO, United States (evidence_cache/C1.1/wb_societal_poverty_rate.json)"
WP = "Integral white paper v0.1 (December 2025)"
NOEST = ("no source the unit cites, and none located in this adjudication, states an estimate of the clause's quantity "
         "(protocol 2.3(b))")


def U(est, src):
    return ("U", est, src)


def S(est, src):
    return ("S", est, src)


def C(est, src):
    return ("C", est, src)


def M(est, src):
    return ("M", est, src)


def unit(kind, clauses, flag=None, note="", zero=None):
    v = 0.0 if zero else (1.0 if all(c[0] in "CM" for c in clauses) else 0.5)
    return dict(kind=kind, verdict=v, clauses=[tuple(c) for c in clauses], flag=flag, note=note, zero=zero)


UNITS = {
    # ---- C1.2b: a 1.0 needs an estimate of the distribution, or a structural argument that bounds all of it ----------
    ("DG", "C1.2b"): unit("change", [
        U("not shown: the literature proposes caps on income and wealth, commons and universal services, which would lower "
          "concentration, but the design keeps private property and markets and no source estimates the wealth "
          "distribution; a cap on the top does not bound a Gini, which the bottom of the distribution also sets", f"{V1}, "
          f"DG C1.2b; {OR}")],
        flag=[[1.0], "the published reading: decentralisation, wealth caps and cooperative ownership as a named structural "
                     "ceiling of the kind the 1.0 band describes"],
        note="adjudicated in Session 83 (adopt): the class W 1.0 rested on the 1.0 band's description, with no estimate"),
    ("INT", "C1.2b"): unit("change", [
        U("not shown: inside the network time-decaying, non-transferable credits and node commons make accumulation "
          "impossible, but the design 'is designed to emerge gradually, non-coercively, and in parallel with existing "
          "market and state systems', becoming 'supplementary' before 'essential', and no source estimates the wealth "
          "held by its population, inside the network or outside it; Jev reads the clause not shown in both passes",
          f"{WP}, sections 11 to 11.6 (the source pack design__INT__C1.2b); {OR}")],
        flag=[[1.0], "the published reading: no stock of wealth exists anywhere in the network for any participant to "
                     "convert into leverage over others"],
        note="adjudicated in Session 83 (adopt)"),
    ("MC", "C1.2b"): unit("change", [
        ("R", "out of reach: a mutual-credit network governs its members' exchange balances (zero-sum, capped, usually "
              "interest-free), not the holdings of land, capital and savings that set an economy's wealth Gini, even "
              "generalised (protocol 3.2, D28(c))", f"{V1}, MC C1.2b; SCORING_PROTOCOL.md 3.2")],
        note="adjudicated in Session 83 (adopt): the published 1.0 credited the network's own balances"),
    ("FALC", "C1.2b"): unit("change", [
        U("not shown: common ownership of automated production, universal services and socialised housing are named in the "
          "literature as the design's answer to concentration, but who owns and controls the machines is left unresolved "
          "(the entry's own C4.4) and no source estimates the distribution", f"{V1}, FALC C1.2b and C4.4; {OR}")],
        flag=[[0.0], "the published reading: the unresolved control of the machines read as no structural prevention"],
        note="adjudicated in Session 83 (third reading): the published 0.0 rested on unresolved risk, which protocol 2.1 "
             "places at 0.5; the reader's 1.0 rested on no estimate"),
    # ---- C1.5 ----------------------------------------------------------------------------------------------------------
    ("LM", "C1.5"): unit("change", [
        U("not shown: the design leaves wage saving, home and share ownership open to anyone through markets, gated by "
          "income rather than by prior wealth; no figure for the share with an active pathway is stated or located (the "
          "outside reader's closed-book estimate is 60-70%)", f"{V1}, LM C1.5; {OR}")],
        flag=[[0.0], "the published reading: without public education and a safety net, effective access narrows to those "
                     "born with capital (the 0.0 band)"],
        note="adjudicated in Session 83 (adopt): the published 0.0 rested on no figure, and Status Quo, on the same market "
             "pathways with more public support, is 0.5"),
    # ---- C2.2 ----------------------------------------------------------------------------------------------------------
    ("UBI", "C2.2"): unit("change", [
        U("not shown in full: the provision is unconditional, but the threshold asks that it cover 100% of basic needs "
          "(housing, food, healthcare, utilities) for all residents; the mechanism's literature includes partial and full "
          "variants (the definition sets no level), and the entry's own C1.3 records that rents can absorb the payment",
          f"{V1}, UBI C2.2 and C1.3; {OR}")],
        flag=[[1.0], "the 1.0 band's reading: provision explicitly unconditional"],
        note="adjudicated in Session 83 (adopt), with CCO-PTF-CIP-SZH's C2.2 read alike (to the owner)"),
    # ---- C3.2 ----------------------------------------------------------------------------------------------------------
    ("SG", "C3.2"): unit("change", [
        C("cleared: core inflation averaged 0.7% in 2025 and long-run inflation is within the bar", "NEEC_StateCapitalism_"
          "Singapore_scoring_scratch.md, C3.2 (MAS, January 2026)"),
        S("short: headline inflation averaged 6.1% in 2022, the stress year, above the bar of 5% (core 4.1%), the measure "
          "on which the pass read Status Quo's clause 2 (part (b4))", "BIS Papers No. 142, as the scoring document cites "
          "it; NEEC_Rescoring_s41.md, SQ C3.2"),
        U("not estimated: whether the MAS's exchange-rate band, reset at its policy reviews, is automatic adjustment is left "
          "to Report v2.0, as for Status Quo", "NEEC_Rescoring_s41.md, SQ C3.2")],
        flag=[[1.0], "the published reading: core inflation of 4.1% in 2022 below the stress bar"],
        note="adjudicated in Session 83 (adopt); the scoring document flagged the headline reading itself"),
    # ---- C3.3: a 1.0 needs an estimate of the core functions' degradation under the scenarios -------------------------
    ("DG", "C3.3"): unit("change", [
        U("not shown: low throughput, localised production and design 'for crisis as norm' are the 1.0 band's features, but "
          "no source estimates the fall of poverty, housing stability, essential services or democratic function under "
          "any of the four compound scenarios", f"{V1}, DG C3.3; {OR}")],
        flag=[[1.0], "the 1.0 band's reading: explicit design for compound shocks through decentralisation and redundancy"],
        note="adjudicated in Session 83 (adopt): the class W 1.0 rested on the band's description, with no estimate"),
    ("PE", "C3.3"): unit("change", [
        U("not shown: distributed decision-making and the absence of a financial sector are the 1.0 band's features, but no "
          "source estimates the core functions' degradation under any of the four compound scenarios",
          f"{V1}, PE C3.3; {OR}")],
        flag=[[1.0], "the 1.0 band's reading: explicit design for compound shocks through decentralisation"],
        note="adjudicated in Session 83 (adopt)"),
    ("INT", "C3.3"): unit("change", [
        U("not shown: the published 1.0 cites a review of the design (not the white paper) estimating degradation under "
          "25% in each scenario, which does not show under 20%; the white paper describes redundancy and monitoring "
          "(FRS, Coordination Envelopes) and estimates no degradation; Jev reads the clause not shown in both passes",
          f"{V1}, INT C3.3; Integral_NEEC_Review.md, C3.3; {WP}; {OR}")],
        flag=[[1.0], "the 1.0 band's reading: redundancy at every layer, so that node failures do not cascade"],
        note="adjudicated in Session 83 (adopt)"),
    ("SQ", "C3.3"): unit("change", [
        U("not shown: on the criterion's own poverty measure the configuration's two recent compound shocks did not degrade "
          "the function -- the United States' headcount at the Societal Poverty Line was 19.7% in 2008, 19.0% in 2009 and "
          "19.2% in 2010, and 19.8% in 2019, 18.2% in 2020 and 16.7% in 2021 -- but the four scenarios (a 30% fall in GDP "
          "among them) lie beyond the record, and housing, services and democratic function under them are not estimated",
          SPL)],
        flag=[[0.0], "the published reading: optimised for normal conditions, with 2008 and 2020 requiring extraordinary "
                     "policy action"],
        note="adjudicated in Session 83 (adopt): the published 0.0 ('fails catastrophically') is contradicted on the "
             "criterion's own measure, so protocol 2.1's 'far below' is not shown"),
    # ---- C3.5 ----------------------------------------------------------------------------------------------------------
    ("CPS", "C3.5"): unit("change", [
        S("short: shortages and queues were visible to all, but failure information was suppressed: the Kyshtym accident "
          "of 1957 was acknowledged only in 1989, the famine of 1932-33 was officially denied, and Chernobyl's release was "
          "announced only after radiation was detected in Sweden (28 April 1986)", f"{V1}, CPS C3.5; {OR}"),
        U("not shown: no diagnostic record or independent evaluation reporting the share of failures whose cause was "
          "established", f"{V1}, CPS C3.5"),
        S("correction came through eventual collapse and reform, in every Soviet-type economy: a failure replicated across "
          "independent implementations (D29(a))", f"{V1}, CPS C3.5"),
        U("not estimated: no externalised cost is projected as a share of total costs (the outside reader, closed-book, "
          "puts unpriced pollution and energy far above 10% of GDP)", f"{OR}")],
        zero="the system actively suppressed failure information (protocol 2.1; the 0.0 band: active suppression of "
             "failure information), the ground on which China's C3.5 is 0.0",
        flag=[[0.5], "the published reading: failures such as shortages were visible, and correction came through reform"],
        note="adjudicated in Session 83 (adopt)"),
    # ---- C4.5 (I9, item 1) ----------------------------------------------------------------------------------------------
    ("LM", "C4.5"): unit("change", [
        S("short: no mechanism limits extraction; the design treats voluntary exchange as non-exploitative by definition and "
          "keeps every relationship type (employer and employee, landlord and tenant, lender and borrower)",
          f"{V1}, LM C4.5; NEEC_BlindReview_s71.md, reading 4.5.3"),
        S("short: exit is the formal right to quit, with no subsistence floor and no assured alternative",
          f"{V1}, LM C4.5; NEEC_BlindReview_s71.md, reading 4.5.3")],
        zero="reading 4.5.3's 0.0 line (protocol 2.1): far below on both clauses, every relationship type in place, exit no "
             "more than the formal right to quit, and no rule or instrument that removes one, as for Status Quo",
        flag=[[0.5], "parts (a) and (b8)'s reading: both clauses not shown, held at 0.5 under D28(f)"],
        note="adjudicated in Session 83 (adopt); settles ledger I9's first item for this entry"),
    # ---- C5.1 ----------------------------------------------------------------------------------------------------------
    ("FALC", "C5.1"): unit("change", [
        S("short: the components with twenty-year records at scale (renewable energy, cooperatives, public services) are "
          "the design's peripheral ones; its distinctive ones (full automation, post-work distribution) have none, so "
          "well under 70% of its components are proven", f"{V1}, FALC C5.1; {OR}"),
        U("not shown: no integrated implementation, so no outcome to match against the system's claims", f"{V1}, FALC C5.1")],
        flag=[[0.0], "the 0.0 band's reading: the distinctive components are a novel projection"],
        note="adjudicated in Session 83 (adopt): the published text, components proven individually but not integrated, "
             "is the 0.5 band"),
    # ---- C5.3 ----------------------------------------------------------------------------------------------------------
    ("UBI", "C5.3"): unit("change", [
        C("implementable at municipal, state or national scale", "as audited (the unit's own text)"),
        C("Alaska shows coexistence with the market economy", "as audited (the unit's own text)"),
        C("cleared on observed operation, at least as strong as modelling (protocol 2.3(d)): pilots of thousands; Alaska's "
          "dividend at state scale since 1982; and since December 2010 a universal, unconditional monthly cash transfer "
          "per person that nearly every resident of Iran receives", f"{TAB}; {V1}, UBI C5.1"),
        M("moot: a single jurisdiction adopts the mechanism without coordination with others (Alaska, Iran), as Georgism's "
          "and Sovereign Wealth Fund Statism's clause 4 are read (protocol 2.3(e))", f"{V1}, GEO C5.3 and SWF C5.3")],
        flag=[[0.5], "Iran's transfer compensates for removed price subsidies rather than paying an income as of right "
                     "(Tabatabai), and no adequate basic income has been scaled"],
        note="adjudicated in Session 83 (adopt), read as the two other single-jurisdiction mechanisms are"),
    # ---- C5.4 ----------------------------------------------------------------------------------------------------------
    ("SC", "C5.4"): unit("change", [
        S("short: business leaders and centrists back it (the Business Roundtable's 2019 statement; the World Economic "
          "Forum), while state laws against ESG investing, from 2021, show organised resistance on the right", f"{OR}; "
          f"{V1}, SC C5.4"),
        U("not shown: no measure of opposition to repeal", f"{V1}, SC C5.4; {OR}"),
        U("not shown: no record across administrations of a framework that is voluntary", f"{V1}, SC C5.4; {OR}")],
        flag=[[0.0], "the published reading: it satisfies neither capital nor labour, a political homelessness"],
        note="adjudicated in Session 83 (adopt): the published 0.0 rested on no figure (protocol 4.1)"),
    # ---- C5.5 ----------------------------------------------------------------------------------------------------------
    ("MS", "C5.5"): unit("change", [
        U("not shown: implementations span high-income (the Basque Country, Northern Italy) and middle-income (Yugoslavia) "
          "economies; none is located in a low-income one", f"{V1}, MS C5.5; {OR}"),
        U("not shown: the strongest records are in regions with cooperative traditions, and wider transfer is 'uncertain'",
          f"{V1}, MS C5.5"),
        U("not shown: no documented range of adjustment in a named parameter", f"{V1}, MS C5.5; {OR}"),
        U("not shown: one sustained national implementation (Yugoslavia) ended with the state", f"{OR}")],
        flag=[[0.0], "the published reading: successful only in specific cultural contexts"],
        note="adjudicated in Session 83 (adopt): the published 0.0 calls wider scaling uncertain, which is the 0.5 band"),
    ("UBI", "C5.5"): unit("change", [
        C("cleared: transfers of the kind have operated at high income (Alaska, Finland), middle income (Iran, Mongolia) "
          "and low income (Kenya, Namibia, India)", f"{OR}; {TAB}"),
        C("cleared: in more than five cultural settings (the same programmes)", f"{OR}"),
        C("cleared: the payment level, a named parameter, ranges far more than 40% across implementations (Alaska's "
          "dividend alone from $331 in 1984 to $3,284 in 2022)", "Alaska Permanent Fund Dividend Division, dividend "
          "amounts by year"),
        S("short: no full, permanent national basic income has operated, so successful operation across diverse "
          "implementations is shown for partial or temporary forms only", f"{OR}")],
        flag=[[0.0], "the published reading: acceptance of income without work is a cultural precondition the mechanism "
                     "cannot itself produce"],
        note="adjudicated in Session 83 (adopt): the published 0.0 asserted cultural resistance with no figure"),
    # ---- revisions: a clause's reading corrected, the verdict holding -------------------------------------------------
    ("INT", "C3.2"): unit("revision", [
        C("there is no money supply to inflate", "as audited (the unit's own text)"),
        U("not shown: the white paper does specify the boundary -- Interface Cooperatives let the design 'operate inside a "
          "monetary environment without internalizing monetary logic', 'a containment strategy: money is allowed to cross "
          "the boundary only where necessary, and only in one direction' (section 11.6) -- correcting the earlier reading's "
          "'a mechanism the design does not specify'; but no source estimates the system under an external 8% inflation "
          "while its nodes buy from markets, and the paper calls the hybrid integration 'an experimental concept that "
          "needs more development'", f"{WP}, sections 11.5 and 11.6 (the source pack design__INT__C3.2); {OR}"),
        C("matched to capacity through COS", "as audited (the unit's own text)")],
        flag=[[1.0], "the outside reader's reading: no internal prices and a one-way boundary keep internal inflation at "
                     "zero, as clause 1 is read"],
        note="clause 2 corrected in Session 83's adjudication; the verdict holds"),
    ("INT", "C5.3"): unit("revision", [
        C("the federated structure starts with a handful of people", "as audited (the unit's own text)"),
        C("nodes coexist with traditional markets", "as audited (the unit's own text)"),
        U("not shown: the white paper says thresholds 'are derived from: empirical system modeling, ecological science, "
          "historical performance data', how they are to be set, not a model validating the path from pilot to regional "
          "to national scale; Jev reads the clause short in both passes", f"{WP} (the source pack design__INT__C5.3)"),
        C("cleared: the white paper establishes coordination protocols between nodes (Node State Summaries, threshold "
          "classification, Coordination Envelopes, internodal reciprocity protocols); Jev reads the clause cleared in both "
          "passes", f"{WP}, sections 9.3 to 9.5 and 10")],
        note="clause 4 read in Session 83's adjudication; the verdict holds"),
    ("SWF", "C3.4"): unit("revision", [
        C("the strategic equity share moved from 40% (1998) to 60% (decided June 2007) to 70% (2017): a core parameter "
          "moved by half its value; the expected return in the fiscal rule from 4% to 3% (2017)",
          "Norges Bank, Matsen speech (1 December 2016); Ministry of Finance press release (16 February 2017)"),
        C("the 2017 decisions came on 16 February, eleven weeks after Norges Bank's recommendation of 1 December 2016",
          "NBIM letter to the Ministry (1 December 2016); Ministry of Finance (16 February 2017)"),
        C("cleared on v2.0's wording (contestable through a process that does not depend on the officials who made the "
          "change; ledger I9): Alaska's dividend veto of 2016 was challenged in the state Supreme Court (Wielechowski v. "
          "State, 2017), and Alaskans may legislate by initiative", "Courthouse News (2017), as UBI's C3.4 cites the same "
          "case; Alaska Constitution, article XI"),
        C("the new equity share held through 2008-2009 without collapse", "as audited (the unit's own text)")],
        flag=[[0.5], "evidence dated from the market evidence of lower expected returns rather than from the formal "
                     "assessment, which makes the expected-return revision slow"],
        note="clause 3 re-read on v2.0's wording in Session 83 (ledger I9); the verdict holds"),
    # ---- flags: a held verdict gains a close call ---------------------------------------------------------------------
    ("QA", "C1.4"): unit("flag", [
        U("citizens' incomes rest on a hydrocarbon rent automation would not touch, through state jobs; non-citizens, most "
          "of the population the protocol counts (3.2), have no mechanism beyond departure; no model or estimate of poverty "
          "on the Societal Poverty Line under a 30%, 50% or 70% displacement of paid hours is stated or cited, and none was "
          "located", "NEEC_StateCapitalism_Qatar_scoring_scratch.md, C1.4; SCORING_PROTOCOL.md 3.2"),
        U("no model or estimate of real final consumption expenditure against a pre-displacement baseline in any of the "
          "three scenarios is stated or cited, and none was located", "NEEC_StateCapitalism_Qatar_scoring_scratch.md, C1.4")],
        flag=[[0.0], "the outside reader's reading: for the non-citizen majority, income and demand rest wholly on wage "
                     "labour (the 0.0 band)"],
        note="a buffer covering part of the relevant population is the 0.5 band (protocol 2.1)"),
    ("MC", "C2.2"): unit("flag", [
        S("short: credit can be extended before a member has contributed, but balances are capped and are repaid by "
          "supplying goods or services, so the system expects reciprocity over time rather than providing a baseline "
          "with no expectation of return", f"{V1}, MC C2.2")],
        flag=[[0.0], "the outside reader's reading: a capped, repayable credit line is no baseline independent of work"],
        note="held at the published 0.5 in Session 83's adjudication (the 0.5 band: requires some ongoing contribution)"),
    ("MS", "C3.4"): unit("flag", [
        C("the pay-ratio cap, a core distributive parameter, moved from 1:3 at founding to 1:4.5 in the 1970s and 1:6 in "
          "1988, a 100% range", "Co-operative News, Co-operative approaches to pay (thenews.coop)"),
        C("democratic governance enables rapid adaptation to evidence; consistent with the record: in 2009 Eroski's worker-"
          "members voted to freeze pay and work 10% more, and a cooperative's assembly agreed rotating leave at 80% of "
          "pay, though no source dates a decision against the evidence that called for it", "as audited (the unit's own "
          "text); YES! Magazine, via Resilience.org (4 September 2009); EITB"),
        C("the pay-ratio changes were decided at the cooperatives' General Assemblies, the members themselves (v2.0's "
          "wording; ledger I9)", "Co-operative News (thenews.coop); Report v1.6, MS C3.4"),
        C("stated search: no collapse caused by a parameter adjustment located; Fagor Electrodomesticos, the founding "
          "cooperative, failed in 2013 after heavy losses in the euro-area and Spanish real-estate crises, carrying debt "
          "from its 2005 Brandt acquisition, causes that clear it of an adjustment",
          "Fortune (27 November 2013); The Local (14 November 2013); Mondragon Annual Report 2013")],
        flag=[[0.5], "the outside reader's reading: no source dates a policy update within six months of the evidence"],
        note="clause 2 rests on the unit's own text, as part (a)'s convention carries an addressed clause; Report v2.0's "
             "clause-level Part I should time an update against the evidence that called for it"),
    ("MS", "C4.4"): unit("flag", [
        C("the audited phrase, economic power distributed through democratic ownership, claims the defined condition: the "
          "system places enterprises in the ownership of those who work in them and removes the employer-employee "
          "hierarchy, and in its principal component each cooperative's worker-members elect the governing council, one "
          "member one vote, and can dismiss it in general assembly (all of the system's employment)",
          "as audited, re-read against decision 48.3's measure (the unit's own text); Report v1.6, MS C4.4; Ley 11/2019, "
          "de 20 de diciembre, de Cooperativas de Euskadi, article 46; International Co-operative Alliance, Statement on "
          "the Cooperative Identity, principle 2"),
        C("as part (b7) recorded: administrators serve two to five years and the general assembly may dismiss them and "
          "elect their replacements in the same session", "NEEC_Rescoring_s47.md, MS C4.4, clause 2")],
        flag=[[0.5], "the outside reader's reading: the design's family includes variants (Lange and Lerner's state firms, "
                     "Roemer's coupon boards) that place firm control elsewhere (protocol 4.2)"],
        note="held in Session 83's adjudication"),
    ("FALC", "C5.2"): unit("flag", [
        U("no pathway is specified: the entry's destination rests on technologies not yet developed (general artificial "
          "intelligence, abundant clean energy and storage) together with a political transformation, and no stage of "
          "deployment of that destination is located or possible before they exist (reading 3.5)",
          "Report v1.6, System 10, C5.2"),
        U("no rapid pathway is stated, and none can be deployed before the technologies exist (reading 3.5)",
          "Report v1.6, System 10, C5.2"),
        U("no milestones are stated (reading 3.5)", "Report v1.6, System 10, C5.2"),
        U("no resource requirements are stated (reading 3.5)", "Report v1.6, System 10, C5.2"),
        U("no risk mitigation for a transition is stated (reading 3.5)", "Report v1.6, System 10, C5.2")],
        zero="no structural mechanism addresses the criterion: 'fully automated' is a destination without a roadmap, whose "
             "defining condition cannot be deployed by any pathway until technologies not yet developed exist",
        flag=[[0.5], "the outside reader's reading: the literature sketches a political route (municipal ownership, public "
                     "banks, universal basic services), the 0.5 band's pathway sketched but unspecific"],
        note="one of the 0.0s the published C5.2 count names; it holds"),
    ("SWF", "C5.4"): unit("flag", [
        C("Alaska's dividend has held approval across the political spectrum for four decades, the corpus's own anchor "
          "case for this criterion", f"{V1}, SWF C5.4"),
        U("not shown: no measure of opposition to repeal is cited (the outside reader's closed-book figure, about 70% "
          "opposed to cutting the dividend, was not located)", f"{OR}"),
        S("short: the dividend has been paid every year since 1982, but its statutory formula was overridden by veto in "
          "2016 and by appropriation since, and the 2025 dividend was the smallest in real terms (the entry's own C5.1)",
          f"{V1}, SWF C5.4 and C5.1")],
        flag=[[1.0], "the outside reader's reading, and the published flag: the mechanism has survived every change of "
                     "administration, in Alaska since 1982 and in Norway since 1990"],
        note="held at the published 0.5 in Session 83's adjudication"),
    ("DG", "C5.4"): unit("flag", [
        S("short: support is concentrated on the left and among Greens (the outside reader's closed-book estimate is 15-30%), "
          "with resistance from unions and developing nations", f"{V1}, DG C5.4; {OR}"),
        U("not shown: the design is not enacted, so no repeal can be measured", f"{V1}, DG C5.4; {OR}"),
        U("not shown: no record across administrations", f"{V1}, DG C5.4; {OR}")],
        zero="structural or rhetorical features actively repel broad coalition-building (protocol 2.1; the 0.0 band): the "
             "name is chosen as a provocation, and the design's own literature records resistance among unions and "
             "developing nations",
        flag=[[0.5], "the outside reader's reading: strong appeal to part of the spectrum against resistance from another "
                     "(the 0.5 band)"],
        note="held at the published 0.0 in Session 83's adjudication"),
    ("IF", "C5.5"): unit("flag", [
        C("cleared: high income (the United Kingdom, Qatar), middle income (Malaysia, Turkiye) and low income (Bangladesh, "
          "Sudan, the Kyrgyz Republic)", "NEEC_IslamicFinance_scoring_scratch.md, C5.5"),
        C("cleared: Southeast Asia, South Asia, the Gulf and wider Middle East, Sub-Saharan Africa, Central Asia and Europe",
          "NEEC_IslamicFinance_scoring_scratch.md, C5.5"),
        C("cleared on the scoring document's reading: the schools of jurisprudence produce materially different permissible "
          "product sets, and jurisdictions choose among them", "NEEC_IslamicFinance_scoring_scratch.md, C5.5"),
        C("cleared: operation validated in Malaysia, the Gulf, Iran and the sukuk markets",
          "NEEC_IslamicFinance_scoring_scratch.md, C5.5")],
        flag=[[0.5], "read as requiring a documented range of at least 40% in a named parameter, which the scoring document "
                     "does not give (as Mutual Credit's flag reads its clause 3)"],
        note="held at the published 1.0 in Session 83's adjudication"),
    ("CPS", "C5.5"): unit("flag", [
        S("short: low- and middle-income economies only; no centrally planned economy reached high income", f"{OR}"),
        C("cleared: implemented in Russian, Chinese, Cuban, Eastern European, Korean and Vietnamese settings",
          f"{V1}, CPS C5.5"),
        S("short: key parameters were fixed centrally, and cultural variation suppressed rather than accommodated",
          f"{V1}, CPS C5.5"),
        S("short: every implementation either collapsed or survived by abandoning central planning", f"{OR}")],
        flag=[[0.0], "a failure replicated across independent implementations is evidence about the system's own logic "
                     "(D29(a)), read as far below with no pathway"],
        note="held at the published 0.5 in Session 83's adjudication: with clause 2 cleared, 0.0 is barred"),
    ("SC", "C5.5"): unit("flag", [
        U("not shown: no whole-system implementation in a low-income economy", f"{OR}"),
        U("not shown: stakeholder-oriented governance operates in Germany, Japan and the Nordic economies, but the "
          "comprehensive system is not validated in five settings", f"{OR}"),
        U("not shown: principle-based, with no parameters to adjust", f"{OR}"),
        S("short: signatories' commitments are not reflected in their governance (Bebchuk and Tallarita, The Illusory "
          "Promise of Stakeholder Governance, Cornell Law Review, 2020)", f"{V1}, SC C5.5")],
        zero="the system requires a cultural consensus that corporations serve the social good, which competitive pressures "
             "contradict and which it cannot itself produce (the 0.0 band)",
        flag=[[0.5], "the outside reader's reading: stakeholder governance operates in several economies"],
        note="held at the published 0.0 in Session 83's adjudication"),
}

# The adjudicated readings that go to the owner (decision 57.2; decision 79.4 is the owner's): never applied here.
OWNER = {
    ("CCO", "C2.2"): dict(now=1.0, proposed=0.5, ledger="D65", unit=unit("owner", [
        U("not shown in full: the provision is unconditional (no means test or work requirement), but the design's "
          "legislative text pays 'every citizen and legal resident 18 years or older', its BLEI accounting values the "
          "Basic Units against food and utilities, essentials are paid partly in primary currency, and its published model "
          "leaves adults below their cost of living (the share falls 60.3% to 70.7% against no programme, the entry's C1.1)",
          "the source pack design__CCO__C2.2 (integrated-implementation-roadmap.html, section 102; basic-living-economic-"
          "index.html); NEEC_Rescoring_s57.md, CCO C1.1")],
        flag=[[1.0], "the published reading: the basic amount covers essential needs unconditionally"])),
    ("CCO", "C5.3"): dict(now=1.0, proposed=0.5, ledger="D65", unit=unit("owner", [
        S("short on the preponderance of the design's own texts (protocol 4.2): the modelling paper finds 'minimum viable "
          "participation at 55%' ('below 55% participation rate, network effects fail to sustain system growth'), the BLEI "
          "paper a self-funding threshold of 60-65%, the sensitivity analysis 55-60%, and the model warns below 55%; the "
          "integrated framework's 'viability at 30%' states no computation", "the source pack design__CCO__C5.3 (economic-"
          "modeling-simulation.html, section 7.1; basic-living-economic-index.html, section 6.3; cco-ptf-simulation-"
          "replication.html); NEEC_Rescoring_s57.md, reading 3.12"),
        C("Can coexist with traditional markets", "as audited (the unit's own text)"),
        C("Scaling pathway validated through modeling", "as audited (the unit's own text)"),
        C("Inter-jurisdictional coordination protocols specified", "as audited (the unit's own text)")],
        flag=[[1.0], "the integrated framework's reading: viability at 30% participation"])),
    ("DG", "C3.4"): dict(now=1.0, proposed=0.5, ledger="D66", unit=unit("owner", [
        U("not shown: the published rationale's 'democratic governance allows evidence-based adjustments' states no range "
          "of adjustment", f"{V1}, DG C3.4; {OR}"),
        U("not shown: 'decentralised experimentation enables rapid learning' dates no update against evidence", f"{V1}, "
          f"DG C3.4; {OR}"),
        C("cleared on v2.0's wording: participatory democracy, citizens' assemblies and referendums let those affected "
          "challenge and reverse decisions", f"{OR}"),
        U("not shown: no implementation record, and no modelling of adjustments to the design's parameters in operation "
          "(part (b1), reading 3.1); decision 79.4's rule needs clauses 1 to 3 cleared", f"{V1}, DG C3.4")])),
    ("PE", "C3.4"): dict(now=1.0, proposed=0.5, ledger="D66", unit=unit("owner", [
        C("councils adjust proposals based on feedback, every planning cycle", "as audited (the unit's own text)"),
        U("not shown: 'democratic structure enables rapid evidence-based changes' dates no update against evidence; the "
          "planning cycle is annual (the outside reader reads the clause short)", f"{V1}, PE C3.4; {OR}"),
        C("cleared on v2.0's wording: self-managed councils of those affected decide and can reverse", f"{OR}"),
        U("not shown: no implementation record, and no modelling of adjustments in operation (part (b1), reading 3.1); "
          "decision 79.4's rule needs clauses 1 to 3 cleared", f"{V1}, PE C3.4")])),
}
