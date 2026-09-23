# NEEC Project Handoff 41

**Session 41 · 2026-09-23 · Owner: Duke Johnson · Scorer and engineer: Claude**
**Predecessor:** Handoff 40 (in the repository). This handoff supersedes its sections 6–11; its section 12 (notes for
the simulation's maintainers) stands unchanged.

Session 41 verified the Session 40 repository and did the fourth group of part (b) of the rescoring pass: **the eleven
part (b) units of C1.4 (2), C2.1 (5) and C3.2 (4)**, re-estimated clause by clause on cited evidence. **None stands;
all eleven become 0.5 (5.5 points); no failure count or tier changes.** CCO-PTF-CIP-SZH keeps first place, 21.5 → 21.0.
A check added this session found that **no scored system now clears five criteria (C1.1, C2.1, C2.3, C2.4, C3.1)**,
and that Session 40's statement that C1.1 was the first such criterion was wrong (section 2.3). Nothing is applied
yet: the record is scratch, and the corpus, CSV and scoring documents change only when the pass ends (protocol
10.1–10.3). The harness is at version 16, **84 of 84 checks passing**, byte-identical on a second run.

---

## 1. Session-start checks

- **Repository.** `main` at `c0ff1a9` (the merge of pull request #7): 242 tracked files, all mode 100644; digest
  `e984c0fd6f8f1b673ac5d73cac10f9cf` (exact match); harness v15 ran 83 of 83, byte-identical to its capture.
  Handoff 40 in the repository is byte-identical with the Project's copy.
- **Tags.** `s34` to `s40` exist; `s40` → `c0ff1a9`. Handoff 40's section 6 is complete.
- **Actions.** Run 34 on `main` (the merge of pull request #7) completed successfully (the REST API was rate-limited;
  the Actions page was read over HTTPS).
- **Simulation.** `BetterToBest/compassionism-simulation` HEAD is still `cd0ceec` (v4.15); `harness.js` md5
  `035d1be8…` and `index.html` md5 `1c8273b1…` unchanged. Research hub at `8e8a6ba`.

## 2. What changed

### 2.1 The rescoring pass, part (b), fourth group (`NEEC_Rescoring_s41.md`, `rescoring_s41.py`)

- **C1.4 (FALC, PE):** the threshold asks for poverty under 8% and demand above 85% of baseline under 30/50/70%
  displacement. Neither design, nor its literature, estimates any scenario. PE's poverty clause stands as audited
  (Albert specifies an average income for those who cannot work); its demand clause is not shown.
- **C2.1 (DG, FALC, PE, CCO, INT):** clause 2 is a method clause (protocol 2.3(d)). The Paper's own section 7.3
  defines it as self-reported autonomy correlated (r > 0.65) with observed behaviour. No design has such evidence; the
  closest component evidence for CCO (OpenResearch's randomised $1,000-a-month study: longer, more selective job
  searches and more moves) shows the behaviour but tests no self-reported share.
- **C3.2 (SQ, NSD):** the stress clause is **short** on the 2021-23 episode. Global inflation averaged 8.7% in 2022;
  US CPI peaked at 9.1% (core 6.6%); every Nordic economy ran HICP inflation above 5% in every month May–October 2022
  (October: Denmark 11.4%, Sweden 9.8%, Finland and Norway 8.4%, Iceland 6.4%), while Switzerland held 2.9%. Clause 3
  (automatic adjustment) is not estimated; the verdict is already fixed.
- **C3.2 (PE, INT):** no stress estimate. INT is read alike with FALC's part (a) unit; a moot reading is not open
  because the corpus's review of Integral records procurement from traditional markets during transition.
- **Cumulatively with parts (a) to (b3):** 98 units re-estimated, 6 stand, 92 become 0.5 (46.0 points). Dominance
  pairs 18 → 18 (new IF>SQ; lost PE>CN); frontier 12 → 12. PE and INT share second at 16.5. **47 D28 units remain.**

### 2.2 Decisions under the delegation (record, section 3)

- **3.1** C2.5 moves after C3.2, so its ten units' readings are made together (procedural; no score changes).
- **3.2** C1.4 asks for levels under the three displacement scenarios; a mechanism decoupling income from employment is
  not an estimate (extends part (b3)'s reading 3.1). A moot reading of the demand clause was weighed and rejected.
- **3.3** C2.1 clause 2 is shown only by observed behaviour tested against self-reports; a specification or model
  cannot supply it; component precedents calibrate (protocol 4.1).
- **3.4** C3.2's stress clause is read on the 2021-23 shock for configured economies, whatever the inflation's origin;
  for designs, part (b3)'s reading 3.1 applies.
- **3.5** Part (b3)'s reading 3.5 applies to **every** 1.0 band left with no corpus unit: C1.1, C2.1, C2.3, C2.4 and
  C3.1. Each keeps its description and drops its example when the pass is applied.

### 2.3 Corrections found (not polish; record, section 6)

1. **Session 40's record (reading 3.5, section 6 item 3) and Handoff 40 (section 2.3(3)) are wrong** that C1.1 was
   the first criterion left with no 1.0. Part (b1) had emptied C2.3 and C2.4, and part (b2) C3.1; the earlier scripts
   counted moved examples, not remaining units. **The finding the v2.0 documents must state is now: after the pass so
   far, no scored system clears five criteria (C1.1, C2.1, C2.3, C2.4, C3.1), three of them in Domain 2, although
   every criterion had a 1.0 in the published corpus.**
2. Report v1.6, CCO C2.1's "Modeling shows 75%+ report genuine autonomy": the engine has no autonomy measure and no
   hub document states the figure. Source it or remove it in v2.0.
3. C1.4's Pass Threshold and Measurement line differ (poverty <8% across all three scenarios versus 5/7/10%; demand
   >85% versus 90/85/80% with 110% caps). Flagged per protocol 2.3; decides no unit. Paper v2.0 aligns them.
4. Report v1.6's SQ and NSD C3.2 rationales rest on normal-conditions records; v2.0 states the 2021-23 record.

*Polish, optional:* C2.1's clause 2 wording differs from the Paper's own section 7.3 method.

### 2.4 Other files

`run_all_checks.py` v16 adds check 84; `README.md` regenerated (only the check count changes).

## 3. Files

The repository update is **7 files** at the zip's top level, `NEEC_repository_s41.zip`:

| File | MD5 (first 8) | Status |
|---|---|---|
| `NEEC_Rescoring_s41.md` | `2b5cac54` | new (the pass's record, part (b), fourth group) |
| `rescoring_s41.py` | `566993f1` | new |
| `rescoring_s41_output.txt` | `f722e0a2` | new |
| `NEEC_Project_Handoff_41.md` | (this file) | new |
| `run_all_checks.py` | `ee4899cb` | replaced (v16) |
| `run_all_checks_output.txt` | `aa3d7fd0` | replaced |
| `README.md` | `55caa38b` | replaced |

**The Project** gets this handoff only (GitHub is canonical, D27(b)).

## 4. Pins

- `rescoring_s41.py` imports `rescoring_s37.py` to `rescoring_s40.py` and reads the corpus in force. When the pass is
  applied, its consequence figures and the record's tables need a successor or a pinned corpus snapshot, as for the
  four earlier scripts.
- No simulation run is used in this group. Handoff 40 section 4's pins stand.

## 5. Decision register

The protocol's section 13 (D2–D31) is unchanged. The readings of section 2.2 are recorded in the rescoring record and
join the protocol's register when the pass ends. Nothing awaits the owner except the simulation notes (Handoff 40,
section 12), which are his project's choice.

## 6. Updating the repository (owner)

1. **Upload the zip**: on the repository page, **Add file → Upload files**, drop in `NEEC_repository_s41.zip`,
   **Commit changes** (to `main`).
2. **Paste to Claude Code:**

```
Session 41 update. NEEC_repository_s41.zip is now on main. Please:
1. Pull main and create a new branch from it.
2. Unzip NEEC_repository_s41.zip into the repository root, overwriting (7 files: 4 new, 3 replaced), then delete the zip and stage everything (git add -A).
3. Confirm git ls-files shows 246 files.
4. Run: python3 run_all_checks.py > /tmp/out.txt ; cmp /tmp/out.txt run_all_checks_output.txt
   Expect "SUMMARY: 84 passed, 0 failed, 0 skipped (of 84)." and cmp reporting no difference.
5. Run the fingerprint snippet in section 7 of NEEC_Project_Handoff_41.md; expect 1e7c45b58d268e760216669483372a45.
6. Commit "NEEC Session 41: rescoring pass part (b), fourth group, C1.4 C2.1 C3.2 (harness v16)", push, open a pull request into main, and merge it with a merge commit if you are able to (otherwise tell me).
7. Show me the full SHA of the merge commit. Do not create or push any tags.
8. Confirm the harness workflow passed on main.
```

3. **Tag the merge commit on GitHub:**
   - Go to **Releases → Draft a new release → Choose a tag**, type `s41`, and click **Create new tag: s41 on publish**.
   - Under **Target → Recent commits**, pick the Session 41 merge commit (the SHA Claude Code showed you).
   - Title it `s41` and click **Publish release**.
4. **Add this handoff to the Project**, and remove `NEEC_Project_Handoff_40.md` from it (section 11).

## 7. Next session: start here

1. **Clone:** `git clone https://github.com/BetterToBest/NormativeEvaluation /home/claude/neec`. If the directory
   already exists, run `git fetch --tags origin` and confirm `HEAD` equals `origin/main` before trusting it.
2. **Verify:**
   - Tags `s34` to `s41` exist.
   - 246 tracked files.
   - The digest below, over every tracked file except this handoff, equals `1e7c45b58d268e760216669483372a45`.
   - Harness v16 runs 84 of 84, byte-identical to `run_all_checks_output.txt`.
   - The latest Actions run on `main` passed.
   - The simulation's HEAD: if it has moved past `cd0ceec` (v4.16), note it; every NEEC run stays pinned, and a new
     version reopens CCO units only through the reopening conditions of section 9.

   If the Session 41 update has not been applied, ask the owner to finish section 6 first (the zip is in the
   Session 41 conversation).

```
import hashlib, subprocess
h = hashlib.md5()
for f in sorted(x for x in subprocess.check_output(["git", "ls-files"]).decode().split("\n") if x):
    if f != "NEEC_Project_Handoff_41.md":
        h.update(f.encode() + b"\0" + hashlib.md5(open(f, "rb").read()).digest())
print(h.hexdigest())
```

3. **Then** section 8, item 3.

## 8. Next steps, in priority order

1. **Owner:** section 6.
2. **Next session:** verify (section 7).
3. **The rescoring pass, part (b), continued**, as a new record part with its own script (`NEEC_Rescoring_s42.md`,
   importing parts (a) to (b4)), through the 47 remaining D28 units:
   - **C2.5 next (10: CCO, DE, GEO, IF, INT, LM, MC, OS, SWF, UBS)**, taken whole. Leads found while scoping it, to be
     tested rather than assumed: GEO, UBS, SWF and IF carry a clause-4 reach code (voluntary association), which holds
     them at 0.5 under D28(c) unless a D31 source places association inside the mechanism, so their clause 2 may be
     left not estimated; clause 2's "no differential treatment" needs a reading (the Measurement line equates it with
     "penalties for non-participation"); for OS, Ostrom's design principle 7 (minimal recognition of rights to
     organise) bears on clause 4, and residence-bound appropriation rights bear on clause 3 ("relocate without losing
     essential benefits"); for DE, a comprehensive system, host-jurisdiction protections are not credited (D29(c)); for
     LM, Nozick's framework for utopia is the founding source on association and exit.
   - Then C3.5 (2: CCO, INT); C4.1 (8); C4.2 (6); C4.3 (6); C4.4 (4); C4.5 (3); C5.2 (4); C5.4 (2); C5.5 (2).
   - Hold designs' modelled figures to protocol 4.1, run a design's published model only under part (b1)'s decision
     3.2, and apply the readings of all five records alike.
4. **Parts (c)–(e)**, then apply the whole pass by generator (pin the corpus; regenerate the corpus, CSV, README and
   Appendix A.4; recompute the changed flag registers; **replace the seven anchor examples the pass moves, or remove
   them from the five 1.0 bands left with no corpus unit** (reading 3.5); restate the protocol's corpus statements;
   give the claims and protocol verifiers and the five rescoring scripts successors).
5. **Step 5 → Report v2.0 and Paper v2.0**, as Handoff 36 section 8 item 4 describes, now also covering the
   corrections of all five rescoring records, including **the finding that no system clears five criteria**.
6. **Pages site and Hub**; **second pilot**; **Visual Suite v3**, as in Handoff 36, section 8, items 5–7. The site is
   to be linked from the Better To Best Research Hub (`bettertobest.github.io/research-hub/`); Handoff 37 section 10's
   Hub text stands. The five-criteria finding belongs in the v2.0 site's summary, stated with its reasons.

## 9. Known limitations (stated, not hidden)

1. This group is one scorer's re-estimation on evidence located in one session. "Not shown" means no evidence was
   located, not that the clause fails. Every unit fell on a clause no rationale estimated.
2. The two short clauses rest on official statistics for one stress episode (2021-23); the record names it.
3. **Reopening conditions.** A scoring document that estimates C1.4 under the three displacement scenarios, validates
   C2.1 by observed behaviour, or estimates C3.2 under an external 8% scenario, at the entry's tier, reopens its unit.
   Handoff 40's and Handoff 39's reopening conditions stand.
4. Handoff 38's limitations 3–4 stand.

## 10. Hub text

Unchanged from Handoff 37, section 10.

## 11. Standing working notes

- Shell is `sh` (no `time`, no process substitution); `git` and Node are available. Maximum effort; accuracy over
  speed.
- `github.com` and `raw.githubusercontent.com` are reachable from the sandbox. The web-fetch tool opens only URLs
  returned by a search; it did open an `ec.europa.eu` PDF that a search returned. `bettertobest.github.io`,
  `ec.europa.eu` and `db.nomics.world` are not reachable from bash, so read the Hub by cloning
  `BetterToBest/research-hub` and the simulation by cloning `BetterToBest/compassionism-simulation`.
- **The sandbox can keep `/home/claude` between turns of one conversation.** Fetch and confirm an existing clone
  against `origin` before using it.
- **Claude Code cannot push tags** (permissions). Its prompts end at the merge and the merge commit's SHA; the owner
  tags through Releases.
- **The Project holds only the latest handoff.** Every other file is in the repository, which each session clones.
- Scratch before insert; programmatic verification over visual checking; generate, don't transcribe (this session's
  record was assembled from its script's generated tables). Scripts find inputs beside themselves, print file names
  only, and are deterministic.
- Decisions are Claude's under the delegation. Record them with reasons, flag substantive changes, distinguish
  corrections from optional polish, say plainly when a file does not exist, and prefer precise, defensible language.
- Give the owner click-by-click steps for anything in GitHub. If the chat disconnects, the owner refreshes; a
  completed reply will be there, and "continue" resumes otherwise.
