# NEEC Project Handoff 66

> **Next session (67): Opus 5.5 at high effort.** Task: Report v2.0 and Paper v2.0 (stage 4), judgment prose from the per-unit
> tables in the rescoring records. Reason: the scores are live, so the prose is what remains and it needs judgment.

## 1. What changed (Session 66, a short publish session)

The owner asked for the v2.0 scores to go live with the provisional notice (decision 66.1, the owner's go on d49; optional in
scope, delegated by the owner's message). Done as Handoff 65, section 4 set out:

- `site/config.json`: `scores.publish` true; `corpus`, `csv`, `summary_blocks` point at `neec_corpus_v2.json`,
  `neec_scores_v2.csv`, `summary_blocks_v2.json`; new `scores.provisional_note` setting.
- `build_site.py`: when the gate is true and `provisional_note` is set, every page prints it in the existing banner style.
  The preview banner is unchanged.
- `docs/` rebuilt (61 pages, scores published); `build_site_check_output.txt` regenerated.
- `run_all_checks.py`: the site check's file list now names the three v2 files. Harness: 112 of 112, byte-identical.

The banner reads: "Provisional scores. These version 2.0 scores come from a rescoring pass still in progress: Report v2.0 and
Paper v2.0 are not yet written, and some readings are open to challenge (see the Contribute page). Totals may change before release."
When Report and Paper v2.0 land, remove `provisional_note` from `site/config.json` and rebuild.

The site goes live when the owner merges the pull request (`land-session.yml` requests the Pages build). No ledger entry was
written in this session (artifact tools not used); d49 should be marked answered "publish" by the owner or the next session.

## 2. Files

`site/config.json`, `build_site.py`, `run_all_checks.py`, `build_site_check_output.txt`, `run_all_checks_output.txt`, `docs/*`.

## 3. Next session (67): start here

1. `session_check.py` per Handoff 63's method; read the ledger for d38, d42 to d49 and record the answers.
2. Report v2.0 and Paper v2.0 (STATE.md, Next work 2), then remove the provisional note, rebuild, commit `docs/`.
3. The PDF (stage 5, Sonnet 5.5) and the open items in STATE.md.
