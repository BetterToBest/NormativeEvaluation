# NEEC: Normative Economic Evaluation Criteria

NEEC compares economic systems on one fixed set of normative criteria, so that systems as different as
Nordic social democracy, Georgism and state capitalism can be set side by side, with every score traceable
to stated evidence. Version 2 scores **23 systems** on **26 criteria** in five domains: Material Security,
Human Autonomy, System Resilience, Ethical Integrity and Implementation Viability.

> **Status: version 2.0 in preparation.** This repository holds the v2 working corpus: the scores, the
> scoring documents, the scoring protocol, the first blind replication and the verification harness.
> Version 1 (12 systems, 25 criteria) is published on the [NEEC site](https://sites.google.com/view/normativeeconomicevaluation/home), with its
> [Paper](https://sites.google.com/view/normativeeconomicevaluation/paper) and [Report](https://sites.google.com/view/normativeeconomicevaluation/report). Paper v2.0 and Report v2.0 have not been generated yet:
> `NEEC_Paper_v1_4.md` and `NEEC_Report_v1_6.md` are the latest v1.x revisions, and their Part I does not
> yet include eight of the 23 systems.

## How a system is scored

Each criterion is scored 0, 0.5 or 1, and a 0 on any criterion counts as a **structural failure**. The
adequacy tier depends only on the number of structural failures, not on the total: 0 to 2 failures,
Potentially Adequate; 3 to 5, Partially Adequate; 6 or more, Structurally Inadequate. A higher total can
therefore sit in a lower tier: Universal Basic Income (14.5/26, 7 failures) outscores
Georgism / Land Value Tax (13.5/26, 2 failures) and sits two tiers lower.

[`SCORING_PROTOCOL.md`](SCORING_PROTOCOL.md) (version 2.0-draft.9) states how each
criterion is scored and what a scoring document must contain. Close calls are recorded rather than
smoothed over: each scoring document registers the scores a reasonable scorer could set differently, in
which direction, and what they would do to the total and the tier.

## Current scores (equal weighting)

23 systems: 6 Potentially Adequate, 8 Partially Adequate,
9 Structurally Inadequate. Rank is the competition rank; `=` marks a tie.

| Rank | System | Score (of 26) | Percent | Structural failures | Adequacy tier |
|---:|---|---:|---:|---:|---|
| 1 | CCO-PTF-CIP-SZH | 24.5 | 94% | 0 | Potentially Adequate |
| 2 | Participatory Economics | 20.5 | 79% | 1 | Potentially Adequate |
| 3= | Nordic Social Democracy | 19.5 | 75% | 2 | Potentially Adequate |
| 3= | Integral | 19.5 | 75% | 3 | Partially Adequate |
| 5 | Degrowth Economics | 19.0 | 73% | 2 | Potentially Adequate |
| 6 | Market Socialism | 16.5 | 63% | 2 | Potentially Adequate |
| 7 | MMT + Job Guarantee | 15.5 | 60% | 3 | Partially Adequate |
| 8= | Universal Basic Income | 14.5 | 56% | 7 | Structurally Inadequate |
| 8= | Mutual Credit / LETS | 14.5 | 56% | 3 | Partially Adequate |
| 8= | Ostrom-Style Commons Governance | 14.5 | 56% | 3 | Partially Adequate |
| 11= | Sovereign Wealth Fund Statism | 14.0 | 54% | 3 | Partially Adequate |
| 11= | State Capitalism / Singapore (GLC Developmental Capitalism) | 14.0 | 54% | 4 | Partially Adequate |
| 13= | Georgism / Land Value Tax (LVT + Citizen's Dividend) | 13.5 | 52% | 2 | Potentially Adequate |
| 13= | Universal Basic Services | 13.5 | 52% | 3 | Partially Adequate |
| 13= | Islamic Finance / Profit-Sharing Banking | 13.5 | 52% | 5 | Partially Adequate |
| 16 | Fully Automated Luxury Communism | 13.0 | 50% | 10 | Structurally Inadequate |
| 17 | Doughnut Economics | 11.5 | 44% | 8 | Structurally Inadequate |
| 18 | Status Quo Market Capitalism | 10.5 | 40% | 9 | Structurally Inadequate |
| 19= | Centrally Planned Socialism | 10.0 | 38% | 12 | Structurally Inadequate |
| 19= | Stakeholder Capitalism | 10.0 | 38% | 9 | Structurally Inadequate |
| 19= | State Capitalism / China (Party-State-Directed Market Economy) | 10.0 | 38% | 8 | Structurally Inadequate |
| 22 | State Capitalism / Qatar (Gulf Rentier-Distributive Statism) | 9.0 | 35% | 10 | Structurally Inadequate |
| 23 | Libertarian Minarchism | 8.0 | 31% | 15 | Structurally Inadequate |

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
Governance, cannot change its tier, and the pass reports any failure count it changes. The pass now also
applies the v2.0 criteria ([`NEEC_Criteria_v2_s45.md`](NEEC_Criteria_v2_s45.md)): 29 criteria, adding
Civil Liberties and Rule of Law, Productive and Innovative Capacity and Harm Internalization, with eight thresholds restated. Unlike D28, these can change failure counts
and tiers.

## Disclosure

NEEC is written by Duke Johnson and Claude (Anthropic). Duke Johnson designed CCO-PTF-CIP-SZH, one of the
scored systems (four of the five components of his Compassionism framework, scored as one system), and it
ranks first (24.5/26); Claude does the scoring and the engineering. The Paper addresses this self-referential concern in its
Section 10.5. The published protocol, the criterion-by-criterion evidence in the scoring documents, the
registers of contestable calls, and blind replication by scorers outside the project exist so that any
score can be checked and contested. The first blind replication (Ostrom-style commons governance) is
recorded in [`NEEC_OstromCommons_replication_record.md`](NEEC_OstromCommons_replication_record.md); the
next is planned for CCO-PTF-CIP-SZH itself, with a replicator outside the Claude family.

## Reproducing every result

Requirements: Python 3.12 (standard library only) and, for three checks, Node.js.

```
python3 run_all_checks.py
```

This runs 95 checks. Each copies exactly the files one script needs into a fresh temporary
directory, runs the script there, and compares its output byte for byte with the captured copy in this
repository; negative controls confirm that the verifiers reject superseded states. The captured output of
the whole run is [`run_all_checks_output.txt`](run_all_checks_output.txt), and GitHub Actions repeats the
run on every push. A finished working session reaches `main` only through
[`land-session.yml`](.github/workflows/land-session.yml), after every check passes on the merged tree. Not covered: the prose of the Paper and the Report, and the fidelity of the Appendix G
JavaScript checks to the Compassionism Simulation's source. The repository keeps every file in one flat
directory because each check copies its inputs by name.

## What is here

- **Data.** `neec_scores.csv` (totals, domain scores, failures, tiers); `neec_corpus.json` (score vectors);
  `criteria.json` (the v2.0 criteria, 29, with their clauses and anchors; the scores above use the 26 of
  Paper v1.4 until the rescoring pass is applied), with `criteria_schema.json` and
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

Part of the [Better To Best Research Hub](https://bettertobest.github.io/research-hub/).
