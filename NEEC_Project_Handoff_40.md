# NEEC Project Handoff 40

**Session 40 · 2026-09-23 · Owner: Duke Johnson · Scorer and engineer: Claude**
**Predecessor:** Handoff 39 (in the Project and the repository). This handoff supersedes its sections 6–11.

Session 40 verified the Session 39 repository and did the third group of part (b) of the rescoring pass (Handoff 39,
section 8 item 3): **C1.1's nine part (b) units**, whose stress clause (≥85% under stress testing) the audit coded
silent on every one, re-estimated clause by clause on cited evidence, with **CCO-PTF-CIP-SZH's base clause tested
against the design's own published model.** **None stands; all nine become 0.5 (4.5 points); no failure count or
tier changes. After this group no entry scores 1.0 on C1.1.** Nothing is applied yet: the record is scratch, and the
corpus, CSV and scoring documents change only when the pass ends (protocol 10.1–10.3). The harness is at version 15,
**83 of 83 checks passing**, byte-identical on a second run.

---

## 1. Session-start checks

- **Repository.** `main` at `94a1e8e` (the merge of pull request #6): 236 tracked files, all mode 100644; digest
  `d5985aa1dd94f95f7a108cdc9d51c52e` (exact match); harness v14 ran 82 of 82, byte-identical to its capture.
  Handoff 39 in the repository is byte-identical with the Project's copy.
- **Tags.** `s34` to `s39` exist; `s39` → `94a1e8e`. Handoff 39's section 6 is complete.
- **Actions.** Run 29 on `main` (the merge of pull request #6) completed successfully (the REST API was rate-limited;
  the Actions page was read over HTTPS).
- **Simulation.** `BetterToBest/compassionism-simulation` HEAD is still `cd0ceec` (v4.15); `harness.js` md5
  `035d1be8…` unchanged. v4.16 is in development and not yet pushed.
- **Attachments.** The seven CSV files attached to the opening message arrived empty again; the repository copies
  were used.

## 2. What changed

### 2.1 The rescoring pass, part (b), third group (`NEEC_Rescoring_s40.md`, `rescoring_s40.py`)

- **Short (2):** Centrally Planned Socialism's stress clause (Cuba's Special Period: daily energy intake 2,899 →
  1,863 kcal, a neuropathy outbreak of about 50,000 cases in 1992–93, infant mortality's decline reversed); and
  CCO-PTF-CIP-SZH on both clauses (below).
- **Not shown (7):** Nordic Social Democracy (Finland's 1991–93 depression: relative poverty fell slightly while
  social-assistance receipt doubled and poverty rose in real terms), **flagged toward 1.0** on the relative-measure
  reading; Market Socialism (Fagor's 2013 failure: member protections reached the 1,898 members, not the
  subsidiaries' employees; no poverty figure under stress); and the five designs without a stress estimate (MMT + Job
  Guarantee, UBI, Degrowth, FALC, Participatory Economics).
- **CCO-PTF-CIP-SZH:** the rationale's 98% is the stated outcome of the design's parameter file (research hub,
  `data/optimal-parameters.json`, v1.0.0, 2025-09-18) for a Basic Unit of $1,200, octave 6, 78% participation and 20%
  PTH uptake, which are the simulation's own reference settings. Run there on the pinned engine for 20 years and 100
  seeds, it reduces wealth poverty by 78.5% and BLEI poverty by 82.1% against the paired Baseline (no seed reaches
  90%); under the engine's adverse channels at the same settings, by 56.4% and 60.0%; under its own Stress Test preset,
  by 31.0% and 32.6%. **Flagged toward 1.0** on the papers' modelled figures. It keeps first place, 22.0 → 21.5.
- **Cumulatively with parts (a), (b1) and (b2):** 87 units re-estimated, 6 stand, 81 become 0.5 (40.5 points).
  Dominance pairs 18 → 18; frontier 12 → 12. 58 D28 units remain.

### 2.2 Decisions under the delegation (record, section 3)

- **3.1** C1.1 clause 2 requires an estimate under an adverse scenario at the entry's tier; a mechanism specified to
  operate in a downturn is not one (protocol 2.1's "untested conditions" is 0.5; part (b1)'s reading 3.5).
- **3.2** C1.1's measure is absolute poverty against a basket; where a stress record's relative and absolute
  indicators diverge, the absolute ones govern.
- **3.3** For CCO-PTF-CIP-SZH's base clause, the design's published, reproducible model governs over the papers'
  figure, whose model is not published in runnable form; the engine's two headcounts are read as its nearest
  measures, against its paired Baseline (the reading more favourable to the design).
- **3.4** The stress run: the engine's adverse channels at the reference settings, paired as `index.html` pairs them,
  plus its shipped Stress Test preset; the two recession functions appended verbatim from `index.html` at `cd0ceec`.
- **3.5** **No entry now scores 1.0 on C1.1.** When the pass is applied, C1.1's 1.0 band keeps its description and
  drops its example (the schema allows a band with none); a hypothetical example is rejected.

### 2.3 Corrections found (not polish; record, section 6)

1. Report v1.6's Nordic Social Democracy C1.1 "94-96% poverty elimination": unsourced, measure unstated; it is also
   C1.1's 1.0 anchor example.
2. Report v1.6's CCO-PTF-CIP-SZH C1.1 "98% poverty elimination in modeling": the design's published model, at the
   settings its own parameter file credits with 98%, gives 78.5% and 82.1%.
3. **A sixth anchor example moves** (C1.1's 1.0, Nordic Social Democracy), and it is the first band left with no corpus
   unit at its value (decision 3.5).
4. **A finding the v2.0 documents must state:** no scored system now clears C1.1, because no rationale in the corpus
   estimated poverty under stress.

### 2.4 Other files

- `cco_simulation_checks_s40.js` and its output: runs of the Compassionism Simulation's own engine (`harness.js` and
  `index.html` at `cd0ceec`, both pinned by digest), reproducing the seed-42 regression and Session 38's run 1 first.
- `run_all_checks.py` v15 adds check 83; `README.md` regenerated (only the check count changes).

## 3. Files

The repository update is **9 files** at the zip's top level, `NEEC_repository_s40.zip`:

| File | MD5 (first 8) | Status |
|---|---|---|
| `NEEC_Rescoring_s40.md` | `eea155ae` | new (the pass's record, part (b), third group) |
| `rescoring_s40.py` | `f0a286f7` | new |
| `rescoring_s40_output.txt` | `62fccbf3` | new |
| `cco_simulation_checks_s40.js` | `5a7ad514` | new |
| `cco_simulation_checks_s40_output.txt` | `175adc3c` | new |
| `NEEC_Project_Handoff_40.md` | (this file) | new |
| `run_all_checks.py` | `68f861ee` | replaced (v15) |
| `run_all_checks_output.txt` | `13b73e36` | replaced |
| `README.md` | `8333ac08` | replaced |

**The Project** gets this handoff only (GitHub is canonical, D27(b)). See section 11 for trimming the Project.

## 4. Pins

- `rescoring_s40.py` imports `rescoring_s37.py`, `rescoring_s38.py` and `rescoring_s39.py` and reads the corpus in
  force. When the pass is applied, its consequence figures and the record's tables need a successor or a pinned corpus
  snapshot, as for the three earlier scripts.
- `cco_simulation_checks_s40_output.txt` is pinned by two digests (`harness.js` `035d1be8…`, `index.html`
  `1c8273b1…`); the harness checks them but does not rerun the JavaScript. To rerun: clone
  `BetterToBest/compassionism-simulation`, check out `cd0ceec`, and run
  `node cco_simulation_checks_s40.js path/to/harness.js path/to/index.html`.
- Unchanged: Handoff 39 section 4's pins.

## 5. Decision register

The protocol's section 13 (D2–D31) is unchanged. The decisions of section 2.2 are recorded in the rescoring record and
join the protocol's register when the pass ends. Nothing awaits the owner except the simulation notes (section 12),
which are his project's choice.

## 6. Updating the repository (owner)

1. **Upload the zip**: on the repository page, **Add file → Upload files**, drop in `NEEC_repository_s40.zip`,
   **Commit changes** (to `main`).
2. **Paste to Claude Code** (it no longer tags; you do, in step 3):

```
Session 40 update. NEEC_repository_s40.zip is now on main. Please:
1. Pull main and create a new branch from it.
2. Unzip NEEC_repository_s40.zip into the repository root, overwriting (9 files: 6 new, 3 replaced), then delete the zip and stage everything (git add -A).
3. Confirm git ls-files shows 242 files.
4. Run: python3 run_all_checks.py > /tmp/out.txt ; cmp /tmp/out.txt run_all_checks_output.txt
   Expect "SUMMARY: 83 passed, 0 failed, 0 skipped (of 83)." and cmp reporting no difference.
5. Run the fingerprint snippet in section 7 of NEEC_Project_Handoff_40.md; expect e984c0fd6f8f1b673ac5d73cac10f9cf.
6. Commit "NEEC Session 40: rescoring pass part (b), third group, C1.1 (harness v15)", push, open a pull request into main, and merge it with a merge commit if you are able to (otherwise tell me).
7. Show me the full SHA of the merge commit. Do not create or push any tags.
8. Confirm the harness workflow passed on main.
```

3. **Tag the merge commit on GitHub:**
   - Go to **Releases → Draft a new release → Choose a tag**, type `s40`, and click **Create new tag: s40 on publish**.
   - Under **Target → Recent commits**, pick the Session 40 merge commit (the SHA Claude Code showed you).
   - Title it `s40` and click **Publish release**.
4. **Add this handoff to the Project**, and trim the Project as section 11 describes.

## 7. Next session: start here

1. **Clone:** `git clone https://github.com/BetterToBest/NormativeEvaluation /home/claude/neec`.
2. **Verify:**
   - Tags `s34` to `s40` exist.
   - 242 tracked files.
   - The digest below, over every tracked file except this handoff, equals `e984c0fd6f8f1b673ac5d73cac10f9cf`.
   - Harness v15 runs 83 of 83, byte-identical to `run_all_checks_output.txt`.
   - The latest Actions run on `main` passed.
   - The simulation's HEAD: if it has moved past `cd0ceec` (v4.16), note it; every NEEC run stays pinned, and a new
     version reopens CCO units only through the reopening conditions of section 9.

   If the Session 40 update has not been applied, ask the owner to finish section 6 first (the zip is in the
   Session 40 conversation).

```
import hashlib, subprocess
h = hashlib.md5()
for f in sorted(x for x in subprocess.check_output(["git", "ls-files"]).decode().split("\n") if x):
    if f != "NEEC_Project_Handoff_40.md":
        h.update(f.encode() + b"\0" + hashlib.md5(open(f, "rb").read()).digest())
print(h.hexdigest())
```

3. **Then** section 8, item 3.

## 8. Next steps, in priority order

1. **Owner:** section 6.
2. **Next session:** verify (section 7).
3. **The rescoring pass, part (b), continued**, as a new record part with its own script (for example
   `NEEC_Rescoring_s41.md`, importing parts (a), (b1), (b2) and (b3) for cumulative consequences), criterion by
   criterion through the 58 remaining D28 units:
   - C1.4 (2: FALC, PE) first; then C2.1 (5: CCO, DG, FALC, INT, PE); C2.5 (10: CCO, DE, GEO, IF, INT, LM, MC, OS,
     SWF, UBS); C3.2 (4: INT, NSD, PE, SQ); C3.5 (2: CCO, INT); C4.1 (8: CCO, DE, DG, FALC, INT, OS, PE, SWF); C4.2
     (6: CCO, DE, DG, FALC, INT, PE); C4.3 (6: CPS, DG, MMT, NSD, PE, UBI); C4.4 (4: CCO, DG, INT, PE); C4.5 (3: DG,
     FALC, INT); C5.2 (4: IF, LM, NSD, SC); C5.4 (2: CCO, NSD); C5.5 (2: MC, PE).
   - Hold designs' modelled figures to protocol 4.1, run a design's published model only under part (b1)'s decision
     3.2, and apply the readings of all four records alike.
4. **Parts (c)–(e)**, then apply the whole pass by generator (pin the corpus; regenerate the corpus, CSV, README and
   Appendix A.4; recompute the changed flag registers; **replace the anchor examples of section 2.3(3) and Handoff 39
   section 2.3(3), and remove C1.1's 1.0 example** (decision 3.5); restate the protocol's corpus statements; give the
   claims and protocol verifiers and the four rescoring scripts successors).
5. **Step 5 → Report v2.0 and Paper v2.0**, as Handoff 36 section 8 item 4 describes, now also covering the
   corrections of all four rescoring records, including the finding that no system clears C1.1.
6. **Pages site and Hub**; **second pilot**; **Visual Suite v3**, as in Handoff 36, section 8, items 5–7. The site is
   to be linked from the Better To Best Research Hub (`bettertobest.github.io/research-hub/`); Handoff 37 section 10's
   Hub text stands.

## 9. Known limitations (stated, not hidden)

1. This group is one scorer's re-estimation on evidence located in one session. "Not shown" means no evidence was
   located, not that the clause fails. The stress clause fell for every unit chiefly because no rationale estimated
   poverty under stress.
2. **The simulation's figures are the model's**, at the modelling tier, on measures that are not C1.1's basket measure
   (wealth below $25,000; under 30 days of runway). Its Baseline deteriorates sharply over 20 years, which favours the
   design in every reduction measured against it.
3. **Reopening conditions.** CCO-PTF-CIP-SZH's C1.1 reopens if a later simulation version reaches 90% in the reference
   run and 85% in the stress run on its documented measures, or if the model behind the papers' 98% is published and
   reproduces it. Nordic Social Democracy's C1.1 reopens if an absolute-poverty series for Finland's or Sweden's
   early-1990s crisis is located. Handoff 39's reopening conditions stand.
4. Handoff 38's limitations 3–4 stand.

## 10. Hub text

Unchanged from Handoff 37, section 10.

## 11. Standing working notes

- Shell is `sh` (no `time`, no process substitution); `git` and Node are available. Maximum effort; accuracy over
  speed.
- `github.com` and `raw.githubusercontent.com` are reachable from the sandbox. The web-fetch tool opens only URLs
  returned by a search. `bettertobest.github.io`, `ec.europa.eu` and `db.nomics.world` are not reachable from bash,
  so read the Hub by cloning `BetterToBest/research-hub` and the simulation by cloning
  `BetterToBest/compassionism-simulation` (its `harness.js` is the engine; its recession functions are in
  `index.html`).
- **Claude Code cannot push tags** (permissions). Its prompts end at the merge and the merge commit's SHA; the owner
  tags through Releases.
- **The Project holds only the latest handoff.** Every other file is in the repository, which each session clones;
  the owner may remove all Project files except the newest `NEEC_Project_Handoff_N.md`. The CSV attachments to the
  opening message have arrived empty for four sessions and are not needed.
- Scratch before insert; programmatic verification over visual checking; generate, don't transcribe. Scripts find
  inputs beside themselves, print file names only, and are deterministic.
- Decisions are Claude's under the delegation. Record them with reasons, flag substantive changes, distinguish
  corrections from optional polish, say plainly when a file does not exist, and prefer precise, defensible language.
- Give the owner click-by-click steps for anything in GitHub. If the chat disconnects, the owner refreshes; a
  completed reply will be there, and "continue" resumes otherwise.

## 12. Notes for the simulation's maintainers (the owner's project; not NEEC corrections)

Found while running the pinned engine (`cd0ceec`, v4.15) in Sessions 38 and 40, for whoever works on v4.16:

1. **The 98% and $82,000 headline is not reproduced.** At the parameter file's own 98% settings, the engine gives
   78.5% (wealth poverty) and 82.1% (BLEI poverty), and carries $82,000 and 5% as `TARGET_*` constants. Publish the
   model behind 98%, or restate the papers against the current engine.
2. **No income or basket poverty measure.** The headcounts are net wealth under $25,000 and under 30 days of runway;
   the papers use income below 60% of the median. An income-versus-basket headcount (the engine already has
   `LIVING_WAGE_ANNUAL` and `BASE_DAILY_COST`) would map onto NEEC's C1.1 and onto the papers.
3. **The Baseline deteriorates sharply:** wealth poverty 37.7% → 71.4% and BLEI poverty 2.7% → 70.5% over 20 years.
   Calibrate it or document why, and report reductions against year 0 as well as against the Baseline.
4. **An early rise in the reference run:** BLEI poverty goes from 2.7% at year 0 to 19.6% at year 5 before falling to
   12.6%. Check whether it is a year-0 initialisation artifact.
5. **Recessions are missing from `harness.js`.** Port `updateRecession` and `buildRecessionPath`, with a shock option
   in `runScenario`, so stress runs need nothing from `index.html`.
6. **Separate two kinds of stress.** The Stress Test preset mixes an adverse environment with weaker settings (40%
   participation, Basic Unit $900); a preset with the adverse environment at the reference settings is what stress
   criteria test.
7. **The 55% participation collapse** described in three documents is not in the dynamics (Handoff 38, 2.3(3)):
   build it in or relabel it.
8. **A parity drift:** `structuralStability` uses `Math.max(1, …)` in `harness.js` and `Math.max(2, …)` in
   `index.html`; they diverge for runs shorter than 8 years.
9. **Prices are exogenous; recessions only multiply wages; automation only slows wage growth.** An endogenous price
   channel would reopen CCO's C3.4 (Handoff 38).
10. **Record regression changes.** When v4.16 ships, state any change to the seed-42 regression (1965 d, 16.6%, 0.534,
    88.5%) in its changelog, so NEEC's pinned checks can be rerun against it.
