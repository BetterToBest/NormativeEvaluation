# NEEC blind replication — brief

**What this is.** A blind re-scoring of one system in the NEEC (Normative
Economic Evaluation Criteria) corpus. Its purpose is to test whether an
independent scorer, following the scoring protocol, reaches the same scores
(`SCORING_PROTOCOL.md`, section 11). You are the replicator. The system's
original scoring is not in this kit, and you should not look for it.

## The system to score

**Ostrom-style commons governance**: the self-governance of common-pool resources by the communities that use them, through rules those communities make, monitor and enforce, in the tradition of Elinor Ostrom's work (*Governing the Commons*, 1990) and the research that followed it.

Everything else is yours to decide under the protocol, and to state and
justify: the scope class and population rule (section 3), the evidence
(section 4), the peers (section 5), and the flags, joint readings and
scenarios (section 6).

## What is in this kit

| File | What it is |
|---|---|
| `SCORING_PROTOCOL.md` | the scoring protocol as a blind copy: 8 passages that report or refer to this system's original scoring are withheld and marked where they stood, and 1 example code naming it is replaced by another entry's; every rule is as in the full protocol |
| `criteria.json`, `criteria_schema.json` | the 26 criteria with their 1.0 / 0.5 / 0.0 anchors, and the schema |
| `summary_block_schema.json` | the schema of the summary block your document ends with |
| `neec_entry.py` | the entry verifier (Python 3, standard library only) |
| `neec_corpus.json` | the corpus: the other 22 scored entries, with their codes, scope classes and 26 scores |
| `REPLICATION_BRIEF.md` | this brief |

## What to produce

One Markdown scoring document, laid out as protocol section 7 requires,
ending with one summary block (section 9). Name it `NEEC_OstromCommons_replication_scoring.md`. In the block
use:

- `key` and `display_name`: `Ostrom-Style Commons Governance`
- `code`: `OSR`
- `record`: `documents` your file name; `scored` who scored it and when;
  `structure` `native-v2`
- `scope`: your declaration, with `basis` `stated`
- `peers`: the corpus entries you calibrated against (section 5)

## Checking your block

```
python3 neec_entry.py --candidate NEEC_OstromCommons_replication_scoring.md
```

It must end with `ALL BLOCKS VALID.` It also prints your peer matrix
(section 5.2); print it before you fix your scores, and reconcile every
difference it marks (5.3). The verifier checks structure and arithmetic, not
whether the evidence supports a score.

## Rules of blindness

1. Consult no NEEC material outside this kit: not the NEEC repository
   (github.com/BetterToBest/NormativeEvaluation) or its site, not the NEEC
   Paper, Report or Visual Suite, and no other account of how NEEC scored this
   system. If you come across such material, stop reading it and say so in
   your reviewer disclosure.
2. Use the evidence section 4 asks for: the founding literature, empirical
   work, implementations, and critical sources from more than one direction.
3. Send your document as it stands when you finish; do not revise it after
   seeing the original scoring.

## Reviewer disclosure

In the reviewer disclosure (section 7.2, item 9), state who or what scored
the entry (for an AI system, the model and the interface), the dates, the
tools used (web search, code execution), any NEEC material you encountered,
and every point where the protocol was ambiguous or silent. Those points are
the most useful result of a pilot: ambiguities become revisions of the
protocol.

---

*Kit built by `build_replication_kit.py` from `SCORING_PROTOCOL.md` (md5
13e382bc) and `neec_corpus.json` (md5 ba3c7f70).*
