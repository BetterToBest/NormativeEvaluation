# NEEC Project Handoff — Session 32

**Date:** 2026-09-19 to 2026-09-21. **Owner:** Duke Johnson. **Scorer/engineer:** Claude.
**Session result:** the first blind replication is back and closed out. It was
compared criterion by criterion (`compare_replication.py`), recorded and
attributed (`NEEC_OstromCommons_replication_record.md`), and it decided D18(b).
One new decision, D26, is recommended. Harness v7: **61/61 passed**,
byte-identical on a second run. No canonical file, score or document changed.

---

## What this session did

1. **Session-start checks: clean.** All 30 files pinned in Handoff 30's MD5 table
   matched; the v6 harness reproduced 56/56 byte for byte (`735c28ed`); the OS kit
   rebuilt byte for byte (`81a254e8`); the replicator's block validated as a
   candidate inside the rebuilt kit.
2. **The pilot.** Claude Sonnet 5, in an incognito claude.ai chat outside the
   Project, scored Ostrom-Style Commons Governance blind from the kit on
   2026-09-19 (code `OSR`): **13.0/26, 5 failures, Partially Adequate**, 5 flags,
   tier-robust. The original: 14.0/26, 4 failures, Partially Adequate, 20 flags,
   three tiers reachable.
3. **`compare_replication.py`** (protocol 11.4). Validates both blocks as
   candidates against the kit's corpus, proves the original is the canonical
   entry and the kit's corpus the canonical one minus the target, and reports
   vectors, flags, scope, joint readings with D13, and tier, plus kappa and
   alpha labelled descriptive. `--record` checks a replication record's
   generated tables and requires its attribution table to name every difference
   once, from {evidence, interpretation, scope, protocol}; `--fill` writes the
   tables. Runs only in a kit's layout. Self-test 12/12; five mutations of the
   script were each caught by the self-test case meant for it, and five altered
   records were each rejected (ad hoc; not yet in the harness).
4. **The comparison.** 22 of 26 criteria exact, 26 of 26 within one step, same
   tier, failure status agreeing on 23. Kappa 0.719, alpha 0.803. The four
   differences (C1.4, C3.2, C4.1, C4.3) all lie inside the original's register;
   the replication's vector is a combination of the original's register, not the
   reverse.
5. **The replication record** (protocol 11.5). Attributions: C1.4
   **interpretation**; C3.2, C4.1 and C4.3 **protocol** — an anchor that
   contradicts itself, an unstated relation between anchors and conjunctive
   thresholds, and an unstated treatment of replicated implementation failure.
   None to evidence or scope. The record states what the pilot does not show:
   one replicator in the original's model family; a blindness leak (below);
   calibration against the corpus; maintainers' attribution.
6. **The blindness leak, confirmed.** The kit's blind protocol, section 3.1,
   marks the withheld example inside the mechanism list and names its archetype,
   disclosing the class the pilot was meant to test. The class agreement is
   therefore not evidence; nothing else is affected. Fix: R8.
7. **D18(b) decided** (below), with its figures computed by
   `d18b_reexpression_s32.py`.
8. **Harness v7** (`run_all_checks.py`, 61 checks). Five new: the replication's
   candidate validation with its peer matrix; the `compare_replication.py`
   self-test; the pilot comparison with the record check; a negative control
   (refusal beside the canonical script); and the D18(b) script.
9. **Research Hub and v1 site read** (the owner's new context). See
   "Repository and Hub" below.

---

## Files (update the mount with these)

**Add:**

| File | MD5 | Role |
|---|---|---|
| `NEEC_OstromCommons_replication_scoring.md` | `cbe4a3ab` | the replicator's document, as returned |
| `NEEC_OstromCommons_replication_record.md` | `35c798c8` | the replication record (11.5) |
| `compare_replication.py` | `3fedd4d8` | protocol 11.4 comparison and record check |
| `compare_replication_selftest_output.txt` | `560f516f` | 12 of 12 |
| `compare_replication_OS_pilot1_output.txt` | `e5022c67` | the pilot comparison; record current |
| `compare_replication_canonical_refusal_output.txt` | `d41d8cd9` | empty (the refusal goes to stderr, exit 1) |
| `neec_entry_candidate_OSR_output.txt` | `ca4f6212` | the replication validated, with its peer matrix |
| `d18b_reexpression_s32.py` | `8dc8da77` | D18(b) and D26, computed; changes no file |
| `d18b_reexpression_s32_output.txt` | `2ad14bd4` | its output |
| `NEEC_Project_Handoff_32.md` | — | this file |

**Replace:**

| File | MD5 | Note |
|---|---|---|
| `run_all_checks.py` | `2462c306` | v7, 61 checks |
| `run_all_checks_output.txt` | `8e4f3d9f` | 61/61 |

The mount then holds 169 files: the 159 it holds now, plus the ten above.
**Expected:** `python3 run_all_checks.py` →
61 passed, output MD5 `8e4f3d9f`. Copy every extension, `.js` included.

**Still missing from the mount (owner):** `NEEC_Runpod_Replication_Harness.md`,
which Handoff 31 lists as added. Add it if it exists; its essentials (endpoints,
marker protocol, costs) are summarised in Handoff 31.

---

## Decisions

- D2, D3(a), D3(b), D6, D8–D17, D18(a), D19–D22: unchanged.
- **D18(b): decided (Session 32).** Ostrom's register is re-expressed by a stated
  test (revision R1) applied to each flag's own stated alternative reading: a
  reading against another population, domain or frame, or one counting an
  adjacent instrument in or out of the boundary, is a scope question and becomes
  a scenario. **Four flags move** (C1.3, C3.1, C3.5, C4.2); two borderline flags
  stay (C4.3, C5.2). No score changes. Register 20 → 16; D13 still three tiers
  (8.0 points, 10 failures); still the least tier-robust entry; flag count now
  tied with Islamic finance's 16. Sensitivity and all figures: record 10.1 and
  the script's output. **Application next pass** (below).
- **D23: adopted** at the owner's standing instruction: `neec_corpus.json` is
  published in the repository beside the CSV as the corpus's machine-readable
  dataset.
- **D24: confirmed by use** — the pilot ran on the blind copy. Its marking rule is
  amended for future kits by R8.
- **D25: closed as moot.** The pilot ran in an incognito chat, the NEEC-blind
  option Handoff 31 recommended; Runpod was not used (spend ~$0.02 of $15).
- **D26 (new): the C3.2 anchor — recommended; to be applied with D18(b) unless
  the owner decides otherwise.** C3.2's 0.0 band says both "no credible
  mechanism is specified" and "reserve it for an active inflationary mechanism
  ... rather than merely unaddressed". Recommended: the note governs. Consequence:
  Ostrom's C3.2, the corpus's only 0.0 there, becomes **0.5** — 14.5/26,
  3 failures, Partially Adequate — its C3.2 flag lapses (register 15), it stays
  the least tier-robust, and its knowledge-commons scenario would reach
  Potentially Adequate. **This changes a canonical score.**

### Protocol revisions queued for v2.0-draft.5 (record 10.3)

R1 scope-or-doubt test (3.4) · R2 replicated implementation failure (2.1, 4.1) ·
R3 C3.2 anchor per D26 with Correction 7 · R4 conjunctive thresholds — **audit
the corpus's 1.0s on multi-clause thresholds first** · R5 archetypes defined by
table (5.1) · R6 extension boundaries (3.2) · R7 pilot result (11.6) · R8 blind
copy marking (11.2; builder, future kits only).

---

## Owner review

1. The four attributions (record section 4).
2. D18(b)'s classification — above all the two borderline flags, C4.3 and C5.2.
3. **D26** — a canonical score change.
4. Add `NEEC_Runpod_Replication_Harness.md` to the mount, if it exists.

---

## Repository and Hub (read this session)

- **The Hub's link point** is its "Economic System Comparison" section, which
  links to the v1 Google Site and the Medium article, and describes NEEC as
  evaluating "how CCO and the broader Compassionism framework compare to major
  competing systems".
- **The live v1 Paper** is the January 11, 2026 release: 12 systems, 25
  criteria, CCO-PTF-CIP-SZH at 23.5/25. v2 supersedes it (23 systems, 26
  criteria, protocol, replication), so the v1 site needs a pointer to v2.
- **Timing.** The Ostrom pilot is back, so Handoff 30's hold on publishing the
  Ostrom document is lifted.
- **The next pilot and blindness.** Recommended target: **CCO-PTF-CIP-SZH**, the
  entry the self-referential concern bears on, with a replicator outside the
  Claude family. Its v1 scoring is already public on the v1 site and the Hub, so
  blindness cannot rest on non-publication: the kit's brief must forbid NEEC
  sources, the replicator should run without browsing NEEC's domains, and the
  record must disclose this. Design this in the kit before running it.
- **Hub framing (owner's call, optional).** When the link moves to v2, text
  that leads with the 23-system corpus, the published protocol and the blind
  replication, and states that CCO's designer co-authors the framework, would
  support the credibility the protocol exists for.
- **Repository layout (decide before the first commit).** Recommended: keep
  every harness input flat at the repository root for v2.0 — all 61 checks copy
  files by name — and add a separate folder for the Pages presentation layer.
  Reorganise into subfolders only after CI guards the byte-identical outputs.
- **Claude Code.** With Claude Pro, repository assembly fits Claude Code in the
  existing empty repository `BetterToBest/NormativeEvaluation`: README, LICENSE
  (CC BY 4.0), `CITATION.cff`, DOI, a GitHub Actions job running the harness,
  issue templates, `llms.txt`, schemas at their `$id` URLs, then Git tags in
  place of the `_sNN_snapshot` files. The root domain's `ai-manifest.json`,
  `research-index.json`, `llms.txt` and `sitemap.xml` each gain a NEEC v2 entry.

---

## Remaining scope: path to v2.0

1. ~~D14 landing~~ (29). ~~`--candidate`~~ (30). ~~Pilot, comparison, record,
   D18(b) decided~~ (32).
2. **The D18(b)/D26/protocol pass** (next): pin the Ostrom document, the protocol
   and the claims verifier as `_s32_snapshot`; restate the Ostrom document in
   place by generator (D18(b): flagged calls, readings, scenarios, block; D26:
   C3.2 and every claim it moves); insert the changed vector through the 10.2
   machinery and regenerate the CSV and `neec_corpus.json`; update the claims
   verifier (e.g. "twenty of twenty-six", "the largest flagged set",
   "tier-neutral", "the only 0.0 on C3.2"); protocol v2.0-draft.5 (R1–R3,
   R5–R7; R4 after its audit); R8 in `build_replication_kit.py`, keeping the OS
   kit reproducible from the pinned Session 30 protocol; harness v8.
3. **Step 5 → Report v2.0 and Paper v2.0**: the eight Part I entries (Ostrom's
   after item 2), Part II / Section 11, Appendix A.4 from
   `a4_rerun_23_raw_output.txt`, the contestable-call register with the D13
   column, Appendix H from the protocol, criteria from `criteria.json` (D19),
   whole percents (D21), Corrections 1–7. Generate, don't transcribe.
4. **Repository readiness**, as above.
5. Visual Suite v3.
6. Pages site, Hub link, v1-site pointer, Medium update (owner).

## Corrections for Paper v2.0 (carried, unchanged)
1. A.4's mislabelled ParEcon vs Stakeholder dominance row.
2. H.9 stale (replaced by protocol section 7).
3. Section 10.5's stale percentages and "thirteen systems".
4. H.7 C4.3 0.0 anchor cites Status Quo (published 0.5).
5. H.7 C4.5 1.0 anchor misattributes Degrowth's rationale to ParEcon.
6. H.7 notes' 13-system comparatives (C1.4, C2.5, C4.2).
7. Stale scope notes in anchors (C3.2 — now also R3/D26; H.7v2's "provisional" note).

## Optional polish (not corrections, carried)
Evidential superlatives (not registered, per 8.1); Qatar's session-relative
"now"; China's "is"/"was"; long lines where an edit landed mid-list; the
report's 36-character name column; `summary_block_schema.json`'s `key`
description; unwrapped lines in the blind copy; a harness "derived file"
mechanism, which would let this session's record mutations become checks.

---

## Notes for the next chat
- Batch shell work; the shell is `sh`. Save finished files to
  `/mnt/user-data/outputs/` and present them. Copy every extension when
  mirroring the mount.
- Scripts find inputs beside themselves, print file names only, and are
  deterministic.
- `compare_replication.py` refuses to run beside the canonical script; run it in
  a kit's layout (the harness's `KIT_LAYOUT` map shows how).
- **Pins** (unchanged): `verify_comparative_claims.py` pins
  `audit_claims_s28.py`, `d14_landing_s29.py`, `summary_blocks_s28.json`,
  `restate_s30.py` (`c15bed57`) and `verify_doughnut.py` (`2946cf0f`);
  `build_replication_kit.py` pins `SCORING_PROTOCOL.md` (`13e382bc`),
  `neec_entry.py` (`6ddd3b0a`), `neec_corpus.json` (`ba3c7f70`),
  `build_corpus_file.py`, `criteria.json` and both schemas.
- Before editing the protocol, `neec_entry.py`, `neec_corpus.json` or the Ostrom
  document: snapshot first, map snapshots into every check that pins them, and
  keep the issued OS kit reproducible.
- `d18b_reexpression_s32.py` reads the canonical Ostrom document; after the
  application pass it must run against the `_s32_snapshot`.
- Appendix G / C14 cross-validation stays on hold until the new Compassionism
  Simulation index ships.

## Immediate next action
1. Owner: review items 1–3 above; add the missing Runpod document.
2. The D18(b)/D26/protocol pass (Remaining scope, item 2).
3. Then Step 5 for the seven entries other than Ostrom.

---

## Version history (condensed)
- Sessions 3–13: Step 1c, Step 5 for 15 systems, Integral, A.4 re-runs,
  Report v1.5–1.6, Paper v1.3–1.4, Visual Suite v2.
- Sessions 14–23: Step 1b (eight systems); insertions in Sessions 16 and 20.
- Sessions 24–26: insertion to 23 systems; harness v1–v2; D12.
- Session 27: reproducibility kit in draft; harness v3 (40).
- Session 28: D16–D19; claim audit (222 claims); harness v4 (43).
- Session 29: the D14 landing; claims verifier (414); protocol draft.3; harness v5 (47).
- Session 30: D22; candidate mode; `neec_corpus.json` (D23); the OS kit (D24);
  protocol draft.4; harness v6 (56).
- Session 31: Runpod validated; D25 raised; no file changes.
- **Session 32:** the pilot returned; `compare_replication.py`; the replication
  record; D18(b) decided; D26 raised; D23 adopted; D25 closed; harness v7 (61).
