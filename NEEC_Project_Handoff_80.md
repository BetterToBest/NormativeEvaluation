> **Next session (80b, the launch): Sonnet 5.5 at medium, Claude Code cloud.** Task: copy the kit, runner and workflow into
> `compassionism-sim-results`, read the three-unit dry run, launch (ledger S63's last part). Send `Continue NEEC.` after the
> owner's setup (ledger S66: the Claude GitHub App on that repository, and an `OPENROUTER_API_KEY` secret there). Reason:
> the rest is mechanical; if the dry run shows a fault in what the reader sees, stop and leave it to Opus 5.5 at high.

This handoff is self-contained. What holds now is in `STATE.md`.

## 1. What changed (Session 80)

The session built the outside blind review (decisions 79.6 and 79.8; plan `NEEC_OutsideReview_Plan_s79.md`, sections 3
to 6). It did not launch it: the results repository refused the push (decision 80.8).

- **Start.** Harness ALL PASS (135). A Session 79 commit made after its pull request merged (decision 79.8, the move to
  free tiers) was found on `claude/neec-s79-owner-decisions` and merged into this branch. The ledger showed D58 to D60
  confirmed and I6 and I8 confirmed resolved (decision 80.1).
- **The owner's setup, as found.** `compassionism-sim-results` has a `test-keys` workflow: `TYPESAFE_API_KEY` is set
  and Jev answers (`jev-1.13.0`). The other route, GitHub Models, was retired on 2026-07-30. Its endpoint returns HTTP 200
  with no completion. The reader therefore moves to OpenRouter's free models (decision 80.2). The session's network
  reaches OpenRouter, TypeSafe and `bettertobest.github.io`. From this container `models.github.ai` is stubbed.
- **The kit** (`outside_kit.py`, `outside_kit/`, 250 files). It holds what the reader sees and nothing else:
  - the instructions;
  - the protocol's sections 2.1 to 2.3, 3.1, 3.2, 4.1, 4.2 and 4.6, with every sentence naming a system, record,
    script or session dropped without a marker (R8);
  - the 29 criteria without their worked examples;
  - 23 system files (name, kind, configuration);
  - the source packs (decision 80.3);
  - the order of the 696 calls: 29 CCO-PTF-CIP-SZH, 116 for the top five's other four, CCO-PTF-CIP-SZH's 29 again,
    135 close calls, 387 calibration units;
  - eight stage B arguments, the answer schema, and a manifest of md5s.

  The design texts are cached in `outside_kit_sources/`, verified by md5 (`--fetch` rebuilds them from the pinned
  clones and the white paper's URL):
  - the Research Hub at `8e8a6ba`;
  - the simulation at `d10ed6e`, with its findings and study pages rendered by `render_pages.js`;
  - Integral's white paper v0.1;
  - the text layers of two cached PDFs.

  The author's name and address are redacted.

  667 units: 294 with a source pack, 373 closed-book. CCO-PTF-CIP-SZH and Integral have their own documents on every
  criterion; most book-published designs are closed-book. This asymmetry is NEEC's own evidence base, and the
  pre-registration reports closed-book units apart.
- **The leak check** (`outside_kit_check.py`). It builds all 696 prompts and 294 Jev states with the runner's own
  functions and scans them for seven kinds of leak:
  - a tier name;
  - a NEEC record, script or session;
  - the author's name or address;
  - a withheld marker;
  - a stage B sentence;
  - another system's name in the rules, criteria or system files;
  - a verdict, status or flag in the packs.

  The first scan found 150 hits:
  - a "Duke Johnson¹" the redaction missed;
  - a C4.2 sentence naming a tier;
  - an Integral example split off by a colon (it would have shown NEEC's reading of Integral's C2.2);
  - false positives ("ledger" in the designs, "estimates not shown" in a paper).

  Each was fixed at its source or the pattern narrowed. The scan now finds 0. The negative control plants one leak of
  each kind, and each is caught alone.
- **The runner** (`outside_review_runner.py`, standard library). It does the following:
  - assembles each prompt from the kit alone;
  - calls the pinned model through OpenRouter (decision 80.4), one call per unit (decision 80.5);
  - validates the `FINAL:` object (clause count, statuses, the clause rule, the 0.0 basis), asking twice more on an
    invalid answer;
  - handles the free tier's per-minute waits and its daily cap;
  - runs Jev over the 294 packs twice (decision 80.6);
  - runs stage B only for units whose blind reading was pushed by an earlier run;
  - resumes where it stopped, writes `heartbeat.json`, pushes every 20 minutes, and writes `DONE` at the end.

  Its self-test passes 15 checks offline.
- **The pre-registration** (`NEEC_OutsideReview_Prereg_s80.md`). It was committed and pushed (`785b2ed`) before any call.
  It pins the kit (manifest `7174064e`), the runner (`7d952ac4`), the NEEC files compared, and the model rule. It sets:
  - verdict agreement by group, system and criterion, with up or down;
  - the reader's lean on the 387 calibration units, and CCO-PTF-CIP-SZH's lean against it with a bootstrap interval;
  - the reader's consistency on the CCO-PTF-CIP-SZH repeat;
  - Jev's agreement;
  - the three standings;
  - stage B, kept apart;
  - adjudication by one rule in Session 82;
  - the outside result on every owner-decided unit is published either way.
- **The results repository.** The workflow (`neec-outside-review.yml`), README and dry-run list were written and
  committed locally for `compassionism-sim-results`, under `neec-outside-review/r1/`. The workflow runs every 4 hours
  for up to 330 minutes, keeps the dry run in its own folder, and disables its schedule at `DONE` (decision 80.7).

  The push was refused (403 on git and on the API: the Claude GitHub App is not installed on that repository), so the
  three files are kept in `outside_review_r1/` here (decision 80.8). Nothing has run, and no reader or Jev call was made.
- **Harness v50, 140 checks:**
  - `outside_kit.py --check`, and its negative control (a criterion file swapped);
  - `outside_kit_check.py`, and `--negative`;
  - `outside_review_runner.py --selftest`.

Files:
- new: `outside_kit.py`, `outside_kit/`, `outside_kit_sources/`, `outside_kit_check.py`, `outside_review_runner.py`,
  `render_pages.js`, `NEEC_OutsideReview_Prereg_s80.md`, `outside_review_r1/`;
- captured outputs: `outside_kit_output.txt`, `outside_kit_negative_output.txt`, `outside_kit_check_output.txt`,
  `outside_kit_check_negative_output.txt`, `outside_review_runner_selftest_output.txt`;
- changed: `run_all_checks.py`, `run_all_checks_output.txt`, `STATE.md`, this handoff; and, from Session 79's late
  commit, `NEEC_OutsideReview_Plan_s79.md`, `NEEC_Project_Handoff_79.md`.

## 2. Decisions

Recorded in full in `STATE.md`, "Decided (Session 80)".

- **80.1** (owner, in the ledger) D58 to D60 confirmed; I6 and I8 resolved; 79.8 merged in.
- **80.2** (correction) GitHub Models is retired; the reader moves to OpenRouter's free models.
- **80.3** (optional, method) the source-pack rule, the dropped examples and sentences, the redaction, closed-book use
  labelled.
- **80.4** (optional; ledger D61) the reader `nvidia/nemotron-3-ultra-550b-a55b:free`; alternative
  `thinkingmachines/inkling:free`.
- **80.5** (optional, method) one call per unit with the whole pack; no `READ:` turns, no search.
- **80.6** (optional, method) Jev on the 294 units with a pack (800 clauses), twice.
- **80.7** (optional, tooling) the workflow's schedule and limits; harness v50.
- **80.8** (blocker) no push access to `compassionism-sim-results`; launch waits on the owner (S66).

## 3. Ledger entries

Applied directly to the ledger this session (`ArtifactData`, `projects/neec`):
- S66 rewritten with the steps below and left `todo`;
- S63 set `blocked`, linked to S66;
- D61 added (the reader model);
- `next`, `left` and `log` updated.

Nothing is queued for a later session to apply.

## 4. The owner's setup (ledger S66)

1. **Give the Claude GitHub App access to `compassionism-sim-results`.**
   - On GitHub: your avatar, then Settings, then Applications, then Installed GitHub Apps, then Claude, then Configure.
   - Under "Repository access", add `compassionism-sim-results` (or choose all repositories), then Save.
   - If GitHub asks you to approve new permissions for the app, approve them. The workflow file needs the app's
     "Workflows" permission.
   - If it is not listed there, install it from https://github.com/apps/claude/installations/select_target.
2. **An OpenRouter key.**
   - Sign in at https://openrouter.ai, open Keys, and create a key.
   - In `compassionism-sim-results`, go to Settings, then Secrets and variables, then Actions, then New repository
     secret. Name it `OPENROUTER_API_KEY` and paste the key.
3. **Optional: $10 of OpenRouter credit.** Buying it once raises the free models' cap from 50 to 1,000 calls a day. That
   cuts the run from about 15 days to about one. The free models do not draw on the credit.
4. **Optional: another model.** On the same Actions settings page, under the Variables tab, add `READER_MODEL` (ledger
   D61).
5. `TYPESAFE_API_KEY` is set and works; nothing to do. The `test-keys` workflow can be deleted.

## 5. Next session (80b): start here

1. Start-of-session check: `python3 run_all_checks.py > /tmp/out.txt; cmp /tmp/out.txt run_all_checks_output.txt`,
   expecting no difference (140 checks).
2. Read the ledger: S66's state and D61's `sel`. Record any change as a numbered decision.
3. If S66 is done, set up the results repository:
   - clone `compassionism-sim-results` and branch;
   - copy `outside_kit/` to `neec-outside-review/r1/kit/`;
   - copy `outside_review_runner.py`, and `NEEC_OutsideReview_Prereg_s80.md` as `PREREG.md`, to
     `neec-outside-review/r1/`;
   - copy `outside_review_r1/neec-outside-review.yml` to `.github/workflows/`;
   - copy `outside_review_r1/README.md` and `DRYRUN` to `neec-outside-review/r1/`.

   Push. The push runs the dry run.
4. Read `neec-outside-review/r1/dryrun/`:
   - `heartbeat.json`;
   - `results/reader.jsonl`: three units, each `ok`, the model served recorded;
   - `results/jev.jsonl`: two units, two passes.

   Look for any sign of a leak or a misread prompt. Then open a pull request there for the owner to merge; the merge
   starts the schedule. Where D61 names another model, the owner sets `READER_MODEL` before the merge.
5. Checkpoint, then finish as `CLAUDE.md` says. Session 81 (Sonnet 5.5 at medium) starts when the heartbeat shows `DONE`.
