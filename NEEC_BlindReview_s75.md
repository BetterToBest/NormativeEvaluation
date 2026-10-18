# NEEC Blind Review, Session 75: C2.1, C2.4, C2.3 (configured economies) and C2.5

**Session 75 · 2026-10-18 · Stage 3b, the blind re-read (ledger S58; decisions 69.1, 69.2; ledger D52, D53, D54) ·
Scorer: Claude (Opus 5.5) · Owner: Duke Johnson**

Script: `blind_s75.py` (checked by the harness, which compares its output with `blind_s75_output.txt` and confirms
that this record carries every table it generates). Evidence: `evidence_cache_s75.py` (ten files, by digest) beside
Session 70's files for C2.1, C2.3 and C2.4, with `evidence_cache/C2.1/`, `C2.3/`, `C2.4/` and `C2.5/sources_s75.md`
naming the sources not cached. Nothing here changes a published score: the final readings are applied by generator in
ledger step S61 (STATE.md, "Next work").

## 1. Summary

Forty-one units were read on Opus 5.5 in two sets, kept apart.

- **First readings (18).** C2.1 Freedom from Coercion, C2.4 Democratic Participation and C2.3 Creative Development
  Opportunities for the six configured economies, whose clause 1 Session 65 held unmeasured (decision 65.2). Every
  clause was read, clause 1 for the first time, on data this session cached: the Gallup freedom share (World Happiness
  Report data application), IDEA's turnout export, the OECD Trust Survey's external-efficacy item and Time Use Database,
  and EU-SILC's meaning-of-life and artistic-practice tables. **No verdict moves once reconciled**: the 18 published
  verdicts stand, now with their clause statuses measured. Two first readings (China's and Qatar's C2.1, 0.5) differed
  from the held 0.0; each moves to the prior's 0.0 on evidence the first reading did not weigh (section 6).
- **Blind re-read of C2.5 Exit Rights and Mobility (23).** The 13 units Session 65 read (part (2.11)) and the 10 Session
  42 read on the pre-v2.0 four-clause list (part (b5)), on v2.0's three clauses. Blind against prior: 1 agree, 22
  revise (the ten part (b5) units revise on clause count alone where nothing else differs), **7 verdicts differ**.
  One moves to the prior's (MMT + Job Guarantee, 1.0 to 0.5: the blind reading's own flag names a dispute within the
  mechanism's literature, which protocol 2.1 places at 0.5); six stand.
- **Final against prior: six verdicts change, all on C2.5:** Centrally Planned Socialism 0.5 to 0.0 (exit and
  non-participation criminalised under the system's own law); Degrowth Economics, Fully Automated Luxury Communism,
  Market Socialism and Nordic Social Democracy 0.0 to 0.5 (the prior's 0.0 rested on the v1.4 band's "requires
  near-universal participation", which no source of these units shows as a bar to exit); Universal Basic Income 0.0 to
  1.0 (every clause cleared: no participation to leave, no condition, a portable payment). Each is flagged toward the
  prior's verdict. No CCO-PTF-CIP-SZH verdict changes (its C2.5 agrees at 0.5).
- **Consequence, once applied (S61):** four failures fewer. **One tier change, with the earlier groups:** Universal
  Basic Income from Structurally Inadequate to Partially Adequate (five failures after Sessions 71 to 75; this group's
  change alone leaves it at six). Ledger D57 asks the owner to confirm (section 9). First place is unchanged
  (Participatory Economics alone at 16.5 with the earlier groups' changes). Three flags would change a tier or first
  place (section 7).
- **Session 70's gaps, settled.** The OECD Trust Survey covers none of the United States, China, Singapore or Qatar
  (2021 and 2023 rounds): C2.4's clause 3 is structurally unmeasurable for them on the named series. The OECD Time Use
  Database (dataflow DF_TIME_USE) covers the United States, China and the four Nordic economies, not Singapore or Qatar.
  Neither gap moves a verdict: each criterion's other clauses already hold the economies at 0.5 or 0.0.

## 2. The blind step

The readings were written from `blind_review.blind_view()` (the v2.0 clause text and the cache file names), the
criteria's measurement text, the sources below, and committed and pushed as checkpoint `6fbcfed` ("NEEC checkpoint
s75: blind readings of C2.1, C2.4, C2.3 (configured economies) and C2.5 recorded, before the prior readings are
opened") before part (2.11)'s, part (b5)'s or part (a)'s readings of these units, Sessions 65's or 42's records, or the
units' published scores and rationales on these criteria were opened. `blind_s75.py` at that commit holds them
exactly: every reading, FIRST and NEW, is unchanged at the session's last commit (`git diff 6fbcfed -- blind_s75.py`
removes only the usage lines of the docstring and the checkpoint's closing print lines). After it were added the comparison,
the reconciliation (RECONCILE), one clause correction (CLAUSE_FIX), four flags toward the prior's verdict on standing
differences whose blind reading carried none (FLAGS), the reasons the standing differences stand (STAND) and the
consequences.

What the session had seen before recording, disclosed so a reader can weigh the blindness:

- **criteria.json's anchors**, which quote published (v1) examples, printed in full for the four criteria: C2.1,
  Universal Basic Income 1.0, Status Quo 0.5, Centrally Planned Socialism and Libertarian Minarchism 0.0; C2.3,
  Degrowth Economics 1.0, Status Quo 0.5, Centrally Planned Socialism 0.0; C2.4, Participatory Economics 1.0, Status
  Quo 0.5, Centrally Planned Socialism and FALC 0.0; C2.5, CCO-PTF-CIP-SZH 1.0, Status Quo 0.5, Nordic Social Democracy
  and Degrowth Economics 0.0, with the C2.5 note that "the failure mode is almost always funding or coherence dependent
  on near-universal participation". The first readings agree with the anchors on Status Quo (0.5, three criteria) and
  Centrally Planned Socialism (0.0, three criteria); a reader should weigh those six agreements accordingly. On C2.5 the
  blind reading departed from the anchors seen for Nordic Social Democracy and Degrowth Economics (0.5 against 0.0) and
  agreed for Status Quo.
- **STATE.md and the handoff**: decision 65.2's statement that C2.1, C2.4 and C2.3 were "held at their published scores
  ... because a 1.0 needs a clause no unit shows", which implies no configured economy is at 1.0 on them.
- **One prose line of a scoring document**: a filtered search of the Sovereign Wealth Fund Statism document (with every
  section and line naming C2.1, C2.3, C2.4 or C2.5 removed) displayed a line saying "a dividend or a bare UBI payment
  are (both correctly scored 0.0 here on" another criterion of that document's own (the accumulation criterion, not one
  of this group's). Every search of a scoring document or the Report excluded this group's criteria's sections and lines.
- **Session 70's notes** (`notes_s70.md` in C2.1, C2.3 and C2.4), which carry no scores; the cache indexes for these
  criteria hold no `index.json`.

After the checkpoint the session read Session 71's record (section 6) for Participatory Economics' allowance for those
who do not work, which corrects one C2.5 clause with no verdict effect (section 6).

## 3. Sources

Cached by `evidence_cache_s75.py` and verified by digest: the Gallup World Poll's "freedom to make life choices" share,
2005 to 2025, for the eight economies the configured entries cover (`C2.1/whr_freedom_s75.json`; the application's
API takes a token its own page computes, so the page was loaded in the container's headless Chromium and the call made
from inside it); IDEA's full turnout export, the eight economies' rows (`C2.4/idea_turnout_s75.json`); the OECD Trust
Survey's external-efficacy item for every country it covers (`C2.4/oecd_trust_pe_ext_s75.json`); IDEA's Democracy
Tracker on Qatar's November 2024 referendum (`C2.4/idea_dt_qatar_2024_11_extract.txt`); EU-SILC's artistic practice by
frequency (2015, 2022) and meaning-of-life rating (2013) for the four Nordic economies, and the OECD Time Use Database
(`C2.3/`); and passages of CCO-PTF-CIP-SZH's research hub at `8e8a6ba`, Integral's white paper v0.1 and the Libertarian
Party platform (`C2.5/`). The `sources_s75.md` files name the uncached sources each reading cites: the configured
economies' law (the US expatriation tax and benefit work conditions, the Nordic activation rules and EEA coordination,
the Soviet criminal code's articles 64 and 209 and the propiska, China's exit controls and hukou, Singapore's
Enlistment Act, CPF and HDB rules, Qatar's 2018 and 2020 labour laws), and the designs' and mechanisms' own literature
(Roemer, Schweickart, Albert and Hahnel, Kallis and Hickel, Bastani, Schwab, Raworth, George, Alaska Statutes
43.23.005, Van Parijs and Vanderborght, Coote and Percy, Tcherneva, Linton and North, Ostrom, AAOIFI). Finland's
citizens' initiative counts are by search, not a primary count, and say so.

## 4. Readings

The script's docstring states the method each reading applies (2.1.1 to 2.1.3, 2.4.1 to 2.4.4, 2.3.1 to 2.3.4, 2.5.1
to 2.5.5); in brief:

- **C2.1:** clause 1 is the Gallup freedom share at 2025, each Nordic economy separately; clause 2 (revealed
  preference) is not shown for any configured economy, so none can be 1.0; 0.0 where the configuration's own law
  substitutes state compulsion of comparable severity.
- **C2.4:** clause 1 is voting-age turnout at the latest parliamentary election, the voting-age population counting
  non-citizens (protocol 3.2); clause 2 is short where no national process of citizen-initiated proposals exists, as the
  measurement text says; clause 3 is not shown outside the OECD survey's coverage; 0.0 where no meaningful
  participation mechanism exists by design.
- **C2.3:** clause 1 is not shown where the only weekly-frequency survey covers part of the clause's activities;
  clause 2 is leisure hours a week (OECD); clause 3 is EU-SILC's meaning-of-life rating times ten; 0.0 for state
  control of cultural production under the system's own doctrine.
- **C2.5:** clause 1 asks what leaving the system's own arrangements costs under its own rules (for a mechanism that
  supplies an unconditional means of subsistence, the capacity it gives to leave other arrangements; out of reach for a
  tax or a fund); clause 2 asks whether its rules penalise non-participation (not receiving a voluntary scheme's
  benefits is not a penalty); clause 3 asks whether moving loses an essential benefit; 0.0 where the system excludes
  exit as illegitimate, or its own sources show its coherence requires near-universal participation. A design silent on
  exit whose coherence does not depend on participation is 0.5: silence is not clearance, and no 0.0 condition holds.

The figures quoted, recomputed by the script from the cache: Gallup freedom share 2025, United States 75.4%, China
67.6%, Singapore 86.9%, the Nordic economies 92.0% to 94.4%, Qatar 92.4% but last in 2012; voting-age turnout, United
States 59.2% (2024), Singapore 51.0% (2025; 92.8% of registered citizens), Denmark 73.3%, Finland 68.9%, Norway 73.1%,
Sweden 80.3%, Qatar's 2024 referendum at most 15.2% of the voting-age population; external efficacy (2023), Denmark
44.3%, Finland 20.9%, Norway 34.8%, Sweden 29.9%; leisure, 26.6 (China) to 41.3 (Norway) hours a week; meaning of life,
78 to 83; artistic practice daily or weekly (2022), 22.1% to 37.8%.

## 5. The readings, and the comparison

### Readings as recorded at the checkpoint

C2.1 (first readings):

| Unit | Clause statuses | Verdict | Flag |
|---|---|---|---|
| Centrally Planned Socialism | U U | 0.0 (0.0 reason stated) | — |
| Nordic Social Democracy | C U | 0.5 | — |
| State Capitalism / China (Party-State-Directed Market Economy) | S U | 0.5 | toward 0.0 |
| State Capitalism / Qatar (Gulf Rentier-Distributive Statism) | U U | 0.5 | toward 0.0 |
| State Capitalism / Singapore (GLC Developmental Capitalism) | C U | 0.5 | — |
| Status Quo Market Capitalism | C U | 0.5 | — |

C2.4 (first readings):

| Unit | Clause statuses | Verdict | Flag |
|---|---|---|---|
| Centrally Planned Socialism | S S U | 0.0 (0.0 reason stated) | — |
| Nordic Social Democracy | S S S | 0.5 | — |
| State Capitalism / China (Party-State-Directed Market Economy) | S S U | 0.0 (0.0 reason stated) | toward 0.5 |
| State Capitalism / Qatar (Gulf Rentier-Distributive Statism) | S S U | 0.0 (0.0 reason stated) | toward 0.5 |
| State Capitalism / Singapore (GLC Developmental Capitalism) | S S U | 0.5 | — |
| Status Quo Market Capitalism | S S U | 0.5 | — |

C2.3 (first readings):

| Unit | Clause statuses | Verdict | Flag |
|---|---|---|---|
| Centrally Planned Socialism | U U U | 0.0 (0.0 reason stated) | toward 0.5 |
| Nordic Social Democracy | U C C | 0.5 | — |
| State Capitalism / China (Party-State-Directed Market Economy) | U C U | 0.5 | toward 0.0 |
| State Capitalism / Qatar (Gulf Rentier-Distributive Statism) | U U U | 0.5 | — |
| State Capitalism / Singapore (GLC Developmental Capitalism) | U U U | 0.5 | — |
| Status Quo Market Capitalism | U C U | 0.5 | — |

C2.5 (blind readings):

| Unit | Clause statuses | Verdict | Flag |
|---|---|---|---|
| CCO-PTF-CIP-SZH | S C C | 0.5 | toward 1.0 |
| Centrally Planned Socialism | S S S | 0.0 (0.0 reason stated) | — |
| Degrowth Economics | U U U | 0.5 | toward 0.0 |
| Doughnut Economics | U U U | 0.5 | — |
| Fully Automated Luxury Communism | U U U | 0.5 | — |
| Georgism / Land Value Tax (LVT + Citizen's Dividend) | R C C | 0.5 | — |
| Integral | C U C | 0.5 | toward 1.0 |
| Islamic Finance / Profit-Sharing Banking | C C R | 0.5 | — |
| Libertarian Minarchism | C C C | 1.0 | toward 0.5 |
| MMT + Job Guarantee | C C C | 1.0 | toward 0.5 |
| Market Socialism | C S U | 0.5 | — |
| Mutual Credit / LETS | S C S | 0.5 | — |
| Nordic Social Democracy | C S C | 0.5 | toward 0.0 |
| Ostrom-Style Commons Governance | C C S | 0.5 | — |
| Participatory Economics | S S U | 0.5 | toward 0.0 |
| Sovereign Wealth Fund Statism | R S C | 0.5 | — |
| Stakeholder Capitalism | U U U | 0.5 | — |
| State Capitalism / China (Party-State-Directed Market Economy) | S S S | 0.5 | toward 0.0 |
| State Capitalism / Qatar (Gulf Rentier-Distributive Statism) | S S S | 0.5 | toward 0.0 |
| State Capitalism / Singapore (GLC Developmental Capitalism) | S S S | 0.5 | — |
| Status Quo Market Capitalism | C S S | 0.5 | — |
| Universal Basic Income | C C C | 1.0 | toward 0.5 |
| Universal Basic Services | C C U | 0.5 | toward 1.0 |

### Comparison with the readings the pass holds

The first readings are set against parts (2.11) and (a), whose clause 1 was held unmeasured; a clause difference there
is a measurement, not a disagreement. C2.5 is set against parts (2.11) and (b5).

C2.1:

| Unit | Part | Prior | First (Session 75) | Result | Differences |
|---|---|---|---|---|---|
| Centrally Planned Socialism | (2.11) | U U / 0.0 | U U / 0.0 | agree | — |
| Nordic Social Democracy | (a) | U U / 0.5 | C U / 0.5 | revise (clauses) | clause 1: U (prior) vs C (new) |
| State Capitalism / China (Party-State-Directed Market Economy) | (2.11) | U U / 0.0 | S U / 0.5 | revise (verdict) | clause 1: U (prior) vs S (new); verdict: 0.0 (prior) vs 0.5 (new) |
| State Capitalism / Qatar (Gulf Rentier-Distributive Statism) | (2.11) | U U / 0.0 | U U / 0.5 | revise (verdict) | verdict: 0.0 (prior) vs 0.5 (new) |
| State Capitalism / Singapore (GLC Developmental Capitalism) | (2.11) | U U / 0.5 | C U / 0.5 | revise (clauses) | clause 1: U (prior) vs C (new) |
| Status Quo Market Capitalism | (2.11) | U U / 0.5 | C U / 0.5 | revise (clauses) | clause 1: U (prior) vs C (new) |

C2.4:

| Unit | Part | Prior | First (Session 75) | Result | Differences |
|---|---|---|---|---|---|
| Centrally Planned Socialism | (2.11) | U U U / 0.0 | S S U / 0.0 | revise (clauses) | clause 1: U (prior) vs S (new); clause 2: U (prior) vs S (new) |
| Nordic Social Democracy | (a) | C S U / 0.5 | S S S / 0.5 | revise (clauses) | clause 1: C (prior) vs S (new); clause 3: U (prior) vs S (new) |
| State Capitalism / China (Party-State-Directed Market Economy) | (2.11) | U U U / 0.0 | S S U / 0.0 | revise (clauses) | clause 1: U (prior) vs S (new); clause 2: U (prior) vs S (new) |
| State Capitalism / Qatar (Gulf Rentier-Distributive Statism) | (2.11) | U U U / 0.0 | S S U / 0.0 | revise (clauses) | clause 1: U (prior) vs S (new); clause 2: U (prior) vs S (new) |
| State Capitalism / Singapore (GLC Developmental Capitalism) | (2.11) | U U U / 0.5 | S S U / 0.5 | revise (clauses) | clause 1: U (prior) vs S (new); clause 2: U (prior) vs S (new) |
| Status Quo Market Capitalism | (2.11) | U U U / 0.5 | S S U / 0.5 | revise (clauses) | clause 1: U (prior) vs S (new); clause 2: U (prior) vs S (new) |

C2.3:

| Unit | Part | Prior | First (Session 75) | Result | Differences |
|---|---|---|---|---|---|
| Centrally Planned Socialism | (2.11) | U U U / 0.0 | U U U / 0.0 | agree | — |
| Nordic Social Democracy | (a) | U C U / 0.5 | U C C / 0.5 | revise (clauses) | clause 3: U (prior) vs C (new) |
| State Capitalism / China (Party-State-Directed Market Economy) | (2.11) | U U U / 0.5 | U C U / 0.5 | revise (clauses) | clause 2: U (prior) vs C (new) |
| State Capitalism / Qatar (Gulf Rentier-Distributive Statism) | (2.11) | U U U / 0.5 | U U U / 0.5 | agree | — |
| State Capitalism / Singapore (GLC Developmental Capitalism) | (2.11) | U U U / 0.5 | U U U / 0.5 | agree | — |
| Status Quo Market Capitalism | (2.11) | U U U / 0.5 | U C U / 0.5 | revise (clauses) | clause 2: U (prior) vs C (new) |

C2.5:

| Unit | Part | Prior | Blind (Session 75) | Result | Differences |
|---|---|---|---|---|---|
| CCO-PTF-CIP-SZH | (b5) | S C C C / 0.5 | S C C / 0.5 | revise (clauses) | clause count 4 (prior) vs 3 (new) |
| Centrally Planned Socialism | (2.11) | U U U / 0.5 | S S S / 0.0 | revise (verdict) | clause 1: U (prior) vs S (new); clause 2: U (prior) vs S (new); clause 3: U (prior) vs S (new); verdict: 0.5 (prior) vs 0.0 (new) |
| Degrowth Economics | (2.11) | U U U / 0.0 | U U U / 0.5 | revise (verdict) | verdict: 0.0 (prior) vs 0.5 (new) |
| Doughnut Economics | (b5) | C C C U / 0.5 | U U U / 0.5 | revise (clauses) | clause count 4 (prior) vs 3 (new) |
| Fully Automated Luxury Communism | (2.11) | U U U / 0.0 | U U U / 0.5 | revise (verdict) | verdict: 0.0 (prior) vs 0.5 (new) |
| Georgism / Land Value Tax (LVT + Citizen's Dividend) | (b5) | C U C R / 0.5 | R C C / 0.5 | revise (clauses) | clause count 4 (prior) vs 3 (new) |
| Integral | (b5) | C U C C / 0.5 | C U C / 0.5 | revise (clauses) | clause count 4 (prior) vs 3 (new) |
| Islamic Finance / Profit-Sharing Banking | (b5) | C U R R / 0.5 | C C R / 0.5 | revise (clauses) | clause count 4 (prior) vs 3 (new) |
| Libertarian Minarchism | (b5) | C C C C / 1.0 | C C C / 1.0 | revise (clauses) | clause count 4 (prior) vs 3 (new) |
| MMT + Job Guarantee | (2.11) | U U U / 0.5 | C C C / 1.0 | revise (verdict) | clause 1: U (prior) vs C (new); clause 2: U (prior) vs C (new); clause 3: U (prior) vs C (new); verdict: 0.5 (prior) vs 1.0 (new) |
| Market Socialism | (2.11) | U U U / 0.0 | C S U / 0.5 | revise (verdict) | clause 1: U (prior) vs C (new); clause 2: U (prior) vs S (new); verdict: 0.0 (prior) vs 0.5 (new) |
| Mutual Credit / LETS | (b5) | C C U C / 0.5 | S C S / 0.5 | revise (clauses) | clause count 4 (prior) vs 3 (new) |
| Nordic Social Democracy | (2.11) | U U U / 0.0 | C S C / 0.5 | revise (verdict) | clause 1: U (prior) vs C (new); clause 2: U (prior) vs S (new); clause 3: U (prior) vs C (new); verdict: 0.0 (prior) vs 0.5 (new) |
| Ostrom-Style Commons Governance | (b5) | C U S U / 0.5 | C C S / 0.5 | revise (clauses) | clause count 4 (prior) vs 3 (new) |
| Participatory Economics | (2.11) | U U U / 0.5 | S S U / 0.5 | revise (clauses) | clause 1: U (prior) vs S (new); clause 2: U (prior) vs S (new) |
| Sovereign Wealth Fund Statism | (b5) | C C C R / 0.5 | R S C / 0.5 | revise (clauses) | clause count 4 (prior) vs 3 (new) |
| Stakeholder Capitalism | (2.11) | U U U / 0.5 | U U U / 0.5 | agree | — |
| State Capitalism / China (Party-State-Directed Market Economy) | (2.11) | U U U / 0.5 | S S S / 0.5 | revise (clauses) | clause 1: U (prior) vs S (new); clause 2: U (prior) vs S (new); clause 3: U (prior) vs S (new) |
| State Capitalism / Qatar (Gulf Rentier-Distributive Statism) | (2.11) | U U U / 0.5 | S S S / 0.5 | revise (clauses) | clause 1: U (prior) vs S (new); clause 2: U (prior) vs S (new); clause 3: U (prior) vs S (new) |
| State Capitalism / Singapore (GLC Developmental Capitalism) | (2.11) | U U U / 0.5 | S S S / 0.5 | revise (clauses) | clause 1: U (prior) vs S (new); clause 2: U (prior) vs S (new); clause 3: U (prior) vs S (new) |
| Status Quo Market Capitalism | (2.11) | U U U / 0.5 | C S S / 0.5 | revise (clauses) | clause 1: U (prior) vs C (new); clause 2: U (prior) vs S (new); clause 3: U (prior) vs S (new) |
| Universal Basic Income | (2.11) | U U U / 0.0 | C C C / 1.0 | revise (verdict) | clause 1: U (prior) vs C (new); clause 2: U (prior) vs C (new); clause 3: U (prior) vs C (new); verdict: 0.0 (prior) vs 1.0 (new) |
| Universal Basic Services | (b5) | C U C R / 0.5 | C C U / 0.5 | revise (clauses) | clause count 4 (prior) vs 3 (new) |

Nordic Social Democracy's C2.4 clause 1 is the one clause the prior had cleared (part (a), Session 37) and the first
reading finds short: Finland's voting-age turnout at its 2023 parliamentary election was 68.9%. The verdict is 0.5 on
both.

## 6. Reconciliation of the nine verdict differences

A new verdict stands unless the prior reading shows evidence the new reading did not weigh, or the new reading departs
from its own stated reading (Session 71's rule). The reconciliation moves a verdict only toward the prior's, and says
why; where it does, the new verdict is kept as the flag.

**Moved to the prior's (three):**

- **China, C2.1: 0.5 (first reading), prior 0.0; moves to 0.0.** The prior (the China scoring document, C2.1) cites
  the state-mandated labour-transfer programme that places Uyghur, Tibetan and other minority workers into jobs under
  surveillance with no real choice to refuse (UN human rights experts, January 2026; Xinjiang's 2021-2025 plan projected
  13.75 million transfers), and the bar on unions outside the party-affiliated federation. The first reading did not
  weigh them. Labour directed by the state with no real choice to refuse is reading 2.1.3's substituted compulsion, and
  the configuration keeps market compulsion beside it. Flagged toward 0.5 (the Gallup share of 67.6%, near the bar).
- **Qatar, C2.1: 0.5 (first reading), prior 0.0; moves to 0.0.** The prior shows that non-citizens have no safety net,
  so that losing a job means losing both income and, usually, the right to stay: the 0.0 band's "maximizes economic
  coercion by design" for the population the protocol counts. The first reading weighed the employer tie and flagged
  toward 0.0; the prior's evidence settles the flag. Flagged toward 0.5 (the 2018 and 2020 reforms in law).
- **MMT + Job Guarantee, C2.5: 1.0 (blind), prior 0.5; moves to 0.5.** The blind reading's own flag names a dispute
  within the mechanism's literature on clause 2: in Tcherneva's design the job offer adds to income support; in the
  buffer-stock proposals it replaces unemployment benefit for those able to work, so declining it costs income.
  Protocol 2.1 places genuinely ambiguous sources at 0.5, flagged, and the blind reading's 1.0 departs from that; clause
  2 becomes "not shown". The prior's point, that the guarantee offers exit from a job but not from employment, is the
  same dispute seen from the other side. Flagged toward 1.0.

**Standing (six), each flagged toward the prior's verdict:**

- **Centrally Planned Socialism, C2.5: 0.0 (blind), prior 0.5; stands.** The prior states that international exit was
  "essentially prohibited" and gives "slight credit for formal job assignment". The blind reading weighed both; a
  system whose own law makes flight abroad treason and non-work a crime excludes exit as illegitimate (reading 2.5.4).
- **Degrowth Economics, C2.5: 0.5 (blind), prior 0.0; stands.** The prior's 0.0 rests on the v1.4 band's reading
  (ecological compliance needs comprehensive participation; a high-consumption minority would break it), which the
  blind reading weighed and flagged. Caps that bind every resident are laws, not a participation one could leave, and
  the sources state no exit terms, so no 0.0 condition is shown.
- **Fully Automated Luxury Communism, C2.5: 0.5 (blind), prior 0.0; stands.** The prior asserts that the automation
  infrastructure "cannot function with partial participation", citing no source; Bastani states no participation
  requirement or exit terms, so the design is silent, which reading 2.5.4 holds at 0.5.
- **Market Socialism, C2.5: 0.5 (blind), prior 0.0; stands.** The prior rests on "comprehensive adoption to function
  optimally" and on workers in traditional firms lacking cooperative benefits. The second is the blind reading's
  clause 2 shortfall; the first is optimality, not a structural requirement: Schweickart keeps a bounded capitalist
  sector.
- **Nordic Social Democracy, C2.5: 0.5 (blind), prior 0.0; stands.** The prior rests on the funding model's need for
  near-universal participation ("cannot function with 30% opt-out"), which the blind reading weighed and flagged.
  Residents leave the tax base only by emigrating, which is free under the configuration's rules, so the counterfactual
  opt-out is not an exit right the system denies.
- **Universal Basic Income, C2.5: 1.0 (blind), prior 0.0; stands.** The prior rests on the funding model's need for
  universal participation. The payment's level is set at the highest sustainable level (Van Parijs and Vanderborght),
  so the design adapts to participation rather than collapsing; the question is the payment's sustainability (domains
  1 and 5), not a penalty on exit. Every clause is cleared on readings 2.5.1 to 2.5.3. The flag toward 0.0 records the
  prior's reading; the blind reading's own flag (toward 0.5: reach, or newcomer waiting periods) is set aside for it.

**One clause correction, no verdict effect:** Participatory Economics' C2.5 clause 2, short to cleared. Session 71's
record (section 6) quotes the design's "consumption allowance for people who simply don't want to work", at a level
meeting basic needs (Hahnel and Wright, 2016), so non-participants are not penalised. The verdict stays 0.5 (clause 1
short: no arrangement within the economy to leave for).

### Final readings

C2.1:

| Unit | Clause statuses | Verdict | Flag |
|---|---|---|---|
| Centrally Planned Socialism | U U | 0.0 (0.0 reason stated) | — |
| Nordic Social Democracy | C U | 0.5 | — |
| State Capitalism / China (Party-State-Directed Market Economy) | S U | 0.0 (0.0 reason stated) | toward 0.5 |
| State Capitalism / Qatar (Gulf Rentier-Distributive Statism) | U U | 0.0 (0.0 reason stated) | toward 0.5 |
| State Capitalism / Singapore (GLC Developmental Capitalism) | C U | 0.5 | — |
| Status Quo Market Capitalism | C U | 0.5 | — |

C2.4:

| Unit | Clause statuses | Verdict | Flag |
|---|---|---|---|
| Centrally Planned Socialism | S S U | 0.0 (0.0 reason stated) | — |
| Nordic Social Democracy | S S S | 0.5 | — |
| State Capitalism / China (Party-State-Directed Market Economy) | S S U | 0.0 (0.0 reason stated) | toward 0.5 |
| State Capitalism / Qatar (Gulf Rentier-Distributive Statism) | S S U | 0.0 (0.0 reason stated) | toward 0.5 |
| State Capitalism / Singapore (GLC Developmental Capitalism) | S S U | 0.5 | — |
| Status Quo Market Capitalism | S S U | 0.5 | — |

C2.3:

| Unit | Clause statuses | Verdict | Flag |
|---|---|---|---|
| Centrally Planned Socialism | U U U | 0.0 (0.0 reason stated) | toward 0.5 |
| Nordic Social Democracy | U C C | 0.5 | — |
| State Capitalism / China (Party-State-Directed Market Economy) | U C U | 0.5 | toward 0.0 |
| State Capitalism / Qatar (Gulf Rentier-Distributive Statism) | U U U | 0.5 | — |
| State Capitalism / Singapore (GLC Developmental Capitalism) | U U U | 0.5 | — |
| Status Quo Market Capitalism | U C U | 0.5 | — |

C2.5:

| Unit | Clause statuses | Verdict | Flag |
|---|---|---|---|
| CCO-PTF-CIP-SZH | S C C | 0.5 | toward 1.0 |
| Centrally Planned Socialism | S S S | 0.0 (0.0 reason stated) | toward 0.5 |
| Degrowth Economics | U U U | 0.5 | toward 0.0 |
| Doughnut Economics | U U U | 0.5 | — |
| Fully Automated Luxury Communism | U U U | 0.5 | toward 0.0 |
| Georgism / Land Value Tax (LVT + Citizen's Dividend) | R C C | 0.5 | — |
| Integral | C U C | 0.5 | toward 1.0 |
| Islamic Finance / Profit-Sharing Banking | C C R | 0.5 | — |
| Libertarian Minarchism | C C C | 1.0 | toward 0.5 |
| MMT + Job Guarantee | C U C | 0.5 | toward 1.0 |
| Market Socialism | C S U | 0.5 | toward 0.0 |
| Mutual Credit / LETS | S C S | 0.5 | — |
| Nordic Social Democracy | C S C | 0.5 | toward 0.0 |
| Ostrom-Style Commons Governance | C C S | 0.5 | — |
| Participatory Economics | S C U | 0.5 | toward 0.0 |
| Sovereign Wealth Fund Statism | R S C | 0.5 | — |
| Stakeholder Capitalism | U U U | 0.5 | — |
| State Capitalism / China (Party-State-Directed Market Economy) | S S S | 0.5 | toward 0.0 |
| State Capitalism / Qatar (Gulf Rentier-Distributive Statism) | S S S | 0.5 | toward 0.0 |
| State Capitalism / Singapore (GLC Developmental Capitalism) | S S S | 0.5 | — |
| Status Quo Market Capitalism | C S S | 0.5 | — |
| Universal Basic Income | C C C | 1.0 | toward 0.0 |
| Universal Basic Services | C C U | 0.5 | toward 1.0 |

## 7. Consequences once applied (not applied here)

Totals on the 29 criteria and failures, with this group's six changes alone and on top of Sessions 71 to 74's final
changes (`blind_s71.FINAL` to `blind_s74.FINAL`, with `blind_s74.EXTRA_FINAL`), from `neec_scores_v2.csv`; nothing is
written:

| Entry | Total on 29 | After this group | After Sessions 71 to 75 | Failures | After all five | Tier after all five |
|---|---:|---:|---:|---:|---:|---|
| Nordic Social Democracy | 15.0 | 15.5 | 15.5 | 1 | 0 | Potentially Adequate |
| Centrally Planned Socialism | 7.5 | 7.0 | 6.5 | 15 | 17 | Structurally Inadequate |
| Market Socialism | 14.5 | 15.0 | 15.0 | 2 | 1 | Potentially Adequate |
| Libertarian Minarchism | 8.5 | 8.5 | 9.5 | 13 | 11 | Structurally Inadequate |
| Universal Basic Income | 12.0 | 13.0 | 13.5 | 7 | 5 | Partially Adequate |
| Degrowth Economics | 14.5 | 15.0 | 15.0 | 2 | 1 | Potentially Adequate |
| Stakeholder Capitalism | 10.5 | 10.5 | 11.0 | 8 | 7 | Structurally Inadequate |
| Fully Automated Luxury Communism | 10.5 | 11.0 | 11.0 | 10 | 9 | Structurally Inadequate |
| Participatory Economics | 16.0 | 16.0 | 16.5 | 0 | 0 | Potentially Adequate |
| Doughnut Economics | 10.5 | 10.5 | 9.5 | 8 | 10 | Structurally Inadequate |
| Sovereign Wealth Fund Statism | 14.5 | 14.5 | 15.0 | 3 | 2 | Potentially Adequate |
| State Capitalism / China (Party-State-Directed Market Economy) | 10.5 | 10.5 | 11.0 | 9 | 8 | Structurally Inadequate |
| State Capitalism / Singapore (GLC Developmental Capitalism) | 13.0 | 13.0 | 13.5 | 4 | 3 | Partially Adequate |
| State Capitalism / Qatar (Gulf Rentier-Distributive Statism) | 10.5 | 10.5 | 10.0 | 9 | 10 | Structurally Inadequate |
| Islamic Finance / Profit-Sharing Banking | 13.0 | 13.0 | 14.0 | 5 | 3 | Partially Adequate |

Each flagged final reading's alternative taken alone, on all five groups' final verdicts:

| Unit | Criterion | Final | Flag toward | Total on 29 then | Failures then | Tier then | Changes |
|---|---|---:|---:|---:|---:|---|---|
| State Capitalism / China (Party-State-Directed Market Economy) | C2.1 | 0.0 | 0.5 | 11.5 | 7 | Structurally Inadequate | — |
| State Capitalism / Qatar (Gulf Rentier-Distributive Statism) | C2.1 | 0.0 | 0.5 | 10.5 | 9 | Structurally Inadequate | — |
| Centrally Planned Socialism | C2.3 | 0.0 | 0.5 | 7.0 | 16 | Structurally Inadequate | — |
| State Capitalism / China (Party-State-Directed Market Economy) | C2.3 | 0.5 | 0.0 | 10.5 | 9 | Structurally Inadequate | — |
| State Capitalism / China (Party-State-Directed Market Economy) | C2.4 | 0.0 | 0.5 | 11.5 | 7 | Structurally Inadequate | — |
| State Capitalism / Qatar (Gulf Rentier-Distributive Statism) | C2.4 | 0.0 | 0.5 | 10.5 | 9 | Structurally Inadequate | — |
| CCO-PTF-CIP-SZH | C2.5 | 0.5 | 1.0 | 16.5 | 0 | Potentially Adequate | first place: shared |
| Centrally Planned Socialism | C2.5 | 0.0 | 0.5 | 7.0 | 16 | Structurally Inadequate | — |
| Degrowth Economics | C2.5 | 0.5 | 0.0 | 14.5 | 2 | Potentially Adequate | — |
| Fully Automated Luxury Communism | C2.5 | 0.5 | 0.0 | 10.5 | 10 | Structurally Inadequate | — |
| Integral | C2.5 | 0.5 | 1.0 | 16.0 | 2 | Potentially Adequate | — |
| Libertarian Minarchism | C2.5 | 1.0 | 0.5 | 9.0 | 11 | Structurally Inadequate | — |
| MMT + Job Guarantee | C2.5 | 0.5 | 1.0 | 13.0 | 4 | Partially Adequate | — |
| Market Socialism | C2.5 | 0.5 | 0.0 | 14.5 | 2 | Potentially Adequate | — |
| Nordic Social Democracy | C2.5 | 0.5 | 0.0 | 15.0 | 1 | Potentially Adequate | — |
| Participatory Economics | C2.5 | 0.5 | 0.0 | 16.0 | 1 | Potentially Adequate | first place: shared |
| State Capitalism / China (Party-State-Directed Market Economy) | C2.5 | 0.5 | 0.0 | 10.5 | 9 | Structurally Inadequate | — |
| State Capitalism / Qatar (Gulf Rentier-Distributive Statism) | C2.5 | 0.5 | 0.0 | 9.5 | 11 | Structurally Inadequate | — |
| Universal Basic Income | C2.5 | 1.0 | 0.0 | 12.5 | 6 | Structurally Inadequate | tier: Partially Adequate to Structurally Inadequate |
| Universal Basic Services | C2.5 | 0.5 | 1.0 | 13.5 | 4 | Partially Adequate | — |

Three flags would change a tier or first place: Universal Basic Income's C2.5 flag toward 0.0 would return it to
Structurally Inadequate; CCO-PTF-CIP-SZH's toward 1.0 would bring it level with Participatory Economics at 16.5; and
Participatory Economics' toward 0.0 would bring it down to share first place at 16.0. The first two are the units the
owner's rules already single out (decision 69.4 for CCO: a rise is applied when the blind re-read confirms it, and this
one is a flag, not a reading; D57 for UBI).

## 8. Anchors

Once applied, C2.5's v1 anchor examples move: Nordic Social Democracy and Degrowth Economics, the 0.0 band's two
examples, are 0.5, so the band would be left with no corpus example at 0.0 except Centrally Planned Socialism, which
the band does not cite; CCO-PTF-CIP-SZH, the 1.0 band's example, was already 0.5. The anchors describe and do not
govern (protocol 2.3(g)); S61's generator reports the anchor examples moved, and the limits page (S44) should say that
C2.5's bands describe v1.4's readings.

## 9. Decisions (Session 75)

- **75.1** (optional, method) readings 2.1.1 to 2.1.3, 2.4.1 to 2.4.4, 2.3.1 to 2.3.4 and 2.5.1 to 2.5.5 (section 4).
- **75.2** (corrections, no verdict effect) the 18 first readings of C2.1, C2.4 and C2.3 for the configured economies:
  clause 1 measured for the first time, every clause status recorded; China's and Qatar's C2.1 reconciled to the
  prior's 0.0. Decision 65.2's holds stand as verdicts.
- **75.3** (corrections) the six C2.5 verdict changes of section 6, each flagged toward the prior's verdict.
- **75.4** (corrections, no verdict effect) the C2.5 clause statuses of section 5, the ten part (b5) units moved to
  v2.0's three clauses, MMT + Job Guarantee reconciled to the prior's 0.5, and Participatory Economics' clause 2.
- **75.5** (optional, tooling) `evidence_cache_s75.py`, `blind_s75.py` and harness v45.
- **Ledger D57** (for the owner; default yes): apply the six C2.5 changes at S61 as read, including Universal Basic
  Income's 0.0 to 1.0, which with Sessions 71 to 74's changes moves it from Structurally Inadequate to Partially
  Adequate (flagged toward 0.0, which would undo the tier change).

## 10. Observations for later sessions

- **Session 70's two gaps** are settled: C2.4's clause 3 has no named measure for the four economies outside Europe
  (the OECD survey and the ESS reach none of them), and C2.3's clause 2 is measurable for six of the eight economies on
  the OECD's current dataflow. The limits page (S44) should state the first as structural.
- **v1.4's "near-universal participation" reading.** The prior held six C2.5 units at 0.0 on the band's v1.4 text
  (funding or coherence dependent on participation) without a source showing it. On v2.0's clauses that reading is a
  flag, not a score; the Report (S41) should say so where it describes C2.5.
- **The WHR application's data** is reachable from a headless browser; `evidence_cache_s75.py` shows how, for C2.1's
  later use.
- **Mechanisms.** No mechanism is at 0.0 on C2.5 on either reading. Two (Georgism, Sovereign Wealth Fund Statism) hold
  a clause out of reach (a tax and a fund are not arrangements one leaves), one (Islamic finance) holds clause 3 out of
  reach.
- Open item (e) (ledger I9) is unchanged: this group touches neither C4.5 nor C3.4.

## 11. Model and disclosure

Read on Opus 5.5 at high, as the routing sends a judgment group (STATE.md, "Model routing"). The disclosures of section
2 bear on six first-reading agreements with the anchors seen (Status Quo's and Centrally Planned Socialism's C2.1, C2.4
and C2.3) and on decision 65.2's implication that no configured economy reaches 1.0 on these criteria, which the
readings bear out on their own clauses (C2.1's clause 2, C2.4's clauses 2 and 3, C2.3's clause 1 are unshown or short
throughout).
