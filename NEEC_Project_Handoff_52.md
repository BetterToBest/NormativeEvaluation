# NEEC Project Handoff 52

**Session 52 · 2026-10-14 · Owner: Duke Johnson · Scorer and engineer: Claude**

> **Next session (53): Opus 5.5 at high effort, Claude Code cloud, network access as in Sessions 49 to 52.** Task: stage 2,
> the C1.2a group (below). The Jev connector may stay attached; it is optional. Then send `Continue NEEC.`

This handoff is self-contained. What holds now is in `STATE.md`; the criteria record `NEEC_Criteria_v2_s45.md` carries
decisions 52.1 to 52.10. The session scored nothing and changed no score.

## 1. What changed

The owner's opening message settled ten items from `STATE.md` and listed no answer for the rest. The session did
`STATE.md`'s items 1 to 3, with a checkpoint after each, and did not stop at a limit.

- **Decisions recorded (item 1).** W3, W4 and W9 are 52.1 to 52.3; the owner's answers are 52.4 (W1, model routing),
  52.5 (W2, shared pass module), 52.6 (W5, evidence cache, to build), 52.7 (W6, consequence triage), 52.8 (W7, Report
  Part I from rationales), 52.9 (W8, simulation pin frozen at `5a7a7b1` for v2.0; Paper v2.0 discloses the overhaul and
  that the owner maintains both the design and the model; a later version is read in v2.1) and 52.10 (W10, chat path).
  One amendment of `NEEC_Criteria_v2_s45.md` and one run of the regeneration chain (`criteria.json`'s `record_md5`
  `255180b0`, the footer of 64 `docs/` pages). The package's start-check failures were as its section 4 predicts.
- **README (item 2).** `build_readme.py`'s sentence now says a session reaches `main` by the owner's merge of its pull
  request after `harness.yml` has run on it, and that `land-session.yml` then reruns the checks and tags it.
- **Shared module (item 3, W2): `pass_common.py`.** The one copy of what every group repeated: loading, the cumulative
  state through the last part (`Pass`), the D28 rule, tier, ranks, dominance, and `run_group` (records complete, the
  rule, consequences, dominance, the ledger, anchor examples moved, the record containing every generated table). A
  group is now a readings file plus a short script and one line in `PARTS`. `python3 pass_common.py --selftest`
  rebuilds group 2.1's four generated tables from the parts before it and finds them identical to the script's own.
  The existing scripts and captures are untouched.
- **Triage (item 3, W6): `triage_s52.py`**, output `triage_s52_output.txt`. Of the 446 units on the published 26
  criteria that the pass has not re-estimated, 275 are in play (class D 30, I 115, M 130) and 171 are fixed by class.
  Each in-play unit's widest reach is tested alone. Results: 245 could change a failure count, 48 an adequacy tier, 235
  a rank, and **10 could change none**. Only CCO-PTF-CIP-SZH cannot change tier even if every unit moved the worst way;
  12 entries have no unit that can change their tier alone. Three single units could change who is first (PE C4.5, INT
  C1.2a, INT C5.2). The 69 new units cannot be carried forward and change every entry's totals. Order of groups by
  tier-capable units, then rank displacement: C1.2a, C3.5, C1.3, C1.4, C4.2, C5.2, C4.1, C4.3, C3.1, C2.3, C2.1, C2.4,
  C1.1, C4.4, C4.5, C2.5, C3.4.
- **`session_check.py`.** Its tag test now also passes when `HEAD` is a merge of the tag's commit with identical files,
  as landing by pull request produces.
- **Harness v27, 101 checks** (two added: the module's self-test, the triage), byte-identical under Python 3.11, 3.12
  and 3.13. `README.md` recaptured.

## 2. Files

New: `pass_common.py`, `pass_common_selftest_output.txt`, `triage_s52.py`, `triage_s52_output.txt`, this handoff.
Changed: `NEEC_Criteria_v2_s45.md`, `criteria.json`, `build_criteria_s50_output.txt`, `build_readme.py`, `README.md`,
64 `docs/` pages (footer), `run_all_checks.py`, `run_all_checks_output.txt`, `session_check.py`, `STATE.md`. 417 tracked
files. MD5s (first 8): `pass_common.py` d03a1c7f, `triage_s52.py` 559fe597, `run_all_checks_output.txt` 0c01bc7f, `STATE.md` 5de6affd.

## 3. Landing

One pull request into `main` from `claude/festive-planck-5vkp80` (Session 52's commit begins `NEEC Session 52: `); it
does not stack on another. The owner reviews and merges; `land-session.yml` then tags `s52`. Workflow files were not
changed. **Items awaiting the owner:** the open items in `STATE.md` (48.3 to S51-3.7); nothing blocks the next group.

## 4. Method choices not yet in the criteria record (optional, not corrections)

- **52.11, the shared module.** One module the groups import instead of each other; group scripts keep only their
  group-specific checks (scan, simulation runs, reopening conditions). Alternative: refactor the existing scripts onto
  it. Rejected: their captures are checked byte for byte and no gain justifies re-capturing 99 checks.
- **52.12, the triage's reach and key.** The widest reach the rules allow (class D rises only; class I and M units at
  0.5 or 0.0 can reach any other score; a published 1.0 only 0.5, by D28(f); re-estimated, W and U units fixed), one
  unit at a time. It is a screen, not a forecast, and says nothing of probability. The ordering key is the number of
  tier-capable units, then summed rank displacement, then units, because failure count and rank are capable for almost
  every unit and so do not separate groups. Alternative: weight by likelihood; rejected, because there is no evidence
  for a probability before a unit is read. The tier thresholds are applied to the published 26 criteria; v2.0's 29 may
  need them restated at stage 3, which the triage then reruns.
Both are carried into the record at its next amendment, in one run of the chain.

## 5. Next session (53): start here

1. `python3 session_check.py --tag s52 --files 417 --digest b36424968544afb2a8c5a13e4863acc6 --handoff NEEC_Project_Handoff_52.md` after the
   owner has merged; expect ALL PASS. If `s52` is missing, read the `land-session` run's log and repair that first. If
   the pull request is still open, branch from its head and say so in your pull request (`CLAUDE.md`).
2. **The C1.2a group**, class M, 23 entries, six units able to change a tier. Read each unit clause by clause against
   Appendix V in the D28 form; the design's C1.2a reads the model at `5a7a7b1` (reading 3.10 of
   `NEEC_Rescoring_s51.md`). Write `NEEC_Rescoring_s53.md` (readings), `rescoring_s53.py` on `pass_common.py` (add
   `("(2.2)", "rescoring_s53", "rescoring_s53.py", 53)` to `PARTS` there; its self-test finds group 2.1 by tag, so it
   keeps passing), add its check to the harness, replace
   `triage_s52_output.txt` by rerunning the triage, recapture, checkpoint.
3. Then, in a Sonnet 5.5 session, the evidence cache (W5) before the first class I group (C3.5). Then the groups in
   the order in `STATE.md`.
4. If a group turns on contestable readings, the interpretation check is optional (50.2 to 50.4).

## 6. Plan to completion

Stage 2: 17 criterion groups and the 69 new units (the Handoff 51 estimate of three to four sessions stands as an
order of magnitude only; the triage shows groups of 14 to 23 units). Stage 3, one session; stage 4, two; stage 5, one.
The owner's plan ends about 2026-10-16: smaller groups suit the chat path (decision 52.10).
