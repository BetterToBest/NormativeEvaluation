# Working on NEEC in Claude Code

This repository is maintained in working sessions by Claude (Anthropic) for its owner, Duke Johnson, who has
asked to stay out of the repository loop (decision 45.7, `NEEC_Criteria_v2_s45.md`). These instructions apply to
every session.

## Start

1. If a `NEEC_repository_s<n>.zip` is at the repository root, a chat session's package has not been applied yet:
   apply it first, as the handoff inside it describes (section 4).
2. Read the newest `NEEC_Project_Handoff_<n>.md` (highest n). Its section "Next session: start here" is the task
   list. Read long records by `grep` for the section needed, not whole; keep tool output short.
3. Run the start-of-session check it gives (`session_check.py`) and expect ALL PASS. If the previous landing
   failed (its tag is missing), repair that first.

## Finish: how a session lands

- Work on your own branch. Never push to main, merge, open a pull request, or create or push tags.
- Before the last commit, `python3 run_all_checks.py > /tmp/out.txt; cmp /tmp/out.txt run_all_checks_output.txt`
  must report no difference, and `NEEC_Project_Handoff_<n>.md` (n = this session's number) must exist.
- The last commit's message begins `NEEC Session <n>: `. Push the branch. `.github/workflows/land-session.yml`
  merges it into main, reruns every check on the merged tree, tags the merge commit `s<n>` and publishes a
  release. Only that message starts a landing; give intermediate commits any other message.
- Workflow files (`.github/workflows/`) are changed only by the owner: the app a session pushes through may lack
  GitHub's workflow permission. A change a session needs there is written into the handoff for the owner.

## Standards

- Record every substantive content change as a decision, with its reason and computed consequences; distinguish
  corrections from optional polish.
- When a file does not exist, say so; never write speculative content in its place.
- Precise, defensible wording. Published scores change only through the recorded rescoring pass, applied by a
  generator, never by hand.
- Decisions the handoff reserves to the owner wait for the owner's message; record them as awaiting the owner
  and continue with the rest.
- Record in each handoff the Claude Code cloud credit remaining, where the session can see it; the owner's cap
  for NEEC is $50.
