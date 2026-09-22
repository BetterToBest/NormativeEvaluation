# NEEC Project Handoff 35

**Session 35 · 2026-09-22 · Owner: Duke Johnson · Scorer and engineer: Claude**
**Predecessor:** Handoff 34 (in the Project and the repository). This handoff supersedes its sections 6–9.

Session 35 verified the pushed repository, recorded the owner's decisions, and did revision R4: an audit of
every corpus 1.0 that rests on a multi-clause Pass Threshold, followed by **decision D28**. No score, corpus
file or scoring document changed. The harness is at version 10, **75 of 75 checks passing**, byte-identical on
a second run.

---

## 1. Session-start checks

- **Project.** Handoff 34's 51 fingerprints matched; the Project holds exactly 200 files.
- **Repository.** Branch `claude/bold-davinci-tmee1x` (commit `25df70e`) of
  `github.com/BetterToBest/NormativeEvaluation`: 209 tracked files, all mode 100644, digest
  `a0acfb35c1a4c0227afbc41f91610c82` (exact match), tree `d96d2262a3ec54dd7c994c88b463a361a3e6603f`. All 200
  shared files are byte-identical with the Project; the nine repository-only files match Handoff 34's MD5s.
  Harness v9 in a clone ran 74 of 74, byte-identical to its capture.
- **GitHub Actions.** Run #1 of the `harness` workflow passed (38 s), which resolves Handoff 34's limitation
  2. It warns that `actions/checkout@v4`, `setup-python@v5` and `setup-node@v4` run on the deprecated Node 20
  (optional polish, section 9 item 8).
- **Open items found.** `main` (`9c28e12`) still holds only `NEEC_repository_s34.zip`; Claude Code has opened
  pull request #1 from the verified branch (CI green, mergeable) and is waiting for the merge. The `s34` tag
  was never created; Claude Code creates it after the merge. `llms.txt`'s raw links assume `main`.

## 2. Owner decisions

- **D27 confirmed:** (a) the full archive is published; (b) GitHub is the canonical file store; (c) licence
  CC BY 4.0 throughout; (d) `CITATION.cff` as built.
- **Decision authority delegated.** The owner asked not to have further decisions put to him ("You decide
  what is best"). From Session 35 Claude takes methodological and engineering decisions, records each with its
  reasons and computed consequences, and flags substantive changes plainly; the owner may reverse any of them.
  The owner still does what only the owner can: clicks in GitHub and claude.ai, and anything in his name.

## 3. Revision R4 and decision D28

Full text: `NEEC_R4_MultiClause_Audit_s35.md`; computation: `r4_audit_s35.py` (harness check 75).

- **Population.** 167 of the corpus's 184 scores of 1.0 rest on one of the 21 multi-clause thresholds; 542
  clause judgments, each coded from the unit's rationale (A addressed, P partial, X shortfall, S silent, N
  moot; lower case outside a mechanism's reach), each coded phrase located in the text.
- **Finding.** Only **33 of 167** are shown clause by clause; 33 contain a clause their own text says falls
  short; 101 leave a clause unaddressed. Eleven clauses are shown cleared by no audited 1.0 (C1.1's stress
  clause, C2.1's revealed preference, C2.3's satisfaction, both of C2.4's other clauses, C3.5's correction,
  C4.1's debt-to-GDP, C4.2's biodiversity, C4.4's removal mechanisms, both of C5.4's other clauses). How an
  out-of-reach clause counts decides only two units (SWF C2.5, OS C4.1).
- **D28 (decided).** 1.0 requires every clause shown cleared; silence is not clearance; a clause outside a
  mechanism's reach cannot be credited (0.5 at most); method clauses are met by evidence at least as strong as
  the method named; moot clauses do not block, read alike within a class; 0.0 stays holistic, so no tier can
  change; anchors describe and thresholds govern.
- **Textual bound.** Up to 134 scores 1.0 → 0.5 (67.0 points), plus up to eleven from C5.1's full second
  clause; no failure count or tier changes. Dominance pairs 14 → 32 and the frontier 12 → 6 under the bound.
  CCO-PTF-CIP-SZH keeps first place under every bound, and the record discloses why (its rationales state
  modelled figures for more clauses); the second pilot is the independent test.
- **Corrections found (not polish).** `criteria.json`'s anchor thresholds for C2.5, C3.1, C5.1 and C5.3
  differ in substance from the definitions. The Islamic finance and Ostrom documents quote the same working
  threshold under every criterion, 12 of 26 abridged or altered; eight audited 1.0s were scored against a
  quotation that drops a clause.
- **Application.** Nothing changes until the rescoring pass (section 9 item 4).

## 4. Harness v10 (75 checks) and landing pages

Check [75] runs `r4_audit_s35.py` (23 internal checks: clauses verbatim against the definitions, population,
rationale location, every coded phrase located, reach reasons, the three rules, quoted thresholds, the bound,
tiers unchanged, the record's two tables verbatim). Checks [1]–[74] are unchanged; [74]'s README capture
changes because `build_readme.py` now counts 75 checks and says the totals are provisional pending D28.
`llms.txt` says the same and links the record.

## 5. Files

The repository update is nine files at the zip's top level, `NEEC_repository_s35.zip`:

| File | MD5 (first 8) | Status |
|---|---|---|
| `r4_audit_s35.py` | `15f5e2aa` | new |
| `r4_audit_s35_output.txt` | `d110a899` | new |
| `NEEC_R4_MultiClause_Audit_s35.md` | `d236040d` | new |
| `NEEC_Project_Handoff_35.md` | (this file) | new |
| `run_all_checks.py` | `7d218da3` | replaced (v10) |
| `run_all_checks_output.txt` | `dc693ad1` | replaced (v10) |
| `build_readme.py` | `a43693f2` | replaced |
| `README.md` | `42506e7c` | replaced |
| `llms.txt` | `2df852a6` | replaced |

**The Project** gets this handoff only. It stays the verified Session 34 mirror (200 files) and is not
pruned: GitHub is canonical (D27b), sessions work from a clone, and removing about 120 files by hand would
free capacity the project no longer needs. Project copies of the five replaced files are stale by design.

## 6. Updating the repository

1. **Merge pull request #1** — either tell Claude Code "Please merge PR #1 yourself with a merge commit,
   then tag it s34 and confirm the checks", or open
   `https://github.com/BetterToBest/NormativeEvaluation/pull/1`, click **Merge pull request**, then
   **Confirm merge**. Claude Code then tags `s34`.
2. **Upload the zip**: on the repository page, **Add file → Upload files**, drop in
   `NEEC_repository_s35.zip`, **Commit changes** (to `main`).
3. **Paste to Claude Code:**

```
Session 35 update. NEEC_repository_s35.zip is now on main. Please:
1. Pull main and create a new branch from it.
2. Unzip NEEC_repository_s35.zip into the repository root, overwriting (9 files: 4 new, 5 replaced), then delete the zip and stage everything (git add -A).
3. Confirm git ls-files shows 213 files.
4. Run: python3 run_all_checks.py > /tmp/out.txt ; cmp /tmp/out.txt run_all_checks_output.txt
   Expect "SUMMARY: 75 passed, 0 failed, 0 skipped (of 75)." and cmp reporting no difference.
5. Run the fingerprint snippet in section 8 of NEEC_Project_Handoff_35.md; expect 20adca567f530ac005259f5a1d9ec94a.
6. Commit "NEEC Session 35: R4 multi-clause audit, decision D28, harness v10", push, open a pull request into main, and merge it with a merge commit if you are able to (otherwise tell me).
7. Tag the merge commit s35, push the tag, and confirm the harness workflow passed on main.
```

## 7. Decision register (for protocol draft.5's section 13)

D27 (owner, confirmed Session 35) and D28 (Claude under delegation, Session 35) join D2–D26. Draft.4 lists
two decisions as awaiting the owner: D23's publication of `neec_corpus.json` is settled by D27(a), and D24
(the blind copy) is confirmed under the delegation when draft.5 is written. Draft.4's "owner review pending"
becomes a record of the delegation.

## 8. Next session: start here

1. **Clone:** `git clone https://github.com/BetterToBest/NormativeEvaluation /home/claude/neec` (the sandbox
   reaches `github.com` through `git`; the REST API is rate-limited, so read Actions pages over HTTPS).
2. **Verify:** tags `s34` and `s35` exist; 213 tracked files; the digest below over every tracked file except
   this handoff equals `20adca567f530ac005259f5a1d9ec94a`; harness v10 runs 75 of 75, byte-identical to
   `run_all_checks_output.txt`; the latest Actions run on `main` passed. If the Session 35 update has not been
   applied, ask the owner to finish section 6 first (the zip is in the Session 35 conversation).

```
import hashlib, subprocess
h = hashlib.md5()
for f in sorted(x for x in subprocess.check_output(["git", "ls-files"]).decode().split("\n") if x):
    if f != "NEEC_Project_Handoff_35.md":
        h.update(f.encode() + b"\0" + hashlib.md5(open(f, "rb").read()).digest())
print(h.hexdigest())
```

3. **Then** section 9, item 3.

## 9. Next steps, in priority order

1. **Owner:** section 6; add this handoff to the Project.
2. **Next session:** verify (section 8).
3. **Protocol v2.0-draft.5.** Write R1 (D18(b)'s scope-or-doubt test, 3.4), R2 (implementation failure
   versus the system's own logic, 2.1 and 4.1), R3 (C3.2's 0.0 band per D26 and Correction 7), R4 (D28's text,
   record section 6, into 2.3, 3.2 and 4.6), R5 (archetype table, 5.1), R6 (extension boundary, 3.2), R7 (the
   pilot's result, 11.6) and R8 (blind-copy withholding, for future kits in `build_replication_kit.py`). R2,
   R5 and R6 are decided in that session and recorded as D29 onward. Correct `criteria.json`'s four anchor
   thresholds to the definitions' text through `build_criteria.py`, pinning the current file as a snapshot for
   the historical checks that read it. The new protocol version changes `README.md` through
   `build_readme.py`: regenerate it and recapture check [74].
4. **D28 rescoring pass** (record section 7), before Step 5 and the second pilot: the 33 stated-shortfall
   units first, then the other 101 criterion by criterion, plus C5.1's full second clause for its thirteen
   1.0s; clause-level estimates in a rescoring document; changes by generator with pinned inputs; scoring
   documents restated in place (D12, D14), including the Islamic finance and Ostrom quotations; corpus, CSV,
   README and Appendix A.4 regenerated.
5. **Step 5 → Report v2.0 and Paper v2.0**: Part I for all 23 entries at clause level (the eight new ones and
   the thirteen restated), Part II / Section 11, Appendix A.4, the contestable-call register with a D13
   column, Appendix H from the protocol, criteria from `criteria.json` (D19), whole percents (D21),
   Corrections 1–7 (Handoff 30, lines 260–292). Then update the status paragraph in `build_readme.py`.
6. **Pages site and Hub**: a `schemas/` path for the schemas' `$id` URLs and a Pages workflow assembling
   `_site/` from the flat root; the Hub link (section 11), the root domain's `ai-manifest.json`,
   `research-index.json`, `llms.txt` and `sitemap.xml`, a pointer on the v1 site, a Medium update.
7. **Second pilot**: CCO-PTF-CIP-SZH, a replicator outside the Claude family, a kit built with R8.
8. Git tags in place of the `_sNN_snapshot` files after v2.0; Visual Suite v3; the Actions versions moved to
   their Node 24 releases (optional polish); Appendix G / C14 on hold until the new Compassionism Simulation
   index ships.

## 10. Known limitations (stated, not hidden)

1. The R4 audit is one coder's reading of text, not evidence; its A/S boundary for qualitative claims involves
   judgment. Every call is traceable to a located phrase or its absence.
2. Until the rescoring pass, the published totals overstate what the rationales show; `README.md` and
   `llms.txt` say so.
3. Handoff 34's limitations 1 and 3 stand (historical `verify_ostrom.py`, the Session 28 staging in the claims
   verifier's group [I], optional CSV polish; the near-duplicate negative-control capture).
4. Commits made through the GitHub web page carry the committer's email address in public history. GitHub's
   Settings → Emails → "Keep my email addresses private" substitutes a noreply address for future commits.

## 11. Suggested Hub text

For the Hub's "Economic System Comparison" section, once `main` holds the corpus:

> Evaluation of how CCO and the broader Compassionism framework compare with 22 other economic systems on 26 normative criteria, with a published scoring protocol, blind replication, and a verification harness that reproduces every result. CCO's designer co-authors NEEC; the repository states this and the checks built for it. [NEEC v2 (in preparation)](https://github.com/BetterToBest/NormativeEvaluation) | [v1](https://sites.google.com/view/normativeeconomicevaluation/home) | [Article](https://medium.com/@duke.t.james/normative-economic-evaluation-for-the-automation-age-35bd4ef5e6a7)

## 12. Standing working notes

Shell is `sh` (no `time`, no process substitution); `git` is available. Maximum effort; accuracy over speed.
Scratch before insert; programmatic verification over visual checking; generate, don't transcribe. Scripts
find inputs beside themselves, print file names only, and are deterministic. `compare_replication.py` refuses
to run beside the canonical script. Decisions are Claude's under the delegation: record them with reasons,
flag substantive changes, distinguish corrections from optional polish, say plainly when a file does not
exist, and prefer precise, defensible language. Give the owner click-by-click steps for anything in GitHub.
