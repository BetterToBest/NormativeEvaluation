# NEEC Project Handoff 68

> **Next session (69): Claude Code, Opus 5.5 at high** (the owner upgraded to Pro on 2026-10-18, so decision 67.2's Chat path is not needed).
> Task: Report v2.0 Part I, one domain per group (s41), then the Paper v2.0 disclosures (s42) and the limits page (s44).
> Reason: that is judgment prose, which the harness cannot check (STATE.md, "Model routing"). This session's work was mechanical
> (a generator, the site's links, two harness checks) and ran on Sonnet 5.5.

## 1. What changed (Session 68)

The owner asked to continue the NEEC research from `BetterToBest/NormativeEvaluation`, believing the next step was applying
stage 3 (`apply_pass_s65.py`), and asked whether applying it would give each system clean evidence files: reports that link
straight to the evidence instead of sending a reader into the long scoring documents. Two findings, then the work.

- **Stage 3 was already applied.** `apply_pass_s65.py --check` passes (check 112); `neec_corpus_v2.json`, `neec_scores_v2.csv`
  and `summary_blocks_v2.json` exist; `site/config.json` has `scores.publish` true and names the v2 files (decision 66.1);
  the Session 66 pull request is merged and `build_site.py --check` reports the v2 scores published. Nothing is left to apply.
- **Stage 3 does not touch evidence files.** It writes those three files only. Each system's Evidence section linked the long
  scoring documents: Report v1.6 (285 KB) and the Step 1c retrofit for 12 entries, Paper v1.4 as well for Integral, and a
  48 to 72 KB scoring document for each of the other ten. Clean evidence reports did not exist.
- **Built: `build_evidence.py` and `evidence/`** (decision 68.1). One report per system (`evidence/<code>.md`, 23 files) and
  an index (`evidence/index.md`). Each report has a section for each of the 29 criteria: the score; for the 496 cells a unit
  of the pass reads (427 re-read, 69 new in v2.0) one row per clause with its status, reading and source, each
  `evidence_cache/` data file linked; the close call (104 in all, from the blocks); the pass's note and any reason for a 0.0;
  a link to the unit's heading in its rescoring record (495 of 496; the 496th is the owner's decision 58.1, linked to
  `owner_s58.py`); and the published (v1) rationale, quoted and linked to its line in the scoring document (all 598 published
  cells, the 171 the pass did not read included). Nothing in a report is typed or newly judged: every figure is read from the
  files the pass already holds. The script asserts that each score and each unit's verdict equals the corpus, each total equals
  the blocks', and every link target exists.
- **The site links them** (decision 68.2). `build_site.py`: each system page's Evidence section leads with its report, each
  criterion row there gets an "evidence" link to that criterion's section (`evidence/<code>.md#c4-1`), the systems index shows
  "Evidence report" first in each row, and the build asserts that every system's report exists. `docs/` rebuilt: 24 files
  changed (23 system pages and `systems/index.html`); the site still has 77 files.
- **Harness v38, 114 checks.** Check 113 is `build_evidence.py --check` (every file of `evidence/` compared byte for byte);
  check 114 is its negative control (a swapped report must be rejected). `build_site.py`'s check now also copies `evidence/`.

No score, criterion, corpus file, record or pass script changed.

## 2. Decisions (all optional records; none is a correction)

- **68.1 (optional; the owner's request, 2026-10-17).** Per-system evidence reports, generated, in `evidence/`. They add no
  judgment: a cell the pass did not read says so and shows its published rationale; a unit is shown as the pass recorded it.
- **68.2 (optional).** The site's system pages and systems index link the reports (`build_site.py`); `docs/` rebuilt by it.
- **68.3 (optional).** Where a unit's clause list has a different length from v2.0's, the report shows the clauses as recorded
  under a caption that says so, and does not attach v2.0's clause text to them. This affects 18 units (C2.5 ten, C4.1 eight;
  below).

## 3. For the owner

1. **18 units carry their earlier clause lists.** C2.5's ten (part (b5)) were read on four clauses; v2.0 deleted the fourth
   (class D), the case the Session 65 record treats ("keeps or raises"). C4.1's eight designs (Degrowth, Fully Automated Luxury
   Communism, Participatory Economics, CCO-PTF-CIP-SZH, Integral, Doughnut Economics, Sovereign Wealth Fund Statism, Ostrom
   Commons; part (b6), Session 43) were read on a four-clause list before v2.0 restated C4.1 to two clauses (class M). The
   reports show both as recorded. Whether the eight C4.1 units should be re-read on v2.0's two clauses is the owner's call; I
   did not find the Session 65 record addressing those eight by name.
2. **The ledger could not be read this session** (the artifact was not shared with it), so nothing was written there; see
   "Ledger entries". I also could not see what d51's dropped "Evidence Ledger (s7)" covered. `evidence/` is a different thing
   if s7 meant a ledger of evidence items; if it meant these reports, they now exist.
3. **After the merge, check two GitHub behaviours** the reports rely on and I could not test: a link such as
   `.../evidence/sq.md#c4-1` scrolls to the criterion's section, and `...NEEC_Report_v1_6.md?plain=1#L292` opens the source
   view at that line. If either fails, the fix is in `build_evidence.py` (`anchor`, `Ctx.blob`).
4. `README.md` is generated from `neec_scores.csv` (the v1 scores) and still describes 26 criteria; not touched here.

## 4. Next session (69): start here

1. Handoff 67 names no start-of-session check. Run `python3 apply_pass_s65.py --check` and `python3 build_evidence.py --check`: expect no difference.
2. **s41, Report v2.0 Part I, one domain per group** (Handoff 67, section 3; decision 52.8 sets the method). In Claude Code, read
   the domain's rows of `neec_scores_v2.csv` and the domain's criteria's sections of the rescoring records by `grep`, never whole;
   the reports in `evidence/` carry the same units in one place per system and may serve as the source tables. Push a checkpoint
   after each domain.
3. s42 (Paper v2.0 disclosures), s44 (the limits page), then the landing (s43): remove `provisional_note` from `site/config.json`,
   `python3 build_site.py`, the harness.
4. **Whenever a score, a record, the blocks or a scoring document changes**, run `python3 build_evidence.py` and then
   `python3 build_site.py`; the harness rejects a stale `evidence/` (check 113).

## 5. Ledger entries (to apply when the artifact tools reach the ledger)

None awaits the owner. For the record: a step "Per-system evidence reports" done in Session 68 (decisions 68.1 to 68.3, the
three files and `evidence/` above); and, for the owner's attention, an issue "18 units carry pre-v2.0 clause lists; the eight
C4.1 designs (part (b6)) may need a re-read on v2.0's two clauses" (severity: low; section 3, item 1).
