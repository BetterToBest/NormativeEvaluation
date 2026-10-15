# NEEC state

**What is true now.** Rewritten by every session before its pull request (`CLAUDE.md`); the handoff says what
changed, this file says what holds. Last rewritten by Session 61 (group 2.8, C4.3 read) (2026-10-15). It consolidates the standing notes and
open items of Handoffs 43 to 58, which no longer need to be read for them.

## Position

- **Stage 2 of the plan** (the rescoring pass on the v2.0 criteria), in progress. Group 2.1 done (Session 51); Session
  52 built the shared module and the triage; group 2.2, C1.2a re-read as class M, done (Session 53,
  `NEEC_Rescoring_s53.md`): all 23 units read, no entry clears C1.2a, five fall, one rises, no tier changes. **Group
  2.3, C1.3 re-read as class M, done (Session 54, `NEEC_Rescoring_s54.md`)**: the 20 units not yet re-estimated read;
  only Centrally Planned Socialism clears C1.3 (flagged); five designs fall from 1.0 to 0.5; no failure count or tier
  changes. **Group 2.4, C3.5 read as class I, done (Session 56, `NEEC_Rescoring_s56.md`)**, the first class I group:
  four rise from 0.0 to 0.5, Universal Basic Services falls from 0.5 to 0.0; no tier changes. **Group 2.5,
  CCO-PTF-CIP-SZH's nine simulation units re-read on v5.6.0, done (Session 57, `NEEC_Rescoring_s57.md`)**: C3.2 fell from
  1.0 to 0.5 (decision 57.7), which **the owner reversed (decision 58.1, ledger d37): C3.2 is 1.0**, applied as a part of
  the pass of its own, "58.1" (`owner_s58.py`); the other eight hold, and the owner has **paused** S57-3.3 (decision
  58.2, ledger d38). **Group 2.6, C5.2 re-read as class M, done (Session 58, `NEEC_Rescoring_s58.md`)**: the 16 units
  not yet re-estimated read on part (b9)'s precedent test; Integral rises from 0.0 to 0.5 on the design's own white paper
  (v0.1, December 2025), flagged toward 0.0; Sovereign Wealth Fund Statism rises from 0.5 to 1.0 on Norway's and
  Timor-Leste's deployments, flagged toward 0.5; the other 14 hold (Centrally Planned Socialism and Fully Automated
  Luxury Communism at 0.0). **Integral moves from Partially to Potentially Adequate**, the pass's first tier change in
  stage 2's groups. **Group 2.7, C1.4 read as class I, done (Session 60, `NEEC_Rescoring_s60.md`)**, on the cache
Session 59 built: no unit's sources state either clause in any displacement scenario, so none is 1.0; Universal Basic
Income falls from 1.0 to 0.5 (a correction, as parts (b4) and 2.5 read the other 1.0s); 19 hold, five at 0.0; Integral
holds at 0.5 on its white paper, so first place stays shared; no tier changes. **Group 2.8, C4.3 re-read as class M,
done (Session 61, `NEEC_Rescoring_s61.md`)**: the 16 units not yet re-estimated read on the measure v2.0 names, the four
configured economies on their household surveys (cached in `evidence_cache/C4.3/`); no unit shows either clause, so none
is 1.0; Status Quo falls from 0.5 to 0.0 (a correction: on the Census series the gap between Black and Asian households
is above 50% and wider than in 2002, and the Black-white gap has stayed between 35% and 45% since 1972), which also
resolves the 0.0 anchor's inconsistency logged since Handoff 30; 15 hold, three at 0.0 (LM, CN, QA); Singapore's clauses
are short on its 2025 survey (the Malay gap widened) and it holds at 0.5; Integral holds at 0.5 on its white paper, so
first place stays shared; Status Quo gains a failure, no tier changes. The next group is named below.
- **Landing:** by pull request and the owner's merge (W9, decision 52.3). The session opens the pull request; `harness.yml`
  checks it; the owner merges; `land-session.yml` reruns the checks on `main` and tags each `NEEC Session <n>` commit.
- **Criteria:** v2.0, 29 criteria in `criteria.json`; protocol draft.9. Published scores remain on 26 criteria until
  stage 3 applies the pass by generator.
- **Simulation pin (decisions 57.3, 57.5; 52.9's freeze superseded):** `BetterToBest/compassionism-simulation` at
  `d10ed6e` (v5.6.0), `harness.js` md5 `84be3bc9`, `index.html` md5 `2e1cc8c7`; its engine is the v5.6 release's.
  Groups 2.1 to 2.3 read `5a7a7b1` (v4.20) and stand as the pass's history. **Research Hub pin:** `8e8a6ba` (its later
  commits, to `1f7781d` on 2026-10-15, move only the simulation's replication page and README and the wiki index; no
  design paper changed).
- **Harness:** v34, 108 checks, byte-identical in the container (Python 3.13 in Sessions 56 to 61; 3.11 before) and
  checked by `harness.yml` on 3.12.
- **Site:** live at https://bettertobest.github.io/NormativeEvaluation/, scores gated (`site/config.json`
  `scores.publish` false, decision 49.1).
- **Provisional standing on the published 26-criterion structure** (not for publication before stage 3): first place
  is shared at 14.5/26 by CCO-PTF-CIP-SZH (published 24.5) and Integral; Participatory Economics 14.0; Nordic Social
  Democracy 13.5. Seven entries are Potentially Adequate (CCO, PE, NSD, INT, DG, MS, GEO). Six units not yet read
  could each change who is first (NSD C2.5, PE C2.5, PE C4.5, CCO C4.5, INT C1.1, INT C3.4; `triage_s52_output.txt`,
  section 2).

## Next work, in order

1. **C3.1 Crisis Response Capacity's evidence cache, in a Sonnet 5.5 session at medium** (mechanical: C3.1 is class I,
   16 units in play, 3 tier-capable, and its readings need the cache first, as Session 59 built C1.4's;
   `evidence_cache_s59.py` is the model). Then **group 2.9, C3.1 read as class I, in an Opus 5.5 session at high**
   (`rescoring_s60.py` is the model for a class I group; `rescoring_s61.py` for one reading national surveys).
2. **Then the groups in the triage's order** (rerun after each group): C3.1, C1.1, C4.2, C4.1, C2.1, C2.3, C2.4, C4.4,
   C4.5, C2.5, C3.4. The class I groups (C3.1, C1.1, C2.1, C2.4, C2.3) need their evidence cache first, in a Sonnet 5.5
   session at medium. Groups already planned partly (C4.4's 17, decision 48.3; C4.1's four part (b6) units on its debt
   clause) are read within their criterion's group. `rescoring_s51.py`'s unit supersedes part (b3)'s C1.1. Write each
   group as groups 2.2 to 2.7 were: a script on `pass_common.py` holding the readings (`U(...)`), its group-specific
   checks and generated tables (`rescoring_s58.py` is the model for a class M criterion, `rescoring_s60.py` and
   `rescoring_s56.py` for a class I one), a record, `PARTS` extended, the harness given the new files. Do not touch
   earlier scripts or their captures. C1.1's group reads the configurations' baseline poverty on the Societal Poverty
   Line, which group 2.7 did not need (reading 3.1).
3. **The 69 new units** (C2.6, C3.6, C4.6; 23 each): no score exists, so none can be carried forward; they change
   every entry's failure count and total on the 29. Done after the class I and M groups, with the evidence cache.
4. **Carry-forward (decision 52.7):** the triage now names six units that could change no failure count, tier or rank
   on their own (CCO C4.5, CN C2.5, CPS C2.5, IF C4.5, SG C2.5, UBS C4.5); with first place shared, CCO C4.5
   could still decide who is first alone, so read it rather than carry it. Reading them is cheap inside their
   criterion's group; any left unread is listed in Report v2.0 and the Paper.
5. **CCO-PTF-CIP-SZH's paused item (decision 58.2):** when the design's last units are read (its C4.5 is the one left in
   play), list every CCO-PTF-CIP-SZH reading together for the owner, as the owner asked under d38, with the owner's d37
   reasoning (the backing by creative output) noted against each unit it could bear on (C1.2a first).
6. Stage 3 (apply the pass by generator; `scores.publish` true; Report v2.0 Part I from per-unit rationales, decision
   52.8, with the clauses group 2.6 and part (b9) left not estimated; C1.2a's 1.0 band drops its example, as C1.1's did;
   C3.5's 0.0 band takes its examples from the units at 0.0 after group 2.4; C5.2's bands take theirs from the units
   after group 2.6), stage 4 (Report and Paper v2.0; the Paper discloses the simulation overhaul, decision 52.9, and
   that Integral was read on its white paper of December 2025), stage 5 (Paper PDF from a committed build script).

## Decided (Session 61, under the delegation; `NEEC_Rescoring_s61.md`, section 3)

No owner's answer was waiting (d38 still paused). **61.1** a method choice: 0.0 and 0.5 on C4.3 are drawn by protocol
2.1's three conditions read on the measure: no mechanism bearing on a gap between groups (group-directed, or a flow whose
form narrows percentage gaps); the system excludes the concern (its logic rules out correction, or it allocates to the
most advantaged group); or, on a long series, a gap far above 20% that does not narrow with no pathway in the system's
own logic. **61.2** Status Quo's C4.3 0.5 → 0.0 (a correction, on Census Table H-5; flagged toward 0.5). **61.3** the
designs' and mechanisms' units held (11 at 0.5, LM at 0.0); published flags' 1.0 sides lapse (GEO, MC, SWF, UBS); their
0.0 sides kept (GEO, MC, SWF, IF, OS); Stakeholder Capitalism flagged toward 0.0. **61.4** Integral's 0.5 held on its
white paper (protected-category adjustments and equity-drift review; no gap projected). **61.5** the gender and wealth
axes not read on a survey (another axis decides each clause read). Singapore holds at 0.5 with both clauses short and
its flag toward 0.0 kept (reading 3.4); China and Qatar hold at 0.0 (reading 3.5); two kept flags could change a tier
(GEO, IF toward 0.0).

## Decided (Session 60, under the delegation; `NEEC_Rescoring_s60.md`, section 3)

No owner's answer was waiting (d38 still paused). **60.1** a method choice: C1.4's clauses are levels in each of three
displacement scenarios on the measure v2.0 names, shown only by a model of the scenarios; a rationale's judgement of what
a system "can maintain" is not an estimate; final consumption expenditure includes general government's, so in-kind
provision counts toward demand. **60.2** Universal Basic Income's C1.4 1.0 → 0.5 (a correction: silence is not
clearance, as for FALC, PE and CCO). **60.3** the fourteen 0.5s held (Universal Basic Services' demand-side finding not
borne out on the measure; Qatar's buffer covers part of the population). **60.4** the five 0.0s held; Status Quo and
Stakeholder Capitalism flagged toward 0.5 and Singapore toward 0.0 on an open peer question (a time-limited jobseeker
payment counted as a buffer for Singapore and not for the United States); no flag could change a tier. **60.5**
Integral's 0.5 held on its white paper (essentials accessible "regardless of age or ability", but access "emerges from
participation"; no model of the scenarios). Islamic Finance's and Ostrom's published flags kept.

## Decided (Session 58; `NEEC_Rescoring_s58.md`, section 3)

From the owner (ledger, 2026-10-15): **58.1** d37 answered with the owner's own option: "Keep CCO at one until an
empirical study shows that it doesn't hold up in real world data"; decision 57.7 is reversed and CCO-PTF-CIP-SZH's C3.2
is 1.0, applied as part "58.1" (`owner_s58.py`), flagged toward 0.5 on group 2.5's reading; **58.2** d38 paused: "wait
until all the CCO readings are in and I'll push back on some of them all at once". Under the delegation (decision 57.2;
no CCO-PTF-CIP-SZH unit read): **58.3** a method choice, C5.2's scope applied (a deployment resting on a seizure of power
by force is not a precedent; staged needs four dated stages, a stalled deployment is short; rapid counts the
deployment's own span to operation, and a deployment that collapsed shows the pace only; 0.5 against 0.0 under
protocol 2.1 and decision 53.2); **58.4** Integral's C5.2 0.0 → 0.5 (a correction, read on the design's white paper;
flagged toward 0.0); **58.5** Sovereign Wealth Fund Statism's C5.2 0.5 → 1.0 (a correction; flagged toward 0.5);
**58.6** Centrally Planned Socialism's (flagged toward 0.5) and Fully Automated Luxury Communism's 0.0 held; **58.7** the
other twelve held at 0.5 (Georgism's staged clause now short; Mutual Credit's and Ostrom's register flags toward 0.0
kept); **58.8** tooling: an owner's decision that changes a score is applied as a part of the pass of its own.

## Decided (Session 57; `NEEC_Rescoring_s57.md`, section 3)

From the owner (2026-10-14): **57.1** the ledger's answers: the default confirmed for d1 to d16 (W1 to W10, 48.3, 49.2,
49.3, 49.5, 49.8, 49.9, 50.2, 50.4, 50.5), d18, d23, d25, d27, d28, d30, d31 and d32 to d36, each now settled for v2.0;
the CCO-PTF-CIP-SZH items d17, d19 to d22, d24, d26 and d29 taken up by 57.3 and group 2.5 (S50-3.4's C5.2 stays 0.5
with its flag: its reopening condition is a deployment, which no simulation meets). **57.2** a standing rule: score
changes for entries other than CCO-PTF-CIP-SZH need no owner confirmation; they are decided under the delegation and
listed here; CCO-PTF-CIP-SZH's score changes still go to the ledger. **57.3** read the overhauled simulation now
(supersedes 52.9 and d26's "in version 2.1"); a later version is read when the owner releases it for scoring; Paper
v2.0 states the version read and that the simulation is still being revised. **57.4** the owner's note on C1.3's tenure
read: the design's tenure forms are features the model does not yet carry; passed to the simulation's maintainers.
Under the delegation: **57.5** the pin to `d10ed6e`; **57.6** a clause clearing only at a backing share the design does
not state is not shown, both ends reported (stands for the design's units other than C3.2, which 58.1 decides);
**57.7** CCO-PTF-CIP-SZH's C3.2 1.0 → 0.5 (reversed by the owner, 58.1); **57.8** C3.4's adjustment run repeated on a
collapse test fixed before the run (clause 4 short, flagged toward 1.0); **57.9** the other seven units held; **57.10**
the shared module and the triage name a shared first place.

## Decided (Session 56, under the delegation; `NEEC_Rescoring_s56.md`)

56.1 the reading of C3.5's clauses on v2.0's indicators (clause 1 from a dated record the scoring document names;
clause 3 the audit office's own rate on its stated basis, 70% clearing; clause 4 the IMF's total implicit subsidies,
2022, cleared under 10% of GDP; two alternatives carried in flags); 56.2 Libertarian Minarchism's C3.5 0.0 → 0.5 (a
correction); 56.3 Nordic Social Democracy's and Stakeholder Capitalism's 0.0 → 0.5 on the named indicators, Status
Quo's 0.5 held; 56.4 Universal Basic Services' 0.5 → 0.0 (a correction), Universal Basic Income's and MMT + Job
Guarantee's 0.0 held; 56.5 China's 0.0 held, Qatar's 0.0 → 0.5, Singapore's 0.5 held. Carried into the criteria record
at its next amendment, with 54.1 to 54.3, 53.1 to 53.3, 52.11 and 52.12.

## Decided (Session 54, under the delegation; `NEEC_Rescoring_s54.md`)

54.1 the reading of C1.3's two clauses (a 5-year rate, or a lower bound from the channels of displacement closed; costs
of households at 80% of the median as a class, renters at market prices included; a design's description is not a
projection); 54.2 the design's C1.3 on its published model (the engine models no housing tenure; its distress proxy is
read as not shown, not short; the population is the whole society, not Public Trust Housing's fifth); 54.3 Centrally
Planned Socialism's C1.3 holds at 1.0 on a bound from the late-Soviet record, flagged toward 0.5. Carried into the
criteria record at its next amendment, with 53.1 to 53.3, 52.11 and 52.12.

## Decided (Session 53, under the delegation; `NEEC_Rescoring_s53.md`)

53.1 the reading of C1.2a's clause (70% of participants each reach the figure; the engaged-participants reading
flagged); 53.2 the form for class M units below 1.0 (0.0 only on a stated whole-criterion reason under protocol 2.1);
53.3 two corrections (Libertarian Minarchism's C1.2a 0.0 → 0.5; MMT + Job Guarantee's 0.5 → 0.0). Carried into the
criteria record at its next amendment, with 52.11 and 52.12.

## Decided (Session 52; the record's decisions 52.1 to 52.10)

Applied or adopted: W1 model routing, W2 shared pass module (built), W3 this file and self-contained handoffs, W4
checkpoints, W5 evidence cache (to build), W6 consequence triage (built), W7 Report Part I from rationales, W8 pin frozen
at `5a7a7b1` for v2.0, W9 landing by pull request, W10 chat path.

## Awaiting the owner

The owner answered every earlier item in the ledger (decisions 57.1, 58.1, 58.2). Under decision 57.2 only
CCO-PTF-CIP-SZH's score changes wait on the owner; other entries' changes are decided under the delegation. One item is
open, paused at the owner's request; it must be settled before stage 3, and nothing else waits on it.

| ID | Item | Recorded in | Ledger |
|---|---|---|---|
| S57-3.3 | CCO-PTF-CIP-SZH's other eight simulation units hold on v5.6.0 (C1.2a and C3.4 flagged toward 1.0; C3.4's clause 4 now short). **Paused by the owner** (decision 58.2) until all of the design's readings are in; Next work, item 5 | `NEEC_Rescoring_s57.md` 3.3 to 3.12 | d38 |

S57-3.9 (ledger d37) was answered: the owner kept C3.2 at 1.0 (decision 58.1).

**The ledger.** Every open item above is also a numbered decision in the owner's Project ledger
(https://claude.ai/artifact/KMdxWQ5KAefQVFxQA236pV, project "NEEC Research"; its id is in the Ledger column), written in
plain words with a default first, the other options after it, and a Reference entry (code = the ID) linking to the
extended description in the record. Ledger rule for sessions: `CLAUDE.md`, "The ledger", with decision 57.2.

Method choices Sessions 52 to 61 made that the criteria record does not yet carry (optional, not corrections; carried
into the record at its next amendment): 53.1, 53.2, 54.1 to 54.3, 56.1, 56.3, 56.5, 57.6, 57.8, 58.3, 58.8, 60.1, 60.3
to 60.5, 61.1, 61.3 to 61.5 (decisions 53.3, 56.2, 56.4, 57.7, 58.4, 58.5, 60.2 and 61.2 are corrections), 52.11, the design of `pass_common.py`; 52.12, the triage's reach assumptions and ordering
key (Handoff 52, section 4).

## Model routing (decision 52.4)

Opus 5.5 at high for judgment groups (class M re-reads, class I readings, the Report and Paper), xhigh only for groups
whose readings are contested; Sonnet 5.5 for mechanical sessions (the evidence cache, the stage 3 generator, the
site, the PDF, harness repairs). Judgment stays with Opus because the harness catches mechanical errors, not
misreadings. Only the owner can set the model; the handoff names it in its first line.

## Reopening conditions (CCO-PTF-CIP-SZH's units and the simulation)

A simulation version the owner releases for scoring (decision 57.3) reopens a unit only through these. Group 2.5
evaluated them on v5.6.0: only C3.4's was met (`rescoring_s57.py`, check [3]).

- **C1.1:** the model behind the papers' 98% is published and reproduces 98%; or a version reaches a 90% reduction in
  the reference run and 85% in the Adverse Environment, on the Societal Poverty Line.
- **C1.4:** an hours-displacement lever, with poverty under 8% and aggregate demand above 85% of baseline in the 30%,
  50% and 70% scenarios.
- **C3.3:** compound scenarios: degradation under 20% on every core function in at least three of four.
- **C3.2** (1.0 by the owner's decision 58.1, flagged toward 0.5): an empirical study showing that the backing of the
  currency by creative output does not hold in real-world data. A simulation version does not reopen it.
- **C3.4** (0.5, flagged toward 1.0): met on v5.6.0 and re-read (group 2.5, reading 3.11). Reopens if a version shows
  no seed collapsing on reading 3.11's test, or if the owner adopts the flag's reading of a collapse.
- **C1.2a** (0.5, flagged toward 1.0): v5.6.0 has a sourced consumption rule and shows 13.9% of participants at the bar
  in the reference run (91.1% at full backing); reopens if the reference run shows 70%; the owner's d37 reasoning on
  the backing may bear on it, under decision 58.2.
- **C1.3** (0.5, S54-3.3; the owner's tenure note, 57.4): a version of the model with housing tenure and a housing-cost line that
  shows 88% of all agents stable over 5-year windows and housing costs at or under 30% of disposable income at 80% of
  the median, in the reference run.
- **C5.2** (0.5, flagged toward 1.0, S50-3.4): a municipal pilot of the currency or the portal, or any deployment of
  either at scale. A simulation does not reopen it.
- Handoff 43 section 9.3's reopening conditions and limitations stand for the units they name.

## Standing notes

- **Site regeneration.** Any change to the site's inputs (`criteria.json`, the corpus, the CSV, the summary blocks,
  `NEEC_Criteria_v2_s45.md`, Paper v1.4, the A.4 weighting script, the WJP extract, `.github/ISSUE_TEMPLATE/`,
  `site/`) needs the chain: `build_criteria.py` in a temporary directory with its four inputs, copy `criteria.json`
  and the capture back, `build_site.py`, `build_readme.py`, then the harness. Every amendment of the criteria record
  changes `criteria.json`'s `record_md5` and the footer of 64 `docs/` pages. Never edit `docs/` by hand (check 93).
- **Python.** The cloud container's `python3` was 3.11 to Session 55 and 3.13 in Session 56; the workflows use 3.12; the
  harness reproduces on each. A
  check's summary line is shown in the harness with `show_summary=True`.
- **PDFs in the container.** `pypdf` fails on the container's `cryptography` build; `apt-get install -y
  poppler-utils` gives `pdftotext`. It does not persist between sessions.
- **Simulation runs.** Clone `BetterToBest/compassionism-simulation` at the pin (`d10ed6e`) beside the repository and run
  `node cco_sim_v56_checks_s57.js run ../compassionism-simulation/harness.js LO HI part_LO.json` for seeds 1-125,
  126-250, 251-375 and 376-500 (side by side, about 90 minutes on four cores), then `node cco_sim_v56_checks_s57.js
  report ../compassionism-simulation/harness.js part_*.json`; output must equal `cco_sim_v56_checks_s57_output.txt` (md5
  `cd2ec0c9`). v5 runners must set the test-bed's study profile (`applyNR6()`, `tbSetG(TB_PROFILE_G)`) before any run, or
  the programme rows do not reproduce the release; the runner checks reproduction before any table. Earlier runners
  (`cco_simulation_checks_s51.js` and the s53, s54 ones) run on `5a7a7b1`. The harness checks captures by digest and does
  not rerun JavaScript.
- **Jev.** Runs go through the owner's Composio connection (a claude.ai chat, or a cloud session with the connector
  attached). Pin the model in every request (`jev-1.13.0`); transcribe responses into a recorded file a script
  checks with no network call. A direct API call would need a TypeSafe key set by the owner as an environment
  secret, never committed. Optional; it changes no score.
- **Network.** Evidence work reads github.com, bettertobest.github.io, the World Bank, IMF, OECD, Eurostat, Freedom
  House, V-Dem, the WJP and similar hosts; without that access it can be recorded but not done.
- **Sources not in the repository** are identified in the record by name and md5 wherever a figure depends on them;
  every figure used is held in that session's script.
- **Workflow files** change only through the owner. `land-session.yml` requests a Pages build after each landing.
- **The Research Hub** is outside this repository; changes there are the owner's. Its roadmap (national launch in
  year 2) and its modelling paper (municipal pilots first) describe different staged pathways (Handoff 50).
- **Version 1** remains on the original Google Site; the owner has been asked to mark its scores as superseded (on
  the v1 home and report pages, the Medium article and the public visual-suite artifact) and to point the Research
  Hub's comparison entry at the v2 site. Whether that is done is not recorded here.
- **The simulation (decision 57.3).** Version 2.0 reads v5.6.0 for CCO-PTF-CIP-SZH's units. Its results turn on the
  backing share, which the design does not state; the pass reads both ends (57.6). The owner notes the simulation still
  has limitations and will be updated again: a later version is read when the owner releases it for scoring, through the
  reopening conditions above. Paper v2.0 states the version read, that the simulation is still being revised, and that
  the owner maintains both the design and the model. The record's section 8 lists what the units would need from the
  model.
- **Ties.** First place is shared after group 2.8, by CCO-PTF-CIP-SZH and Integral at 14.5; `pass_common.py` and
  `triage_s52.py` name a shared first place as shared (57.10). The triage's "could change none" screen reads an entry's
  own rank, so with a tie it can list a unit that decides who is first (Next work, item 4).
- **The shared pass module and the triage.** `python3 pass_common.py --selftest` reproduces group 2.1's tables from the
  parts before it; a new group is added to `PARTS` there, and the harness's S52 checks must then be given the group's
  files (v29 does this through `S54_FILES`; v34 through `S61_FILES`). An owner's decision that changes a score is
  applied as a part of its own (decision 58.8): `owner_s58.py` holds part "58.1"'s one unit, and the next group's
  script checks it. `python3 triage_s52.py` prints the
  consequence triage on the state through the last part (since Session 53 it reads the state from `PARTS` and holds no
  count of its own); after a group lands, replace `triage_s52_output.txt` and recapture the harness.
- **Wealth data used by group 2.2** (not in the repository; figures held in `rescoring_s53.py`): the Survey of Consumer
  Finances 2025 extract (`scfp2025excel.zip`, md5 c938318c; 2025 dollars; released 2026-10-09), Statistics Norway's
  2024 household wealth tables (10318, 10315), and World Bank WDI series retrieved 2026-10-14. The BLS API refused
  requests (its daily limit); FRED served CPI-U over HTTP/1.1 (`curl --http1.1`).
- **Sources used by group 2.3** (not in the repository; figures held in `rescoring_s54.py`): Childress, Kutuzov and
  Haase, *A Decade of Housing Reform in Russia* (Land Tenure Center, 2001; md5 babfbd70, from minds.wisc.edu); the IMF,
  World Bank, OECD and EBRD *Study of the Soviet Economy* (1991), chapter V.9, whose text refused retrieval (the census
  shares are quoted from the publisher's catalogue); JCHS's *State of the Nation's Housing 2025* via NLIHC's summary;
  Census P60-282; Eviction Lab's 2022 update. A new simulation runner, `cco_c13_checks_s54.js`, captured
  (`cco_c13_checks_s54_output.txt`, md5 30d131f0), runs in under a minute.
- **Sources used by group 2.6** (not in the repository; figures held in `rescoring_s58.py`, read 2026-10-15): Integral's
  *Technical White Paper v0.1* (integralcollective.io, December 2025, 345 pages; PDF md5 a6defc9a; `pdftotext` reads
  it), section 11, and the project's site (four communities registered, its Phase 1); NBIM's *The history* and the
  Norwegian Ministry of Finance's fiscal policy framework page; Timor-Leste's Petroleum Fund Law No. 9/2005, the Fund's
  2008 annual report and La'o Hamutuk's consultation notice (through search summaries); Norad's 2007 review of its
  Timor-Leste petroleum assistance; RSIS commentary CO18026 (2018); the NBER Digest's summary of Baker, Gruber and
  Milligan on Quebec's childcare; the ACT Treasury's tax reform page and The Canberra Times of 3 July 2026 (the Pegasus
  Economics review); Isaac and Franke on the Kerala campaign (publisher's summary). The P2P Foundation wiki refused the
  container (HTTP 403).
- **Sources used by group 2.8** (cached in `evidence_cache/C4.3/` by Session 61, digests held in `rescoring_s61.py`):
  the Census Bureau's CPS ASEC Table H-5 (xlsx md5 9086455a; seven series extracted), Singapore's General Household
  Survey 2025, Table 6.1 (PDF md5 051185ee, from singstat.gov.sg/files/), and five passages of Integral's white paper
  v0.1. Not cached: MOE's parliamentary reply of 7 May 2026 on the Tertiary Tuition Fee Subsidy, Executive Order 14173,
  and Qatar's 2012/13 household survey through press reports (psa.gov.qa did not answer). singstat.gov.sg's older
  `-/media/files/` links return 404; the Straits Times' static host does not resolve.
- **Sources used by group 2.7** (cached in `evidence_cache/C1.4/`; Session 59's by `evidence_cache_s59.py --fetch`, two
  added by Session 60 and held by digest in `rescoring_s60.py`): the World Bank's PIP methodology page, the WDI pages for
  final consumption expenditure (current and constant US$), the WDI source note for NE.CON.TOTL.KD (from
  api.worldbank.org), and five passages of Integral's white paper v0.1 (PDF md5 a6defc9a). The OECD national accounts
  page refused the container (HTTP 403). `evidence_cache_s59.py`'s check [2] now reports a failure, as expected once the
  group is read; it is not a harness check.
- **Figures used by group 2.5** (held in `rescoring_s57.py`): CPI-U annual averages 255.657 (2019) and 321.943 (2025;
  BLS, as the simulation's sources cite it; FRED's annual series omits 2025 for October 2025's missing month, and the 11
  published months average to it); the v5.6 release's published figures (`data/releases/v5.6.json` at `d10ed6e`).
- **Sources used by group 2.4** (cached in `evidence_cache/C3.5/` by `rescoring_s56.py --fetch`, digests held in the
  script): the IMF Fossil Fuel Subsidies Data 2023 update, country rows from the IMF Climate Change Indicators
  Dashboard's ArcGIS service (climatedata.imf.org serves the dataset; imf.org's own download link was not found); GAO's
  fiscal 2024 rate through Government Executive (gao.gov and files.gao.gov refuse the container, HTTP 403); China's
  audit rectification reports through Xinhua and China Daily (audit.gov.cn does not answer); Riksrevisionen's 2020 annual
  report on riksdagen.se. Singapore's AGO refuses (403) and Qatar's State Audit Bureau does not answer.
- **Class D count.** Earlier files say "25 units at 0.5" for class D; after decision 48.3 moved C4.4 to class M the
  count is 18 at 0.5 (C2.5 and C4.5), with 12 more at 0.0 that class D could also raise (`triage_s52_output.txt`).
