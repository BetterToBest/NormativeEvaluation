# NEEC Project Handoff 45

**Session 45 · 2026-09-23 · Owner: Duke Johnson · Scorer and engineer: Claude (Opus 5.5)**
**Predecessor:** Handoff 44, whose sections 5–8 stand except where this handoff amends them.

> **Next session (46): Claude Code cloud, Opus 5.5, effort `xhigh`, in the same cloud session that lands this
> package (section 4).** From now on every session runs in the cloud and lands itself (decision 45.7); the owner
> stays out of the repository loop.

Session 45 wrote the **v2.0 criteria** (`NEEC_Criteria_v2_s45.md`): Package A fixed in wording, Package B adopted by
the owner (C2.6 Civil Liberties and Rule of Law, C3.6 Productive and Innovative Capacity), **28 criteria**, domain
maxima 6, 6, 6, 5, 5. `criteria.json` is generated from the pinned s44 criteria and the record's Appendix V by
generator version 2, which asserts seven rules; the protocol is draft.6. No published score changed. Harness v20,
**90 of 90**, byte-identical on a second run. The owner raised a further gap, **Package C** (record section 9):
proposed, awaiting the owner.

## 1. Session-start checks

`main` at `970fd36`, tags s34–s44, 259 files, digest match, harness v19 87 of 87 byte-identical, Handoff 44
identical to the Project's copy; Simulation `cd0ceec` and Research Hub `8e8a6ba` unchanged. The latest Actions run
could not be read (HTTP error from the API): unconfirmed.

## 2. What changed

- **Record** (`NEEC_Criteria_v2_s45.md`), decisions: 45.1 (owner: Package B; integer tier bands kept); 45.2 (Package
  A wording; four Requirement-versus-threshold gaps the review missed, C1.3, C3.3, C4.1, C5.1; K7, C2.5's association
  clause deleted and measured in C2.6); 45.3 (indicators and bars; ▲ choices); 45.4 (four aspirational clauses);
  45.5 (the site's own identity); 45.6 (on 28 criteria the totals 3.5, 10.5, 17.5 and 24.5 fall on a half percent;
  they round half up, which Python's `round()` does not do); 45.7 (sessions land by workflow). **The owner
  confirmed 45.2, 45.3 with every ▲ choice, 45.4 and 45.6.** Revision classes W, D, I, M, N, U fix what the pass
  re-checks (units: 115, 69, 161, 161, 46, 92).
- **`build_criteria.py` version 2**: rules A1–A7 (one figure per quantity, no Requirement figure outside its
  threshold, no dated threshold, no US-only measure, verbatim clauses, anchors equal thresholds, structure);
  `--selftest` plants one violation of each. The structure comes from Appendix V's structure line and new criteria
  are ordered by code, so adopting Package C needs no code change (dry-run on 29 criteria passed).
- **`criteria.json`** (neec-criteria/2.0: clauses, scope, revision class) and **`criteria_schema.json`** version 2.
- **`SCORING_PROTOCOL.md` draft.6**: header, a changes paragraph, 2.3, a 2.4 note on v2.0 arithmetic and Appendix B,
  all generated from the pinned draft.5.
- **`criteria_v2_s45.py`**: figure scan, norm weights (v2.0 range 1.8% to 16.1%; C4.1's derivation change lowers N6
  from 3.8% to 1.8%), units by class, registered quantities.
- **`run_all_checks.py` v20**: the four s44 files pinned as `*_s44_snapshot.*`; the Session 36–44 checks run on
  them, marked [Session 44 state]; three new checks. `build_readme.py` reads `criteria.json`; README regenerated.
- **New**: `CLAUDE.md` (standing session instructions), `.github/workflows/land-session.yml`,
  `NEEC_Site_Design_Brief_s45.md`.

## 3. Files

`NEEC_repository_s45.zip`, 20 files (12 new, 8 replaced), plus `land-session.yml`, uploaded separately (section 4):

| File | MD5 (first 8) | Status |
|---|---|---|
| `NEEC_Criteria_v2_s45.md` | `29e9b976` | new |
| `criteria_v2_s45.py` / `_output.txt` | `b7d2b832` / `9a8f57b9` | new |
| `build_criteria_s45_output.txt` / `_selftest_output.txt` | `5ccdd143` / `8b339b54` | new |
| `criteria_s44_snapshot.json`, `build_criteria_s44_snapshot.py` | `d4b78634`, `945843b2` | new |
| `SCORING_PROTOCOL_s44_snapshot.md`, `criteria_schema_s44_snapshot.json` | `bbee2c45`, `4aa5c6c6` | new |
| `NEEC_Site_Design_Brief_s45.md`, `CLAUDE.md` | `aec60e9d`, `58d5b3d7` | new |
| `NEEC_Project_Handoff_45.md` | (this file) | new |
| `build_criteria.py`, `criteria.json` | `711f27c7`, `f719926c` | replaced |
| `criteria_schema.json`, `SCORING_PROTOCOL.md` | `c49f89d7`, `183f9cd9` | replaced |
| `run_all_checks.py`, `run_all_checks_output.txt` | `a8bc3560`, `43b50414` | replaced |
| `build_readme.py`, `README.md` | `c1319a89`, `eeae50f1` | replaced |
| `.github/workflows/land-session.yml` (not in the zip) | `81b81fc7` | new |

## 4. Applying this package (the owner's last hands-on step)

One-time setup:

1. Claim the Claude Code cloud credit by **October 7, 2026**.
2. At claude.ai/code: connect GitHub, install the Claude GitHub app on `BetterToBest/NormativeEvaluation`, and give
   the environment full internet access (evidence work reads World Bank, IMF, Freedom House and similar sources;
   the default is limited).
3. On GitHub, open the repository's `.github/workflows` folder, **Add file → Upload files**, drop
   `land-session.yml`, **Commit changes** to `main`. You upload it because GitHub refuses workflow-file changes
   from an app without its workflow permission, and I cannot confirm the Claude app has it.

Then:

4. At the repository root, **Add file → Upload files**, drop `NEEC_repository_s45.zip`, **Commit changes** to `main`.
5. Start a cloud session on the repository and send this, filling in the Package C line:

```
NEEC: apply the Session 45 package, then begin Session 46.
Package C decision: <adopt C-1 and C-2 | adopt C-1, C-2 and C-3 | adopt none>
1. On a new branch from main, unzip NEEC_repository_s45.zip into the repository root, overwriting (20 files: 12 new, 8 replaced); delete the zip; git add -A. Confirm git ls-files shows 272 files, including .github/workflows/land-session.yml.
2. Run: python3 run_all_checks.py > /tmp/out.txt ; cmp /tmp/out.txt run_all_checks_output.txt
   Expect "SUMMARY: 90 passed, 0 failed, 0 skipped (of 90)." and no difference.
3. Commit with the message "NEEC Session 45: v2.0 criteria (28), generator v2, harness v20, landing workflow" and push the branch. Do not merge, open a pull request or tag.
4. Poll `git ls-remote --tags origin s45` each minute, up to 30 minutes. When s45 exists and the harness run it starts on main has finished, pull main and run:
   python3 session_check.py --tag s45 --files 272 --digest 115d9137d28ff22b158f4c1e0a96fd27 --handoff NEEC_Project_Handoff_45.md
   Expect ALL PASS. If the tag never appears, read the land-session run's log and repair.
5. Then follow CLAUDE.md and section 6 of NEEC_Project_Handoff_45.md as Session 46, on a new branch from main.
```

Every later session starts with one message: `Continue NEEC.` Replacing Handoff 44 in the claude.ai Project is
optional; GitHub is canonical.

## 5. Decision register

Protocol section 13 (D2–D31) unchanged; 45.1–45.7 join it when the pass ends. **Awaiting the owner: Package C**,
given in the first cloud message. Without it, Session 46 proceeds without C and records it as pending.

## 6. Next session (46): start here

1. Confirm that s45 landed (section 4, step 4).
2. Package C, as the owner decided. For each adopted element: write its block in Appendix V with named sources and
   bars (C-2's third clause from World Justice Project sub-factor 6.2 data; C-3 from WHO and World Bank coverage
   data), update the structure line, register the new quantities in both scripts' `QUANTITIES`, update record
   sections 7 and 9 and 45.6's text as decision 46.1, amending in place (tag s45 keeps the prior state). Regenerate
   by generator, recapture the outputs, harness.
3. Stage 2 begins (section 7).

## 7. Plan to completion (amends Handoff 44 section 7: every stage in the cloud)

| Stage | Sessions | Work | Effort |
|---|---|---|---|
| 1b | 46 | Package C; then stage 2 | xhigh |
| 2 | 46–48 | The pass on v2.0 clauses: part (b) remainder (C4.2, C4.4, C4.3, C4.5, C5.2, C5.4, C5.5); class I re-checks (the 42 configured-economy units, and any unit whose record cites a different measure); class M units clause by clause; class D rises (25 units at 0.5); new units (46; 69 with C-2; 92 with C-3) | xhigh |
| 3 | 49 | Apply the pass by generator (corpus, CSV and totals on v2.0; 45.6 rounding in every generator); R5 not-shown counts; the A.4 constraint scheme (S2) and proportional tiers; band texts and examples of restated criteria; `build_replication_kit.py`'s pinned MD5s before any new kit | high |
| 4 | 50–51 | Report v2.0 and Paper v2.0 (norm-weight table, aspirational disclosures, C2.2 disclosure) | xhigh / high |
| 5 | 52 | Paper v2.0 PDF from a committed build script, attached to the release | high |
| 6 | 53–54 | The site, per `NEEC_Site_Design_Brief_s45.md` | high |

**Credit.** Judgment work in the cloud draws more credit than the mechanical work planned for it. A session cannot
see the balance reliably, so the $50 cap holds only if the owner glances at it occasionally or sessions record
what they can see.

## 8. Standing notes

- Handoff 43's reopening conditions and limitations stand. The ▲ choices rest on the owner's confirmation, not on
  outside review.
- Workflow files change only through the owner (`CLAUDE.md`). `land-session.yml` already requests a Pages build
  after each landing, so stage 6 needs one owner setting: Pages from `main`, `/docs`.
- The Research Hub lives in `BetterToBest/research-hub`; linking it at stage 6 needs the Claude app there too and a
  way to land there (one owner click, or this workflow copied there by the owner). Decided at stage 6.
