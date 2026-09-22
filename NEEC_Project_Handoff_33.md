# NEEC Project Handoff 33

**Session 33 · 2026-09-21 · Owner: Duke Johnson · Scorer and engineer: Claude**
**Predecessors kept in the Project:** Handoff 30 (fingerprint table, pins) and Handoff 32 (the first blind replication and decisions D18(b), D26).

Session 33 applied the two decisions the first blind replication produced, after the owner confirmed both: **D26** (C3.2's 0.0 band is reserved for an active inflationary mechanism) and **D18(b)** (Ostrom-style commons governance's register re-expressed by the scope-or-doubt test). Everything was generated from pinned Session 32 snapshots and verified programmatically; the harness is now at version 8, **71 of 71 checks passing**, byte-identical on a second run and on a clean 193-file mirror of the Project.

---

## 1. Session-start checks

- **Fingerprints.** 35 of the 36 files pinned in Handoffs 30 and 32 matched exactly. The 36th, `compare_replication_canonical_refusal_output.txt`, is absent from the Project: it is *expected to be empty* (the refusal goes to stderr), and a claude.ai Project cannot hold an empty file. Harness v7 crashed on its absence (FileNotFoundError, no summary). **Fixed in v8** (section 5).
- **Project contents.** 168 files: Session 32's 159, minus Handoff 31, plus the nine Session 32 additions, plus `NEEC_Runpod_Replication_Harness.md` (Handoff 32's owner item 4, now closed).
- **Research Hub.** The "Economic System Comparison" section still links only the v1 Google Site and the Medium article. No v2 pointer yet (owner item, unchanged).

## 2. Decisions applied (all confirmed by the owner this session)

| ID | Decision | Effect |
|---|---|---|
| D26 | C3.2's 0.0 band is reserved for an active inflationary mechanism with no counterbalancing element; absence scores 0.5 | Ostrom's C3.2 0.0 → 0.5: **14.0 → 14.5/26 (56%), failures 4 → 3, tier unchanged (Partially Adequate)**. No entry now scores 0.0 on C3.2. |
| D18(b) | Ostrom's register re-expressed by the stated scope-or-doubt test (replication record 10.1) | C1.3, C3.1, C3.5, C4.2 become scope scenarios; C4.3 and C5.2 (borderline) stay; with C3.2 retired by D26 the register is **15 flags** (7 up, 8 down). No score changes from D18(b) itself. |
| — | Item 1C-22 (Step 1c retrofit document) kept as written | Its UBI / Mutual Credit pair tie still holds; the verifier checks it on a re-specified fact list (`RESPEC` in `restate_s33.py`). |
| — | Singapore's share passage restated | Ostrom's 65.6% now exceeds Singapore's 64.1%, so the share ordering changes in both directions. |
| — | UBI's CSV note restated | Names the three-way tie at 14.5/26. |
| — | Two Session 25 register entries reversed by D26 | Qatar's "joint upward 14.0 is SWF Statism's and Singapore's" (the Session 21 wording) is true again, and Islamic finance's "the largest set of any entry" (16 flags against Ostrom's 15) is true again. The verifier's group [G] now treats the D12 wording as the superseded one. |

## 3. Corpus consequences (all computed, all asserted)

| Quantity | Session 32 | Session 33 |
|---|---|---|
| Ostrom total / failures / tier | 14.0 / 4 / Partially Adequate | **14.5 / 3 / Partially Adequate** |
| Ostrom's ties | SWF Statism, Singapore (14.0; one tier) | **Mutual Credit / LETS, UBI (14.5; 3, 3, 7 failures; two tiers)** |
| Ostrom's competition rank | 10= | **8=** |
| SWF Statism and Singapore | tied 10th–12th with Ostrom | tied 11th–12th with each other |
| Strict-dominance pairs | 14 | 14 (none gained or lost) |
| Pareto frontier | 12 systems | 12 (unchanged) |
| Tier counts | 6 / 8 / 9 | 6 / 8 / 9 (every entry's tier unchanged) |
| Ostrom's flags | 20 (11 up, 9 down) | **15 (7 up, 8 down)** |
| Enumeration | 1,048,576 combinations; 46.7% keep the tier | **32,768; 9.0% / 65.6% / 25.4% across Potentially / Partially / Structurally** |
| Joint readings | A 19.5/0 · B (as scored) 14.0/4 · C 9.5/11 | **up 18.0/0 · scored 14.5/3 · down 10.5/9** (D16's extremes) |
| D13 span | 10.0 points / 11 failures | **7.5 / 9** — still the corpus's least tier-robust entry |
| Knowledge-commons scenario | 15.0/26, 3 failures, tier-neutral | **15.5/26, 2 failures, Potentially Adequate** (now crosses a tier) |
| New scope scenarios | — | land trusts out 14.0/26, 4 failures; resource frame 16.0/26, 3 failures |
| Ostrom vs Status Quo / Georgism | +3.5 / +0.5 (3 higher, 2 lower) | +4.0 / +1.0 (3 higher, 1 lower); nearest neighbours now at 4 criteria |

## 4. What was built

- **`insert_session33.py`** — writes both canonical scripts from their Session 32 snapshots: one SCORES cell, one PUBLISHED row, a D26 comment, the Session 33 tie note and two new tie pairs; in the CSV builder, Ostrom's row and UBI's notes are re-rendered from parsed values so every other byte is unchanged.
- **`restate_s33.py`** — restates **seven** documents in place from their `_s32_snapshot.md` copies, using the D14 generator's own edit function and `d18b_reexpression_s32.reexpress()`: 28 edits, 38 restated phrases, 6 phrases in three rewritten Ostrom sections ("The flagged calls…", "The joint readings", "The scope scenarios"), 25 superseded phrases removed; regenerates Ostrom's summary table (renderer first checked to reproduce the Session 32 table byte for byte), the IF and OS corpus tables, and Ostrom's summary block; asserts 13 computed facts before writing anything. Exposes `EDITS`, `SUPERSEDED`, `SECTION_CLAIMS`, `NOWSPEC`, `RESPEC`, `os_block()`, `render_summary_table()` for the verifier. It needs `neec_scores.csv` beside it (read by `neec_entry.py`'s corpus loader; its output does not depend on it).
- **`verify_insertion_s33.py`** — 23 checks in five groups, including three negative tests: exactly one cell changed; CSV, corpus file and corpus consistent; dominance, frontier, tiers and ranks before and after.
- **`verify_comparative_claims.py`, Session 33** — 503 checks, all pass; negative control on the seven Session 32 documents: 391 pass, 112 fail, exit 1. New group **[L]** asserts the restatement. Group [A] tolerates the one D26 cell where the historical, unedited `verify_ostrom.py` differs. The Session 30 version is kept as `verify_comparative_claims_s32_snapshot.py`.
- **`run_all_checks.py` v8** — 71 checks: ten new Session 33 checks first, then all 61 v7 checks re-pinned to the Session 32 snapshots (34 of them marked "[Session 32 state]"). Three fixes for a claude.ai Project: `EMPTY` for expected-empty streams, stderr comparison for the refusal check (exit 1 with empty stdout cannot distinguish a refusal from a crash), and a missing reference file fails its own check instead of aborting the run.

## 5. Files (Session 33)

Replace the 14 changed files in the Project and add the 26 new ones (25 below plus this handoff). Keep Handoffs 30 and 32. After this the Project holds **194 files**. Nothing needs deleting; in particular, do not try to add an empty `compare_replication_canonical_refusal_output.txt` — v8 no longer needs it.

**Changed (14)**

| File | MD5 (first 8) |
|---|---|
| `NEEC_IslamicFinance_scoring_scratch.md` | `9db387f9` |
| `NEEC_MutualCredit_LETS_scoring_scratch.md` | `295f0ece` |
| `NEEC_Ostrom_Commons_scoring_scratch.md` | `54016bc7` |
| `NEEC_SovereignWealthFundStatism_scoring_scratch.md` | `09f46c6f` |
| `NEEC_StateCapitalism_Qatar_scoring_scratch.md` | `a6afb45e` |
| `NEEC_StateCapitalism_Singapore_scoring_scratch.md` | `921f624c` |
| `NEEC_UniversalBasicServices_scoring_scratch.md` | `9a3d5c11` |
| `neec_corpus.json` | `ae19a9bc` |
| `neec_scores.csv` | `081f6915` |
| `neec_scores_csv_builder_v2.py` | `a03e6a83` |
| `neec_weighting_robustness_analysis_v2.py` | `e82ba335` |
| `run_all_checks.py` | `6cd73743` |
| `run_all_checks_output.txt` | `884e6f64` |
| `verify_comparative_claims.py` | `0d8afbc0` |

**New (25, plus this handoff)**

| File | MD5 | File | MD5 |
|---|---|---|---|
| `NEEC_IslamicFinance_scoring_scratch_s32_snapshot.md` | `9643d46d` | `insert_session33.py` | `eb6b4260` |
| `NEEC_MutualCredit_LETS_scoring_scratch_s32_snapshot.md` | `477390c5` | `restate_s33.py` | `3a5b0290` |
| `NEEC_Ostrom_Commons_scoring_scratch_s32_snapshot.md` | `f280ec44` | `verify_insertion_s33.py` | `2456d8a6` |
| `NEEC_SovereignWealthFundStatism_scoring_scratch_s32_snapshot.md` | `70287ebd` | `insert_session33_output.txt` | `49b77db5` |
| `NEEC_StateCapitalism_Qatar_scoring_scratch_s32_snapshot.md` | `931c2695` | `restate_s33_output.txt` | `e5e7c868` |
| `NEEC_StateCapitalism_Singapore_scoring_scratch_s32_snapshot.md` | `d6ad5591` | `verify_insertion_s33_output.txt` | `f9fb66f9` |
| `NEEC_UniversalBasicServices_scoring_scratch_s32_snapshot.md` | `895705a2` | `session33_v2script_output.txt` | `15683acb` |
| `neec_weighting_robustness_analysis_v2_s32_snapshot.py` | `d5041b13` | `session33_csv_builder_output.txt` | `d6d816ff` |
| `neec_scores_csv_builder_v2_s32_snapshot.py` | `7cd53027` | `verify_claims_s33_output.txt` | `6c598ad9` |
| `neec_scores_s32_snapshot.csv` | `ca2eb1f4` | `verify_claims_s33_negative_output.txt` | `381e13a2` |
| `neec_corpus_s32_snapshot.json` | `ba3c7f70` | `build_corpus_file_s33_output.txt` | `3e43fc3b` |
| `verify_comparative_claims_s32_snapshot.py` | `257c7a19` | `neec_entry_documents_s33_output.txt` | `60a24f8c` |
| `compare_replication_canonical_refusal_stderr.txt` | `fb8a38bc` | | |

## 6. Pins (respect these; a changed pinned file makes its dependant refuse to run)

- `insert_session33.py` pins the two Session 32 script snapshots (`d5041b13`, `7cd53027`).
- `restate_s33.py` pins the seven `_s32_snapshot.md` files, `d14_landing_s29.py` (`6ed2d55c`), `d18b_reexpression_s32.py` (`8dc8da77`), `neec_entry.py` (`6ddd3b0a`) and the **Session 33** canonical script (`e82ba335`).
- `verify_insertion_s33.py` pins the three Session 32 corpus snapshots (script, CSV, corpus file).
- `verify_comparative_claims.py` (Session 33) pins, as before, `audit_claims_s28.py` (`11150ac2`), `d14_landing_s29.py`, `summary_blocks_s28.json` (`7973e170`), `restate_s30.py` (`c15bed57`), `verify_doughnut.py` (`2946cf0f`), and now `restate_s33.py` (`3a5b0290`) and `d18b_reexpression_s32.py` (`8dc8da77`).
- `build_replication_kit.py` still pins `neec_corpus.json` at `ba3c7f70` — **the Session 32 value, now `neec_corpus_s32_snapshot.json`**. The issued Ostrom kit must stay reproducible, and harness v8 runs the kit check against the snapshot. A future kit (the second pilot) needs the pin moved deliberately, together with revision R8 (section 8, item 4).

## 7. Known limitations (stated, not hidden)

1. **Appendix A.4's script is Session 25-specific.** `run_a4_full_rerun_23.py` hard-codes the Session 25 tie structure (the 14.0 three-way tie with Ostrom, eight scheme-specific ties) and raises a KeyError on the Session 33 corpus. Harness v8 runs it against the Session 32 corpus, where it still reproduces its capture. **Appendix A.4 for Paper v2.0 needs a Session 33 successor** before Step 5 generates it (section 8, item 2).
2. `verify_ostrom.py` (the Session 23 entry verifier) is historical and unedited; it still states C3.2 = 0.0 and the twenty-flag register. The claims verifier's group [A] checks it against the canonical vector *but for C3.2*, and its register against its own vector.
3. The claims verifier's group [I] evaluates register facts with `audit_claims_s28.py`'s own inputs, including the Session 28 staging of Ostrom's block (the Session 23 register). The current flag-count and D13 claims are asserted from the documents' own blocks in group [F], which is authoritative; no register item currently depends on the difference.
4. Optional polish, not corrections: UBI's CSV note still says "Report Part I (System 7) still shows legacy scores as of this session" (session-relative wording); the CSV builder's printed history has no Session 33 line (its header comment records D26).

## 8. Next steps, in priority order

1. **Owner:** add the files in section 5 to the Project.
2. **`run_a4_full_rerun_33.py`** — Appendix A.4 on the Session 33 corpus, with its assertions re-derived (Ostrom now ties Mutual Credit / LETS and UBI at 14.5; recompute every scheme-specific tie and tie-break), captured and added to the harness beside the pinned Session 32 run.
3. **Protocol v2.0-draft.5** — revisions R1–R8 from the replication record (10.3). R3 is now decided by D26 and can be written into C3.2's anchor; R4 still needs its audit of corpus 1.0s on multi-clause thresholds first; R8 lands in `build_replication_kit.py` for future kits only.
4. **Step 5 → Report v2.0 and Paper v2.0** — the eight Part I entries (DE, UBS, SWF, CN, SG, QA, IF, OS), Part II / Section 11, Appendix A.4 (after item 2), the contestable-call register with a D13 column, Appendix H from the protocol, criteria from `criteria.json` (D19), whole percents (D21), Corrections 1–7 (Correction 7 is now partly resolved by D26 / R3).
5. **Repository readiness** at `github.com/BetterToBest/NormativeEvaluation`: flat layout for v2.0, README, LICENSE (CC BY 4.0), `CITATION.cff`, DOI, GitHub Actions running the harness, `llms.txt`, schemas at their `$id` URLs, Git tags replacing the `_sNN_snapshot` files. The Research Hub (`bettertobest.github.io/research-hub/`) will link to the v2 site.
6. **Second pilot:** CCO-PTF-CIP-SZH, a replicator outside the Claude family, a kit built with R8. Blindness cannot rest on non-publication, since the v1 scoring is public.
7. Visual Suite v3; the Pages site, the Hub link, a pointer on the v1 site, and a Medium update (owner).
8. Appendix G / C14 cross-validation stays on hold until the new Compassionism Simulation index ships.

## 9. Standing working notes

Shell is `sh` (no `time`, no process substitution). Maximum effort; accuracy over speed. Scratch before insert; programmatic verification over visual checking; generate, don't transcribe. Scripts find inputs beside themselves, print file names only, and are deterministic. `compare_replication.py` refuses to run beside the canonical script. The owner's preferences: flag substantive content changes as decisions rather than applying them silently; distinguish corrections from optional polish; say plainly when a file does not exist rather than offering speculative snippets; prefer precise, defensible language.
