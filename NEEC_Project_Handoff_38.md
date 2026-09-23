# NEEC Project Handoff 38

**Session 38 · 2026-09-22 · Owner: Duke Johnson · Scorer and engineer: Claude**
**Predecessor:** Handoff 37 (in the Project and the repository). This handoff supersedes its sections 6–11.

Session 38 verified the Session 37 repository and did the first group of part (b) of the rescoring pass (Handoff
37, section 8 item 3): **the 29 part (b) units on the five criteria whose clause readings part (a) fixed** (C3.4,
C5.3, C2.4, C1.3, C2.3), re-estimated clause by clause on cited evidence. **Two stand; 27 become 0.5 (13.5
points); no failure count or tier changes.** Nothing is applied yet: the record is scratch, and the corpus, CSV and
scoring documents change only when the pass ends (protocol 10.1–10.3). The harness is at version 13, **81 of 81
checks passing**, byte-identical on a second run.

---

## 1. Session-start checks

- **Repository.** `main` at `1cf2c14` (the merge of pull request #4): 226 tracked files, all mode 100644; digest
  `53fd3c82875610d5d3fa8d38d7f168e8` (exact match); harness v12 ran 80 of 80, byte-identical to its capture.
  Handoff 37 in the repository is byte-identical with the Project's copy.
- **Tags.** `s34` to `s37` exist; `s37` → `1cf2c14`. Handoff 37's section 6 is complete.
- **Actions.** Run 18 on `main` completed successfully (the REST API was rate-limited; the Actions page was read
  over HTTPS).
- **Attachments.** The seven CSV files attached to the opening message arrived empty again; the repository copies
  were used.

## 2. What changed

### 2.1 The rescoring pass, part (b), first group (`NEEC_Rescoring_s38.md`, `rescoring_s38.py`)

- **Stand (2):** Market Socialism C3.4 (Mondragon's pay-ratio cap moved 1:3 → 1:4.5 → 1:6 by General Assembly
  votes; a stated search found no collapse caused by an adjustment, Fagor's 2013 failure being attributed to the
  euro-area and Spanish housing crises and acquisition debt) and Universal Basic Services C5.3 (Quebec's childcare
  expanded market activity; Canada-wide childcare agreements with every province and territory are a coordination
  protocol), **flagged with 0.5** because the protocols cover one sector.
- **Become 0.5 (27):** among them Nordic Social Democracy's C3.4 (the 1980s liberalisation led to systemic banking
  crises) and C1.3 (housing cost overburden among the EU's highest in Denmark and Sweden); UBI's C3.4 (Alaska's
  dividend set on an annual cycle); and every design unit on C2.3 and C2.4 (no estimate of the outcome levels).
- **CCO-PTF-CIP-SZH:** C2.3, C2.4 and C3.4 fall (C3.4 flagged with 1.0); it keeps first place, 24.0 → 22.5.
- **Cumulatively with part (a):** 62 units re-estimated, 4 stand, 58 become 0.5 (29.0 points). Dominance pairs 15 →
  14; frontier 11 → 13 (Market Socialism and Sovereign Wealth Fund Statism join). 72 D28 units remain, plus C5.1's
  second clause on eleven 1.0s.

### 2.2 Decisions under the delegation (record, section 3)

- **3.1** C3.4 clause 4 for a design without an implementation record: shown only by modelling adjustments during
  operation, in a model able to represent a way an adjustment could cause a collapse.
- **3.2** A design's published model may be run by the scorer: pinned to commit and digest, engine unchanged,
  documented reference run reproduced first, script and output kept in the repository, modelling tier (4.1).
- **3.3** C5.3 clause 4: moot only where the entry's text establishes coordination is unneeded; intergovernmental
  agreements coordinating a component count as protocols.
- **3.4** C5.3 clause 3 is a method clause: observed scaling to national scale clears it; regional or city-state
  scale does not.
- **3.5** Outcome clauses of C2.3 and C2.4 for designs: an institution specified, or a relative increase projected,
  is not an estimate of the level.
- **3.6** CCO C5.3 raised and resolved: the simulation's 55% "minimum viable" figure is a warning only; the engine at
  30% participation keeps wealth poverty below baseline in 100 of 100 seeds. The unit stays at 1.0.
- **3.7** MMT C2.4 stays out of reach (D31).

### 2.3 Corrections found (not polish; record, section 7)

1. Handoff 37's per-criterion counts for part (b) were wrong (C3.4 10, C5.3 6, C1.3 1, not 11, 8, 3).
2. Integral's C2.3 compares itself with an unsourced range (part (a), correction 3).
3. For the simulation's maintainers: three documents describe a 55% participation collapse the engine does not
   implement. The owner decides whether to build it into the dynamics or relabel it.

### 2.4 Other files

- `cco_simulation_checks_s38.js` and its output: two runs of the Compassionism Simulation's own engine
  (`harness.js` at `compassionism-simulation` commit `cd0ceec`, v4.15, md5 `035d1be8…`).
- `run_all_checks.py` v13 adds check 81; `README.md` regenerated (only the check count changes).

## 3. Files

The repository update is **9 files** at the zip's top level, `NEEC_repository_s38.zip`:

| File | MD5 (first 8) | Status |
|---|---|---|
| `NEEC_Rescoring_s38.md` | `bdb31f46` | new (the pass's record, part (b), first group) |
| `rescoring_s38.py` | `b63f325c` | new |
| `rescoring_s38_output.txt` | `b586586d` | new |
| `cco_simulation_checks_s38.js` | `8f15a713` | new |
| `cco_simulation_checks_s38_output.txt` | `cd9b30d3` | new |
| `NEEC_Project_Handoff_38.md` | (this file) | new |
| `run_all_checks.py` | `a8e6ccac` | replaced (v13) |
| `run_all_checks_output.txt` | `ae8fea22` | replaced |
| `README.md` | `79933652` | replaced |

**The Project** gets this handoff only (GitHub is canonical, D27(b)).

## 4. Pins

- `rescoring_s38.py` reads the corpus in force, the R4 audit's register and part (a)'s units (it imports
  `rescoring_s37.py`). When the pass is applied, its consequence figures and the record's tables need a successor
  or a pinned corpus snapshot, as for `rescoring_s37.py`.
- `cco_simulation_checks_s38_output.txt` is pinned by the engine's digest; the JavaScript is not rerun by the harness
  because the simulation's source is not in this repository. To rerun: clone `BetterToBest/compassionism-simulation`,
  check out `cd0ceec`, and run `node cco_simulation_checks_s38.js path/to/harness.js`.
- Unchanged: Handoff 37 section 4's pins.

## 5. Decision register

The protocol's section 13 (D2–D31) is unchanged. The decisions of section 2.2 are recorded in the rescoring record
and join the protocol's register when the pass ends and the protocol is restated. Nothing awaits the owner except
the simulation note in 2.3(3), which is his project's choice.

## 6. Updating the repository (owner)

1. **Upload the zip**: on the repository page, **Add file → Upload files**, drop in `NEEC_repository_s38.zip`,
   **Commit changes** (to `main`).
2. **Paste to Claude Code:**

```
Session 38 update. NEEC_repository_s38.zip is now on main. Please:
1. Pull main and create a new branch from it.
2. Unzip NEEC_repository_s38.zip into the repository root, overwriting (9 files: 6 new, 3 replaced), then delete the zip and stage everything (git add -A).
3. Confirm git ls-files shows 232 files.
4. Run: python3 run_all_checks.py > /tmp/out.txt ; cmp /tmp/out.txt run_all_checks_output.txt
   Expect "SUMMARY: 81 passed, 0 failed, 0 skipped (of 81)." and cmp reporting no difference.
5. Run the fingerprint snippet in section 7 of NEEC_Project_Handoff_38.md; expect 7494437a882501ee806748bb618fe697.
6. Commit "NEEC Session 38: rescoring pass part (b), first group, C3.4 C5.3 C2.4 C1.3 C2.3 (harness v13)", push, open a pull request into main, and merge it with a merge commit if you are able to (otherwise tell me).
7. Tag the merge commit s38 and push it (git push origin s38), then run git ls-remote --tags origin and show me the result. If pushing the tag is refused, say so plainly.
8. Confirm the harness workflow passed on main.
```

3. **If Claude Code cannot push the tag**, create it on GitHub:
   - Go to **Releases → Draft a new release → Choose a tag**, type `s38`, and click **Create new tag: s38 on publish**.
   - Under **Target → Recent commits**, pick the Session 38 merge commit.
   - Title it `s38` and click **Publish release**.
4. **Add this handoff to the Project.**

## 7. Next session: start here

1. **Clone:** `git clone https://github.com/BetterToBest/NormativeEvaluation /home/claude/neec`.
2. **Verify:**
   - Tags `s34` to `s38` exist.
   - 232 tracked files.
   - The digest below, over every tracked file except this handoff, equals `7494437a882501ee806748bb618fe697`.
   - Harness v13 runs 81 of 81, byte-identical to `run_all_checks_output.txt`.
   - The latest Actions run on `main` passed.

   If the Session 38 update has not been applied, ask the owner to finish section 6 first (the zip is in the
   Session 38 conversation).

```
import hashlib, subprocess
h = hashlib.md5()
for f in sorted(x for x in subprocess.check_output(["git", "ls-files"]).decode().split("\n") if x):
    if f != "NEEC_Project_Handoff_38.md":
        h.update(f.encode() + b"\0" + hashlib.md5(open(f, "rb").read()).digest())
print(h.hexdigest())
```

3. **Then** section 8, item 3.

## 8. Next steps, in priority order

1. **Owner:** section 6.
2. **Next session:** verify (section 7).
3. **The rescoring pass, part (b), continued**, as a new record part with its own script (for example
   `NEEC_Rescoring_s39.md`, importing parts (a) and (b1) for cumulative consequences):
   - C5.1's second clause on its eleven 1.0s outside D28's population (NSD, MS, UBI, CCO, MC, UBS, SWF, CN, SG, QA,
     OS), on part (a)'s reading 3.4: documented outcomes against the benefits the entry's own sources claim.
   - C3.1 (5 units: MMT, UBI, DG, PE, INT), deciding the step-versus-scaling question by protocol 4.2.
   - Then the other 67 D28 units, criterion by criterion (the record's section 6 lists them: C1.1 9, C2.5 10, C4.1 8
     and C4.2 6 are the largest).
   - Hold designs' modelled figures to protocol 4.1 and apply readings 3.1–3.5 alike.
4. **Parts (c)–(e)**, then apply the whole pass by generator, as in Handoff 37, section 8 item 4 (pin the corpus,
   regenerate the corpus, CSV, README and Appendix A.4, recompute the changed flag registers, restate the protocol's
   corpus statements, and give the claims and protocol verifiers and both rescoring scripts successors).
5. **Step 5 → Report v2.0 and Paper v2.0**, as Handoff 36 section 8 item 4 describes, now also covering the
   corrections of both rescoring records.
6. **Pages site and Hub**; **second pilot**; **git tags and Visual Suite v3**, as in Handoff 36, section 8, items 5–7.

## 9. Known limitations (stated, not hidden)

1. This group is one scorer's re-estimation on evidence located in one session. "Not shown" means no evidence was
   located, not that the clause fails. Two units are flagged in the direction a careful second scorer could take.
2. **Reopening conditions.** Nordic Social Democracy's C2.3 (Eurostat still unreachable; a fetch returned the site's
   main page). CCO-PTF-CIP-SZH's C3.4 (reopens if the simulation adds an endogenous price or behavioural channel and
   the adjustment run is repeated).
3. **The simulation runs are pinned, not rerun by the harness** (section 4). The simulation is being calibrated and
   updated, so later versions may reopen CCO units; that is expected, not a defect.
4. Handoff 37's limitations 3–4 stand.

## 10. Hub text

Unchanged from Handoff 37, section 10.

## 11. Standing working notes

- Shell is `sh` (no `time`, no process substitution); `git` and Node are available. Maximum effort; accuracy over
  speed.
- `github.com` and `raw.githubusercontent.com` are reachable from the sandbox. The web-fetch tool opens only URLs
  returned by a search. `bettertobest.github.io`, `ec.europa.eu` and `db.nomics.world` are not reachable from bash,
  so read the Hub's sources by cloning `BetterToBest/research-hub` and the simulation by cloning
  `BetterToBest/compassionism-simulation`; its `harness.js` is the engine to run (its CONTRIBUTING.md records parity
  with `index.html`).
- Scratch before insert; programmatic verification over visual checking; generate, don't transcribe. Scripts find
  inputs beside themselves, print file names only, and are deterministic.
- Decisions are Claude's under the delegation. Record them with reasons, flag substantive changes, distinguish
  corrections from optional polish, say plainly when a file does not exist, and prefer precise, defensible
  language.
- Give the owner click-by-click steps for anything in GitHub. If the chat disconnects, the owner refreshes; a
  completed reply will be there, and "continue" resumes otherwise.
