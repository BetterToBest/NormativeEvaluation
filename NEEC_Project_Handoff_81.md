> **Next session (82, the comparison): Sonnet 5.5 at medium, Claude Code cloud.** Task: write `compare_outside.py` from the
> pre-registration and run it on the reader's 696 answers and stage B's eight, as they stand (ledger S64). Reason: the
> comparison is mechanical and does not need Jev. If the answers cannot be scored as the pre-registration says, stop and
> leave it to Opus 5.5 at high.

This handoff is self-contained. What holds now is in `STATE.md`. The owner called this session 80b; it is numbered 81
because `land-session.yml` tags only numeric session numbers. The sessions after it move up by one (comparison 82,
adjudication 83, prose 84 to 88); `NEEC_OutsideReview_Prereg_s80.md` still says "Session 81's `compare_outside.py`" and
means Session 82's.

## 1. What changed (Session 81)

Nothing in the kit, runner, pre-registration or scores. The session found the outside review already launched by the owner,
read its results in `BetterToBest/compassionism-sim-results` (`neec-outside-review/r1/`, run 39372446024, 2026-10-20
05:09 UTC), checked them, and recorded what is true. No file was copied or pushed to the results repository, and no
reader or Jev call was made from this session.

## 2. What the results show

- **Reader.** 696 of 696 calls answered, all `ok`. 719 attempts: 700 returned and 19 had no HTTP answer (three units,
  retried, then `ok`). Every served model id is `nvidia/nemotron-3-ultra-550b-a55b`; every finish is `stop`; the longest
  answer is 9,602 output tokens. The parameters the runner sent are the registered ones (temperature 0.6, seed 80,
  reasoning effort high, 32,000 output tokens); whether NVIDIA's host honoured `seed` and `reasoning` is not shown.
  Clause statuses: 849 short, 593 not_shown, 335 cleared, 23 moot. The reader's `closed_book` flag is true on 572
  units, though the kit labels 373 units closed-book: the field records what the reader says it used, so the comparison must
  not treat it as the kit's mode.
- **Leak look.** No answer contains "NEEC", the owner's name, "Claude" or "Jev". The two "Anthropic" matches are
  "philanthropic". Nothing suggests a misread prompt in the answers read (the first unit's answer cites the simulation's
  page by name and figure).
- **Stage B.** 8 of 8 `ok`.
- **Jev.** 378 of 588 passes answered (189 of 294 units, both passes). The other 105 units (210 passes) were rejected by
  the TypeSafe API with HTTP 400, `{"detail": {"error_type": "max_tokens_exceeded"}}`, and no usage. They are every unit
  of C2.1 (16), C2.4 (16), C2.6 (18), C3.6 (17), C4.2 (17) and C4.6 (19), and two C4.4 units. It is not the pack's length
  alone: failures start at a request of 60,676 characters and answered requests reach 104,048; 35 of the failing requests
  had their pack cut at 200,000 characters. It is not the number of clauses (answered requests have up to five). It is a
  property of those criteria's requests, cause not found without a test call. Cost so far $0.20. The workflow retries the
  105 units every 4 hours; the retries cost nothing and cannot succeed unchanged. `DONE` is not written while any unit
  is missing, so the schedule stays on.

## 3. Decisions

- **81.1** (optional, provider; the owner's choice of 2026-10-19, recorded in `PROVIDER_NOTE.md`) the reader is called at
  NVIDIA's own API (`https://integrate.api.nvidia.com/v1`, secret `NVIDIA_API_KEY`), not OpenRouter. Same model, kit
  (manifest md5 `7174064e`), runner (md5 `7d952ac4`) and pre-registration. The pre-registration's table names OpenRouter, so
  the host is reported as a deviation beside every result. The whole run was on one host, so r1 is not split.
- **81.2** (blocker for Jev only; ledger I11) Jev's rejection of 105 units. The pre-registration is silent on a rejected
  Jev request. Until the cause is found the comparison reports Jev on the 189 units it answered, and the six criteria
  without Jev are listed as not checked, never imputed (rule of section 2 of the pre-registration, "missing").
- **81.3** (optional, ledger D63; default first) what to do about 81.2: (a) diagnose with one test call per failing
  criterion, then rerun the 105 units under the cause's fix, reported as a deviation with the fix; (b) report Jev on the
  189 units and stop; (c) drop Jev. The default is (a). It needs the owner: the key is a repository secret, and a workflow
  change needs the owner's approval in review (`CLAUDE.md`).
- **81.4** (correction to the plan) the comparison no longer waits for `DONE`: the reader and stage B are complete, and
  Jev is not part of the reader's score. The session numbers move up by one (see the note above).

## 4. Ledger entries

Applied in the same session: S63 `done`; new issue I11 (Jev's rejection; items: cause found, 105 units rerun or reported
without, the deviation recorded); new decision D63 (81.3); S64 note; `next`, `left`, `log`.

## 5. Files

`NEEC_Project_Handoff_81.md` (new); `STATE.md` (rewritten: top, the outside-review bullet, Next work items 1 and 9 to 12,
Awaiting the owner). `run_all_checks_output.txt` is unchanged (140 checks, ALL PASS at the start and the end). The
session stopped at no limit.

## 6. Next session (82): start here

1. `python3 run_all_checks.py > /tmp/out.txt; cmp /tmp/out.txt run_all_checks_output.txt` (no difference; it takes
   about 10 minutes).
2. Read the ledger: I11 and D63's `sel`; record any change as a numbered decision.
3. Clone `compassionism-sim-results` and read `neec-outside-review/r1/results/reader.jsonl`, `stage_b.jsonl`,
   `jev.jsonl` and `heartbeat.json` (never print them; scripts print summaries).
4. Write `compare_outside.py` from `NEEC_OutsideReview_Prereg_s80.md`, sections 2 to 7, and add it to the harness with a
   negative control as the other scripts have. Run it: agreement by unit and clause; the reader's lean on the
   calibration set; the reader against NEEC; Jev against both on the 189 units it answered; stage B; the standing three
   ways. State the host deviation (81.1) and Jev's gap (81.2) beside the results.
5. Write the record (`NEEC_OutsideReview_Result_s82.md`); change no score. Checkpoint, then finish as `CLAUDE.md` says.
   Session 83 (Opus 5.5 at xhigh for CCO-PTF-CIP-SZH and the top five, high for the rest) adjudicates the disagreements.
