# NEEC Jev pilot: automated interpretation check, package for Session 50

Prepared in a claude.ai chat session on 2026-09-25, at the owner's request, from the repository at tag `s48`
(`5aed860`). It records a pilot of Jev, TypeSafe AI's System One model, as an independent, non-Claude judge of clause
verdicts. It changes no score, criterion, protocol text, corpus file or site file.

## 1. What this is, and what it is not

Jev does not generate text, browse, or reason across steps. Given a text (its "state") and a question with fixed
options, it returns the option, a probability for each option and a confidence. The owner adopted it on 2026-09-25
under the label **automated interpretation check**: with the evidence held fixed, it tests whether the reading of a
clause holds up for a judge outside the Claude family, which has produced and checked every NEEC score so far. It is
**not a blind replication** under protocol section 11, which requires gathering evidence, opening sources and scoring
a whole entry; Jev can do none of these.

## 2. Method

- **Model and route.** `jev-1.13.0`, pinned (the `jev-latest` alias moves with new releases), through the Composio Jev
  toolkit connected to the owner's claude.ai account.
- **States.** Pilot 1 and part (c): each system's C2.1 rationale from Report v1.6, with the score removed; no system
  name, score or pass status. Part (a): the pass's C4.4 clause 2 evidence for the five cleared units, as recorded;
  for Degrowth, its Report v1.6 C4.4 rationale. Part (b): the OpenResearch findings from the pass's CCO C2.1 clause 2
  record. Two states were edited, and the edits are declared in the check script: NSD's C4.4 evidence drops the
  pass's verdict phrase ("parliamentary removal functions") and keeps the fact; part (b) drops the pass's evaluative
  clauses and citations and keeps the findings.
- **Questions.** One Choice question per clause. Options map to the pass statuses (C cleared, S short, U not shown).
  Part (a)'s instruction restates part (b7)'s reading 3.5 (`NEEC_Rescoring_s47.md`). Part (b) adds two yes/no questions
  that split C2.1 clause 2 into its parts: behaviour observed, and behaviour compared with self-reports. Part (c)
  repeats pilot 1's clause 1 with one change: a claim the text "projects, or judges plausible" counts as asserted.
- **Runs.** Pilot 1 three times; pilot 2 twice. All 54 requests and responses are in `jev_pilot_2026-09-25.json`.
  Pilot 1's first run was transcribed from the connector's response; every other record is as saved. Token usage is
  omitted; the 54 calls used about 30,000 input tokens (listed price $0.042 per million).

## 3. Results

`jev_pilot_check.py` regenerates every table from the recorded responses and checks each state against its source.
Its output is `jev_pilot_check_output.txt`; its summary line:

    SUMMARY: pilot 1 12 of 16; part (a) 6 of 6; part (b) 1 of 1; part (c) 5 of 8; 0 checks failed

| Part | Clause | Agreement with the pass |
|---|---|---|
| Pilot 1 | C2.1 clause 1, "≥70% report genuine autonomy in major life decisions" | 4 of 8 |
| Pilot 1 | C2.1 clause 2, revealed-preference validation | 8 of 8 (all not shown) |
| 2 (a) | C4.4 clause 2, "removal/replacement mechanisms functional" | 6 of 6 (5 shown, 1 not shown) |
| 2 (b) | C2.1 clause 2, decomposed (CCO component evidence) | 1 of 1 |
| 2 (c) | C2.1 clause 1, revised wording | 5 of 8 |

## 4. Findings

1. **Consistency.** Every question returned the same option in every run. Probabilities moved by at most 0.06.
   Jev is stable but not byte-identical, so no live call belongs in the harness.
2. **Positive evidence is recognised.** Part (a) cleared all five units whose recorded mechanisms meet reading 3.5,
   including Integral by the reading's rule for designs that delegate no authority (0.95 to 0.96). It refused
   Degrowth's text, which names democratic governance as a goal without a mechanism (1.00), as reading 3.5 requires.
3. **Decomposition works.** On the OpenResearch findings, Jev found observed behaviour reported (0.98) and no
   comparison with self-reported autonomy (0.04 to 0.05), and so did not clear the clause: the pass's own reasoning,
   reproduced by two literal questions.
4. **Confidence tracks difficulty.** The least confident answers fell on the units the pass itself found hard: UBI's
   C2.1 clause 1 (0.10 to 0.35; the pass: the figure "straddles the bar, measures an increase rather than genuine
   autonomy, and is unsourced"), Market Socialism's (0.45 to 0.50), and Nordic Social Democracy's C4.4 clause 2
   (0.70 to 0.71), where one confidence vote in operation stands for a capacity.
5. **Every disagreement is a clause carried "as audited".** Under the rule in `NEEC_Rescoring_s37.md`, section 2, a
   clause the R4 audit coded as asserted is carried as cleared on the unit's own text without re-estimation. Jev
   disagreed only there. With the revised wording, Integral moved to agreement (its text calls the 70% level
   "plausible"; 0.74 to 0.76), and nothing else moved: Degrowth, FALC and Participatory Economics still do not state
   the clause (0.89 to 0.98).
6. **Wording matters, as the vendor documents.** One criterion word ("plausible" as against "states") changed one
   verdict. Question wording is part of the method and must be recorded with each run.

## 5. Decisions for the record

Record these as numbered decisions in the criteria record's decision list (or wherever Session 50 judges right).

- **J1 (the owner's, 2026-09-25).** Jev is adopted as an **automated interpretation check**, under that label.
- **J2 (the chat session's, flagged).** Its role is flag-only. A disagreement, or a confidence below a threshold set
  per clause when a full run is designed, routes a unit to review within the recorded rescoring pass. It never changes
  a score, and its output is never described as a replication.
- **J3 (the chat session's).** Each run pins a model version and records it with every response. The harness checks
  recorded responses only (`jev_pilot_check.py` makes no network call).
- **J4 (the chat session's, flagged).** Question design: one clause per question; any comparison of a figure with a
  bar is made in code, never by Jev (its documentation lists numeric precision as a weakness); the instruction restates
  the pass's recorded reading of the clause; states hold source or published text, never a verdict or the scorer's
  reasoning, and any edit to a state is declared.
- **J5 (recommendation, awaiting the owner).** Blind replication under protocol section 11 stays with a generative
  model that can open sources. The next kit, built after stage 3, should go to a non-Claude model (the first pilot's
  replicator was Claude Sonnet 5), so that replication and the interpretation check are independent of Claude in
  different ways.

## 6. Flags for the pass (not corrections)

Degrowth, FALC and Participatory Economics C2.1 clause 1 are carried as cleared "as audited", and their texts do not
state the clause on a literal reading (section 4, finding 5). No score changes: all three units are 0.5 because
clause 2 is not shown. The clause matters if a later session clears clause 2 for any of them, and Report v2.0's
clause-level Part I must estimate it in any case (`NEEC_Rescoring_s37.md`, section 2). Record these three as flagged
for that estimate.

## 7. Limits

Two criteria, 22 distinct unit-clause verdicts (31 comparisons in all). Part (a)'s positive states are the evidence the scorer selected, so agreement
there shows recognition, not independent discovery. The questions were written by Claude: the judge is independent of
Claude, the rubric is not. The states are short published texts and pass records, not source excerpts.

## 8. Applying this package

For the cloud session that finds `NEEC_repository_s50.zip` at the repository root (CLAUDE.md, Start, step 1).

1. On a new branch from main, unzip `NEEC_repository_s50.zip` into the repository root (4 new files: this note,
   `jev_pilot_2026-09-25.json`, `jev_pilot_check.py`, `jev_pilot_check_output.txt`); delete the zip; `git add -A`.
2. Run `python3 jev_pilot_check.py > /tmp/jev.txt ; cmp /tmp/jev.txt jev_pilot_check_output.txt`. Expect exit status
   0, the summary line in section 3, and no difference. The script reads `NEEC_Report_v1_6.md` and
   `rescoring_s37.py` to `rescoring_s48.py`; if a later session has changed a record it reads, report the difference
   and its cause rather than editing the recorded responses.
3. Add a harness check that runs `python3 jev_pilot_check.py`, requires exit status 0 and prints its summary line,
   the way the harness adds its other script checks. Update the check count and summary line, recapture
   `run_all_checks_output.txt`, and run the harness again.
4. Record J1 to J5 (section 5) and the flags in section 6. Then continue with the newest handoff's "Next session:
   start here".
5. In the handoff, carry J5 as awaiting the owner, and add to the standing notes: Jev runs are made in a claude.ai
   chat through the owner's Composio connection and delivered as recorded files; a cloud session that calls Jev
   directly needs a TypeSafe API key set by the owner as an environment secret, never committed.
