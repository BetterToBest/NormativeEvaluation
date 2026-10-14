# NEEC state

**What is true now.** Rewritten by every session before its pull request (`CLAUDE.md`); the handoff says what
changed, this file says what holds. Written by the Session 52 package from tag `s51` (`14f435a`, 410 files) on
2026-09-26 and amended in a claude.ai chat on 2026-10-14, when the package was committed directly and the pull-request
landing (W9) added; it consolidates the standing notes and open items of Handoffs 43 to 51, which no longer need to be
read for them.

## Position

- **Stage 2 of the plan** (the rescoring pass on the v2.0 criteria), in progress. Group 2.1 done (Session 51). No
  session ran between 2026-09-26 and 2026-10-14.
- **Landing:** by pull request and the owner's merge (W9), from Session 52. Pull request #12 (a duplicate Session 49
  branch, `claude/clever-newton-17rt1c`, never merged; Session 49 landed as `a379f74`) was closed unmerged on
  2026-10-14.
- **Criteria:** v2.0, 29 criteria in `criteria.json`; protocol draft.9. Published scores remain on 26 criteria until
  stage 3 applies the pass by generator.
- **Simulation pin:** `BetterToBest/compassionism-simulation` at `5a7a7b1` (v4.20), `harness.js` md5 `fe6fa4a3`,
  `index.html` md5 `c333b632`. **Research Hub pin:** `8e8a6ba`.
- **Harness:** v26, 99 checks, byte-identical under Python 3.11 and 3.12.
- **Site:** live at https://bettertobest.github.io/NormativeEvaluation/, scores gated (`site/config.json`
  `scores.publish` false, decision 49.1).
- **Provisional standing on the published 26-criterion structure:** CCO-PTF-CIP-SZH 15.5/26 (published 24.5);
  Participatory Economics and Integral 14.5. Not for publication before stage 3.

## Next work, in order

1. Record the owner's answers to the items below, if the opening message carries them, in one amendment of
   `NEEC_Criteria_v2_s45.md` (one run of the site's regeneration chain).
2. Correction carried by W9: `build_readme.py` says a session reaches `main` "only through `land-session.yml`"; it now
   reaches `main` by the owner's merge of its pull request, after `harness.yml` passes on it, and `land-session.yml`
   tags it. Amend that sentence, regenerate `README.md` and recapture as the chain requires.
3. If W2 is adopted: the shared pass module, before any new group. If W6 is adopted: the consequence triage (which
   remaining units could change a failure count, an adequacy tier or a rank), written as a script with captured
   output, so that later groups are read in that order.
4. Class M re-checks, cumulative with `rescoring_s51.py` (`PRIOR` gains
   `("(2.1)", "rescoring_s51", "rescoring_s51.py", 51)`; its re-read unit supersedes part (b3)'s C1.1):
   C5.2's 16 units at 0.5 or 0.0 (reading 3.2 of `NEEC_Rescoring_s50.md`); C4.3's other 16 units (part (b8)'s readings
   3.2 to 3.5); C4.4's 17 units (48.3); C4.1's four part (b6) units (FALC, PE, INT, SWF) on its debt clause.
5. The rest of class M (C1.2a, C1.3, C3.4, C4.1, C4.2, C4.3, C5.2 not yet read on v2.0; the design's C1.2a and C1.3
   read the model at `5a7a7b1`, reading 3.10 of `NEEC_Rescoring_s51.md`); class D rises (25 units at 0.5); class I
   re-checks (42 configured-economy units among them); the 69 new units (C2.6, C3.6 and C4.6, 23 each).
6. Stage 3 (apply the pass by generator; `scores.publish` true), stage 4 (Report and Paper v2.0), stage 5 (Paper
   PDF from a committed build script).

## Awaiting the owner

IDs as in the owner's decisions sheet (a Claude Doc the owner holds) and in the opening message. Nothing waits on any
of them yet; all must be settled before stage 3.

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
| W1 | Model routing (below) | this file |
| W2 | A shared pass module; each group a short file of readings; scripts write their tables into records | this file |
| W3 | This file, self-contained handoffs, the usage rule in `CLAUDE.md` (applied by the package) | package note |
| W4 | Checkpoints and resume (applied by the package) | package note |
| W5 | An evidence cache for the class I re-checks and new units, built once, extracts committed with md5s | this file |
| W6 | Stage 2 ordered by consequence (failure count, tier, rank first); any carry-forward disclosed | this file |
| W7 | Report v2.0 Part I generated from per-unit rationales carried into the corpus at stage 3 | this file |
| W8 | The simulation pin for v2.0: freeze at `5a7a7b1`, or read a later version before stage 3 (the simulation has since been overhauled; see Standing notes) | this file |
| W9 | Landing by pull request: the session opens it, the owner merges it, `land-session.yml` tags on merge (applied by the owner's merge of the pull request that carries this file) | package note, section 5 |
| W10 | A chat path for weeks without Claude Code: a free-plan chat session works on a repository ZIP and returns a changed-files ZIP that the owner uploads to a branch and opens as a pull request | package note, section 5 |

## Model routing

Until the owner answers W1, Handoff 45's plan stands: Opus 5.5 at xhigh for stage 2, xhigh and high for the
Report and the Paper (stage 4), high for stages 3 and 5. Proposed in W1 (amended 2026-10-14, Sonnet 5.5 having
replaced Sonnet 5): Opus 5.5 at high for judgment groups, xhigh only for groups whose readings are contested;
Sonnet 5.5 for mechanical sessions (recording decisions, the shared pass module, the triage script, evidence
extraction, the stage 3 generator, the site, the PDF, harness repairs). Judgment stays with Opus because the harness
catches mechanical errors, not misreadings.

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
- **The simulation overhaul.** The owner reports (2026-10-14) that the Compassionism Simulation has been overhauled
  since `5a7a7b1` and that many of its headline figures changed, several less favourably. The pass reads the pin, so
  nothing in the repository changes by that report; W8 decides whether v2.0 reads the pin or a later version. The
  reopening conditions above were written as conditions for raising a unit; a later version that weakens a figure a
  unit rests on is a separate question, to be recorded under W8 if the owner chooses to read it.
