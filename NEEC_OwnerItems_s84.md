# NEEC Session 84: the owner's items applied, and two consistency gaps closed (ledger S68)

> Session 84, 2026-10-21. The layer: `owner_s84.py`; the generator: `apply_owner_s84.py` (writes `neec_corpus_v2.json`,
> `neec_scores_v2.csv`, `summary_blocks_v2.json` and the tables of this record between its `generated` markers; never by
> hand). The Session 83 state is kept byte for byte as `neec_corpus_v2_s83_snapshot.json` and its two companions. From this
> session the entry is shown as **CCO-PTF-PTH-SZH-CIP** (ledger D68, decision 84.5); the records of Sessions 1 to 83, and
> the parts of this record that quote them, keep the old name, CCO-PTF-CIP-SZH.

## 1. What was done, and the result

Session 83's adjudication of the outside review (`NEEC_Adjudication_s83.md`) put four readings to the owner and named
three consistency questions outside its scope (its section 9; ledger I12). The owner answered in the ledger on 2026-10-20.
This session applied the answers by generator, and closed the two gaps the owner's instructions named:

<!-- generated:summary -->
The layer writes 6 units: 4 owner items applied (decisions 84.1 and 84.2), 1 clause revision with the verdict held (84.3) and 1 class reading (84.4); 5 verdicts change. First place: CCO-PTF-PTH-SZH-CIP at 16.5, ahead of Nordic Social Democracy, Market Socialism, Participatory Economics at 15.5; tier changes: none. On the readings alone (no owner decision: the raises of 58.1 and 79.1 to 79.4 reversed): Nordic Social Democracy, Market Socialism, Participatory Economics first at 15.5, CCO-PTF-PTH-SZH-CIP 14.5.
<!-- /generated -->

<!-- generated:changes -->
| Decision | Criterion | Entry | Before | After | What changed |
|---|---|---|---:|---:|---|
| 84.1 | C3.4 Epistemic Adaptability | Degrowth Economics | 1.0 | 0.5 | the owner's answer to D66: the adjudication's reading applied |
| 84.1 | C3.4 Epistemic Adaptability | Participatory Economics | 1.0 | 0.5 | the owner's answer to D66: the adjudication's reading applied |
| 84.2 | C2.2 Labor Non-Necessity | CCO-PTF-PTH-SZH-CIP | 1.0 | 0.5 | the owner's answer to D67: the adjudication's reading applied |
| 84.2 | C5.3 Partial and Parallel Deployability | CCO-PTF-PTH-SZH-CIP | 1.0 | 0.5 | the owner's answer to D67: the adjudication's reading applied |
| 84.3 | C3.4 Epistemic Adaptability | CCO-PTF-PTH-SZH-CIP | 1.0 | 1.0 | clauses 1 and 3 re-read on cited sources; the verdict holds |
| 84.4 | C1.2b Prevention of Exploitative Accumulation | Participatory Economics | 1.0 | 0.5 | read by rule 4 of decision 83.4 (one reading per class) |
<!-- /generated -->

**The finding the Paper must state.** On the scores as decided, CCO-PTF-PTH-SZH-CIP is first alone at 16.5, by 1.0, under
all four weighting schemes and every single-criterion drop. On the readings alone, without any of the owner's decisions,
it stands at 14.5, fifth level with Integral and Ostrom-Style Commons Governance, and Market Socialism, Nordic Social
Democracy and Participatory Economics share first place at 15.5. First place rests on the owner's five raises (58.1, 79.1
to 79.4, which touch four CCO-PTF-PTH-SZH-CIP cells), each disclosed with the reading it replaced (section 5).

## 2. The owner's answers (decisions 84.1 and 84.2)

**84.1 (owner, ledger D66).** Degrowth Economics' and Participatory Economics' C3.4 return to 0.5. Decision 79.4 raised C3.4
to 1.0 where clauses 1 to 3 are cleared and no collapse is located; for Degrowth (clauses 1 and 2) and Participatory
Economics (clause 2) those clearances rested only on the published rationale's words, which rule 3 of decision 83.4 does
not accept. The adjudication's units (`adjudicate_s83.OWNER`) are applied unchanged: Degrowth 14.5 to 14.0, Participatory
Economics 16.5 to 16.0 (before 84.4). Decision 79.4 stands for Integral and Ostrom-Style Commons Governance, whose
clauses 1 to 3 are cleared on sources.

**84.2 (owner, ledger D67; supersedes D65's hold under decision 69.4).** CCO-PTF-PTH-SZH-CIP's C2.2 and C5.3 go to 0.5, as
the adjudication reads them: C2.2's provision is unconditional but pays citizens and legal residents 18 and over, and the
design's own model leaves adults below their cost of living; C5.3's papers put minimum viable participation at 55 to 65%,
against an integrated framework's 30% that states no computation. Each keeps the published reading as its close call
toward 1.0. The owner's reason: holding these two while the adjudication lowers other entries' cells on the same footing
would be a double standard; the route back up is the push-back route (ledger S72) and the Hub v2 work, which feeds the
24th entry (S70), not these cells. CCO-PTF-PTH-SZH-CIP 17.5 to 16.5.

One point for the record: C5.3's unit, as the adjudication wrote it, still clears clauses 2 to 4 "as audited (the unit's
own text)". The verdict is 0.5 on clause 1 whatever those clauses read, so nothing turns on them now; a push-back case on
C5.3 (S72) must source them as section 3 sources C3.4's.

## 3. CCO-PTF-PTH-SZH-CIP's C3.4: clauses 1 and 3 sourced (decision 84.3, correction to the record)

The unit's clauses 1 and 3 rested on "as audited (the unit's own text)", the footing rule 3 of decision 83.4 rejected for
Degrowth and Participatory Economics. Decision 79.3 governs clause 4 only. Each clause is now read on the design's own
documents (the Research Hub at 8e8a6ba, as cached for the outside review in `outside_kit_sources/`):

| # | Clause (v2.0) | Status | Reading | Source |
|---|---|---|---|---|
| 1 | ≥30% parameter adjustability range | cleared | the inflation paper's sensitivity analysis cuts the maximum octaves from 8 to 4 (50%) and runs participation from 5% to 35%, keeping inflation below 1.8% and 89% of the welfare gains; the integrated framework sets the conversion multiplier at 1-9x against tested alternatives of 1-5x and 1-12x, and a regional adjustment factor of 0.8-1.2; the scorer's adjustment run on the v5.6 engine moves the Basic Unit 30% either way from year 10 | dual-currency-inflation.html, section 5.3; cco-ptf-integrated-framework.html, sections 3.1.2 and 5.4; `NEEC_Rescoring_s57.md`, reading 3.11 |
| 3 | changes open to challenge and reversal by those affected | cleared | under the Citizens Internet Portal any citizen can submit a proposal (signature threshold, 30-90 day comment period, amendment); a binding change passes by a 60-67% supermajority with geographic distribution; referenda move from advisory to binding in the second phase (years 4-7); the PTH charter template adds notice, hearing and appeal rights on every enforcement action | citizens-internet-portal.html, sections 4.4 and 7.1; democratic-governance-pth.html, Appendix B.1, Article VI, section 2 |

Both clear, so the verdict holds at 1.0 on decision 79.3's reading of clause 4. The class check (rule 4): Degrowth's and
Participatory Economics' clause 3 were cleared in Session 83 on the same kind of provision (citizens' assemblies,
referendums, councils of those affected that decide and can reverse), so the readings agree. Two limits stand in the
record: the supermajority makes reversal harder than enactment's simple majority for advisory votes, and binding
referenda begin only in the design's second phase. Neither is a bar the clause sets. The outside reader cleared both
clauses on the same documents (its clause 4 was short, the cell decision 79.3 decides).

## 4. Participatory Economics' C1.2b by rule 4 (decision 84.4, correction under the delegation; ledger I12 item 1)

The adjudication lowered Degrowth's, Integral's and Mutual Credit's class W 1.0s on C1.2b ("Gini <0.35 for wealth
distribution") because none rested on an estimate of the distribution, or on a structural argument that bounds all of it.
Participatory Economics' 1.0 rests on the same class W reading; the outside reader agreed with it, so the adjudication did
not reach it. Rule 4 of decision 83.4 (one reading per class) asks whether Participatory Economics' sources distinguish it.

**The reading: 0.5, the clause not shown.** They distinguish it in strength, not on the point the clause turns on. The
design removes private productive property, capital markets and income from ownership, and rates incomes by effort and
sacrifice; that bounds the top of the distribution more firmly than Degrowth's caps (which keep private property and
markets) or Integral's network (which runs beside existing market and state systems). But it states no bound on personal
holdings, which unequal effort ratings and saving across a lifetime leave unequal, and no source the unit cites, and none
the outside reader names, estimates the wealth Gini; the reader projected it from the design's mechanisms, closed book,
which rule 3 does not accept where the threshold asks for a figure. A bound on the top does not bound a Gini, which the
bottom of the distribution also sets. The unit keeps the published reading as its close call toward 1.0. Participatory
Economics 16.0 to 15.5; its failures are unchanged.

## 5. The standing, with and without every owner decision

<!-- generated:standing -->
| Entry | Session 83 (rank) | Session 84 (rank) | Change | Failures | Tier |
|---|---:|---:|---:|---:|---|
| CCO-PTF-PTH-SZH-CIP | 17.5 (1) | 16.5 (1) | -1.0 | 0 to 0 | Potentially Adequate |
| Nordic Social Democracy | 15.5 (3) | 15.5 (2) | 0.0 | 0 to 0 | Potentially Adequate |
| Market Socialism | 15.5 (3) | 15.5 (2) | 0.0 | 0 to 0 | Potentially Adequate |
| Participatory Economics | 16.5 (2) | 15.5 (2) | -1.0 | 0 to 0 | Potentially Adequate |
| Integral | 15.0 (5) | 15.0 (5) | 0.0 | 2 to 2 | Potentially Adequate |
| Sovereign Wealth Fund Statism | 15.0 (5) | 15.0 (5) | 0.0 | 2 to 2 | Potentially Adequate |
| Ostrom-Style Commons Governance | 15.0 (5) | 15.0 (5) | 0.0 | 3 to 3 | Partially Adequate |
| Universal Basic Income | 14.0 (9) | 14.0 (8) | 0.0 | 4 to 4 | Partially Adequate |
| Degrowth Economics | 14.5 (8) | 14.0 (8) | -0.5 | 1 to 1 | Potentially Adequate |
| Georgism / Land Value Tax (LVT + Citizen's Dividend) | 14.0 (9) | 14.0 (8) | 0.0 | 2 to 2 | Potentially Adequate |
| Islamic Finance / Profit-Sharing Banking | 14.0 (9) | 14.0 (8) | 0.0 | 3 to 3 | Partially Adequate |
| Mutual Credit / LETS | 13.5 (12) | 13.5 (12) | 0.0 | 3 to 3 | Partially Adequate |
| State Capitalism / Singapore (GLC Developmental Capitalism) | 13.5 (12) | 13.5 (12) | 0.0 | 3 to 3 | Partially Adequate |
| Status Quo Market Capitalism | 13.0 (14) | 13.0 (14) | 0.0 | 6 to 6 | Structurally Inadequate |
| Universal Basic Services | 13.0 (14) | 13.0 (14) | 0.0 | 4 to 4 | Partially Adequate |
| MMT + Job Guarantee | 12.5 (16) | 12.5 (16) | 0.0 | 4 to 4 | Partially Adequate |
| Fully Automated Luxury Communism | 12.0 (17) | 12.0 (17) | 0.0 | 7 to 7 | Structurally Inadequate |
| Stakeholder Capitalism | 11.5 (18) | 11.5 (18) | 0.0 | 6 to 6 | Structurally Inadequate |
| State Capitalism / China (Party-State-Directed Market Economy) | 11.5 (18) | 11.5 (18) | 0.0 | 8 to 8 | Structurally Inadequate |
| State Capitalism / Qatar (Gulf Rentier-Distributive Statism) | 10.0 (20) | 10.0 (20) | 0.0 | 10 to 10 | Structurally Inadequate |
| Libertarian Minarchism | 9.5 (21) | 9.5 (21) | 0.0 | 11 to 11 | Structurally Inadequate |
| Doughnut Economics | 9.5 (21) | 9.5 (21) | 0.0 | 10 to 10 | Structurally Inadequate |
| Centrally Planned Socialism | 6.5 (23) | 6.5 (23) | 0.0 | 17 to 17 | Structurally Inadequate |
<!-- /generated -->

Each column below reverses one owner decision and keeps the rest; the last reverses all of them, so every cell stands at
its reading. A raise (58.1, 79.1 to 79.4) reverses to the 0.5 it replaced. D66 and D67 applied the readings, so reversing
either restores the 1.0 it replaced (79.4's raise for Degrowth and Participatory Economics; D65's hold under 69.4 for
CCO-PTF-PTH-SZH-CIP); on the readings alone their cells stay at 0.5. The ten entries highest now are shown; the others are
unaffected.

<!-- generated:withwithout -->
| Entry | Session 84 | without 58.1 (C3.2) | without 79.1 (C1.2a) | without 79.2 (C2.5) | without 79.3 (C3.4) | without 79.4 (C3.4 for Integral and Ostrom) | without D66 (C3.4 for Degrowth and PE) | without D67 (C2.2 and C5.3) | on the readings alone (no owner decision) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| CCO-PTF-PTH-SZH-CIP | 16.5 (1) | 16.0 (1) | 16.0 (1) | 16.0 (1) | 16.0 (1) | 16.5 (1) | 16.5 (1) | 17.5 (1) | 14.5 (5) |
| Nordic Social Democracy | 15.5 (2) | 15.5 (2) | 15.5 (2) | 15.5 (2) | 15.5 (2) | 15.5 (2) | 15.5 (3) | 15.5 (2) | 15.5 (1) |
| Market Socialism | 15.5 (2) | 15.5 (2) | 15.5 (2) | 15.5 (2) | 15.5 (2) | 15.5 (2) | 15.5 (3) | 15.5 (2) | 15.5 (1) |
| Participatory Economics | 15.5 (2) | 15.5 (2) | 15.5 (2) | 15.5 (2) | 15.5 (2) | 15.5 (2) | 16.0 (2) | 15.5 (2) | 15.5 (1) |
| Integral | 15.0 (5) | 15.0 (5) | 15.0 (5) | 15.0 (5) | 15.0 (5) | 14.5 (6) | 15.0 (5) | 15.0 (5) | 14.5 (5) |
| Sovereign Wealth Fund Statism | 15.0 (5) | 15.0 (5) | 15.0 (5) | 15.0 (5) | 15.0 (5) | 15.0 (5) | 15.0 (5) | 15.0 (5) | 15.0 (4) |
| Ostrom-Style Commons Governance | 15.0 (5) | 15.0 (5) | 15.0 (5) | 15.0 (5) | 15.0 (5) | 14.5 (6) | 15.0 (5) | 15.0 (5) | 14.5 (5) |
| Universal Basic Income | 14.0 (8) | 14.0 (8) | 14.0 (8) | 14.0 (8) | 14.0 (8) | 14.0 (8) | 14.0 (9) | 14.0 (8) | 14.0 (8) |
| Degrowth Economics | 14.0 (8) | 14.0 (8) | 14.0 (8) | 14.0 (8) | 14.0 (8) | 14.0 (8) | 14.5 (8) | 14.0 (8) | 14.0 (8) |
| Georgism / Land Value Tax (LVT + Citizen's Dividend) | 14.0 (8) | 14.0 (8) | 14.0 (8) | 14.0 (8) | 14.0 (8) | 14.0 (8) | 14.0 (9) | 14.0 (8) | 14.0 (8) |
<!-- /generated -->

The weighting robustness rerun (`weighting_s83.py`, now four states): on the scores as decided, CCO-PTF-PTH-SZH-CIP is
first under all four schemes and under every single-criterion drop. If all its close calls resolved down and the best of
the three entries at 15.5 resolved all of its up, that entry (Nordic Social Democracy, 17.5) would be first. On the
readings alone first place is shared by Market Socialism, Nordic Social Democracy and Participatory Economics on equal
weights, and moves with the scheme (Nordic Social Democracy alone when Domain 1 is doubled; Market Socialism and
Participatory Economics when Domain 5 is halved).

## 6. Ledger I12, items 2 and 3 (decision 84.6)

Not readings this session changes. They go to the limits page (ledger S44) as stated in `NEEC_Adjudication_s83.md`,
section 9: C2.2's means-tested floors (read as no baseline for Status Quo, China, Singapore and Qatar, while the 0.5 band's
"conditional" could read them at 0.5; a class question held for consistency), and C2.1's clause 1 measure (Gallup's latest
year or the World Happiness Report's three-year average; the measurement field is silent).

## 7. Decisions

- **84.1** (owner, recorded; ledger D66): Degrowth's and Participatory Economics' C3.4 to 0.5, as the adjudication reads them.
- **84.2** (owner, recorded; ledger D67, superseding D65's hold under 69.4): CCO-PTF-PTH-SZH-CIP's C2.2 and C5.3 to 0.5.
- **84.3** (correction to the record): CCO-PTF-PTH-SZH-CIP C3.4's clauses 1 and 3 re-read on cited sources; both clear; the
  verdict holds.
- **84.4** (correction under the delegation, decision 57.2; ledger I12 item 1): Participatory Economics' C1.2b 1.0 to 0.5 by
  rule 4 of decision 83.4.
- **84.5** (owner, recorded; ledger D68): the entry is shown as CCO-PTF-PTH-SZH-CIP through one display-name mapping
  (`display_names.py`) in the generators of the current state (corpus, CSV, blocks, evidence reports, site and its visual
  suite); its key (`CCO-PTF-CIP-SZH`) and code (`CCO`) are identifiers and do not change; records before Session 84 keep the
  old name. Quotations of published documents (the v1 rationales in the evidence reports) keep their words.
- **84.6** (record): ledger I12 items 2 and 3 go to the limits page (S44).
- **84.7** (owner, recorded; ledger D69 and its note): v2.0 lands with 23 entries; OEIAS (S70) joins in v2.1 as the 24th, and
  the system Claude may design (S71) as the 25th, released with it.
- **84.8** (optional, tooling): `owner_s84.py`, `final_pass.settled_state()` with its self-test, `apply_owner_s84.py` with
  `--check` and a negative control, the Session 83 snapshots, `weighting_s83.py`'s four states and its handling of a
  shared first place, harness v53.
- **84.9** (method, optional): Report v2.0 Part I (`NEEC_Report_v2_0_Part_I.md`) is ordered by domain, criterion and entry. Its
  scorecards are generated by `build_report_v2.py` from the units' readings and, for cells no unit read, the published
  rationales (decision 52.8), and checked by the harness; the prose between them is written by hand.
- **84.10** (record; ledger I13): three of Nordic Social Democracy's stored readings (C4.3, C4.4 and C5.4) carry unfilled
  template fields ("{LAST}", "{RATIO}", "{SPEND}" and others) from `rescoring_s48.py` to `rescoring_s50.py`, which fill
  them only in their own records. The statuses and scores are unaffected; the fields are filled by generator before the
  landing (S43), and `evidence/` and the Report's scorecards regenerated.

## 8. What this record does not do, and disclosure

It changes no reading other than the six units above, and no criterion. The scores freeze here (decision 83.13, now at the
`s84` tag) except through the push-back route. CCO-PTF-PTH-SZH-CIP was designed by the owner, who co-authors NEEC; decisions
84.1, 84.2 and 84.5 are the owner's, and two of them lower the owner's own entry. Claude (Anthropic) made the readings of
84.3 and 84.4 in this session.
