#!/usr/bin/env python3
"""
build_readme.py -- Session 34 (provisional-totals paragraph revised in Session 36)
=================================================================================
Writes README.md, the repository's landing page, from the canonical data. The
score table, the tier counts, the corpus size, the example of a higher total in
a lower tier, and the number of reproducibility checks are computed here from
neec_scores.csv and run_all_checks.py, never typed in, and run_all_checks.py
regenerates README.md and compares it byte for byte with the committed copy
(the protocol's version and review status are read from SCORING_PROTOCOL.md's header),
so the landing page cannot drift from the data. The prose is fixed text below;
edit it here, then rerun this script.

Run: python3 build_readme.py   (writes README.md beside itself; prints the file name)
"""
import csv
import importlib.util
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TIERS = ("Potentially Adequate", "Partially Adequate", "Structurally Inadequate")


def tier(fails):
    return TIERS[0] if fails < 3 else (TIERS[1] if fails <= 5 else TIERS[2])


with open(os.path.join(HERE, "neec_scores.csv"), newline="", encoding="utf-8") as f:
    ROWS = list(csv.DictReader(f))
for r in ROWS:
    r["total"] = float(r["total_score"])
    r["fails"] = int(r["failures"])
    assert r["criteria_count"] == "26", r["system"]
    assert r["adequacy_tier"] == tier(r["fails"]), r["system"]
    assert r["total_percent"] == f"{round(r['total'] / 26 * 100)}%", r["system"]

spec = importlib.util.spec_from_file_location("harness", os.path.join(HERE, "run_all_checks.py"))
harness = importlib.util.module_from_spec(spec)
spec.loader.exec_module(harness)
N_CHECKS = len(harness.CHECKS)

import re  # noqa: E402  (the protocol's version and review status, read from its header)
with open(os.path.join(HERE, "SCORING_PROTOCOL.md"), encoding="utf-8") as f:
    HEAD = f.read(2000)
PROTOCOL_VERSION = re.search(r"\*\*Version (\S+) ", HEAD).group(1)
PROTOCOL_STATUS = (", owner review pending" if "review of the whole text is pending" in HEAD.replace("\n", " ")
                   else "")

N = len(ROWS)
COUNTS = {t: sum(r["adequacy_tier"] == t for r in ROWS) for t in TIERS}
ranked = sorted(ROWS, key=lambda r: -r["total"])  # stable: ties keep the CSV's order
for r in ranked:
    r["rank"] = 1 + sum(o["total"] > r["total"] for o in ROWS)
    r["tied"] = sum(o["total"] == r["total"] for o in ROWS) > 1

# The example of a higher total in a lower tier: the largest tier gap, then the largest score gap.
pairs = [(TIERS.index(a["adequacy_tier"]) - TIERS.index(b["adequacy_tier"]), a["total"] - b["total"], a, b)
         for a in ROWS for b in ROWS if a["total"] > b["total"]
         and TIERS.index(a["adequacy_tier"]) > TIERS.index(b["adequacy_tier"])]
gap, _, HI, LO = max(pairs, key=lambda p: (p[0], p[1]))
TOP = ranked[0]
assert TOP["system"] == "CCO-PTF-CIP-SZH" and ranked[1]["total"] < TOP["total"]


def fmt(x):
    return f"{x:.1f}"


def short(name):
    return name.split(" (")[0]


WORDS = {1: "one", 2: "two"}


table = ["| Rank | System | Score (of 26) | Percent | Structural failures | Adequacy tier |",
         "|---:|---|---:|---:|---:|---|"]
for r in ranked:
    table.append(f"| {r['rank']}{'=' if r['tied'] else ''} | {r['system']} | {fmt(r['total'])} | "
                 f"{r['total_percent']} | {r['fails']} | {r['adequacy_tier']} |")

V1 = "https://sites.google.com/view/normativeeconomicevaluation"
HUB = "https://bettertobest.github.io/research-hub/"
TEXT = f"""# NEEC: Normative Economic Evaluation Criteria

NEEC compares economic systems on one fixed set of normative criteria, so that systems as different as
Nordic social democracy, Georgism and state capitalism can be set side by side, with every score traceable
to stated evidence. Version 2 scores **{N} systems** on **26 criteria** in five domains: Material Security,
Human Autonomy, System Resilience, Ethical Integrity and Implementation Viability.

> **Status: version 2.0 in preparation.** This repository holds the v2 working corpus: the scores, the
> scoring documents, the scoring protocol, the first blind replication and the verification harness.
> Version 1 (12 systems, 25 criteria) is published on the [NEEC site]({V1}/home), with its
> [Paper]({V1}/paper) and [Report]({V1}/report). Paper v2.0 and Report v2.0 have not been generated yet:
> `NEEC_Paper_v1_4.md` and `NEEC_Report_v1_6.md` are the latest v1.x revisions, and their Part I does not
> yet include eight of the {N} systems.

## How a system is scored

Each criterion is scored 0, 0.5 or 1, and a 0 on any criterion counts as a **structural failure**. The
adequacy tier depends only on the number of structural failures, not on the total: 0 to 2 failures,
Potentially Adequate; 3 to 5, Partially Adequate; 6 or more, Structurally Inadequate. A higher total can
therefore sit in a lower tier: {short(HI['system'])} ({fmt(HI['total'])}/26, {HI['fails']} failures) outscores
{short(LO['system'])} ({fmt(LO['total'])}/26, {LO['fails']} failures) and sits {WORDS[gap]} tier{'s' if gap > 1 else ''} lower.

[`SCORING_PROTOCOL.md`](SCORING_PROTOCOL.md) (version {PROTOCOL_VERSION}{PROTOCOL_STATUS}) states how each
criterion is scored and what a scoring document must contain. Close calls are recorded rather than
smoothed over: each scoring document registers the scores a reasonable scorer could set differently, in
which direction, and what they would do to the total and the tier.

## Current scores (equal weighting)

{N} systems: {COUNTS[TIERS[0]]} Potentially Adequate, {COUNTS[TIERS[1]]} Partially Adequate,
{COUNTS[TIERS[2]]} Structurally Inadequate. Rank is the competition rank; `=` marks a tie.

""" + "\n".join(table) + f"""

Source: [`neec_scores.csv`](neec_scores.csv) (field definitions in
[`neec_scores_data_dictionary.md`](neec_scores_data_dictionary.md)); the score vectors are in
[`neec_corpus.json`](neec_corpus.json). Tiers do not depend on weights. How the ranking responds to three
alternative weighting schemes is computed by Appendix A.4's script,
[`run_a4_full_rerun_33.py`](run_a4_full_rerun_33.py).

These totals are provisional. A clause-by-clause audit of the scores of 1.0
([`NEEC_R4_MultiClause_Audit_s35.md`](NEEC_R4_MultiClause_Audit_s35.md), decision D28) found that most of
those resting on a multi-clause Pass Threshold do not yet show every clause cleared. They are re-estimated
in a rescoring pass before version 2.0, which can lower totals and ranks but, under that decision, cannot
change a failure count or a tier. The same pass applies two rules adopted with scoring protocol draft.5
(decisions D29 and D31: how implementation failures count, and what belongs to a scored mechanism), which
can turn a 0.5 into a structural failure; the two such cases identified so far, both in Ostrom-Style Commons
Governance, cannot change its tier, and the pass reports any failure count it changes.

## Disclosure

NEEC is written by Duke Johnson and Claude (Anthropic). Duke Johnson designed {TOP['system']}, one of the
scored systems (four of the five components of his Compassionism framework, scored as one system), and it
ranks first ({fmt(TOP['total'])}/26); Claude does the scoring and the engineering. The Paper addresses this self-referential concern in its
Section 10.5. The published protocol, the criterion-by-criterion evidence in the scoring documents, the
registers of contestable calls, and blind replication by scorers outside the project exist so that any
score can be checked and contested. The first blind replication (Ostrom-style commons governance) is
recorded in [`NEEC_OstromCommons_replication_record.md`](NEEC_OstromCommons_replication_record.md); the
next is planned for {TOP['system']} itself, with a replicator outside the Claude family.

## Reproducing every result

Requirements: Python 3.12 (standard library only) and, for three checks, Node.js.

```
python3 run_all_checks.py
```

This runs {N_CHECKS} checks. Each copies exactly the files one script needs into a fresh temporary
directory, runs the script there, and compares its output byte for byte with the captured copy in this
repository; negative controls confirm that the verifiers reject superseded states. The captured output of
the whole run is [`run_all_checks_output.txt`](run_all_checks_output.txt), and GitHub Actions repeats the
run on every push. Not covered: the prose of the Paper and the Report, and the fidelity of the Appendix G
JavaScript checks to the Compassionism Simulation's source. The repository keeps every file in one flat
directory because each check copies its inputs by name.

## What is here

- **Data.** `neec_scores.csv` (totals, domain scores, failures, tiers); `neec_corpus.json` (score vectors);
  `criteria.json` (the 26 criteria and their anchors), with `criteria_schema.json` and
  `summary_block_schema.json`.
- **Canonical scripts.** `neec_weighting_robustness_analysis_v2.py` (the score vectors, weighting schemes
  and dominance checks) and `neec_scores_csv_builder_v2.py` (which builds the CSV).
- **Scoring documents.** Ten systems have full scoring documents, `NEEC_<System>_scoring_scratch.md`; the
  thirteen earlier systems are scored in Paper v1.4 and carried onto the 26-criterion structure by
  `NEEC_Step1c_Retrofit_C1_2ab_C1_5.md`.
- **Protocol and contributing.** `SCORING_PROTOCOL.md`; [`NEEC_CONTRIBUTING.md`](NEEC_CONTRIBUTING.md).
- **Replication.** The issued blind kit (`replication_kit_OS_*`), the replicator's entry
  (`NEEC_OstromCommons_replication_scoring.md`), the record, and `compare_replication.py`.
- **Verification.** `run_all_checks.py` and the scripts it runs, each with its captured output
  (`*_output.txt`).
- **Pinned historical states.** `*_sNN_snapshot.*` files are byte-identical copies of files as they stood
  at session NN, so that each historical script runs against the corpus it was written for.
- **Working log.** `NEEC_Project_Handoff_NN.md`, one per working session.

## Contributing, citing, licence

Challenges to any score are welcome: open an issue naming the system, the criterion, the score you propose
and your evidence ([`NEEC_CONTRIBUTING.md`](NEEC_CONTRIBUTING.md) describes replication audits and the
scoring of new systems). To cite NEEC, use [`CITATION.cff`](CITATION.cff) ("Cite this repository" on
GitHub). Licensed under [CC BY 4.0](LICENSE).

Part of the [Better To Best Research Hub]({HUB}).
"""

with open(os.path.join(HERE, "README.md"), "w", encoding="utf-8", newline="\n") as f:
    f.write(TEXT)
print("README.md")
