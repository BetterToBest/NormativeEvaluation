# NEEC Blind Review, Session 73: C4.4 and C4.2

**Session 73 · 2026-10-18 · Stage 3b, the blind re-read (ledger S56; decisions 69.1, 69.2; ledger D52, D53) ·
Scorer: Claude (Opus 5.5) · Owner: Duke Johnson**

Script: `blind_s73.py` (checked by the harness, which compares its output with `blind_s73_output.txt` and confirms
that this record carries every table it generates). Evidence: `evidence_cache_s73.py` (ten files, by digest) beside
Session 65's one file for C4.4 and Session 64's two for C4.2 (`evidence_cache_s65.py`, `evidence_cache_s64.py`), with
`evidence_cache/C4.4/sources_s73.md` and `evidence_cache/C4.2/sources_s73.md` naming the sources not cached. Nothing
here changes a published score: the final readings are applied by generator in ledger step S61 (STATE.md, "Next
work").

## 1. Summary

Thirty-three units were re-read on Opus 5.5, blind to the earlier readings, then compared with them: the 17 C4.4 Power
Distribution units Session 65 read on Sonnet 5.5 (part (2.11)), on v2.0's two clauses ("Democratic accountability for
≥80% of major decisions", "removal/replacement mechanisms functional"), and the 16 C4.2 Ecological Compliance units
Session 64 read on Sonnet 5.5 (part (2.10)), on v2.0's four (consumption-based carbon falling ≥3.8% a year,
biodiversity neutral or positive, extraction within regeneration, no more than two of four downscaled boundaries
transgressed).

- **Blind against prior.** C4.4: 4 agree, 13 revise, **6 verdicts differ** (Doughnut Economics, Fully Automated Luxury
  Communism, Islamic Finance, Stakeholder Capitalism, Singapore and Universal Basic Income, each 0.0 to 0.5). C4.2: 1
  agree, 15 revise, **5 verdicts differ** (China, Islamic Finance, Singapore and Sovereign Wealth Fund Statism 0.0 to
  0.5; Centrally Planned Socialism 0.5 to 0.0). Most clause revisions are of two kinds: a mechanism's clause the prior
  left "not shown" that the mechanism does not govern at all (out of reach, D28(c)); and C4.2's clauses 3 and 4, which
  the prior left "not shown" because the footprint and boundary accounts were not reachable, and which this session
  read on the country data of Fanning et al. (2022) and O'Neill et al. (2018), cached.
- **Reconciliation (protocol 5.3, Session 71's rule):** three blind verdicts move to the prior's (Doughnut Economics'
  C4.4, Singapore's C4.4 and Singapore's C4.2; section 6), each keeping its blind verdict as a flag; eight stand.
- **Final against prior: eight verdicts change.** C4.4: Fully Automated Luxury Communism, Islamic Finance, Stakeholder
  Capitalism and Universal Basic Income, 0.0 to 0.5, each flagged toward 0.0. C4.2: China, Islamic Finance and
  Sovereign Wealth Fund Statism 0.0 to 0.5 (each flagged toward 0.0), Centrally Planned Socialism 0.5 to 0.0 (flagged
  toward 0.5). No CCO-PTF-CIP-SZH unit is in this group.
- **The two flagged units Session 64 named.** Market Socialism's C4.2 is 0.5 on both readings, flagged toward 0.0 on
  both. Sovereign Wealth Fund Statism's C4.2 rises to 0.5: the mechanism scored is a fund that holds a non-recurring
  revenue, classically but not necessarily resource royalties (its scoring document's own scope), so the exemplars'
  extraction is the host's, not the mechanism's (protocol 3.2), and the prior's own flag said so.
- **Consequence, once applied (S61):** seven failures fewer and one more; **one tier changes: Sovereign Wealth Fund
  Statism, Partially Adequate to Potentially Adequate** (three failures to two), alone and with Sessions 71 and 72.
  First place is unchanged by this group (CCO-PTF-CIP-SZH and Participatory Economics shared at 16.0, or Participatory
  Economics alone at 16.5 with Sessions 71's and 72's changes). Four flags would change a tier (section 7). Because a
  tier changes, ledger D56 asks the owner to confirm that the eight changes are applied at S61 as read (default yes).

## 2. The blind step

The readings were written from `blind_review.blind_view()` (the v2.0 clause text and the cache file names), the
criteria's measurement text, the sources below, and the units' scoring documents' overviews and the Report's overview
lines, and committed and pushed as checkpoint `7a6e0df` ("NEEC checkpoint s73: blind readings of C4.4 and C4.2
recorded, before the prior readings are opened") before part (2.11)'s or part (2.10)'s readings of these units, or
Session 64's record, were opened. `blind_s73.py` at that commit holds them exactly: every reading, from the first C4.4 unit to the last C4.2 one, is
unchanged at the session's last commit. After it were added the docstring's paragraph on the comparison and its usage
line, the constant naming the post-checkpoint file below and its entry in `READ`, and the comparison, the
reconciliation (RECONCILE) and six flags (FLAGS).

What the session had seen before recording, disclosed so a reader can weigh the blindness:

- **criteria.json's anchors**, which quote published (v1) examples: on C4.4, Participatory Economics 1.0, Libertarian
  Minarchism 0.5, Status Quo Market Capitalism and Centrally Planned Socialism 0.0; on C4.2, Participatory Economics
  1.0, Nordic Social Democracy 0.5, Stakeholder Capitalism 0.0.
- **STATE.md, the handoff and the ledger** (step S56): Session 64 "flagged Market Socialism toward 0.0 and Sovereign
  Wealth Fund Statism toward 0.5", which implies the prior's 0.5 and (most likely) 0.0 for those two units on C4.2.
  `blind_s72.py`'s docstring cites "the precedent of decision 64.5" for a mechanism that governs neither quantity
  holding at 0.5, without naming the units.
- **Report lines seen while listing its headings and overviews:** the abstract's v1 finding that ecological compliance
  fails 3 of 15 systems, Status Quo's "Key Deficiencies" line, which names ecological compliance and power
  distribution among its v1 failures (the anchor already quotes its C4.4 0.0), and Nordic Social Democracy's overview
  ("insufficient ... particularly [on] automation and ecological sustainability"). No C4.4 or C4.2 line of the Report
  or of a scoring document was opened; every search excluded them.
- **`evidence_cache_s64.py`'s first docstring lines** (C4.2's clause 1 read as the compound annual rate on the Global
  Carbon Budget's consumption accounts), a method, no reading.

One file was added after the checkpoint: `evidence_cache/C4.2/fanning_2022_biophysical_bau.csv` (Fanning et al.'s
business-as-usual projections to 2030), read only for the reconciliation of China's C4.2 (section 6). The Libertarian
Party page is served dynamically, so its header digest changed on a re-fetch within the session; the cached extract is
the checkpoint's, and its passages are unchanged.

## 3. Sources

Cached by `evidence_cache_s73.py` (digests in `FILES`): C4.4, self-employment as a share of employment (World Bank WDI,
modelled ILO estimates) for the United States, China, Singapore and Qatar; US government and total nonfarm payrolls
(BLS, through FRED); V-Dem's Regimes of the World for the Soviet years (through OWID). C4.2, the Red List Index
unrounded (UN SDG database, SDG 15.5.1), 2000 to 2025 (the OWID file Session 64 cached rounds to two decimals, at
which the Nordic series reads as flat); Fanning, O'Neill, Hickel and Roux (2022), the historical biophysical data, 1992
to 2015, and the business-as-usual projections (post-checkpoint); O'Neill, Fanning, Lamb and Steinberger (2018),
biophysical data (blue water); the Soviet republics' territorial CO2, 1960 to 1991 (Global Carbon Budget through OWID's
co2-data, which allocates the Soviet years to the successor states); the Libertarian Party platform's sections 2.2
and 2.3. Session 65's V-Dem file and Session 64's consumption-CO2 and Red List files are read as cached. The sources
cited but not cached (the instruments in each configuration, the designs' literature) are named in the two
`sources_s73.md` files. Network access was open from the start; goodlife.leeds.ac.uk and the Footprint Network's API
refused the container, and the White Rose and Springer copies of the two papers' data served instead.

## 4. Readings

The method each unit applies is stated in full in `blind_s73.py`'s docstring (readings 4.4.1 to 4.4.4 and 4.2.1 to
4.2.6). In brief:

- **C4.4 clause 1** is the share of employment in organizations whose major decisions answer to those they affect, as
  the measurement defines it; a configured economy's public sector counts only where V-Dem rates it an electoral or
  liberal democracy at the stated date, and the share is read on the most generous count. **Clause 2** is the
  capacity to remove decision-makers in practice: V-Dem's classification for a configured economy (cleared at 2 or 3),
  the design's own mechanism or its unmodified host's, out of reach for a mechanism. **0.0** where there are no free
  elections and no member control and clause 1 is far short (4.4.3), and on protocol 2.1's first condition.
- **C4.2 clause 1** is the compound annual rate of consumption-based CO2 over 2013 to 2023 and since 2019; **clause 2**
  the Red List Index in 2025 against 2016, unrounded; **clause 3** the ecological footprint against world biocapacity
  per person (Fanning et al., 2015); **clause 4** the count of phosphorus, nitrogen, land-system change (Fanning et
  al., 2015) and blue water (O'Neill et al., 2011) above the boundary, cleared at two or fewer. **0.0** with no clause
  cleared, far below, and no absolute-reduction mechanism (a target relative to business as usual, an intensity
  benchmark or voluntary disclosure does not count), or where the system's logic rejects public limits (4.2.5). A
  mechanism that governs none of the quantities holds at 0.5 (D28(c)).

## 5. The blind readings, and the comparison

The blind readings, as recorded at the checkpoint (C4.4, then C4.2):

| Unit | Clause statuses | Verdict | Flag |
|---|---|---|---|
| Centrally Planned Socialism | S S | 0.0 (0.0 reason stated) | — |
| Doughnut Economics | U U | 0.5 | toward 0.0 |
| Fully Automated Luxury Communism | U C | 0.5 | — |
| Georgism / Land Value Tax (LVT + Citizen's Dividend) | R R | 0.5 | — |
| Islamic Finance / Profit-Sharing Banking | R R | 0.5 | — |
| Libertarian Minarchism | S C | 0.5 | — |
| MMT + Job Guarantee | R R | 0.5 | — |
| Mutual Credit / LETS | R R | 0.5 | — |
| Ostrom-Style Commons Governance | S R | 0.5 | — |
| Sovereign Wealth Fund Statism | R R | 0.5 | — |
| Stakeholder Capitalism | S C | 0.5 | — |
| State Capitalism / China (Party-State-Directed Market Economy) | S S | 0.0 (0.0 reason stated) | — |
| State Capitalism / Qatar (Gulf Rentier-Distributive Statism) | S S | 0.0 (0.0 reason stated) | — |
| State Capitalism / Singapore (GLC Developmental Capitalism) | S S | 0.5 | toward 0.0 |
| Status Quo Market Capitalism | S C | 0.5 | toward 0.0 |
| Universal Basic Income | R R | 0.5 | — |
| Universal Basic Services | S R | 0.5 | — |

| Unit | Clause statuses | Verdict | Flag |
|---|---|---|---|
| Centrally Planned Socialism | S S U U | 0.0 (0.0 reason stated) | toward 0.5 |
| Georgism / Land Value Tax (LVT + Citizen's Dividend) | R R R R | 0.5 | — |
| Islamic Finance / Profit-Sharing Banking | R R R R | 0.5 | — |
| Libertarian Minarchism | S U U U | 0.0 (0.0 reason stated) | toward 0.5 |
| Market Socialism | U U U U | 0.5 | toward 0.0 |
| Mutual Credit / LETS | R R R R | 0.5 | — |
| Nordic Social Democracy | S C S S | 0.5 | — |
| Ostrom-Style Commons Governance | R U R R | 0.5 | — |
| Sovereign Wealth Fund Statism | R R R R | 0.5 | toward 0.0 |
| Stakeholder Capitalism | S S S S | 0.0 (0.0 reason stated) | toward 0.5 |
| State Capitalism / China (Party-State-Directed Market Economy) | S S S C | 0.5 | — |
| State Capitalism / Qatar (Gulf Rentier-Distributive Statism) | S S S U | 0.0 (0.0 reason stated) | — |
| State Capitalism / Singapore (GLC Developmental Capitalism) | S S S U | 0.5 | toward 0.0 |
| Status Quo Market Capitalism | S S S S | 0.0 (0.0 reason stated) | toward 0.5 |
| Universal Basic Income | R R R R | 0.5 | — |
| Universal Basic Services | U R U R | 0.5 | — |

The comparison with part (2.11) (C4.4) and part (2.10) (C4.2), by `compare_group()`:

| Unit | Prior | Blind (Session 73) | Result | Differences |
|---|---|---|---|---|
| Centrally Planned Socialism | S S / 0.0 | S S / 0.0 | agree | — |
| Doughnut Economics | U U / 0.0 | U U / 0.5 | revise (verdict) | verdict: 0.0 (prior) vs 0.5 (new) |
| Fully Automated Luxury Communism | U U / 0.0 | U C / 0.5 | revise (verdict) | clause 2: U (prior) vs C (new); verdict: 0.0 (prior) vs 0.5 (new) |
| Georgism / Land Value Tax (LVT + Citizen's Dividend) | U U / 0.5 | R R / 0.5 | revise (clauses) | clause 1: U (prior) vs R (new); clause 2: U (prior) vs R (new) |
| Islamic Finance / Profit-Sharing Banking | U U / 0.0 | R R / 0.5 | revise (verdict) | clause 1: U (prior) vs R (new); clause 2: U (prior) vs R (new); verdict: 0.0 (prior) vs 0.5 (new) |
| Libertarian Minarchism | S U / 0.5 | S C / 0.5 | revise (clauses) | clause 2: U (prior) vs C (new) |
| MMT + Job Guarantee | U U / 0.5 | R R / 0.5 | revise (clauses) | clause 1: U (prior) vs R (new); clause 2: U (prior) vs R (new) |
| Mutual Credit / LETS | U U / 0.5 | R R / 0.5 | revise (clauses) | clause 1: U (prior) vs R (new); clause 2: U (prior) vs R (new) |
| Ostrom-Style Commons Governance | U U / 0.5 | S R / 0.5 | revise (clauses) | clause 1: U (prior) vs S (new); clause 2: U (prior) vs R (new) |
| Sovereign Wealth Fund Statism | U U / 0.5 | R R / 0.5 | revise (clauses) | clause 1: U (prior) vs R (new); clause 2: U (prior) vs R (new) |
| Stakeholder Capitalism | S U / 0.0 | S C / 0.5 | revise (verdict) | clause 2: U (prior) vs C (new); verdict: 0.0 (prior) vs 0.5 (new) |
| State Capitalism / China (Party-State-Directed Market Economy) | S S / 0.0 | S S / 0.0 | agree | — |
| State Capitalism / Qatar (Gulf Rentier-Distributive Statism) | S S / 0.0 | S S / 0.0 | agree | — |
| State Capitalism / Singapore (GLC Developmental Capitalism) | S S / 0.0 | S S / 0.5 | revise (verdict) | verdict: 0.0 (prior) vs 0.5 (new) |
| Status Quo Market Capitalism | S C / 0.5 | S C / 0.5 | agree | — |
| Universal Basic Income | S U / 0.0 | R R / 0.5 | revise (verdict) | clause 1: S (prior) vs R (new); clause 2: U (prior) vs R (new); verdict: 0.0 (prior) vs 0.5 (new) |
| Universal Basic Services | U U / 0.5 | S R / 0.5 | revise (clauses) | clause 1: U (prior) vs S (new); clause 2: U (prior) vs R (new) |

| Unit | Prior | Blind (Session 73) | Result | Differences |
|---|---|---|---|---|
| Centrally Planned Socialism | U U U U / 0.5 | S S U U / 0.0 | revise (verdict) | clause 1: U (prior) vs S (new); clause 2: U (prior) vs S (new); verdict: 0.5 (prior) vs 0.0 (new) |
| Georgism / Land Value Tax (LVT + Citizen's Dividend) | U U U U / 0.5 | R R R R / 0.5 | revise (clauses) | clause 1: U (prior) vs R (new); clause 2: U (prior) vs R (new); clause 3: U (prior) vs R (new); clause 4: U (prior) vs R (new) |
| Islamic Finance / Profit-Sharing Banking | U U U U / 0.0 | R R R R / 0.5 | revise (verdict) | clause 1: U (prior) vs R (new); clause 2: U (prior) vs R (new); clause 3: U (prior) vs R (new); clause 4: U (prior) vs R (new); verdict: 0.0 (prior) vs 0.5 (new) |
| Libertarian Minarchism | U U U U / 0.0 | S U U U / 0.0 | revise (clauses) | clause 1: U (prior) vs S (new) |
| Market Socialism | U U U U / 0.5 | U U U U / 0.5 | agree | — |
| Mutual Credit / LETS | U U U U / 0.5 | R R R R / 0.5 | revise (clauses) | clause 1: U (prior) vs R (new); clause 2: U (prior) vs R (new); clause 3: U (prior) vs R (new); clause 4: U (prior) vs R (new) |
| Nordic Social Democracy | S C U U / 0.5 | S C S S / 0.5 | revise (clauses) | clause 3: U (prior) vs S (new); clause 4: U (prior) vs S (new) |
| Ostrom-Style Commons Governance | R U U R / 0.5 | R U R R / 0.5 | revise (clauses) | clause 3: U (prior) vs R (new) |
| Sovereign Wealth Fund Statism | U U U U / 0.0 | R R R R / 0.5 | revise (verdict) | clause 1: U (prior) vs R (new); clause 2: U (prior) vs R (new); clause 3: U (prior) vs R (new); clause 4: U (prior) vs R (new); verdict: 0.0 (prior) vs 0.5 (new) |
| Stakeholder Capitalism | U U U U / 0.0 | S S S S / 0.0 | revise (clauses) | clause 1: U (prior) vs S (new); clause 2: U (prior) vs S (new); clause 3: U (prior) vs S (new); clause 4: U (prior) vs S (new) |
| State Capitalism / China (Party-State-Directed Market Economy) | S S U U / 0.0 | S S S C / 0.5 | revise (verdict) | clause 3: U (prior) vs S (new); clause 4: U (prior) vs C (new); verdict: 0.0 (prior) vs 0.5 (new) |
| State Capitalism / Qatar (Gulf Rentier-Distributive Statism) | S S U U / 0.0 | S S S U / 0.0 | revise (clauses) | clause 3: U (prior) vs S (new) |
| State Capitalism / Singapore (GLC Developmental Capitalism) | S S U U / 0.0 | S S S U / 0.5 | revise (verdict) | clause 3: U (prior) vs S (new); verdict: 0.0 (prior) vs 0.5 (new) |
| Status Quo Market Capitalism | S S U U / 0.0 | S S S S / 0.0 | revise (clauses) | clause 3: U (prior) vs S (new); clause 4: U (prior) vs S (new) |
| Universal Basic Income | U U U U / 0.5 | R R R R / 0.5 | revise (clauses) | clause 1: U (prior) vs R (new); clause 2: U (prior) vs R (new); clause 3: U (prior) vs R (new); clause 4: U (prior) vs R (new) |
| Universal Basic Services | U U U U / 0.5 | U R U R / 0.5 | revise (clauses) | clause 2: U (prior) vs R (new); clause 4: U (prior) vs R (new) |

What the clause revisions are, besides the verdicts (section 6):

- **Out of reach where the prior had "not shown".** Every mechanism's clauses on both criteria (Georgism, Islamic
  finance, Mutual Credit/LETS, MMT, Sovereign Wealth Fund Statism, UBI, and Ostrom's and UBS's where they reach), as
  Sessions 71 and 72 read them. Ostrom's and UBS's clause 1 on C4.4 is short rather than out of reach: each governs the
  accountability of some organizations, but generalised they employ far less than 80%.
- **C4.2 clauses 3 and 4 read where the prior could not.** Every configured economy's footprint is several times world
  biocapacity (2.24 for China to 8.29 for Qatar, 2015); the United States transgresses all four boundaries, each Nordic
  economy three; China transgresses two (phosphorus and nitrogen; land-system change at 0.42 and blue water at 0.54
  within), so its clause 4 is cleared; Singapore and Qatar lack one boundary each in the accounts.
- **Clause 2 of C4.4 cleared for Libertarian Minarchism, Stakeholder Capitalism and FALC**, which keep elected
  government (the design's own, or the host's that the reform leaves unmodified, as Session 72 read Stakeholder
  Capitalism).
- **Clause 1 of C4.2 short for Libertarian Minarchism and Stakeholder Capitalism** on their own sources and the host's
  record (the prior had "not shown").

## 6. Reconciliation of the eleven verdict differences

A blind verdict stands unless the prior reading shows evidence the blind reading did not weigh, or the blind reading
departs from its own stated reading (section 4). The reconciliation moves a verdict only toward the prior's, and says
why; where it does, the blind verdict is kept as the flag. A standing difference whose blind reading had no flag keeps
the prior's verdict as its flag.

**Reconciled to the prior's (three):**

- **Doughnut Economics, C4.4: 0.5 (blind) to 0.0, the prior's.** The blind estimates found the ownership forms offered
  "as a menu, not an adopted design" and no institution of removal specified, and the blind flag stated protocol 2.1's
  first condition; the 0.5 credited the menu as though it were a mechanism, which the estimates deny. Session 71
  reconciled the same framework's C4.5 to 0.0 on the same ground. Flagged toward 0.5.
- **Singapore, C4.4: 0.5 (blind) to 0.0, the prior's.** Reading 4.4.3, stated before the readings, sets 0.0 where there
  are no free elections and no member control and clause 1 is far short, and reading 4.4.2 takes V-Dem's
  classification as the test of free elections. Singapore is an electoral autocracy throughout 2014 to 2025, its public
  sector does not count and self-employment is 12.7%; the blind 0.5 rested on a judgment of the elections'
  competitiveness that the stated reading does not make. Flagged toward 0.5, as the prior was.
- **Singapore, C4.2: 0.5 (blind) to 0.0, the prior's.** The blind reading credited the carbon tax as an
  absolute-reduction mechanism. The prior cites the entry's own account that Singapore's 2030 target path rises (rated
  highly insufficient by the Climate Action Tracker), which the blind reading did not weigh and which its own flag
  anticipated; a tax set under a target that lets emissions rise is not, on reading 4.2.5, an absolute-reduction
  mechanism in the configuration at the stated date. Flagged toward 0.5, as the prior was.

**Standing (eight):**

- **Fully Automated Luxury Communism, C4.4: 0.5 (blind), prior 0.0; stands.** The prior left clause 2 "not shown" and
  held 0.0 on the published finding that the control of the machines is unresolved. That finding is clause 1's, and
  the blind reading weighs it (not shown). But the design is pursued through elections in a liberal democracy whose
  removal mechanisms it keeps, so clause 2 is cleared, and 2.1's 0.0 cannot hold with a clause cleared (D28(f)).
  Flagged toward 0.0, the prior's reading.
- **Stakeholder Capitalism, C4.4: 0.5 (blind), prior 0.0; stands.** Both readings find clause 1 short in the
  definition's own words (an owner-elected majority). The prior found no mechanism of removal in the reform's sources;
  the blind reading reads the host's institutions, which the reform leaves unmodified, as Session 72 read Stakeholder
  Capitalism's C4.1 (`NEEC_BlindReview_s72.md`, section 6). Flagged toward 0.0.
- **Islamic Finance and Universal Basic Income, C4.4: 0.5 (blind), prior 0.0; stand.** Both are mechanisms. The prior
  read them "not shown" and 0.0 on 2.1's first condition, while holding Georgism, Mutual Credit, MMT, Sovereign Wealth
  Fund Statism, Ostrom-style commons and UBS at 0.5 on the same pattern, a class inconsistency (protocol 2.3(e): the
  same reading for every entry of the same class). A mechanism that does not govern the quantity is out of reach, which
  holds it at 0.5 and does not by itself make 0.0 (D28(c)). Flagged toward 0.0, the prior's reading.
- **China, C4.2: 0.5 (blind), prior 0.0; stands.** The prior left clauses 3 and 4 "not shown" because the accounts were
  unreachable. On the cached accounts China transgresses two of the four boundaries (phosphorus 3.00, nitrogen 2.68;
  land-system change 0.42 in 2015, blue water 0.54 in 2011), and Fanning et al.'s business-as-usual projection keeps
  land-system change within the boundary to 2030 (0.48, upper bound 0.54), so clause 4 is cleared and 2.1's 0.0 cannot
  hold with it (D28(f)). Flagged toward 0.0, on reading clause 4 as not shown at the stated date.
- **Islamic Finance, C4.2: 0.5 (blind), prior 0.0; stands.** The prior read green sukuk and value-based intermediation
  as allocative labels substituting for absolute limits (the anchor's second 0.0 case). They are labels on part of the
  mechanism's finance, not its answer to the criterion's quantities, which it does not govern; on the class reading
  above (Georgism, Mutual Credit and UBI held at 0.5 by the prior), it holds at 0.5. Flagged toward 0.0.
- **Sovereign Wealth Fund Statism, C4.2: 0.5 (blind), prior 0.0; stands.** The prior held 0.0 because "the mechanism's
  own funding is continued fossil-fuel extraction". The scoring document's scope defines the mechanism as a fund for "a
  large, non-recurring revenue stream — classically natural-resource royalties, though not exclusively", and the
  exemplars' extraction is the host economy's (protocol 3.2: "score the mechanism, not a country"), as the prior's own
  flag said. The blind reading weighed the classic form in its flag toward 0.0, which stands.
- **Centrally Planned Socialism, C4.2: 0.0 (blind), prior 0.5; stands.** The prior left all four clauses "not shown"
  for want of a projection and held 0.5 on the published account, flagged toward 0.0. The historical record is the
  evidence for a historical system (protocol 4.1): the Soviet territories' emissions rose from 1,446 Mt in 1960 to
  3,935 Mt in 1988 (1.54% a year over 1980 to 1988), and the plan's own irrigation programme destroyed the Aral Sea and
  its fishery. Neither is weighed by the prior, which calls the Aral Sea "damage, not a level of the index". Flagged
  toward 0.5.

The final readings (`blind_s73.FINAL`, what S61 applies), C4.4 then C4.2:

| Unit | Clause statuses | Final verdict | Flag | Against the prior |
|---|---|---|---|---|
| Centrally Planned Socialism | S S | 0.0 | — | the prior's verdict |
| Doughnut Economics | U U | 0.0 | toward 0.5 | reconciled to the prior's |
| Fully Automated Luxury Communism | U C | 0.5 | toward 0.0 | changes, 0.0 to 0.5 |
| Georgism / Land Value Tax (LVT + Citizen's Dividend) | R R | 0.5 | — | the prior's verdict |
| Islamic Finance / Profit-Sharing Banking | R R | 0.5 | toward 0.0 | changes, 0.0 to 0.5 |
| Libertarian Minarchism | S C | 0.5 | — | the prior's verdict |
| MMT + Job Guarantee | R R | 0.5 | — | the prior's verdict |
| Mutual Credit / LETS | R R | 0.5 | — | the prior's verdict |
| Ostrom-Style Commons Governance | S R | 0.5 | — | the prior's verdict |
| Sovereign Wealth Fund Statism | R R | 0.5 | — | the prior's verdict |
| Stakeholder Capitalism | S C | 0.5 | toward 0.0 | changes, 0.0 to 0.5 |
| State Capitalism / China (Party-State-Directed Market Economy) | S S | 0.0 | — | the prior's verdict |
| State Capitalism / Qatar (Gulf Rentier-Distributive Statism) | S S | 0.0 | — | the prior's verdict |
| State Capitalism / Singapore (GLC Developmental Capitalism) | S S | 0.0 | toward 0.5 | reconciled to the prior's |
| Status Quo Market Capitalism | S C | 0.5 | toward 0.0 | the prior's verdict |
| Universal Basic Income | R R | 0.5 | toward 0.0 | changes, 0.0 to 0.5 |
| Universal Basic Services | S R | 0.5 | — | the prior's verdict |

| Unit | Clause statuses | Final verdict | Flag | Against the prior |
|---|---|---|---|---|
| Centrally Planned Socialism | S S U U | 0.0 | toward 0.5 | changes, 0.5 to 0.0 |
| Georgism / Land Value Tax (LVT + Citizen's Dividend) | R R R R | 0.5 | — | the prior's verdict |
| Islamic Finance / Profit-Sharing Banking | R R R R | 0.5 | toward 0.0 | changes, 0.0 to 0.5 |
| Libertarian Minarchism | S U U U | 0.0 | toward 0.5 | the prior's verdict |
| Market Socialism | U U U U | 0.5 | toward 0.0 | the prior's verdict |
| Mutual Credit / LETS | R R R R | 0.5 | — | the prior's verdict |
| Nordic Social Democracy | S C S S | 0.5 | — | the prior's verdict |
| Ostrom-Style Commons Governance | R U R R | 0.5 | — | the prior's verdict |
| Sovereign Wealth Fund Statism | R R R R | 0.5 | toward 0.0 | changes, 0.0 to 0.5 |
| Stakeholder Capitalism | S S S S | 0.0 | toward 0.5 | the prior's verdict |
| State Capitalism / China (Party-State-Directed Market Economy) | S S S C | 0.5 | toward 0.0 | changes, 0.0 to 0.5 |
| State Capitalism / Qatar (Gulf Rentier-Distributive Statism) | S S S U | 0.0 | — | the prior's verdict |
| State Capitalism / Singapore (GLC Developmental Capitalism) | S S S U | 0.0 | toward 0.5 | reconciled to the prior's |
| Status Quo Market Capitalism | S S S S | 0.0 | toward 0.5 | the prior's verdict |
| Universal Basic Income | R R R R | 0.5 | — | the prior's verdict |
| Universal Basic Services | U R U R | 0.5 | — | the prior's verdict |

## 7. Consequences once applied (not applied here)

On the 29 criteria (`neec_scores_v2.csv`), this group's final verdict changes alone and on top of Sessions 71's and 72's
(`blind_s71.FINAL`, `blind_s72.FINAL`), entries that change:

| Entry | Total on 29 | After this group | After Sessions 71 to 73 | Failures | After all three | Tier after all three |
|---|---:|---:|---:|---:|---:|---|
| Centrally Planned Socialism | 7.5 | 7.0 | 7.0 | 15 | 16 | Structurally Inadequate |
| Libertarian Minarchism | 8.5 | 8.5 | 9.5 | 13 | 11 | Structurally Inadequate |
| Universal Basic Income | 12.0 | 12.5 | 12.5 | 7 | 6 | Structurally Inadequate |
| Stakeholder Capitalism | 10.5 | 11.0 | 11.0 | 8 | 7 | Structurally Inadequate |
| Fully Automated Luxury Communism | 10.5 | 11.0 | 10.5 | 10 | 10 | Structurally Inadequate |
| Participatory Economics | 16.0 | 16.0 | 16.5 | 0 | 0 | Potentially Adequate |
| Sovereign Wealth Fund Statism | 14.5 | 15.0 | 15.0 | 3 | 2 | Potentially Adequate |
| State Capitalism / China (Party-State-Directed Market Economy) | 10.5 | 11.0 | 11.0 | 9 | 8 | Structurally Inadequate |
| State Capitalism / Singapore (GLC Developmental Capitalism) | 13.0 | 13.0 | 13.5 | 4 | 3 | Partially Adequate |
| Islamic Finance / Profit-Sharing Banking | 13.0 | 14.0 | 14.0 | 5 | 3 | Partially Adequate |

Each final reading's flag taken alone, on all three groups' final verdicts:

| Unit | Criterion | Final | Flag toward | Total on 29 then | Failures then | Tier then | Changes |
|---|---|---:|---:|---:|---:|---|---|
| Centrally Planned Socialism | C4.2 | 0.0 | 0.5 | 7.5 | 15 | Structurally Inadequate | — |
| Islamic Finance / Profit-Sharing Banking | C4.2 | 0.5 | 0.0 | 13.5 | 4 | Partially Adequate | — |
| Libertarian Minarchism | C4.2 | 0.0 | 0.5 | 10.0 | 10 | Structurally Inadequate | — |
| Market Socialism | C4.2 | 0.5 | 0.0 | 14.0 | 3 | Partially Adequate | tier: Potentially Adequate to Partially Adequate |
| Sovereign Wealth Fund Statism | C4.2 | 0.5 | 0.0 | 14.5 | 3 | Partially Adequate | tier: Potentially Adequate to Partially Adequate |
| Stakeholder Capitalism | C4.2 | 0.0 | 0.5 | 11.5 | 6 | Structurally Inadequate | — |
| State Capitalism / China (Party-State-Directed Market Economy) | C4.2 | 0.5 | 0.0 | 10.5 | 9 | Structurally Inadequate | — |
| State Capitalism / Singapore (GLC Developmental Capitalism) | C4.2 | 0.0 | 0.5 | 14.0 | 2 | Potentially Adequate | tier: Partially Adequate to Potentially Adequate |
| Status Quo Market Capitalism | C4.2 | 0.0 | 0.5 | 12.5 | 6 | Structurally Inadequate | — |
| Doughnut Economics | C4.4 | 0.0 | 0.5 | 11.0 | 7 | Structurally Inadequate | — |
| Fully Automated Luxury Communism | C4.4 | 0.5 | 0.0 | 10.0 | 11 | Structurally Inadequate | — |
| Islamic Finance / Profit-Sharing Banking | C4.4 | 0.5 | 0.0 | 13.5 | 4 | Partially Adequate | — |
| Stakeholder Capitalism | C4.4 | 0.5 | 0.0 | 10.5 | 8 | Structurally Inadequate | — |
| State Capitalism / Singapore (GLC Developmental Capitalism) | C4.4 | 0.0 | 0.5 | 14.0 | 2 | Potentially Adequate | tier: Partially Adequate to Potentially Adequate |
| Status Quo Market Capitalism | C4.4 | 0.5 | 0.0 | 11.5 | 8 | Structurally Inadequate | — |
| Universal Basic Income | C4.4 | 0.5 | 0.0 | 12.0 | 7 | Structurally Inadequate | — |

Four flags would change a tier: Market Socialism's C4.2 toward 0.0 and Sovereign Wealth Fund Statism's toward 0.0
(each Potentially to Partially Adequate), Singapore's C4.4 and C4.2 toward 0.5 (each Partially to Potentially
Adequate, on Session 71's changes). None would change first place.

## 8. Decisions (Session 73)

- **73.1** (optional, method) readings 4.4.1 to 4.4.4 and 4.2.1 to 4.2.6 (section 4): C4.4 on V-Dem, the most generous
  employment count and the designs' own institutions; C4.2's clause 2 on the unrounded index over 2016 to 2025, its
  clauses 3 and 4 on Fanning et al. (2022) and O'Neill et al. (2018).
- **73.2** (corrections) C4.4: Fully Automated Luxury Communism, Islamic Finance, Stakeholder Capitalism and Universal
  Basic Income, 0.0 to 0.5, each flagged toward 0.0.
- **73.3** (corrections) C4.2: China, Islamic Finance and Sovereign Wealth Fund Statism 0.0 to 0.5, each flagged toward
  0.0; Centrally Planned Socialism 0.5 to 0.0, flagged toward 0.5. Sovereign Wealth Fund Statism's tier rises to
  Potentially Adequate once applied.
- **73.4** (corrections, no verdict effect) the clause statuses section 5 lists, and the three reconciliations to the
  prior's verdict (section 6), with their flags.
- **73.5** (optional, tooling) `evidence_cache_s73.py` and `blind_s73.py`, harness v43.
- **Ledger D56** (for the owner; default yes): apply the eight changes at S61 as read, including the tier change.
  Until answered, S61 applies the default.

## 9. Observations for later sessions

- **Clauses 3 and 4 of C4.2 elsewhere.** The units of C4.2 read in parts (a) and (b7) (Doughnut Economics, FALC, MMT,
  Participatory Economics, Degrowth, CCO-PTF-CIP-SZH, Integral) were not in this group; the configured economies'
  footprint and boundary data cached here would not bear on those designs, which are read on projections.
- **Mechanisms held at 0.0 on 2.1's first condition.** The prior placed two mechanisms at 0.0 on each criterion while
  holding the others at 0.5 on the same pattern. The same check is worth making in the groups that remain (C1.1, C3.1,
  C2.x, C3.6, C4.6), which is where ledger I9's C4.5 item already points.
- **Singapore's two 0.0s are the closest calls of the group**, each reconciled from a blind 0.5 and each, taken alone,
  enough to move Singapore to Potentially Adequate on Sessions 71 and 72's changes.

## 10. Model and disclosure

Session 73 ran on Opus 5.5 at high, as routed. The readings are judgments on the stated sources; the record states
each one's method and source so a reader can re-read a unit. Nothing in this record is applied to a published file:
the generator session (S61) applies `blind_s73.FINAL` as a part of the pass after Sessions 71's and 72's.
