# NEEC Project Handoff 49

**Session 49 · 2026-09-25 · Owner: Duke Johnson · Scorer and engineer: Claude**
**Predecessor:** Handoff 48, whose sections 5–8 stand except where this handoff amends them.

> **Next session (50): Claude Code cloud, network access as in Session 49** (Full, or the evidence hosts listed in
> section 1). Then send `Continue NEEC.`

The session found the owner's site package, `NEEC_repository_s49.zip`, at the repository root, and applied it first,
as `CLAUDE.md` asks. **The public v2.0 site is now in the repository** (`build_site.py`, `site/`, `docs/`, six issue
forms, a new `.github/CONTRIBUTING.md`); it shows no scores until version 2.0's are final. Its ten decisions are
recorded as **49.1 to 49.10** (`NEEC_Criteria_v2_s45.md`). The site check is harness check 93, with a negative control,
check 94 (49.12). **One correction was needed to make it run here (49.11):** the package's `build_site.py` used Python
3.12-only syntax, and the cloud sessions run Python 3.11. It now runs on 3.10 to 3.13 with `docs/` unchanged. One
correction from the package's list was made (**49.13**, `llms.txt`). Then Handoff 48's task: **part (b)'s eighth group,
C4.3 and C4.5** (`NEEC_Rescoring_s49.md`, `rescoring_s49.py`, check 95). All seven C4.3 1.0s become 0.5, the owner's
design included (re-checked now as class M so that it is read as its peers are). On C4.5, FALC and Integral stand and
Degrowth becomes 0.5. Part (a)'s three C4.5 units stay 0.5. Net −4.0; no failure count or tier changes.
**CCO-PTF-CIP-SZH keeps first place at 18.0/26** after the pass so far (published 24.5). Eight D28 units remain.
Harness v24, **95 of 95**, byte-identical on a second run and under Python 3.12. No published score changed.

## 1. Session-start checks

`main` was at `2b23bf7`, the owner's upload of the package on top of tag `s48` (`5aed860`). `session_check.py --tag
s48 --files 284 --digest e137e7f3037da062e78b4ce0affa8be0 --handoff NEEC_Project_Handoff_48.md` gave the two failures
the upload explains ("s48 points at HEAD", and the digest), and passed the rest: tags s34–s48, the harness 92 of 92
byte-identical. The only difference between `s48` and `main` was the zip. Without it the tree is 283 files and its
digest is `e137e7f3…`, as Handoff 48 gives. **The latest Actions run on main failed:** run 1 of "pages build and
deployment" at `2b23bf7`. The owner had turned Pages on (branch `main`, folder `/docs`) before `docs/` existed, and the
build found no folder. The harness run on the same commit (run 66) passed. The landing of this session adds `docs/`
(with `.nojekyll`) and requests a Pages build. Simulation HEAD `11f9299` and Research Hub HEAD `1d74076` have moved
from the pins (`cd0ceec`, `8e8a6ba`); the pass reads the pins. Network: the Eurostat API, integralcollective.io,
raw.githubusercontent.com, github.com (the hub, read at its pin), roiw.org and api.crossref.org answered; annualreviews.org
returned a stub page (not needed).

## 2. What changed

- **The site package** (`NEEC_Site_Package_s49.md`, prepared in a claude.ai chat session at the owner's request from
  tag `s48`): applied as its section 4 says. 106 files added, 2 replaced, 2 deleted, the zip removed.
  `build_site.py --check` reported `site matches its sources: 77 files, scores not yet published` under Python 3.12
  before any change here.
- **Record** (`NEEC_Criteria_v2_s45.md`, amended in place; tag `s48` keeps its prior text): decisions **49.1 to 49.10**
  (the package's S1 to S10, attributed as it marks them), **49.11** (correction: `build_site.py` on Python 3.10+),
  **49.12** (polish: check 94), **49.13** (correction: `llms.txt`). Session 49 recomputed from the corpus and the CSV
  every figure 49.9 names (12 systems non-dominated on 26 criteria; CCO-PTF-CIP-SZH alone on the two-axis frontier;
  8 Partially Adequate, 6 Potentially Adequate; Nordic Social Democracy 19.5/26, 75%; C1.5 and C2.2 each failed by
  11 of 23), and confirmed 49.10's two links in `docs/`. The record's md5 is carried in `criteria.json`, so
  `criteria.json` and the footers of 64 `docs/` pages were regenerated. Nothing else in them changed.
- **`build_site.py`**: two attribute strings bound to names before their f-strings (49.11); output byte-identical.
- **`llms.txt`**: 29 criteria in `criteria.json` (the published scores on 26), protocol draft.9 (49.13).
- **Part (b), eighth group** (`NEEC_Rescoring_s49.md`, `rescoring_s49.py`, `rescoring_s49_output.txt`, new; cumulative
  with parts (a) to (b7) and 48.3). Readings, all under the delegation:
  - 3.2: C4.3's new declared-axis scope and household-income measure mean its A codes are re-read, not carried "as
    audited", following Session 48's correction.
  - 3.3: designs and mechanisms must project the gap.
  - 3.4: Nordic Social Democracy is short on its immigrant axis. Eurostat EU-SILC, by country of birth and by
    citizenship: in each of the four countries a gap above 20% falls by less than 5 points in five years, on
    three-year means and on the ten-edition trend.
  - 3.5: no Soviet series by nationality exists before 1988.
  - 3.6: C4.5's "genuine exit rights" means leaving a relationship without losing subsistence, through a floor or an
    assured alternative. FALC is cleared; Integral cleared and flagged toward 0.5; Degrowth not shown and flagged
    toward 1.0.
  - 3.7: part (a)'s C4.5 units re-read.
  - 3.8: CCO-PTF-CIP-SZH's C4.3, the one C4.3 1.0 outside D28, re-checked now as class M on the same readings. It
    falls, and **C4.3 joins the criteria no scored system clears, now nine**.

  The record's section 5 carries the updated score ledger (a column per part, (b8) included).
- **`run_all_checks.py` v24**: checks 93 (`build_site.py --check`, its line shown), 94 (negative control) and 95
  (`rescoring_s49.py`); a check's files may now name paths in subdirectories. The build capture is renamed
  `build_criteria_s49_output.txt`. **95 checks.** `README.md` regenerated (95 checks).

## 3. Files

The package's 106 new, 2 replaced and 2 deleted files (its section 3), and the session's own changes below. The zip is
deleted. 393 tracked files with this handoff.

| File | MD5 (first 8) | Status |
|---|---|---|
| `NEEC_Criteria_v2_s45.md` | `2b549947` | amended (49.1–49.13) |
| `criteria.json`, `SCORING_PROTOCOL.md` | `fd134dbd`, `dde8e834` | `criteria.json` regenerated (record md5 only); protocol unchanged |
| `build_criteria_s49_output.txt` | `fc451715` | renamed from `_s48_` and recaptured |
| `build_site.py` | `aaeff51b` | from the package; 49.11 |
| `docs/` (77 files) | — | from the package; 64 pages' footers regenerated |
| `NEEC_Site_Package_s49.md`, `NEEC_Site_Design_Brief_s45.md`, `site/config.json`, `.github/CONTRIBUTING.md` | `11bb4a33`, `f9015bce`, `252a63a3`, `ad18c891` | from the package, unchanged here |
| `build_site_check_output.txt`, `build_site_check_negative_output.txt` | `6abfe096`, `119a10e0` | new (checks 93, 94) |
| `llms.txt` | `d856a866` | 49.13 |
| `NEEC_Rescoring_s49.md`, `rescoring_s49.py`, `rescoring_s49_output.txt` | `4d9ec7ed`, `738f8b43`, `5bd45e56` | new |
| `run_all_checks.py`, `run_all_checks_output.txt` | `b293c33c`, `85f4fc25` | v24, recaptured |
| `README.md` | `00d85dbf` | regenerated |
| `NEEC_Project_Handoff_49.md` | (this file) | new |

## 4. Landing

The session's last commit, "NEEC Session 49: …", is pushed on `claude/vibrant-brown-ucux73`; `land-session.yml` merges
it into main, reruns every check (Python 3.12), tags `s49`, publishes the release and requests a Pages build. No owner
step. No workflow file needed a change.

## 5. Decision register

Protocol section 13 (D2–D31) unchanged; 45.1–45.7, 46.1–46.4, 47.1–47.2, 48.1–48.3 and 49.1–49.13 join it when the
pass ends. **For the owner, when convenient (nothing waits on any of them):**
- **49.3:** read the Thresholds page's 11 judgment-call paraphrases once (`site/thresholds.json`).
- **49.2, 49.5, 49.8, 49.9, flagged by the package:** the navigation; the AI prompt's design; the contributing routes
  and labels; the visual suite's adaptation. Under 49.9, v1's closing panel, "The Choice Before Humanity", is not
  carried over, because it is advocacy and the author's own design ranks first; it could live on the Research Hub
  instead.
- **Reading 3.8 of `NEEC_Rescoring_s49.md`:** your design's C4.3 was re-checked now, not in stage 2, so that it is read
  as its six peers are; it falls to 0.5. Its two flags are on other entries (Integral's C4.5 toward 0.5, Degrowth's
  toward 1.0).
- **48.3, flagged (from Handoff 48):** still open for your confirmation.

## 6. The owner's steps (one time; the package's section 6, updated)

1. **Pages is already on** (branch `main`, folder `/docs`): the failed build at `2b23bf7` shows it. The landing requests
   a build; the site should appear at https://bettertobest.github.io/NormativeEvaluation/ within minutes. If it does
   not, open **Settings → Pages** and confirm "Deploy from a branch", `main`, `/docs`.
2. Optional: **Settings → General → Features → Discussions**, then ask a session to set `site.discussions` to true in
   `site/config.json`.
3. Optional: **Issues → Labels → New label** for `evidence`, `push-back`, `ai-replication` and `criterion-proposal`.
4. Optional: add the new site's address to the Research Hub's NEEC entry.

## 7. Next session (50): start here

1. Run `python3 session_check.py --tag s49 --files 393 --digest 0ab437d7f99d2b1b4cc03fcecd4304f5 --handoff NEEC_Project_Handoff_49.md`
   and expect ALL PASS. If tag `s49` is missing, read the land-session run's log and repair that first. The latest
   Actions run on main may be a Pages build; if that run failed, read its log (the Jekyll step should find
   `docs/.nojekyll`) and record the cause.
2. **Check that the site is live** (`curl -sI https://bettertobest.github.io/NormativeEvaluation/`). If it is, record a
   decision pointing `CITATION.cff`'s `url` at it and adding it to `llms.txt` (package, section 5). If it is not,
   record that and leave both.
3. **Part (b), ninth and last group: C5.2** (4 units: NSD, LM, SC, IF), **C5.4** (2: NSD, CCO) and **C5.5** (2: PE,
   MC), in the form of `rescoring_s49.py`, cumulative with it. That finishes part (b).
4. If time remains, the class M re-checks. C4.3's other 16 units (thirteen 0.5s, three 0.0s) on readings 3.2 to 3.5,
   with the four other configured national economies (Status Quo, China, Singapore, Qatar) on national household
   survey series. Then C4.4's 17 units on 48.3, and C4.1's four part (b6) units (FALC, PE, INT, SWF) on its debt
   clause.

## 8. Plan to completion (amends Handoff 48, section 7)

Part (b) has one group left. Stage 2 (part (b), the class re-checks, and the 69 new units) is estimated at **sessions
50–52, possibly 53**. The later stages follow as before: stage 3, one session; Report and Paper v2.0, two; the PDF,
one. The site no longer needs two sessions of its own. It is built and gated: stage 3 sets `scores.publish` and names
the new summary-blocks file (package, section 7), and `build_site.py --check` keeps it equal to its sources at every
landing.

**Credit.** This session cannot see the Claude Code cloud credit balance; no tool available to it reports one. The
owner's cap for NEEC is $50. If the remaining sessions would exceed it, Handoff 47's narrowing of stage 2 stands as
the option.

## 9. Standing notes

- Handoff 48's standing notes stand.
- **Any change to the site's inputs needs `python3 build_site.py` before the harness.** The inputs are
  `criteria.json`, the corpus, the CSV, the summary blocks, `NEEC_Criteria_v2_s45.md`, Paper v1.4, the A.4 weighting
  script, the WJP extract, `.github/ISSUE_TEMPLATE/` and `site/`. Every amendment of the criteria record changes
  `criteria.json`'s `record_md5`, and so the footer of 64 `docs/` pages. The chain is: `build_criteria.py` (in a
  temporary directory with its four inputs), copy `criteria.json` and the capture back, `build_site.py`,
  `build_readme.py`, then the harness. Never edit `docs/` by hand; check 93 fails.
- The cloud container's `python3` is 3.11; the workflows use 3.12. The harness reproduces its capture on both.
- Sources read this session that are not in the repository, identified where a figure depends on them: Eurostat
  ilc_di16 and ilc_di15 (JSON md5 `2b786488`, `9f69c948`; every figure used is held in `rescoring_s49.py`); Alexeev and
  Gaddy (1993), Review of Income and Wealth 39(1) (PDF md5 `6e1b8367`); integralcollective.io's ITC page (md5
  `e5e589fa`); the Compassionism Simulation at `cd0ceec` (`harness.js` md5 `035d1be8`, `index.html` md5 `1c8273b1`); the
  Research Hub at `8e8a6ba`, searched with `git grep`; Paul, Darity and Hamilton (2018), as cited.
