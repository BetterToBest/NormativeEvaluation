# NEEC Blind Review, Session 77: C2.6, C3.6 and C4.6 for the six configured economies

**Session 77 · 2026-10-18 · Stage 3b, the blind re-read (ledger S60; decisions 69.1, 69.2; ledger D52, D53) ·
Scorer: Claude (Opus 5.5) · Owner: Duke Johnson**

Script: `blind_s77.py` (checked by the harness, which compares its output with `blind_s77_output.txt` and confirms
that this record carries every table it generates). Evidence: `evidence_cache_s77.py` (21 files by digest: Freedom
House's and V-Dem's series, Freedom in the World 2026's country pages, the law in force of eight jurisdictions, Penn
World Table 11.0, the World Bank's Poverty and Inequality Platform, a transcription of Easterly and Fischer's tables, the
OECD's GBD 2019 mortality dataset, the WHO's poisoning series), beside Session 65's WJP file and Session 70's files, with
`evidence_cache/C2.6/`, `C3.6/` and `C4.6/sources_s77.md` naming what is cited but not cached or was not reached.
Nothing here changes a published score: the final readings are applied by generator in ledger step S61 (STATE.md,
"Next work").

## 1. Summary

Eighteen units were read on Opus 5.5: C2.6 Civil Liberties and Rule of Law, C3.6 Productive and Innovative Capacity and
C4.6 Harm Internalization, the three criteria v2.0 added (class N), for the six configured national economies (Status
Quo Market Capitalism, the United States; Nordic Social Democracy, Denmark, Finland, Norway and Sweden; Centrally
Planned Socialism, the Soviet Union on its late record; State Capitalism in China, Singapore and Qatar). Session 65
(part (2.11), Sonnet 5.5) had read them on Freedom House's 1-7 rating and Penn World Table 10.01, with C2.6's and
C4.6's law-in-force clauses and C4.6's mortality clause not shown for any economy and C3.6's clause 3 not assessed (open
item (c), ledger I6).

- **The law in force was read** for the United States, Denmark, Finland, Sweden, Norway (consent only: lovdata.no
  refused the container), the Soviet Union (the Fundamentals of Health Legislation, 1969), China and Singapore; Qatar's
  statutes could not be reached (almeezan.qa serves a client-rendered application). **Easterly and Fischer (1995)** was
  read as page images and its tables transcribed. **C4.6's mortality clause** was read on the GBD's risk-attributable
  rates through the OECD's GBD 2019 dataset (the WHO's SDG series give single years), crude rates, 1999 to 2019.
- **Blind against prior: all 18 revise; four verdicts differ, all on C3.6** (section 6). Every blind reading stands
  under Session 71's rule.
- **Final against prior: four verdict changes, all upward.** C3.6: Status Quo Market Capitalism, State Capitalism /
  China and State Capitalism / Singapore 0.5 to 1.0 (clause 3, which the prior did not assess, cleared; Singapore's TFP
  rising on PWT 11.0 where PWT 10.01 had it falling); Centrally Planned Socialism 0.0 to 0.5 (output per worker rose in
  1970-87, so clause 1 is cleared and D28(f) bars 0.0, although TFP fell, the 0.0 band's case, which is flagged).
  C2.6 and C4.6 keep every verdict: their clause statuses now rest on the law in force and the mortality series.
- **Consequence once applied (S61):** Status Quo, China and Singapore each +0.5, Centrally Planned Socialism +0.5 with
  one failure fewer; no tier or first-place change, alone or with Sessions 71 to 76 (Participatory Economics stays first
  alone at 16.5). **Eight flags**, none of which would change a tier or first place (section 7).
- **No CCO-PTF-CIP-SZH unit** is in this group.

## 2. The blind step

The readings were written from `blind_review.blind_view()` (the v2.0 clause text and the cache file names), the
criteria's measurement text, and the sources below, and committed and pushed as checkpoint `3cdf73d` ("NEEC checkpoint
s77: blind readings of C2.6, C3.6 and C4.6 for the six configured economies recorded, before the prior readings are
opened"), after two partial checkpoints (`2a12fe0`, C2.6; `f069602`, C3.6), before part (2.11)'s readings of these units
(`rescoring_s65.NEW_UNITS`), Session 65's record, or the units' published rationales on these criteria were opened.
`git diff 3cdf73d -- blind_s77.py` adds the comparison and what follows it, the docstring's comparison paragraph and
usage, and the last line of `main()`; no reading changed.

What the session had seen before recording, disclosed so a reader can weigh the blindness:

- **The prior's form, from STATE.md, Handoff 76 and the ledger.** Their task text says the priors read clause 1 on
  Freedom House's 1-7 rating, that the law-in-force clauses and C4.6's mortality clause were "not shown for any
  economy" (ledger I6, item (c)), and that Centrally Planned Socialism's C3.6 rests on Easterly and Fischer (1995); and
  Session 70's `C4.6/notes_s70.md` quotes STATE.md's "clause 1 is not shown for any economy". So the prior's status of
  C2.6's clauses 2 and 3 and C4.6's clause 1 (not shown) was known for all six; its verdicts and other clauses were not.
- **Decision 47.1's indicative consequence** (`NEEC_Criteria_v2_s45.md`), read to find the stated date of the historical
  configuration: the 2025 WJP sub-factor 6.2 values of the seven current economies and that the Index does not cover the
  Soviet Union. These are the data clause 3 reads, not a reading.
- **A published total.** `evidence/cps.md`'s header, opened to find the Soviet configuration's stated date, gives
  Centrally Planned Socialism's total on the 29 (7.5, 15 failures, rank 23 of 23); no criterion row of these three was
  read.
- **Session 76's reading 3.6.1**, which lists the four market economies whose PWT 10.01 output per hour and TFP rose in
  1999-2019 (the United States, Denmark, Finland, Sweden).
- **criteria.json** for C2.6, C3.6, C4.6 and C1.1, printed in full; the class N anchors carry no examples.

After the checkpoint, and disclosed: the Poverty and Inequality Platform file gained its Societal Poverty Rate column
(`spr`), used only for the flag on Status Quo's C3.6 (section 6); the raw pages' digests in the extracts' headers vary
from fetch to fetch on pages served dynamically (Freedom House, Wikisource, Singapore Statutes Online), while the
passages are identical, so a re-fetch reproduces the passages, not the headers.

## 3. Sources

Cached (`evidence_cache_s77.py`, each file's md5 in its FILES). For C2.6: `owid_fh_civil_liberties_score_s77.csv`,
`owid_fh_civil_liberties_rating_su_s77.csv`, `owid_vdem_civil_liberties_s77.csv`, `fh_fiw2026_cl_f1_extract.txt`, and
the law-in-force extracts `us_`, `dk_`, `fi_`, `se_`, `no_`, `su_`, `cn_` and `sg_law_c26_extract.txt`. For C3.6:
`pwt110_selected_economies.csv`, `pip_spl_selected_economies.csv`, `easterly_fischer_1995_tables_s77.csv` (transcribed
from Session 70's scanned PDF, pages 40, 43 and 44). For C4.6: `oecd_exp_morsc_gbd2019_s77.csv`,
`who_gho_sdgpoison_s77.csv`, `us_law_c46_extract.txt`, `nordic_law_c46_extract.txt`, `cn_law_c46_extract.txt`,
`su_environment_c46_extract.txt`; Session 65's `wjp_rol_sf62_2012_2025.csv` for clause 3. Session 70's US CFR sections
(federal quarantine) are read with the United States' C2.6 extract.

Not cached or not reached (`sources_s77.md` in each directory): Qatar's statutes (almeezan.qa); Norway's compulsion
and pollution-liability acts (lovdata.no, HTTP 405); Singapore's consent law (common law, *Hii Chii Kok v Ooi Peng Jin*,
2017); the GBD's own results tool (registration) and Our World in Data's GBD charts (non-redistributable); the
Conference Board's Total Economy Database (registration); V-Dem's PanDem index and the Oxford tracker (not needed, the
law in force deciding every clause 3); the Nordic group-action statutes; any claim decided and paid within the window.

## 4. Readings

`blind_s77.py`'s docstring states each reading in full. In short:

- **C2.6.** 2.6.1: Freedom House's civil-liberties score for 2025 (Freedom in the World 2026), cross-checked against
  V-Dem; the Soviet configuration on Freedom House's 1-7 rating over the planned economy's last years before the
  reforms of 1987-88, ratings 6 and 7 being the 0.0 band's 16 or less. 2.6.2: consent cleared on a statute, code or
  constitutional provision requiring consent in general and protecting refusal, its exceptions being emergency and
  compulsion under statutes with a time limit and a court; short where consent covers only some interventions or the
  law permits admission on another's consent. 2.6.3: compulsion cleared only where every measure is statutory, lapses at
  a stated time and is open to a court, with no standing requirement penalising refusal; short otherwise, and short
  where Freedom House scores the judiciary's independence (F1) at 0 or 1. 2.6.4: the band's case.
- **C3.6.** 3.6.1: PWT 11.0, 2003-2023 (output per hour on rgdpna, TFP on rtfpna); the Soviet configuration on Easterly
  and Fischer's Western estimates to 1987 (output per worker; growth-accounting TFP, with the CES estimates as the
  alternative). 3.6.2: clause 3 cleared where mean income or consumption per person exceeds C1.1's Societal Poverty Line
  at the economy's actual hours (for Singapore, output per person against the highest line its median could set).
  3.6.3: the band's case, never with a clause cleared (D28(f)).
- **C4.6.** 4.6.1: the GBD's crude rates (OECD), ambient and household air pollution and unsafe water, sanitation and
  handwashing, plus the WHO's unintentional poisoning, 1999 to 2019; a fall in a crude rate is a fall in the
  standardized one. 4.6.2: liability cleared only with an independent court, collective standing, no immunity shifting a
  class of harm to public funds, and a named claim decided and paid; short on such an immunity or F1 at 0 or 1; not
  shown where no claim is named. 4.6.3: the WJP's sub-factor 6.2, 2025, against 0.77. 4.6.4: the band's case.

## 5. The readings, and the comparison

The figures the readings quote, recomputed from the cache by `blind_s77.py`:

- Freedom House civil-liberties score, 2025 (FIW 2026): USA 49; DNK 57; FIN 60; NOR 60; SWE 59; CHN 11; SGP 29; QAT 18
- Freedom House civil-liberties score, 2024 (FIW 2025): USA 50; DNK 57; FIN 60; NOR 60; SWE 59; CHN 11; SGP 29; QAT 18
- V-Dem Civil Liberties Index, 2025: USA 0.826; DNK 0.959; FIN 0.947; NOR 0.947; SWE 0.960; CHN 0.179; SGP 0.717; QAT 0.357
- Freedom House question F1 (independent judiciary), FIW 2026: USA 3; DNK 4; FIN 4; NOR 4; SWE 4; CHN 1; SGP 1; QAT 1
- Freedom House civil-liberties rating (1-7), USSR: 1972-1979 6; 1980-1986 7; 1987 6; 1988-1989 5; 1990 4
- V-Dem Civil Liberties Index, Soviet Union (V-Dem's Russia), 1960-1984, range: 0.145 to 0.150
- PWT 11.0, output per hour, compound % a year, 2003-2023: USA +1.30; DNK +1.07; FIN +0.61; NOR +0.22; SWE +0.91; CHN +8.18; SGP +2.31; QAT -1.22 (2005-2023)
- PWT 11.0, TFP (rtfpna), compound % a year, 2003-2023: USA +0.45; DNK +0.18; FIN -0.38; NOR -0.78; SWE +0.18; CHN +3.02; SGP +0.36; QAT -4.48
- PIP, mean per person over the Societal Poverty Line, latest national survey: CHN 2.15; DNK 2.30; FIN 2.18; NOR 2.16; QAT 2.32; SWE 2.16; USA 2.56
- Singapore, PWT output per person a day (2023) and its ratio to the highest line its median could set: 309.0; 1.98
- Easterly and Fischer, USSR, output per worker / growth-accounting TFP / CES TFP, 1960s, 1970s, 1980-87: [3.0, 2.1, 1.4] / [-0.1, -0.8, -1.2] / [1.1, 1.16, 1.09]
- Pollution mortality per 100,000 (crude; air, WASH, poisoning), 1999 to 2019: USA 33.8 to 15.7; DNK 51.3 to 23.5; FIN 19.1 to 7.7; NOR 28.0 to 8.3; SWE 23.2 to 7.4; CHN 144.7 to 127.5; SGP 27.5 to 24.3; QAT 42.2 to 19.4
- WJP sub-factor 6.2, 2025: USA 0.87; DNK 0.97; FIN 0.97; NOR 0.99; SWE 0.92; CHN 0.61; SGP 0.94; QAT 0.66

### Readings as recorded at the checkpoint

C2.6:

| Unit | Clause statuses | Verdict | Flag |
|---|---|---|---|
| Status Quo Market Capitalism | S C S | 0.5 | — |
| Nordic Social Democracy | C C S | 0.5 | — |
| Centrally Planned Socialism | S S S | 0.0 (0.0 reason stated) | toward 0.5 |
| State Capitalism / China (Party-State-Directed Market Economy) | S S S | 0.0 (0.0 reason stated) | — |
| State Capitalism / Singapore (GLC Developmental Capitalism) | S U S | 0.5 | — |
| State Capitalism / Qatar (Gulf Rentier-Distributive Statism) | S U S | 0.5 | — |

C3.6:

| Unit | Clause statuses | Verdict | Flag |
|---|---|---|---|
| Status Quo Market Capitalism | C C C | 1.0 | — |
| Nordic Social Democracy | C S C | 0.5 | — |
| Centrally Planned Socialism | C S U | 0.5 | toward 0.0 |
| State Capitalism / China (Party-State-Directed Market Economy) | C C C | 1.0 | toward 0.5 |
| State Capitalism / Singapore (GLC Developmental Capitalism) | C C C | 1.0 | — |
| State Capitalism / Qatar (Gulf Rentier-Distributive Statism) | S S C | 0.5 | toward 0.0 |

C4.6:

| Unit | Clause statuses | Verdict | Flag |
|---|---|---|---|
| Status Quo Market Capitalism | C S C | 0.5 | — |
| Nordic Social Democracy | C U C | 0.5 | toward 1.0 |
| Centrally Planned Socialism | U U U | 0.0 (0.0 reason stated) | toward 0.5 |
| State Capitalism / China (Party-State-Directed Market Economy) | C S S | 0.5 | — |
| State Capitalism / Singapore (GLC Developmental Capitalism) | C S C | 0.5 | — |
| State Capitalism / Qatar (Gulf Rentier-Distributive Statism) | C S S | 0.5 | — |

### Comparison with part (2.11)'s readings

C2.6:

| Unit | Prior | Blind (Session 77) | Result | Differences |
|---|---|---|---|---|
| Status Quo Market Capitalism | S U U / 0.5 | S C S / 0.5 | revise (clauses) | clause 2: U (prior) vs C (new); clause 3: U (prior) vs S (new) |
| Nordic Social Democracy | C U U / 0.5 | C C S / 0.5 | revise (clauses) | clause 2: U (prior) vs C (new); clause 3: U (prior) vs S (new) |
| Centrally Planned Socialism | S U U / 0.0 | S S S / 0.0 | revise (clauses) | clause 2: U (prior) vs S (new); clause 3: U (prior) vs S (new) |
| State Capitalism / China (Party-State-Directed Market Economy) | S U U / 0.0 | S S S / 0.0 | revise (clauses) | clause 2: U (prior) vs S (new); clause 3: U (prior) vs S (new) |
| State Capitalism / Singapore (GLC Developmental Capitalism) | S U U / 0.5 | S U S / 0.5 | revise (clauses) | clause 3: U (prior) vs S (new) |
| State Capitalism / Qatar (Gulf Rentier-Distributive Statism) | S U U / 0.5 | S U S / 0.5 | revise (clauses) | clause 3: U (prior) vs S (new) |

C3.6:

| Unit | Prior | Blind (Session 77) | Result | Differences |
|---|---|---|---|---|
| Status Quo Market Capitalism | C C U / 0.5 | C C C / 1.0 | revise (verdict) | clause 3: U (prior) vs C (new); verdict: 0.5 (prior) vs 1.0 (new) |
| Nordic Social Democracy | C S U / 0.5 | C S C / 0.5 | revise (clauses) | clause 3: U (prior) vs C (new) |
| Centrally Planned Socialism | S S U / 0.0 | C S U / 0.5 | revise (verdict) | clause 1: S (prior) vs C (new); verdict: 0.0 (prior) vs 0.5 (new) |
| State Capitalism / China (Party-State-Directed Market Economy) | C C U / 0.5 | C C C / 1.0 | revise (verdict) | clause 3: U (prior) vs C (new); verdict: 0.5 (prior) vs 1.0 (new) |
| State Capitalism / Singapore (GLC Developmental Capitalism) | C S U / 0.5 | C C C / 1.0 | revise (verdict) | clause 2: S (prior) vs C (new); clause 3: U (prior) vs C (new); verdict: 0.5 (prior) vs 1.0 (new) |
| State Capitalism / Qatar (Gulf Rentier-Distributive Statism) | U S U / 0.5 | S S C / 0.5 | revise (clauses) | clause 1: U (prior) vs S (new); clause 3: U (prior) vs C (new) |

C4.6:

| Unit | Prior | Blind (Session 77) | Result | Differences |
|---|---|---|---|---|
| Status Quo Market Capitalism | U C C / 0.5 | C S C / 0.5 | revise (clauses) | clause 1: U (prior) vs C (new); clause 2: C (prior) vs S (new) |
| Nordic Social Democracy | U U C / 0.5 | C U C / 0.5 | revise (clauses) | clause 1: U (prior) vs C (new) |
| Centrally Planned Socialism | S S S / 0.0 | U U U / 0.0 | revise (clauses) | clause 1: S (prior) vs U (new); clause 2: S (prior) vs U (new); clause 3: S (prior) vs U (new) |
| State Capitalism / China (Party-State-Directed Market Economy) | U U S / 0.5 | C S S / 0.5 | revise (clauses) | clause 1: U (prior) vs C (new); clause 2: U (prior) vs S (new) |
| State Capitalism / Singapore (GLC Developmental Capitalism) | U U C / 0.5 | C S C / 0.5 | revise (clauses) | clause 1: U (prior) vs C (new); clause 2: U (prior) vs S (new) |
| State Capitalism / Qatar (Gulf Rentier-Distributive Statism) | U U S / 0.5 | C S S / 0.5 | revise (clauses) | clause 1: U (prior) vs C (new); clause 2: U (prior) vs S (new) |

## 6. The revisions, and why each stands

Session 71's rule: a blind reading stands unless the prior shows evidence it did not weigh. The prior stated, for the
law-in-force clauses, "the law in force is not named in this pass", and for C3.6's clause 3 "not assessed in this
pass"; for C4.6's mortality clause, that "the IHME series was not reachable". So every revision that reads a clause
the prior did not read stands. The others:

- **Centrally Planned Socialism's C3.6, 0.0 to 0.5.** The prior's clause 1, "output per hour growth slowed to a halt in
  the 1970s and 1980s", cites Easterly and Fischer without the paper; its table 1 gives output per worker in the total
  economy (Western estimates) rising 3.0%, 2.1% and 1.4% a year in the 1960s, the 1970s and 1980-87. The clause asks
  whether output per hour is non-declining, not whether its growth slowed, so it is cleared (no Soviet hours series is
  at hand; output per worker is the record the paper gives). The prior's 0.0 reason, TFP declining with no pathway, is
  what the blind reading found too (table 4: -0.1, -0.8 and -1.2% a year in 1960-70, 1970-80 and 1980-87), but D28(f)
  bars 0.0 with a clause cleared. The flag toward 0.0 states the band's case; it also records the paper's own CES
  estimates (table 5), which attribute the slowdown to diminishing returns to capital with TFP constant at about 1.1% a
  year, an alternative that would clear clause 2 instead.
- **Singapore's C3.6, 0.5 to 1.0.** The prior's clause 2 was short on PWT 10.01's TFP, -0.36% a year in 1999-2019.
  PWT 11.0 revises the same years to +0.38% and gives +0.36% for 2003-2023, the 20 years to its last year. The
  criterion's indicators name PWT 11.0 and the window ends at the stated date, so the newer edition governs; the prior's
  figure is carried as a flag toward 0.5 (FLAGS). Clause 3, not assessed in the prior, is cleared.
- **Status Quo's and China's C3.6, 0.5 to 1.0.** Both cleared clauses 1 and 2 on both editions; clause 3 is cleared. The
  test (3.6.2) is met by any economy whose median is not far below its mean, and the criterion means it to bind designs
  with short stated hours; a stricter reading, that the basket must reach the whole population, would leave every
  economy short (Societal Poverty Rates from 7.4% in Denmark to 20.2% in the United States), and is the flag added to
  Status Quo's unit (FLAGS). China's unit carries its own flag, on the official accounts PWT rests on.
- **Status Quo's C4.6 clause 2, cleared to short.** The prior cleared it on tort, CERCLA and class actions, with BP's
  Deepwater Horizon settlement as the claim decided and paid. The clause also asks that no immunity leave a class of
  harm compensated from public funds alone; the PREP Act makes a covered person immune from suit and liability for loss
  from a declared countermeasure, the only remedy a fund of emergency appropriations exclusive of any civil action. The
  prior did not weigh the immunity; the reading stands. The verdict, 0.5, is the same.
- **Centrally Planned Socialism's C4.6, short to not shown on each clause.** The prior's three shortfalls cite the
  Report's findings (the Aral Sea, Chernobyl, the state as polluter and regulator). Those findings are not the clauses'
  measures (a 20-year mortality rate the GBD does not reach; the WJP's index, which does not cover the Soviet Union) but
  the 0.0 band's case, which is the blind reading's 0.0 reason. The verdict is the same.
- **Nordic Social Democracy's C2.6.** The prior's flag toward 1.0 falls: clause 3 is short in Sweden (a quarantine and
  an area closure with no stated time limit, the closure not appealable) and Finland (the standing vaccination
  requirement for health and social-care workers).

`blind_s77.py` holds each reason (STAND) and checks that every revision has one.

## 7. Consequences once applied (not applied here)

The standing on the 29 criteria with this group's four verdict changes, alone and on top of Sessions 71 to 76's final
readings (entries whose standing differs from the published provisional scores):

| Entry | Total on 29 | After this group | After Sessions 71 to 77 | Failures | After all seven | Tier after all seven |
|---|---:|---:|---:|---:|---:|---|
| Status Quo Market Capitalism | 12.0 | 12.5 | 12.5 | 7 | 7 | Structurally Inadequate |
| Nordic Social Democracy | 15.0 | 15.0 | 15.5 | 1 | 0 | Potentially Adequate |
| Centrally Planned Socialism | 7.5 | 8.0 | 7.0 | 15 | 16 | Structurally Inadequate |
| Market Socialism | 14.5 | 14.5 | 15.0 | 2 | 1 | Potentially Adequate |
| Libertarian Minarchism | 8.5 | 8.5 | 9.5 | 13 | 11 | Structurally Inadequate |
| Universal Basic Income | 12.0 | 12.0 | 13.5 | 7 | 5 | Partially Adequate |
| Degrowth Economics | 14.5 | 14.5 | 15.0 | 2 | 1 | Potentially Adequate |
| Stakeholder Capitalism | 10.5 | 10.5 | 11.0 | 8 | 7 | Structurally Inadequate |
| Fully Automated Luxury Communism | 10.5 | 10.5 | 11.0 | 10 | 9 | Structurally Inadequate |
| Participatory Economics | 16.0 | 16.0 | 16.5 | 0 | 0 | Potentially Adequate |
| Doughnut Economics | 10.5 | 10.5 | 9.5 | 8 | 10 | Structurally Inadequate |
| Sovereign Wealth Fund Statism | 14.5 | 14.5 | 15.0 | 3 | 2 | Potentially Adequate |
| State Capitalism / China (Party-State-Directed Market Economy) | 10.5 | 11.0 | 11.5 | 9 | 8 | Structurally Inadequate |
| State Capitalism / Singapore (GLC Developmental Capitalism) | 13.0 | 13.5 | 14.0 | 4 | 3 | Partially Adequate |
| State Capitalism / Qatar (Gulf Rentier-Distributive Statism) | 10.5 | 10.5 | 10.0 | 9 | 10 | Structurally Inadequate |
| Islamic Finance / Profit-Sharing Banking | 13.0 | 13.0 | 14.0 | 5 | 3 | Partially Adequate |

First place: this group alone, CCO-PTF-CIP-SZH and Participatory Economics at 16.0 (as published); after Sessions 71 to
77, Participatory Economics alone at 16.5. Tier changes: none from this group; after all seven groups, Universal Basic
Income from Structurally Inadequate to Partially Adequate; Sovereign Wealth Fund Statism from Partially Adequate to
Potentially Adequate (ledger D57 and D56, confirmed).

The final readings' eight flags, each taken alone on all seven groups' final verdicts:

| Unit | Criterion | Final | Flag toward | Total on 29 then | Failures then | Tier then | Changes |
|---|---|---:|---:|---:|---:|---|---|
| Centrally Planned Socialism | C2.6 | 0.0 | 0.5 | 7.5 | 15 | Structurally Inadequate | — |
| Status Quo Market Capitalism | C3.6 | 1.0 | 0.5 | 12.0 | 7 | Structurally Inadequate | — |
| Centrally Planned Socialism | C3.6 | 0.5 | 0.0 | 6.5 | 17 | Structurally Inadequate | — |
| State Capitalism / China (Party-State-Directed Market Economy) | C3.6 | 1.0 | 0.5 | 11.0 | 8 | Structurally Inadequate | — |
| State Capitalism / Singapore (GLC Developmental Capitalism) | C3.6 | 1.0 | 0.5 | 13.5 | 3 | Partially Adequate | — |
| State Capitalism / Qatar (Gulf Rentier-Distributive Statism) | C3.6 | 0.5 | 0.0 | 9.5 | 11 | Structurally Inadequate | — |
| Nordic Social Democracy | C4.6 | 0.5 | 1.0 | 16.0 | 0 | Potentially Adequate | — |
| Centrally Planned Socialism | C4.6 | 0.0 | 0.5 | 7.5 | 15 | Structurally Inadequate | — |

None would change a tier or first place. Nordic Social Democracy's C4.6 toward 1.0 would bring it to 16.0, half a
point behind Participatory Economics.

## 8. Anchors

The three criteria's anchors carry no examples. Candidates, for the owner if examples are added in v2.1: C2.6's 0.0,
State Capitalism / China (civil-liberties score 11 of 60); C3.6's 1.0, State Capitalism / Singapore (output per hour
and TFP rising over 2003-2023 at 2,283 hours a year); C4.6's 0.5, Status Quo Market Capitalism (mortality falling and
regulation clean, with the PREP Act's immunity). None is proposed here.

## 9. Decisions (Session 77)

- **77.1** (optional, method) readings 2.6.1 to 2.6.4, 3.6.1 to 3.6.3 and 4.6.1 to 4.6.4 (section 4), including the use
  of Freedom House's F1 as the test of an independent court (C2.6 clause 3, C4.6 clause 2).
- **77.2** (optional, data) PWT 11.0 in place of PWT 10.01 for C3.6, and the OECD's GBD 2019 dataset (crude rates) for
  C4.6's clause 1, where the WHO's SDG series do not span the window.
- **77.3** (corrections, for S61) the four C3.6 verdict changes of section 6 (Status Quo, China and Singapore 0.5 to
  1.0; Centrally Planned Socialism 0.0 to 0.5) and the clause revisions of all 18 units; FINAL is the blind readings
  with two flags added after the comparison (FLAGS: Singapore's and Status Quo's C3.6). No tier or first
  place changes.
- **77.4** (optional, tooling) `evidence_cache_s77.py`, `blind_s77.py` and harness v47 (130 checks); `blind_s76.py`'s
  check that blind_view lists only files it reads now sets aside the files this session added to the same
  directories (its `LATER`), since the harness copies the whole cache; its output is unchanged.

Nothing is added for the owner: no tier, first-place or CCO-PTF-CIP-SZH change.

## 10. Observations for later sessions

- **D28(f) and the 0.0 band of C3.6.** The band's case reads "productivity *or* TFP declining", but D28(f) bars 0.0
  with any clause cleared, so a configured economy whose TFP falls while output per hour rises, or whose basket is
  provisioned, stays at 0.5 (Centrally Planned Socialism, Qatar, both flagged toward 0.0). The rule has held in every
  group; the limits page should state it for C3.6.
- **Session 76's calibration.** Its reading 3.6.1 calibrated the designs against the four market economies on PWT
  10.01's 1999-2019, all non-declining; on PWT 11.0's 2003-2023 Finland's TFP falls (-0.38% a year). The designs it
  cleared (Stakeholder Capitalism's C3.6 clauses 1 and 2) still rest on three of the four; no verdict turns on it, as
  their clause 3 is not shown.
- **Not reached:** Qatar's statutes, Norway's compulsion and liability acts, and a record of claims decided and paid for
  any economy. Each leaves a clause not shown or short on another ground; none would raise a verdict except the Nordic
  claims record (the flag on Nordic Social Democracy's C4.6).
- **C3.6's clause 3 for a configured economy** is near-automatic on reading 3.6.2; the stricter reading is the flag on
  Status Quo's unit, and the Report should say which reading the published scores use.
- S61 (Session 78) applies `blind_s77.FINAL` with Session 76's: both are held in `rescoring_s65.NEW_UNITS`'s form, so the
  generator places the 69 class N readings where `NEW_UNITS` feeds the v2 files.

## 11. Model and disclosure

Read on Opus 5.5 at high effort, from the cached statutes and series; where a statute is quoted in translation, the
translation is the scorer's, from the cached original (Danish, Finnish, Swedish, Norwegian, Russian, Chinese). The
prior was opened only after checkpoint `3cdf73d`.
