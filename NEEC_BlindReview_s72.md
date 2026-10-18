# NEEC Blind Review, Session 72: C4.1

**Session 72 · 2026-10-18 · Stage 3b, the blind re-read (ledger S55; decisions 69.1, 69.2; ledger D52 to D54) ·
Scorer: Claude (Opus 5.5) · Owner: Duke Johnson**

Script: `blind_s72.py` (checked by the harness, which compares its output with `blind_s72_output.txt` and confirms
that this record carries every table it generates). Evidence: `evidence_cache_s72.py` (eight files, by digest) beside
Session 65's three (`evidence_cache_s65.py`), with `evidence_cache/C4.1/sources_s72.md` naming the sources not cached.
Nothing here changes a published score: the final readings are applied by generator in ledger step S61 (STATE.md,
"Next work").

## 1. Summary

The 23 C4.1 Intergenerational Justice units were re-read on Opus 5.5 on v2.0's two clauses ("Debt-to-GDP <80%",
"positive wealth transfer to next generation"), blind to the earlier readings, then compared with them: the 15 units
Session 65 read on Sonnet 5.5 (part (2.11)), and the 8 designs part (b6) read on the pre-v2.0 four-clause list
(decision 69.2, ledger D54).

- **Blind against prior:** 5 agree (the five configured economies read on national accounts), 18 revise. Eight of the
  revisions are the clause-count difference of part (b6)'s designs (four clauses against two), as decision 69.2
  expected; eight more are clause statuses only, mostly where the prior left a clause "not shown" for a mechanism
  that does not govern the quantity at all (out of reach, D28(c)) or where the unit's own sources state what the
  clause asks. **Two verdicts differ**: Libertarian Minarchism and Stakeholder Capitalism, 0.0 (prior) to 0.5.
- **Reconciliation (protocol 5.3, Session 71's rule):** both blind verdicts stand (section 6). The prior's 0.0 is kept
  as a flag on Libertarian Minarchism; Stakeholder Capitalism's blind reading already carries one.
- **Final against prior:** the same, 5 agree and 18 revise; **two verdicts change**: Libertarian Minarchism C4.1 0.0 to
  0.5 (flagged toward 0.0); Stakeholder Capitalism C4.1 0.0 to 0.5 (flagged toward 0.0). No CCO-PTF-CIP-SZH verdict
  changes (it holds at 0.5; only its clause list moves to v2.0's two).
- **Qatar's rise, looked at closely (STATE.md's one contested call):** the blind reading reaches 1.0 independently, as
  the prior did. The prior's flag toward 0.5 rested on net national saving not netting hydrocarbon depletion; the
  World Bank's adjusted net savings, which does, is 17.9% to 33.5% of GNI over 2012 to 2021, so that reason does not
  hold. The blind reading flags 1.0 toward 0.5 on a different ground: with no fiscal rule, debt rose from 24.9% of
  GDP in 2014 to 72.6% in 2020 as gas prices fell.
- **Consequence, once applied (S61):** two failures fewer, each in a Structurally Inadequate entry; no tier changes;
  first place is unchanged by this group (CCO-PTF-CIP-SZH and Participatory Economics shared at 16.0, or Participatory
  Economics alone at 16.5 with Session 71's changes, which the owner confirmed, ledger D55). No flag of this group
  would change a tier or first place.

## 2. The blind step

The readings were written from `blind_review.blind_view()` (the v2.0 clause text and the cache file names), the
sources below, and the units' scoring documents' overviews, and committed and pushed as checkpoint `4c8bc9f` ("NEEC
checkpoint s72: blind readings of C4.1 recorded, before the prior readings are opened") before part (2.11)'s or part
(b6)'s readings of these units were opened. `blind_s72.py` at that commit holds them exactly; the comparison, the
reconciliation and one flag (FLAGS, section 6) were added after it, and the blind readings themselves were not
edited after it.

What the session had seen before recording, disclosed so a reader can weigh the blindness:

- **criteria.json's anchors** for C4.1, which quote published (v1) examples: Degrowth Economics 1.0, Nordic Social
  Democracy 0.5, Status Quo Market Capitalism 0.0.
- **STATE.md's summary** of the prior's one contested move: Qatar's C4.1 0.5 to 1.0, flagged toward 0.5 (no reason
  given there).
- **Two published (v1) C4.1 lines, seen inadvertently** while listing the Report's and a scoring document's headings:
  Status Quo's Report line (0.0, the text the anchor already quotes) and the heading of Georgism's C4.1 section in its
  scoring document (0.5). Neither is part (2.11)'s reading; every later search of the scoring documents and the
  Report excluded C4.1's lines and sections.
- **Other criteria's readings and records:** Session 64's record on C4.2 (its window reading, decision 64.1, and its
  mechanisms at 0.5, decision 64.5), Session 54's and 49's late-Soviet sources for Centrally Planned Socialism, the
  Session 71 record and script (C4.5 and C3.4), and the scoring documents' overviews and other criteria's sections,
  used as evidence about a design. One line of the Ostrom-style commons document's C4.1 section surfaced in a search
  (it notes that v1.4's criterion carried a debt clause and a carbon clause); it gives no reading or score.

## 3. Sources

Cached before this session (`evidence_cache_s65.py`): the IMF's general government gross debt (% of GDP, World
Economic Outlook through the DataMapper, to 2031) and the World Bank's gross national saving and consumption of fixed
capital (% of GNI, to 2021), for the eight economies the configured entries cover. Cached by `evidence_cache_s72.py`
(each verified by md5): US net saving and gross national income (BEA, NIPA table 5.1, through FRED), 2000 to 2025;
the World Bank's adjusted net savings (% of GNI); Ofer (1990), "Macroeconomic Issues of Soviet Reforms" (the state
budget table, the investment share of GNP, the capital stock's growth); the "400 days" programme (1990), Appendix 1,
on the rouble state debt; the Libertarian Party platform's two passages on debt and future generations; Hahnel and
Wright (2016), three passages on the investment plan and on borrowing and saving in the consumption councils; Integral's
*Technical White Paper v0.1*, four passages; the Research Hub at its pin `8e8a6ba`, five passages. Named, not cached
(`sources_s72.md`): Singapore's Government Securities Act and the Ministry of Finance's account of its debt; Qatar's
fiscal arrangements; Timor-Leste's Petroleum Fund record (East Asia Forum, 2025; IMF, 2017); Norway's fiscal rule;
Whyte and Whyte (1991) and the Italian Civil Code, art. 2545-quater; Daly (1991), Kerschner (2010), Kallis (2011);
Kelton (2020); Van Parijs and Vanderborght (2017); the Institute for Global Prosperity (2017) and Coote and Percy
(2020); Raworth (2017); Bastani (2019).

Figures the readings quote, recomputed by the script from the cache:

- US gross debt 2025 / range 2016-2025 / 2031 (WEO): 124.4 / 106.5-132.6 / 145.0
- US net national saving 2012-2021 (WDI), range: 1.4-3.8
- US net saving 2016-2025 (BEA), lowest: 0.9
- US years of negative net saving 2000-2025 (BEA): 2008, 2009, 2010
- China gross debt 2025 / first year above 80 / 2031: 98.6 / 2023 / 122.1
- China net national saving 2012-2021, range: 17.1-26.7
- Singapore gross debt 2025 / range 2016-2025: 165.7 / 105.9-170.4
- Singapore net national saving 2012-2021, range: 25.7-34.9
- Qatar gross debt 2025 / range 2016-2025 / highest 2026-2031: 42.5 / 41.4-72.6 / 46.4
- Qatar gross debt 2014 and 2020: 24.9 and 72.6
- Qatar net national saving / adjusted net savings 2012-2021, ranges: 24.5-47.9 / 17.9-33.5
- Finland gross debt 2025 / first year above 80 / 2031: 88.4 / 2024 / 101.2
- Denmark, Norway, Sweden gross debt, highest 2016-2025: 45.2, 54.0, 43.2
- Nordic net national saving 2012-2021, lowest (DNK, FIN, NOR, SWE): 7.6, 1.2, 6.6, 9.1
- Norway adjusted net savings 2012-2021, range: 13.6-22.7

## 4. Readings

- **4.1.1 Clause 1, debt below 80% of GDP.** A configured economy: general government gross debt (IMF WEO), cleared if
  below 80% in every year of the ten to the stated date (2016 to 2025) and on the WEO's projection to 2031, short if
  above 80% at the stated date; a configuration of several economies clears only if each does (as Sessions 50 and 64
  read the four Nordic economies). Centrally Planned Socialism is read on the late-Soviet record, its level and its
  path. A design: its projected debt path from its own sources, cleared where they state a rule or a construction
  that keeps public borrowing below the bar, short where they reject the bound or keep a host economy's public
  finances unmodified (that economy's figure is then the design's, as Session 71 read Stakeholder Capitalism's exit),
  not shown where they are silent. A mechanism: out of reach (D28(c)) unless it governs public borrowing itself, as
  functional finance does for MMT + Job Guarantee.
- **4.1.2 Clause 2, positive wealth transfer.** Net national saving (gross national saving less consumption of fixed
  capital, % of GNI; World Bank WDI, to 2021) positive in every year of the latest ten years of the accounts (2012 to
  2021), the United States carried to 2025 on BEA's net saving (2016 to 2025); adjusted net savings (less resource
  depletion and pollution damage) as the check for the resource economies, a sign disagreement to be flagged. A
  design: cleared where its sources state a rule that retains net surplus as capital, short where they state an end
  to net accumulation (a steady state, sufficiency in place of accumulation), not shown where silent; a design that
  keeps a host economy unmodified carries the host's figure here too (the script's statement of 4.1.2 did not repeat
  4.1.1's host sentence; the two units it applies to, Stakeholder Capitalism and CCO-PTF-CIP-SZH, state it in their
  estimates, "on the host's figures"). A mechanism: out of reach unless it accumulates or decumulates national wealth
  itself, as a sovereign fund does.
- **4.1.3 0.0** (protocol 2.1, decision 53.2): far below on both clauses, debt above the bar and net saving negative
  over the window, with no rule or instrument that corrects either; or a system whose own logic rejects the
  criterion's concern on both clauses; never with a clause cleared. A mechanism that governs neither quantity holds at
  0.5 (D28(c); decision 64.5's precedent). On this reading no unit is 0.0: every configured economy saves positively
  over the window, and no design rejects both concerns.
- **4.1.4** The ecological transfer is C4.2's (v2.0's requirement says so); the anchors' band texts on climate debt
  and resource depletion describe v1.4's threshold and do not govern (protocol 2.3(g)).

## 5. The blind readings, and the comparison

The blind readings, as committed at `4c8bc9f`:

| Unit | Clause statuses | Verdict | Flag |
|---|---|---|---|
| CCO-PTF-CIP-SZH | S C | 0.5 | — |
| Centrally Planned Socialism | S C | 0.5 | toward 1.0 |
| Degrowth Economics | U S | 0.5 | — |
| Doughnut Economics | U U | 0.5 | — |
| Fully Automated Luxury Communism | U U | 0.5 | — |
| Georgism / Land Value Tax (LVT + Citizen's Dividend) | R R | 0.5 | — |
| Integral | C S | 0.5 | — |
| Islamic Finance / Profit-Sharing Banking | R R | 0.5 | — |
| Libertarian Minarchism | C U | 0.5 | — |
| MMT + Job Guarantee | S U | 0.5 | toward 0.0 |
| Market Socialism | U C | 0.5 | — |
| Mutual Credit / LETS | R R | 0.5 | — |
| Nordic Social Democracy | S C | 0.5 | toward 1.0 |
| Ostrom-Style Commons Governance | R R | 0.5 | — |
| Participatory Economics | U U | 0.5 | — |
| Sovereign Wealth Fund Statism | R S | 0.5 | — |
| Stakeholder Capitalism | S C | 0.5 | toward 0.0 |
| State Capitalism / China (Party-State-Directed Market Economy) | S C | 0.5 | — |
| State Capitalism / Qatar (Gulf Rentier-Distributive Statism) | C C | 1.0 | toward 0.5 |
| State Capitalism / Singapore (GLC Developmental Capitalism) | S C | 0.5 | — |
| Status Quo Market Capitalism | S C | 0.5 | toward 0.0 |
| Universal Basic Income | R R | 0.5 | — |
| Universal Basic Services | R R | 0.5 | — |

Compared with the prior (`compare_group`; part (b6)'s designs carry four pre-v2.0 clauses, so their row reports the
clause count and the verdict):

| Unit | Prior part | Prior | Blind (Session 72) | Result | Differences |
|---|---|---|---|---|---|
| CCO-PTF-CIP-SZH | (b6) | C U U C / 0.5 | S C / 0.5 | revise (clauses) | clause count 4 (prior) vs 2 (new) |
| Centrally Planned Socialism | (2.11) | U U / 0.5 | S C / 0.5 | revise (clauses) | clause 1: U (prior) vs S (new); clause 2: U (prior) vs C (new) |
| Degrowth Economics | (b6) | C C S C / 0.5 | U S / 0.5 | revise (clauses) | clause count 4 (prior) vs 2 (new) |
| Doughnut Economics | (b6) | U C U U / 0.5 | U U / 0.5 | revise (clauses) | clause count 4 (prior) vs 2 (new) |
| Fully Automated Luxury Communism | (b6) | U C U C / 0.5 | U U / 0.5 | revise (clauses) | clause count 4 (prior) vs 2 (new) |
| Georgism / Land Value Tax (LVT + Citizen's Dividend) | (2.11) | U U / 0.5 | R R / 0.5 | revise (clauses) | clause 1: U (prior) vs R (new); clause 2: U (prior) vs R (new) |
| Integral | (b6) | U C U C / 0.5 | C S / 0.5 | revise (clauses) | clause count 4 (prior) vs 2 (new) |
| Islamic Finance / Profit-Sharing Banking | (2.11) | U U / 0.5 | R R / 0.5 | revise (clauses) | clause 1: U (prior) vs R (new); clause 2: U (prior) vs R (new) |
| Libertarian Minarchism | (2.11) | U U / 0.0 | C U / 0.5 | revise (verdict) | clause 1: U (prior) vs C (new); verdict: 0.0 (prior) vs 0.5 (new) |
| MMT + Job Guarantee | (2.11) | U U / 0.5 | S U / 0.5 | revise (clauses) | clause 1: U (prior) vs S (new) |
| Market Socialism | (2.11) | U U / 0.5 | U C / 0.5 | revise (clauses) | clause 2: U (prior) vs C (new) |
| Mutual Credit / LETS | (2.11) | U U / 0.5 | R R / 0.5 | revise (clauses) | clause 1: U (prior) vs R (new); clause 2: U (prior) vs R (new) |
| Nordic Social Democracy | (2.11) | S C / 0.5 | S C / 0.5 | agree | — |
| Ostrom-Style Commons Governance | (b6) | R C R C / 0.5 | R R / 0.5 | revise (clauses) | clause count 4 (prior) vs 2 (new) |
| Participatory Economics | (b6) | U C U U / 0.5 | U U / 0.5 | revise (clauses) | clause count 4 (prior) vs 2 (new) |
| Sovereign Wealth Fund Statism | (b6) | R R U C / 0.5 | R S / 0.5 | revise (clauses) | clause count 4 (prior) vs 2 (new) |
| Stakeholder Capitalism | (2.11) | U U / 0.0 | S C / 0.5 | revise (verdict) | clause 1: U (prior) vs S (new); clause 2: U (prior) vs C (new); verdict: 0.0 (prior) vs 0.5 (new) |
| State Capitalism / China (Party-State-Directed Market Economy) | (2.11) | S C / 0.5 | S C / 0.5 | agree | — |
| State Capitalism / Qatar (Gulf Rentier-Distributive Statism) | (2.11) | C C / 1.0 | C C / 1.0 | agree | — |
| State Capitalism / Singapore (GLC Developmental Capitalism) | (2.11) | S C / 0.5 | S C / 0.5 | agree | — |
| Status Quo Market Capitalism | (2.11) | S C / 0.5 | S C / 0.5 | agree | — |
| Universal Basic Income | (2.11) | U U / 0.5 | R R / 0.5 | revise (clauses) | clause 1: U (prior) vs R (new); clause 2: U (prior) vs R (new) |
| Universal Basic Services | (2.11) | U U / 0.5 | R R / 0.5 | revise (clauses) | clause 1: U (prior) vs R (new); clause 2: U (prior) vs R (new) |

The clause statuses that change without a verdict change, in four kinds:

- **Out of reach, not "not shown" (five mechanisms of part (2.11): Georgism, Mutual Credit, Islamic Finance,
  Universal Basic Income, Universal Basic Services).** None of them governs public borrowing or a stock of national
  wealth; D28(c) reads such a clause as out of reach, holding the unit at 0.5, as decision 64.5 read the mechanisms on
  C4.2. Ostrom-style commons and, on clause 1, Sovereign Wealth Fund Statism (part (b6)) are read the same way.
- **Shown from the unit's own sources, where the prior found nothing stated:** Centrally Planned Socialism (the
  late-Soviet debt and accumulation record: clause 1 short on its path, clause 2 cleared); Market Socialism (the
  cooperatives' retention of net surplus as capital: clause 2 cleared); MMT + Job Guarantee (functional finance and
  the framework's account of the debt burden as a myth: clause 1 short).
- **The host economy's figures:** Stakeholder Capitalism and CCO-PTF-CIP-SZH, which keep the host's public finances
  (clause 1 short, clause 2 cleared narrowly).
- **The designs on v2.0's two clauses for the first time** (part (b6)): Degrowth (clause 2 short on the steady state),
  Integral (clause 1 cleared by construction, clause 2 short on sufficiency), Participatory Economics, Doughnut
  Economics and FALC (neither clause stated), Sovereign Wealth Fund Statism (clause 2 short on Timor-Leste's
  drawdown), CCO-PTF-CIP-SZH (above).

## 6. Reconciliation of the two verdict differences

A blind verdict stands unless the prior reading shows evidence the blind reading did not weigh, or the blind reading
departs from its own stated reading (section 4). The reconciliation moves a verdict only toward the prior's, and says
why; where a blind verdict stands, the prior's verdict is kept as a flag if the unit has none (Session 71's
practice).

- **Libertarian Minarchism: 0.5 (blind), prior 0.0; stands, a correction.** The prior held 0.0 on protocol 2.1's first
  condition, "no structural mechanism addresses debt or saving in the design as specified", reading only the Report's
  rationale. The design's own programme states a debt rule in the criterion's own terms: "Government should not incur
  debt, which burdens future generations without their consent", with a balanced-budget amendment balanced by
  cutting expenditure (the Libertarian Party platform), in a state confined to protecting rights; that is a
  structural mechanism addressing clause 1, which it clears as a stated rule, so 0.0 cannot hold (decision 53.2).
  Clause 2 is not shown (the platform's move to defined-contribution pensions is a funded saving channel, not a
  projection). Flagged toward 0.0, the prior's reading: the platform is a party's programme, and the minimal-state
  design as the Report specifies it states no fiscal rule.
- **Stakeholder Capitalism: 0.5 (blind), prior 0.0; stands, a correction.** The prior held 0.0 on the same first
  condition, reading the published reasons (short-termism, ESG funds) as firm governance. The blind reading agrees
  that the reform adds no fiscal or saving rule, but reads the unit, as Session 71 read its exit, on the host market
  economy whose public finances and saving it leaves unmodified: debt far above the bar, net saving small but positive
  in every year of the window. On those figures the prior itself raised Status Quo to 0.5 in the same part ("0.0
  cannot stand (protocol 2.1 and D28(f))"); the reform does not lower the host's saving, so a 0.0 for the reformed
  economy beside a 0.5 for the unreformed one would be inconsistent. The blind reading does not depart from its
  stated reading: 4.1.1 states the host rule, and the unit's clause-2 estimate states that it reads the host's figures
  (section 4 records that the script's 4.1.2 did not repeat it). Flagged toward 0.0, tracking Status Quo's flag.

**Flags the prior carried, compared.** Qatar: both readings flag 1.0 toward 0.5, on different grounds; the prior's
(depletion unnetted) is answered by adjusted net savings (section 1), and the blind ground (the debt's path without a
fiscal rule) is the one kept. Nordic Social Democracy: both flag 0.5 toward 1.0 on Finland alone. Singapore: the prior
flagged 0.5 toward 1.0 because the debt funds assets; the blind reading weighed the same point and holds that v2.0's
measure is gross debt and governs (protocol 2.3(g)), so a 1.0 is not a reading a careful scorer could reach on the
threshold as written, and no flag is kept; the point is stated in the unit's estimate. Degrowth: the prior (b6)
flagged 0.5 toward 1.0 at the horizon of v1.4's carbon clause, which v2.0 no longer has; the prior also cites Jackson
and Victor's LowGrow SFC (2020), in which a post-growth Canada's public debt rises from about 55% of GDP in 2017 to
more than 80% by 2067; the blind reading keeps clause 1 not shown for degrowth itself, since, as the prior notes, the
model is post-growth rather than degrowth and the degrowth model it located reports no debt level, and clause 2 is
short on the steady state either way.

The final readings' flags, each taken alone, on both groups' final verdicts (Sessions 71 and 72):

| Unit | Final | Flag toward | Total on 29 then | Failures then | Tier then | Changes |
|---|---:|---:|---:|---:|---|---|
| Centrally Planned Socialism | 0.5 | 1.0 | 8.0 | 15 | Structurally Inadequate | — |
| Libertarian Minarchism | 0.5 | 0.0 | 9.0 | 12 | Structurally Inadequate | — |
| MMT + Job Guarantee | 0.5 | 0.0 | 12.0 | 5 | Partially Adequate | — |
| Nordic Social Democracy | 0.5 | 1.0 | 15.5 | 1 | Potentially Adequate | — |
| Stakeholder Capitalism | 0.5 | 0.0 | 10.0 | 9 | Structurally Inadequate | — |
| State Capitalism / Qatar (Gulf Rentier-Distributive Statism) | 1.0 | 0.5 | 10.0 | 9 | Structurally Inadequate | — |
| Status Quo Market Capitalism | 0.5 | 0.0 | 11.5 | 8 | Structurally Inadequate | — |

## 7. Consequences once applied (not applied here)

Totals on the 29 criteria (`neec_scores_v2.csv`), with this group's two verdict changes alone, and with Session 71's
five (ledger D55, confirmed by the owner) as well:

| Entry | Total on 29 | After this group | After Sessions 71 and 72 | Failures | After both | Tier after both |
|---|---:|---:|---:|---:|---:|---|
| Libertarian Minarchism | 8.5 | 9.0 | 9.5 | 13 | 11 | Structurally Inadequate |
| Stakeholder Capitalism | 10.5 | 11.0 | 10.5 | 8 | 8 | Structurally Inadequate |
| Fully Automated Luxury Communism | 10.5 | 10.5 | 10.0 | 10 | 11 | Structurally Inadequate |
| Participatory Economics | 16.0 | 16.0 | 16.5 | 0 | 0 | Potentially Adequate |
| State Capitalism / Singapore (GLC Developmental Capitalism) | 13.0 | 13.0 | 13.5 | 4 | 3 | Partially Adequate |

No tier changes. First place: unchanged by this group (CCO-PTF-CIP-SZH and Participatory Economics shared at 16.0);
with Session 71's changes, Participatory Economics alone at 16.5. Libertarian Minarchism's and Stakeholder
Capitalism's totals rise by 0.5 each and their failure counts fall by one; both stay Structurally Inadequate. The
table's other rows are Session 71's changes (FALC's C3.4, Singapore's and Participatory Economics' C4.5, and
Stakeholder Capitalism's C4.5, which offsets this group's rise for that entry).

## 8. Decisions (Session 72)

All under the delegation (decision 57.2), except 72.1, the owner's.

- **72.1** (the owner's, = ledger D55, confirmed in the ledger before this session read it) Session 71's five verdict
  changes are applied at S61 as read: Participatory Economics C4.5 0.5 to 1.0 (alone first, its C4.5 flagged toward
  0.5), Stakeholder Capitalism C4.5 0.5 to 0.0, Singapore C4.5 0.0 to 0.5, FALC C3.4 0.5 to 0.0, Libertarian
  Minarchism C3.4 0.0 to 0.5. Consequence: once S61 applies them, Participatory Economics stands alone first at 16.5
  on the 29 criteria (15.0 on the 26), CCO-PTF-CIP-SZH second at 16.0; no tier changes.
- **72.2** (optional, method) readings 4.1.1 to 4.1.4 (section 4).
- **72.3** (correction) Libertarian Minarchism C4.1 0.0 to 0.5, flagged toward 0.0 (section 6).
- **72.4** (correction) Stakeholder Capitalism C4.1 0.0 to 0.5, flagged toward 0.0 (section 6).
- **72.5** (correction, no verdict effect) 8 part (2.11) units' clause statuses, and the 8 part (b6) designs read on v2.0's two
  clauses (decision 69.2), as section 5 lists them; Qatar's flag rests on the debt's path, not on unnetted depletion;
  Singapore's flag toward 1.0 lapses; Degrowth's flag toward 1.0 lapses with v1.4's carbon clause.
- **72.6** (optional, tooling) `blind_s72.py`, `evidence_cache_s72.py`, harness v42 (120 checks), `README.md`
  regenerated.

## 9. Observations for later sessions

- **The window.** v2.0 says "positive over the scoring window" and names none for a national economy; this group read
  the latest ten years of the accounts (as decision 64.1 read C4.2's windows, reporting the longer one where it
  differs). On the 20 years to 2025 the United States' net saving is negative in 2008 to 2010, which is Status Quo's
  and Stakeholder Capitalism's flag toward 0.0. The criteria record's next amendment could fix the window.
- **Gross debt.** Singapore's case shows the gross measure counting debt issued to build assets; v2.0 names gross
  debt, and the readings follow it. A net measure is a matter for the criteria record, not for a reading.
- **I9, again.** Libertarian Minarchism's rise here is on its own programme's debt rule; its C4.5, held at 0.5 by D28
  while Status Quo's is 0.0 (ledger I9), is a separate item and unchanged.
- **The World Bank's saving series end in 2021.** A later session may extend clause 2 with the IMF's or the national
  statistics offices' accounts; on the series cached no sign changes.

## 10. Model and disclosure

Read on Opus 5.5 (Claude Code cloud), at high effort, as STATE.md's routing gave; the earlier readings compared are
Session 65's on Sonnet 5.5 (part (2.11)) and Session 43's (part (b6)), read on the pre-v2.0 four-clause list.
