# NEEC state

**What is true now.** Rewritten by every session before its pull request (`CLAUDE.md`); the handoff says what
changed, this file says what holds. Last rewritten by Session 52 (2026-10-14). It consolidates the standing notes and
open items of Handoffs 43 to 52, which no longer need to be read for them.

## Position

- **Stage 2 of the plan** (the rescoring pass on the v2.0 criteria), in progress. Group 2.1 done (Session 51). Session
  52 recorded the owner's decisions, corrected the README, and built the shared module and the triage; it scored
  nothing. The next group is named below.
- **Landing:** by pull request and the owner's merge (W9, decision 52.3). The session opens the pull request; `harness.yml`
  checks it; the owner merges; `land-session.yml` reruns the checks on `main` and tags each `NEEC Session <n>` commit.
- **Criteria:** v2.0, 29 criteria in `criteria.json`; protocol draft.9. Published scores remain on 26 criteria until
  stage 3 applies the pass by generator.
- **Simulation pin, frozen for v2.0 (decision 52.9):** `BetterToBest/compassionism-simulation` at `5a7a7b1` (v4.20),
  `harness.js` md5 `fe6fa4a3`, `index.html` md5 `c333b632`. **Research Hub pin:** `8e8a6ba`.
- **Harness:** v27, 101 checks, byte-identical under Python 3.11, 3.12 and 3.13.
- **Site:** live at https://bettertobest.github.io/NormativeEvaluation/, scores gated (`site/config.json`
  `scores.publish` false, decision 49.1).
- **Provisional standing on the published 26-criterion structure** (not for publication before stage 3): CCO-PTF-CIP-SZH
  15.5/26 (published 24.5), first; Participatory Economics and Integral 14.5; no single unit can change who is first
  except PE C4.5, INT C1.2a and INT C5.2 (`triage_s52_output.txt`).

## Next work, in order

1. **The next group, from the triage (`triage_s52_output.txt`, section 4): C1.2a Wealth Building for Resilience**,
   class M, 23 units, 6 of them able to change an adequacy tier on their own (most of any criterion). Model: Opus 5.5
   at high; xhigh only if a reading is contested (decision 52.4). Written in the new form: a short readings file
   (`UNITS` in the form of `rescoring_s37.U`) and a short script on `pass_common.py` (its `Pass`, `run_group`, and
   the group-specific checks only); add the group to `PARTS` in `pass_common.py`. The design's C1.2a reads the model at
   `5a7a7b1` (reading 3.10 of `NEEC_Rescoring_s51.md`). Do not touch the existing scripts or their captures.
2. **Then the groups in the triage's order** (section 4 of its output): C3.5, C1.3, C1.4, C4.2, C5.2, C4.1, C4.3, C3.1,
   C2.3, C2.1, C2.4, C1.1, C4.4, C4.5, C2.5, C3.4. Groups already planned partly (C5.2's 16 units at 0.5 or 0.0, reading
   3.2 of `NEEC_Rescoring_s50.md`; C4.3's other 16, part (b8)'s readings 3.2 to 3.5; C4.4's 17, decision 48.3; C4.1's
   four part (b6) units on its debt clause) are read within their criterion's group. `rescoring_s51.py`'s unit supersedes
   part (b3)'s C1.1. Class I groups use the evidence cache (W5, decision 52.6): build it first, in a Sonnet 5.5 session,
   before the first class I group (C3.5 is the first).
3. **The 69 new units** (C2.6, C3.6, C4.6; 23 each): no score exists, so none can be carried forward; they change
   every entry's failure count and total on the 29. Done after the class I and M groups, with the evidence cache.
4. **Carry-forward (decision 52.7):** the triage names ten units that could change no failure count, tier or rank on
   their own (CCO C1.2a, CCO C1.3, CCO C4.5, CN C2.5, CPS C1.3, MS C4.5, NSD C4.5, PE C2.5, SQ C2.5, UBI C1.4). Reading
   them is cheap inside their criterion's group; any left unread is listed in Report v2.0 and the Paper. The triage is
   rerun after each group (`python3 triage_s52.py`; its capture is replaced when the state changes).
5. Stage 3 (apply the pass by generator; `scores.publish` true; Report v2.0 Part I from per-unit rationales, decision
   52.8), stage 4 (Report and Paper v2.0; the Paper discloses the simulation overhaul, decision 52.9), stage 5 (Paper
   PDF from a committed build script).

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

Method choices Session 52 made that the criteria record does not yet carry (optional, not corrections; carried into the
record at its next amendment): 52.11, the design of `pass_common.py`; 52.12, the triage's reach assumptions and ordering
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
  parts before it; a new group is added to `PARTS` there. `python3 triage_s52.py` prints the consequence triage on the
  state through the last part; after a group lands, replace `triage_s52_output.txt` and recapture the harness.
- **Class D count.** Earlier files say "25 units at 0.5" for class D; after decision 48.3 moved C4.4 to class M the
  count is 18 at 0.5 (C2.5 and C4.5), with 12 more at 0.0 that class D could also raise (`triage_s52_output.txt`).
