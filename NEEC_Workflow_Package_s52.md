# NEEC workflow package, for Session 52

Prepared in a claude.ai chat session on 2026-09-26, at the owner's request, from the repository at tag `s51` (`main`
at `14f435a`, 410 files). The Claude Code cloud credit is spent, and sessions now run on the owner's Pro plan: a
five-hour session limit and a weekly limit, shared with every other use of the account. The package changes how
sessions start, work and finish. It changes no score, criterion, protocol text, corpus file, script, `docs/` or
`site/`.

## 1. What the package does

- **`CLAUDE.md` (replaced).** Additions: resume an unlanded branch that carries checkpoint commits (Start, step 2);
  read `STATE.md` before the handoff (step 3); record the owner's decisions by `STATE.md` ID first (step 5); a
  section "Working within the usage limits" (one group per session, checkpoint commits, no large outputs, the next
  session's model and effort from `STATE.md`); `STATE.md` rewritten at every landing and handoffs self-contained
  (Finish). The credit rule is replaced: a session cannot see the plan's usage, so the handoff records only what the
  session did and whether it stopped at a limit. Everything else is unchanged, word for word.
- **`STATE.md` (new).** What is true now: position, next work, the items awaiting the owner (IDs 48.3 to W8), model
  routing, the reopening conditions of the design's units, and the standing notes of Handoffs 43 to 51,
  consolidated so that no session need follow the chain of "sections stand" references back through them.
- **This note (new).**

## 2. Decisions for the record

- **W3 (the owner's, by uploading this package).** `STATE.md` holds the standing state; handoffs are self-contained;
  the usage rule replaces the credit rule.
- **W4 (the owner's, by uploading this package).** Checkpoint commits (`NEEC checkpoint s<n>: `) after each group, and
  a new session resumes an unlanded branch before new work.
- **W1, W2 and W5 to W8** are proposals awaiting the owner, listed in `STATE.md`. The owner holds a decisions sheet
  (a Claude Doc) with the reasons and the chat session's suggestion for each of the 23 items; the answers arrive in
  the opening message by ID.

Suggested numbering: 52.1 (W3), 52.2 (W4) and 52.3 (W9, section 5), then the owner's answers from 52.4. **Record them in one amendment of
`NEEC_Criteria_v2_s45.md`**, so that the site's regeneration chain (every amendment changes `criteria.json`'s
`record_md5` and 64 `docs/` footers) runs once, not once per decision.

## 3. Files

| File | Status |
|---|---|
| `CLAUDE.md` | replaced (amended 2026-10-14 for W9: sessions finish by opening a pull request) |
| `STATE.md` | new (amended 2026-10-14: W9, W10, the simulation overhaul, Sonnet 5.5 in W1) |
| `NEEC_Workflow_Package_s52.md` | new (this note) |
| `.github/workflows/land-session.yml` | replaced (2026-10-14, W9): lands on a merged pull request instead of on push |

After the pull request that carries these files is merged: **412 tracked files** (the workflow file is replaced, not
added). With them in place, `run_all_checks.py` reproduces `run_all_checks_output.txt` byte for byte (SUMMARY 99 of
99; verified 2026-10-14 under Python 3.13), because no check reads them.

## 4. Applying this package

The package was not uploaded as a ZIP. On 2026-10-14 a claude.ai chat session committed its files directly to the
branch `claude/s52-pr-workflow` and opened a pull request; the owner's merge applies it. Session 52 therefore starts
from `main` with the package in place, and does not unzip anything.

1. Run `python3 session_check.py --tag s51 --files 410 --digest ec86eaae1c9c8ab0e50120e627503ba7 --handoff NEEC_Project_Handoff_51.md`.
   Expect failures that the package explains: "s51 points at HEAD", the file count (412), and the digest. Confirm
   with `git diff --stat s51 HEAD` that the four files above (and the merge) are the only difference. The other
   checks must pass.
2. Record the decisions (section 2), W9 (section 5) and the owner's answers, in one amendment.
3. Continue with `STATE.md`, "Next work". Rewrite `STATE.md` and write Handoff 52 before opening the session's pull
   request, as `CLAUDE.md` says.

## 5. Added on 2026-10-14

- **W9, landing by pull request (the owner's, by merging the pull request that carries it).** The owner asked to
  review each session before it reaches `main`. Decision 45.7's push-triggered landing merged a branch the moment its
  `NEEC Session <n>` commit arrived, so it is replaced: `land-session.yml` now runs when a pull request into `main` is
  merged, reruns every check on `main`, and tags each session commit the pull request carried. A pull request that
  stacks two sessions (opened while the earlier one awaited review) lands both. `harness.yml` already runs on pull
  requests, so the owner sees the checks before merging. Requiring that check to pass before merging (branch
  protection) is the owner's option in the repository's settings. Consequence: the README's sentence on landing
  becomes inaccurate; Session 52 corrects it through `build_readme.py` (`STATE.md`, Next work, item 2).
- **W10, a chat path (awaiting the owner).** From about 2026-10-16 the owner may have no Claude Code. The same
  landing then works by hand: the owner downloads the repository ZIP from GitHub, a chat session works on it and runs
  the harness in its own sandbox, and returns a ZIP of changed files with the handoff; the owner uploads those files
  through GitHub's web interface to a new branch, with a commit message beginning `NEEC Session <n>: `, and opens a
  pull request. `harness.yml` checks it and `land-session.yml` tags it on merge. Smaller groups suit that path, which
  is part of the case for W2 and W6.
- **PR #12** (`claude/clever-newton-17rt1c`, "Session 49: Apply NEEC site package") was a second Session 49 branch
  that never landed; Session 49 landed from `claude/vibrant-brown-ucux73` as `a379f74` (tag `s49`). It was closed
  unmerged, with a comment, on 2026-10-14. Merging it would have reintroduced superseded files.
- **Remaining work, as estimated in Handoff 51:** stage 2, three to four sessions; stage 3, one; the Report and the
  Paper v2.0, two; the PDF, one. That is more than one Pro week's remaining usage; W6's triage and W7 are the
  scope decisions that shorten it.
