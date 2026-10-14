# NEEC state

**What is true now.** Rewritten by every session before its pull request (`CLAUDE.md`); the handoff says what
changed, this file says what holds. Last rewritten by Session 55 (2026-10-14). It consolidates the standing notes and
open items of Handoffs 43 to 55, which no longer need to be read for them.

## Position

- **Stage 2 of the plan** (the rescoring pass on the v2.0 criteria), in progress. Group 2.1 done (Session 51); Session
  52 built the shared module and the triage; group 2.2, C1.2a re-read as class M, done (Session 53,
  `NEEC_Rescoring_s53.md`): all 23 units read, no entry clears C1.2a, five fall, one rises, no tier changes. **Group
  2.3, C1.3 re-read as class M, done (Session 54, `NEEC_Rescoring_s54.md`)**: the 20 units not yet re-estimated read;
  only Centrally Planned Socialism clears C1.3 (flagged); five designs fall from 1.0 to 0.5; no failure count or tier
  changes. The next group is named below.
- **Landing:** by pull request and the owner's merge (W9, decision 52.3). The session opens the pull request; `harness.yml`
  checks it; the owner merges; `land-session.yml` reruns the checks on `main` and tags each `NEEC Session <n>` commit.
- **Criteria:** v2.0, 29 criteria in `criteria.json`; protocol draft.9. Published scores remain on 26 criteria until
  stage 3 applies the pass by generator.
- **Simulation pin, frozen for v2.0 (decision 52.9):** `BetterToBest/compassionism-simulation` at `5a7a7b1` (v4.20),
  `harness.js` md5 `fe6fa4a3`, `index.html` md5 `c333b632`. **Research Hub pin:** `8e8a6ba`.
- **Harness:** v29, 103 checks, byte-identical under Python 3.11 (the container) and checked by `harness.yml` on 3.12.
- **Site:** live at https://bettertobest.github.io/NormativeEvaluation/, scores gated (`site/config.json`
  `scores.publish` false, decision 49.1).
- **Provisional standing on the published 26-criterion structure** (not for publication before stage 3): CCO-PTF-CIP-SZH
  14.5/26 (published 24.5), first; Participatory Economics and Integral 14.0; eight units not yet read could each change
  who is first (`triage_s52_output.txt`, section 2).

## Next work, in order

1. **C3.5 Failure-Mode Transparency, read in an Opus 5.5 session at high** (class I, 20 units in play, 4 able to change
   an adequacy tier on their own; `triage_s52_output.txt`, section 4). The C3.5 evidence cache is built (Session 55,
   `evidence_cache_s55.py`, `evidence_cache/C3.5/`): it holds the rationale location and citation strings of each of the
   20 units, and four of the five external sources v2.0's measure names (IMF fossil fuel subsidies page and working
   paper, INTOSAI, UK NAO), as landing-page extracts with md5s. It does not hold the GAO's recommendation-implementation
   figures (gao.gov refuses this container, HTTP 403), nor the IMF data tables, nor the dated failure records clause 1
   needs; five units (DG, FALC, MS, PE, SQ) have one-line published rationales that cite nothing. The reading must say
   where a clause is therefore "not shown" rather than "short". Write it as groups 2.2 and 2.3 were: a script on
   `pass_common.py` holding the readings (`U(...)`), its group-specific checks and generated tables
   (`rescoring_s54.py` is the model for a two-clause criterion), a record, `PARTS` extended, the harness given the new
   files (as v29 did through `S54_FILES`). Do not touch earlier scripts or their captures. Then the cache for C1.4,
   C3.1, C2.4, C2.1, C2.3 and C1.1 in a Sonnet 5.5 session, in that order, before each is read.
2. **Then the groups in the triage's order** (section 4 of its output, rerun after each group): C1.4, C4.2, C5.2, C4.1,
   C4.3, C3.1, C2.4, C2.1, C2.3, C1.1, C4.4, C4.5, C2.5, C3.4. Groups already planned partly (C5.2's 16 units at 0.5
   or 0.0, reading 3.2 of `NEEC_Rescoring_s50.md`; C4.3's other 16, part (b8)'s readings 3.2 to 3.5; C4.4's 17, decision
   48.3; C4.1's four part (b6) units on its debt clause) are read within their criterion's group. `rescoring_s51.py`'s
   unit supersedes part (b3)'s C1.1.
3. **The 69 new units** (C2.6, C3.6, C4.6; 23 each): no score exists, so none can be carried forward; they change
   every entry's failure count and total on the 29. Done after the class I and M groups, with the evidence cache.
4. **Carry-forward (decision 52.7):** the triage now names six units that could change no failure count, tier or rank
   on their own (CCO C4.5, CN C2.5, MS C4.5, NSD C4.5, OS C4.5, SQ C2.5). Reading them is cheap inside their
   criterion's group; any left unread is listed in Report v2.0 and the Paper.
5. Stage 3 (apply the pass by generator; `scores.publish` true; Report v2.0 Part I from per-unit rationales, decision
   52.8; C1.2a's 1.0 band drops its example, as C1.1's did), stage 4 (Report and Paper v2.0; the Paper discloses the
   simulation overhaul, decision 52.9), stage 5 (Paper PDF from a committed build script).

## Decided (Session 54, under the delegation; `NEEC_Rescoring_s54.md`)

54.1 the reading of C1.3's two clauses (a 5-year rate, or a lower bound from the channels of displacement closed; costs
of households at 80% of the median as a class, renters at market prices included; a design's description is not a
projection); 54.2 the design's C1.3 on its published model (the engine models no housing tenure; its distress proxy is
read as not shown, not short; the population is the whole society, not Public Trust Housing's fifth); 54.3 Centrally
Planned Socialism's C1.3 holds at 1.0 on a bound from the late-Soviet record, flagged toward 0.5. Carried into the
criteria record at its next amendment, with 53.1 to 53.3, 52.11 and 52.12.

## Decided (Session 53, under the delegation; `NEEC_Rescoring_s53.md`)

53.1 the reading of C1.2a's clause (70% of participants each reach the figure; the engaged-participants reading
flagged); 53.2 the form for class M units below 1.0 (0.0 only on a stated whole-criterion reason under protocol 2.1);
53.3 two corrections (Libertarian Minarchism's C1.2a 0.0 → 0.5; MMT + Job Guarantee's 0.5 → 0.0). Carried into the
criteria record at its next amendment, with 52.11 and 52.12.

## Decided (Session 52; the record's decisions 52.1 to 52.10)

Applied or adopted: W1 model routing, W2 shared pass module (built), W3 this file and self-contained handoffs, W4
checkpoints, W5 evidence cache (to build), W6 consequence triage (built), W7 Report Part I from rationales, W8 pin frozen
at `5a7a7b1` for v2.0, W9 landing by pull request, W10 chat path.

## Awaiting the owner

IDs as in the owner's decisions sheet (a Claude Doc the owner holds). The owner's message of 2026-10-14 listed no
answers for these; all stay open and must be settled before stage 3. Nothing else waits on them.

| ID | Item | Recorded in |
|---|---|---|
| 48.3 | C4.4 clause 1 defined as the share of employment in democratically accountable organizations (flagged) | record, 48.3 |
| 49.2 | Site navigation (flagged) | record, 49.1 to 49.10 |
| 49.3 | The Thresholds page's 11 paraphrases: the owner reads them once | record, 49.1 to 49.10 |
| 49.5 | The Replicate page's AI prompt design (flagged) | record, 49.1 to 49.10 |
| 49.8 | `.github/CONTRIBUTING.md`, six issue forms, four new labels (flagged) | record, 49.1 to 49.10 |
| 49.9 | The visual suite's adaptation; v1's closing panel not carried over (flagged) | record, 49.1 to 49.10 |
| 50.2 | Jev flag-only (flagged) | record, 50.1 to 50.5 |
| 50.4 | Jev question design (flagged) | record, 50.1 to 50.5 |
| 50.5 | Blind replication after stage 3 by a model outside the Claude family (awaiting) | record, 50.1 to 50.5 |
| S50-3.4 | CCO-PTF-CIP-SZH's C5.2 at 0.5, flagged toward 1.0 | `NEEC_Rescoring_s50.md` 3.4 |
| S51-3.2 | Scope: published 1.0s resting on the entry's own modelling | `NEEC_Rescoring_s51.md` 3.2 |
| S51-3.4 | CCO-PTF-CIP-SZH's C1.1 flag toward 1.0 removed | `NEEC_Rescoring_s51.md` 3.4 |
| S51-3.5 | CCO-PTF-CIP-SZH's C1.2b to 0.5 | `NEEC_Rescoring_s51.md` 3.5 |
| S51-3.6 | CCO-PTF-CIP-SZH's C1.4 to 0.5 | `NEEC_Rescoring_s51.md` 3.6 |
| S51-3.7 | CCO-PTF-CIP-SZH's C3.3 to 0.5 | `NEEC_Rescoring_s51.md` 3.7 |
| S53-3.1 | C1.2a's clause read as a share (70% each reach $60,000), not the engaged participants' median; four entries flagged | `NEEC_Rescoring_s53.md` 3.1 |
| S53-3.4 | CCO-PTF-CIP-SZH's C1.2a to 0.5: the model's figure rests on agents saving 47% of income (flagged toward 1.0) | `NEEC_Rescoring_s53.md` 3.4 |
| S53-3.6 | Libertarian Minarchism's C1.2a to 0.5 and MMT + Job Guarantee's to 0.0 (corrections) | `NEEC_Rescoring_s53.md` 3.6 |
| S54-3.2 | Four designs' C1.3 (Degrowth, FALC, Participatory Economics, Integral) to 0.5: neither clause estimated | `NEEC_Rescoring_s54.md` 3.2 |
| S54-3.3 | CCO-PTF-CIP-SZH's C1.3 to 0.5: the model has no housing tenure; on its proxy 78.5% to 86.4% of agents are stable over 5 years, 93.6% to 96.8% inside Public Trust Housing (a fifth of agents) | `NEEC_Rescoring_s54.md` 3.3 |
| S54-3.4 | Centrally Planned Socialism's C1.3 held at 1.0 on a bound (94%), flagged toward 0.5 | `NEEC_Rescoring_s54.md` 3.4 |
| S54-3.6 | Doughnut Economics' C1.3 held at 0.5, flagged toward 0.0 (the reading of its C1.2a) | `NEEC_Rescoring_s54.md` 3.6 |

Method choices Sessions 52 to 54 made that the criteria record does not yet carry (optional, not corrections; carried
into the record at its next amendment): 53.1, 53.2, 54.1 to 54.3 (decision 53.3 is a correction), 52.11, the design of `pass_common.py`; 52.12, the triage's reach assumptions and ordering
key (Handoff 52, section 4).

## Model routing (decision 52.4)

Opus 5.5 at high for judgment groups (class M re-reads, class I readings, the Report and Paper), xhigh only for groups
whose readings are contested; Sonnet 5.5 for mechanical sessions (the evidence cache, the stage 3 generator, the
site, the PDF, harness repairs). Judgment stays with Opus because the harness catches mechanical errors, not
misreadings. Only the owner can set the model; the handoff names it in its first line.

## Reopening conditions (CCO-PTF-CIP-SZH's units and the simulation)

A new simulation version reopens a unit only through these, recorded before the version existed:

- **C1.1:** the model behind the papers' 98% is published and reproduces 98%; or a version reaches a 90% reduction in
  the reference run and 85% in the Adverse Environment, on the Societal Poverty Line.
- **C1.4:** an hours-displacement lever, with poverty under 8% and aggregate demand above 85% of baseline in the 30%,
  50% and 70% scenarios.
- **C3.3:** compound scenarios: degradation under 20% on every core function in at least three of four.
- **C3.4** (0.5, flagged toward 1.0): an endogenous price or behavioural channel, with the adjustment run repeated.
- **C1.2a** (0.5, flagged toward 1.0, S53-3.4): for version 2.1, a version of the model with a sourced consumption rule
  that still shows 70% of agents accumulating $60,000 (2019 dollars) in 20 years in the reference run.
- **C1.3** (0.5, S54-3.3): for version 2.1, a version of the model with housing tenure and a housing-cost line that
  shows 88% of all agents stable over 5-year windows and housing costs at or under 30% of disposable income at 80% of
  the median, in the reference run.
- **C5.2** (0.5, flagged toward 1.0, S50-3.4): a municipal pilot of the currency or the portal, or any deployment of
  either at scale. A simulation does not reopen it.
- Handoff 43 section 9.3's reopening conditions and limitations stand for the units they name.

## Standing notes

- **Site regeneration.** Any change to the site's inputs (`criteria.json`, the corpus, the CSV, the summary blocks,
  `NEEC_Criteria_v2_s45.md`, Paper v1.4, the A.4 weighting script, the WJP extract, `.github/ISSUE_TEMPLATE/`,
  `site/`) needs the chain: `build_criteria.py` in a temporary directory with its four inputs, copy `criteria.json`
  and the capture back, `build_site.py`, `build_readme.py`, then the harness. Every amendment of the criteria record
  changes `criteria.json`'s `record_md5` and the footer of 64 `docs/` pages. Never edit `docs/` by hand (check 93).
- **Python.** The cloud container's `python3` is 3.11; the workflows use 3.12; the harness reproduces on both. A
  check's summary line is shown in the harness with `show_summary=True`.
- **PDFs in the container.** `pypdf` fails on the container's `cryptography` build; `apt-get install -y
  poppler-utils` gives `pdftotext`. It does not persist between sessions.
- **Simulation runs.** Clone `BetterToBest/compassionism-simulation` at the pin beside the repository and run
  `node cco_simulation_checks_s51.js ../compassionism-simulation/harness.js ../compassionism-simulation/index.html`;
  output must equal `cco_simulation_checks_s51_output.txt` (md5 `b4f481e7`). Its runner is the model for later runs;
  the harness checks captures by digest and does not rerun JavaScript.
- **Jev.** Runs go through the owner's Composio connection (a claude.ai chat, or a cloud session with the connector
  attached). Pin the model in every request (`jev-1.13.0`); transcribe responses into a recorded file a script
  checks with no network call. A direct API call would need a TypeSafe key set by the owner as an environment
  secret, never committed. Optional; it changes no score.
- **Network.** Evidence work reads github.com, bettertobest.github.io, the World Bank, IMF, OECD, Eurostat, Freedom
  House, V-Dem, the WJP and similar hosts; without that access it can be recorded but not done.
- **Sources not in the repository** are identified in the record by name and md5 wherever a figure depends on them;
  every figure used is held in that session's script.
- **Workflow files** change only through the owner. `land-session.yml` requests a Pages build after each landing.
- **The Research Hub** is outside this repository; changes there are the owner's. Its roadmap (national launch in
  year 2) and its modelling paper (municipal pilots first) describe different staged pathways (Handoff 50).
- **Version 1** remains on the original Google Site; the owner has been asked to mark its scores as superseded (on
  the v1 home and report pages, the Medium article and the public visual-suite artifact) and to point the Research
  Hub's comparison entry at the v2 site. Whether that is done is not recorded here.
- **The simulation overhaul (decision 52.9).** The owner reports (2026-10-14) that the Compassionism Simulation has been
  overhauled since `5a7a7b1` and that many headline figures changed, several less favourably. Version 2.0 is frozen at
  the pin; Paper v2.0 discloses that the simulation has since been overhauled with revised headline figures, and that the
  owner maintains both the design and the model. A later version is read in version 2.1. The reopening conditions above
  are written for raising a unit in 2.0 and do not take effect from a later version's figures.
- **The shared pass module and the triage.** `python3 pass_common.py --selftest` reproduces group 2.1's tables from the
  parts before it; a new group is added to `PARTS` there, and the harness's S52 checks must then be given the group's
  files (v29 does this through `S54_FILES`; a later version extends it the same way). `python3 triage_s52.py` prints the
  consequence triage on the state through the last part (since Session 53 it reads the state from `PARTS` and holds no
  count of its own); after a group lands, replace `triage_s52_output.txt` and recapture the harness.
- **Wealth data used by group 2.2** (not in the repository; figures held in `rescoring_s53.py`): the Survey of Consumer
  Finances 2025 extract (`scfp2025excel.zip`, md5 c938318c; 2025 dollars; released 2026-10-09), Statistics Norway's
  2024 household wealth tables (10318, 10315), and World Bank WDI series retrieved 2026-10-14. The BLS API refused
  requests (its daily limit); FRED served CPI-U over HTTP/1.1 (`curl --http1.1`).
- **Sources used by group 2.3** (not in the repository; figures held in `rescoring_s54.py`): Childress, Kutuzov and
  Haase, *A Decade of Housing Reform in Russia* (Land Tenure Center, 2001; md5 babfbd70, from minds.wisc.edu); the IMF,
  World Bank, OECD and EBRD *Study of the Soviet Economy* (1991), chapter V.9, whose text refused retrieval (the census
  shares are quoted from the publisher's catalogue); JCHS's *State of the Nation's Housing 2025* via NLIHC's summary;
  Census P60-282; Eviction Lab's 2022 update. A new simulation runner, `cco_c13_checks_s54.js`, captured
  (`cco_c13_checks_s54_output.txt`, md5 30d131f0), runs in under a minute.
- **Class D count.** Earlier files say "25 units at 0.5" for class D; after decision 48.3 moved C4.4 to class M the
  count is 18 at 0.5 (C2.5 and C4.5), with 12 more at 0.0 that class D could also raise (`triage_s52_output.txt`).
