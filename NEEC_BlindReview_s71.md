# NEEC Blind Review, Session 71: C4.5 and C3.4

**Session 71 · 2026-10-18 · Stage 3b, the blind re-read (ledger S54; decisions 69.1, 69.2; ledger D52, D53) ·
Scorer: Claude (Opus 5.5) · Owner: Duke Johnson**

Script: `blind_s71.py` (checked by the harness, which compares its output with `blind_s71_output.txt` and confirms
that this record carries every table it generates). Evidence: `evidence_cache_s71.py` (nine files, by digest), with
`evidence_cache/C4.5/sources_s71.md` and `evidence_cache/C3.4/sources_s71.md` naming the sources not cached. Nothing
here changes a published score: the final readings are applied by generator in ledger step S61 (STATE.md, "Next
work").

## 1. Summary

The 24 units Session 65 read on Sonnet 5.5 for the two criteria that decide first place, C4.5 Exploitation
Elimination (17 units) and C3.4 Epistemic Adaptability (7 units), were re-read on Opus 5.5, blind to the earlier
reading, then compared with it.

- **Blind against prior:** 1 agree, 23 revise. Most revisions are clause statuses only: part (2.11) left C4.5's
  clause 2 not estimated for 16 of 17 units ("no exit-rights evidence is stated beyond the published rationale"),
  which this group reads, mostly as short. Eight blind verdicts differ from the prior's.
- **Reconciliation (protocol 5.3):** five of the eight blind verdicts stand; three (China, Doughnut Economics and
  Sovereign Wealth Fund Statism on C4.5) return to the prior's 0.0, because the blind reading departed from its own
  stated reading or did not weigh evidence the prior cites (section 6). Each keeps the blind reading's 0.5 as a flag.
- **Final against prior:** 2 agree, 22 revise; **five verdicts change**: Participatory Economics C4.5 0.5 to 1.0;
  Stakeholder Capitalism C4.5 0.5 to 0.0; Singapore C4.5 0.0 to 0.5; Fully Automated Luxury Communism C3.4 0.5 to
  0.0; Libertarian Minarchism C3.4 0.0 to 0.5. No CCO-PTF-CIP-SZH verdict changes (its C4.5 unit gains a clause-2
  status only).
- **Consequence, once applied (S61):** **Participatory Economics alone first at 16.5 on the 29 criteria (15.0 on the
  26)**, ahead of CCO-PTF-CIP-SZH at 16.0 (14.5); the flag on its C4.5 (toward 0.5) is the one call that would restore
  the shared first place. No tier changes. The two flags STATE.md named as contested resolve as follows: Participatory
  Economics' C4.5 flag toward 0.0 lapses (it rested on the residual-coercion reading v2.0 deleted) and the unit rises;
  Integral's C3.4 holds at 0.5, flagged toward 1.0 as before, on clause 4 only.

## 2. The blind step

The readings were written from `blind_review.blind_view()` (the v2.0 clause text and the cache file names), the
sources below, and the peers' readings, and committed and pushed as checkpoint `8b6428c` ("NEEC checkpoint s71: blind
readings of C4.5 and C3.4 recorded, before the prior readings are opened") before part (2.11)'s readings of these
units, or their published (v1) scores and rationales on these two criteria, were opened. `blind_s71.py` at that
commit holds them exactly; the comparison and the reconciliation were added after it, and the blind readings
themselves were not edited after it.

What the session had seen before recording, disclosed so a reader can weigh the blindness:

- **criteria.json's anchors** for both criteria, which quote published examples: on C4.5, Participatory Economics
  (published 0.0, by the anchor's own correction note), Nordic Social Democracy 0.5, Status Quo 0.0, Degrowth 1.0;
  on C3.4, Market Socialism 1.0, Status Quo 0.5, Centrally Planned Socialism 0.0, Libertarian Minarchism 0.0.
- **STATE.md's summary** of two of the prior's moves: Participatory Economics' C4.5 0.0 to 0.5 (flagged toward 0.0)
  and Integral's C3.4 1.0 to 0.5 (flagged toward 1.0), and the provisional standings.
- **The peers' readings** on these criteria in the parts read on Opus: C4.5 in parts (a) and (b8) (Centrally Planned
  Socialism, Libertarian Minarchism, Universal Basic Income, Degrowth, FALC, Integral); C3.4 in parts (a), (b1) and
  (2.5) (the other 16 entries). These are calibration (protocol 5), not the prior reading of the 24 units.
- **Other criteria's published rationales** used as evidence about a design (FALC's C2.2, C2.4, C2.5, C3.1, C3.3,
  C3.5, C4.4, C5.1, C5.2; Georgism's C1.4, C2.2, C2.5), and the overviews of the Report and the scoring documents.

## 3. Sources

Cached by `evidence_cache_s71.py` (each verified by md5): Penn World Table 10.01's labour share (labsh) for the eight
economies the configured entries cover; the US national-income components (BEA through FRED: compensation, corporate
profits, rental income of persons, net interest, proprietors' income, GDP), 2000 to 2025; the World Bank's
natural-resource rents (% of GDP); the UN SDG database's labour share of GDP (10.4.1), which carries Denmark, Finland
and Sweden; Sweden's unemployment-insurance law, 43 b; Hahnel and Wright, *Alternatives to Capitalism* (2016), three
passages; the Research Hub at its pin `8e8a6ba`, passages of five pages; Integral's *Technical White Paper v0.1*, six
passages; CPI-U and the federal funds rate, monthly, 2019 to 2023. Named, not cached: Census P60-291, the Department
of Labor's comparison of state unemployment-insurance laws, MOHRSS's 2024 bulletin, SingStat's dwelling table, MOM's
transfer rules, Qatar's 2020 laws and the ILO's 2022 figures, Bebchuk and Tallarita (2020), the FDIC's and the FCIC's
accounts of the US banking crises, Xiao and others (2023), and the histories cited for the planned economy.

Figures the readings quote, recomputed by the script from the cache: one minus the labour share of GDP in 2019 is
40.3% (United States), 41.4% (China), 56.1% (Singapore), 82.4% (Qatar; 60.0% net of resource rents of 22.4%), 38.0%
(Denmark), 42.9% (Finland), 47.1% (Norway; 40.9% net of resource rents), 44.3% (Sweden). The US narrow count,
corporate profits plus rental income plus net interest, is 18.7% of GDP in 2025 (13.0%, 3.7% and 2.0%), up from 14.8%
in 2000. US CPI-U inflation first exceeded 4% in April 2021 (4.1%); the first rise in the federal funds rate came in
March 2022, 11 months later.

## 4. Readings

**C4.5 Exploitation Elimination** (class D: v2.0 deleted the residual-coercion clause; clauses: extraction rates below
10% of GDP; genuine exit rights from exploitative relationships).

- **4.5.1 Clause 1.** Extraction is the transfer to owners of capital, landlords and lenders as a share of GDP, the
  three relationships the measurement names. A configured economy is read on the broad count, one minus the labour
  share (the criterion's own rationale counts the capital share: "42% of GDP extracted from labor to capital"), and,
  for the United States, on the narrow count (corporate profits, rental income and net interest); a design or
  mechanism on its own sources, by the flows it removes and those it leaves. State appropriation is extraction
  relocated, not removed (parts (a) and (b8) on the planned economy). Public capture of land rent removes the
  landlord's share of that flow, as Georgism's tax does.
- **4.5.2 Clause 2.** Shown when a person can leave an employment, tenancy or credit relationship without losing
  subsistence, through an unconditional floor or an assured alternative that is not itself extractive, for each such
  relationship the system keeps (part (b8)'s readings 3.6: FALC and Integral cleared, Degrowth not shown). The formal
  right to quit one employer for another is the minimum, not genuine exit. Short: a partial floor or alternative, or
  one for some relationship types or part of the population.
- **4.5.3 The 0.0 line** (protocol 2.1; decision 53.2): far below on both clauses, every relationship type in place and
  exit no more than the formal right to quit, with no rule or instrument in the system that removes one. A structural
  mechanism removing one relationship type for a large part of the population, or a substantial if conditional floor,
  is 0.5 (the 0.5 band: "elimination in one relationship type while another persists"; protocol 2.1: a mechanism
  that "covers only part of the relevant population").
- **4.5.4 Mechanisms** are scored generalised (protocol 3.2): a flow the mechanism removes is credited; the flows it
  does not govern stay the host economy's, so clause 1 is short unless it governs all three.

**C3.4 Epistemic Adaptability** (class M: v2.0 replaced "democratic governance for changes" with contestability;
clauses: at least 30% parameter adjustability; policy updates within six months of evidence; changes open to challenge
and reversal by those affected; zero collapses during parameter adjustments).

- **3.4.1** A core parameter moved by at least 30% of its value without redesign (part (a), Sovereign Wealth Fund
  Statism; part (b1), Market Socialism).
- **3.4.2** An update timed against the evidence that called for it (part (b1), MMT + Job Guarantee and Universal
  Basic Income); for a design, a stated rule of review within six months (part (b1), CCO-PTF-CIP-SZH's crisis
  protocol).
- **3.4.3** Those affected can challenge a change and have it reversed through a process independent of the officials
  who made it: independent courts, free elections, or, in a design with no officials, a participatory process any
  participant can open. The clause requires no particular governance form.
- **3.4.4** A systemic crisis caused by changes to the configuration's own parameters is a collapse (part (b1), Nordic
  Social Democracy); a design with no implementation and no modelling of its parameter adjustments does not show the
  clause (part (b1), reading 3.1).
- **3.4.5** 0.0 only on a stated whole-criterion reason under protocol 2.1, never with a clause cleared (decision 53.2;
  `pass_common.check_rule`).

## 5. The blind readings, and the comparison

The blind readings as recorded at the checkpoint (each unit's clause estimates and sources are in `blind_s71.py`):

| Unit | Criterion | Clause statuses | Verdict | Flag |
|---|---|---|---|---|
| CCO-PTF-CIP-SZH | C4.5 | S S | 0.5 | — |
| Doughnut Economics | C4.5 | U U | 0.5 | toward 0.0 |
| Georgism / Land Value Tax (LVT + Citizen's Dividend) | C4.5 | S S | 0.5 | — |
| Islamic Finance / Profit-Sharing Banking | C4.5 | S S | 0.5 | toward 0.0 |
| MMT + Job Guarantee | C4.5 | S S | 0.5 | — |
| Market Socialism | C4.5 | U S | 0.5 | — |
| Mutual Credit / LETS | C4.5 | S S | 0.5 | — |
| Nordic Social Democracy | C4.5 | S S | 0.5 | — |
| Ostrom-Style Commons Governance | C4.5 | S S | 0.5 | — |
| Participatory Economics | C4.5 | C C | 1.0 | toward 0.5 |
| Sovereign Wealth Fund Statism | C4.5 | S S | 0.5 | toward 0.0 |
| Stakeholder Capitalism | C4.5 | S S | 0.0 (0.0 reason stated) | toward 0.5 |
| State Capitalism / China (Party-State-Directed Market Economy) | C4.5 | S S | 0.5 | toward 0.0 |
| State Capitalism / Qatar (Gulf Rentier-Distributive Statism) | C4.5 | S S | 0.0 (0.0 reason stated) | toward 0.5 |
| State Capitalism / Singapore (GLC Developmental Capitalism) | C4.5 | S S | 0.5 | toward 0.0 |
| Status Quo Market Capitalism | C4.5 | S S | 0.0 (0.0 reason stated) | toward 0.5 |
| Universal Basic Services | C4.5 | S S | 0.5 | — |
| Centrally Planned Socialism | C3.4 | S S S S | 0.0 (0.0 reason stated) | toward 0.5 |
| Fully Automated Luxury Communism | C3.4 | U U U U | 0.0 (0.0 reason stated) | toward 0.5 |
| Integral | C3.4 | C C C U | 0.5 | toward 1.0 |
| Libertarian Minarchism | C3.4 | S S C U | 0.5 | toward 0.0 |
| State Capitalism / China (Party-State-Directed Market Economy) | C3.4 | C S S S | 0.5 | — |
| State Capitalism / Qatar (Gulf Rentier-Distributive Statism) | C3.4 | C S S C | 0.5 | — |
| Status Quo Market Capitalism | C3.4 | C S C S | 0.5 | — |

The comparison with part (2.11), blind (`blind_review.compare_group`: agree only if every clause status and the
verdict match):

| Unit | Criterion | Prior (Session 65) | Blind (Session 71) | Result | Differences |
|---|---|---|---|---|---|
| CCO-PTF-CIP-SZH | C4.5 | S U / 0.5 | S S / 0.5 | revise (clauses) | clause 2: U (prior) vs S (new) |
| Doughnut Economics | C4.5 | U U / 0.0 | U U / 0.5 | revise (verdict) | verdict: 0.0 (prior) vs 0.5 (new) |
| Georgism / Land Value Tax (LVT + Citizen's Dividend) | C4.5 | S U / 0.5 | S S / 0.5 | revise (clauses) | clause 2: U (prior) vs S (new) |
| Islamic Finance / Profit-Sharing Banking | C4.5 | U U / 0.5 | S S / 0.5 | revise (clauses) | clause 1: U (prior) vs S (new); clause 2: U (prior) vs S (new) |
| MMT + Job Guarantee | C4.5 | S U / 0.5 | S S / 0.5 | revise (clauses) | clause 2: U (prior) vs S (new) |
| Market Socialism | C4.5 | S U / 0.5 | U S / 0.5 | revise (clauses) | clause 1: S (prior) vs U (new); clause 2: U (prior) vs S (new) |
| Mutual Credit / LETS | C4.5 | S U / 0.5 | S S / 0.5 | revise (clauses) | clause 2: U (prior) vs S (new) |
| Nordic Social Democracy | C4.5 | S U / 0.5 | S S / 0.5 | revise (clauses) | clause 2: U (prior) vs S (new) |
| Ostrom-Style Commons Governance | C4.5 | U U / 0.5 | S S / 0.5 | revise (clauses) | clause 1: U (prior) vs S (new); clause 2: U (prior) vs S (new) |
| Participatory Economics | C4.5 | C U / 0.5 | C C / 1.0 | revise (verdict) | clause 2: U (prior) vs C (new); verdict: 0.5 (prior) vs 1.0 (new) |
| Sovereign Wealth Fund Statism | C4.5 | U U / 0.0 | S S / 0.5 | revise (verdict) | clause 1: U (prior) vs S (new); clause 2: U (prior) vs S (new); verdict: 0.0 (prior) vs 0.5 (new) |
| Stakeholder Capitalism | C4.5 | S U / 0.5 | S S / 0.0 | revise (verdict) | clause 2: U (prior) vs S (new); verdict: 0.5 (prior) vs 0.0 (new) |
| State Capitalism / China (Party-State-Directed Market Economy) | C4.5 | S U / 0.0 | S S / 0.5 | revise (verdict) | clause 2: U (prior) vs S (new); verdict: 0.0 (prior) vs 0.5 (new) |
| State Capitalism / Qatar (Gulf Rentier-Distributive Statism) | C4.5 | S U / 0.0 | S S / 0.0 | revise (clauses) | clause 2: U (prior) vs S (new) |
| State Capitalism / Singapore (GLC Developmental Capitalism) | C4.5 | S U / 0.0 | S S / 0.5 | revise (verdict) | clause 2: U (prior) vs S (new); verdict: 0.0 (prior) vs 0.5 (new) |
| Status Quo Market Capitalism | C4.5 | S U / 0.0 | S S / 0.0 | revise (clauses) | clause 2: U (prior) vs S (new) |
| Universal Basic Services | C4.5 | S U / 0.5 | S S / 0.5 | revise (clauses) | clause 2: U (prior) vs S (new) |
| Centrally Planned Socialism | C3.4 | S S S S / 0.0 | S S S S / 0.0 | agree | — |
| Fully Automated Luxury Communism | C3.4 | U U U U / 0.5 | U U U U / 0.0 | revise (verdict) | verdict: 0.5 (prior) vs 0.0 (new) |
| Integral | C3.4 | U U C U / 0.5 | C C C U / 0.5 | revise (clauses) | clause 1: U (prior) vs C (new); clause 2: U (prior) vs C (new) |
| Libertarian Minarchism | C3.4 | U S U U / 0.0 | S S C U / 0.5 | revise (verdict) | clause 1: U (prior) vs S (new); clause 3: U (prior) vs C (new); verdict: 0.0 (prior) vs 0.5 (new) |
| State Capitalism / China (Party-State-Directed Market Economy) | C3.4 | U C S U / 0.5 | C S S S / 0.5 | revise (clauses) | clause 1: U (prior) vs C (new); clause 2: C (prior) vs S (new); clause 4: U (prior) vs S (new) |
| State Capitalism / Qatar (Gulf Rentier-Distributive Statism) | C3.4 | U C S U / 0.5 | C S S C / 0.5 | revise (clauses) | clause 1: U (prior) vs C (new); clause 2: C (prior) vs S (new); clause 4: U (prior) vs C (new) |
| Status Quo Market Capitalism | C3.4 | U C C S / 0.5 | C S C S / 0.5 | revise (clauses) | clause 1: U (prior) vs C (new); clause 2: C (prior) vs S (new) |

## 6. Reconciliation of the eight verdict differences

A blind verdict stands unless the prior reading shows evidence the blind reading did not weigh, or the blind reading
departs from its own stated reading (section 4). The reconciliation moves a verdict only toward the prior's, and says
why; where it does, the blind verdict is kept as the flag.

**Standing (five):**

- **Participatory Economics, C4.5: 1.0 (blind), prior 0.5; stands.** Clause 1 is cleared on both readings: the design
  keeps no owners of productive assets, so no profit, rent or interest income accrues to them. On clause 2 the prior
  found exit "not shown" because "the design requires comprehensive participation", reading only the published
  rationale. The design's own literature provides what clause 2 asks: besides the effort-rated budget, allowances for
  those excused from production and "a consumption allowance for people who simply don't want to work (this is, in
  effect, an unconditional basic income, presumably set at a level to fully meet basic needs)" (Wright's statement of
  the procedure in Hahnel and Wright, 2016, which Hahnel's reply keeps as "effort rating plus any allowance"), with no
  employer, landlord or creditor; as part (b8) cleared the clause for Integral and FALC on subsistence not depending
  on any relationship. Flagged toward 0.5 on Wright's "presumably": the allowance's level is set in the plan, not
  fixed by the design. The prior's flag toward 0.0 rested on the published "different form of exploitation"
  (coordination burdens, informal hierarchy), the residual-coercion reading v2.0 moved to C2.1; it lapses.
- **Stakeholder Capitalism, C4.5: 0.0 (blind), prior 0.5 (published 0.5); stands, a correction.** The published 0.5
  credited "better wages and conditions in some stakeholder firms" while finding "capital-labor exploitation ...
  structurally unchanged"; better terms are what the requirement excludes ("remove extractive relationships, not
  merely regulate them"), and the entry is voluntary corporate responsibility within the market framework, so on
  reading 4.5.3 it fails as Status Quo does (both readings agree Status Quo is 0.0). Class D's "keep or raise"
  describes what deleting a clause can do; a fall on the remaining clauses is a correction of the published reading,
  stated here. Flagged toward 0.5.
- **Singapore, C4.5: 0.5 (blind), prior 0.0 (published 0.0); stands.** The published reading's evidence of a
  debt-financed, employer-tied workforce of 1.22 million Work Permit holders without independent bargaining is not in
  dispute, and is why clause 2 is short and the unit flagged toward 0.0. But HDB removes the private landlord for
  77.2% of resident households, a structural mechanism on one relationship type covering a large part of the
  population (reading 4.5.3; protocol 2.1's "covers only part of the relevant population"); the published reading did
  not weigh it, and itself noted the score would be 0.5 on a residents-only scope. The blind reading's "about a
  quarter of the workforce" for Work Permit holders is low if domestic workers are counted (1.22 million with 316,900
  domestic workers, in the published reading); the verdict does not turn on it.
- **Fully Automated Luxury Communism, C3.4: 0.0 (blind), prior 0.5 (published 0.5); stands, a correction.** The
  published 0.5 rested on "AI/automation could enable rapid evidence-based optimization", a capability claim with no
  procedure; the prior marked every clause not shown. With no procedure for adjusting the design's rules or
  parameters, and its governance recorded as unspecified in its own scoring (C2.4, C4.4), protocol 2.1's first
  condition holds. Flagged toward 0.5 (the programme enacted through the democratic institutions it assumes).
- **Libertarian Minarchism, C3.4: 0.5 (blind), prior 0.0 (published 0.0); stands, a correction.** The prior held
  0.0 on the second condition of protocol 2.1 and read clause 3 as "not part of the design". v2.0's clause 3 asks
  for contestability in whatever governance form, and the minimal state's core function is independent courts under
  a constitution of limited powers, as the United States' clause 3 is cleared on its courts; with a clause cleared,
  0.0 cannot hold (decision 53.2). Flagged toward 0.0 on the second condition.

**Reconciled to the prior's verdict (three):**

- **China, C4.5: 0.5 (blind), final 0.0.** The blind reading credited public and collective land ownership with capturing the land rent, as a land value tax does; on reconciliation that holds only for the lease premium paid at sale, since the 70-year use right leaves the later rise in land value with private holders, landlords included; and the published reading cites state-organised forced labour (US Department of Labor, 2022), which the blind reading did not weigh. With the mechanism it credited much weaker and both clauses far short, reading 4.5.3 gives 0.0.
- **Doughnut Economics, C4.5: 0.5 (blind), final 0.0.** The blind reading's 0.5 rested on the framework addressing extraction 'in principle, by name, without a mechanism of its own', but reading 4.5.3, stated before it, gives 0.5 only for a structural mechanism; and the published reading's implementation record (over 50 jurisdictions, an overlay modifying none of the three relationships) is evidence, under D29(a), that the blind reading did not weigh. The blind reading's own flag, toward 0.0, is the reading that stands.
- **Sovereign Wealth Fund Statism, C4.5: 0.5 (blind), final 0.0.** The blind reading's clause 1 estimate found the relationships 'in the economy it is layered onto and in the firms it owns' unmodified, and reading 4.5.3 gives 0.5 only where a relationship type is removed or a substantial floor provided; the 0.5 departed from that reading, and its flag, toward 0.0, which the published reading also states, is the reading that stands. Unlike the planned economy (parts (a) and (b8), 0.5), the mechanism does not end private capital's employment of labour.

The final readings against the prior (what ledger S61 applies):

| Unit | Criterion | Prior (Session 65) | Final (Session 71) | Result | Differences |
|---|---|---|---|---|---|
| CCO-PTF-CIP-SZH | C4.5 | S U / 0.5 | S S / 0.5 | revise (clauses) | clause 2: U (prior) vs S (new) |
| Doughnut Economics | C4.5 | U U / 0.0 | U U / 0.0 | agree | — |
| Georgism / Land Value Tax (LVT + Citizen's Dividend) | C4.5 | S U / 0.5 | S S / 0.5 | revise (clauses) | clause 2: U (prior) vs S (new) |
| Islamic Finance / Profit-Sharing Banking | C4.5 | U U / 0.5 | S S / 0.5 | revise (clauses) | clause 1: U (prior) vs S (new); clause 2: U (prior) vs S (new) |
| MMT + Job Guarantee | C4.5 | S U / 0.5 | S S / 0.5 | revise (clauses) | clause 2: U (prior) vs S (new) |
| Market Socialism | C4.5 | S U / 0.5 | U S / 0.5 | revise (clauses) | clause 1: S (prior) vs U (new); clause 2: U (prior) vs S (new) |
| Mutual Credit / LETS | C4.5 | S U / 0.5 | S S / 0.5 | revise (clauses) | clause 2: U (prior) vs S (new) |
| Nordic Social Democracy | C4.5 | S U / 0.5 | S S / 0.5 | revise (clauses) | clause 2: U (prior) vs S (new) |
| Ostrom-Style Commons Governance | C4.5 | U U / 0.5 | S S / 0.5 | revise (clauses) | clause 1: U (prior) vs S (new); clause 2: U (prior) vs S (new) |
| Participatory Economics | C4.5 | C U / 0.5 | C C / 1.0 | revise (verdict) | clause 2: U (prior) vs C (new); verdict: 0.5 (prior) vs 1.0 (new) |
| Sovereign Wealth Fund Statism | C4.5 | U U / 0.0 | S S / 0.0 | revise (clauses) | clause 1: U (prior) vs S (new); clause 2: U (prior) vs S (new) |
| Stakeholder Capitalism | C4.5 | S U / 0.5 | S S / 0.0 | revise (verdict) | clause 2: U (prior) vs S (new); verdict: 0.5 (prior) vs 0.0 (new) |
| State Capitalism / China (Party-State-Directed Market Economy) | C4.5 | S U / 0.0 | S S / 0.0 | revise (clauses) | clause 2: U (prior) vs S (new) |
| State Capitalism / Qatar (Gulf Rentier-Distributive Statism) | C4.5 | S U / 0.0 | S S / 0.0 | revise (clauses) | clause 2: U (prior) vs S (new) |
| State Capitalism / Singapore (GLC Developmental Capitalism) | C4.5 | S U / 0.0 | S S / 0.5 | revise (verdict) | clause 2: U (prior) vs S (new); verdict: 0.0 (prior) vs 0.5 (new) |
| Status Quo Market Capitalism | C4.5 | S U / 0.0 | S S / 0.0 | revise (clauses) | clause 2: U (prior) vs S (new) |
| Universal Basic Services | C4.5 | S U / 0.5 | S S / 0.5 | revise (clauses) | clause 2: U (prior) vs S (new) |
| Centrally Planned Socialism | C3.4 | S S S S / 0.0 | S S S S / 0.0 | agree | — |
| Fully Automated Luxury Communism | C3.4 | U U U U / 0.5 | U U U U / 0.0 | revise (verdict) | verdict: 0.5 (prior) vs 0.0 (new) |
| Integral | C3.4 | U U C U / 0.5 | C C C U / 0.5 | revise (clauses) | clause 1: U (prior) vs C (new); clause 2: U (prior) vs C (new) |
| Libertarian Minarchism | C3.4 | U S U U / 0.0 | S S C U / 0.5 | revise (verdict) | clause 1: U (prior) vs S (new); clause 3: U (prior) vs C (new); verdict: 0.0 (prior) vs 0.5 (new) |
| State Capitalism / China (Party-State-Directed Market Economy) | C3.4 | U C S U / 0.5 | C S S S / 0.5 | revise (clauses) | clause 1: U (prior) vs C (new); clause 2: C (prior) vs S (new); clause 4: U (prior) vs S (new) |
| State Capitalism / Qatar (Gulf Rentier-Distributive Statism) | C3.4 | U C S U / 0.5 | C S S C / 0.5 | revise (clauses) | clause 1: U (prior) vs C (new); clause 2: C (prior) vs S (new); clause 4: U (prior) vs C (new) |
| Status Quo Market Capitalism | C3.4 | U C C S / 0.5 | C S C S / 0.5 | revise (clauses) | clause 1: U (prior) vs C (new); clause 2: C (prior) vs S (new) |

## 7. Consequences once applied (not applied here)

| Entry | Total on 29 | After | Total on 26 | After | Failures | After | Tier after |
|---|---:|---:|---:|---:|---:|---:|---|
| Libertarian Minarchism | 8.5 | 9.0 | 7.0 | 7.5 | 13 | 12 | Structurally Inadequate |
| Stakeholder Capitalism | 10.5 | 10.0 | 9.0 | 8.5 | 8 | 9 | Structurally Inadequate |
| Fully Automated Luxury Communism | 10.5 | 10.0 | 9.0 | 8.5 | 10 | 11 | Structurally Inadequate |
| Participatory Economics | 16.0 | 16.5 | 14.5 | 15.0 | 0 | 0 | Potentially Adequate |
| State Capitalism / Singapore (GLC Developmental Capitalism) | 13.0 | 13.5 | 11.5 | 12.0 | 4 | 3 | Partially Adequate |

First place on the 29 criteria: Participatory Economics alone at 16.5 (on the 26: 15.0, CCO-PTF-CIP-SZH 14.5).
Integral 15.5, Nordic Social Democracy 15.0 unchanged. No tier changes: Singapore goes from 4 failures to 3 and
stays Partially Adequate; Stakeholder Capitalism (9), FALC (11) and Libertarian Minarchism (12) stay Structurally
Inadequate.

The final readings carry 13 flags. Taken alone (on top of the other final verdicts), three would change a tier
or first place: Participatory Economics' C4.5 toward 0.5 (first place shared again with CCO-PTF-CIP-SZH at 16.0);
Sovereign Wealth Fund Statism's C4.5 toward 0.5 (3 failures to 2: Partially to Potentially Adequate), the blind
reading's own verdict; and Islamic Finance's C4.5 toward 0.0 (5 failures to 6: Partially to Structurally
Inadequate). The last two are new: part (2.11) flagged neither unit.

| Unit | Criterion | Final | Flag toward | Total on 29 then | Failures then | Tier then | Changes |
|---|---|---:|---:|---:|---:|---|---|
| Doughnut Economics | C4.5 | 0.0 | 0.5 | 11.0 | 7 | Structurally Inadequate | — |
| Islamic Finance / Profit-Sharing Banking | C4.5 | 0.5 | 0.0 | 12.5 | 6 | Structurally Inadequate | tier: Partially Adequate to Structurally Inadequate |
| Participatory Economics | C4.5 | 1.0 | 0.5 | 16.0 | 0 | Potentially Adequate | first place: shared |
| Sovereign Wealth Fund Statism | C4.5 | 0.0 | 0.5 | 15.0 | 2 | Potentially Adequate | tier: Partially Adequate to Potentially Adequate |
| Stakeholder Capitalism | C4.5 | 0.0 | 0.5 | 10.5 | 8 | Structurally Inadequate | — |
| State Capitalism / China (Party-State-Directed Market Economy) | C4.5 | 0.0 | 0.5 | 11.0 | 8 | Structurally Inadequate | — |
| State Capitalism / Qatar (Gulf Rentier-Distributive Statism) | C4.5 | 0.0 | 0.5 | 11.0 | 8 | Structurally Inadequate | — |
| State Capitalism / Singapore (GLC Developmental Capitalism) | C4.5 | 0.5 | 0.0 | 13.0 | 4 | Partially Adequate | — |
| Status Quo Market Capitalism | C4.5 | 0.0 | 0.5 | 12.5 | 6 | Structurally Inadequate | — |
| Centrally Planned Socialism | C3.4 | 0.0 | 0.5 | 8.0 | 14 | Structurally Inadequate | — |
| Fully Automated Luxury Communism | C3.4 | 0.0 | 0.5 | 10.5 | 10 | Structurally Inadequate | — |
| Integral | C3.4 | 0.5 | 1.0 | 16.0 | 2 | Potentially Adequate | — |
| Libertarian Minarchism | C3.4 | 0.5 | 0.0 | 8.5 | 13 | Structurally Inadequate | — |

## 8. Decisions (Session 71)

All under the delegation (decision 57.2); none touches CCO-PTF-CIP-SZH's verdicts.

- **71.1** (optional, method) The readings of section 4 (4.5.1 to 4.5.4, 3.4.1 to 3.4.5), carried into the criteria
  record at its next amendment with the method choices STATE.md lists.
- **71.2** (correction) Participatory Economics' C4.5 0.5 to 1.0, flagged toward 0.5.
- **71.3** (correction) Stakeholder Capitalism's C4.5 0.5 to 0.0, flagged toward 0.5.
- **71.4** (correction) Singapore's C4.5 0.0 to 0.5, flagged toward 0.0.
- **71.5** (correction) FALC's C3.4 0.5 to 0.0, flagged toward 0.5.
- **71.6** (correction) Libertarian Minarchism's C3.4 0.0 to 0.5, flagged toward 0.0.
- **71.7** (procedural) The reconciliation rule of section 6; China's, Doughnut Economics' and Sovereign Wealth Fund
  Statism's C4.5 hold at 0.0, each flagged toward 0.5 (new flags).
- **71.8** (correction, no verdict effect) The 17 clause-status revisions of the final comparison: clause 2 of C4.5
  estimated where the prior left it not shown; on C3.4, clause 1 cleared for the three configured economies and
  Integral, clause 2 short for the three configured economies (an update timed against its evidence, not the
  rationale's assertion), cleared as designed for Integral; clause 4 short for China, cleared for Qatar.
- **71.9** (optional, tooling) `blind_s71.py` and `evidence_cache_s71.py`; harness v41, 118 checks.

## 9. Observations for later sessions

- **Peer consistency on C4.5.** Libertarian Minarchism and Centrally Planned Socialism stand at 0.5 on C4.5 (parts
  (a) and (b8), held under D28's rule that a clause-level gap never makes 0.0). On reading 4.5.3 Libertarian
  Minarchism (no mechanism limiting extraction; formal freedom of contract only) would be 0.0, as Status Quo, Stakeholder
  Capitalism and Qatar are; the planned economy's state appropriation and penalised exit raise the same question.
  Neither unit is in stage 3b's scope (both were read on Opus); a correction route is recorded in STATE.md for the
  owner (ledger I9).
- **C3.4's clause 3 for the 16 earlier-read units.** Parts (a) and (b1) read clause 3 as v1.4's "democratic
  governance for changes" (for example "governed, not democratic" for Islamic Finance, Singapore and Stakeholder
  Capitalism). v2.0's clause 3 is contestability in any form. No verdict appears to turn on it (each such unit has
  another clause short, and the two 1.0s, Market Socialism and Sovereign Wealth Fund Statism, clear contestability
  through general assemblies and courts), but the clause statuses are on the old wording (ledger I9).
- **Part (2.11)'s clause 2 on C4.5** was left not estimated for 16 of 17 units; the verdicts did not depend on it,
  but evidence reports built from it would show the clause as unread. Applying the final readings (S61) replaces it.
- **Evidence that will date:** the BEA components (revised annually), the SDG labour shares, the ILO's Qatar figures
  (2022, the latest located), MOHRSS's insured count (2024).

## 10. Model and disclosure

This group ran on Opus 5.5, the model the owner's routing names for it (STATE.md, "Model routing", and Handoff 70:
Opus 5.5 at xhigh, as the readings are contested; a session cannot see its own effort setting). It is the first group of stage 3b's blind re-read; the comparison is between an Opus reading and the
Sonnet reading of Session 65, as decisions 69.1 and 69.2 direct.
