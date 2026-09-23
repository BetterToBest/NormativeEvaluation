# NEEC Project Handoff 37

**Session 37 · 2026-09-22 · Owner: Duke Johnson · Scorer and engineer: Claude**
**Predecessor:** Handoff 36 (in the Project and the repository). This handoff supersedes its sections 6–11.

Session 37 verified the Session 36 repository and did part (a) of the rescoring pass (Handoff 36, section 8 item
3): the **33 stated-shortfall 1.0s**, re-estimated clause by clause on cited evidence. **Two stand; 31 become
0.5 (15.5 points); no failure count or tier changes.** Nothing is applied yet: the record is scratch, and the
corpus, CSV and scoring documents change only when the pass ends (protocol 10.1–10.3). The harness is at version
12, **80 of 80 checks passing**, byte-identical on a second run and in a fresh clone.

---

## 1. Session-start checks

- **Repository.** `main` at `1b595c1` (the merge of pull request #3, a true merge commit): 222 tracked files, all
  mode 100644; digest `2f431ae6d8e118d80ba0476a16aa3002` (exact match); harness v11 ran 79 of 79, byte-identical
  to its capture. Handoff 36 in the repository is byte-identical with the Project's copy.
- **Tags.** `s34` → `ecdd095`, `s35` → `4be59a5`, `s36` → `1b595c1`, all true merges. Handoff 36's open item is
  closed.
- **Actions.** Run 11 on `main` (the merge of pull request #3) completed successfully; the badge reads passing.
  The REST API was rate-limited, so the Actions page was read over HTTPS.
- **Attachments.** The seven CSV files attached to the opening message arrived empty again; the repository
  copies were used.

## 2. What changed

### 2.1 The rescoring pass, part (a) (`NEEC_Rescoring_s37.md`, `rescoring_s37.py`)

Each of the 33 units has an estimate for every clause of its Pass Threshold, in Appendix B's order, with a status
(cleared, short, not shown, out of reach, moot) and a source. Evidence came from web search, the entries' own
scoring documents, and, for CCO-PTF-CIP-SZH, the design's own published plans (`BetterToBest/research-hub` at
`8e8a6ba`; `BetterToBest/compassionate-meritocracy-plan`).

**Standing (2):**
- **CCO-PTF-CIP-SZH C5.2**, on the design's own documents: a 7-phase roadmap, a 3-month national launch plan,
  milestones, resource figures and a risk-mitigation section.
- **Sovereign Wealth Fund Statism C3.4**, on Norwegian primary sources: the equity share moved 40% → 60% → 70%,
  and the 2017 decision came eleven weeks after Norges Bank's advice. It is flagged, with 0.5 as the alternative.

**Falling to 0.5 (31).** Among them:
- Nordic Social Democracy, five units (2.5 points; 3rd → 5th).
- MMT + Job Guarantee, three units (1.5).
- Universal Basic Income, three units (1.5; 8th → 12th).
- CCO-PTF-CIP-SZH C3.1. The design's own roadmap specifies a fixed 20% crisis increase, below the threshold's
  1:1 example.

**Consequences (computed, not applied).**
- CCO-PTF-CIP-SZH keeps first place (24.5 → 24.0).
- Dominance pairs go from 14 to 15 and the frontier from 12 to 11 entries.
- 101 D28 units remain for part (b), with a textual bound of 50.5 points.

**Flag registers of eight entries change.** Five flags are added: Status Quo C5.1 → 1.0; Centrally Planned
Socialism C4.5 → 0.0; Libertarian Minarchism C4.5 → 0.0; SWF C3.4 → 0.5; Ostrom C3.4 → 1.0. Three are removed
(Singapore C3.4, Qatar C5.3, Islamic finance C3.4), because their alternative is now the score. Their
enumerations are recomputed when the pass is applied.

### 2.2 Decisions under the delegation (record, section 3)

1. **Part (a) scores 1.0 or 0.5, never 0.0.** Two units that arguably meet a whole-criterion 0.0 condition (LM
   C4.5, CPS C4.5) are scored 0.5 and flagged with 0.0 as the alternative.
2. **D31, MMT + Job Guarantee's environmental work is in.** Sources: Tcherneva 2007, Levy Economics Institute
   Working Paper 517; Tcherneva 2021, on the job guarantee as the Green New Deal's social arm. C4.2's four
   clauses are therefore within reach, superseding Session 35's reach coding. The unit is 0.5, not a possible
   0.0. A scope scenario counts the work out.
3. **D31, MMT's social housing stays out.** No source was located; the score is unchanged either way.
4. **Eight clause readings are fixed for part (b).** They cover C1.3 clause 2, C2.3 clause 1, C2.4, C3.1 clause 2
   (its step-versus-scaling question left open for part (b)), C3.4 clauses 2 and 4, C5.1 clause 2, and C5.2.
5. **C5.2's definition embeds CCO's own pathway text.** It moves out of the definition at Step 5, under D19; the
   Pass Threshold is unaffected.

### 2.3 Corrections found (not polish; record, section 6)

These land in Report v2.0.
- Report v1.6's CCO C3.1 "50%" is in no published CCO document located; the design says 20%.
- NSD C2.4's "65-75% voter turnout" understates recent turnouts (77.2–84.2% in four countries, 68.5% in Finland).
- NSD C2.3's "35-45%" and UBI C2.1's "65-75%" are unsourced.

### 2.4 Other files

- **`run_all_checks.py` v12**: check [80] appended; nothing else changed. Output differs from v11 only in the
  count lines, [74]'s README MD5 and the new entry.
- **`README.md`** (via `build_readme.py`, unchanged): only the check count changes, from 79 to 80.

## 3. Files

The repository update is **7 files** at the zip's top level, `NEEC_repository_s37.zip`:

| File | MD5 (first 8) | Status |
|---|---|---|
| `NEEC_Rescoring_s37.md` | `77d6ed04` | new (the pass's record, part (a)) |
| `rescoring_s37.py` | `88fe5ee2` | new |
| `rescoring_s37_output.txt` | `634c4587` | new |
| `NEEC_Project_Handoff_37.md` | (this file) | new |
| `run_all_checks.py` | `996d1fc9` | replaced (v12) |
| `run_all_checks_output.txt` | `f422e080` | replaced |
| `README.md` | `0dd1c7df` | replaced |

**The Project** gets this handoff only (GitHub is canonical, D27(b)).

## 4. Pins

- `rescoring_s37.py` reads the corpus in force and the R4 audit's register (`r4_audit_s35.py`). It pins nothing.
- When the pass is applied and the corpus changes, its population checks keep passing (they read the audit's
  register). Its consequence figures and the record's generated tables will then need a successor, as
  `verify_protocol_s36.py` does. The pass's generator should therefore pin `neec_corpus.json` as it stood
  (`_s37_snapshot`) and point this check at the snapshot.
- Unchanged: Handoff 36 section 4's pins.

## 5. Decision register

The protocol's section 13 (D2–D31) is unchanged. The decisions of section 2.2 are recorded in the rescoring record
and join the protocol's register when the pass ends and the protocol is restated. Nothing awaits the owner.

## 6. Updating the repository (owner)

1. **Upload the zip**: on the repository page, **Add file → Upload files**, drop in `NEEC_repository_s37.zip`,
   **Commit changes** (to `main`).
2. **Paste to Claude Code:**

```
Session 37 update. NEEC_repository_s37.zip is now on main. Please:
1. Pull main and create a new branch from it.
2. Unzip NEEC_repository_s37.zip into the repository root, overwriting (7 files: 4 new, 3 replaced), then delete the zip and stage everything (git add -A).
3. Confirm git ls-files shows 226 files.
4. Run: python3 run_all_checks.py > /tmp/out.txt ; cmp /tmp/out.txt run_all_checks_output.txt
   Expect "SUMMARY: 80 passed, 0 failed, 0 skipped (of 80)." and cmp reporting no difference.
5. Run the fingerprint snippet in section 7 of NEEC_Project_Handoff_37.md; expect 53fd3c82875610d5d3fa8d38d7f168e8.
6. Commit "NEEC Session 37: rescoring pass part (a), the 33 stated-shortfall 1.0s (harness v12)", push, open a pull request into main, and merge it with a merge commit if you are able to (otherwise tell me).
7. Tag the merge commit s37 and push it (git push origin s37), then run git ls-remote --tags origin and show me the result. If pushing the tag is refused, say so plainly.
8. Confirm the harness workflow passed on main.
```

3. **If Claude Code cannot push the tag**, create it on GitHub:
   - Go to **Releases → Draft a new release → Choose a tag**, type `s37`, and click **Create new tag: s37 on publish**.
   - Under **Target → Recent commits**, pick the Session 37 merge commit.
   - Title it `s37` and click **Publish release**.
4. **Add this handoff to the Project.**

## 7. Next session: start here

1. **Clone:** `git clone https://github.com/BetterToBest/NormativeEvaluation /home/claude/neec`.
2. **Verify:**
   - Tags `s34` to `s37` exist.
   - 226 tracked files.
   - The digest below, over every tracked file except this handoff, equals `53fd3c82875610d5d3fa8d38d7f168e8`.
   - Harness v12 runs 80 of 80, byte-identical to `run_all_checks_output.txt`.
   - The latest Actions run on `main` passed.

   If the Session 37 update has not been applied, ask the owner to finish section 6 first (the zip is in the
   Session 37 conversation).

```
import hashlib, subprocess
h = hashlib.md5()
for f in sorted(x for x in subprocess.check_output(["git", "ls-files"]).decode().split("\n") if x):
    if f != "NEEC_Project_Handoff_37.md":
        h.update(f.encode() + b"\0" + hashlib.md5(open(f, "rb").read()).digest())
print(h.hexdigest())
```

3. **Then** section 8, item 3.

## 8. Next steps, in priority order

1. **Owner:** section 6.
2. **Next session:** verify (section 7).
3. **The rescoring pass, part (b).** The other 101 units, criterion by criterion, applying the record's section 3.4
   readings. Extend `rescoring_s37.py`'s successor with them, as a new record part (for example
   `NEEC_Rescoring_s38.md` with its own script), rather than editing Session 37's record. Suggested order:
   - First, the criteria whose readings are fixed: C3.4 (11 units), C5.3 (8), C2.4 (6), C1.3 (3) and C2.3 (6).
   - C5.1's second clause on its eleven remaining 1.0s.
   - C3.1, deciding the step-versus-scaling question by protocol 4.2 with UBI, MMT and the designs.
   - Then the rest.
   - Hold designs' modelled figures to protocol 4.1.
   - Read CCO's own published documents, as part (a) did.
4. **Parts (c)–(e):**
   - (c) the 131 mechanism-class 0.5s against D29, Ostrom's C4.3 first.
   - (d) D31's source for Ostrom's community land trusts.
   - (e) the Islamic finance and Ostrom quoted thresholds restated.
   - Then apply the whole pass by generator:
     - pin the corpus as `_s37_snapshot`;
     - regenerate the corpus, CSV, README and Appendix A.4;
     - recompute the changed flag registers;
     - restate the protocol's corpus statements;
     - give the claims and protocol verifiers (and this script) successors.
5. **Step 5 → Report v2.0 and Paper v2.0**, as Handoff 36 section 8 item 4 describes. It now also covers the
   corrections of the record's section 6, including moving C5.2's CCO-specific text out of the definition.
6. **Pages site and Hub**; **second pilot**; **git tags and Visual Suite v3**, as in Handoff 36, section 8, items 5–7.

## 9. Known limitations (stated, not hidden)

1. Part (a) is one scorer's re-estimation on evidence located in one session. "Not shown" means no evidence was
   located, not that the clause fails. Five units are flagged in the direction a careful second scorer could take.
2. **Nordic Social Democracy's C2.3 has a reopening condition.** Eurostat's database (EU-SILC `ilc_scp07`, and
   the well-being module) was not reachable here. If both clear their bars, the unit returns to 1.0.
3. **CCO-PTF-CIP-SZH's units were read on the owner's own documents.** Protocol 4.1 makes them the evidence
   for what the design specifies, and the second pilot is the independent test (record, section 7).
4. Handoff 36's limitations 1–4 stand. They cover D30's assignments, D29's reach (131 scores read in part (c)),
   R8's synthetic test, and Handoff 35's items.

## 10. Hub text

The suggested text in Handoff 36, section 10, is usable now that `main` holds the corpus: it says "in
preparation", and the README says the totals are provisional. Adding it to the Hub is the owner's edit whenever
he chooses. The fuller integration (the Pages site, the root domain's manifest, `research-index.json`,
`llms.txt` and `sitemap.xml`) stays at item 6.

## 11. Standing working notes

- Shell is `sh` (no `time`, no process substitution); `git` is available. Maximum effort; accuracy over speed.
- `github.com` and `raw.githubusercontent.com` are reachable from the sandbox. The web-fetch tool opens only URLs
  returned by a search. `bettertobest.github.io`, `ec.europa.eu` and `db.nomics.world` are not reachable from
  bash, so read the Hub's sources by cloning `BetterToBest/research-hub`.
- Scratch before insert; programmatic verification over visual checking; generate, don't transcribe. Scripts find
  inputs beside themselves, print file names only, and are deterministic.
- Decisions are Claude's under the delegation. Record them with reasons, flag substantive changes, distinguish
  corrections from optional polish, say plainly when a file does not exist, and prefer precise, defensible
  language.
- Give the owner click-by-click steps for anything in GitHub.
