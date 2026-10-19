# NEEC outside blind review: the plan (Session 79, decision 79.6)

**Status.** Plan only (revised the same day for free tiers, decision 79.8); nothing has been built or run. Sessions 80 to 82 carry it out (STATE.md, "Next work"; ledger S63 to
S64). It comes before the Report and Paper v2.0 prose, which now start at Session 83.

## 1. Why

Every NEEC score so far was produced and checked by Claude models, and Claude also wrote the Compassionism Simulation
and helped draft the Research Hub papers that CCO-PTF-CIP-SZH is scored on. The owner, who designed CCO-PTF-CIP-SZH and
co-authors NEEC, has made four decisions on its scores (58.1, 79.1 to 79.3) and one rule that reaches four other entries
(79.4). With them CCO-PTF-CIP-SZH is first at 17.5. On the readings alone it would be 15.5. An outside reader with no
stake, from outside the Claude family, reading blind, is the check a reader of the Paper will look for first.

## 2. Two instruments, at near-zero cost (decision 79.8)

The owner ruled out the cost on 2026-10-19: paid inference on Runpod (about $30 to $55) is too high. The review keeps
both instruments and runs on free tiers, taking days instead of hours.

| | A free-tier reasoning model (the reader) | Jev, TypeSafe (the interpretation check) |
|---|---|---|
| What it is | An open or hosted model from outside the Claude family on a free API tier: GitHub Models (the owner's GitHub account), Google's Gemini API, Groq or OpenRouter's free models. Session 80 confirms each tier's current limits and model list, picks the strongest model whose daily limit can carry the run, and pins it | Fixed-option judge (option, probabilities, confidence); piloted Session 50, pinned `jev-1.13.0` |
| What it does here | Reads each unit blind from the criterion and the source pack, states each clause's status with an estimate and source, and the verdict by D28 | For each clause, with the source pack held fixed: cleared, short or not shown |
| Coverage | All 667 units, in priority order (section 4); the order means an early stop still covers CCO-PTF-CIP-SZH and the top five | All 1,725 clauses of the 23 entries, twice |
| Cost | Free (within the tier's limits) | About $1 |
| Time | Set by the daily limits: likely several days for all 667, the priority units first | Under an hour |

Free tiers may use inputs for training; every input here is already public under CC BY 4.0. One model is used for the
whole run, so the lean measured on the calibration set applies to its CCO readings. A second free model may read the 29
CCO units as an inter-rater check if a tier allows it.

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

## 5. Running it (a scheduled GitHub Actions job, pushing every run)

The run lives in `BetterToBest/compassionism-sim-results`, folder `neec-outside-review/<run id>/`, as a scheduled GitHub
Actions workflow (free on a public repository; no pod to stop). Each run reads as many units as the day's limit allows,
commits and pushes, and stops; the next picks up where it left off.

- `outside_review_runner.py` (standard library only): reads `kit/units.jsonl` in priority order, skips every unit already
  in the results, answers `READ:` from the kit, validates each `FINAL:` against a JSON schema (one status, estimate and
  source per clause, the verdict, D28), retries an invalid answer twice, and appends to `results/reader.jsonl`. It records
  model id, sampling settings and tokens per call. The Jev pass appends to `results/jev.jsonl`.
- **Rate limits:** the runner reads the provider's limit headers and stops cleanly before the daily cap. Each run also
  stops after about 50 minutes, committing what it has. Pushing every run (and every 20 minutes within a run) means a
  failed run loses at most one batch.
- **Progress:** `heartbeat.json` (units done, by priority group, last error) is visible on GitHub from the Chromebook.
- **Schedule:** every few hours, set from the tier's limits; the job disables its own schedule when every unit is done.
- **Secrets, set by the owner as repository secrets, never committed:** the free tier's key (`GITHUB_TOKEN`'s built-in
  models permission for GitHub Models, or `GEMINI_API_KEY`, `GROQ_API_KEY`, `OPENROUTER_API_KEY`), and
  `TYPESAFE_API_KEY` for Jev (or the Composio route of the Session 50 pilot).
- **The workflow file** is in the results repository, not in NormativeEvaluation, so this repository's rule on workflow
  files is not touched; the owner adds it there (or approves it in review) as with the simulation's study workflows.

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
| (run) | Unattended on GitHub Actions over several days | none | No Claude in the loop |
| 81 | Pull the results; `compare_outside.py`: agreement tables, the reader's lean, Jev against the reader against NEEC, stage B; the record | **Sonnet 5.5 at medium** | Mechanical |
| 82 | Adjudicate the disagreements on the sources; generator for any change; owner items to the ledger | **Opus 5.5 at xhigh** for CCO-PTF-CIP-SZH and the top five, high for the rest | Contested readings that decide first place |

Session 80 needs, from the owner (ledger S66): a free-tier API key set as a secret in `compassionism-sim-results` (or
GitHub Models enabled for it), the TypeSafe key for Jev, and network access for the session to the chosen provider and
`bettertobest.github.io` (to cache the Research Hub pages).
