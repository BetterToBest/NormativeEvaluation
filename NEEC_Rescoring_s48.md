# NEEC Rescoring Pass — Record: C4.4 Power Distribution Re-read on Decision 48.3, and the Score Ledger

**Session 48 · 2026-09-24 · Scorer and engineer: Claude · Owner: Duke Johnson**
**Status: scratch (protocol 10.1). Parts (a) to (b7) are `NEEC_Rescoring_s37.md` to `NEEC_Rescoring_s43.md` and
`NEEC_Rescoring_s47.md`; this record continues the pass and edits none of them.** No corpus file, score or scoring
document changes until the pass ends. Its changes are then applied by generator with pinned inputs and restated in
place (protocol 10.2, 10.3; decisions D12, D14), and until then the published totals stand, provisional as
`README.md` says. Decision 48.3 is Claude's under a delegation the owner extended to this question in Session 48;
it is recorded with its reasons in `NEEC_Criteria_v2_s45.md`, and the owner may reverse it.
**Reproduce:** `python3 rescoring_s48.py` (harness check 92). The script holds the six C4.4 records below on
decision 48.3's measure, checks them against part (b7)'s, computes Nordic Social Democracy's clause 1 bound from its
published inputs, computes every figure in sections 5 and 6 cumulatively with parts (a) to (b7) on the published
26-criterion structure, checks the published totals against `neec_scores.csv`, and checks that this record contains
its generated tables verbatim.

---

## 1. What this record is

The owner's message for Session 48 settled or delegated the three questions Handoff 47 left open, and asked why the
totals fell although three criteria were added. This record carries the one of the three that changes a score, and
answers the question.

- **The WJP bar (48.1).** Delegated to Claude; kept at 0.77, with reasons. No unit has been scored on C4.6, so no
  score changes.
- **Time-limited compulsion (48.2).** The owner's decision: standing vaccination requirements are included. The
  adopted text already said so; no score changes until C2.6's units are scored in stage 2.
- **Nordic Social Democracy's C4.4 (48.3).** Delegated to Claude. C4.4 clause 1 is defined now rather than in v2.1:
  the share of employment in organizations whose investment, production and employment decisions answer to those
  they affect, at least 80%. Part (b7) scored all six of C4.4's units in the pass on the undefined clause, so each is
  re-read here on the defined one (section 3).
- **The owner's question** is answered by the score ledger (section 6), which traces every entry's total from its
  published figure through each part of the pass.

**Outcome.** Nordic Social Democracy stays at 0.5 on C4.4, now short on clause 1 rather than not shown, and its flag
is removed. CCO-PTF-CIP-SZH, the owner's design, falls from 1.0 to 0.5: its sources place its accountable
organizations beside private markets and state no share of employment for them. Participatory Economics, Integral
and Market Socialism stand; Degrowth stays at 0.5. Net −0.5 points; no failure count and no tier changes;
CCO-PTF-CIP-SZH keeps first place, 18.5 against Participatory Economics' 15.5.

## 2. How a clause is recorded, and the rule

As in part (a), section 2: each clause is cleared, short, not shown, out of reach or moot; a 1.0 stands only if every
clause is cleared or moot, and otherwise becomes 0.5 (D28, protocol 2.3). The clauses are v2.0's, unchanged by 48.3
(`criteria.json`; protocol draft.9, Appendix B). Clause 2's records are part (b7)'s, carried: 48.3 changes clause 1's
measure only, and the script asserts that clause 2's status is unchanged in every unit.

## 3. Readings (under the delegation)

**3.1 A codes on the defined measure.** The R4 audit coded clause 1 (its Session 44 clause 3) A for four of the six
units, and part (b7) carried each "as audited". Decision 48.3 restates the clause's measure, so the audited phrases are
read again against it, as part (b7)'s reading 3.2 re-read A codes on restated clauses: a phrase is carried where it
claims the defined condition, with the design's own sources for how its organizations are governed, and the clause
is estimated otherwise. Participatory Economics ("comprehensive economic democracy"), Integral ("broad democratic
accountability") and Market Socialism ("economic power distributed through democratic ownership") claim that the
economy's work is organised in bodies answerable to those who do it, and their sources say so for all of it: carried.
CCO-PTF-CIP-SZH's phrase, "CIP provides direct democratic power", claims democratic power, not a share of the
economy's decisions: estimated (reading 3.3).

**3.2 Nordic Social Democracy: short, not "not shown".** On the defined measure the clause can be read from
published series (48.3(d)). The four economies are liberal democracies on V-Dem's Regimes of the World, so their
public sectors count. The most generous count adds general government, every central-government state-owned
enterprise, the self-employed and the whole social economy (cooperatives, mutuals, associations and foundations,
though foundations are not member-governed): it is below 50% in each. The rest of employment is in companies whose
boards shareholders elect; the Nordic laws give employees a minority of seats. The figures come
from different years and bases (2022 for employment, end-2015 for state-owned enterprises, 2014–15 for the social
economy), which matters little against a gap of at least 31 points. Municipal companies are not in the OECD's count;
to close the gap they would have to employ 31–36% of workers, more than general government does in any of the four.

| Country | Regimes of the World | General government | State-owned enterprises | Self-employed | Social economy | Most generous count | Short of 80% by |
|---|---:|---:|---:|---:|---:|---:|---:|
| Denmark | 3 (liberal democracy) | 27.4% | 2.9% | 8.0% | 5.9% | 44.2% | 35.8 |
| Finland | 3 (liberal democracy) | 24.9% | 3.5% | 12.5% | 7.7% | 48.6% | 31.4 |
| Norway | 3 (liberal democracy) | 30.1% | 9.6% | 4.4% | not covered | 44.1% | 35.9 |
| Sweden | 3 (liberal democracy) | 28.2% | 2.9% | 9.5% | 4.2% | 44.8% | 35.2 |

**3.3 CCO-PTF-CIP-SZH: not shown.** The design's Public Trust Foundations are governed democratically by employees,
customers and community representatives, and CIP manages democratic voting for their decisions and Public Trust
Housing's; within them, decisions answer to those they affect. But the design's sources say, in two places, that
this network coexists with private markets rather than replacing them (the corporate transformation paper, section
3) and complements rather than displaces private operations (the glossary). Its corporate paper describes a shift
"from shareholder to stakeholder models" without saying who would elect the boards of transformed corporations, and
the participation figures the design states are a 50% market-share target for housing and a 55% threshold of
merchant participation within designated zones, neither a share of employment. No source states or projects that
the design's accountable organizations would employ 80% of workers. *Reopening:* a stated or modelled share of
employment in Public Trust Foundations and other member-governed organizations at full implementation, or a
governance rule for transformed corporations under which those they affect elect a majority of the board.

**3.4 The other units.** Participatory Economics and Integral have no owners of capital; Market Socialism places
enterprises in their workers' ownership, and in its principal component the worker-members elect and can dismiss
the governing council (Ley 11/2019, article 46). Degrowth's clause stays not shown on the defined measure: no source
states the share of employment degrowth would place in accountable organizations.

## 4. The units

### 4.1 Summary (generated)

| Entry | Criterion | Clauses | Verdict |
|---|---|---|---|
| DG | C4.4 | U U | part (b7) 0.5 → 0.5 |
| PE | C4.4 | C C | part (b7) 1.0 → 1.0 |
| CCO | C4.4 | U C | part (b7) 1.0 (flagged) → 0.5 |
| INT | C4.4 | C C | part (b7) 1.0 → 1.0 |
| NSD | C4.4 | S C | part (b7) 0.5 (flagged) → 0.5 |
| MS | C4.4 | C C | part (b7) 1.0 → 1.0 |

Clause statuses are listed in the v2.0 Pass Threshold's order: C cleared, S short, U not shown, R out of reach, M
moot. "Part (b7)" is the verdict `NEEC_Rescoring_s47.md` recorded; this record supersedes it for these six units.

### 4.2 Clause by clause (generated)

#### DG C4.4 Power Distribution: part (b7) 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Democratic accountability for ≥80% of major decisions | not shown | on decision 48.3's measure as on part (b7)'s reading: the rationale names decentralisation, wealth caps, cooperative ownership and democratic governance, and degrowth research holds the forms of democracy compatible with degrowth to need additional study; no source states or projects the share of employment degrowth would place in organizations whose decisions answer to those they affect | Report v1.6, DG C4.4; Kallis, Kostakis, Lange, Muraca, Paulson and Schmelzer, Research on Degrowth, Annual Review of Environment and Resources 43 (2018) 291-316; NEEC_Rescoring_s47.md, DG C4.4, clause 1 |
| 2 | removal/replacement mechanisms functional | not shown | as part (b7) recorded: no mechanism of the entry's own for removing or replacing those who hold decision-making authority is specified or located | NEEC_Rescoring_s47.md, DG C4.4, clause 2 |

#### PE C4.4 Power Distribution: part (b7) 1.0 → 1.0

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Democratic accountability for ≥80% of major decisions | cleared | the audited phrase, comprehensive economic democracy, claims the defined condition: the model has no owners of capital and no managerial hierarchy, places all production in workers' councils that decide by their members' votes and all consumption in consumers' councils, and federations of councils they elect decide wider matters, so the investment, production and employment decisions of every workplace are taken by those who work there or by those they elect (all of the design's employment) | as audited, re-read against decision 48.3's measure (the unit's own text); Report v1.6, PE C4.4; participatoryeconomy.org, The Model: Overview (The Participatory Economy Project), accessed 2026-09-24 |
| 2 | removal/replacement mechanisms functional | cleared | as part (b7) recorded: workers' and consumers' councils elect recallable and rotated representatives to their federations | NEEC_Rescoring_s47.md, PE C4.4, clause 2 |

#### CCO C4.4 Power Distribution: part (b7) 1.0 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Democratic accountability for ≥80% of major decisions | not shown | the audited phrase, CIP provides direct democratic power, does not claim the defined condition, so the clause is estimated: CIP administers the currency and manages democratic voting for the Public Trust Housing and Public Trust Foundation decisions, and the Public Trust Foundations (grocers, restaurants, utilities and transit accepting basic units) are governed democratically by employees, customers and community representatives; but the design's sources say this network coexists with private markets rather than replacing them and complements rather than displaces private operations, its corporate paper describes a shift from shareholder to stakeholder models without saying who would elect the boards of transformed corporations, and the participation figures it states are for housing (a 50% market share target) and for merchants within designated zones (55% before synergy effects activate), not for employment; no source states or projects that the accountable organizations would employ 80% of workers | research hub at 8e8a6ba: corporate-transformation.html (abstract and section 3); wiki/glossary.html (Public Trust Foundation); cco-ptf-simulation-replication.html (glossary: SZH, CIP); index.html (PTH penetration target); Report v1.6, CCO C4.4 |
| 2 | removal/replacement mechanisms functional | cleared | as part (b7) recorded: Public Trust Housing leadership has term limits, mandatory rotation and recall elections, and the merit juries are selected at random and rotated | NEEC_Rescoring_s47.md, CCO C4.4, clause 2 |

*Note:* part (b7)'s flag on clause 2 (alternative 0.5) no longer bears on the verdict, which clause 1 fixes at 0.5, and is dropped; under the alternative recorded in decision 48.3(e) the unit would return to 1.0 with that flag.

#### INT C4.4 Power Distribution: part (b7) 1.0 → 1.0

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Democratic accountability for ≥80% of major decisions | cleared | the audited phrase, broad democratic accountability, claims the defined condition: the design delegates no managerial authority, decisions are taken by participants in CDS at every scale with local autonomy preserved, production is coordinated by rotating teams that coordinate rather than command, and ITC's non-accumulability keeps wealth from converting into power, so the investment, production and employment decisions are taken by those they affect (all of the design's employment) | as audited, re-read against decision 48.3's measure (the unit's own text); Integral white paper v0.1 (INTEGRAL-Paper-V0.1.pdf, md5 a6defc9a, accessed 2026-09-24), sections 5.2 and 5.5; Report v1.6, INT C4.4 |
| 2 | removal/replacement mechanisms functional | cleared | as part (b7) recorded: decisions taken in CDS can be reaffirmed, amended, revoked or reopened by its review module, and no managerial authority is delegated | NEEC_Rescoring_s47.md, INT C4.4, clause 2 |

#### NSD C4.4 Power Distribution: part (b7) 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Democratic accountability for ≥80% of major decisions | short | V-Dem's Regimes of the World classes Denmark, Finland, Norway and Sweden as liberal democracies, so their public sectors count; on the most generous count (all of general government, every central-government state-owned enterprise, the self-employed, and every cooperative, mutual, association and foundation) the share of employment in organizations whose decisions answer to those they affect is at most 44.2% in Denmark, 48.6% in Finland and 44.8% in Sweden, and 44.1% in Norway before its social economy, which would have to employ 35.9% of workers, 3.6 times the highest share in the EU-28 (Luxembourg's 9.9%); the rest work in companies whose boards shareholders elect, employees electing a minority (Sweden two or three members, a quarter to a third of the board; Norway and Denmark a third; Finland as agreed, in companies of 150 or more); short of 80% in each, by at least 31 points (decision 48.3(d)) | OECD, Government at a Glance 2025 (general government employment, % of total employment, 2022); OECD, The Size and Sectoral Distribution of State-Owned Enterprises (2017), Figure 10; Eurostat lfsa_egaps (2022); CIRIEC for the EESC, Recent Evolutions of the Social Economy in the European Union (2017), Table 7.2; V-Dem Regimes of the World (Our World in Data, political-regime, 2022); worker-participation.eu, Denmark, Finland, Norway and Sweden (board-level representation) |
| 2 | removal/replacement mechanisms functional | cleared | parliamentary removal functions: Sweden's prime minister lost a confidence vote on 21 June 2021, as part (a) found | NEEC_Rescoring_s47.md, NSD C4.4, clause 2 (Riksdag confidence vote, 21 June 2021) |

*Note:* part (b7)'s flag (alternative 1.0, on its reading 3.6(b)) is removed: decision 48.3 fixes the reading, and the reading the flag named is recorded there as the alternative for the owner.

#### MS C4.4 Power Distribution: part (b7) 1.0 → 1.0

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Democratic accountability for ≥80% of major decisions | cleared | the audited phrase, economic power distributed through democratic ownership, claims the defined condition: the system places enterprises in the ownership of those who work in them and removes the employer-employee hierarchy, and in its principal component each cooperative's worker-members elect the governing council, one member one vote, and can dismiss it in general assembly (all of the system's employment) | as audited, re-read against decision 48.3's measure (the unit's own text); Report v1.6, MS C4.4; Ley 11/2019, de 20 de diciembre, de Cooperativas de Euskadi, article 46; International Co-operative Alliance, Statement on the Cooperative Identity, principle 2 |
| 2 | removal/replacement mechanisms functional | cleared | as part (b7) recorded: administrators serve two to five years and the general assembly may dismiss them and elect their replacements in the same session | NEEC_Rescoring_s47.md, MS C4.4, clause 2 |

## 5. What the pass so far changes (generated)

| Entry | Published (rank) | After (b7) (rank) | After 48.3 (rank) | Change here | Failures | Tier |
|---|---:|---:|---:|---:|---:|---|
| CCO | 24.5 (1) | 19.0 (1) | 18.5 (1) | -0.5 | 0 | Potentially Adequate |
| PE | 20.5 (2) | 15.5 (2) | 15.5 (2) | 0.0 | 1 | Potentially Adequate |
| NSD | 19.5 (3) | 14.5 (3) | 14.5 (3) | 0.0 | 2 | Potentially Adequate |
| INT | 19.5 (3) | 14.5 (3) | 14.5 (3) | 0.0 | 3 | Partially Adequate |
| DG | 19.0 (5) | 14.5 (3) | 14.5 (3) | 0.0 | 2 | Potentially Adequate |
| MS | 16.5 (6) | 13.5 (6) | 13.5 (6) | 0.0 | 2 | Potentially Adequate |
| MMT | 15.5 (7) | 12.0 (11) | 12.0 (11) | 0.0 | 3 | Partially Adequate |
| UBI | 14.5 (8) | 11.5 (15) | 11.5 (15) | 0.0 | 7 | Structurally Inadequate |
| MC | 14.5 (8) | 12.5 (8) | 12.5 (8) | 0.0 | 3 | Partially Adequate |
| OS | 14.5 (8) | 13.0 (7) | 13.0 (7) | 0.0 | 3 | Partially Adequate |
| SWF | 14.0 (11) | 12.5 (8) | 12.5 (8) | 0.0 | 3 | Partially Adequate |
| SG | 14.0 (11) | 12.0 (11) | 12.0 (11) | 0.0 | 4 | Partially Adequate |
| GEO | 13.5 (13) | 12.5 (8) | 12.5 (8) | 0.0 | 2 | Potentially Adequate |
| UBS | 13.5 (13) | 12.0 (11) | 12.0 (11) | 0.0 | 3 | Partially Adequate |
| IF | 13.5 (13) | 12.0 (11) | 12.0 (11) | 0.0 | 5 | Partially Adequate |
| FALC | 13.0 (16) | 9.5 (16) | 9.5 (16) | 0.0 | 10 | Structurally Inadequate |
| DE | 11.5 (17) | 9.0 (19) | 9.0 (19) | 0.0 | 8 | Structurally Inadequate |
| SQ | 10.5 (18) | 9.5 (16) | 9.5 (16) | 0.0 | 9 | Structurally Inadequate |
| CPS | 10.0 (19) | 8.0 (21) | 8.0 (21) | 0.0 | 12 | Structurally Inadequate |
| SC | 10.0 (19) | 9.0 (19) | 9.0 (19) | 0.0 | 9 | Structurally Inadequate |
| CN | 10.0 (19) | 9.5 (16) | 9.5 (16) | 0.0 | 8 | Structurally Inadequate |
| QA | 9.0 (22) | 8.0 (21) | 8.0 (21) | 0.0 | 10 | Structurally Inadequate |
| LM | 8.0 (23) | 6.5 (23) | 6.5 (23) | 0.0 | 15 | Structurally Inadequate |

"After (b7)" is the total after parts (a) to (b7) (`NEEC_Rescoring_s47.md`, section 5, whose "D28 units left"
column this record does not change). Totals are on the published 26-criterion structure.

After this record the corpus has 21 dominance pairs against 21 after part (b7) (new: none; lost: none), and its frontier holds 13 entries against 13 (NSD, MS, LM, UBI, DG, FALC, PE, CCO, INT, MC, SWF, IF, OS). First place: CCO, 19.0 after part (b7), 18.5 now. Across the pass so far 128 units have been re-estimated, each counted once: 10 stand and 118 are at 0.5 (59.0 points). C4.4 keeps 3 1.0s (MS, PE, INT) against 6 published; its anchor example, Participatory Economics, stands.

Flags added by the pass so far: 18 (against 20 after part (b7)); removed: 7. Across the pass so far, 15 entries' flag registers change (CCO, CN, CPS, DG, IF, LM, MC, NSD, OS, QA, SG, SQ, SWF, UBI, UBS).

## 6. The score ledger: why the totals fell although three criteria were added (generated)

The owner asked why every total went down although v2.0 adds three criteria, recalling CCO-PTF-CIP-SZH at 22.5/26
and now at 19/29, and asked for care about version drift. The ledger below answers from the files, not from memory.

**What was published.** CCO-PTF-CIP-SZH's published total is 24.5/26 (94%), 0 failures: `neec_corpus.json`,
`neec_scores.csv`, `README.md` and Report v1.6 agree, and the script asserts the first three and the Report's
figure. Report v1.6 also records its history: 23.5/25 in version 1, and 24.5/26 after Session 8's retrofit split
C1.2 into C1.2a and C1.2b (one more criterion, one more point). No file in the repository's history gives it 22.5/26;
the one total of 22.5 in Paper v1.4 is Integral's, under two of Appendix A.4's alternative weightings (out of 32 and
30).

**What "19" was.** Handoff 47's 19.0 was CCO-PTF-CIP-SZH's total on the published 26 criteria after parts (a) to
(b7) of the pass: 19.0/26, not 19/29. No total on 29 criteria exists yet: the three new criteria (C2.6 Civil
Liberties and Rule of Law, C3.6 Productive and Innovative Capacity, C4.6 Harm Internalization) have 69 units, none
scored, so they add nothing to any total and are left out of every denominator until stage 2 scores them.

**Why the totals fell.** Every fall so far is the rescoring pass of decision D28 (Session 35). The R4 audit found that
most published 1.0s resting on a Pass Threshold of several clauses showed only some of the clauses. D28 requires a
1.0 to show every clause, on evidence named in the scoring record, and otherwise scores 0.5; it never scores 0.0 in
the pass, so no failure count and no tier can change. The pass has re-estimated 128 units so far and 118 are at 0.5.
The entries that lose most are those with the most 1.0s whose sources state goals rather than estimates of each
clause: CCO-PTF-CIP-SZH was published with 23 criteria at 1.0, more than any other entry. The ledger shows each
entry's published total, the change each part of the pass made, and where it stands; each entry's changes sum to its
move, and the published totals equal `neec_scores.csv`'s.

| Entry | Published | (a) | (b1) | (b2) | (b3) | (b4) | (b5) | (b6) | (b7) | 48.3 | Now | Re-estimated | At 0.5 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| CCO | 24.5 | -0.5 | -1.5 | -0.5 | -0.5 | -0.5 | -0.5 | -1.0 | -0.5 | -0.5 | 18.5 | 13 | 12 |
| PE | 20.5 |  | -1.5 | -0.5 | -0.5 | -1.5 |  | -0.5 | -0.5 |  | 15.5 | 11 | 10 |
| NSD | 19.5 | -2.5 | -1.0 | -0.5 | -0.5 | -0.5 |  |  |  |  | 14.5 | 10 | 10 |
| INT | 19.5 | -0.5 | -1.0 | -0.5 |  | -1.0 | -0.5 | -1.0 | -0.5 |  | 14.5 | 11 | 10 |
| DG | 19.0 |  | -1.5 | -0.5 | -0.5 | -0.5 |  | -0.5 | -1.0 |  | 14.5 | 9 | 9 |
| MS | 16.5 | -1.0 | -1.5 | -0.5 | -0.5 |  |  |  | 0.5 |  | 13.5 | 8 | 6 |
| MMT | 15.5 | -1.5 | -1.0 | -0.5 | -0.5 |  |  |  |  |  | 12.0 | 7 | 7 |
| UBI | 14.5 | -1.5 | -0.5 | -0.5 | -0.5 |  |  |  |  |  | 11.5 | 7 | 6 |
| MC | 14.5 |  | -1.0 | -0.5 |  |  | -0.5 |  |  |  | 12.5 | 4 | 4 |
| OS | 14.5 | -0.5 |  |  |  |  | -0.5 | -0.5 |  |  | 13.0 | 4 | 3 |
| SWF | 14.0 |  |  | -0.5 |  |  | -0.5 | -0.5 |  |  | 12.5 | 4 | 3 |
| SG | 14.0 | -1.0 | -0.5 | -0.5 |  |  |  |  |  |  | 12.0 | 4 | 4 |
| GEO | 13.5 | -0.5 |  |  |  |  | -0.5 |  |  |  | 12.5 | 2 | 2 |
| UBS | 13.5 |  | -0.5 | -0.5 |  |  | -0.5 |  |  |  | 12.0 | 4 | 3 |
| IF | 13.5 | -1.0 |  |  |  |  | -0.5 |  |  |  | 12.0 | 3 | 3 |
| FALC | 13.0 | -0.5 | -0.5 |  | -0.5 | -1.0 |  | -0.5 | -0.5 |  | 9.5 | 7 | 7 |
| DE | 11.5 | -0.5 | -0.5 |  |  |  | -0.5 | -0.5 | -0.5 |  | 9.0 | 5 | 5 |
| SQ | 10.5 | -0.5 |  |  |  | -0.5 |  |  |  |  | 9.5 | 2 | 2 |
| CPS | 10.0 | -1.5 |  |  | -0.5 |  |  |  |  |  | 8.0 | 4 | 4 |
| SC | 10.0 |  | -1.0 |  |  |  |  |  |  |  | 9.0 | 2 | 2 |
| CN | 10.0 |  |  | -0.5 |  |  |  |  |  |  | 9.5 | 1 | 1 |
| QA | 9.0 | -0.5 |  | -0.5 |  |  |  |  |  |  | 8.0 | 2 | 2 |
| LM | 8.0 | -1.5 |  |  |  |  |  |  |  |  | 6.5 | 4 | 3 |

Parts (a) to (b7) are Sessions 37 to 43 and 47; "48.3" is this record. "Re-estimated" counts the entry's units the
pass has re-estimated; "At 0.5" those it scores 0.5. Every re-estimated unit was a published 1.0; one of them, Market
Socialism's C4.4, fell in part (a) and returned to 1.0 in part (b7).

CCO-PTF-CIP-SZH was published at 24.5/26 with 23 criteria at 1.0, more than any other entry (the next, Participatory Economics, had 16). The pass has re-estimated 13 of them; 12 are at 0.5, so it stands at 18.5/26 (24.5 - 12 x 0.5). Its three v2.0 criteria (C2.6, C3.6, C4.6) are not scored yet, so no total on 29 criteria exists: when they are, its 29-criterion total will be its 26-criterion total after the pass plus 0 to 3.

| Criterion | Published | Now | Part (session) | Clauses not shown or short |
|---|---:|---:|---|---|
| C1.1 | 1.0 | 0.5 | (b3) (s40) | 1 (≥90% poverty reduction within 20 years under base scenario) short; 2 (≥85% under stress testing) short |
| C2.1 | 1.0 | 0.5 | (b4) (s41) | 2 (validated through revealed preference showing acceptance of initially refused employment/living situations when alternatives exist) not shown |
| C2.3 | 1.0 | 0.5 | (b1) (s38) | 1 (≥50% regular creative engagement) not shown; 3 (meaning/purpose satisfaction scores ≥70/100) not shown |
| C2.4 | 1.0 | 0.5 | (b1) (s38) | 2 (≥35% citizen proposals adopted) not shown; 3 (≥65% satisfaction with responsiveness) not shown |
| C2.5 | 1.0 | 0.5 | (b5) (s42) | 1 (Exit feasible within 3 months without material penalty) short |
| C3.1 | 1.0 | 0.5 | (a) (s37) | 2 (scaling 1:1 with crisis severity (30% GDP decline = 30% benefit increase)) short; 3 (≥90% population coverage) not shown |
| C3.4 | 1.0 | 0.5 | (b1) (s38) | 4 (zero collapses during parameter adjustments) not shown |
| C3.5 | 1.0 | 0.5 | (b6) (s43) | 3 (correction success ≥70%) not shown; 4 (externalization <10% of total costs) not shown |
| C4.1 | 1.0 | 0.5 | (b6) (s43) | 2 (resource use ≤90% regeneration) not shown; 3 (debt-to-GDP <80%) not shown |
| C4.2 | 1.0 | 0.5 | (b7) (s47) | 1 (Consumption-based carbon emissions falling ≥3.8% a year) not shown; 2 (biodiversity neutral or positive) not shown; 3 (resource extraction ≤ regeneration) not shown; 4 (no more than two of the four nationally downscaled planetary boundaries transgressed) not shown |
| C4.4 | 1.0 | 0.5 | 48.3 (s48) | 1 (Democratic accountability for ≥80% of major decisions) not shown |
| C5.1 | 1.0 | 0.5 | (b2) (s39) | 1 (≥70% of system components proven through ≥20 years operation at scale ≥10,000 participants) not shown |
| C5.2 | 1.0 | 1.0 | (a) (s37) | none: stands |

Clause texts are those the part scored against: the Session 44 clauses for parts (a) to (b6), v2.0's for part (b7)
and this record. C5.2 is the one re-estimated unit that stands.

**What comes next for the totals.** Three things remain before any total on 29 criteria is published, and two of
them can raise totals: stage 2 scores the 69 new units (each entry gains 0 to 3 points); the class D, I and M
re-checks can raise units as well as lower them (a class D unit at 0.5 rises when a deleted clause was the only one
not shown; 18 such units wait); and 17 D28 units remain for part (b), which can only stay or fall. Stage 3 then
applies the pass by generator to the corpus, the CSV and the totals, with every change traceable to a record like this
one.

**Version drift.** The published scores have one source, `neec_corpus.json`, from which the CSV, `README.md` and the
generated figures are built and checked; the file has not changed since the repository's first commit (Session 34). Every change the pass makes
is held in a committed script (`rescoring_s37.py` to `rescoring_s48.py`), each recomputing the totals from the corpus
and every earlier part, so a figure in any handoff can be reproduced from the files; the harness runs all of them on
every landing. The ledger above is that reproduction for every entry.

## 7. Corrections found (not polish)

1. **Part (b7) applied the accountability clause unevenly.** Its reading 3.6 held Nordic Social Democracy's clause
   1 not shown because the major decisions of private firms answer to their owners, while CCO-PTF-CIP-SZH's clause 1
   was carried "as audited" although its own sources place its accountable organizations beside private markets.
   The carry rule shielded the owner's design from the test applied to Nordic Social Democracy. Decision 48.3 and
   reading 3.1 here apply one test to both.
2. **Report v1.6, Nordic Social Democracy, C4.4,** scores 1.0 on "corporate governance reforms (worker board
   representation)", while its Stakeholder Capitalism entry scores 0.0 because "Worker directors remain a minority
   on boards". Nordic board representation is a minority (a quarter to a third of seats). Report v2.0 states Nordic
   Social Democracy's C4.4 on the defined measure.

## 8. Disclosure

CCO-PTF-CIP-SZH is the owner's design. It falls on C4.4 (0.5 points) on a definition Claude adopted under the owner's
delegation, the same definition on which Nordic Social Democracy is short and on which Participatory Economics,
Integral and Market Socialism stand. The alternative recorded for the owner (48.3(e)) would restore it to 1.0 and
raise Nordic Social Democracy to 1.0. The design's sources are the research hub at `8e8a6ba`; no simulation run is
used (the published model does not represent enterprise governance).

*Note for the design's maintainers* (the owner's project, not a NEEC correction): the sources state how Public Trust
Foundations are governed but not what share of the economy's employment they are designed to hold, nor who elects the
boards of the corporations the corporate transformation paper describes; either would decide C4.4 clause 1.

## 9. What remains

- **(b), continued:** 17 D28 units, unchanged by this record (`NEEC_Rescoring_s47.md`, section 8): C4.3 (6), C4.5
  (3), C5.2 (4), C5.4 (2) and C5.5 (2), on their v2.0 clauses.
- **Stage 2's other work** as Handoff 47 lists it, with one change: C4.4 is now class M, so its seven published 0.5s
  and ten published 0.0s are re-checked clause by clause on the defined measure (for the configured national
  economies, from the series 48.3(d) names), and class D's rises are 18 units.
- When the pass ends, its changes are applied by generator (stage 3).

## 10. What this record does not show

It is one scorer's re-reading, on the entries' own texts, the design's research-hub sources, Integral's white paper,
the cooperative law in force and the published employment series named in section 3. "Not shown" means no evidence
was located, not that the clause fails. The employment share stands in for a share of decisions, which no source
counts (48.3(c)); a weighting by value added or by capital is not published on this basis and is not attempted.
Whether these calls reproduce is what the replication programme tests.
