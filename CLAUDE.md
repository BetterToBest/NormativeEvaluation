# Working on NEEC in Claude Code

This repository is maintained in working sessions by Claude (Anthropic) for its owner, Duke Johnson. From Session 52
the owner reviews every session before it reaches `main`: a session finishes by opening a pull request, and the owner
merges it (decision W9, `NEEC_Workflow_Package_s52.md`). These instructions apply to every session. Sessions run on
the owner's Claude plan, which has a session limit and a weekly limit; a session that stops at a limit must lose
nothing.

## Start

**The owner's opening prompt is usually just `Continue NEEC.`** That means: do the steps below, then the task in the
newest handoff's "Next session: start here" (its first line names the model and effort), and finish with a pull
request. Ask nothing the repository answers. Where the opening message carries decisions, record them first (step 5).

1. If a `NEEC_repository_s<n>.zip` is at the repository root, a chat session's package has not been applied yet:
   apply it first, as the note inside it describes.
2. Run `git fetch -q origin` and list open pull requests with
   `gh api 'repos/BetterToBest/NormativeEvaluation/pulls?state=open' --jq '.[] | "\(.number) \(.head.ref) \(.title)"'`
   (GraphQL is unavailable; use the REST API).
   - If a `claude/` branch carries commits whose messages begin `NEEC checkpoint` and no `NEEC Session` commit, a
     previous session stopped before finishing: merge that branch into your own, read its last checkpoint message,
     and continue its work before starting anything new.
   - If a session's pull request is open (title `NEEC Session <n>: ...`), the owner has not reviewed it yet. Branch
     from that pull request's head, not from `main`, so the work stacks; say so in your own pull request.
3. Read `STATE.md` (what is true now: open items, standing notes, reopening conditions, model routing), then the
   newest `NEEC_Project_Handoff_<n>.md` (highest n), whose section "Next session: start here" is the task list.
   Read long records by `grep` for the section needed, never whole; keep tool output short.
4. Run the start-of-session check the handoff gives (`session_check.py`) and expect ALL PASS, except as the handoff
   explains. If the previous session's pull request was merged but its tag is missing, read the `land-session` run's
   log and repair that first.
5. If the owner's opening message carries decisions by the IDs in `STATE.md`, record each as a numbered decision
   with its consequence before other work.

## Working within the usage limits

- One group of units per session. Push a checkpoint after each group, or sooner in long work: a commit whose
  message begins `NEEC checkpoint s<n>: `, pushed to your branch. A checkpoint need not pass the harness.
- Never print large files or long outputs: the Paper, the Report, `criteria.json`, recorded Jev responses, harness
  output (compare with `cmp`; show only its SUMMARY line). Scripts print file names and summaries, not data.
- **Suggest the next session's model and effort.** Every session ends by recommending both for the one after it,
  from `STATE.md`, "Model routing" (Opus 5.5 at high for judgment groups, xhigh only where the readings are
  contested; Sonnet 5.5 for mechanical sessions). Put the recommendation, with a clause of reason, in three places:
  the handoff's first line, the first item of `STATE.md`'s "Next work, in order", and the pull request body. If the
  next group looks harder or easier than the routing assumed, say so and name the model and effort you would
  choose instead. Only the owner can set them.

## Finish: how a session lands

- Work on your own `claude/` branch. Never push to main, merge into main, or create or push tags.
- Before the last commit, `python3 run_all_checks.py > /tmp/out.txt; cmp /tmp/out.txt run_all_checks_output.txt`
  must report no difference, `NEEC_Project_Handoff_<n>.md` (n = this session's number) must exist, and `STATE.md`
  must be rewritten to the state the session leaves.
- A handoff is self-contained: what changed, the files, the next session's steps. Standing notes and open items
  live in `STATE.md`; a handoff never says that an earlier handoff's sections "stand".
- The last commit's message begins `NEEC Session <n>: `. Push the branch, then open a pull request into `main` with
  the REST API (`gh api repos/BetterToBest/NormativeEvaluation/pulls -f title=... -f head=<branch> -f base=main -f
  body=...`). Title: the last commit's subject line. Body, short: what changed; the decisions the session made, each
  marked correction or optional; the items awaiting the owner; the suggested model and effort for the next session;
  whether the session stopped at a limit; and, if the branch stacks on another open pull request, its number. Never
  merge it.
- The owner reviews and merges. `.github/workflows/harness.yml` runs every check on the pull request;
  `.github/workflows/land-session.yml` runs when it is merged, reruns every check on `main`, tags each
  `NEEC Session <n>` commit the pull request carries `s<n>`, publishes a release and requests a Pages build.
- Workflow files (`.github/workflows/`) are changed only with the owner's approval in review: the app a session
  pushes through may lack GitHub's workflow permission, in which case the change is written into the handoff for
  the owner.

## Standards

- Record every substantive content change as a decision, with its reason and computed consequences; distinguish
  corrections from optional polish.
- When a file does not exist, say so; never write speculative content in its place.
- Precise, defensible wording. Published scores change only through the recorded rescoring pass, applied by a
  generator, never by hand.
- Decisions reserved to the owner wait for the owner's message; list them in `STATE.md` as awaiting the owner and
  continue with the rest.
- A session cannot see the plan's usage; the owner reads it in Settings > Usage. Record in the handoff only what
  the session did, and whether it stopped at a limit.
