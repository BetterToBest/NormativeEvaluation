# NEEC Project Handoff 42

**Session 42 · 2026-09-23 · Owner: Duke Johnson · Scorer and engineer: Claude**
**Predecessor:** Handoff 41 (in the repository). This handoff supersedes its sections 6–11; Handoff 40's section 12
(notes for the simulation's maintainers) stands, with three further notes in section 2.4 below.

Session 42 verified the Session 41 repository and did the fifth group of part (b) of the rescoring pass: **C2.5 Exit
Rights and Mobility, its ten part (b) units** (all ten of its published 1.0s), re-estimated clause by clause on cited
evidence. **One stands (Libertarian Minarchism, flagged toward 0.5); nine become 0.5 (4.5 points); no failure count
or tier changes.** CCO-PTF-CIP-SZH keeps first place, 21.0 → 20.5, and falls on **one clause only**: its own
documents set the Acre Equity a Public Trust Housing resident can realise on leaving below face value for five years
(section 2.1). Nothing is applied yet: the record is scratch, and the corpus, CSV and scoring documents change only
when the pass ends (protocol 10.1–10.3). The harness is at version 17, **85 of 85 checks passing**, byte-identical on
a second run.

---

## 1. Session-start checks

- **Repository.** `main` at `5c85d44` (the merge of pull request #8): 246 tracked files, all mode 100644; digest
  `1e7c45b58d268e760216669483372a45` (exact match); harness v16 ran 84 of 84, byte-identical to its capture.
  Handoff 41 in the repository is byte-identical with the Project's copy.
- **Tags.** `s34` to `s41` exist; `s41` → `5c85d44`. Handoff 41's section 6 is complete.
- **Actions.** Run 39 on `main` (the merge of pull request #8) completed successfully (the REST API was rate-limited;
  the Actions page was read over HTTPS).
- **Simulation.** `BetterToBest/compassionism-simulation` HEAD is still `cd0ceec` (v4.15); `harness.js` md5
  `035d1be8…` and `index.html` md5 `1c8273b1…` unchanged. Research hub at `8e8a6ba`.

## 2. What changed

### 2.1 The rescoring pass, part (b), fifth group (`NEEC_Rescoring_s42.md`, `rescoring_s42.py`)

- **Libertarian Minarchism: stands at 1.0, flagged (alternative 0.5).** Clause 2 (no differential treatment), the one
  the audit found silent, is cleared on Nozick: the minimal state protects everyone in its territory (the principle of
  compensation extends protection to independents), and the framework for utopia lets no community impose itself on
  anyone who stays out. The flag: C2.5's 0.5 anchor example (Status Quo) and a same-archetype peer (Stakeholder
  Capitalism) count real economic constraints on exit against the criterion; read that way, clauses 1 and 3 fail for
  an entry whose own text records survival "entirely contingent on market participation" (protocol 5.3).
- **CCO-PTF-CIP-SZH: 0.5, on clause 1 alone.** A departure from the audit's A code, because the design's own sources
  contradict "opt-out without penalty": the BLEI paper's Table 1a (10–20% of face value realisable in months 0–6,
  rising to 80–90% after five years; "exit fees" among the causes), the housing paper (cash equivalent $67,000–134,000
  of $168,000–336,000 upon exit), and the model's `pthLiquidShare` (0.15 → 0.85). Clauses 2–4 are **cleared on the
  design's own legislative texts** (the draft Act's universal automatic basic unit, opt-in housing with the private
  market intact, equal non-housing Acre Equity; the draft constitutional amendment on voluntary associations).
  **Exit terms under which a resident can realise Acre Equity within three months without material loss would reopen
  the unit, which would then stand.** That is the design's choice, not the scorer's.
- **Integral: 0.5.** Clause 2 not shown: goods are released only against verified credit access and the design aims to
  replace the market it grows alongside, with no statement of what a non-participant then receives (the corpus's own
  review records the same gap). Clause 3 cleared on the design's cross-node credit reciprocity (ITC-6).
- **Mutual Credit: 0.5.** Clause 2 cleared (credit by and for members; levies nothing on non-members); clause 3 not
  shown (a balance and credit line are held in one node).
- **Doughnut Economics: 0.5.** Clause 4 not shown: political voice is a floor of the social foundation, not a
  protection, and the host jurisdiction's law is not credited (protocol 3.2; D29(c)).
- **Ostrom: 0.5.** Clause 3 short (bounded membership, design principle 1; the Törbel articles of 1483 bar outsiders
  from the communal rights); clause 4 not shown (design principle 7 is forbearance by external authorities); clause 2
  not estimated.
- **Georgism, Universal Basic Services, Sovereign Wealth Fund Statism, Islamic finance: 0.5 on reach.** The audit's
  five out-of-reach codes are confirmed: no D31 source places voluntary association (or, for Islamic finance,
  geographic mobility) inside the mechanism. Clause 2 of the first two and of Islamic finance is not estimated.
- **Flags:** Libertarian Minarchism added; Islamic finance and Ostrom removed (each now scored at its own
  alternative).
- **Cumulatively with parts (a) to (b4):** 108 units re-estimated, 7 stand, 101 become 0.5 (50.5 points). Dominance
  pairs 18 → 18 (new PE>DE; lost CCO>LM); **frontier 12 → 13 (Libertarian Minarchism joins)**. PE second at 16.5;
  Integral and Degrowth third at 16.0. Still five criteria with no 1.0 (C2.5 keeps one). **37 D28 units remain.**

### 2.2 Decisions under the delegation (record, section 3)

- **3.1** C2.5 clause 2 means no burden on non-participants beyond forgone benefits (the Measurement line's
  "penalties for non-participation"); identical treatment would be a test that cannot be passed. A model that cannot
  represent a burden on non-participants cannot show it. Left open: who is a non-participant under a jurisdiction-wide
  mechanism, and whether a residence-based boundary rule differentiates.
- **3.2** Clause 3 requires that essential benefits survive a move within the area the system serves; a move beyond
  it is an exit (clause 1).
- **3.3** Clause 4 requires a protection the entry's sources specify; a goal is not one, and the host's law is not
  credited.
- **3.4** The five reach codes confirmed by D31 search; Sovereign Wealth Fund Statism is not flagged (D28(c) decides
  it, as with MMT + Job Guarantee's C2.4).
- **3.5** CCO-PTF-CIP-SZH clause 1: the design's exit terms are a material cost for Public Trust Housing residents.
- **3.6** Libertarian Minarchism stands with a flag, not an exception: the question is calibration with a peer, not a
  contradiction in its own sources.
- **3.7** C2.5's 1.0 anchor example moves (the eighth); when the pass is applied it cites Libertarian Minarchism with
  its flag noted, since a corpus 1.0 exists.

### 2.3 Corrections found (not polish; record, section 6)

1. Report v1.6, CCO-PTF-CIP-SZH C2.5, "enabling opt-out without penalty", is contradicted by the design's own exit
   terms. Report v2.0 states them.
2. `Integral_NEEC_Review.md` estimates no penalty for non-participants and mobility across nodes without evidence,
   while its own C1.1 section says non-participants' access to essentials is unclear. Report v2.0 restates Integral's
   C2.5 on the design's sources.
3. The Islamic finance and Ostrom documents quote C2.5's threshold in its anchor form; part (e) covers it.
4. Report v1.6, Libertarian Minarchism C2.5, does not address non-participants or the calibration; Report v2.0 states
   the Nozick basis and the flag.

*Polish, optional:* Paper v2.0 could write "no penalty for non-participation" for "no differential treatment".

### 2.4 Notes for the design's maintainers (the owner's project; add to Handoff 40, section 12)

(a) The model pays the basic unit only to its participating share (`partRate` 0.78) while the draft Act pays every
citizen and legal resident automatically. (b) The zone-formation pseudocode weights preferences by "engagement" and
tenure without defining engagement. (c) The Acre Equity exit terms differ across documents (a tenure schedule in the
BLEI paper and the model; 40% of face value after 20 years in the housing paper), and the model does not simulate an
exit from Public Trust Housing.

### 2.5 Other files

`run_all_checks.py` v17 adds check 85; `README.md` regenerated (only the check count changes).

## 3. Files

The repository update is **7 files** at the zip's top level, `NEEC_repository_s42.zip`:

| File | MD5 (first 8) | Status |
|---|---|---|
| `NEEC_Rescoring_s42.md` | `8d125686` | new (the pass's record, part (b), fifth group) |
| `rescoring_s42.py` | `b848a475` | new |
| `rescoring_s42_output.txt` | `462c4498` | new |
| `NEEC_Project_Handoff_42.md` | (this file) | new |
| `run_all_checks.py` | `b668b51a` | replaced (v17) |
| `run_all_checks_output.txt` | `b07688de` | replaced |
| `README.md` | `7e752368` | replaced |

**The Project** gets this handoff only (GitHub is canonical, D27(b)).

## 4. Pins

- `rescoring_s42.py` imports `rescoring_s37.py` to `rescoring_s41.py` and reads the corpus in force. When the pass is
  applied, its consequence figures and the record's tables need a successor or a pinned corpus snapshot, as for the
  five earlier scripts.
- The design's sources used here are pinned by commit: research hub `8e8a6ba`; simulation `cd0ceec` (`harness.js`
  constants only; no run). Integral's system pages were read on 2026-09-23 (its v0.1, March 2026); its white-paper
  PDFs returned 404. Handoff 40 section 4's pins stand.

## 5. Decision register

The protocol's section 13 (D2–D31) is unchanged. The readings of section 2.2 are recorded in the rescoring record and
join the protocol's register when the pass ends. **Nothing awaits the owner as a NEEC decision.** Two things are his
project's choices: the simulation notes (Handoff 40, section 12, and section 2.4 above), and whether to change the
Public Trust Housing exit terms, which alone decide CCO-PTF-CIP-SZH's C2.5.

## 6. Updating the repository (owner)

1. **Upload the zip**: on the repository page, **Add file → Upload files**, drop in `NEEC_repository_s42.zip`,
   **Commit changes** (to `main`).
2. **Paste to Claude Code:**

```
Session 42 update. NEEC_repository_s42.zip is now on main. Please:
1. Pull main and create a new branch from it.
2. Unzip NEEC_repository_s42.zip into the repository root, overwriting (7 files: 4 new, 3 replaced), then delete the zip and stage everything (git add -A).
3. Confirm git ls-files shows 250 files.
4. Run: python3 run_all_checks.py > /tmp/out.txt ; cmp /tmp/out.txt run_all_checks_output.txt
   Expect "SUMMARY: 85 passed, 0 failed, 0 skipped (of 85)." and cmp reporting no difference.
5. Run the fingerprint snippet in section 7 of NEEC_Project_Handoff_42.md; expect 63f7c0e4abfcb1499502fa86ada37a00.
6. Commit "NEEC Session 42: rescoring pass part (b), fifth group, C2.5 (harness v17)", push, open a pull request into main, and merge it with a merge commit if you are able to (otherwise tell me).
7. Show me the full SHA of the merge commit. Do not create or push any tags.
8. Confirm the harness workflow passed on main.
```

3. **Tag the merge commit on GitHub:**
   - Go to **Releases → Draft a new release → Choose a tag**, type `s42`, and click **Create new tag: s42 on publish**.
   - Under **Target → Recent commits**, pick the Session 42 merge commit (the SHA Claude Code showed you).
   - Title it `s42` and click **Publish release**.
4. **Add this handoff to the Project**, and remove `NEEC_Project_Handoff_41.md` from it (section 11).

## 7. Next session: start here

1. **Clone:** `git clone https://github.com/BetterToBest/NormativeEvaluation /home/claude/neec`. If the directory
   already exists, run `git fetch --tags origin` and confirm `HEAD` equals `origin/main` before trusting it.
2. **Verify:**
   - Tags `s34` to `s42` exist.
   - 250 tracked files.
   - The digest below, over every tracked file except this handoff, equals `63f7c0e4abfcb1499502fa86ada37a00`.
   - Harness v17 runs 85 of 85, byte-identical to `run_all_checks_output.txt`.
   - The latest Actions run on `main` passed.
   - The simulation's HEAD: if it has moved past `cd0ceec` (v4.15), note it; every NEEC run stays pinned, and a new
     version reopens CCO units only through the reopening conditions of section 9.

   If the Session 42 update has not been applied, ask the owner to finish section 6 first (the zip is in the
   Session 42 conversation).

```
import hashlib, subprocess
h = hashlib.md5()
for f in sorted(x for x in subprocess.check_output(["git", "ls-files"]).decode().split("\n") if x):
    if f != "NEEC_Project_Handoff_42.md":
        h.update(f.encode() + b"\0" + hashlib.md5(open(f, "rb").read()).digest())
print(h.hexdigest())
```

3. **Then** section 8, item 3.

## 8. Next steps, in priority order

1. **Owner:** section 6.
2. **Next session:** verify (section 7).
3. **The rescoring pass, part (b), continued**, as a new record part with its own script (`NEEC_Rescoring_s43.md`,
   importing parts (a) to (b5)), through the 37 remaining D28 units:
   - **C3.5 next (2: CCO-PTF-CIP-SZH, Integral).** Clauses: detection within 1 week; diagnosis ≥80%; correction
     ≥70%; externalisation <10% of total costs. The audit coded CCO `AASS` and Integral `ASSA`; no audited 1.0 shows
     the correction rate (clause 3). Leads to test, not assume: the rates are outcome levels, so part (b1)'s reading
     3.5 (an institution specified is not an estimate of the level) should apply alike; Integral's FRS pages
     (integralcollective.io/system/frs.html) are the design's own source; for CCO, whether the published model
     represents detection, diagnosis or correction of failures at all (it may not, which would leave the rates not
     shown at the modelling tier). C3.5 is small enough to take with C4.1 (8) in the same session.
   - Then C4.1 (8); C4.2 (6); C4.3 (6); C4.4 (4); C4.5 (3); C5.2 (4); C5.4 (2); C5.5 (2).
   - Hold designs' modelled figures to protocol 4.1, run a design's published model only under part (b1)'s decision
     3.2, and apply the readings of all six records alike.
4. **Parts (c)–(e)**, then apply the whole pass by generator (pin the corpus; regenerate the corpus, CSV, README and
   Appendix A.4; recompute the changed flag registers; **replace the eight anchor examples the pass moves, or remove
   them from the five 1.0 bands left with no corpus unit** (part (b4), reading 3.5; part (b5), reading 3.7); restate
   the protocol's corpus statements; give the claims and protocol verifiers and the six rescoring scripts successors).
5. **Step 5 → Report v2.0 and Paper v2.0**, as Handoff 36 section 8 item 4 describes, now also covering the
   corrections of all six rescoring records, including **the finding that no system clears five criteria**.
6. **Pages site and Hub**; **second pilot**; **Visual Suite v3**, as in Handoff 36, section 8, items 5–7. The site is
   to be linked from the Better To Best Research Hub (`bettertobest.github.io/research-hub/`); Handoff 37 section 10's
   Hub text stands. The five-criteria finding belongs in the v2.0 site's summary, stated with its reasons.

## 9. Known limitations (stated, not hidden)

1. This group is one scorer's re-estimation on evidence located in one session. "Not shown" means no evidence was
   located, not that the clause fails.
2. Libertarian Minarchism's 1.0 rests on a flagged reading of "exit"; the other reading gives 0.5.
3. **Reopening conditions.** Public Trust Housing exit terms that let a resident realise Acre Equity within three
   months without material loss reopen CCO-PTF-CIP-SZH's C2.5 (it would then stand). A design source stating what a
   non-participant receives once Integral has replaced the market reopens Integral's; a source in a mechanism's own
   literature placing voluntary association inside it reopens Georgism's, Universal Basic Services', Sovereign Wealth
   Fund Statism's or Islamic finance's (their clause 2 would then need estimating). Handoff 41's, 40's and 39's
   reopening conditions stand.
4. Handoff 38's limitations 3–4 stand.

## 10. Hub text

Unchanged from Handoff 37, section 10.

## 11. Standing working notes

- Shell is `sh` (no `time`, no process substitution); `git` and Node are available. Maximum effort; accuracy over
  speed.
- `github.com` and `raw.githubusercontent.com` are reachable from the sandbox. The web-fetch tool opens only URLs
  returned by a search. `bettertobest.github.io`, `ec.europa.eu` and `db.nomics.world` are not reachable from bash, so
  read the Hub by cloning `BetterToBest/research-hub` and the simulation by cloning
  `BetterToBest/compassionism-simulation`. Integral's system pages (`integralcollective.io/system/*.html`) open with
  the web-fetch tool; its white-paper PDFs return 404.
- **The sandbox can keep `/home/claude` between turns of one conversation.** Fetch and confirm an existing clone
  against `origin` before using it.
- **Claude Code cannot push tags** (permissions). Its prompts end at the merge and the merge commit's SHA; the owner
  tags through Releases.
- **The Project holds only the latest handoff.** Every other file is in the repository, which each session clones.
- Scratch before insert; programmatic verification over visual checking; generate, don't transcribe (this session's
  record was assembled from a template whose tables were filled from its script's output). Scripts find inputs beside
  themselves, print file names only, and are deterministic.
- Decisions are Claude's under the delegation. Record them with reasons, flag substantive changes, distinguish
  corrections from optional polish, say plainly when a file does not exist, and prefer precise, defensible language.
- Give the owner click-by-click steps for anything in GitHub. If the chat disconnects, the owner refreshes; a
  completed reply will be there, and "continue" resumes otherwise.
