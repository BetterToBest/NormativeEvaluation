# NEEC Revision R4 — The Multi-Clause Audit and Decision D28

**Session 35 · 2026-09-22 · Scorer and engineer: Claude · Owner: Duke Johnson**
**Status: decided.** From Session 35 the owner has delegated methodological decisions to Claude. Each decision
is recorded here with its reasons and its computed consequences, and the owner may reverse any of them.
**Reproduce:** `python3 r4_audit_s35.py` (harness check 75). The script locates every rationale and every
coded phrase, computes every figure below, and checks that this record contains its two tables verbatim.
No score, corpus file or scoring document changes in this session.

---

## 1. Why this audit

The first blind replication (`NEEC_OstromCommons_replication_record.md`, section 4) scored Ostrom-style
commons governance 0.5 on C4.1 where the original scored 1.0. Both agreed on the evidence. They disagreed on
the rule: C4.1's Pass Threshold has four clauses, two of which (carbon trajectory, debt-to-GDP) lie outside
what a commons institution governs, while the anchor's 1.0 band asks only that preservation be "structural,
not incidental". Protocol 2.1 makes 1.0 "a claim that the threshold is cleared" and 2.3 scores against the
Pass Threshold; 4.6 supplies anchors that describe each band more loosely. Revision R4 (replication record,
10.3) asked for an audit of every corpus 1.0 resting on a multi-clause threshold before any rule was written.

## 2. What was audited, and how

**Population.** Twenty-one of the 26 criteria have a Pass Threshold with more than one clause; five (C1.2a,
C1.2b, C1.5, C2.2, C3.3) have one. Of the corpus's 184 scores of 1.0, **167** rest on a multi-clause
threshold. Each threshold is split into verbatim clauses (542 clause judgments in all).

**Text.** Each unit's rationale as scored: the criterion line of the entry's Part I block in Report v1.6 for
the thirteen entries scored before the v2 scoring documents (124 units), and the criterion section of the
entry's own scoring document for the other ten (43 units).

**Codes.** Each clause of each unit is coded from the unit's own text:

| Code | Meaning |
|---|---|
| A | addressed: the text claims the clause's condition holds, in terms compatible with its bar (hedged projections for designs count) |
| P | partial: the text addresses the clause but its own claim stops short (an improvement where a level is set, "moderately", a straddling range, fewer phases than required, the question left open or scored elsewhere) |
| X | shortfall: a figure below the bar, or a concession that the condition does not hold |
| S | silent: no claim about the clause's subject (naming a mechanism without saying what it achieves counts as silent) |
| N | moot: the text establishes that the clause cannot apply (a transition, scale-up or coordination shown not to be needed) |
| lower case | outside the reach of a mechanism-class entry: a quantity the mechanism does not govern even when generalised (protocol 3.2) |

Every A, P, X and N carries a phrase located in the rationale; every lower-case code carries a stated reason
(18 clauses in 10 units). The coding reads the text as written. It measures whether each 1.0 is *shown*
clause by clause; it is not a rescoring on the evidence.

## 3. Results

| Criterion | Clauses | Audited 1.0s | Clause judgments | Stand under D28 | Stand if out-of-reach clauses are excused | Survive the stated-shortfall rule |
|---|---:|---:|---:|---:|---:|---:|
| C1.1 | 2 | 9 | 18 | 0 | 0 | 9 |
| C1.3 | 2 | 9 | 18 | 6 | 6 | 7 |
| C1.4 | 2 | 4 | 8 | 2 | 2 | 4 |
| C2.1 | 2 | 8 | 16 | 0 | 0 | 5 |
| C2.3 | 3 | 8 | 24 | 0 | 0 | 6 |
| C2.4 | 3 | 8 | 24 | 0 | 0 | 6 |
| C2.5 | 4 | 10 | 40 | 0 | 1 | 10 |
| C3.1 | 3 | 7 | 21 | 0 | 0 | 5 |
| C3.2 | 3 | 9 | 27 | 3 | 3 | 7 |
| C3.4 | 4 | 17 | 68 | 1 | 1 | 11 |
| C3.5 | 4 | 3 | 12 | 0 | 0 | 2 |
| C4.1 | 4 | 8 | 32 | 0 | 1 | 8 |
| C4.2 | 4 | 7 | 28 | 0 | 0 | 6 |
| C4.3 | 3 | 7 | 21 | 1 | 1 | 7 |
| C4.4 | 4 | 6 | 24 | 0 | 0 | 4 |
| C4.5 | 3 | 6 | 18 | 0 | 0 | 3 |
| C5.1 | 2 | 13 | 26 | 11 | 11 | 11 |
| C5.2 | 5 | 7 | 35 | 1 | 1 | 5 |
| C5.3 | 4 | 15 | 60 | 6 | 6 | 12 |
| C5.4 | 3 | 2 | 6 | 0 | 0 | 2 |
| C5.5 | 4 | 4 | 16 | 2 | 2 | 4 |
| All | | 167 | 542 | 33 | 35 | 134 |

**Only 33 of the 167 are shown clause by clause.** A further 101 leave at least one clause unaddressed, and 33
contain a clause that their own text states falls short.

**Clauses no audited 1.0 shows cleared.** C1.1's stress clause (≥85% under stress testing, 9 of 9 units, although
protocol 2.1 asks a pass to hold "where the criterion specifies one, under stress"); C2.1's revealed-preference validation (8 of 8); C2.3's
satisfaction score (8 of 8); C2.4's proposal-adoption and responsiveness clauses (8 of 8 each); C3.5's
correction rate (3 of 3); C4.1's debt-to-GDP clause (8 of 8); C4.2's biodiversity clause (7 of 7); C4.4's
removal mechanisms (6 of 6); and C5.4's repeal-opposition and survival clauses (2 of 2).

**Stated shortfalls inside a 1.0.** Among the 33: Nordic Social Democracy's C4.4 gives a wealth Gini of
"~0.65-0.75" against <0.35, and its C2.3 gives 35–45% engagement against ≥50%; Libertarian Minarchism's C2.3
"only applies to economically secure minorities" and its C2.4 finds "economic democracy is entirely absent";
Centrally Planned Socialism's price controls "created shortage inflation" (C3.2) and its failures were
corrected only through "eventual collapse" (C3.5); Fully Automated Luxury Communism's C3.2 "Assumes away the
problem"; Singapore's C3.4 concedes that "some evidence-based proposals have been slow or refused"; Qatar's C5.3
flag finds "no validated scaling pathway"; Islamic finance's C5.1 leaves open "Whether the outcomes match the
design's promise". Partial claims include a 65–75% range against ≥70% (UBI C2.1; Nordic C2.4 turnout), a fixed
50% crisis increase against 1:1 scaling (CCO-PTF-CIP-SZH C3.1), three-phase pathways against ≥4 phases (MMT +
Job Guarantee and CCO-PTF-CIP-SZH C5.2), a single 25% parameter change against a ≥30% range (Sovereign Wealth
Fund Statism C3.4), and Ostrom's C3.4 setting its zero-collapse clause aside to other criteria.

**Moot clauses.** Status Quo's C5.2 ("no transition required") and three of its C5.3 clauses are moot, and
three mechanisms (Georgism, Mutual Credit, Sovereign Wealth Fund Statism) show that independent adoption needs
no coordination protocol. Status Quo's reading matches the one the three state-capitalist entries apply to
C5.2 — a pathway from where prospective adopters start, which China's entry names as "the pluralist market
democracy that most prospective adopters would start from" — so Status Quo, being that starting point, needs
none.

**How an out-of-reach clause counts decides two units.** Once silence is not credited, excusing out-of-reach
clauses changes the verdict only for Sovereign Wealth Fund Statism's C2.5 (voluntary association) and
Ostrom's C4.1 (carbon, debt-to-GDP) — the replication's case. The rule the replication tested is therefore
mostly a rule about silence.

## 4. Quoted thresholds that are not the definitions

**`criteria.json`.** Four anchor thresholds differ in substance from their definitions: C2.5 drops "voluntary
association protected"; C5.1 drops "matching claimed benefits"; C5.3 drops "validated through modeling" and
"coordination protocols established"; C3.1 adds "no legislative delay" (from the Measurement line). C2.1's
anchor also drops the revealed-preference elaboration while keeping the clause.

**The Islamic finance and Ostrom documents** quote the same working threshold under every criterion. Twelve of
the 26 differ in substance from the definitions (C2.1, C2.3, C2.4, C2.5, C3.1, C3.4, C4.2, C4.3, C4.4, C5.1,
C5.2, C5.3). C2.5's quotation replaces three clauses with "the system continues functioning at partial
participation", which comes from the anchor's 1.0 band; C3.4's drops "democratic", on which Ostrom's
"definitionally met" rests. The quotations of C5.1 and C5.3 share their anchors' departures;
C3.1's shares its anchor's addition and also drops "1:1"; C2.5's borrows the anchor's 1.0 band and C5.2's the
anchor's note ("Judge this on specificity"); the other seven (C2.1, C2.3, C2.4, C3.4, C4.2, C4.3, C4.4) drop a
clause that both the definition and the anchor keep. Eight audited 1.0s were scored against a quotation that
drops a clause (both entries, C2.5, C3.4, C5.1 and C5.3).

These are **corrections**, not polish: the anchors are to carry the definitions' text, and the two documents'
quotations are to be restated in place.

## 5. What the rules would change (the textual bound)

A 1.0 that a rule does not let stand becomes 0.5, never 0.0: each rationale describes a working mechanism, so
protocol 2.1's 0.0 conditions are not met by a clause-level gap. **No failure count and no tier can change.**
The table gives, for each entry, the audited 1.0s, those not shown clause by clause, those with a stated
shortfall, and the totals and competition ranks if every such 1.0 became 0.5.

| Entry | Audited 1.0s | Not shown (D28) | Stated shortfall | Total now (rank) | D28 bound (rank) | Stated-shortfall bound (rank) |
|---|---:|---:|---:|---:|---:|---:|
| CCO | 19 | 13 | 2 | 24.5 (1) | 18.0 (1) | 23.5 (1) |
| PE | 14 | 13 | 0 | 20.5 (2) | 14.0 (2) | 20.5 (2) |
| NSD | 13 | 12 | 5 | 19.5 (3) | 13.5 (3) | 17.0 (5) |
| INT | 14 | 12 | 1 | 19.5 (3) | 13.5 (3) | 19.0 (3) |
| DG | 12 | 11 | 0 | 19.0 (5) | 13.5 (3) | 19.0 (3) |
| MS | 8 | 7 | 2 | 16.5 (6) | 13.0 (6) | 15.5 (6) |
| MMT | 8 | 8 | 3 | 15.5 (7) | 11.5 (13) | 14.0 (8) |
| UBI | 9 | 7 | 3 | 14.5 (8) | 11.0 (15) | 13.0 (12) |
| MC | 5 | 4 | 0 | 14.5 (8) | 12.5 (8) | 14.5 (7) |
| OS | 6 | 3 | 1 | 14.5 (8) | 13.0 (6) | 14.0 (8) |
| SWF | 5 | 3 | 1 | 14.0 (11) | 12.5 (8) | 13.5 (10) |
| SG | 5 | 3 | 2 | 14.0 (11) | 12.5 (8) | 13.0 (12) |
| GEO | 3 | 2 | 1 | 13.5 (13) | 12.5 (8) | 13.0 (12) |
| UBS | 4 | 3 | 0 | 13.5 (13) | 12.0 (12) | 13.5 (10) |
| IF | 6 | 4 | 2 | 13.5 (13) | 11.5 (13) | 12.5 (15) |
| FALC | 9 | 8 | 1 | 13.0 (16) | 9.0 (18) | 12.5 (15) |
| DE | 5 | 5 | 1 | 11.5 (17) | 9.0 (18) | 11.0 (17) |
| SQ | 4 | 2 | 1 | 10.5 (18) | 9.5 (17) | 10.0 (18) |
| CPS | 6 | 5 | 3 | 10.0 (19) | 7.5 (22) | 8.5 (21) |
| SC | 3 | 3 | 0 | 10.0 (19) | 8.5 (20) | 10.0 (18) |
| CN | 2 | 0 | 0 | 10.0 (19) | 10.0 (16) | 10.0 (18) |
| QA | 2 | 1 | 1 | 9.0 (22) | 8.5 (20) | 8.5 (21) |
| LM | 5 | 5 | 3 | 8.0 (23) | 5.5 (23) | 6.5 (23) |

Under the D28 bound the corpus's dominance pairs rise from 14 to 32 and the frontier narrows from twelve
entries to six (Status Quo, Nordic Social Democracy, CCO-PTF-CIP-SZH, Integral, Islamic finance, Ostrom).
Mechanism entries with terse Report rationales fall furthest (MMT + Job Guarantee 7th to 13th, UBI 8th to
15th); entries whose rationales address clauses one by one rise (Ostrom 8th to 6th; China 19th to 16th).

**Disclosure.** CCO-PTF-CIP-SZH, which the owner designed, keeps first place under every bound, and under the
D28 bound it dominates seven entries it does not dominate now. The reason is textual: its rationales state a
figure for more clauses than most, many of them from its own modelling. A textual bound rewards stated
figures, so the rescoring below holds every design's modelled figures to the evidentiary tier of protocol 4.1,
and the second pilot — CCO-PTF-CIP-SZH, scored by a replicator outside the Claude family — is the independent
test of exactly this.

## 6. Decision D28

**Decided (Session 35).** Protocol text for v2.0-draft.5, sections 2.3, 3.2 and 4.6:

- **(a) Clause by clause.** Where a Pass Threshold has several clauses, 1.0 requires every clause to be shown
  cleared on its own estimate (2.2). The scoring document states an estimate for each clause, in order.
- **(b) Silence is not clearance.** A clause the document does not estimate cannot support a 1.0.
- **(c) Reach.** For a mechanism, a clause whose quantity the mechanism does not govern even when generalised
  (3.2) cannot be credited, since crediting it would credit the host economy. Such a clause holds the
  criterion at 0.5 at most. It does not by itself make the criterion 0.0.
- **(d) Method clauses.** A clause that names how a condition is evidenced ("validated through revealed
  preference", "validated through modeling") is satisfied by evidence at least as strong as the method named.
  Observed operation at the relevant scale is at least as strong as modelling.
- **(e) Moot clauses.** A clause whose condition cannot apply to the entry, as its document establishes, does
  not block a 1.0. The same reading is applied to every entry of the same class.
- **(f) 0.0 is unchanged.** Protocol 2.1's 0.0 conditions apply to the criterion as a whole; a clause-level
  gap alone never makes 0.0. D28 cannot change a failure count or a tier.
- **(g) Anchors describe; thresholds govern.** Where an anchor's wording and the Pass Threshold differ, the
  Pass Threshold governs (2.3). `criteria.json`'s anchor thresholds are corrected to the definitions' text,
  and a scoring document quotes the definition, not an abridgement.

**Why not the alternatives.** *Excusing out-of-reach clauses* would let a mechanism clear a threshold with
clauses uncleared, measuring it against a lower bar than a comprehensive system faces on the same criterion,
contrary to 3.2's rule that a mechanism is credited only where it does the work; the audit shows it would
decide two units. *Demoting only stated shortfalls* would count silence as clearance, although 2.1 already
places performance that "holds only under favourable or untested conditions" at 0.5, and it would make 1.0
mean different things for a terse rationale and a thorough one; independent replicators, who read the protocol
as written, would keep disagreeing on exactly these units. On the case that raised R4, Ostrom's C4.1, D28
gives the blind replication's value for the replication's reason.

## 7. Application

D28 changes scores only through the **rescoring pass**, which comes before Step 5 (Report and Paper v2.0) and
before the second pilot:

1. **Stated shortfalls first (33 units).** Each is re-estimated on the clause its own text says falls short,
   and on any clause it leaves unshown.
2. **Then the rest (101 units), criterion by criterion**, so that one criterion's clauses are read alike across
   the corpus (protocol 5): each unshown clause is estimated on cited evidence — for designs, their own
   specification and modelling at 4.1's evidentiary tier. A 1.0 stays only if every clause is then shown
   cleared; otherwise it becomes 0.5.
3. Each clause-level estimate is recorded in a rescoring document; changes are applied by generator with
   pinned inputs and restated in place (decisions D12, D14), and carried into Report v2.0's Part I, which
   replaces the Report v1.6 rationales of record for the thirteen earlier entries.

The textual bound is **134 changes, 67.0 points across the corpus, no tier changes**. One clause needs more
than its text: C5.1's second clause was coded A wherever a rationale cites documented outcomes, because no
rationale was written against "matching claimed benefits" — the anchor drops it. The rescoring therefore also
tests that clause in full for all thirteen C5.1 1.0s, eleven of which stand in section 3's table, so up to
eleven further changes are possible there. The two corrections of section 4 land with protocol draft.5 (the anchors) and with the rescoring pass (the two
documents' quotations).

## 8. What this audit does not show

It reads text, not evidence: a clause coded S may well be met, and the rescoring may restore it; a clause
coded A may rest on a claim the evidence does not bear out, which is the replication programme's question.
The boundary between A and S for qualitative claims involves judgment, and one coder made every call; each call is
traceable to a located phrase or its absence, and the register in the script's output lists, for every unit,
the clauses not shown. The textual bound counts what the text does not show; it is not a prediction of what
the rescoring will change.
