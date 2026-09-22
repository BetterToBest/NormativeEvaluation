# NEEC Project Handoff 36

**Session 36 · 2026-09-22 · Owner: Duke Johnson · Scorer and engineer: Claude**
**Predecessor:** Handoff 35 (in the Project and the repository). This handoff supersedes its sections 6–12.

Session 36 verified the Session 35 repository and did Handoff 35's item 3: **scoring protocol
v2.0-draft.5**, with the first blind replication's eight revisions (R1–R8) written in and three decisions
taken under the delegation (**D29, D30, D31**). `criteria.json` is corrected to match, the replication-kit
builder carries R8 for later kits, and a new verifier asserts the protocol's own statements about the corpus.
**No score changed**, and no corpus file or scoring document changed. The harness is at version 11, **79 of
79 checks passing**, byte-identical on a second run and in a fresh clone.

---

## 1. Session-start checks

- **Repository.** `main` at `4be59a5` (the merge of pull request #2; pull request #1 merged at `ecdd095`,
  both true merge commits): 213 tracked files, all mode 100644; digest `20adca567f530ac005259f5a1d9ec94a`
  (exact match); harness v10 in a fresh clone ran 75 of 75, byte-identical to its capture; the Actions run on
  `main` (run 7) passed. Handoff 35 in the repository is byte-identical with the Project's copy.
- **Open item found: the tags.** `git ls-remote --tags` shows **no tags**: neither `s34` nor `s35` was
  created. Section 6 creates them with `s36`.
- **Attachments.** The seven CSV files attached to the opening message arrived with empty content, as in
  Session 34; the repository copies were used.

## 2. What changed (all decisions are Claude's under the delegation; the owner may reverse any)

### 2.1 Protocol v2.0-draft.5 (`SCORING_PROTOCOL.md`; draft.4 pinned as `SCORING_PROTOCOL_s35_snapshot.md`)

| Revision | Where | What |
|---|---|---|
| R1 (D18(b)) | 3.4 | the scope-or-doubt test, and 3.4(b) restated as decided and applied |
| R2 (**D29**) | 2.1, 3.2, 4.1 | implementation failure and the system's own logic; remedies from outside the scope |
| R3 (D26) | 2.1, 4.6, `criteria.json` | C3.2's 0.0 band reserved for an active inflationary mechanism; absence written into the 0.5 band; Correction 7's stale count removed |
| R4 (D28) | 2.3, 3.2, 4.6, Appendix B | clause by clause; reach; anchors describe, thresholds govern; **Appendix B** (new) lists each multi-clause threshold's clauses, generated from `r4_audit_s35.py` |
| R5 (**D30**) | 5.1 | the archetype table: five archetypes, every entry assigned, peers declared by rule |
| R6 (**D31**) | 3.2 | the extension test for a mechanism's boundary |
| R7 | 11.6–11.7 | the first pilot's result; the second pilot |
| R8 | 11.2, `build_replication_kit.py` | no marker where a marker would disclose; the builder refuses one in 3.1 or 5.1 |

Also restated because Session 33 left them stale: 3.5 (the worked example) and 6.4 (the full-disclosure
example still gave Ostrom's pre-D18(b) figures, 10.0 points / 11 failures / 46.7% of 1,048,576). Section 13
records the delegation, settles draft.4's two open confirmations (D23 by D27(a); D24 under the delegation),
and adds D25–D31 with reasons and consequences.

### 2.2 The three decisions

- **D29 — implementation failure and remedies from outside (R2).** A failure replicated across independent
  implementations is evidence about the system's own logic, unless the system's own sources show the failing
  implementations lacked a required feature; a credible pathway must be one the system itself provides; a
  remedy from outside the declared scope is not credited (a scope scenario counts it in); whether an inside
  remedy works is evidence. **Unlike D28, D29 can turn a 0.5 into a 0.0.** Known case: Ostrom's C4.3 (0.5 as
  scored, or 0.0: 14.0/26, 4 failures, Partially Adequate). The rescoring pass reads all **131** 0.5s of the
  eight mechanism-class entries against it and reports every failure count it changes. Its reach elsewhere is
  not audited (limitation 2).
- **D30 — archetypes (R5).** The four archetypes named in Step 1b are kept; one is added, **comprehensive
  design with committed mechanisms** (MS, LM, DG, SC, FALC, PE, CCO, INT), because eight comprehensive entries
  fit none of the four. MMT + JG and UBI join the narrow single mechanisms. Close calls stated in 5.1 (MMT + JG;
  Degrowth and FALC against Doughnut Economics; Stakeholder Capitalism). No score changes. Peers: same
  archetype, widened to the scope class when the archetype has fewer than three other members.
- **D31 — extensions (R6).** An extension belongs to a mechanism when the mechanism's own literature pairs it
  with the mechanism or applies its defining design to it one by one, and does not dispute the transfer; the
  deciding source is cited, and the scorer's own mapping is not that source. It codifies the four precedents
  (Georgism's dividend in; zakat out; knowledge commons out; land trusts in). **One source is to be confirmed
  in the rescoring pass:** both Ostrom scorings count community land trusts in on their own mapping. If no
  source is found, C1.3 → 0.0 (14.0/26, 4 failures); with C4.3 also 0.0, 13.5/26, 5 failures — Ostrom stays
  Partially Adequate either way.

### 2.3 `criteria.json` corrected (through `build_criteria.py`; the old file and script pinned as `*_s35_snapshot`)

**A decision beyond the handoff's wording, flagged:** Handoff 35 asked for four anchor thresholds to be
corrected. D28(g) says the anchors carry *the definitions' text*, so **every** anchor threshold now equals its
definition's Pass Threshold: 25 of 26 lines replaced (6 in substance, 19 in wording, 3 of those only in the case
of the first letter). The substantive six are the audit's four (C2.5, C3.1, C5.1, C5.3), C2.1 (noted by the
audit outside its four), and **C2.2, found this session: the anchor dropped the population clause "for all
residents"** (a correction, not polish). C1.5's H.7v2 threshold line carried a sentence of band reasoning; it
moves unchanged into the anchor's empty note. C3.2's bands carry D26 (R3). Every change is recorded in the
file (`source.corrections`) and printed by the script; the file still validates against the unchanged
`criteria_schema.json`, and nothing else in it changed (checked).

### 2.4 Other files

- **`build_replication_kit.py`**: per-target pins; R8 for targets with `r8=True` (drops, a guard on 3.1 and
  5.1, note and brief wording); `--selftest-r8`, which tests R8 on draft.5 without building a kit and shows that
  the first kit's 3.1 marker is one R8 refuses. The OS kit still rebuilds **byte for byte** (zip `81a254e8`).
- **`verify_protocol_s36.py`** (new): 58 checks on the protocol's own statements — the D17 class lines, the
  archetype table against the corpus, every figure about an entry (3.4, 3.5, 6.1, 6.4, 6.5, section 13's notes),
  4.6 against `criteria.json`, Appendix B against the audit's clause table, the register, R1–R8 placement, and
  eight superseded draft.4 statements. Its negative control rejects draft.4 (44 of 58 fail). It would have
  caught the staleness Session 33 left in 3.5 and 6.4.
- **`NEEC_CONTRIBUTING.md`** — **two corrections** (stale statements): step 7 said candidate mode did not
  exist (it has since Session 30), and the first pilot was described as future. Also aligned with draft.5
  (clause by clause, archetype peers, extensions).
- **`README.md`** (via `build_readme.py`): protocol version; 79 checks; the provisional-totals paragraph now
  says that D29 and D31 can add a structural failure, and that the two known cases cannot change Ostrom's tier.
  **`llms.txt`**: the same.
- **`run_all_checks.py` v11**: checks [76]–[79] appended; every earlier check that reads the protocol,
  `criteria.json` or `build_criteria.py` reads the Session 35 snapshots ([24], [30], [44], [75]). Output
  differs from v10 only in the count lines, [24]'s reference name, [74]'s README MD5, [75]'s name suffix and
  the four new entries (checked by `diff`).

## 3. Files

The repository update is **19 files** at the zip's top level, `NEEC_repository_s36.zip`:

| File | MD5 (first 8) | Status |
|---|---|---|
| `SCORING_PROTOCOL.md` | `bbee2c45` | replaced (draft.5) |
| `criteria.json` | `d4b78634` | replaced |
| `build_criteria.py` | `945843b2` | replaced |
| `build_replication_kit.py` | `f900d652` | replaced |
| `build_readme.py` | `4a2cc58f` | replaced |
| `README.md` | `62c43e1c` | replaced |
| `llms.txt` | `0e3af6cc` | replaced |
| `NEEC_CONTRIBUTING.md` | `b12831cd` | replaced |
| `run_all_checks.py` | `bdf07909` | replaced (v11) |
| `run_all_checks_output.txt` | `74358119` | replaced |
| `SCORING_PROTOCOL_s35_snapshot.md` | `13e382bc` | new (draft.4, pinned) |
| `criteria_s35_snapshot.json` | `6542331e` | new (pinned) |
| `build_criteria_s35_snapshot.py` | `2a601c00` | new (pinned) |
| `build_criteria_s36_output.txt` | `e2621e30` | new |
| `build_replication_kit_r8_selftest_output.txt` | `2ec2c6c3` | new |
| `verify_protocol_s36.py` | `71e14421` | new |
| `verify_protocol_s36_output.txt` | `1664f812` | new |
| `verify_protocol_s36_negative_output.txt` | `5df11a76` | new |
| `NEEC_Project_Handoff_36.md` | (this file) | new |

**The Project** gets this handoff only (GitHub is canonical, D27(b)); its copies of replaced files are stale by
design.

## 4. Pins (respect these)

- `build_replication_kit.py`: the OS target pins the Session 30 protocol (`13e382bc`), `criteria.json`
  (`6542331e`) and the Session 32 corpus (`ba3c7f70`); the harness supplies them from the snapshots. A new
  target carries its own pins, set when it is defined.
- `verify_protocol_s36.py` pins nothing: it asserts the protocol against the corpus in force. **When the
  rescoring pass changes the corpus, its corpus-dependent checks will fail until the protocol is restated** —
  by design; restate the protocol in place and give the verifier a successor, as the claims verifier does.
- Unchanged: Handoff 33 section 6's pins; `r4_audit_s35.py` now reads `criteria_s35_snapshot.json`.

## 5. Decision register

Section 13 of the protocol is the register (D2–D31). Nothing awaits the owner.

## 6. Updating the repository (owner)

1. **Upload the zip**: on the repository page, **Add file → Upload files**, drop in
   `NEEC_repository_s36.zip`, **Commit changes** (to `main`).
2. **Paste to Claude Code:**

```
Session 36 update. NEEC_repository_s36.zip is now on main. Please:
1. Pull main and create a new branch from it.
2. Unzip NEEC_repository_s36.zip into the repository root, overwriting (19 files: 9 new, 10 replaced), then delete the zip and stage everything (git add -A).
3. Confirm git ls-files shows 222 files.
4. Run: python3 run_all_checks.py > /tmp/out.txt ; cmp /tmp/out.txt run_all_checks_output.txt
   Expect "SUMMARY: 79 passed, 0 failed, 0 skipped (of 79)." and cmp reporting no difference.
5. Run the fingerprint snippet in section 8 of NEEC_Project_Handoff_36.md; expect 2f431ae6d8e118d80ba0476a16aa3002.
6. Commit "NEEC Session 36: scoring protocol v2.0-draft.5 (R1-R8, D29-D31), criteria.json corrected, harness v11", push, open a pull request into main, and merge it with a merge commit if you are able to (otherwise tell me).
7. The Session 34 and 35 tags were never created. Create s34 at commit ecdd095 (the merge of pull request #1), s35 at commit 4be59a5 (the merge of pull request #2), and s36 at the new merge commit. Push them (git push origin s34 s35 s36), then run git ls-remote --tags origin and show me the result. If pushing tags is refused, say so plainly.
8. Confirm the harness workflow passed on main.
```

3. **If Claude Code cannot push tags**, create each on GitHub instead: **Releases → Draft a new release →
   Choose a tag**, type `s34`, click **Create new tag: s34 on publish**, then **Target → Recent commits** and
   pick `ecdd095` ("Merge pull request #1…"); title it `s34`, **Publish release**. Repeat for `s35` (`4be59a5`,
   "…(#2)") and `s36` (the Session 36 merge commit). Each also creates a release entry, which is harmless.
4. **Add this handoff to the Project.**

## 7. Next session: start here

1. **Clone:** `git clone https://github.com/BetterToBest/NormativeEvaluation /home/claude/neec`.
2. **Verify:** tags `s34`, `s35` and `s36` exist (`git ls-remote --tags origin`); 222 tracked files; the digest
   below over every tracked file except this handoff equals `2f431ae6d8e118d80ba0476a16aa3002`; harness v11 runs
   79 of 79, byte-identical to `run_all_checks_output.txt`; the latest Actions run on `main` passed. If the
   Session 36 update has not been applied, ask the owner to finish section 6 first (the zip is in the Session 36
   conversation).

```
import hashlib, subprocess
h = hashlib.md5()
for f in sorted(x for x in subprocess.check_output(["git", "ls-files"]).decode().split("\n") if x):
    if f != "NEEC_Project_Handoff_36.md":
        h.update(f.encode() + b"\0" + hashlib.md5(open(f, "rb").read()).digest())
print(h.hexdigest())
```

3. **Then** section 8, item 3.

## 8. Next steps, in priority order

1. **Owner:** section 6.
2. **Next session:** verify (section 7).
3. **The rescoring pass (D28, D29, D31)** — before Step 5 and the second pilot, and more than one session.
   Scratch document first (`NEEC_Rescoring_s37.md` or similar), clause-level estimates on cited evidence,
   changes by generator with pinned inputs, documents restated in place (D12, D14). Suggested order:
   (a) the 33 stated-shortfall 1.0s (audit record, section 7); (b) the other 101 1.0s, criterion by criterion,
   and C5.1's second clause for its thirteen 1.0s; (c) the 131 mechanism-class 0.5s against D29, Ostrom's
   C4.3 first; (d) the D31 source for Ostrom's land trusts; (e) the Islamic finance and Ostrom documents'
   quoted thresholds restated to the definitions (audit record, section 4). Then regenerate the corpus, CSV,
   README and Appendix A.4, restate the protocol's corpus statements (section 4 above), and give the claims and
   protocol verifiers successors. Hold every design's modelled figures to protocol 4.1's evidentiary tier
   (the CCO disclosure in the audit record, section 5).
4. **Step 5 → Report v2.0 and Paper v2.0**: Part I for all 23 entries at clause level, Part II / Section 11,
   Appendix A.4, the contestable-call register with a D13 column, Appendix H from the protocol, criteria from
   `criteria.json` (D19, with 4.6's two wrong examples corrected), whole percents (D21), Corrections 1–7
   (Handoff 30, lines 260–292; Correction 7's C3.2 part is done), then the status paragraph in `build_readme.py`.
5. **Pages site and Hub**: a `schemas/` path for the schemas' `$id` URLs and a Pages workflow assembling
   `_site/` from the flat root; the Hub link (section 10), the root domain's `ai-manifest.json`,
   `research-index.json`, `llms.txt` and `sitemap.xml`, a pointer on the v1 site, a Medium update.
6. **Second pilot**: CCO-PTF-CIP-SZH, a replicator outside the Claude family; define its target in
   `build_replication_kit.py` with `r8=True` and its own pins after the rescoring pass; the brief forbids NEEC
   sources (its v1 scoring is public).
7. Git tags in place of the `_sNN_snapshot` files after v2.0; Visual Suite v3; the Actions versions moved to
   their Node 24 releases (optional polish); Appendix G / C14 on hold until the new Compassionism Simulation
   index ships.

## 9. Known limitations (stated, not hidden)

1. **D30's assignments** of the thirteen earlier entries are one maintainer's classification of their sources;
   the close calls are named in 5.1, and an archetype changes no score.
2. **D29's reach is bounded only for mechanism-class 0.5s** (131, read in the rescoring pass); for comprehensive
   systems and configured economies it is applied where the pass meets it. Until the pass reports, a tier could
   in principle change; the README says so.
3. **R8 is tested on a synthetic withholding** (the second pilot's target dropped from 3.1 and 5.1); the second
   kit's full withhold list, leak-scan terms and brief remain to be written against the post-rescoring protocol.
4. Handoff 35's limitations 1–4 stand (the R4 audit is one coder's reading; totals provisional; the historical
   `verify_ostrom.py` and group [I] staging; the near-duplicate negative capture; commit emails in public history).

## 10. Suggested Hub text (unchanged)

> Evaluation of how CCO and the broader Compassionism framework compare with 22 other economic systems on 26 normative criteria, with a published scoring protocol, blind replication, and a verification harness that reproduces every result. CCO's designer co-authors NEEC; the repository states this and the checks built for it. [NEEC v2 (in preparation)](https://github.com/BetterToBest/NormativeEvaluation) | [v1](https://sites.google.com/view/normativeeconomicevaluation/home) | [Article](https://medium.com/@duke.t.james/normative-economic-evaluation-for-the-automation-age-35bd4ef5e6a7)

## 11. Standing working notes

Shell is `sh` (no `time`, no process substitution); `git` is available. Maximum effort; accuracy over speed.
Scratch before insert; programmatic verification over visual checking; generate, don't transcribe. Scripts
find inputs beside themselves, print file names only, and are deterministic. `compare_replication.py` refuses
to run beside the canonical script; `verify_protocol_s36.py` refuses to run beside it too (it reads the corpus
file). Decisions are Claude's under the delegation: record them with reasons, flag substantive changes,
distinguish corrections from optional polish, say plainly when a file does not exist, and prefer precise,
defensible language. Give the owner click-by-click steps for anything in GitHub.
