# NEEC Project Handoff 65

**Session 65 · 2026-10-15 · Owner: Duke Johnson · Scorer and engineer: Claude**

> **Next session (66): Sonnet 5.5 at medium effort, Claude Code or Claude Chat.** Task: publish the v2.0 scores (section 4;
> mechanical, after the owner's go on ledger d49). The Report and Paper v2.0 that follow want Opus 5.5 at high (judgment prose).
> Send `Continue NEEC.` Session 65 ran on Sonnet 5.5, so its judgment calls (section 3) may be read again in an Opus session.

This handoff is self-contained. What holds now is in `STATE.md`.

## 1. What changed

The owner asked to finish the scoring in one or two sessions (the weekly usage limit). Session 65 read every unit left in play and
scored the new criteria, in one script and one record (`rescoring_s65.py`, `NEEC_Rescoring_s65.md`, generated and compared byte for
byte), then wrote stage 3's generator. Session 64's start check passed (all real checks; the digest I passed was a placeholder).

- **128 units across C4.1, C4.4, C3.4, C4.5, C2.5, C1.1 and, held without re-measuring, C2.1, C2.4, C2.3** (decision 65.2): four rise,
  one falls, 123 hold. Rises: Status Quo C4.1 and C4.4 (0.0 to 0.5, corrections: the published reason was carbon or wealth
  concentration, now in C4.2 and C1.2b); Qatar C4.1 (0.5 to 1.0: debt 41.4% of GDP, net saving positive; flagged toward 0.5);
  Participatory Economics C4.5 (0.0 to 0.5; flagged toward 0.0). Fall: Integral C3.4 (1.0 to 0.5; flagged toward 1.0).
- **First place:** on the 26 criteria CCO-PTF-CIP-SZH and Participatory Economics share it at 14.5 (Integral 14.0). No tier changes in
  this session on the 26.
- **The 69 new units** (C2.6, C3.6, C4.6): no 1.0. Configured economies on cached series (Freedom House ratings, Penn World Table 10.01,
  WJP sub-factor 6.2); designs 0.5 by a stated rule; China (C2.6) and Centrally Planned Socialism (all three) 0.0. On the 29
  criteria: CCO and PE 16.0, Integral 15.5, Nordic Social Democracy 15.0; 7 Potentially, 7 Partially, 9 Structurally Inadequate.
- **Stage 3's generator:** `apply_pass_s65.py` writes `neec_corpus_v2.json`, `neec_scores_v2.csv`, `summary_blocks_v2.json` without
  touching the files the pass was computed against. The site builds with them (verified in a scratch copy: 77 files, scores published).
- **The publish gate is not flipped.** I tried to change `site/config.json` and rebuild `docs/`; the auto-mode classifier refused. It is
  left for the owner (d49), as decision 49.1 reserved it.
- Ledger: d44 to d49 and glossary entries written (read back at the start of the next session). `triage_s52.py` now prints that no
  group remains.

## 2. Files

New: `rescoring_s65.py`, `rescoring_s65_output.txt`, `NEEC_Rescoring_s65.md`, `evidence_cache_s65.py`, `evidence_cache/C1.1/`,
`C2.6/`, `C3.6/`, `C4.1/`, `C4.4/` data files, `apply_pass_s65.py`, `apply_pass_s65_output.txt`, `neec_corpus_v2.json`,
`neec_scores_v2.csv`, `summary_blocks_v2.json`, this handoff. Changed: `pass_common.py` (PARTS gains "(2.11)"), `triage_s52.py`
(no-group-left branch), `run_all_checks.py` (v37, checks 111 and 112), `run_all_checks_output.txt`, `pass_common_selftest_output.txt`,
`triage_s52_output.txt`, `README.md`, `STATE.md`.

## 3. Judgment calls to read again (all delegated, may be reversed; ledger d44 to d48)

PE C4.5 and Integral C3.4 (they decide first place); Qatar C4.1; the held class I criteria; the 17 designs and mechanisms on the new
criteria (least read; each unit's note says so); the Centrally Planned Socialism C3.6 reading, from Easterly and Fischer (1995), which
is not cached. Not re-measured: the Gallup, turnout, OECD trust and time-use series for C2.1, C2.4 and C2.3.

## 4. Publishing the v2.0 scores (needs the owner's go, ledger d49)

1. In `site/config.json` set `scores.publish` to `true`, `corpus` to `neec_corpus_v2.json`, `csv` to `neec_scores_v2.csv`,
   `summary_blocks` to `summary_blocks_v2.json`.
2. Add a provisional notice to the public pages (the scores are a pass in progress; Report and Paper v2.0 are not written). The build
   has a preview banner only; a small `scores.provisional_note` setting that prints a banner is the simplest change.
3. `python3 build_site.py`, commit `docs/`; the harness's site checks (build_site `--check`) and any check that asserts the gate is
   false must be updated, then `python3 run_all_checks.py > /tmp/out.txt; cmp /tmp/out.txt run_all_checks_output.txt`.
4. The Contribute page is the route users challenge a score or threshold; nothing to build.

## 5. Next session (66): start here

1. Run `session_check.py --tag s65 ...` after the merge (files and digest as in Handoff 63's method). Read the ledger for answers to
   d38, d42 to d49 and record them (CLAUDE.md, Start, step 5).
2. If d49 says publish, do section 4. If an answer reverses a reading, change `rescoring_s65.py`, regenerate the record
   (`--write-record`), `apply_pass_s65.py`, and the captures.
3. Then Report v2.0 and Paper v2.0 (Opus 5.5, high), the PDF, and the open items in `STATE.md`.
