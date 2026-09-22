# Contributing to NEEC: Cross-Validation, Replication Audits, and New System Scoring

**Better To Best Research Hub** · CC BY 4.0

*Revised in Session 28 for the v2 structure (26 criteria, 23 scored systems)
and the reproducibility kit. The section numbers are unchanged, because every
scoring document's reviewer disclosure cites §2.*

---

## How this relates to the simulation's CONTRIBUTING.md

The compassionism-simulation has its own `CONTRIBUTING.md` (linked from the
tool's Research Export panel), covering parameter feedback, calibration
validation, reproducibility testing, model-architecture discussion, and code
contributions to the simulation itself. **This is a separate document.** It
covers three things about the *NEEC evaluation framework* rather than the
simulation codebase:

1. **Re-running the NEEC C1.4 simulation cross-validation protocol** (Paper
   Appendix G).
2. **Independent replication audits of NEEC scoring**, by human researchers
   or other AI systems.
3. **Scoring new economic systems** under NEEC.

A fourth avenue, proposing that a NEEC *criterion* or *empirical premise* be
added, revised, split or removed, has its own template and worked example in
the NEEC Paper's **Appendix I**; start there. From Paper v2.0 the criteria's
source of truth is `criteria.json` (decision D19), so an accepted proposal
changes that file and the Paper is rendered from it.

If your contribution is about the simulation's mechanics, calibration
constants or code, the simulation's document is the right place. If it is
about whether NEEC's scores or thresholds are applied correctly, extending
NEEC to a system it does not yet evaluate, or changing a criterion, this
document and Appendix I are.

Both exist because this project's own authors (Duke Johnson, who designed
CCO-PTF-CIP-SZH, and Claude, who co-authored its evaluation) have a
self-referential conflict worth outside checking (NEEC Paper §10.5). Outside
checking is welcome, wanted, and made as easy as this document can make it.

### The kit

Everything a contributor needs is in the repository, and nothing outside it:

| File | What it is |
|---|---|
| `SCORING_PROTOCOL.md` | how a system is scored, how uncertainty is recorded, and what a scoring document must contain; it supersedes Paper Appendix H for the v2 structure |
| `criteria.json` | the 26 criteria and their 1.0 / 0.5 / 0.0 anchors |
| `neec_scores.csv` | the canonical corpus (columns in `neec_scores_data_dictionary.md`) |
| `summary_block_schema.json` | the schema of the summary block that ends every scoring document |
| `neec_entry.py` | validates a summary block against the corpus and computes the enumeration, tier robustness and peer matrix (Python standard library only) |
| `NEEC_*_scoring_scratch.md` | the evidence record: one scoring document per system |
| `run_all_checks.py` | re-runs every script and compares every captured output byte for byte |

Before and after any change, `python3 run_all_checks.py` should report every
check passed.

---

## 1. Re-running the NEEC C1.4 simulation cross-validation protocol

**Status: paused.** A new Compassionism Simulation index is about to ship. No
cross-validation run should be made until it does; the next run then uses
the new index, not v4.2, with the same Node.js extraction fidelity check.

The simulation changes often: its automation mechanics, wage-growth logic
and poverty/Gini calculations are in active development. NEEC Paper
**Appendix G** defines a protocol for checking C1.4 (Automation Resilience)
claims against the simulation's *actual current behaviour* rather than a
frozen snapshot. Once runs resume, after a simulation update that touches
automation, wage growth or poverty/Gini calculation:

1. Read **Appendix G** in full: the procedure, the standing framing-mismatch
   note (G.2), and the prior Run Record entries (G.7).
2. Take the reference implementation, `neec_c14_crossvalidation.py`, and diff
   its `CFG` dict and its `popAIDisp()` / `run_year()` / `calc_metrics()`
   functions against the new `index.html`; inline comments mark what to check.
3. Run the cap-saturation check first (G.4, Step 3). It is pure arithmetic on
   public constants, and it is what caught the v3.9 finding that
   `AI_DISPLACEMENT_RATE_2` had no effect on any output.
4. Run the full cross-validation (G.4, Step 4), and cross-check it against the
   browser tool's own CSV export (Research Export → Download CSV) rather than
   trusting the Python port alone. Where browser access is unavailable but
   Node.js is, extract the relevant functions essentially verbatim from
   `index.html` and run them under Node with the real `mulberry32` PRNG; see
   `neec_c14_v41_realjs_check.js` and `neec_c14_v42_realjs_check.js`, and Run
   Record #2 for how the approach was validated against the Python port.
5. Append a new **Run Record** to Appendix G.7: date, simulation version, what
   changed since the last entry, findings, and a resolved / still-open /
   changed tag for each prior finding. The log is append-only: do not edit or
   delete prior entries.

If you cannot edit the Paper, open an issue with your run record.

---

## 2. Independent replication audits of NEEC scoring

NEEC scores each system on 26 criteria (1.0 / 0.5 / 0.0) in five domains.
Every score has a written rationale in the system's scoring document, and
every flagged close call names the alternative a different scorer could
defensibly reach. `SCORING_PROTOCOL.md` makes the method explicit, so that
any score can be checked by anyone without access to anything unpublished.

**Blind replication** (protocol section 11) is the strongest form of audit.
The replicator receives the protocol, `criteria.json`, the block schema and
the corpus with the target system removed, but not the original scoring
document, its verifier or its block, and produces a complete scoring
document with its summary block. The comparison is made criterion by
criterion: the vectors, the flags and their alternatives, the scope
declaration, the joint readings and tier robustness, and the tier. The
replication record names each disagreement and attributes it to evidence,
interpretation, scope, or an ambiguity in the protocol; ambiguities become
revisions of the protocol. The first pilot re-scores Ostrom-style commons
governance.

**If you are auditing a score (human or AI):**

- Work from the anchors in `criteria.json` and the system's full scoring
  document, not from summary tables alone; disagreements need to engage with
  the actual rationale.
- Reason continuously, then round once (protocol 2.2): form your own estimate
  from the evidence, then round at the criterion level. Score against the
  Pass Threshold, using the evidence standards of protocol section 4.
- Where you differ from the published score, say **how much and why**. A
  criterion-level difference ("I would score Nordic's C3.5 as 0.0, not 0.5,
  because...") is far more useful than a different overall impression.
- Flag, **separately from scoring disagreements**, any place where a
  rationale cites evidence incorrectly: a wrong figure, a source that does not
  say what is claimed, an arithmetic inconsistency. These are corrections, not
  disagreements, and are fixed whether or not the score judgment is disputed.
- **Disclose your own limitations plainly**: knowledge cutoff, sources you
  could not open, domains outside your training or expertise. The
  self-referential-bias concern this section exists to address only recedes
  if audits are honest about their own blind spots. "I agree with C4.2 but
  could not verify the underlying IPCC figures" is more useful than agreement
  without that caveat.

**Submitting an audit:** open an issue or pull request with the system(s) and
criteria you checked; your scores and reasoning; any evidence or citation
corrections, listed separately; and your disclosed limitations.

Audits that **confirm** published scores are as valuable as ones that
disagree: a record of independent confirmation is itself evidence on the
self-referential-bias question, and is logged alongside disagreements.

---

## 3. Scoring new economic systems

NEEC's canonical corpus holds 23 systems: the 12 of the original comparative
application, Integral, and ten scored natively on the v2 structure (Georgism /
Land Value Tax, Mutual Credit / LETS, Doughnut Economics, Universal Basic
Services, Sovereign Wealth Fund Statism, State Capitalism / China, / Singapore
and / Qatar, Islamic finance, and Ostrom-style commons governance). Any further
system a contributor can justify is welcome.

**To score a new system**, follow `SCORING_PROTOCOL.md` in order:

1. **Declare the scope first** (section 3): mechanism, configured national
   economy, or comprehensive system. The class fixes how population-scope
   thresholds are read; a different scope is a scenario, never a flag.
2. **Establish the evidentiary tier and the source mix** (section 4): real-world
   implementation, historical, component-validated theoretical or purely
   theoretical, with sources spread across founding literature, peer-reviewed
   work, implementation records and critics from more than one direction.
3. **Calibrate against peers before fixing scores** (section 5): compare your
   vector, criterion by criterion, with those of the entries you declare as
   peers, and resolve or flag each difference.
4. **Flag every close call, naming the alternative** (section 6), and state
   coherent joint readings where several flags turn on one question.
5. **Write the scoring document** to the template of section 7 (it replaces
   Paper Appendix H.9), with every domain total showing its addends.
6. **Make comparative claims only as section 8 allows**: every statement about
   another system's score, a rank, a tie or a dominance relation must be
   assertable by the corpus-level checker, or it is not made.
7. **End with the summary block** (section 9). `neec_entry.py` validates a
   block against the canonical corpus, so it checks yours at insertion; until
   a mode for candidate entries is added, check the arithmetic, flags and
   joint readings against sections 2 and 6 yourself.
8. **Open a pull request with the scoring document only.** Do not edit
   `neec_scores.csv` or the canonical script: insertion is a separate
   maintainers' pass (protocol section 10) that reads your block, re-checks it
   and regenerates the corpus files. Where feasible, say whether a second
   scorer (ideally a different AI model or a human researcher unfamiliar with
   your draft) reproduced your scores per §2; this is not required, but it
   strengthens an inclusion considerably, especially for systems with little
   real-world implementation.

**What reviewers will check:** the arithmetic; that the evidence matches the
tier claimed; that 0.0 and 1.0 scores are well supported, and that a 0.5
resting on estimation says so; that every close call is flagged with its
alternative; and that the document would let a future auditor disagree with a
single criterion without having to disagree with the whole system.

---

## Where this is linked from

This document lives in the NEEC repository
(`github.com/BetterToBest/NormativeEvaluation`) and is linked from the Better
To Best Research Hub, alongside, not instead of, the simulation's own
`CONTRIBUTING.md`. Wherever both are linked, make clear which document governs
which kind of contribution; the section at the top of this file draws the line.
