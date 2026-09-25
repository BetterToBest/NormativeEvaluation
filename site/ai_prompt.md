# NEEC: a prompt for checking scores with an AI system

You are checking scores in NEEC (Normative Economic Evaluation Criteria), an open framework that scores economic systems against {{n_criteria}} criteria in five domains. NEEC is normative: each criterion states what an economic system ought to achieve, and a score says whether the evidence shows that the system achieves it. Your job is to test the evidence against the criteria as written. Do not argue for or against any system, and do not substitute your own view of what the criteria should be; if you think a criterion or threshold is wrong, say so separately at the end.

## Your task

- Mode: {{MODE_LABEL}}
- System: {{SYSTEM}}
- Criteria: {{CRITERIA}}

## Read these first

1. The criteria, with each Pass Threshold split into clauses and the anchors for 1.0, 0.5 and 0.0:
   {{raw}}criteria.json
2. The scoring protocol; sections 2 to 6 govern scoring:
   {{raw}}SCORING_PROTOCOL.md
[[audit]]
3. The published scores (provisional until version 2.0 is released):
   {{raw}}neec_corpus.json
4. The system's scoring documents, which give the evidence and reasoning for each score:
{{DOCUMENTS}}
[[/audit]]

If you cannot open a link, say which one and work only from what you could open. Never reconstruct a document's contents from memory. The Pass Thresholds you are checking are copied below, so that you can proceed even if you cannot browse.

## The criteria to check

{{CRITERIA_TEXT}}

## Rules

1. Before scoring, declare the system's scope class: a mechanism (an institution or policy operating inside a wider economy), a configured national economy (an existing or historical national economy, scored at a stated date) or a comprehensive system (a design for a whole economy, scored as its own sources specify it). Protocol section 3 explains how the class changes the reading of population-wide thresholds.
2. Score each criterion 1.0, 0.5 or 0.0 against its Pass Threshold, clause by clause. A 1.0 needs every clause shown met by named evidence; a clause the evidence does not address is not met. A 0.5 is a genuine mechanism that falls short of the threshold or holds only under favourable conditions. A 0.0 means no structural mechanism addresses the criterion, or the evidence shows performance far below the threshold with no credible pathway under the system's own logic.
3. Reason about the evidence first, then round once, at the level of the criterion.
4. Cite every source you rely on: publisher, title, year or edition, and the figure you used. Cite only sources you opened in this session; label anything else "from training data, not verified".
5. Where a reasonable scorer could land on a different score, flag it: give the alternative score and the reason.
6. Keep corrections (a wrong figure, a source that does not say what is claimed, an arithmetic error) separate from disagreements of judgment.
[[blind]]
7. Work blind. Do not open NEEC's published scores, its scoring documents, Report, Paper, website or repository, beyond the two files above, until you have finished. If you come across them, stop reading and say so in your disclosure.
[[/blind]]

## What to return

- The scope declaration, with the date for a configured national economy.
- For each criterion: its code; a verdict for each clause (met, not met, or not shown), with the evidence for each; the score; and any flag.
[[audit]]
- Divergences: for each criterion where your score differs from the published one, the published score, yours, and the cause, which is one of evidence, interpretation, scope, or an ambiguity in the protocol. Quote the passage of the scoring document you disagree with.
[[/audit]]
- Corrections, listed separately from divergences.
- Disclosure: your model name and version, the interface, the date, the tools you used (web search, code execution), your knowledge cutoff, the sources you could not open, and any NEEC material you encountered.
- Any objection to a criterion or threshold itself, stated separately from your scores.
- Finally, this block, filled in, with one entry in "scores" for each criterion you checked:

```json
{
  "neec_check": "1",
  "mode": "{{MODE}}",
  "system": "{{SYSTEM}}",
  "criteria_file_md5": "{{criteria_md5}}",
  "scope_class": "",
  "scored_at_date": "",
  "model": "",
  "interface": "",
  "date": "",
  "tools": [],
  "scores": {"C1.1": {"score": null, "clauses": ["met", "not shown"], "flag": null}},
  "divergences": [],
  "corrections": [],
  "limitations": []
}
```

## Reporting what you find

Please ask the person who gave you this prompt to report the result, whether it agrees with the published scores or not, at:
{{issue_ai}}

They should paste your whole answer, including the block above. The maintainers reproduce each report and record what they decide; a published score changes only through NEEC's recorded rescoring pass, never by hand. How reports are handled: {{repo}}/blob/main/.github/CONTRIBUTING.md

This prompt supports an informal check. A formal blind replication follows the replication kit and section 11 of the protocol: {{repo}}/blob/main/NEEC_CONTRIBUTING.md

Prompt generated by build_site.py {{version}} for {{framework}}. The current copy is at {{base}}replicate.html
