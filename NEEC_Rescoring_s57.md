# NEEC Rescoring Pass — Record, Stage 2, Group 2.5: CCO-PTF-CIP-SZH's Simulation Units on the Design's Published Model, v5.6.0

**Session 57 · 2026-10-14 · Scorer and engineer: Claude · Owner: Duke Johnson**
**Status: scratch (protocol 10.1). Parts (a) and (b) and groups 2.1 to 2.4 are `NEEC_Rescoring_s37.md` to
`NEEC_Rescoring_s56.md`; this record edits none of them.** No corpus file, score or scoring document changes until the
pass ends. Its changes are then applied by generator with pinned inputs and restated in place (protocol 10.2, 10.3;
decisions D12, D14), and until then the published totals stand, provisional as `README.md` says. Decisions taken here
are Claude's under the owner's delegation (Handoff 35, section 2), except those recorded from the owner's own answers
(section 3.1); each is recorded with its reasons, and the owner may reverse any of them. **CCO-PTF-CIP-SZH's score
changes wait on the owner's confirmation (decision 57.2).**
**Reproduce:** `python3 rescoring_s57.py` (harness check 105). It is written on the shared module (`pass_common.py`,
decision 52.5): the script holds the nine readings and the group's own checks, and the module computes the consequences
cumulatively with every part before it. It checks the captured output of the simulation runs by digest, finds there
every figure the readings quote, evaluates the reopening conditions from those figures, and checks that this record
contains its generated tables verbatim. The runs themselves: `node cco_sim_v56_checks_s57.js run HARNESS LO HI OUT.json`
in four parts of 125 seeds, then `node cco_sim_v56_checks_s57.js report HARNESS OUT1.json ... OUT4.json`, with HARNESS
the simulation's `harness.js` at `d10ed6e` (section 5); the harness does not run JavaScript.

---

## 1. What this group is

On 2026-10-14 the owner wrote that the Compassionism Simulation, CCO-PTF-CIP-SZH's published model, "has been updated
since its last full scoring", and asked the pass to review it and update the data set with any changes it makes,
noting that it still has limitations and will be updated again (decision 57.3). The pass had read the model at
`5a7a7b1` (v4.20) since group 2.1 and, by decision 52.9, would have kept that pin for version 2.0. Between v4.20 and
v5.6.0 (`d10ed6e`, 316 commits) the simulation was rebuilt. What matters for the design's units:

- **One engine, two paired runs.** Since v5.3 the engine is one copy, in `index.html`, which `harness.js` runs in Node.
  Each result is 500 paired runs (seeds 1 to 500) of the same 500 adults and their children, with the programme and
  with none, in three environments: Reference, Adverse (recessions, an automation wave, 2% outside inflation) and the
  Stress Test (the Adverse with weaker settings, 40% taking part).
- **Since v5.6 the run with no programme has today's safety net** (SNAP with its work rule, the EITC and the refundable
  Child Tax Credit), so every change is what the design adds to current US policy.
- **Prices are computed.** What the Source pays out, less any new output that backs it, is new money that moves the
  price level; essentials' prices also move with demand above capacity. Before v5.0 prices were an input.
- **People respond.** A labour response (one elasticity for every change in the return to work, one income effect per
  unconditional dollar) and, since v5.4, job loss and re-employment.
- **Households.** Adults live in households of the Census composition; children are counted.
- **The decisive unknown is the backing share** (`a`): how much of what the Source pays new output backs. The Hub names
  no tax that pays the Source, so the model's main result, the release row, takes none (`a = 0`); the simulation reports
  a sweep to `a = 1` ("H1"), where every dollar is backed.

**What this group does.** It moves the pass's simulation pin to `d10ed6e` (reading 3.2) and re-reads, on v5.6.0, the
nine units of CCO-PTF-CIP-SZH that rest on the simulation or that the simulation can now decide: C1.1, C1.2a, C1.2b,
C1.3 and C1.4, the domain-1 units the pass read on v4.20; C3.2 and C5.3, which group 2.1 carried because the model then
computed neither prices nor participation; C3.3; and C3.4, whose reopening condition (an endogenous price or behavioural
channel, with the adjustment run repeated) v5.6.0 meets. It runs the model itself (section 5), checks that the runs
reproduce the v5.6 release's published figures, and evaluates every reopening condition recorded for these units before
v5.6.0 existed (reading 3.12). It also records the owner's ledger answers and message as decisions 57.1 to 57.4.

**Outcome.** **C3.2 falls from 1.0 to 0.5**: the model's main reading shows the programme raising prices 50.8% a year,
and inflation stays under 3% only if new output backs every dollar the Source pays, which the design's sources do not
establish (reading 3.9). It is a CCO-PTF-CIP-SZH score change and **waits on the owner's confirmation** (decision 57.2).
The other eight units hold: C1.1, C1.2b and C1.3 stay short or not shown at either end of the backing sweep; C1.2a
clears only at full backing (not shown, flagged toward 1.0); C1.4 and C3.3 still cannot be run as the criteria define
them; C3.4's clause 4 moves from not shown to short on the test fixed before the run, flagged toward 1.0; C5.3 is
carried. Net −0.5 points; no failure count and no tier changes. **CCO-PTF-CIP-SZH falls to 14.0 and shares first place
with Participatory Economics and Integral** on the provisional 26-criterion standing.

## 2. How a clause is recorded, and the rule

As in part (a), section 2: each clause is cleared, short, not shown, out of reach or moot; a 1.0 stands only if every
clause is cleared or moot, and otherwise becomes 0.5 (D28, protocol 2.3); a clause-level gap never makes 0.0 (D28(f)).
The clauses are v2.0's (`criteria.json`; protocol draft.9, Appendix B). Every unit's clauses are restated in full here,
including those this group carries unchanged (C3.4's first three, C5.3's four), so that each unit is complete in this
record.

## 3. Decisions and readings

**3.1 The owner's decisions of 2026-10-14 (recorded first, as `CLAUDE.md`, Start, step 5 asks).** The owner answered
every open item in the Project ledger (project "NEEC Research", read at version 71) and sent a message with two further
decisions. Each is recorded here with its consequence.

- **57.1 (the owner's ledger answers).** The default was confirmed for d1 to d16 (W1 to W10; 48.3; 49.2, 49.3, 49.5,
  49.8, 49.9; 50.2, 50.4, 50.5), d18 (S51-3.2), d23 (S53-3.1), d25 (S53-3.6), d27 (S55-1), d28 (S54-3.2), d30
  (S54-3.4), d31 (S54-3.6) and d32 to d36 (S56-3.1, S56-3.3 to S56-3.6). *Consequence:* each of these is settled for
  version 2.0 and leaves `STATE.md`'s list of items awaiting the owner; no score changes, since each confirms what the
  pass already holds. Among them: C4.4's clause 1 keeps its definition (48.3); the site's navigation, the Thresholds
  page's paraphrases, the Replicate page's prompt design, the contributing guide and the visual suite stand (49.2 to
  49.9); Jev stays flag-only with its question design (50.2, 50.4); the blind replication after stage 3 uses a model
  outside the Claude family (50.5). For CCO-PTF-CIP-SZH's units the owner answered d17 (S50-3.4) and d19 to d22
  (S51-3.4 to S51-3.7) that the simulation has undergone major revision and another scoring round may be needed, d24
  (S53-3.4) "hold for the overhauled simulation", d26 to keep what the pass held and read the overhauled simulation in
  version 2.1, and d29 (S54-3.3) with a note on the design's housing tenure. Decision 57.3 takes up all of them; the
  note is read in 3.7.
- **57.2 (the owner's standing rule).** "I don't need to confirm any score changes to anything other than CCO."
  *Consequence:* from this session, a change to the score of any entry other than CCO-PTF-CIP-SZH is decided under the
  delegation, recorded with its reasons and listed in `STATE.md` as decided; it is not put to the owner in the ledger. A
  change to CCO-PTF-CIP-SZH's score, including one that follows from a method choice, still waits on the owner's
  confirmation and goes to the ledger. Method choices that change no CCO-PTF-CIP-SZH score are recorded the same way as
  other entries' score changes.
- **57.3 (the owner's message: read the updated simulation now).** "The simulation has been updated since its last full
  scoring, so you can review it and update the repo data set with any changes it might make, though there are still
  limitations and it will be updated again." *Consequence:* this supersedes decision 52.9 (W8, ledger d5: version 2.0
  frozen at `5a7a7b1`) and d26's "read the overhauled simulation in version 2.1" for CCO-PTF-CIP-SZH's units: the pass
  reads the simulation at `d10ed6e` (v5.6.0) in this group (2.5), ahead of group 2.6 (C5.2), which the triage had put
  next. The reopening conditions recorded for the design's units (`STATE.md`; Handoff 43, section 9.3) are applied to
  v5.6.0's figures (3.12). Paper v2.0 states the version read and that the simulation is still being revised, so a later
  version may move these units; a later version is read when the owner releases it for scoring, as here. The records of
  groups 2.1 to 2.3, read at `5a7a7b1`, are not edited: they are the pass's history, and this group's units supersede
  theirs for the units it re-reads.
- **57.4 (the owner's note on C1.3, d29).** Read in 3.7.

**3.2 The pin moves to v5.6.0.** *Decision (under 57.3):* the pass reads `BetterToBest/compassionism-simulation` at
`d10ed6e` (v5.6.0), `harness.js` md5 `84be3bc9`, `index.html` md5 `2e1cc8c7`. Its engine is the v5.6 release's: the
release file's manifest (`data/releases/v5.6.json`, commit `5bf5bcc`) gives the SHA-256 of `harness.js` and of the
engine block in `index.html`, and both match (`d10ed6e` changed the page's text, not the engine). The runner builds the
release row and its no-programme run exactly as `node harness.js testbed 500 release ref,adv,st --v54 --snab --slope`
does, and before any table is read it reproduces the release's published figures for the no-programme run, the release
row and H1 in all three environments (too little wealth, the share below the cost of living and programme inflation, and
the Reference wealth Gini). The Research Hub pin stays `8e8a6ba`: its commits since then (to 2026-10-03) move the
simulation's replication page to the simulation's own repository and rewrite its wiki entry; no design paper changed.

**3.3 How the design's model is read when its result turns on the backing share.** Most of v5.6.0's figures for the
design depend on `a`, which the design's sources do not state. The simulation's own reading takes `a = 0` and labels it
cautious ("Claude's reading of the design: the Hub names no tax that pays the Source, so the model treats what it pays
out as new money, except what new output backs"). *Reading:* a figure that clears a clause only at a backing share the
design's sources do not establish is **not shown**: the projection holds only under a favourable and untested condition
(protocol 2.1, as decision 53.2's form read C1.2a's saving rule). A figure short at both ends of the sweep is **short**.
The unit is flagged toward the alternative where full backing would clear it. *Alternatives rejected:* reading the
release row alone would make the scorer's choice of the simulation's cautious reading decide clauses the design's
sources leave open; reading H1 alone would credit the design with an output response no source quantifies. Both ends are
reported for every unit. The no-programme run is the comparator wherever a clause measures a reduction; it now includes
today's safety net, so a reduction is what the design adds to current policy.

**3.4 C1.1 on the Societal Poverty Line.** Computed per adult from the engine's disposable income, with the line
max($3.00, $1.30 + 0.5 × median) a day as in group 2.1 (the 2021 PPP intercept is not inflated to 2025 dollars; at US
incomes it moves the line by under $100 a year). In the Reference the line's poverty is 7.7% at year 20 in the release
row against 7.9% with no programme, and 9.5% at full backing, higher than at adoption (7.3%) in every run: the
programme narrows the cost-of-living gap but not relative income poverty, since conversion income and price cuts reach
participants who also work less. The release's own measure, adults below their cost of living, falls 60.3% (release
row) and 70.7% (H1) against no programme; the largest reduction on any measure is 74.5%. In the Adverse no measure
falls 85%. Both clauses stay short.

**3.5 C1.2a at both ends of the sweep.** The bar, $60,000 in 2019 dollars, is $75,557 in the engine's 2025 dollars
(CPI-U annual averages 321.943 and 255.657, the 2025 figure as the simulation's sources cite it). In the release row
13.9% of participants reach it (no seed at 70%) against 61.2% of adults with no programme: at `a = 0` the programme's
inflation erodes savings faster than conversion and price cuts build them. At full backing 91.1% do, in every seed. The
saving rule group 2.2 questioned (agents keeping 47% of income) is gone: v5.6.0 spends a sourced share of the surplus,
graded by income from the BLS Consumer Expenditure Survey. Group 2.2's reopening condition asked for exactly this rule
still showing 70% in the reference run; the reference run, the release row, shows 13.9%, so it is not met. The clause
holds only under full backing (reading 3.3): not shown, 0.5, flagged toward 1.0 on H1. The owner's answer to d24
("hold for the overhauled simulation") is answered here.

**3.6 C1.2b.** The wealth Gini at year 20 is 0.492 (release row) and 0.602 (H1), against 0.755 with no programme; no
seed is below 0.35 in any run or environment. Short at both ends; 0.5.

**3.7 C1.3, and the owner's note on tenure (decision 57.4).** In answering d29 the owner wrote: "The design does call for
tenure in several ways, such as people who sell-in to PTH, people who buy in, earn in, and even rent, although they can
move within the system and keep Acre Equity." *Reading:* the note is right about the design, and it describes the forms
of tenure Public Trust Housing offers; C1.3's clauses ask for a rate (88% stable over 5-year periods) and a cost share
(at most 30% of disposable income at 80% of the median), and a description of tenure forms states neither (decision
54.1: a design's description is not a projection). The model at v5.6.0 still represents Public Trust Housing from the
member's side only (a 35% cut in the housing component and Acre Equity; `MODEL_SPEC.md`, sections 6.10 and 11) and has
no tenure, eviction or rent line, so it cannot yet show the forms the owner names. On its nearest measure the weakest
5-year window is 78.0% (release row) and 86.1% (H1), against 70.1% with no programme; inside Public Trust Housing 79.4%
and 87.3%; all under 88%. The unit holds at 0.5, not shown. *Consequence:* the note is passed to the simulation's
maintainers (section 8): a tenure module with the four routes in, movement within the system and Acre Equity kept would
let the model compute clause 1, which is C1.3's reopening condition. No ledger decision follows, since no score changes;
the ledger's log records the answer.

**3.8 C1.4.** The model still has no lever that displaces 30%, 50% or 70% of paid hours, and computes no final
consumption. Its automation wave now also ends jobs (2.377 automation job losses per 100 adult-years in the Adverse,
3.587% of adult-years out of work) and its labour response lowers paid hours by 8.3% (Reference) to 11.3% (Adverse);
poverty on the Societal Poverty Line in the Adverse is 8.3% and 9.7% at year 20, above 8%. Both clauses not shown; 0.5.

**3.9 C3.2 re-read (a correction; it waits on the owner).** Group 2.1 carried C3.2 at 1.0 under its reading 3.2
(published 1.0s resting on the design's own modelling are re-read where the published model computes the quantity)
because the model then computed no price. It now does. In the release row the programme raises the basket index 50.8%
a year in the Reference (median price level 2,441 times its start at year 20), 60.9% in the Adverse and 27.4% in the
Stress Test, in no seed at or under 3%. At full backing it is 0.1% a year, in every seed under 3%; the sweep's midpoints
are 38.7% (`a` = 0.25), 26.2% (0.5) and 13.3% (0.75) a year (the release's backing sweep). Financing by a flat wage
contribution instead holds prices but leaves 68.9% of adults below the cost of living, against 49.2% with no programme.
The dual-currency paper's 0.95% a year and the framework paper's 3.2% under 8% outside inflation come from models not
published in runnable form. Clause 1 rests on the backing share (reading 3.3): not shown. Clause 2: no 8% scenario is
modelled: not shown. Clause 3: the one automatic adjustment modelled, the Inflation Surge Protocol's indexation of the
Basic Unit when prices rise faster than 5%, raises the payout with prices; no restraining adjustment is modelled: not
shown. **C3.2 1.0 → 0.5**, flagged toward 1.0 if the design's supply response is read as full backing. *Correction or
polish:* a correction; the published 1.0's ground (inflation held to the bar) is not shown by the design's own published
model. *Consequence:* CCO-PTF-CIP-SZH −0.5, to 14.0; first place becomes shared with Participatory Economics and
Integral; no failure count or tier changes; the dominance pairs CCO > China and CCO > Singapore are lost.

**3.10 C3.3.** One of four compound scenarios is modelled (the Adverse; the Stress Test is the same with weaker
settings). Against the Reference on the same seeds at year 20, the share not below the cost of living degrades 28.6%
(release row) and 40.0% (H1); the share not in housing distress 28.7% and 14.7%; the share above the Societal Poverty
Line under 1%. Not shown; 0.5.

**3.11 C3.4's adjustment run repeated.** Part (b1) read clause 4 ("zero collapses during parameter adjustments") as
shown only by modelling adjustments made during operation in a model able to represent a way an adjustment could cause a
collapse; v4.15 could not. v5.6.0 can. *The run:* the monthly Basic Unit multiplied by 0.7, 0.8, 1.2 or 1.3 from the
start of year 10 and held, Reference, every seed against its unadjusted run, at `a = 0` and `a = 1`. *The test, fixed in
the runner's header before the 500-seed run:* a seed collapses if, in any year from year 10, the share of adults below
the cost of living is 10 points or more above the unadjusted run's, or the year's price rise is 10 points or more above
it, or a value is not finite. *Result:* the 0.7 step collapses in 339 of 500 seeds and the 0.8 step in 43 at `a = 0`;
97 and 1 at `a = 1`; the 1.2 and 1.3 steps in none (they add at most 6.8 points to a year's price rise at `a = 0`). No
step makes prices run away or a run fail. *Reading:* on the test as fixed, clause 4 is **short**; the unit stays 0.5
(clauses 1 to 3 carried as part (b1) read them). The test counts the direct effect of a 20-30% cut in the allowance on
the share below the cost of living, which a reader may not call a collapse; on the reading that a collapse is a
breakdown the step causes (runaway prices, a failed run), no step collapses at either backing, and the clause would
clear. That alternative is the flag toward 1.0. The test was not changed after its result was seen.

**3.12 The reopening conditions, C5.3 and the design's other units.** The conditions recorded before v5.6.0 existed
(`STATE.md`; Handoff 43, 9.3) are evaluated in the script's check [3]: C1.1's (90% and 85% on the Societal Poverty Line),
C1.2a's (a sourced consumption rule still showing 70%), C1.3's (housing tenure and a cost line), C1.4's (an
hours-displacement lever) and C3.3's (three of four compound scenarios under 20%) are not met; C3.4's is met and the unit
is re-read (3.11). C5.2's condition is a deployment, which no simulation meets. **C5.3** is carried at 1.0: the model
still reads no aggregate participation threshold (the 55% minimum is a run warning) and computes no economic activity
or scaling path; its Stress Test, at 40% taking part, still lowers the share below the cost of living against no
programme, so it neither supports nor contradicts the rationale. **The design's other re-estimated units** whose sources
name the simulation (C2.5, C3.5, C4.1 to C4.4, C5.2, C5.4) were checked against v5.6.0: none turns on a quantity the
model now computes (it still has no resource flows, emissions, public debt, group income gaps, power distribution or
political survival; C2.5's exit liquidity follows the same liquid-share rule for Acre Equity as when it was read), so none reopens.

## 4. The units

### 4.1 Summary (generated)

Clauses: C cleared, S short, U not shown. "Before" is the unit this group supersedes and the part that set it.

| Criterion | Class | Before (part) | Clauses | Verdict | Flag |
|---|---|---:|---|---:|---|
| C1.1 | I | 0.5 (2.1) | S S | 0.5 |  |
| C1.2a | M | 0.5 (2.2) | U | 0.5 | toward 1.0 |
| C1.2b | W | 0.5 (2.1) | S | 0.5 |  |
| C1.3 | M | 0.5 (2.3) | U U | 0.5 |  |
| C1.4 | I | 0.5 (2.1) | U U | 0.5 |  |
| C3.2 | U | 1.0 (2.1) | U U U | 0.5 | toward 1.0 |
| C3.3 | W | 0.5 (2.1) | U | 0.5 |  |
| C3.4 | M | 0.5 (b1) | C C C S | 0.5 | toward 1.0 |
| C5.3 | U | 1.0 (2.1) | C C C C | 1.0 |  |

### 4.2 Clause by clause (generated)

#### CCO C1.1 Poverty Elimination Capacity: 1.0 (published), 0.5 (2.1) → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥90% poverty reduction within 20 years under base scenario | short | on the design's published model at v5.6.0 (500 seeds, 20 years, the Reference environment), poverty on the Societal Poverty Line, v2.0's indicator, computed from the engine's disposable income per adult, is 7.7% at year 20 in the release row (nothing the Source pays backed by new output, the model's main reading) against 7.9% in the paired run with no programme and today's safety net, a reduction of 1.5%, and 9.5% at full backing; with the in-kind value of price cuts counted, 4.6%; it was 7.3% at adoption, so it rises over the run; the largest reduction on any measure the engine reports is 74.5% (below 30 days of basic living, at full backing), and the release's own measure, adults below their cost of living, falls 60.3% (release row) and 70.7% (full backing) against no programme (readings 3.3, 3.4) | Compassionism Simulation at d10ed6e (v5.6.0), harness.js (md5 84be3bc9) and index.html (md5 2e1cc8c7), the v5.6 release's engine; cco_sim_v56_checks_s57_output.txt; the simulation's v5.6 release, data/releases/v5.6.json and dev/reports/v5-34-v56-release.md at d10ed6e; MODEL_SPEC.md at d10ed6e, sections 6.12 and 9; Foster, Jolliffe, Lara Ibarra, Lakner and Tetteh-Baah, Global Poverty Revisited Using 2021 PPPs and New Data on Consumption, World Bank Policy Research Working Paper 11137 (June 2025), section 3.4.1 (PDF md5 1128f547) |
| 2 | ≥85% under stress testing | short | in the Adverse environment (recessions, an automation wave and 2% outside inflation), poverty on the Societal Poverty Line is 8.3% at year 20 in the release row and 9.7% at full backing, against 7.3% with no programme, higher in both; the share below the cost of living falls 52.9% against no programme; no measure falls 85% (reading 3.4) | Compassionism Simulation at d10ed6e (v5.6.0), harness.js (md5 84be3bc9) and index.html (md5 2e1cc8c7), the v5.6 release's engine; cco_sim_v56_checks_s57_output.txt; the simulation's v5.6 release, data/releases/v5.6.json and dev/reports/v5-34-v56-release.md at d10ed6e; MODEL_SPEC.md at d10ed6e, sections 6.12 and 9; Foster, Jolliffe, Lara Ibarra, Lakner and Tetteh-Baah, Global Poverty Revisited Using 2021 PPPs and New Data on Consumption, World Bank Policy Research Working Paper 11137 (June 2025), section 3.4.1 (PDF md5 1128f547) |

*Note:* re-read on v5.6.0 (decision 57.3); both clauses stay short at either end of the backing sweep, and the unit stays 0.5. The reopening condition (90% in the reference run and 85% in the Adverse environment on the Societal Poverty Line) is not met.

#### CCO C1.2a Wealth Building for Resilience: 1.0 (published), 0.5 (2.2) → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥$60,000 median net-wealth accumulation over 20 years for 70%+ of participants, in constant 2019 US dollars at purchasing-power parity | not shown | on the design's published model at v5.6.0 (500 seeds, Reference), which spends by a sourced rule (a share 0.593 of the surplus, graded by income from the BLS Consumer Expenditure Survey), 13.9% of participants reach net wealth with Acre Equity of $60,000 in 2019 dollars ($75,557 in the engine's 2025 dollars) at year 20 in the release row, 0 of 500 seeds at 70%, median $30,728, against 61.2% of adults with no programme; at full backing (every dollar the Source pays backed by new output) 91.1% do, in 500 of 500 seeds, median $437,409; the design's sources state no backing share, and the model's main reading takes none; in the Adverse environment 1.7% and 77.9% (reading 3.5) | Compassionism Simulation at d10ed6e (v5.6.0), harness.js (md5 84be3bc9) and index.html (md5 2e1cc8c7), the v5.6 release's engine; cco_sim_v56_checks_s57_output.txt; the simulation's v5.6 release, data/releases/v5.6.json and dev/reports/v5-34-v56-release.md at d10ed6e; MODEL_SPEC.md at d10ed6e, sections 6.12 and 9; Report v1.6, System 12, C1.2a |

*Flag (reading 3.5):* toward 1.0: at full backing the engine's figure clears the bar in every seed.

*Note:* re-read on v5.6.0 (decision 57.3): the clause holds only if new output backs what the Source pays, a condition the design's sources do not state (protocol 2.1, reading 3.3), so it is not shown and the unit stays 0.5; the reopening condition (a sourced consumption rule that still shows 70% in the reference run) is not met, since the reference run, the release row, shows 13.9%.

#### CCO C1.2b Prevention of Exploitative Accumulation: 1.0 (published), 0.5 (2.1) → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Gini <0.35 for wealth distribution | short | on the design's published model at v5.6.0 (500 seeds, Reference), the wealth Gini at year 20, as the engine reports it (debts as zero), is 0.492 in the release row (0.477 with Acre Equity) and 0.602 at full backing, against 0.755 with no programme; no seed is below 0.35 in any run or environment; the design narrows the distribution, but not to the bar (reading 3.6) | Compassionism Simulation at d10ed6e (v5.6.0), harness.js (md5 84be3bc9) and index.html (md5 2e1cc8c7), the v5.6 release's engine; cco_sim_v56_checks_s57_output.txt; the simulation's v5.6 release, data/releases/v5.6.json and dev/reports/v5-34-v56-release.md at d10ed6e; MODEL_SPEC.md at d10ed6e, sections 6.12 and 9 |

*Note:* re-read on v5.6.0 (decision 57.3); short at either end of the backing sweep. The design's mechanisms lower the Gini against no programme, so the unit is 0.5, not 0.0.

#### CCO C1.3 Housing Security: 1.0 (published), 0.5 (2.3) → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥88% housing stability over 5-year periods | not shown | the engine still models no housing tenure, eviction or rent line (Public Trust Housing enters from the member's side only: a 35% cut in the housing component and Acre Equity), so it computes no stability rate; on its nearest measure, a year in which cash income and savings cannot cover the year's cost, 78.0% of adults pass the weakest 5-year window with no such year in the release row and 86.1% at full backing, against 70.1% with no programme; inside Public Trust Housing (20.0% of adults) 79.4% and 87.3%; every figure is under 88%; the tenure forms the owner describes (selling in, buying in, earning in, renting, moving within the system and keeping Acre Equity) are design features the model does not yet carry (reading 3.7) | Compassionism Simulation at d10ed6e (v5.6.0), harness.js (md5 84be3bc9) and index.html (md5 2e1cc8c7), the v5.6 release's engine; cco_sim_v56_checks_s57_output.txt; the simulation's v5.6 release, data/releases/v5.6.json and dev/reports/v5-34-v56-release.md at d10ed6e; MODEL_SPEC.md at d10ed6e, sections 6.12 and 9; the owner's note in the Project ledger, d29 (2026-10-14) |
| 2 | housing costs ≤30% of disposable income at 80% of regional median household disposable income | not shown | the engine carries no housing-cost line: Public Trust Housing cuts the housing component by 35% for its members (20.0% of adults), and no cost share at 80% of the median is stated or computed (reading 3.7) | Compassionism Simulation at d10ed6e (v5.6.0), harness.js (md5 84be3bc9) and index.html (md5 2e1cc8c7), the v5.6 release's engine; cco_sim_v56_checks_s57_output.txt; MODEL_SPEC.md at d10ed6e, sections 6.10 and 11 |

*Note:* re-read on v5.6.0 (decision 57.3); neither clause is shown and the nearest measure is under 88% at either end of the backing sweep. The reopening condition (housing tenure and a housing-cost line) is not met.

#### CCO C1.4 Automation Resilience: 1.0 (published), 0.5 (2.1) → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Poverty <8% | not shown | v2.0 names the design's own model of three scenarios displacing 30%, 50% and 70% of paid hours; the model at v5.6.0 still cannot run them: its automation wave slows wages and, since v5.4, ends jobs, at 2.377 automation job losses per 100 adult-years in the Adverse environment, with 3.587% of adult-years out of work, and its labour response lowers paid hours by 8.3% in the Reference and 11.3% in the Adverse environment, far from a 30% displacement; in the Adverse environment poverty on the Societal Poverty Line is 8.3% (release row) and 9.7% (full backing) at year 20, above 8% in both (reading 3.8) | Compassionism Simulation at d10ed6e (v5.6.0), harness.js (md5 84be3bc9) and index.html (md5 2e1cc8c7), the v5.6 release's engine; cco_sim_v56_checks_s57_output.txt; the simulation's v5.6 release, data/releases/v5.6.json and dev/reports/v5-34-v56-release.md at d10ed6e; MODEL_SPEC.md at d10ed6e, sections 6.12 and 9 |
| 2 | aggregate demand >85% baseline | not shown | the model computes no final consumption expenditure and no aggregate demand against a pre-displacement baseline (reading 3.8) | Compassionism Simulation at d10ed6e (v5.6.0), harness.js (md5 84be3bc9) and index.html (md5 2e1cc8c7), the v5.6 release's engine; cco_sim_v56_checks_s57_output.txt; MODEL_SPEC.md at d10ed6e, section 9 |

*Note:* re-read on v5.6.0 (decision 57.3); the reopening condition (an hours-displacement lever) is not met.

#### CCO C3.2 Inflation Control Mechanisms: 1.0 (published), 1.0 (2.1) → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Long-term inflation ≤3% | not shown | the design's published model now computes prices (since v5.0): what the Source pays out, less output that backs it, is new money that moves the price level; in the release row, its main reading, the programme raises the basket index 50.8% a year over 20 years in the Reference environment (median price level 2440.74 times its start), 60.9% in the Adverse and 27.4% in the Stress Test, in no seed at or under 3%; at full backing it raises it 0.1% a year, in every seed under 3%; financed by a flat wage contribution instead, prices hold but 68.9% of adults are below the cost of living, against 49.2% with no programme; the design states no backing share, so the clause rests on a condition its sources do not establish (readings 3.3, 3.9) | Compassionism Simulation at d10ed6e (v5.6.0), harness.js (md5 84be3bc9) and index.html (md5 2e1cc8c7), the v5.6 release's engine; cco_sim_v56_checks_s57_output.txt; the simulation's v5.6 release, data/releases/v5.6.json and dev/reports/v5-34-v56-release.md at d10ed6e; MODEL_SPEC.md at d10ed6e, sections 6.12 and 9; research hub at 8e8a6ba, dual-currency-inflation.html (md5 329235ce), sections 5.2 and 5.4 |
| 2 | stress test inflation ≤5% (when external 8%) | not shown | the model's environments carry 0% and 2% outside inflation; no 8% scenario is modelled, and the framework paper's 8% scenario (local inflation 3.2% while national inflation reaches 8.1%) comes from a model not published in runnable form (reading 3.9) | Compassionism Simulation at d10ed6e (v5.6.0), harness.js (md5 84be3bc9) and index.html (md5 2e1cc8c7), the v5.6 release's engine; cco_sim_v56_checks_s57_output.txt; research hub at 8e8a6ba, cco-ptf-integrated-framework.html (md5 10ab8364), section 5.2 |
| 3 | automatic adjustment preventing runaway inflation | not shown | the one automatic adjustment the model carries, the Inflation Surge Protocol's indexation of the Basic Unit when prices rise faster than 5%, raises the payout with prices (in the release row the indexed and unindexed readings give the same figures, since prices always rise faster than 5%); no adjustment that restrains issuance or conversion is modelled, so the model does not show adjustment preventing runaway inflation (reading 3.9) | Compassionism Simulation at d10ed6e (v5.6.0), harness.js (md5 84be3bc9) and index.html (md5 2e1cc8c7), the v5.6 release's engine; cco_sim_v56_checks_s57_output.txt; the simulation's v5.6 release, data/releases/v5.6.json and dev/reports/v5-34-v56-release.md at d10ed6e; MODEL_SPEC.md at d10ed6e, sections 6.12 and 9; research hub at 8e8a6ba, integrated-implementation-roadmap.html (Appendix G) |

*Flag (reading 3.9):* toward 1.0: if the design's supply response is read as backing every dollar the Source pays, the model's inflation is 0.1% a year and the papers' own modelling carries the other clauses, as reading 3.8 of group 2.1 did.

*Note:* re-read on v5.6.0 under reading 3.2 of group 2.1 (a published 1.0 resting on the design's own modelling is re-read where the published model computes the quantity): group 2.1 carried the unit because the model then computed no price; it now does, and its main reading shows inflation far above 3% a year. The design's mechanisms (spending limited to essentials, expiring units, supply response) are genuine, so the unit is 0.5, not 0.0. A CCO-PTF-CIP-SZH score change: it waits on the owner's confirmation (decision 57.2).

#### CCO C3.3 Multi-Failure Resistance: 1.0 (published), 0.5 (2.1) → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Maintain core functions across ≥3 of 4 compound scenarios with degradation <20% | not shown | the design's published model at v5.6.0 runs one compound scenario, the Adverse environment (recessions, an automation wave and 2% outside inflation at the reference settings), milder than C3.3's recession-and-automation scenario, and a weaker-settings variant of it, the Stress Test; against the Reference environment on the same seeds at year 20, the share of adults not below the cost of living degrades 28.6% (release row) and 40.0% (full backing), and the share not in housing distress 28.7% and 14.7%; the share above the Societal Poverty Line degrades under 1%; essential-service and democratic-function capacity are not modelled, and the other three compound scenarios are not modelled (reading 3.10) | Compassionism Simulation at d10ed6e (v5.6.0), harness.js (md5 84be3bc9) and index.html (md5 2e1cc8c7), the v5.6 release's engine; cco_sim_v56_checks_s57_output.txt; the simulation's v5.6 release, data/releases/v5.6.json and dev/reports/v5-34-v56-release.md at d10ed6e; MODEL_SPEC.md at d10ed6e, sections 6.12 and 9 |

*Note:* re-read on v5.6.0 (decision 57.3); one of four scenarios is modelled, and in it two measured functions degrade by more than 20% at either end of the backing sweep. The reopening condition (three of four compound scenarios under 20%) is not met.

#### CCO C3.4 Epistemic Adaptability: 1.0 (published), 0.5 (b1) → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥30% parameter adjustability range | cleared | octave caps, basic amounts (5-20% of GDP per capita), conversion multipliers and the phi-rate adjustable | as audited (the unit's own text) |
| 2 | policy updates within 6 months of evidence | cleared | the design's crisis protocol schedules parameter recalibration within one to six months, and monthly cost-of-living adjustments in an inflation surge | research hub at 8e8a6ba, integrated-implementation-roadmap.html (Appendix G) |
| 3 | changes open to challenge and reversal by those affected | cleared | CIP enables democratic parameter adjustment | as audited (the unit's own text) |
| 4 | zero collapses during parameter adjustments | short | the design's published model now has an endogenous price channel and a labour response, so the scorer's adjustment run was repeated (the Basic Unit multiplied by 0.7, 0.8, 1.2 or 1.3 from year 10, each seed against the unadjusted run, Reference): on the test fixed before the run (in a year from year 10, the share below the cost of living 10 points or more above the unadjusted run's, or the price rise 10 points or more above it), the 0.7 step collapses in 339 of 500 seeds and the 0.8 step in 43 of 500 in the release row, and in 97 of 500 and 1 of 500 at full backing (largest excess 16.6 and 14.0 points); the 1.2 and 1.3 steps collapse in none, adding at most 6.8 points to a year's price rise (reading 3.11) | Compassionism Simulation at d10ed6e (v5.6.0), harness.js (md5 84be3bc9) and index.html (md5 2e1cc8c7), the v5.6 release's engine; cco_sim_v56_checks_s57_output.txt |

*Flag (reading 3.11):* toward 1.0: if a collapse is read as a breakdown the step causes (runaway prices, a run that fails), not the cut's own effect on poverty, no step collapses at either backing.

*Note:* part (b1)'s reopening condition is met (an endogenous price and behavioural channel, the run repeated); the clause moves from not shown to short on the test fixed before the run, and the unit stays 0.5. The test counts the direct effect of a 20-30% cut in the allowance on the share below the cost of living, which is why the flag toward 1.0 is kept on another reading.

#### CCO C5.3 Partial and Parallel Deployability: 1.0 (published), 1.0 (2.1) → 1.0

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Viable at ≥30% participation | cleared | Viable at 30%+ participation | as audited (the unit's own text) |
| 2 | coexistence with traditional markets maintaining ≥90% economic activity | cleared | Can coexist with traditional markets | as audited (the unit's own text) |
| 3 | scaling pathway validated through modeling | cleared | Scaling pathway validated through modeling | as audited (the unit's own text) |
| 4 | coordination protocols established | cleared | Inter-jurisdictional coordination protocols specified | as audited (the unit's own text) |

*Note:* re-read on v5.6.0 and carried (reading 3.12): the model still reads no aggregate participation threshold (the 55% minimum is a run warning), computes no economic activity or scaling path, and its Stress Test, at 40% taking part (43.7% by year 19), still lowers the share below the cost of living against no programme, so it neither supports nor contradicts the rationale's figures; its labour response lowers paid hours by 8.3% to 11.3%, while the projects' output, which it values separately, is not an economic-activity measure.

## 5. The simulation runs (from `cco_sim_v56_checks_s57_output.txt`)

Engine: `harness.js` at `BetterToBest/compassionism-simulation` commit `d10ed6e` (v5.6.0), md5 `84be3bc9…`, with the
engine block of `index.html` at the same commit, md5 `2e1cc8c7…`; both are the v5.6 release's (reading 3.2). Runs:
`node cco_sim_v56_checks_s57.js run HARNESS 1 125 part_1.json` and three more parts to seed 500, then `report` on the
four parts (seeds are paired, so splitting changes no figure; a 2-seed trial in one and in two parts gave identical
tables). Before any table is read the report checks the engine's digests, that the parts cover seeds 1 to 500, and that
the release's published figures are reproduced. N = 500 seeds, 500 adults and their households, 20 years; figures are
seed means. "Release row" is the model's main result (`a = 0`); "H1" is full backing (`a = 1`); "No program" is the
paired run with today's safety net. Shares of adults at year 20 unless stated; dollars are the engine's year-0 (2025)
dollars.

[3] C1.1: THE SOCIETAL POVERTY LINE (2021 PPP: max($3.00, $1.30 + 0.5 x median) a day; disposable income per adult, year-0 dollars; X = with the in-kind value of price cuts)
| Environment | Run | SPL, year 0 | SPL, year 20 | Reduction from year 0 | SPL X, year 20 | Below the cost of living, year 20 | Median disposable income, year 20 |
|---|---|---:|---:|---:|---:|---:|---:|
| Reference | No program (today's safety net) | 6.1% | 7.9% | -27.9% | 7.9% | 41.3% | $52,515 |
| Reference | Compassionism, release row (a = 0) | 7.3% | 7.7% | -6.0% | 4.6% | 14.9% | $48,109 |
| Reference | Compassionism, H1 (a = 1) | 7.3% | 9.5% | -30.0% | 5.7% | 9.3% | $62,234 |
| Adverse | No program (today's safety net) | 6.1% | 7.3% | -18.3% | 7.3% | 73.1% | $33,263 |
| Adverse | Compassionism, release row (a = 0) | 7.3% | 8.3% | -14.0% | 6.8% | 39.2% | $30,249 |
| Adverse | Compassionism, H1 (a = 1) | 7.3% | 9.7% | -32.3% | 8.8% | 45.6% | $36,499 |
| Stress Test | No program (today's safety net) | 6.1% | 7.3% | -18.3% | 7.3% | 73.1% | $33,263 |
| Stress Test | Compassionism, release row (a = 0) | 6.6% | 7.3% | -11.2% | 9.4% | 62.4% | $31,122 |
| Stress Test | Compassionism, H1 (a = 1) | 6.6% | 8.1% | -23.3% | 8.4% | 61.7% | $34,499 |

Reductions against the paired no-programme run at year 20 (release row; H1):
- Reference: SPL 1.5%; -20.8%. SPL X 42.0%; 27.7%. Below the cost of living (person-years, the release's measure) 60.3%; 70.7%. Below 30 days of basic living 55.9%; 74.5%.
- Adverse: SPL -14.5%; -32.8%. SPL X 6.9%; -20.3%. Below the cost of living (person-years, the release's measure) 52.9%; 49.9%. Below 30 days of basic living 44.6%; 61.9%.
- Stress Test: SPL -0.8%; -11.8%. SPL X -29.2%; -15.0%. Below the cost of living (person-years, the release's measure) 20.0%; 20.3%. Below 30 days of basic living -12.0%; 24.5%.
PASS  Reference: no reduction above reaches 90% (largest 74.5%)

[4] C1.2a: NET WEALTH WITH ACRE EQUITY AT YEAR 20, AGAINST $60,000 IN 2019 DOLLARS ($75,557 in the engine's year-0 dollars, 2025)
| Environment | Run | Adults at the bar | Without Acre Equity | Participants at the bar | Participants | Seeds with 70% of participants at the bar | Median net wealth |
|---|---|---:|---:|---:|---:|---:|---:|
| Reference | No program (today's safety net) | 61.2% | 61.2% | - | - | - | $174,124 |
| Reference | Compassionism, release row (a = 0) | 12.1% | 11.4% | 13.9% | 84.0% | 0 of 500 | $30,728 |
| Reference | Compassionism, H1 (a = 1) | 87.2% | 87.0% | 91.1% | 82.6% | 500 of 500 | $437,409 |
| Adverse | No program (today's safety net) | 47.0% | 47.0% | - | - | - | $55,535 |
| Adverse | Compassionism, release row (a = 0) | 1.5% | 1.3% | 1.7% | 84.0% | 0 of 500 | $9,384 |
| Adverse | Compassionism, H1 (a = 1) | 69.8% | 69.5% | 77.9% | 57.7% | 498 of 500 | $209,707 |
| Stress Test | No program (today's safety net) | 47.0% | 47.0% | - | - | - | $55,535 |
| Stress Test | Compassionism, release row (a = 0) | 5.0% | 4.9% | 8.9% | 43.7% | 0 of 500 | $585 |
| Stress Test | Compassionism, H1 (a = 1) | 56.0% | 55.9% | 69.7% | 30.0% | 235 of 500 | $115,140 |

[5] C1.2b: THE WEALTH GINI AT YEAR 20 (debts as zero, x n/(n-1), as the engine reports it)
| Environment | Run | Gini | With Acre Equity | Seeds below 0.35 |
|---|---|---:|---:|---:|
| Reference | No program (today's safety net) | 0.755 | 0.755 | 0 of 500 |
| Reference | Compassionism, release row (a = 0) | 0.492 | 0.477 | 0 of 500 |
| Reference | Compassionism, H1 (a = 1) | 0.602 | 0.600 | 0 of 500 |
| Adverse | No program (today's safety net) | 0.803 | 0.803 | 0 of 500 |
| Adverse | Compassionism, release row (a = 0) | 0.644 | 0.610 | 0 of 500 |
| Adverse | Compassionism, H1 (a = 1) | 0.684 | 0.682 | 0 of 500 |
| Stress Test | No program (today's safety net) | 0.803 | 0.803 | 0 of 500 |
| Stress Test | Compassionism, release row (a = 0) | 0.762 | 0.748 | 0 of 500 |
| Stress Test | Compassionism, H1 (a = 1) | 0.759 | 0.759 | 0 of 500 |

[6] C1.3: ADULTS PASSING A 5-YEAR WINDOW WITH NO YEAR OF DISTRESS (years 1-5 ... 16-20; PTH = Public Trust Housing)
| Environment | Run | Years 1-5 | 6-10 | 11-15 | 16-20 | Lowest | In PTH (share; lowest window) | Outside PTH, lowest window |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| Reference | No program (today's safety net) | 75.7% | 72.4% | 70.7% | 70.1% | 70.1% | - | - |
| Reference | Compassionism, release row (a = 0) | 82.2% | 79.0% | 78.0% | 79.6% | 78.0% | 20.0%; 79.4% | 77.6% |
| Reference | Compassionism, H1 (a = 1) | 86.1% | 90.8% | 91.9% | 92.7% | 86.1% | 20.0%; 87.3% | 85.8% |
| Adverse | No program (today's safety net) | 73.8% | 67.4% | 62.1% | 57.5% | 57.5% | - | - |
| Adverse | Compassionism, release row (a = 0) | 80.5% | 70.4% | 62.5% | 55.9% | 55.9% | 20.0%; 57.0% | 55.6% |
| Adverse | Compassionism, H1 (a = 1) | 85.3% | 86.2% | 83.3% | 79.8% | 79.8% | 20.0%; 81.0% | 79.4% |
| Stress Test | No program (today's safety net) | 73.8% | 67.4% | 62.1% | 57.5% | 57.5% | - | - |
| Stress Test | Compassionism, release row (a = 0) | 74.9% | 63.0% | 50.7% | 41.5% | 41.5% | 9.9%; 43.5% | 41.3% |
| Stress Test | Compassionism, H1 (a = 1) | 78.7% | 75.1% | 70.7% | 66.5% | 66.5% | 9.9%; 68.1% | 66.4% |

[7] C3.2: PROGRAMME INFLATION (the basket index's annual rise from the programme) AND THE PRICE LEVEL AT YEAR 20
| Environment | Outside inflation | Run | Programme inflation a year | Price level, year 20 (median over seeds) | Seeds at or under 3% |
|---|---:|---|---:|---:|---:|
| Reference | 0% | Compassionism, release row (a = 0) | 50.8% | 2440.74 | 0 of 500 |
| Reference | 0% | Compassionism, H1 (a = 1) | 0.1% | 1.02 | 500 of 500 |
| Adverse | 2% | Compassionism, release row (a = 0) | 60.9% | 12159.65 | 0 of 500 |
| Adverse | 2% | Compassionism, H1 (a = 1) | 0.1% | 1.47 | 500 of 500 |
| Stress Test | 2% | Compassionism, release row (a = 0) | 27.4% | 145.14 | 0 of 500 |
| Stress Test | 2% | Compassionism, H1 (a = 1) | 0.0% | 1.46 | 500 of 500 |

[8] C3.3: THE ADVERSE ENVIRONMENT AGAINST THE REFERENCE, YEAR 20, SAME SEEDS (degradation = fall in the share, % of the Reference share)
| Run | Function (share of adults at year 20) | Reference | Adverse | Degradation | Stress Test | Degradation |
|---|---|---:|---:|---:|---:|---:|
| Compassionism, release row (a = 0) | Not below the cost of living | 85.1% | 60.8% | 28.6% | 37.6% | 55.8% |
| Compassionism, release row (a = 0) | Above the Societal Poverty Line | 92.3% | 91.7% | 0.6% | 92.7% | -0.4% |
| Compassionism, release row (a = 0) | Not in housing distress | 83.7% | 59.7% | 28.7% | 43.7% | 47.8% |
| Compassionism, release row (a = 0) | Above the wealth line (six months of costs) | 55.6% | 19.1% | 65.7% | 23.7% | 57.3% |
| Compassionism, H1 (a = 1) | Not below the cost of living | 90.7% | 54.4% | 40.0% | 38.3% | 57.7% |
| Compassionism, H1 (a = 1) | Above the Societal Poverty Line | 90.5% | 90.3% | 0.2% | 91.9% | -1.5% |
| Compassionism, H1 (a = 1) | Not in housing distress | 93.8% | 80.0% | 14.7% | 66.9% | 28.6% |
| Compassionism, H1 (a = 1) | Above the wealth line (six months of costs) | 91.3% | 77.4% | 15.3% | 63.9% | 30.1% |

[9] C3.4: THE BASIC UNIT STEPPED FROM YEAR 10 AND HELD, REFERENCE, EACH SEED AGAINST THE UNADJUSTED RUN
| Backing | Step | Below the cost of living, year 20: adjusted / unadjusted | Price level, year 20 (median): adjusted / unadjusted | Largest excess rise, cost of living (points) | Largest excess price rise (points) | Seeds collapsing |
|---|---|---:|---:|---:|---:|---:|
| a = 0 (release row) | x0.7 | 24.1% / 14.9% | 1286.04 / 2440.74 | 16.6 | 0.0 | 339 of 500 |
| a = 0 (release row) | x0.8 | 21.5% / 14.9% | 1690.58 / 2440.74 | 12.8 | 0.0 | 43 of 500 |
| a = 0 (release row) | x1.2 | 10.4% / 14.9% | 2978.14 / 2440.74 | -0.6 | 5.9 | 0 of 500 |
| a = 0 (release row) | x1.3 | 9.0% / 14.9% | 2976.78 / 2440.74 | -1.2 | 6.8 | 0 of 500 |
| a = 1 (H1) | x0.7 | 15.3% / 9.3% | 1.02 / 1.02 | 14.0 | 0.1 | 97 of 500 |
| a = 1 (H1) | x0.8 | 13.2% / 9.3% | 1.02 / 1.02 | 10.8 | 0.1 | 1 of 500 |
| a = 1 (H1) | x1.2 | 6.7% / 9.3% | 1.02 / 1.02 | 0.0 | 0.1 | 0 of 500 |
| a = 1 (H1) | x1.3 | 6.1% / 9.3% | 1.02 / 1.02 | 0.0 | 0.1 | 0 of 500 |

## 6. What parts (a), (b) and groups 2.1 to 2.5 change (generated)

**Consequences** (totals on the published 26-criterion structure, with ranks; failures and tiers after this group):

| Entry | Published (rank) | After group 2.4 (rank) | After group 2.5 (rank) | Change here | Failures | Tier |
|---|---:|---:|---:|---:|---:|---|
| CCO | 24.5 (1) | 14.5 (1) | 14.0 (1) | -0.5 | 0 | Potentially Adequate |
| PE | 20.5 (2) | 14.0 (2) | 14.0 (1) | 0.0 | 1 | Potentially Adequate |
| NSD | 19.5 (3) | 13.5 (4) | 13.5 (4) | 0.0 | 1 | Potentially Adequate |
| INT | 19.5 (3) | 14.0 (2) | 14.0 (1) | 0.0 | 3 | Partially Adequate |
| DG | 19.0 (5) | 13.0 (5) | 13.0 (5) | 0.0 | 2 | Potentially Adequate |
| MS | 16.5 (6) | 13.0 (5) | 13.0 (5) | 0.0 | 2 | Potentially Adequate |
| MMT | 15.5 (7) | 11.0 (14) | 11.0 (14) | 0.0 | 4 | Partially Adequate |
| UBI | 14.5 (8) | 11.0 (14) | 11.0 (14) | 0.0 | 7 | Structurally Inadequate |
| MC | 14.5 (8) | 12.5 (8) | 12.5 (8) | 0.0 | 3 | Partially Adequate |
| OS | 14.5 (8) | 13.0 (5) | 13.0 (5) | 0.0 | 3 | Partially Adequate |
| SWF | 14.0 (11) | 12.5 (8) | 12.5 (8) | 0.0 | 3 | Partially Adequate |
| SG | 14.0 (11) | 11.5 (11) | 11.5 (11) | 0.0 | 4 | Partially Adequate |
| GEO | 13.5 (13) | 12.5 (8) | 12.5 (8) | 0.0 | 2 | Potentially Adequate |
| UBS | 13.5 (13) | 11.5 (11) | 11.5 (11) | 0.0 | 4 | Partially Adequate |
| IF | 13.5 (13) | 11.5 (11) | 11.5 (11) | 0.0 | 5 | Partially Adequate |
| FALC | 13.0 (16) | 9.0 (18) | 9.0 (18) | 0.0 | 10 | Structurally Inadequate |
| DE | 11.5 (17) | 9.0 (18) | 9.0 (18) | 0.0 | 8 | Structurally Inadequate |
| SQ | 10.5 (18) | 9.5 (16) | 9.5 (16) | 0.0 | 9 | Structurally Inadequate |
| CPS | 10.0 (19) | 7.5 (22) | 7.5 (22) | 0.0 | 12 | Structurally Inadequate |
| SC | 10.0 (19) | 9.0 (18) | 9.0 (18) | 0.0 | 8 | Structurally Inadequate |
| CN | 10.0 (19) | 9.5 (16) | 9.5 (16) | 0.0 | 8 | Structurally Inadequate |
| QA | 9.0 (22) | 8.5 (21) | 8.5 (21) | 0.0 | 9 | Structurally Inadequate |
| LM | 8.0 (23) | 7.0 (23) | 7.0 (23) | 0.0 | 13 | Structurally Inadequate |

After this group the corpus has 14 dominance pairs against 16 after group 2.4 (new: none; lost: CCO>CN, CCO>SG), and its frontier holds 16 entries against 15 (SQ, NSD, CPS, MS, LM, UBI, DG, FALC, PE, CCO, INT, MC, SWF, SG, IF, OS). First place is shared by PE, CCO and INT at 14.0 (PE 14.0, CCO 14.5, INT 14.0 after group 2.4), ahead of NSD at 13.5. Across the pass so far 215 units have been re-estimated, each counted once: 16 are at 1.0, 182 at 0.5 and 17 at 0.0; against their published scores 148 fell, 5 rose and 62 are unchanged (net -71.5 points).

**The score ledger** (each part's change to each entry's total; units re-estimated and at 0.5 after this group):

| Entry | Published | (a) | (b1) | (b2) | (b3) | (b4) | (b5) | (b6) | (b7) | 48.3 | (b8) | (b9) | (2.1) | (2.2) | (2.3) | (2.4) | (2.5) | Now | Re-estimated | At 0.5 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| CCO | 24.5 | -0.5 | -1.5 | -0.5 | -0.5 | -0.5 | -0.5 | -1.0 | -0.5 | -0.5 | -0.5 | -1.0 | -1.5 | -0.5 | -0.5 |  | -0.5 | 14.0 | 22 | 21 |
| PE | 20.5 |  | -1.5 | -0.5 | -0.5 | -1.5 |  | -0.5 | -0.5 |  | -0.5 | -0.5 |  |  | -0.5 |  |  | 14.0 | 16 | 15 |
| NSD | 19.5 | -2.5 | -1.0 | -0.5 | -0.5 | -0.5 |  |  |  |  | -0.5 | -0.5 |  | -0.5 |  | 0.5 |  | 13.5 | 15 | 14 |
| INT | 19.5 | -0.5 | -1.0 | -0.5 |  | -1.0 | -0.5 | -1.0 | -0.5 |  |  |  |  |  | -0.5 |  |  | 14.0 | 14 | 11 |
| DG | 19.0 |  | -1.5 | -0.5 | -0.5 | -0.5 |  | -0.5 | -1.0 |  | -1.0 |  |  |  | -0.5 |  |  | 13.0 | 14 | 14 |
| MS | 16.5 | -1.0 | -1.5 | -0.5 | -0.5 |  |  |  | 0.5 |  |  |  |  | -0.5 |  |  |  | 13.0 | 11 | 9 |
| MMT | 15.5 | -1.5 | -1.0 | -0.5 | -0.5 |  |  |  |  |  | -0.5 |  |  | -0.5 |  |  |  | 11.0 | 10 | 8 |
| UBI | 14.5 | -1.5 | -0.5 | -0.5 | -0.5 |  |  |  |  |  | -0.5 |  |  |  |  |  |  | 11.0 | 11 | 8 |
| MC | 14.5 |  | -1.0 | -0.5 |  |  | -0.5 |  |  |  |  |  |  |  |  |  |  | 12.5 | 8 | 5 |
| OS | 14.5 | -0.5 |  |  |  |  | -0.5 | -0.5 |  |  |  |  |  |  |  |  |  | 13.0 | 7 | 5 |
| SWF | 14.0 |  |  | -0.5 |  |  | -0.5 | -0.5 |  |  |  |  |  |  |  |  |  | 12.5 | 7 | 5 |
| SG | 14.0 | -1.0 | -0.5 | -0.5 |  |  |  |  |  |  |  |  |  | -0.5 |  |  |  | 11.5 | 6 | 6 |
| GEO | 13.5 | -0.5 |  |  |  |  | -0.5 |  |  |  |  |  |  |  |  |  |  | 12.5 | 5 | 4 |
| UBS | 13.5 |  | -0.5 | -0.5 |  |  | -0.5 |  |  |  |  |  |  |  |  | -0.5 |  | 11.5 | 7 | 4 |
| IF | 13.5 | -1.0 |  |  |  |  | -0.5 |  |  |  |  | -0.5 |  |  |  |  |  | 11.5 | 7 | 7 |
| FALC | 13.0 | -0.5 | -0.5 |  | -0.5 | -1.0 |  | -0.5 | -0.5 |  |  |  |  |  | -0.5 |  |  | 9.0 | 11 | 9 |
| DE | 11.5 | -0.5 | -0.5 |  |  |  | -0.5 | -0.5 | -0.5 |  |  |  |  |  |  |  |  | 9.0 | 8 | 7 |
| SQ | 10.5 | -0.5 |  |  |  | -0.5 |  |  |  |  |  |  |  |  |  |  |  | 9.5 | 6 | 5 |
| CPS | 10.0 | -1.5 |  |  | -0.5 |  |  |  |  |  | -0.5 |  |  |  |  |  |  | 7.5 | 7 | 5 |
| SC | 10.0 |  | -1.0 |  |  |  |  |  |  |  |  | -0.5 |  |  |  | 0.5 |  | 9.0 | 6 | 6 |
| CN | 10.0 |  |  | -0.5 |  |  |  |  |  |  |  |  |  |  |  |  |  | 9.5 | 4 | 3 |
| QA | 9.0 | -0.5 |  | -0.5 |  |  |  |  |  |  |  |  |  |  |  | 0.5 |  | 8.5 | 5 | 5 |
| LM | 8.0 | -1.5 |  |  |  |  |  |  |  |  |  | -0.5 |  | 0.5 |  | 0.5 |  | 7.0 | 8 | 6 |

Anchor examples citing a unit the pass moves: C1.1's 1.0 example, NSD (part (b3)); C1.2a's 1.0 example, MS (part (2.2)); C1.2b's 1.0 example, CCO (part (2.5)); C1.4's 1.0 example, CCO (part (2.5)); C2.1's 1.0 example, UBI (part (a)); C2.3's 1.0 example, DG (part (b1)); C2.4's 1.0 example, PE (part (b1)); C2.5's 1.0 example, CCO (part (b5)); C3.1's 1.0 example, UBI (part (b2)); C3.2's 1.0 example, PE (part (b4)); C3.5's 1.0 example, CCO (part (b6)); C3.5's 0.0 example, LM (part (2.4)); C3.5's 0.0 example, SC (part (2.4)); C4.1's 1.0 example, DG (part (b6)); C4.2's 1.0 example, PE (part (b7)); C4.3's 1.0 example, CCO (part (b8)); C5.1's 1.0 example, MS (part (b2)); C5.2's 1.0 example, CCO (part (b9)); C5.4's 1.0 example, CCO (part (b9)); C5.5's 1.0 example, PE (part (b9)). Bands whose example the pass moves and which no corpus unit then scores at their value: C1.1's 1.0, C1.2a's 1.0, C2.1's 1.0, C2.3's 1.0, C2.4's 1.0, C3.1's 1.0, C3.5's 1.0, C4.1's 1.0, C4.2's 1.0, C4.3's 1.0.

## 7. Corrections found (not polish)

- **CCO-PTF-CIP-SZH, C3.2, 1.0 → 0.5 (reading 3.9).** The published 1.0 rests on the design's own modelling of
  inflation; the design's published model now computes prices and, on its main reading, shows the programme raising them
  50.8% a year; inflation stays under 3% only if new output backs every dollar the Source pays, which no design source
  establishes. A correction, awaiting the owner's confirmation (decision 57.2).

No other unit changes. C3.4's clause 4 moving from not shown to short changes no score.

## 8. Notes for the simulation's maintainers (the owner's project; not NEEC corrections)

These are what the design's units would need from a later version, in the order of their reach. None is a request to
change a result; each names a quantity a criterion asks for that the model does not yet compute.

1. **Housing tenure (C1.3; the owner's note, d29).** Public Trust Housing's routes in (selling in, buying in, earning
   in, renting), movement within the system with Acre Equity kept, and tenure outside it (owners and renters at market
   rents), with a housing-cost line, would let the model compute 5-year housing stability and the cost share at 80% of
   the median.
2. **The backing share (C1.2a, C3.2).** Every result the units read turns on it. A sourced estimate of the output
   response to conversion rewards, or the design's own statement of how the Source is paid for, would decide C3.2's
   clause 1 and C1.2a's clause.
3. **A restraining automatic adjustment (C3.2, clause 3).** The modelled Inflation Surge Protocol indexes the Basic Unit
   to prices; an adjustment of issuance, conversion rates or the conversion tax in response to inflation, if the design
   specifies one, would let the model test clause 3; an 8% outside-inflation scenario would test clause 2.
4. **An hours-displacement lever and final consumption (C1.4).** Scenarios displacing 30%, 50% and 70% of paid hours,
   with consumption expenditure reported against the pre-displacement baseline.
5. **Compound scenarios (C3.3).** The other three of C3.3's four (each pairing two shocks), with essential-service
   capacity reported.
6. **The Societal Poverty Line (C1.1).** Reporting it beside the cost-of-living measure would let readers see that the
   programme narrows absolute shortfalls more than relative income poverty.

## 9. Disclosure

The scorer that wrote the simulation's math and code (Claude, in the owner's simulation sessions) is the same model
family that scores it here; the owner maintains both the design and the model. The scorer ran the model through its
published engine with no change to it, and every figure in this record comes from that run, which reproduces the
release's own published figures. A first 500-seed run omitted the study profile the simulation's test-bed sets before every run (`applyNR6`, `TB_PROFILE_G`); its programme rows did not reproduce the release, so it was discarded unread and the run repeated with the profile set. The test of a collapse in reading 3.11 was fixed before the 500-seed run (a 3-seed
trial had been run to time the job). The owner's message notes that the simulation still has limitations and will be
updated again; Paper v2.0 states the version read (decision 57.3).

## 10. What remains

- **The owner:** confirm or reverse C3.2 (S57-3.9) in the ledger; the other eight units' holds and flags, which follow
  from reading 3.3, are listed there as S57-3.3.
- **Group 2.6: C5.2 Staged Transition Pathways**, re-read as class M (the next group in the triage, rerun after this
  one), then the groups in the triage's order, the 69 new units and stages 3 to 5 (`STATE.md`).
- **A later simulation version** is read when the owner releases it for scoring (decision 57.3), through the reopening
  conditions this record restates.

## 11. What this record does not show

It does not show that any figure of the model is a forecast: the model's own pages say it shows what its rules imply.
It does not decide the backing share, which the design leaves open, and so cannot say whether the design's inflation
control or wealth building succeed; it reports both ends. It does not rerun the earlier groups' simulation readings at
v4.20, which stand as the pass's history. The harness checks the runs' captured output by digest; it does not rerun the
JavaScript, which needs the simulation's source.
