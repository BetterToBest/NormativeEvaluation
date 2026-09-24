# NEEC Project Handoff 44

**Session 44 · 2026-09-23 · Owner: Duke Johnson · Scorer and engineer: Claude (Opus 5.5)**
**Predecessor:** Handoff 43, whose sections 9–11 stand except where section 8 below amends them.

> **Next session (45): Claude Opus 5.5, Extra effort, in the chat Project.** It restates thresholds and picks
> published indicators, which is judgment and web research. Drop to Medium if only the handoff remains.

Session 44 verified the Session 43 repository and, at the owner's request, **reviewed the 26 criteria for gaps,
redundancy and reproducibility** (`NEEC_Criteria_Review_s44.md`). Findings: five quantities are scored twice, three at
two different bars; two new Requirement-versus-threshold gaps; dated, US-bound and unpublished-quantity clauses; and two
gaps (productive capacity, civil liberties). **Package A** (corrections and restatements, still 26 criteria) is adopted
under the delegation and flagged; **Package B** (two new criteria, 26 → 28) **awaits the owner**. No score changed.
Harness v19, **87 of 87**, byte-identical on a second run.

## 1. Session-start checks

`main` at `649554c` (merge of pull request #10), tag `s43` on it; 254 tracked files; digest
`658f55fa2f282fdf9d7d2c65d1453135` (match); harness v18 86 of 86, byte-identical; Actions run 49 passed; Handoff 43
identical to the Project's copy. Simulation HEAD `cd0ceec`, Research Hub `8e8a6ba`, both unchanged.

## 2. What changed

- **Criteria review** (record, sections 2–7; evidence from `criteria_review_s44.py`):
  - K1–K5: wealth Gini (C1.2b, C4.4), proposals adopted (C2.4 at ≥35%, C4.4 at ≥40%), carbon and regeneration (C4.1,
    C4.2; regeneration at ≤90% and ≤100%), coercion share (C2.1, C4.5) each enter twice; each is kept in one criterion.
  - K6: C1.2a's Requirement says $70,000+ against a ≥$60,000 threshold; C1.4's measurement says <5% and 90–110%
    against <8% and >85%. (C1.1's 95%/90% gap was known.)
  - R1–R6: dated clauses; US-bound measures; clauses on quantities nobody publishes (the cause of most of the seven
    no-1.0 criteria); instrument clauses; 0.5 meaning either partial or not shown (publish a per-system count of
    not-shown units); "Racial and Gender Equity" → Group Equity.
  - S1–S3: implicit norm weights run from 15.4% (N7) to 1.9% (N11); N6 is called a hard constraint but scored
    compensatorily (add an A.4 constraint scheme, restate the sentence); N13 and N14 lack a core criterion.
  - G1 productive and innovative capacity (C3.6), G2 civil liberties and rule of law (C2.6), G3 N14 through
    consumption-based C4.2 and non-citizen coverage in C4.3.
- **Decision 7.1 (delegation, flagged):** Package A adopted; the pass continues on the revised clauses, so C4.2 and C4.4
  are scored once. **Decision 7.2 (owner):** Package B; recommended.
- **`session_check.py`** (new): the whole start-of-session check in one command (section 6). A session tool (needs git
  and network), not a harness check.
- `run_all_checks.py` v19 adds check 87; `README.md` regenerated (check count only).

## 3. Files

`NEEC_repository_s44.zip`, **8 files** at its top level:

| File | MD5 (first 8) | Status |
|---|---|---|
| `NEEC_Criteria_Review_s44.md` | `bc56676a` | new |
| `criteria_review_s44.py` | `e5cc159c` | new |
| `criteria_review_s44_output.txt` | `09427bb9` | new |
| `session_check.py` | `06db904c` | new |
| `NEEC_Project_Handoff_44.md` | (this file) | new |
| `run_all_checks.py` | `c71bb580` | replaced (v19) |
| `run_all_checks_output.txt` | `73d29f6c` | replaced |
| `README.md` | `7f42565e` | replaced |

The Project gets this handoff only (GitHub is canonical).

## 4. Updating the repository (owner)

1. On the repository page: **Add file → Upload files**, drop in `NEEC_repository_s44.zip`, **Commit changes** to `main`.
2. Paste to Claude Code (local, or a cloud session at claude.ai/code; see section 7 on the credit):

```
Session 44 update. NEEC_repository_s44.zip is now on main. Please:
1. Pull main and create a new branch from it.
2. Unzip NEEC_repository_s44.zip into the repository root, overwriting (8 files: 5 new, 3 replaced), then delete the zip and stage everything (git add -A).
3. Confirm git ls-files shows 259 files.
4. Run: python3 run_all_checks.py > /tmp/out.txt ; cmp /tmp/out.txt run_all_checks_output.txt
   Expect "SUMMARY: 87 passed, 0 failed, 0 skipped (of 87)." and cmp reporting no difference.
5. Run the fingerprint snippet in section 7 of NEEC_Project_Handoff_43.md, replacing NEEC_Project_Handoff_43.md with NEEC_Project_Handoff_44.md; expect 9631a8dba79932d8dd2765c056de0472.
6. Commit "NEEC Session 44: criteria review, Package A adopted (harness v19)", push, open a pull request into main, and merge it with a merge commit if you are able to (otherwise tell me).
7. Show me the full SHA of the merge commit. Do not create or push any tags.
8. Confirm the harness workflow passed on main.
```

3. Tag the merge commit: **Releases → Draft a new release → Choose a tag**, type `s44`, **Create new tag: s44 on
   publish**; **Target → Recent commits** → the Session 44 merge commit; title `s44`; **Publish release**.
4. In the Project, replace `NEEC_Project_Handoff_43.md` with this file.
5. **Tell Session 45 your Package B decision** in its first message: adopt both, G1 only, G2 only, or neither.

## 5. Decision register

Protocol section 13 (D2–D31) unchanged. Decisions 7.1 and 7.2 of the review join it when the pass ends. **Awaiting the
owner: Package B.** Without an answer, Session 45 proceeds on Package A and asks.

## 6. Next session: start here

1. Clone `https://github.com/BetterToBest/NormativeEvaluation` to `/home/claude/neec` (or fetch and confirm an existing
   clone), then run:
   `python3 session_check.py --tag s44 --files 259 --digest 9631a8dba79932d8dd2765c056de0472 --handoff NEEC_Project_Handoff_44.md`
   Expect `ALL PASS`. If the Session 44 update is not applied, ask the owner to finish section 4 first.
2. Take the owner's Package B decision.
3. **Write the v2.0 criteria** as a record with its script (`NEEC_Criteria_v2_s45.md`): each restated Pass Threshold
   with its reason; for the R3 criteria (C2.1, C2.3, C2.4, C3.1, C3.5), a published indicator with a named source, or
   an "aspirational" declaration; the dated clauses as rates from a stated base year; C1.1, C1.2a and C1.3 on
   international, price-year-stated measures. Then, by generator: snapshot `criteria.json` as
   `criteria_s44_snapshot.json` and pin every check that reads `criteria.json` to it; update `build_criteria.py` and
   regenerate `criteria.json` and protocol Appendix B; add assertions that each quantity appears in one Pass Threshold
   and that Requirement figures equal the threshold's. Harness v20.
4. Then the pass resumes (section 7, stage 2).

## 7. Plan to completion, with where and how to run each stage

**Claude Code cloud credit.** Pro subscribers get a one-time $100 credit for Claude Code cloud sessions, separate from
plan usage limits; **claim it by October 7, 2026** (the claim link, or `/claim-credit` in the CLI); a GitHub connection
is required, and each session works on its own branch and copy of the repository. Sources differ on whether the credit
is drawn first or only after the plan's limit is reached, so **record the remaining credit after each cloud session
here**. The owner caps NEEC at **$50**. Cloud sessions suit repository-mechanical, long-running work; judgment and
web-research work stays in the chat Project on the plan's limits, unless those limits bind.

| Stage | Sessions | Work | Where | Model · effort |
|---|---|---|---|---|
| 1 | 45 | v2.0 criteria (section 6) | chat | Opus 5.5 · Extra |
| 2 | 46–48 | Pass, part (b) remainder on the revised clauses: C4.2 and C4.4, then C4.3, C4.5, C5.2, C5.4, C5.5; units a removed clause decided (can only rise); Package B's 46 units if adopted | chat | Opus 5.5 · Extra |
| 3 | 49 | Parts (c)–(e); apply the whole pass by generator (Handoff 43 §8 item 4); publish the per-system count of not-shown units (R5) | cloud | Opus 5.5 · High |
| 4 | 50–51 | Report v2.0 and Paper v2.0 (Handoff 43 §8 item 5, plus the review's corrections, the norm-weight table and the A.4 constraint scheme) | chat for argument, cloud for regenerated tables | Opus 5.5 · Extra / High |
| 5 | 52 | **Paper v2.0 PDF** from the Markdown by a committed build script, so anyone can rebuild it; attach it to the release and the site | cloud | Opus 5.5 · High |
| 6 | 53–54 | **Pages site** from `/docs`, generated by a script from the repository's data (one source of truth, a harness check that the site's data equals the corpus): landing summary with the no-1.0 finding stated with its reasons, the Report, **Visual Suite v3** as a no-build page, the Paper PDF, the replication kit; styled to match the Research Hub (read its CSS from `BetterToBest/research-hub`); linked from the Hub (Handoff 37 §10) | cloud | Opus 5.5 · High |

Effort guide: **Extra** for threshold wording, evidence re-estimation and argument prose; **High** for generators,
site and build work; **Medium** when only a handoff is left. Opus 5.5 throughout; Fable 5.1 is not needed. In Claude
Code the Extra level is named `xhigh`. The second pilot and the Google Sites v1 pointer to v2 follow stage 6.

**Token economy.** Start with `session_check.py` (one call); read records by `grep` for the section needed, not whole;
keep tool output short (`tail`, `grep`); keep handoffs under about 1,300 words and refer to standing text by section.

## 8. Standing notes (amending Handoff 43 §11)

- Handoff 43's reopening conditions (§9.3) and limitations stand. The review is one reviewer's reading in one session;
  its draft clauses are wording proposals that Session 45 fixes; Package A's effect on scores is not yet computed.
- In a cloud session, whether tags can be pushed is untested; if refused, the owner tags through Releases as before.
- Check in the first cloud session whether its network settings reach the source sites evidence work needs; if not,
  keep evidence work in chat.
