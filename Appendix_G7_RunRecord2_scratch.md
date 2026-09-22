# NEEC Appendix G.7 — Run Record #2 (SCRATCH DRAFT, pending insertion)

**Status: not yet inserted into `NEEC_Paper_v1_2.md`.** Per the project's
scratch-before-insert discipline, this is a reviewable draft. Appendix G.7 is
append-only — when inserted, this text should be added *after* Run Record #1
without editing it, exactly as this draft does not edit Run Record #1's own
findings below (it re-confirms them independently instead).

---

## Run #2 — v4.1, August 2026

**Trigger:** the Compassionism Simulation's v4.1 `index.html` was uploaded to
the project (Session 5's handoff had deferred this at the user's explicit
request, since v4.0 was known to be superseded imminently). This is the
session's first task, per that handoff's explicit recommendation.

**What changed since Run Record #1 (v3.9):** v4.0, released between the two
run records, is — by its own changelog's description — "the largest revision
to date" to the simulation. It is not a parameter recalibration; it changes
five mechanisms this cross-validation protocol depends on. v4.1 itself adds
only one functional fix (a paired-population synergy-bonus leak scoped to the
ablation/attribution feature, not the main simulation path) plus UI/label/
documentation corrections. Full accounting below.

### Step 1–2: Constants and dead-code check

Every CFG constant shared between the v3.9 script and v4.1's actual `CFG`
object was compared value-by-value: `WAGE_BASE_GROWTH`, `WAGE_BLEI_BONUS`,
`WAGE_OCTAVE_BONUS`, `WAGE_MEDIAN_SIU`, `POVERTY_LINE`, `SIM_COST_SCALE`,
`BASE_DAILY_COST`, `CCO_PTH_DAILY_COST`, `AI_DISPLACEMENT_YEAR_1/2`,
`AI_DISPLACEMENT_RATE_1/2`, `BLEI_PRECARIOUS_MAX`, `PROG_PIVOT`,
`PROG_RATE`, `PROG_TAX_MAX`, `SZH_ALL_RESIDENTS`, `SZH_PTF_BONUS`,
`WEALTH_FLOOR`, `PHI_RATIO`, `PHI_QUALITY_THRESH` — **all identical, byte
for byte.** v4.0/v4.1 add new constants (`SZH_THETA_*`, `FBS_*`,
`PTH_EQUITY_CONTRIB_SHARE`, `PTF_BASS_Q`, `SIU_TO_USD`) rather than changing
existing ones.

**Re-confirmed (not assumed): `SZH_PTF_BONUS` remains an unused constant in
v4.1.** It is still present in `CFG` (value 0.05, unchanged) but does not
appear in any formula in `agentBLEI()`, `calcBLEIComponents()`, `runYear()`,
or anywhere else the full v4.1 script block was searched. The SZH/PTF
synergy effect is computed entirely through `szhTheta()` instead (see
below). This was flagged as a candidate finding, not yet verified, at the
close of Session 5; it is now independently re-confirmed against the actual
v4.1 source rather than carried forward on the strength of the v4.0 read.

**Re-confirmed and clarified: `szhTheta()` is gated on the Zone Coherence
Index slider, not on simulated PTF density, despite what the in-app
documentation says.** Every call site — inside `agentBLEI()`,
`calcBLEIComponents()`, and `runYear()` — passes `szhCoh` (the user-facing
0–0.95 slider, sourced from `p.szhCoh`) to `szhTheta()`. The simulation
*does* separately compute an actual PTF-adoption fraction each year
(`ptfAdoptFrac`, `runYear()`), but that variable is used only for the Bass
(1969) diffusion term governing new PTF adoption — it is never passed to
`szhTheta()`. Meanwhile, the v4.0 changelog and the in-app Assumptions panel
both describe this mechanism as "network-density-gated... 0 below 55% PTF
density, scaling to 0.25 at 90%+" (density, not coherence). This is a real
documentation/implementation mismatch, not a hypothetical: a user who sets
Zone Coherence to 0.90 with PTF participation still building toward that
level gets the full synergy bonus immediately, regardless of how many
agents have actually adopted PTF. Also re-confirmed unchanged from the
candidate note: this does not affect any number in this run (Reference
preset holds `szhCoh` fixed at 0.72 throughout, so the *value* of
`szhTheta(0.72)` is correct for what it's fed regardless of which input
variable is philosophically the "right" one) — it matters for interpreting
what the mechanism represents, not for this run's arithmetic.

### Step 3: Cap-saturation / inert-parameter check

Unchanged result, re-run against v4.1's (identical) `popAIDisp` logic:
first year the 10-point cap is hit is year 13 (0-indexed), and the
acceleration branch (`yr >= AI_Y2`) computes 0.142 the instant it activates
at year 15 — already above the cap — rising to 0.340 by year 24. **`AI_DISPLACEMENT_RATE_2`
still has zero effect on any output, at any parameter setting, in v4.1.**
This is not carried forward from Run Record #1 uncritically — `popAIDisp`'s
code is verified byte-identical between v3.9 and v4.1, and the check was
re-run fresh (see `cap_saturation_check()` output, reproduced in full in
the updated script).

### Step 3.5 (new this run): mechanism-level diff of `runYear()`

This is the substantive addition Run Record #2 makes over #1. The v3.9
Python script's `run_year()` was checked line-by-line against v4.1's actual
`runYear()` and found to diverge in five places, all introduced in v4.0:

1. **Octave advancement: fixed-probability → FBS-gated.** v3.9: any
   CCO-participating agent above the BLEI precarious threshold advances an
   octave with flat probability `0.08 + cipDemo×0.04` per year. v4.1:
   `P(advance) = 1 − exp(−λ·FBS)`, where FBS is a real-USD residual-income
   calculation and λ is a per-agent capability coefficient drawn at
   construction. An agent with FBS=0 cannot advance at all under v4.1,
   regardless of BLEI — structurally impossible under v3.9's formula.
2. **CCO conversion-rate ceiling: quality-only → octave-and-quality.** v3.9:
   `baseRate = 1 + (quality/maxMult)×(maxMult−1)` — octave plays no role in
   conversion. v4.1: octave sets the *ceiling* (`octCeiling`), quality sets
   how much of that ceiling is realized (`qualityFactor`). Since (1) makes
   octave advancement itself slower and need-gated, this compounds with (2)
   rather than being independent.
3. **SZH/PTF synergy bonus: plain-linear → threshold-gated.** v3.9:
   `ptfConvBonus = 1.30 + (szhCoh − 0.50)×0.35`, always active whenever SZH
   and PTF are both on. v4.1: `1.30 + szhTheta(szhCoh)`, zero below 0.55
   coherence. At the Reference preset's szhCoh=0.72: v3.9 gives 1.377×;
   v4.1 gives 1.421× — close at this specific parameter value, but the two
   formulas diverge sharply below 0.55 coherence (v3.9 still gives a
   positive bonus there; v4.1 gives none) and would diverge in the opposite
   direction above ~0.83 coherence (v3.9's linear term has no ceiling; v4.1
   caps at 1.55×).
4. **PTH Acre Equity: appreciation-only → adds a payment-to-equity
   contribution.** v3.9 has no equivalent step at all. v4.1 adds: 25% of
   the agent's annual PTH housing-cost *saving* is moved from liquid
   `wealth` into illiquid `acreEquity` before appreciation is applied. See
   the new methodological finding below — this interacts with how poverty
   is measured in a way worth flagging on its own.
5. **PTF adoption: distress-only → adds Bass (1969) imitation.** v3.9:
   `ap = 0.005 + (0.015 if BLEI < precarious else 0)`. v4.1 adds
   `PTF_BASS_Q × ptfAdoptFrac` to the same base rate, so adoption
   probability rises with how many peers have already adopted.

`popAIDisp` itself, the wage-growth formula upstream of it
(`WAGE_BASE_GROWTH`/`WAGE_BLEI_BONUS`/`WAGE_OCTAVE_BONUS`), and the basic
`wealth += wage×12 − cost` accumulation step are **unchanged** across all
three versions checked so far (v3.9, v4.0, v4.1) — this matters for
interpreting the results below, since it means the aggregate-wage-income
demand proxy is measuring the same mechanism throughout even though the
*wealth*-side poverty metric now reflects a materially different model.

### New finding (this run): a port-fidelity gap in the reference
implementation's median-wealth calculation, present since v3.9

While re-deriving `calcMetrics()`, the v3.9-targeting Python script was
found to clamp wealth to ≥0 before computing the median poverty-relevant
wealth figure:
`ws = sorted(max(0.0, a['wealth']) for a in agents)`. The actual `index.html`
— in v4.1 and, from a source-history read, apparently since well before
v3.9 too — does **not** apply this clamp when computing the median (only a
*separate* Gini/net-wealth calculation clamps to zero, for a different,
unrelated reason: avoiding a divide-by-zero in the Gini formula when total
wealth sums to zero). This means the Python reference implementation's
poverty figure was always correct (both versions compute it identically,
from raw wealth), but its **median wealth** figure has been silently
different from what the real tool would report whenever a non-trivial
share of agents sit below zero wealth (bounded by `WEALTH_FLOOR=−10000`).
Under the Reference preset specifically this effect is small — median
wealth sits well above zero throughout the 25-year run in every scenario
checked — but it is not zero, and it would matter more under stress
presets. **Fixed in this revision** (`calc_metrics_v41`, and noted
explicitly in `calc_metrics_v39`'s docstring rather than silently changed,
so a reader can still reproduce the *original* v3.9 script's exact
behavior if needed). This was caught by the discipline of re-deriving
`calcMetrics()` from source rather than assuming a previously-working
function needed no re-check — worth naming as a generalizable lesson
alongside the project's existing "verify before proceeding" principle.

### New finding (this run): the v4.0 PTH Acre-Equity mechanism mechanically
raises measured wealth-poverty for PTH participants, independent of any
real change in their economic position

This is the most consequential new finding from this pass, and is distinct
from a bug — it's a definitional interaction worth flagging for whoever
next revises either NEEC's own C1.1/C1.5 measurement protocol or the sim's
poverty/wealth KPI.

`calcMetrics()` computes poverty and median wealth from `a.wealth` alone —
it does not include `a.acreEquity`. Mechanism #4 above (new in v4.0) moves
25% of a PTH participant's annual housing-cost saving *out of* `a.wealth`
and *into* `a.acreEquity` every year, before appreciation. The sim's own
in-app documentation is explicit that this "does not reintroduce new
wealth" in an accounting sense (appreciation is halved for liquidity, the
rest tracked illiquidly) — and that's correct as an accounting statement.
But it is not a poverty-neutral statement: a PTH participant's *measured*
wealth-poverty status can now be worse purely because a real, non-trivial
asset (home equity) is deliberately excluded from the metric that
determines whether they count as poor. This has a plausible real-world
analogue (illiquid home equity genuinely doesn't cover this month's
groceries) but it also means pre-v4.0 and v4.1 cross-validation runs are
not fully comparable on the poverty/median-wealth figures specifically for
scenarios with meaningful PTH uptake, independent of anything about
automation.

**This finding is reported, not fully attributed.** Isolating exactly how
much of the year-20/year-25 poverty-rate shift between v3.9 and v4.1
mechanics (below) is due to this mechanism specifically, versus the slower
FBS-gated octave advancement or the changed conversion ceiling, would
require an ablation run (v4.1 mechanics with the PTH equity-contribution
step artificially disabled, holding everything else fixed) that was not
performed in this pass. Flagged as a natural, cheap follow-up for whoever
next touches this script — the ablation machinery `runYear()` already
supports (by constructing a modified `p` dict) makes this a small addition,
not a new capability.

### Step 4: Full cross-validation — v3.9 mechanics (freshly re-run) vs. v4.1
mechanics, matched seeds/n/years

Both runs below use the identical protocol: Reference preset, 500 agents,
25 years, seeds `(1, 2, 3, 4, 5, 42, 99, 777)`. The v3.9 run uses the
*unmodified* legacy functions (renamed `_v39` in the updated script, not
edited) — a genuine re-run of the old mechanics, not a citation of Run
Record #1's rounded prose. This also serendipitously resolved an apparent
discrepancy: Run Record #1's published "mean 11.6%, sd 0.7" (off) / "mean
12.0%, sd 0.7" (on) figures turn out to correspond to **year 20** of the
25-year run, not year 25 as the final-value-only `cross_validate()`
function on its own would suggest — confirmed by checking both years
explicitly (see table). This isn't a new problem introduced by this
revision; it's a pre-existing ambiguity in how Run Record #1's prose
described "plateaus... by year 20" that this pass resolved by checking
both reporting points rather than assuming one.

| | Year 20, mean (sd) | Year 25, mean (sd) |
|---|---|---|
| **v3.9 mechanics, automation OFF** | poverty 11.57% (0.69) | poverty 11.95% (0.87), median wealth $107,755* |
| **v3.9 mechanics, automation ON** | poverty 11.97% (0.74) | poverty 12.88% (1.01), median wealth $103,101* |
| **v4.1 mechanics, automation OFF** | poverty 14.65% (1.64), wealth $82,191 | poverty 13.50% (1.92), median wealth $99,645 |
| **v4.1 mechanics, automation ON** | poverty 16.25% (1.62), wealth $79,099 | poverty 15.95% (1.68), median wealth $93,053 |

*v3.9 median-wealth figures use the corrected (unclamped) convention
retroactively for comparability, not the original script's clamped
convention — the two differ negligibly at these specific wealth levels,
confirmed by spot-check, since wealth stays well above zero throughout.

Aggregate wage income (demand proxy), automation ON as % of no-automation
baseline at year 25: **40.7% under v3.9 mechanics, 40.7% under v4.1
mechanics** — unchanged to one decimal place. This is exactly what the
mechanism diff above predicts: none of the five things that changed in
v4.0 touch the wage-growth/`popAIDisp` pathway that this proxy measures,
so it shouldn't have moved, and it didn't.

**Reading the poverty-rate comparison.** Two things move together and
should not be conflated: (a) v4.1 mechanics show *higher absolute poverty*
than v3.9 mechanics in both automation conditions (e.g., 13.50% vs. 11.95%
off, at year 25) — plausibly connected to the Acre-Equity finding above,
not yet isolated; and (b) v4.1 mechanics show a *clearer automation effect*
than v3.9 did — a 2.45-point on/off gap at year 25 (15.95 vs. 13.50) versus
v3.9's 0.93-point gap (12.88 vs. 11.95), with the v4.1 gap holding up
across the whole yr20–yr25 window rather than only appearing at one point.
Given the sd's involved (roughly 1.6–1.9 points per condition), the v4.1
gap is more clearly outside stochastic noise than v3.9's was, though
neither reaches anything resembling the severity NEEC's 50%/70%
displacement scenarios describe — consistent with, and now more sharply
illustrating, Run Record #1's standing finding.

Both mechanics versions remain far from NEEC's C1.4 pass threshold
(poverty <8%, aggregate demand >85% of baseline) and from C1.1's cited 98%
elimination figure, at every checked year and under both automation
settings.

### Step 4b (new this run): cross-check against literally-extracted v4.1
JavaScript, executed in Node.js

No browser is available in this environment, so a literal "Research Export
→ Download CSV" cross-check (Appendix G.4 Step 4's stated preference) could
not be performed. As the next-best available substitute, the relevant v4.1
functions (`CFG`, `szhTheta`, `agentBLEI`, `makeAgent`, `runYear`, a
minimal `calcMetrics`) were extracted essentially verbatim from
`index.html` and executed directly under Node v22, using the real
`mulberry32` PRNG and the same 8 seeds, same Reference preset, same 25-year
horizon (`neec_c14_v41_realjs_check.js`, included with this run record).
This eliminates port-fidelity risk for the mechanics themselves; the
residual risk is transcription error in the extraction (mitigated by
building it directly from the same source text used for the Python port,
function by function) and — irrelevantly here — RNG-stream non-equivalence
between Python's Mersenne Twister and JS's mulberry32 (not a concern, since
neither run claims seed-for-seed identity with the other; both are
independent 8-draws used only for a mean/sd spread, exactly as the existing
cross-language protocol already treats them).

| | Node (real extracted JS), yr 25 | Python port, yr 25 |
|---|---|---|
| Poverty, automation OFF | 14.10% (sd 1.17) | 13.50% (sd 1.92) |
| Poverty, automation ON | 16.07% (sd 1.52) | 15.95% (sd 1.68) |
| Median wealth, OFF | $97,950 | $99,645 |
| Median wealth, ON | $91,658 | $93,053 |
| Demand ratio (ON/OFF), yr 25 | 41.0% | 40.7% |

Agreement is close across every metric despite fully independent RNG
streams — within 0.6 points of poverty, within $1,700 of median wealth,
within 0.3 points of the demand ratio. This is treated as a positive
validation of the Python port's fidelity to the real v4.1 mechanics, and
resolves (for this run, not permanently) the standing "discrepancies
should be assumed until checked" caveat this script's own docstring
carries. The year-by-year trajectory also confirms the mechanism timing
directly: automation ON and OFF are byte-identical through year 5 (as
`AI_DISPLACEMENT_YEAR_1=5` requires) and first diverge at year 6, exactly
as the constants specify — see `neec_c14_v41_realjs_yearbyyear.csv`.

### Status vs. NEEC C1.1/C1.4 thresholds

Unchanged in kind from Run Record #1, sharper in degree: the simulation's
population-wide automation mechanism remains structurally incapable of
producing anything resembling a 50% or 70% population-displacement
scenario (the standing framing mismatch, Appendix G.2, holds — the 10-point
annual cap on wage-growth drag is a ceiling on how much automation can slow
wage growth, not a lever for modeling large-scale job loss, and this is
unchanged in v4.1). At the closest available analogue — the low end of
NEEC's stress-test range — wealth-based poverty (13.5–16.0% across
mechanics versions and automation settings) exceeds C1.4's <8% pass
threshold and is far from C1.1's cited 98% elimination figure. The
aggregate-demand proxy fails C1.4's >85%-of-baseline threshold outright
under automation (40.7–41.0% of baseline by year 25) — though, per the
mechanism diff above, this specific number is unaffected by any of the
v4.0/v4.1 changes and should be read as measuring something narrower
(wage-income growth specifically) than "aggregate demand" in the fuller
sense C1.4 intends, since CCO/PTF/PTH wealth accumulation is substantially
decoupled from wages in this model.

### Recommended follow-up (for whoever next updates this script)

1. **Ablation-isolate the PTH Acre-Equity poverty-measurement interaction**
   flagged above — cheap to add (one modified `p` dict, no new machinery),
   and would let a future write-up state a specific attribution instead of
   "not yet isolated."
2. **Re-verify all three re-confirmed findings again against v4.2+** when
   it ships, per this protocol's standing instructions — none of them are
   guaranteed to still hold, and the discipline of re-checking rather than
   assuming carried this run record's actual new content (the PTH finding
   and the median-clamp fix were both caught only by re-deriving from
   source rather than trusting the prior pass).
3. **If browser/Node access becomes available together**, run
   `neec_c14_v41_realjs_check.js` and compare its CSV output against a
   literal Research-Export download from the live tool — this run used
   Node as the strongest available substitute for that step, not a
   replacement for it.
4. Consider whether Appendix G.4's own protocol text should be updated to
   explicitly include a "grep every newly-introduced CFG constant for
   usage" step (Step 2, effectively) — this is what caught `SZH_PTF_BONUS`
   in the first place and is cheap enough to be routine rather than
   incidental to a broader audit.
