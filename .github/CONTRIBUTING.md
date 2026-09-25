# Contributing to NEEC

NEEC is built to be challenged. This page says where each kind of contribution goes and what happens to
it. The method for replication audits and for scoring a new system is in
[`NEEC_CONTRIBUTING.md`](../NEEC_CONTRIBUTING.md), and the scoring rules are in
[`SCORING_PROTOCOL.md`](../SCORING_PROTOCOL.md). The [site](https://bettertobest.github.io/NormativeEvaluation/) has a button for each route on
every system and criterion page.

## Where each contribution goes

| You want to | Use |
|---|---|
| Contest one score for one system | [Challenge a score](https://github.com/BetterToBest/NormativeEvaluation/issues/new?template=score-challenge.yml) |
| Offer a source, figure or new edition that bears on a score | [Add evidence](https://github.com/BetterToBest/NormativeEvaluation/issues/new?template=new-evidence.yml) |
| Set a threshold, a reading or a weight differently | [Push back on a threshold](https://github.com/BetterToBest/NormativeEvaluation/issues/new?template=push-back.yml) |
| Report what an AI system found with the site's prompt | [Report an AI check](https://github.com/BetterToBest/NormativeEvaluation/issues/new?template=ai-replication.yml) |
| Suggest a system for NEEC to score | [Propose a system](https://github.com/BetterToBest/NormativeEvaluation/issues/new?template=propose-system.yml) |
| Suggest something an economy ought to achieve that no criterion measures | [Propose a criterion](https://github.com/BetterToBest/NormativeEvaluation/issues/new?template=propose-criterion.yml) |

The forms need a free GitHub account. Each asks only for what a maintainer needs to reproduce your point.

## Before you report a score

1. Read the criterion's Pass Threshold clause by clause, with its anchors for 1.0, 0.5 and 0.0, on its page
   on the site or in [`criteria.json`](../criteria.json). A 1.0 needs every clause shown by named evidence
   (protocol 2.3); a clause the evidence does not address is not met.
2. Read the system's scoring document, linked from its page. Disagreements need to engage with the actual
   rationale, not with a summary table.
3. Check whether the call is already registered as close: each scoring document lists the scores a
   reasonable scorer could set differently, and each system's page shows them once scores are published.

## Four kinds of difference

Say which kind yours is; each is handled differently.

- **Evidence.** A figure is wrong or out of date, or a source does not say what is claimed. This is a
  correction: it is made whether or not anyone disputes the judgment.
- **Interpretation.** The same evidence, read against the same clause, gives a different score. Quote the
  passage you disagree with.
- **Scope.** A different configuration or date, or a mechanism counted in that the entry leaves out
  (protocol section 3). A different scope is a scenario, not an error.
- **Protocol.** The protocol is silent or ambiguous at this point. These become revisions of the protocol.

## Reporting an AI check

The [Replicate](https://bettertobest.github.io/NormativeEvaluation/replicate.html#prompt) page builds a prompt that tells any AI system how to score and
what to return, in two modes: an audit of the published scores against their evidence, or a blind score
made without them. Paste the whole answer, including its JSON block, and name the model, the interface,
the date and the tools it used. Report confirmations too: independent confirmation is evidence on the
self-referential concern the Paper discusses (section 10.5), and it is logged as carefully as
disagreement. A formal blind replication follows the kit described in `NEEC_CONTRIBUTING.md`, section 2.

## Pushing back on a threshold

Thresholds are judgments about how much is enough, and NEEC wants disagreements about them on the record.
Say where you would set the bar, or how you would read the clause, and why. If you know which systems
would move, say so; if the data for the bar are public, name them. The
[Thresholds](https://bettertobest.github.io/NormativeEvaluation/thresholds.html) page lists the consequential choices already recorded, each with its
reason and alternative.

## Proposing a system or a criterion

A new system is scored in its own document under the protocol and inserted by a separate maintainers'
pass (`NEEC_CONTRIBUTING.md`, section 3; protocol sections 7 and 10). A new criterion joins only through a
recorded decision and a new version of the criteria, as the three added in version 2.0 did; a proposal
should say what the criterion asks, why no existing criterion measures it, and a threshold that published
data could test.

## What happens to a report

The maintainers are the project owner and the Claude working sessions that maintain the repository.

1. A maintainer reproduces the report: the figure, the source, the reading.
2. A correction of fact is made. A disagreement of judgment is weighed against the protocol and recorded
   as a numbered decision with its reason, in the criteria record or the protocol's decision register,
   whichever way it goes.
3. A score that changes does so through the recorded rescoring pass, applied by a script and checked by the
   verification harness before it is merged, never by hand. The record links the report.

## Pull requests

Open a pull request for a new system's scoring document only (`NEEC_CONTRIBUTING.md`, section 3, step 8).
Do not edit generated files: `neec_scores.csv`, `neec_corpus.json` and everything in `docs/` are
regenerated by scripts, and the verification harness checks each against the script that makes it. The site is generated by `build_site.py` from
the canonical files and the sources in `site/`.

## Conduct and licence

Engage with the evidence and the reasoning, not with people. Under GitHub's terms of service, content you
add to this repository is licensed under the repository's licence, CC BY 4.0.
