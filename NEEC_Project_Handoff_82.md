> **Next session (83, adjudication): Opus 5.5, xhigh for CCO-PTF-CIP-SZH and the top five, high for the rest, Claude Code cloud.**
> Task: adjudicate the 177 verdict disagreements of the outside review on the sources (ledger S65). Reason: contested readings that
> decide first place; the reader's total puts Nordic Social Democracy first, and the CCO-PTF-CIP-SZH lean excludes 0.

This handoff is self-contained. What holds now is in `STATE.md`.

## 1. What changed (Session 82, ledger S64)

`compare_outside.py` was written from the pre-registration and run on the reader's 696 answers, Jev's 294 units and stage B's eight.
No score, reading, criterion or `docs/` file changed; Jev set no verdict. The record is `NEEC_OutsideReview_Result_s82.md`;
every table is in `compare_outside_output.txt`. The run's own result files are not changed.

Headline: the reader's verdict equals NEEC's on 490 of 667 first readings (73.5%; 74.4% against NEEC without the owner's decisions);
clause statuses on 56.1% of 1,208 clauses (R excluded). Calibration lean +0.012. CCO-PTF-CIP-SZH's lean is -0.103 (difference
-0.115, interval [-0.205, -0.027]), which comes from the owner-decided cells: the reader reads seven of the eight at 0.5; stage B
moved one (Ostrom C3.4 to 1.0). Nordic Social Democracy +0.103 (difference interval [+0.000, +0.185], marginal). Under the reader's
verdicts first place changes to Nordic Social Democracy (18.5), CCO-PTF-CIP-SZH 14.5, rank 7. Jev is reported apart, whole-pack
(189 units) and windowed (105): section 4 of the record. The windowed units do not show the expected lean toward not_shown in the
aggregate (77.7% against 80.7%), but they are different criteria. The host deviation (NVIDIA's API, 81.1) is stated in the record.

## 2. Files

`compare_outside.py`, `compare_outside_output.txt`, `compare_outside_negative_output.txt` (new); `NEEC_OutsideReview_Result_s82.md`,
`NEEC_Project_Handoff_82.md` (new); `outside_review_r1/kit_units.jsonl` and `outside_review_r1/results/{reader,jev,stage_b}.jsonl.gz`
(committed copies of the results repository's files, byte-identical once decompressed, so the harness can rerun the comparison);
`run_all_checks.py` (v51, two checks added: 142) and `run_all_checks_output.txt` (regenerated); `STATE.md` (rewritten).

## 3. Decisions

- **82.1** (optional; ledger D64) The pre-registration is silent on five points, and the script reads them as stated in its header
  (R1 clause status R excluded from the primary clause rate and also shown counted as short or not_shown; R2 both closed-book
  definitions; R3 Jev pass by pass and on stable clauses; R4 moot left out of Jev comparisons; R5 "closed-book source" from the source
  field). None changes a verdict figure. If the owner prefers another reading, `compare_outside.py` is rerun.
- **82.2** (optional, tooling) The results are committed to this repository in gzip, as `outside_review_r1/results/`, so the harness
  can rerun the comparison; the results repository remains the source.
- **82.3** (correction to the record of Session 81) Session numbering: this session is 82; adjudication is 83, prose 84 to 88.

## 4. Ledger entries

Applied in the same session: S64 `done` (archived); D64 added (82.1; `conf` false); S65's text pointed at the record; `next`, `left`,
`updated`, `log`. I11 (ready) and D63 stay the owner's to confirm.

## 5. Next session (83): start here

1. `python3 run_all_checks.py > /tmp/out.txt; cmp /tmp/out.txt run_all_checks_output.txt` (no difference; about 10 minutes).
2. Read the ledger (S65, D64, I9, I11) and `NEEC_OutsideReview_Result_s82.md`; grep `compare_outside_output.txt` for tables 3e (disagreements in
   the top five), 6c (window conflicts) and 6d (Jev and the reader agree against NEEC: read first).
3. Adjudicate each disagreement on the sources by one rule: the protocol as written, the unit's pack, the reader's estimates and
   sources (`outside_review_r1/results/reader.jsonl.gz`, field `final`), Jev's clause choices, NEEC's record. Changes by generator;
   CCO-PTF-CIP-SZH's go to the owner (57.2). Publish the reader's result on every CCO-PTF-CIP-SZH and owner-decided unit either way.
4. Settle I9 (C3.4 clause 3, bearing on decision 79.4), rerun `neec_weighting_robustness_analysis_v2.py`, freeze the scores.
5. Finish as `CLAUDE.md` says. Session 84 starts the prose.
