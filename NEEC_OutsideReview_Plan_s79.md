# NEEC outside blind review: the plan (Session 79, decision 79.6)

**Status.** Plan only; nothing has been built or run. Sessions 80 to 82 carry it out (STATE.md, "Next work"; ledger S63 to
S64). It comes before the Report and Paper v2.0 prose, which now start at Session 83.

## 1. Why

Every NEEC score so far was produced and checked by Claude models, and Claude also wrote the Compassionism Simulation
and helped draft the Research Hub papers that CCO-PTF-CIP-SZH is scored on. The owner, who designed CCO-PTF-CIP-SZH and
co-authors NEEC, has made four decisions on its scores (58.1, 79.1 to 79.3) and one rule that reaches four other entries
(79.4). With them CCO-PTF-CIP-SZH is first at 17.5. On the readings alone it would be 15.5. An outside reader with no
stake, from outside the Claude family, reading blind, is the check a reader of the Paper will look for first.

## 2. Two instruments

| | Kimi K2.6 on Runpod (the reader) | Jev, TypeSafe (the interpretation check) |
|---|---|---|
| What it is | Open-weight reasoning LLM (Moonshot), Runpod public endpoint `moonshot-kimi`, validated Session 31 (`NEEC_Runpod_Replication_Harness.md`) | Fixed-option judge: returns an option, a probability per option and a confidence; piloted Session 50 (`NEEC_Jev_Pilot_Package_s50.md`), pinned `jev-1.13.0` |
| What it does here | Reads each unit blind from the criterion and the source pack, states each clause's status with an estimate and source, and the verdict by D28 | For each clause, with the source pack held fixed: cleared, short or not shown |
| Coverage | All 667 units, in priority order (section 4) | All 1,725 clauses of the 23 entries |
| Cost (est.) | About $0.04 to $0.08 a unit: $30 to $55 for all 667 at the Session 31 prices ($0.95/M input, $4.00/M output) | About $1 for every clause, twice ($0.042/M input) |
| Time (est.) | 1 to 3 minutes a unit; 4 at a time: about 2 hours for the priority set, 5 to 8 for all | Under an hour |

Two instruments that work differently guard against one model's quirks: Kimi tests the whole reading; Jev tests whether
the clause statuses follow from the evidence. Where both disagree with NEEC, the case is strong. Where they split, the
evidence is ambiguous, and that is a finding in its own right. If Runpod's public endpoints offer a stronger open-weight
model from another lab when Session 80 checks, a second LLM reader on the priority set is worth its cost. Session 31's
other model, Qwen3-32B, is weaker and costs more per token.

## 3. Blindness: what the reader sees and never sees

**Sees:** the protocol's scale and clause rule (sections 2.1 to 2.3), the criterion's v2.0 text with its clauses and
bands, the system's name and kind, and a **source pack** per unit:
- primary sources only: `evidence_cache/<criterion>/` extracts and data, the design's own public documents (for
  CCO-PTF-CIP-SZH, the Research Hub pages and the simulation's v5.6 release data and reports; for Integral, its white
  paper), and the cached series for the configured economies;
- for criteria with no cache directory (C1.2a, C1.2b, C1.3, C1.5, C2.2, C3.2, C3.3, C5.1 to C5.5), the design's own
  documents. For entries with no cacheable primary text (designs published as books), the reader answers from its own
  knowledge of the literature, labelled closed-book.
- **Optional:** `SEARCH:` and `FETCH:` through a search API key the owner provides, handled by the runner script, not by
  Claude.

**Never sees:** any NEEC score, verdict, clause status, reading, flag, close call, total, rank or tier; the v1
rationales (they are NEEC's earlier readings); `evidence/`, `docs/`, `STATE.md`, handoffs, rescoring, blind or owner
records; `sources_s*.md` notes in the cache, unless screened; the owner's authorship of the design (the Paper discloses
it).

**Checks before launch:** `outside_kit_check.py` scans the kit for verdict words and score patterns next to criterion
ids, tier names, record names, "close call", "flag", and withheld-target markers. The Ostrom pilot leaked through a
marker like this (`NEEC_OstromCommons_replication_record.md`). Any hit fails the harness. **No Claude session is in the
loop while it runs:** the runner answers `READ:` and `SEARCH:` mechanically, which removes the relay problem
`NEEC_Runpod_Replication_Harness.md` (D25) raised.

## 4. Order of work (priority, so an early stop loses the least)

1. The 29 CCO-PTF-CIP-SZH units.
2. The other four of the top five: Participatory Economics, Integral, Nordic Social Democracy, Degrowth Economics (116
   units), which together decide first place.
3. Every other unit carrying a close call (135).
4. Everything else (387): the calibration set. It measures the reader's general lean (generous or strict against NEEC),
   against which its CCO-PTF-CIP-SZH readings are judged.
5. **Stage B (not blind, labelled so):** for the eight units with an owner decision (C3.2 and the seven of Session 79),
   after the blind reading is stored and pushed, the reader is shown the owner's argument (the decision text) and asked
   whether it changes its reading. It is recorded separately.

The 29 CCO-PTF-CIP-SZH units run twice, to measure the reader's own consistency.

## 5. Running it (Runpod, auto-push every 20 minutes)

As with the simulation's long studies, the work runs unattended on a Runpod **CPU pod** (the model is a public endpoint;
the pod only runs the loop) and pushes its results to `BetterToBest/compassionism-sim-results`, folder
`neec-outside-review/<run id>/`, so a lost pod loses at most 20 minutes.

- `outside_review_runner.py` (standard library only): reads `kit/units.jsonl` in priority order, runs 4 units at a time,
  answers `READ:` from the kit, validates each `FINAL:` against a JSON schema (one status, estimate and source per
  clause, the verdict, D28), retries an invalid answer twice, and appends to `results/kimi.jsonl`. It records model id,
  sampling settings, tokens and cost per call. The Jev pass appends to `results/jev.jsonl`.
- **Resumable:** a restart skips every unit already in the results.
- **Pusher:** every 20 minutes and at the end it commits and pushes `results/` and a `heartbeat.json` (units done, cost,
  last error), so progress shows on GitHub from the Chromebook.
- **Budget guard:** stops at a ceiling the owner sets (suggested $60).
- **Stops billing:** at the end it pushes, then stops its own pod (`runpodctl stop pod $RUNPOD_POD_ID`).
- **Secrets, set by the owner as Runpod pod secrets, never committed:** `RUNPOD_API_KEY` (endpoint calls),
  `TYPESAFE_API_KEY` (Jev; or the Composio route of the Session 50 pilot), `GITHUB_TOKEN` (write to the results repo
  only; the simulation studies' token if it has that scope), optional `SEARCH_API_KEY`.
- **Fallback:** the same script runs as a GitHub Actions job in the results repo (up to 6 hours a job, free on a public
  repository), if a pod is inconvenient.

## 6. Pre-registered comparison (committed in Session 80, before the run)

- A unit **agrees** when the verdict matches; clause agreement is reported alongside it. For CCO-PTF-CIP-SZH, the
  reader's lean measured on the calibration set is reported with its agreement rate.
- Every disagreement is adjudicated on the sources by an Opus session, by the same rule for every entry. Changes go in
  by generator. Changes to CCO-PTF-CIP-SZH go to the owner (decision 57.2).
- **Whatever the owner decides, the Report and Paper publish the outside review's result for every CCO-PTF-CIP-SZH unit
  and every owner-decided unit, up or down.** Decision 69.4 holds falls back from the scores for the site's push-back
  feature, but it does not keep them out of the record.
- The standing is published three ways: NEEC's scores, NEEC's scores without owner decisions, and the outside
  reader's.

## 7. Sessions

| Session | Work | Model and effort | Why |
|---|---|---|---|
| 80 | Build the kit and source packs, `outside_kit_check.py` (in the harness), the runner, the schema and the pre-registered rules; dry run on 3 non-CCO units; launch, or hand the owner a one-line launch | **Opus 5.5 at high** | The blindness design is judgment work (the Ostrom pilot leaked); the runner is routine |
| (run) | Unattended on Runpod, 2 to 8 hours | none | No Claude in the loop |
| 81 | Pull the results; `compare_outside.py`: agreement tables, the reader's lean, Jev against Kimi against NEEC, stage B; the record | **Sonnet 5.5 at medium** | Mechanical |
| 82 | Adjudicate the disagreements on the sources; generator for any change; owner items to the ledger | **Opus 5.5 at xhigh** for CCO-PTF-CIP-SZH and the top five, high for the rest | Contested readings that decide first place |

Session 80 needs, from the owner: the Runpod connector attached to the session (this session had none) or a
`RUNPOD_API_KEY` environment secret; network access to `api.runpod.ai` and `bettertobest.github.io` (checked here: the
container reaches `api.runpod.ai`); and the secrets above set on the pod.
