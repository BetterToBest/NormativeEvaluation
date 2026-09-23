# NEEC Project Handoff 39

**Session 39 · 2026-09-23 · Owner: Duke Johnson · Scorer and engineer: Claude**
**Predecessor:** Handoff 38 (in the Project and the repository). This handoff supersedes its sections 6–11.

Session 39 verified the Session 38 repository and did the second group of part (b) of the rescoring pass (Handoff
38, section 8 item 3): **C5.1's second clause tested in full on its eleven 1.0s outside D28's population, and C3.1's
five part (b) units**, re-estimated clause by clause on cited evidence. **Two stand; 14 become 0.5 (7.0 points); no
failure count or tier changes.** Nothing is applied yet: the record is scratch, and the corpus, CSV and scoring
documents change only when the pass ends (protocol 10.1–10.3). The harness is at version 14, **82 of 82 checks
passing**, byte-identical on a second run.

---

## 1. Session-start checks

- **Repository.** `main` at `ab16090` (the merge of pull request #5): 232 tracked files, all mode 100644; digest
  `7494437a882501ee806748bb618fe697` (exact match); harness v13 ran 81 of 81, byte-identical to its capture.
  Handoff 38 in the repository is byte-identical with the Project's copy.
- **Tags.** `s34` to `s38` exist; `s38` → `ab16090`. Handoff 38's section 6 is complete.
- **Actions.** Run 23 on `main` (the merge of pull request #5) completed successfully (the REST API was
  rate-limited; the Actions page was read over HTTPS).
- **Attachments.** The seven CSV files attached to the opening message arrived empty again; the repository copies
  were used.

## 2. What changed

### 2.1 The rescoring pass, part (b), second group (`NEEC_Rescoring_s39.md`, `rescoring_s39.py`)

- **Stand (2):** UBI's C5.1 (Alaska's dividend cut poverty by an estimated 2.5–4 points a year from 1990, about a
  third in 2015, with no fall in employment), **flagged with 0.5** because the precedent is a dividend far below the
  entry's proposed level; and Ostrom's C5.1 (its three multi-case datasets and Cox et al.'s review of 91 studies).
- **Become 0.5 (14):** Market Socialism's C5.1 is **short** (Mondragon's members are 32–45% of its 81,000 workers,
  not "80,000+ worker-owners"); Nordic Social Democracy, China, Singapore and Qatar fall on the reading part (a)
  applied to Status Quo, each flagged toward 1.0; Mutual Credit and Sovereign Wealth Fund Statism on outcomes mixed
  across their implementations (UK LETS and Argentina's barter networks; Timor-Leste's over-withdrawals), flagged
  toward 1.0; Universal Basic Services on both clauses (its published flag resolves). All five C3.1 units: none
  specifies support per person rising with crisis severity (MMT and UBI short, the other three not shown).
- **CCO-PTF-CIP-SZH:** C5.1 falls on clause 1: the design's own site lists five components, and the precedents
  the rationale cites cover at most three (the Citizens Internet Portal's precedents are under twenty years; none is
  cited for Social Zone Harmonization). Its clause 2 clears on community land trusts' documented foreclosure rate.
  It keeps first place, 22.5 → 22.0.
- **Cumulatively with parts (a) and (b1):** 78 units re-estimated, 6 stand, 72 become 0.5 (36.0 points). Dominance
  pairs 14 → 18; frontier 13 → 12. 67 D28 units remain; C5.1's second clause is now tested on all thirteen 1.0s.

### 2.2 Decisions under the delegation (record, section 3)

- **3.1** C5.1 clause 2: the benefits are those the unit's C5.1 rationale claims for the components it counts; a
  configured economy's component is the configuration, so its headline claims (Status Quo's precedent). Cleared,
  short or not shown by stated tests; outcomes mixed across the implementations counted are not shown.
- **3.2** C5.1 clause 1: the own-source exception reopens two component counts (CCO-PTF-CIP-SZH 60%, UBS 43%),
  recorded as not shown, not short.
- **3.3** C3.1 clause 2: proportional scaling, decided by protocol 4.2. No unit in the corpus turns on it.
- **3.4** MMT's C3.1 clause 2: the audit's A rested on widening enrolment, which part (a)'s reading assigns to
  clause 3.
- **3.5** China, Singapore and Qatar follow Status Quo's reading, as their rationales adopt its reasoning.

### 2.3 Corrections found (not polish; record, section 6)

1. Report v1.6's Market Socialism C5.1 figures (worker-owners; the survival comparison).
2. Report v1.6's CCO-PTF-CIP-SZH C5.1 "70%+ components proven".
3. **Five anchor examples in `criteria.json` cite units the pass moves** (C2.1 and C3.1: UBI; C2.3: Degrowth; C2.4:
   Participatory Economics; C5.1: Market Socialism). Parts (a) and (b1) did not list the first three.
   `build_criteria.py` will fail on them when the pass is applied unless each band gets a new example.
4. The UBS document's C5.1 sector count.

### 2.4 Other files

`run_all_checks.py` v14 adds check 82; `README.md` regenerated (only the check count changes).

## 3. Files

The repository update is **7 files** at the zip's top level, `NEEC_repository_s39.zip`:

| File | MD5 (first 8) | Status |
|---|---|---|
| `NEEC_Rescoring_s39.md` | `317a50c0` | new (the pass's record, part (b), second group) |
| `rescoring_s39.py` | `1a9e0a96` | new |
| `rescoring_s39_output.txt` | `7ed2cdf1` | new |
| `NEEC_Project_Handoff_39.md` | (this file) | new |
| `run_all_checks.py` | `a85ff134` | replaced (v14) |
| `run_all_checks_output.txt` | `177af529` | replaced |
| `README.md` | `59f66737` | replaced |

**The Project** gets this handoff only (GitHub is canonical, D27(b)).

## 4. Pins

- `rescoring_s39.py` imports `rescoring_s37.py` and `rescoring_s38.py` and reads the corpus in force. When the pass
  is applied, its consequence figures and the record's tables need a successor or a pinned corpus snapshot, as for
  the two earlier scripts.
- Unchanged: Handoff 38 section 4's pins.

## 5. Decision register

The protocol's section 13 (D2–D31) is unchanged. The decisions of section 2.2 are recorded in the rescoring record
and join the protocol's register when the pass ends. Nothing awaits the owner except Handoff 38's simulation note
(2.3(3) there), which is his project's choice.

## 6. Updating the repository (owner)

1. **Upload the zip**: on the repository page, **Add file → Upload files**, drop in `NEEC_repository_s39.zip`,
   **Commit changes** (to `main`).
2. **Paste to Claude Code:**

```
Session 39 update. NEEC_repository_s39.zip is now on main. Please:
1. Pull main and create a new branch from it.
2. Unzip NEEC_repository_s39.zip into the repository root, overwriting (7 files: 4 new, 3 replaced), then delete the zip and stage everything (git add -A).
3. Confirm git ls-files shows 236 files.
4. Run: python3 run_all_checks.py > /tmp/out.txt ; cmp /tmp/out.txt run_all_checks_output.txt
   Expect "SUMMARY: 82 passed, 0 failed, 0 skipped (of 82)." and cmp reporting no difference.
5. Run the fingerprint snippet in section 7 of NEEC_Project_Handoff_39.md; expect d5985aa1dd94f95f7a108cdc9d51c52e.
6. Commit "NEEC Session 39: rescoring pass part (b), second group, C5.1 clause 2 and C3.1 (harness v14)", push, open a pull request into main, and merge it with a merge commit if you are able to (otherwise tell me).
7. Tag the merge commit s39 and push it (git push origin s39), then run git ls-remote --tags origin and show me the result. If pushing the tag is refused, say so plainly.
8. Confirm the harness workflow passed on main.
```

3. **If Claude Code cannot push the tag**, create it on GitHub:
   - Go to **Releases → Draft a new release → Choose a tag**, type `s39`, and click **Create new tag: s39 on publish**.
   - Under **Target → Recent commits**, pick the Session 39 merge commit.
   - Title it `s39` and click **Publish release**.
4. **Add this handoff to the Project.**

## 7. Next session: start here

1. **Clone:** `git clone https://github.com/BetterToBest/NormativeEvaluation /home/claude/neec`.
2. **Verify:**
   - Tags `s34` to `s39` exist.
   - 236 tracked files.
   - The digest below, over every tracked file except this handoff, equals `d5985aa1dd94f95f7a108cdc9d51c52e`.
   - Harness v14 runs 82 of 82, byte-identical to `run_all_checks_output.txt`.
   - The latest Actions run on `main` passed.

   If the Session 39 update has not been applied, ask the owner to finish section 6 first (the zip is in the
   Session 39 conversation).

```
import hashlib, subprocess
h = hashlib.md5()
for f in sorted(x for x in subprocess.check_output(["git", "ls-files"]).decode().split("\n") if x):
    if f != "NEEC_Project_Handoff_39.md":
        h.update(f.encode() + b"\0" + hashlib.md5(open(f, "rb").read()).digest())
print(h.hexdigest())
```

3. **Then** section 8, item 3.

## 8. Next steps, in priority order

1. **Owner:** section 6.
2. **Next session:** verify (section 7).
3. **The rescoring pass, part (b), continued**, as a new record part with its own script (for example
   `NEEC_Rescoring_s40.md`, importing parts (a), (b1) and (b2) for cumulative consequences):
   - **C1.1 (9 units: NSD, CPS, MS, MMT, UBI, DG, FALC, PE, CCO)** first. Its stress clause (≥85% under stress
     testing) is shown by no audited unit. CCO-PTF-CIP-SZH's rationale says "98% poverty elimination in modeling";
     under part (b1)'s decision 3.2, test it against the pinned engine (`harness.js` at `compassionism-simulation`
     `cd0ceec`): Session 38's reference run reduced wealth poverty from 71.4% to 15.3% (about 79%) and BLEI poverty
     from 70.5% to 12.6% (about 82%). Read those against clause 1 at the modelling tier, and design a stress run for
     clause 2 within the engine's own parameters, as decision 3.2 requires.
   - Then C1.4 (2), C2.1 (5), C2.5 (10), C3.2 (4), C3.5 (2), C4.1 (8), C4.2 (6), C4.3 (6), C4.4 (4), C4.5 (3), C5.2
     (4), C5.4 (2) and C5.5 (2), criterion by criterion.
   - Hold designs' modelled figures to protocol 4.1 and apply parts (a), (b1) and (b2)'s readings alike.
4. **Parts (c)–(e)**, then apply the whole pass by generator, as in Handoff 37, section 8 item 4 (pin the corpus,
   regenerate the corpus, CSV, README and Appendix A.4, recompute the changed flag registers, **replace the five
   anchor examples of section 2.3(3)**, restate the protocol's corpus statements, and give the claims and protocol
   verifiers and the three rescoring scripts successors).
5. **Step 5 → Report v2.0 and Paper v2.0**, as Handoff 36 section 8 item 4 describes, now also covering the
   corrections of all three rescoring records.
6. **Pages site and Hub**; **second pilot**; **git tags and Visual Suite v3**, as in Handoff 36, section 8, items 5–7.

## 9. Known limitations (stated, not hidden)

1. This group is one scorer's re-estimation on evidence located in one session. "Not shown" means no evidence was
   located, not that the clause fails. Seven of the sixteen units are flagged, six toward 1.0 and one toward 0.5.
2. **Reading 3.1 is demanding for configured economies** and draws partly on the corpus's own amended scoring, so
   C5.1 is not independent of the criteria it cites. Every configured economy it decides is flagged toward 1.0.
3. **Reopening conditions.** CCO-PTF-CIP-SZH's C5.1 reopens if a scoring document cites twenty-year precedents for
   four of its five components. Handoff 38's reopening conditions stand (Nordic Social Democracy's C2.3;
   CCO-PTF-CIP-SZH's C3.4).
4. Handoff 38's limitations 3–4 stand.

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
- The design's papers index labels PTH, SZH and CIP "v0.9, Working Model" and CCO and PTF "v1.0 Draft". Those labels
  describe the design documents' maturity, not the existence of precedents; no score rests on them.
- Scratch before insert; programmatic verification over visual checking; generate, don't transcribe. Scripts find
  inputs beside themselves, print file names only, and are deterministic.
- Decisions are Claude's under the delegation. Record them with reasons, flag substantive changes, distinguish
  corrections from optional polish, say plainly when a file does not exist, and prefer precise, defensible
  language.
- Give the owner click-by-click steps for anything in GitHub. If the chat disconnects, the owner refreshes; a
  completed reply will be there, and "continue" resumes otherwise.
