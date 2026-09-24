# NEEC Project Handoff 47

**Session 47 · 2026-09-24 · Owner: Duke Johnson · Scorer and engineer: Claude**
**Predecessor:** Handoff 46, whose sections 5–8 stand except where this handoff amends them.

> **Next session (48): Claude Code cloud, effort `xhigh`, network access as in Session 47** (Full, or the evidence
> hosts allowed). Then send `Continue NEEC.`

Session 47 had the network access Session 46 lacked and did both things Handoff 46 set. **C4.6's clause 3 bar is
fixed** (decision 47.1): a World Justice Project sub-factor 6.2 score of **0.77 or more**, the upper quartile of the
Index's 2025 edition, fixed as a figure. The Index normalizes its scores against a 2015 base and publishes no bands,
so the bar had to come from the distribution. The Pass Threshold carries it, `build_criteria.py` version 2.2
regenerates `criteria.json` and protocol **draft.8**, and `criteria_v2_s45.py` asserts every figure from a committed
extract of the Project's data. **Stage 2 began:** part (b)'s seventh group, C4.2 and C4.4, the first scored on the
v2.0 clauses (`NEEC_Rescoring_s47.md`, `rescoring_s47.py`). All six C4.2 units fall to 0.5 on the biodiversity
clause, which no design source projects, so C4.2 joins the criteria no scored system clears (now eight). On C4.4
three units stand (Participatory Economics, CCO-PTF-CIP-SZH flagged, Integral) and Degrowth falls. Of part (a)'s
three units re-read on v2.0, Market Socialism's C4.4 returns to 1.0. Net −3.0 points on the published structure;
no tier changes. Harness v22, **91 of 91**, byte-identical on a second run. No published score changed.

## 1. Session-start checks

s46 landed: `main` and tag `s46` at `f379254`. `session_check.py --tag s46 --files 273 --digest
3a93a8b8b548fc35affb645d045af4c7 --handoff NEEC_Project_Handoff_46.md`: ALL PASS (tags s34–s46; 273 files; digest
match; harness v21 90 of 90 byte-identical; latest Actions run on main, run 61 at `f379254`, completed/success);
Simulation `cd0ceec` and Research Hub `8e8a6ba` unchanged. Network: worldjusticeproject.org, who.int,
ghoapi.azureedge.net, freedomhouse.org, api.worldbank.org and v-dem.net answered 200; imf.org's front page answered
403 (its data hosts were not needed and not tested).

## 2. What changed

- **Record** (`NEEC_Criteria_v2_s45.md`, amended in place; tag `s46` keeps its prior text): decision **47.1**
  (under the delegation, ▲). C4.6 clause 3, for a configured national economy, reads "a World Justice Project
  sub-factor 6.2 score of 0.77 or more", compared at the Index's two published decimals. The reasons: the Index
  normalizes its scores against a 2015 base (its 2025 Methodology), so a point on its scale has no meaning of its own;
  it publishes no bands; the upper quartile is the conventional top group and the nearest the Index comes to C2.6's
  Freedom House top band. It is 0.7665 (inclusive) or 0.7712 (exclusive), 0.77 on both; 36 of 143 jurisdictions meet
  it, and the quartile lay between 0.75 and 0.78 in every edition from 2014 to 2025. Fixed as a figure, it does not
  move with later editions. The sub-factor's questions ask whether an environmental or public-health authority's
  notice to a polluter or food producer ends in compliance or in bribery or influence. *Indicative consequence (2025
  edition):* the United States (0.87), Denmark, Finland, Norway, Sweden (0.92–0.99) and Singapore (0.94) meet it;
  Qatar (0.66) and China (0.61) do not. Every bar from 0.67 to 0.87 gives the same verdicts; the recorded alternative,
  the median (0.61), would pass all eight. The Index does not cover the Soviet Union, Cuba or North Korea, so
  Centrally Planned Socialism's clause 3 needs the one reading for historical configurations that its class I
  re-checks need anyway (stage 2). **47.2** (correction): the record's status line said draft.6 with six edits; it
  now says draft.8, seven. Sections 4, 6, 8 and 9 and decision 46.4 now say the bar is fixed.
- **`wjp_rol_sf62_2012_2025.csv`** (new): sub-factor 6.2 for every edition, 1,484 scores, extracted from
  `2025_wjp_rule_of_law_index_HISTORICAL_DATA_FILE.xlsx` (md5 `56724a01`, sheet "Historical Data"). The workbook
  itself is not committed; the extract's md5 is pinned in `criteria_v2_s45.py`.
- **`criteria_v2_s45.py`**: section 5 computes the quartiles by edition, the count at the bar, the reference
  economies' scores and the range of bars with the same verdicts, and asserts each figure 47.1 states.
- **`build_criteria.py` version 2.2**: generates draft.8 (version line, changes paragraph, Appendix B header); the
  code is otherwise unchanged. Rules A1–A7 pass; the self-test still rejects 7 of 7 planted violations, with its
  capture unchanged. The build capture is renamed `build_criteria_s47_output.txt`.
- **Part (b), seventh group** (`NEEC_Rescoring_s47.md`, `rescoring_s47.py`, output `rescoring_s47_output.txt`): the
  ten part (b) units of C4.2 and C4.4 on the v2.0 clauses, and part (a)'s three units of those criteria re-read. Each
  v2.0 clause is mapped to the Session 44 clause the R4 audit coded. Readings: 3.2, audit A codes on restated clauses
  are re-read against the new wording (six carried, one estimated); 3.3, biodiversity for designs needs a projection
  of pressure on species and habitat (Otero et al. 2024 state that no degrowth biodiversity scenarios exist yet);
  3.4, carbon as a rate; 3.5, "removal/replacement mechanisms functional" is shown by a mechanism the system's own
  sources specify (recall, fixed terms, rotation, sortition, revocation), not by a stated goal; 3.6, C4.4's
  accountability clause for a configured economy (Nordic Social Democracy, not shown, flagged toward 1.0);
  3.7, part (a)'s re-reads. **Results:** C4.2: DG, FALC, PE, CCO, INT and DE all go to 0.5. C4.4: PE, CCO (flagged,
  alternative 0.5) and INT stand; DG goes to 0.5. MMT's C4.2 and NSD's C4.4 stay 0.5; MS's C4.4 goes 0.5 → 1.0.
  First place CCO 19.0; PE 15.5; NSD, INT and DG tied at 14.5; three new dominance pairs over Doughnut Economics;
  frontier unchanged. Across the pass so far, 128 units: 11 stand, 117 at 0.5 (58.5 points). 17 D28 units remain
  for part (b). Two corrections (Report v1.6's CCO C4.2 carbon-tax claim; the Integral review's C4.4 line), a
  disclosure for the owner's design, and notes for its maintainers.
- **`run_all_checks.py` v22**: the three Session 45 checks run on the amended inputs (build capture renamed; the
  evidence check reads the WJP extract); check 91 runs `rescoring_s47.py`, unpinned because it reads the v2.0
  `criteria.json` and the pinned `criteria_s44_snapshot.json` side by side. **91 checks.** `README.md` regenerated
  (draft.8, 91 checks).

## 3. Files

14 files changed or added (one of them renamed), plus this handoff: 278 tracked files.

| File | MD5 (first 8) | Status |
|---|---|---|
| `NEEC_Criteria_v2_s45.md` | `640db5a6` | amended (47.1, 47.2) |
| `criteria.json`, `SCORING_PROTOCOL.md` | `fa5da0cd`, `f0a17a96` | regenerated (draft.8) |
| `build_criteria.py`, `build_criteria_s47_output.txt` | `485e974a`, `52dd303c` | version 2.2; capture renamed from `_s46_` and recaptured |
| `criteria_v2_s45.py`, `criteria_v2_s45_output.txt` | `c41439cb`, `d16c414c` | section 5 added; recaptured |
| `wjp_rol_sf62_2012_2025.csv` | `a636d6a2` | new (WJP extract) |
| `NEEC_Rescoring_s47.md`, `rescoring_s47.py`, `rescoring_s47_output.txt` | `0a8970f4`, `0efbfcb2`, `3f7bc63e` | new |
| `run_all_checks.py`, `run_all_checks_output.txt` | `e49de096`, `a9b005c1` | v22, recaptured |
| `README.md` | `21bf3ea3` | regenerated |
| `NEEC_Project_Handoff_47.md` | (this file) | new |

## 4. Landing

The session's last commit, "NEEC Session 47: …", is pushed on `claude/amazing-gauss-sg9i6r`; `land-session.yml`
merges it into main, reruns every check, tags `s47` and publishes the release. No owner step.

## 5. Decision register

Protocol section 13 (D2–D31) unchanged; 45.1–45.7, 46.1–46.4 and 47.1–47.2 join it when the pass ends, with the
rescoring records' readings. **For the owner, when convenient (nothing waits on them):**
- 46.2(e), unchanged: whether "time-limited" binds standing requirements (as adopted) or only orders and emergency
  powers.
- 47.1 ▲: the upper quartile (0.77) or the median (0.61). It decides Qatar's and China's C4.6 clause 3.
- Two flagged calls in the seventh group: the owner's design stands on C4.4, flagged (its non-housing Public Trust
  Foundations state no removal mechanism); Nordic Social Democracy stays 0.5 on C4.4, flagged (no source measures
  the share of major decisions accountable to those they affect).
- For v2.1, not the pass's to change: C4.4's accountability clause names no indicator and leaves "major decisions"
  undefined (record s47, section 8).

## 6. Next session (48): start here

1. Run `python3 session_check.py --tag s47 --files 278 --digest 3e3019e7d43e50a374e913732076349a --handoff NEEC_Project_Handoff_47.md`
   and expect ALL PASS. If tag `s47` is missing, read the land-session run's log and repair that first.
2. Part (b), eighth group: **C4.3** (6 units, class M: v2.0 deletes the 150%+ clause and adds the declared-axis
   scope) and **C4.5** (3 units, class D), in the form of `NEEC_Rescoring_s47.md` and `rescoring_s47.py`: map each
   v2.0 clause to the Session 44 clause the audit coded, and re-read part (a)'s units of both criteria on v2.0, as
   reading 3.7 did. Then C5.2 (4), C5.4 (2) and C5.5 (2), which finishes part (b).
3. If time remains, begin the class M re-checks with the units earlier groups scored on clauses v2.0 restates:
   v2.0's C4.1 keeps only its debt and transfer clauses, so the four part (b6) units whose debt clause was left
   not estimated (FALC, PE, INT, SWF) now turn on it.

## 7. Plan to completion (amends Handoff 46, section 7)

This session re-estimated 13 units with full clause records. Stage 2 still holds 17 part (b) units; the class I
re-checks (the 42 configured-economy units and any unit whose record cites a different measure); the class M
re-checks, clause by clause, of every unit of C1.2a, C1.3, C3.4, C4.1, C4.2, C4.3 and C5.2 not already re-read on
v2.0 (C4.2's 16 published 0.5 and 0.0 units among them); the class D rises (25 units at 0.5, among them C4.4's seven
published 0.5s); and the 69 new units. Many are quicker than this group's (published series; units already at 0.0),
but at this pace stage 2 needs **at least four more sessions, 48–51, and possibly six**. The later stages move with
it:

| Stage | Sessions | Work | Effort |
|---|---|---|---|
| 1b | 46–47 | Package C; the WJP bar (47.1), done | — |
| 2 | 47–51 (to 53 at worst) | The pass on v2.0 clauses: part (b) remainder (C4.3, C4.5, C5.2, C5.4, C5.5); class I re-checks; class M units clause by clause; class D rises; new units (69) | xhigh |
| 3 | after stage 2 (one session) | Apply the pass by generator (corpus, CSV and totals on v2.0, 29 criteria; 45.6 rounding in every generator); R5 not-shown counts; the A.4 constraint scheme (S2) and proportional tiers; band texts and examples of restated criteria; `build_replication_kit.py`'s pinned MD5s before any new kit | high |
| 4 | two sessions | Report v2.0 and Paper v2.0 | xhigh / high |
| 5 | one session | Paper v2.0 PDF from a committed build script, attached to the release | high |
| 6 | two sessions | The site, per `NEEC_Site_Design_Brief_s45.md` | high |

**Credit.** This session cannot see the Claude Code cloud credit balance; no tool available to it reports one.
The owner's cap for NEEC is $50. The longer stage 2 estimate above is the reason to check the balance now: if the
remaining sessions would exceed the cap, the owner can narrow stage 2 (for example, class I re-checks only where a
published series could change a verdict, and new units before class M re-checks of units already at 0.0).

## 8. Standing notes

- Handoff 46's standing notes stand. The network access recorded in section 1 is what stage 2's evidence work needs.
- The source files read this session that are not in the repository are identified by name and md5 where a figure
  depends on them: the WJP workbook (`56724a01`) and Integral's white paper v0.1 (`a6defc9a`, 33.5 MB, read in full
  text, unlike Session 43's summary-page reading).
