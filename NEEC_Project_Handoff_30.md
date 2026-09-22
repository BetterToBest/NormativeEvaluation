# NEEC Project Handoff — Session 30

**Date:** 2026-09-19. **Owner:** Duke Johnson. **Scorer/engineer:** Claude.
**Session result:** the kit gap is closed and the first pilot is ready to run.
`verify_doughnut.py` is reconstructed and the Doughnut Economics Verification
section restated (D22); `neec_entry.py` has a candidate mode; the corpus exists
as one JSON file (D23); the blind replication kit for the Ostrom pilot is built,
with a blind copy of the protocol (D24). Protocol v2.0-draft.4. Harness v6:
**56/56 passed**, byte-identical on a second run.

---

## What this session did

1. **Fingerprint check of the Session 29 state: clean.** All 22 Session 29
   file MD5s matched Handoff 29; the mount held 138 files; the v5 harness
   reproduced 47/47, byte-identical to its captured output (`0fd5fbfd`).
2. **Owner review.** The owner read Handoff 29's wording judgment calls and
   accepted them. They are closed.
3. **`verify_doughnut.py`, reconstructed (D22).** The owner asked for the
   script, which could not be found. The Session 14 original was never added
   to the project files and cannot be recovered. The new script says in its
   header that it is a Session 30 reconstruction, not that script. It:
   - reads the vector from the document's 26 criterion headings (never
     retyped);
   - repeats the two checks the Verification section describes;
   - reproduces the recorded transcript byte for byte;
   - checks the vector against canonical `SCORES` and `PUBLISHED`, the CSV
     row and the summary block, and the block's flags against the headings
     marked contestable.

   It passes 24/24. Four altered copies of the document (one score changed,
   one transcript line changed, the total changed, one flag mark removed)
   were each caught. That test was ad hoc; it is not in the harness.
4. **The D22 restatement.** With a file named `verify_doughnut.py` on file,
   the D14 wording "an ad hoc script (`verify_doughnut.py`) that is not among
   the project files" no longer read true. `restate_s30.py` restates the
   section in place from its pinned Session 29 snapshot, using the D14
   generator's own edit function. The diff is exactly two paragraphs:
   - DE-05: the Session 14 check is described without the "not on file"
     claim;
   - D22: a sentence says what the reconstruction is and does.

   The DE-06 phrase, the transcript and the block are untouched.
   `verify_comparative_claims.py` (Session 30) checks DE-05 on its new wording
   and adds group **[K]**: the phrases in place, the superseded D14 wording
   gone, and `verify_doughnut.py` pinned and describing itself as a
   reconstruction. It runs **419 checks, all pass**. Its negative control
   rejects the Session 29 Doughnut text on exactly those four checks.
5. **`neec_entry.py --candidate`** (protocol 9.3). This closes the kit gap
   from Handoffs 28 and 29.
   - **What candidate mode checks.** The key, the display name and the code
     must all be absent from the corpus. The display name must begin with the
     key, and the record must be `native-v2`. Every internal check runs; the
     vector is not compared with the corpus. The peer matrix is printed for
     every candidate, with the peers' scope classes; a candidate without
     declared peers is told that section 5 asks for them.
   - **Self-test.** `--selftest --candidate` builds one synthetic candidate
     and seven altered ones; all eight cases behave as expected.
   - **Corpus-file mode.** When the canonical script is absent, as in a kit,
     the corpus is read from `neec_corpus.json`. Beside the canonical script,
     that file must match the canonical corpus exactly or the run stops.
   - **Nothing earlier changed.** All six earlier `neec_entry` outputs are
     byte-identical under the new version. The D14 generator pins
     `neec_entry.py` by MD5, so its check now runs against the pinned Session
     29 copy.
6. **`neec_corpus.json` (D23).** `neec_scores.csv` has no criterion vectors,
   so neither peer calibration nor a blind corpus could be read from it.
   `build_corpus_file.py` writes each entry's key, code, display name, scope
   class and vector. Sources: the canonical script, the CSV, and the blocks in
   the eleven documents (every block valid, all 23 entries covered once). It
   reads the file back through `neec_entry.py`'s loader and compares it with
   the canonical corpus.
7. **The first blind replication kit (D24).**
   - **The leak.** The protocol itself reports Ostrom's results: the 3.5
     worked example gives both joint readings; the 6.4 example gives its
     20-flag enumeration; 3.1 gives its scope class; 3.4(b) and 11.6 describe
     the pilot. A replicator given the protocol as it stood would not have
     been blind, above all on the scope question the pilot exists to test.
   - **The builder.** `build_replication_kit.py OS` writes a blind copy of
     the protocol: 8 passages withheld and marked where they stood, and one
     example code (`OS`) replaced by `GEO`; a header note says so, and no rule
     changes. It also writes the corpus with the target withheld (22 entries),
     a brief, and byte copies of `criteria.json`, the two schemas and
     `neec_entry.py`.
   - **Its checks.** It scans every kit file except the brief for the
     target's names, code and signature figures (**0 hits**). It runs
     `neec_entry.py`'s two self-tests inside the kit, with no canonical
     script present (both pass).
   - **The archive.** It writes `neec_replication_kit_OS.zip`: 7 files,
     stored, fixed timestamps, MD5 `81a254e8`, identical on rebuild.
   - **The maintainers' baseline.** The original Ostrom entry, run as a
     candidate against the kit's corpus, is validated with its D9 peer
     matrix (nearest neighbours: Georgism, Mutual Credit / LETS, Universal
     Basic Services).
8. **Protocol v2.0-draft.4.** Section by section:
   - 1.2: `neec_corpus.json` added; the blind corpus is named.
   - 5.2: the draft matrix command is now `--candidate`.
   - 9.2: `key` for a candidate.
   - 9.3: candidate mode.
   - 10.2: insertion checks the entry as a candidate first, and regenerates
     the corpus file.
   - Section 11: kit, blind copy, validation, comparison, record, pilot
     (items 1–6).
   - Section 12: what is checked.
   - Section 13: D22–D24, with notes.
   - Appendix A: new files.

   Section 3.1 is untouched, since `stage_blocks_s28.py` parses it.
9. **Correction applied:** `neec_scores_data_dictionary.md` column 10 still
   called D21 open. It now states the adopted rule, and the file section
   points to `neec_corpus.json`.
10. **Harness v6** (`run_all_checks.py`, 56 checks). Nine new checks:
    - `verify_doughnut.py`;
    - `restate_s30.py`;
    - the Session 30 claims verifier, and its negative control;
    - `build_corpus_file.py`;
    - the candidate self-test;
    - the candidate negative control (a canonical entry is rejected);
    - the kit builder (blind protocol, corpus and brief compared byte for
      byte);
    - the pilot baseline.

    Three earlier checks were redirected to pinned Session 29 copies: the D14
    generator (Doughnut output compared with its snapshot; `neec_entry.py` as
    it pins it), and the Session 29 claims verifier and its negative control.
    All earlier outputs reproduce unchanged.
11. **Repository check.** `github.com/BetterToBest/NormativeEvaluation`
    exists and is empty. GitHub Pages is not enabled. Its casing matches the
    schemas' `$id` URLs.

---

## Files (update the mount with these)

**Replace** (same names):

| File | MD5 | Note |
|---|---|---|
| `NEEC_DoughnutEconomics_scoring_scratch.md` | `9953fe32` | D22: Verification section restated |
| `SCORING_PROTOCOL.md` | `13e382bc` | v2.0-draft.4 |
| `neec_entry.py` | `6ddd3b0a` | candidate mode; corpus-file mode |
| `neec_scores_data_dictionary.md` | `36592680` | D21 note corrected |
| `verify_comparative_claims.py` | `257c7a19` | Session 30: 419 checks, group [K] |
| `run_all_checks.py` | `177a2e1e` | v6, 56 checks |
| `run_all_checks_output.txt` | `735c28ed` | 56/56 |

**Add:**

| File | MD5 | Role |
|---|---|---|
| `NEEC_DoughnutEconomics_scoring_scratch_s29_snapshot.md` | `1c527415` | the document as the D14 pass left it |
| `verify_comparative_claims_s29_snapshot.py` | `0af89bed` | the Session 29 verifier, pinned |
| `neec_entry_s29_snapshot.py` | `b9bf5acf` | the Session 29 entry verifier, pinned |
| `verify_doughnut.py` | `2946cf0f` | D22 reconstruction |
| `verify_doughnut_output.txt` | `65bdaff9` | 24/24 |
| `restate_s30.py` | `c15bed57` | the D22 generator |
| `restate_s30_output.txt` | `fe5686fb` | its output |
| `verify_claims_s30_output.txt` | `a16f9a53` | 419/419 |
| `verify_claims_s30_negative_output.txt` | `ee729d7e` | negative control (exit 1) |
| `build_corpus_file.py` | `adad7d3b` | D23 builder |
| `build_corpus_file_output.txt` | `ee9ecc42` | its output |
| `neec_corpus.json` | `ba3c7f70` | the corpus, 23 entries |
| `neec_entry_selftest_candidate_output.txt` | `69c1ee1b` | 8 of 8 |
| `neec_entry_candidate_negative_output.txt` | `64838309` | a canonical entry rejected (exit 1) |
| `build_replication_kit.py` | `35717ebd` | D24 kit builder |
| `build_replication_kit_OS_output.txt` | `e2f748bf` | its manifest (every kit file's MD5) |
| `replication_kit_OS_SCORING_PROTOCOL.md` | `c824a8d2` | the kit's blind protocol, for review |
| `replication_kit_OS_neec_corpus.json` | `9e803a00` | the kit's corpus (22 entries) |
| `replication_kit_OS_REPLICATION_BRIEF.md` | `1441b665` | the kit's brief, for review |
| `neec_entry_candidate_OS_blind_output.txt` | `6a088f00` | the pilot baseline |
| `NEEC_Project_Handoff_30.md` | — | this file |

**Deliver, don't mount:** `neec_replication_kit_OS.zip` (`81a254e8`) is what
the replicator receives. The harness regenerates its contents, so it does not
need to be on the mount; if it is lost, `python3 build_replication_kit.py OS`
rebuilds it byte for byte.

The mount then holds 159 files, or 158 if Handoff 29 is removed.
**Expected:** `python3 run_all_checks.py` → 56 passed, output MD5 `735c28ed`.

---

## Decisions

- D2, D3(a), D3(b), D6, D8–D21: closed.
- **D22: adopted and applied** (Session 30, at the owner's request; the owner
  replied "continue" to the proposed wording). The two restated paragraphs
  are open to wording review. Reverting is one mount change: restore the
  `_s29_snapshot` text and drop the Session 30 checks.
- **D23: adopted for tooling.** `neec_corpus.json` is used by candidate mode
  and the kits. **Owner to decide:** publish it in the repository beside the
  CSV as the corpus's machine-readable dataset (recommended; the CSV lacks
  the vectors), or keep it internal. This can wait until the repository step.
- **D24: adopted, awaiting owner confirmation before the pilot runs.** Read
  the header note of `replication_kit_OS_SCORING_PROTOCOL.md` and the list of
  withheld passages in `build_replication_kit_OS_output.txt`. The trade-off:
  the replicator's protocol differs from the canonical one, but only in
  passages that report the target's scoring, each marked where it stood.
- **D18(b)** stays deferred to the pilot.

---

## Running the pilot (owner)

1. **Confirm D24**, and read the brief (`replication_kit_OS_REPLICATION_BRIEF.md`).
2. **Choose a replicator with no access to NEEC's Ostrom scoring.** Options:
   - an incognito claude.ai chat outside the NEEC Project (no project files,
     no memory), with the seven unzipped files uploaded and code execution on;
   - Claude Code in a new, empty folder holding only the unzipped kit;
   - another AI system, or a human scorer.
3. **Blindness depends on timing.** Run the pilot before the repository
   publishes the Ostrom scoring document, or keep that document out of the
   repository until the pilot is back. The brief tells the replicator not to
   consult NEEC material, but it cannot prevent it.
4. **Start the replicator.** Give it only the kit and a prompt such as:
   "Follow REPLICATION_BRIEF.md."
5. **Collect two things:** the replicator's scoring document
   (`NEEC_OstromCommons_replication_scoring.md`) and its `neec_entry.py
   --candidate` output. Add both to the NEEC Project.

---

## Remaining scope: path to v2.0

1. ~~D14 landing~~ (Session 29). ~~`neec_entry.py --candidate`~~ (Session 30).
2. **Pilot replication (D2).** The kit is built. When the replicator's
   document is back:
   - `compare_replication.py`, the criterion-level comparison of protocol
     11.4: vectors, flag overlap, scope, joint readings, D13 measure, tier;
   - the replication record (11.5);
   - D18(b) decided;
   - protocol revisions for every ambiguity the pilot finds.
3. **Step 5 → Report v2.0 and Paper v2.0** (unchanged from Handoff 29):
   - eight Part I entries: DE, UBS, SWF, CN, SG, QA, IF, OS;
   - Part II / Section 11 regenerated (three three-way ties);
   - Appendix A.4 from `a4_rerun_23_raw_output.txt`;
   - the contestable-call register with the D13 column;
   - Appendix H from the protocol, and the criteria from `criteria.json`
     (D19);
   - whole percents (D21) and Corrections 1–7.

   The blocks and `neec_corpus.json` are the machine-readable sources: generate,
   don't transcribe. Ostrom's Part I entry should wait for D18(b).
4. **Repository readiness (Claude Code):** as in Handoff 29 (README, LICENSE
   CC BY 4.0, `CITATION.cff`, DOI, GitHub Actions running the harness, issue
   templates, `llms.txt`, schemas at their `$id` URLs, Git tags replacing the
   `_sNN_snapshot` files). Additions from this session:
   - **Layout.** The harness assumes one flat directory (each check copies
     files by name), so a layout with subfolders needs the harness's file map
     to carry paths. Decide the layout before the first commit.
   - **Hub integration.** The Hub's "Economic System Comparison" section is
     the link point. The root domain's `ai-manifest.json`,
     `research-index.json`, `llms.txt` and `sitemap.xml` would each gain a
     NEEC v2 entry (owner's repository).
   - **Timing.** Pilot first, or hold back the Ostrom document.
5. Visual Suite v3.
6. Pages site, Hub link, v1-site pointer, Medium update (owner).

## Corrections for Paper v2.0 (carried, unchanged)
1. A.4's mislabelled ParEcon vs Stakeholder dominance row.
2. H.9 stale (replaced by protocol section 7).
3. Section 10.5's stale percentages and "thirteen systems".
4. H.7 C4.3 0.0 anchor cites Status Quo (published 0.5).
5. H.7 C4.5 1.0 anchor misattributes Degrowth's rationale to ParEcon.
6. H.7 notes' 13-system comparatives (C1.4, C2.5, C4.2).
7. Stale scope notes in anchors (C3.2; H.7v2's "provisional" note).

## Optional polish (not corrections)
- Carried from Handoff 29:
  - evidential superlatives in the documents (not registered, per protocol
    8.1);
  - Qatar's session-relative "now";
  - China's history sentence ("is" could read "was");
  - long lines where an edit landed mid-list;
  - the full report's 36-character name column.
- `summary_block_schema.json` still describes `key` as "the entry's key in
  the canonical SCORES dict". Protocol 9.2 now covers candidates; the schema
  was left unchanged to avoid churn.
- The blind protocol copy's replaced lines are not re-wrapped. They render
  the same in Markdown.
- A harness "derived file" mechanism would let perturbation tests, like the
  four run ad hoc on `verify_doughnut.py`, become reproducible negative
  controls.
- **The Hub's framing (owner's site; a judgment call, not a correction).**
  It describes NEEC as evaluating how CCO and Compassionism "compare to major
  competing systems." When the link moves to v2, wording that leads with the
  23-system corpus and states the self-referential-bias disclosure would
  better support the credibility the protocol is built for.

---

## Notes for the next chat
- Batch shell work. Save each finished file to `/mnt/user-data/outputs/` and
  present files before the end. The shell is `sh`, not bash: no process
  substitution, no `PIPESTATUS`.
- Scripts look for inputs beside themselves, print file names only, and are
  deterministic; keep new scripts to that pattern.
- **Pins to respect:**
  - `verify_comparative_claims.py` pins `audit_claims_s28.py`,
    `d14_landing_s29.py`, `summary_blocks_s28.json`, `restate_s30.py`
    (`c15bed57`) and `verify_doughnut.py` (`2946cf0f`).
  - `build_replication_kit.py` pins `SCORING_PROTOCOL.md` (`13e382bc`),
    `neec_entry.py` (`6ddd3b0a`), `neec_corpus.json` (`ba3c7f70`),
    `build_corpus_file.py`, `criteria.json` and both schemas.
- **Before editing the protocol, `neec_entry.py` or `neec_corpus.json`:** the
  issued kit must stay reproducible. Snapshot each file first
  (`*_s30_snapshot`), map the snapshot into the kit check under its canonical
  name, and keep the baseline check on the same versions.
- Any later restatement starts from the documents as they now are; pin them
  first.
- The chat viewer renders CSV attachments blank; the mount files are fine.
- Appendix G / C14 cross-validation stays on hold until the new Compassionism
  Simulation index ships.

## Immediate next action
1. Update the mount per "Files", then run the harness; expect **56/56**
   (`735c28ed`).
2. Owner:
   - confirm D24;
   - read D22's two paragraphs;
   - run the pilot as described above;
   - decide D23 when convenient.
3. **Default work while the pilot runs:** `compare_replication.py`, tested
   on synthetic replicator blocks. Then Step 5 for the seven entries other
   than Ostrom.

---

## Version history (condensed)
- Sessions 3–13: Step 1c, Step 5 for 15 systems, Integral, A.4 re-runs,
  Report v1.5–1.6, Paper v1.3–1.4, Visual Suite v2.
- Sessions 14–23: Step 1b (eight systems); insertions in Sessions 16 and 20.
- Sessions 24–26: insertion to 23 systems; harness v1–v2; D12.
- Session 27: reproducibility kit in draft; harness v3 (40 checks).
- Session 28: D16–D19 closed; D18(a) applied to the blocks; claim audit of
  the eight documents (222 claims); harness v4 (43).
- Session 29: the D14 landing (eleven documents restated, 23 blocks
  embedded); claims verifier generalised (414 checks, with a negative
  control); D20 confirmed, D21 applied; protocol v2.0-draft.3; harness v5
  (47).
- **Session 30:** `verify_doughnut.py` reconstructed and the Doughnut
  Verification section restated (D22); candidate mode and corpus-file mode in
  `neec_entry.py`; `neec_corpus.json` (D23); the first blind replication kit,
  for Ostrom, with a blind protocol copy (D24); claims verifier 419 checks;
  protocol v2.0-draft.4; harness v6 (56).
