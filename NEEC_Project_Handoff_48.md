# NEEC Project Handoff 48

**Session 48 · 2026-09-24 · Owner: Duke Johnson · Scorer and engineer: Claude**
**Predecessor:** Handoff 47, whose sections 5–8 stand except where this handoff amends them.

> **Next session (49): Claude Code cloud, effort `xhigh`, network access as in Session 48** (Full, or the evidence
> hosts listed in section 1). Then send `Continue NEEC.`

The owner's message for Session 48 answered Handoff 47's three open questions and asked why the totals fell although
three criteria were added. **All three are recorded as decisions** (`NEEC_Criteria_v2_s45.md`): **48.1**, the WJP bar
for C4.6 clause 3 stays at 0.77, with reasons (delegated); **48.2**, "time-limited" includes standing vaccination
requirements (the owner's decision; the adopted text already said so); **48.3**, C4.4 clause 1 is defined now rather
than in v2.1, as the share of employment in organizations whose investment, production and employment decisions
answer to those they affect, at least 80% (delegated; flagged). C4.4 moves to class M, `build_criteria.py` version 2.3
generates protocol **draft.9**, and `rescoring_s48.py` re-reads C4.4's six units in the pass on the defined measure:
Nordic Social Democracy stays 0.5, now short and unflagged; **the owner's design, CCO-PTF-CIP-SZH, falls from 1.0 to
0.5**, on the same test; Participatory Economics, Integral and Market Socialism stand. Net −0.5. **The owner's
question is answered by a generated score ledger** (`NEEC_Rescoring_s48.md`, section 6; summary in section 2a here).
**Part (b)'s eighth group (C4.3, C4.5) was not begun** (section 6). Harness v23, **92 of 92**, byte-identical on a
second run. No published score changed.

## 1. Session-start checks

s47 landed: `main` and tag `s47` at `a4d37eb`. `session_check.py --tag s47 --files 278 --digest
3e3019e7d43e50a374e913732076349a --handoff NEEC_Project_Handoff_47.md`: ALL PASS (tags s34–s47; 278 files; digest
match; harness v22 91 of 91 byte-identical; latest Actions run on main, run 63 at `a4d37eb`, completed/success);
Simulation `cd0ceec` and Research Hub `8e8a6ba` unchanged. Network: sdmx.oecd.org, ec.europa.eu (Eurostat),
ourworldindata.org, v-dem.net, worker-participation.eu, ciriec.uliege.be and github.com answered 200; www.oecd.org
answered 403 and lovdata.no 405 (neither was needed).

## 2. What changed

- **Record** (`NEEC_Criteria_v2_s45.md`, amended in place; tag `s47` keeps its prior text): decisions **48.1** to
  **48.3**. 48.1 keeps 0.77 because the clause asks for regulation without improper influence, not typical
  regulation (the median is the typical jurisdiction), because v2.0's other rating bar (C2.6, Freedom House) is the
  top band, and because the choice decides only Qatar (0.66) and China (0.61), China having scored 0.45 to 0.61 in
  every edition. The owner's message called it "the Gini bar"; it quotes 47.1's alternative, so it is read as the
  WJP bar, and no Gini bar is open. 48.2 closes 46.2(e)'s ▲ with no text change. 48.3 is set out in full in the
  record: its reasons, the measure, how a configured economy and a design are read, the alternative for the owner,
  and the class change; the Appendix V block for C4.4 carries the measure and names the indicators. Sections 4, 5,
  7 and 8 updated (class D is now 46 units, 18 at 0.5; class M 184).
- **`build_criteria.py` version 2.3**: generates draft.9 (version line, changes paragraph, Appendix B header); code
  otherwise unchanged. A1–A7 pass; the self-test's capture is unchanged. Build capture renamed
  `build_criteria_s48_output.txt`.
- **`criteria_v2_s45.py`**: section 3 counts the classes anew; section 5 asserts China's series and Qatar's single
  edition (48.1).
- **`criteria_s47_snapshot.json`** (new): `criteria.json` as it stood at tag `s47`, byte-identical. `rescoring_s47.py`
  asserts C4.4's Session 47 class, so check 91 now reads this snapshot under the canonical name.
- **`NEEC_Rescoring_s48.md`, `rescoring_s48.py`, `rescoring_s48_output.txt`** (new): C4.4's six units re-read on
  48.3 (part (b7)'s records superseded), Nordic Social Democracy's clause 1 bound computed from published series
  (most generous count 44.1–48.6% against 80%), consequences, and the score ledger. Two corrections: part (b7)'s
  uneven application of the accountability clause (the "as audited" carry shielded the owner's design from the
  test applied to Nordic Social Democracy), and Report v1.6's Nordic C4.4, which credits minority board
  representation that its Stakeholder Capitalism entry scores 0.0.
- **`run_all_checks.py` v23**: check 91 pinned to the Session 47 criteria; check 92 runs `rescoring_s48.py`, unpinned.
  **92 checks.** `README.md` regenerated (draft.9, 92 checks, eight thresholds restated).

### 2a. The owner's question: why the totals fell although three criteria were added

- **What was published.** CCO-PTF-CIP-SZH's published total is **24.5/26**, 0 failures (`neec_corpus.json`,
  `neec_scores.csv`, `README.md`, Report v1.6). Its history: 23.5/25 in version 1, 24.5/26 after Session 8 split
  C1.2 in two. No file in the repository's history gives it 22.5/26.
- **What "19" was.** Handoff 47's 19.0 was on the **26** published criteria, after parts (a) to (b7) of the pass: 19.0/26,
  not 19/29. After 48.3 it is **18.5/26**. No total on 29 criteria exists: the three new criteria's 69 units are not
  scored, so they add nothing yet and are in no denominator.
- **Why totals fell.** Every fall is the D28 rescoring pass (Session 35): a 1.0 must now show every clause of its
  Pass Threshold on named evidence, or it becomes 0.5 (never 0.0, so no failures or tiers change). Of 128 units
  re-estimated, 118 are at 0.5. CCO-PTF-CIP-SZH was published with 23 criteria at 1.0, more than any other entry
  (Participatory Economics had 16), so it had the most to re-check: 13 re-estimated, 12 at 0.5, 24.5 − 6.0 = 18.5.
  The ledger lists every entry's change by part and CCO-PTF-CIP-SZH's by criterion, with the clause that decided each.
- **What comes next.** Stage 2 scores the 69 new units (0 to 3 points per entry) and runs the class re-checks, which
  can raise units as well as lower them; 17 D28 units remain, which can only stay or fall. Only then does a total on
  29 criteria exist.
- **Drift.** `neec_corpus.json`, the one source of the published scores, has not changed since the repository's first
  commit (Session 34); every change the pass makes is in a committed script that recomputes totals from it and every
  earlier part, and the harness reruns all of them at each landing. The ledger reconciles each entry's total and
  checks the published totals against the CSV.

## 3. Files

14 files changed or added (one renamed), plus this handoff: 283 tracked files.

| File | MD5 (first 8) | Status |
|---|---|---|
| `NEEC_Criteria_v2_s45.md` | `c318eabd` | amended (48.1–48.3) |
| `criteria.json`, `SCORING_PROTOCOL.md` | `af69e2e8`, `dde8e834` | regenerated (draft.9) |
| `build_criteria.py`, `build_criteria_s48_output.txt` | `b2f166cc`, `5baf75ee` | version 2.3; capture renamed from `_s47_` and recaptured |
| `criteria_v2_s45.py`, `criteria_v2_s45_output.txt` | `58813464`, `3fb1e0ff` | 48.1 assertions; class counts; recaptured |
| `criteria_s47_snapshot.json` | `fa5da0cd` | new (pinned `criteria.json` at `s47`) |
| `NEEC_Rescoring_s48.md`, `rescoring_s48.py`, `rescoring_s48_output.txt` | `3582d228`, `e5a9453d`, `5de0cba5` | new |
| `run_all_checks.py`, `run_all_checks_output.txt` | `a0442b0c`, `3d03a594` | v23, recaptured |
| `README.md` | `b4c9e227` | regenerated |
| `NEEC_Project_Handoff_48.md` | (this file) | new |

## 4. Landing

The session's last commit, "NEEC Session 48: …", is pushed on `claude/confident-einstein-cjqclj`; `land-session.yml`
merges it into main, reruns every check, tags `s48` and publishes the release. No owner step.

## 5. Decision register

Protocol section 13 (D2–D31) unchanged; 45.1–45.7, 46.1–46.4, 47.1–47.2 and 48.1–48.3 join it when the pass ends.
Closed this session: 47.1's ▲ (by 48.1), 46.2(e)'s ▲ (by 48.2), and Handoff 47's two flagged C4.4 calls (by 48.3).
**For the owner, when convenient (nothing waits on it):**
- **48.3, flagged.** The alternative (decisions within law made by an elected legislature count as accountable)
  would raise Nordic Social Democracy's C4.4 to 1.0 and restore CCO-PTF-CIP-SZH's to 1.0. It would also leave C4.4
  measuring removal only and contradict the published Stakeholder Capitalism reading. Because the adopted reading
  lowers the owner's own design, the owner may wish to confirm it.

## 6. Next session (49): start here

1. Run `python3 session_check.py --tag s48 --files 283 --digest e137e7f3037da062e78b4ce0affa8be0 --handoff NEEC_Project_Handoff_48.md`
   and expect ALL PASS. If tag `s48` is missing, read the land-session run's log and repair that first.
2. **Part (b), eighth group, still to do: C4.3** (6 units, class M: v2.0 deletes the 150%+ clause and adds the
   declared-axis scope) and **C4.5** (3 units, class D), in the form of `NEEC_Rescoring_s47.md` and `rescoring_s47.py`,
   with part (a)'s units of both re-read on v2.0 and cumulative with `rescoring_s48.py`. Then C5.2 (4), C5.4 (2)
   and C5.5 (2), which finishes part (b). Session 48 did not begin this group. The environment's permission
   classifier (Claude Code auto mode) denied the command that listed the group's units, with the reason "Code from
   External", and a second command toward the same list; the session stopped that line of work, as the classifier
   instructs, and did the rest. The owner can allow such commands with a Bash permission rule in the session's
   settings; if the next session meets the same denial, it should say so and carry on with the rest.
3. If time remains, the class M re-checks: C4.4 is now among them (its seven published 0.5s and ten 0.0s, the
   configured national economies read from the series 48.3(d) names), and v2.0's C4.1 leaves four part (b6) units
   (FALC, PE, INT, SWF) turning on their debt clause.

## 7. Plan to completion (amends Handoff 47, section 7)

Stage 2 did not advance on part (b) this session, so its estimate moves by one: **sessions 49–52, possibly 54.**
The later stages are unchanged and follow it (stage 3, one session; Report and Paper v2.0, two; the PDF, one; the
site, two).

**Credit.** This session cannot see the Claude Code cloud credit balance; no tool available to it reports one. The
owner's cap for NEEC is $50. If the remaining sessions would exceed it, Handoff 47's narrowing of stage 2 stands as
the option (class I re-checks only where a published series could change a verdict; new units before class M
re-checks of units already at 0.0).

## 8. Standing notes

- Handoff 47's standing notes stand.
- Sources read this session that are not in the repository, identified where a figure depends on them: OECD, *The
  Size and Sectoral Distribution of State-Owned Enterprises* (2017, PDF md5 `93290021`); CIRIEC for the EESC,
  *Recent Evolutions of the Social Economy in the European Union* (2017, PDF md5 `64f29fa8`); OECD SDMX
  `DF_GOV_EMPPS_REP_2025`; Eurostat `lfsa_egaps`; Our World in Data `political-regime`; worker-participation.eu
  country pages; the Research Hub at `8e8a6ba` (corporate-transformation, glossary, simulation-replication and index
  pages). Every figure used is held, with its source, in `rescoring_s48.py`.
