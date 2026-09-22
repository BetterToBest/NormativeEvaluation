/* ============================================================================
 * neec_c14_v42_realjs_check.js
 * ============================================================================
 * Companion to neec_c14_v41_realjs_check.js, retargeted to v4.2.
 *
 * PROVENANCE NOTE (important, see Run Record #3): the /mnt/project/index.html
 * file mounted for this session is still the v4.1 build (verified: zero
 * occurrences of "makeLatentAgent", md5 identical to a fresh v4.1 copy). The
 * v4.2 source used to write this file was supplied directly in this
 * conversation, not read from /mnt/project/. Every function below was checked
 * against that v4.2 source line-by-line before inclusion. This discrepancy
 * (project mount not yet reflecting the v4.2 upload) is flagged in this
 * session's handoff for the next session to confirm/resolve.
 *
 * WHAT CHANGED v4.1->v4.2 (per the v4.2 changelog + direct comparison against
 * the functions neec_c14_v41_realjs_check.js already extracted from v4.1):
 *   - runYear(), agentBLEI(), calcMetrics()'s poverty/median logic, and every
 *     CFG constant relevant to C1.4/C1.1 are BYTE-IDENTICAL between v4.1 and
 *     v4.2 (confirmed by direct textual comparison, not assumed).
 *   - Population construction changed substantially: v4.1's makeAgent() drew
 *     three eligibility uniforms (uCCO/uPTF/uPTH) via short-circuit `&&`,
 *     consuming a variable number of RNG calls depending on which subsystems
 *     were toggled on. v4.2 replaces this with makeLatentAgent() (draws all
 *     three unconditionally, plus wealth/wage/octaveShape/qualityZ/
 *     automationRisk/lambda) + instantiateAgent() (a pure, zero-RNG-call
 *     function that turns one latent draw into a scenario-specific agent).
 *   - This means a given seed's RNG call SEQUENCE during population
 *     construction differs between v4.1 and v4.2 -- seed-for-seed identical
 *     reproduction across versions should NOT be expected. What's being
 *     tested here is whether the AGGREGATE, cross-seed statistics (which is
 *     all the NEEC C1.4 protocol actually uses) move materially or stay
 *     within the same noise band, given the underlying formulas/distributions
 *     are unchanged.
 *   - Also new in v4.2: a structural System Stability metric and expanded
 *     validation-suite checks. Neither touches poverty/wealth/demand
 *     calculations and both are out of scope for this check, exactly as
 *     Gini/BLEI-tier/FBS-detail machinery was already out of scope in the
 *     v4.1 checker.
 *
 * SCOPE (unchanged from v4.1 checker): poverty rate, median wealth, and
 * aggregate wage income (demand proxy) per year, Reference preset, 8 seeds,
 * 25 years, automation on vs off. One unified seeded stream per scenario run
 * (population then simulation) -- the same simplification the v4.1 checker
 * already used relative to the live tool's internal three-population
 * (main/baseline/CCO-only) offset-stream scheme, which exists for the live
 * tool's own three-way UI comparison and isn't needed for a single-scenario
 * aggregate check. This was already true for v4.1; it isn't a new
 * simplification introduced for v4.2.
 * ==========================================================================*/

'use strict';

// ---- CFG: verified byte-identical to neec_c14_v41_realjs_check.js's CFG ----
var CFG = {
  POVERTY_LINE: 25000, BLEI_PRECARIOUS_MAX: 30,
  BASE_DAILY_COST: 68.33, CCO_PTH_DAILY_COST: 31.67,
  SZH_ALL_RESIDENTS: 0.06, SZH_PTF_BONUS: 0.05, // still present in CFG, still unreferenced by any formula below (re-confirmed for v4.2)
  SZH_THETA_THRESHOLD: 0.55, SZH_THETA_MAX_COH: 0.90, SZH_THETA_MAX: 0.25,
  PROG_PIVOT: 3.0, PROG_RATE: 0.040, PROG_TAX_MAX: 0.75,
  SIM_COST_SCALE: 1500,
  WAGE_MEDIAN_SIU: 35,
  WEALTH_FLOOR: -10000,
  WAGE_BASE_GROWTH: 0.010, WAGE_BLEI_BONUS: 0.008, WAGE_OCTAVE_BONUS: 0.003,
  AI_DISPLACEMENT_YEAR_1: 5, AI_DISPLACEMENT_YEAR_2: 15,
  AI_DISPLACEMENT_RATE_1: 0.012, AI_DISPLACEMENT_RATE_2: 0.022,
  PHI_RATIO: 1.618, PHI_QUALITY_THRESH: 0.70,
  FBS_LAMBDA_LO: 0.001, FBS_LAMBDA_HI: 0.008,
  FBS_EDC_RESIDUAL_BASE: 0.12, FBS_EDC_RESIDUAL_PTH: 0.025,
  FBS_CIP_LAMBDA_BOOST: 0.20,
  PTH_EQUITY_CONTRIB_SHARE: 0.25,
  PTF_BASS_Q: 0.05
};
CFG.SIU_TO_USD = (CFG.BASE_DAILY_COST * 365) / CFG.SIM_COST_SCALE;

// ---- PRNG: mulberry32, verbatim, unchanged ----
var RNG = Math.random;
function mulberry32(seed) {
  var s = seed >>> 0;
  return function () {
    s = (s + 0x6D2B79F5) >>> 0;
    var t = Math.imul(s ^ (s >>> 15), 1 | s);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

// ---- distribution helpers: verbatim, unchanged ----
function lognormal(mu, sigma) {
  var u = Math.max(1e-14, 1 - RNG()), v = RNG();
  return Math.exp(mu + sigma * Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v));
}
function betaDist(a, b) { var x = gammaDist(a); return x / (x + gammaDist(b)); }
function gammaDist(a) {
  if (a < 1) return gammaDist(1 + a) * Math.pow(Math.max(1e-14, RNG()), 1 / a);
  for (var i = 0; i < 5000; i++) {
    var u = RNG(), v = RNG(), y = Math.tan(Math.PI * u), x = Math.sqrt(2 * a - 1) * y + a - 1;
    if (x > 0 && v <= (1 + y * y) * Math.exp((a - 1) * Math.log(x / (a - 1)) - Math.sqrt(2 * a - 1) * y)) return x;
  }
  return a;
}
// NEW in v4.2: standardNormal(), used by makeLatentAgent() for qualityZ.
// Mathematically the same Box-Muller draw lognormal() already used internally
// (u,v -> sqrt(-2 ln u) cos(2 pi v)) -- v4.2 factors it out so the raw Z score
// can be stored on the latent agent and the lognormal transform (which needs
// scenario-specific maxMult) applied later in instantiateAgent().
function standardNormal() {
  var u = Math.max(1e-14, 1 - RNG()), v = RNG();
  return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v);
}

// ---- szhTheta(): verbatim, unchanged ----
function szhTheta(coh) {
  coh = isNaN(coh) ? 0 : coh;
  if (coh < CFG.SZH_THETA_THRESHOLD) return 0;
  return Math.min(CFG.SZH_THETA_MAX, (coh - CFG.SZH_THETA_THRESHOLD) / (CFG.SZH_THETA_MAX_COH - CFG.SZH_THETA_THRESHOLD) * CFG.SZH_THETA_MAX);
}

// ---- agentBLEI(): verbatim except local var renamed gamma_ (same naming-
// hygiene reason documented in neec_c14_v41_realjs_check.js: avoids shadowing
// the gammaDist() PRNG helper's name in THIS standalone file only -- zero
// effect on arithmetic, index.html itself has no such collision either). ----
function agentBLEI(a, buAlloc, ccoOn, pthOn, szhOn, szhCoh, ptfOn) {
  var liquid = Math.max(0, (isNaN(a.wealth) ? 0 : a.wealth) * 0.20);
  var gamma_ = (ccoOn && a.inCCO) ? 0.20 : 0.12;
  var mInc = Math.max(isNaN(a.wage) ? 1 : a.wage, 0.1) * CFG.SIU_TO_USD;
  var buFood = (ccoOn && a.inCCO && buAlloc > 0) ? buAlloc * (990 / 1200) : 0;
  var szhD = szhOn ? szhCoh * CFG.SZH_ALL_RESIDENTS : 0;
  if (szhOn && ptfOn && a.inPTF) szhD += szhTheta(szhCoh) * 0.20;
  var baseCost = (ccoOn && a.inCCO && pthOn && a.inPTH) ? CFG.CCO_PTH_DAILY_COST : CFG.BASE_DAILY_COST;
  var dc = Math.max(baseCost * (1 - szhD), 0.1);
  var r = (liquid + gamma_ * mInc + buFood) / dc;
  return (isNaN(r) || !isFinite(r)) ? 0 : Math.max(0, r);
}

// ---- v4.2 population construction: makeLatentAgent / instantiateAgent /
// makeAgent wrapper -- extracted verbatim from the v4.2 source. THIS is the
// actual v4.1->v4.2 delta relevant to this protocol. ----
function makeLatentAgent() {
  var uCCO = RNG(), uPTF = RNG(), uPTH = RNG(); // unconditional draws (the v4.2 fix)
  return {
    uCCO: uCCO, uPTF: uPTF, uPTH: uPTH,
    wealth: lognormal(10.5, 1.2), wage: lognormal(3.5, 0.5),
    octaveShape: betaDist(2, 5), qualityZ: standardNormal(),
    automationRisk: 0.2 + RNG() * 0.8,
    lambda: CFG.FBS_LAMBDA_LO + RNG() * (CFG.FBS_LAMBDA_HI - CFG.FBS_LAMBDA_LO)
  };
}
function instantiateAgent(latent, cfgP) {
  var qN = cfgP.cip ? (1 - cfgP.cipDemo * 0.5) : 1.0;
  var maxOct = cfgP.maxOct || 1, maxMult = cfgP.maxMult || 1;
  var inPTH = !!(cfgP.pth && latent.uPTH < cfgP.pthUptake);
  return {
    wealth: latent.wealth, wage: latent.wage,
    octave: Math.floor(latent.octaveShape * maxOct),
    quality: Math.min(maxMult, Math.max(0, Math.exp(Math.log(maxMult * 0.5) + 0.4 * latent.qualityZ) * qN)),
    automationRisk: latent.automationRisk, lambda: latent.lambda,
    inCCO: !!(cfgP.ccoOn && latent.uCCO < cfgP.partRate),
    inPTF: !!(cfgP.ptf && latent.uPTF < cfgP.ptfShare),
    inPTH: inPTH,
    buBalance: 0, acreEquity: inPTH ? 5000 : 0
  };
}
function makeAgent(cfgP) { return instantiateAgent(makeLatentAgent(), cfgP); }

// ---- runYear(): verified byte-identical to v4.1 (neec_c14_v41_realjs_check.js).
// Copied verbatim; not re-derived, so any transcription slip here would show
// up as a real mechanical difference from v4.1, which the comparison below
// would catch. ----
function runYear(agentSet, yr, p, automationOn) {
  var pthApprBonus = p.szh ? p.szhCoh * 0.01 : 0;
  var szhThetaVal = p.szh ? szhTheta(p.szhCoh) : 0;
  var ptfConvBonus = 1.30 + ((p.szh && p.ptf) ? szhThetaVal : 0);
  var szhPartBoost = (p.szh && p.ccoOn) ? szhThetaVal * 0.16 : 0;
  var inflRate = p.inflRate || 0;
  if (p.ptf && inflRate > 0) inflRate *= (1 - p.ptfShare * 0.5);
  if (p.pth && inflRate > 0) inflRate *= 0.90;
  var simCost = CFG.SIM_COST_SCALE * Math.pow(1 + inflRate, yr);
  var dollarCost = CFG.BASE_DAILY_COST * 365 * Math.pow(1 + inflRate, yr);
  var popShock = 1.0; // Reference preset: shock off
  var ptfAdoptFrac = 0;
  if (p.ptf && p.ptfShare > 0) {
    var ptfCount = 0; agentSet.forEach(function (a) { if (a.inPTF) ptfCount++; });
    ptfAdoptFrac = ptfCount / Math.max(1, agentSet.length);
  }
  var popAIDisp = 0;
  if (automationOn) {
    if (yr >= CFG.AI_DISPLACEMENT_YEAR_2) popAIDisp = CFG.AI_DISPLACEMENT_RATE_1 * (CFG.AI_DISPLACEMENT_YEAR_2 - CFG.AI_DISPLACEMENT_YEAR_1) + CFG.AI_DISPLACEMENT_RATE_2 * (yr - CFG.AI_DISPLACEMENT_YEAR_2 + 1);
    else if (yr >= CFG.AI_DISPLACEMENT_YEAR_1) popAIDisp = CFG.AI_DISPLACEMENT_RATE_1 * (yr - CFG.AI_DISPLACEMENT_YEAR_1 + 1);
    popAIDisp = Math.min(0.10, popAIDisp);
  }
  var totalWageIncome = 0;
  agentSet.forEach(function (a) {
    if (isNaN(a.wealth)) a.wealth = 0;
    if (isNaN(a.wage) || a.wage <= 0) a.wage = 1;
    var agentVar = 0.90 + RNG() * 0.20, incomeShock = popShock * agentVar;
    var bleiCheck = agentBLEI(a, p.bu, p.ccoOn, p.pth, p.szh, p.szhCoh, p.ptf);
    var wg = CFG.WAGE_BASE_GROWTH;
    if (bleiCheck > CFG.BLEI_PRECARIOUS_MAX) {
      var drFactor = 1 / (1 + 0.5 * Math.max(0, a.wage / CFG.WAGE_MEDIAN_SIU - 1));
      wg += CFG.WAGE_BLEI_BONUS * Math.max(0.1, drFactor);
    }
    wg += a.octave * CFG.WAGE_OCTAVE_BONUS;
    if (p.cip) wg += p.cipDemo * 0.005;
    wg -= popAIDisp * (a.automationRisk || 0.5);
    a.wage = Math.max(a.wage * 0.80, a.wage * (1 + wg));
    if (isNaN(a.wage)) a.wage = 1;
    totalWageIncome += a.wage * 12;

    var cf = 1.0;
    if (p.ptf && a.inPTF) cf *= (1 - (p.szh ? 0.12 + p.szhCoh * 0.04 : 0.12));
    if (p.pth && a.inPTH) cf *= 0.65;
    if (p.ccoOn && a.inCCO && p.bu > 0) cf *= 0.80;
    a.wealth += a.wage * 12 * incomeShock - simCost * cf;
    if (isNaN(a.wealth)) a.wealth = 0;

    if (p.ccoOn && a.inCCO) {
      var decay = p.expiry < 2 ? 0 : 0.7;
      a.buBalance = Math.min(a.buBalance * decay + p.bu, p.bu * 3);
      var spend = a.buBalance * (0.60 + RNG() * 0.30); a.buBalance -= spend;
      if (p.cip && RNG() < p.cipDemo * 0.15) a.quality = Math.min(p.maxMult, a.quality + 0.1);
      var octCeiling = 1 + (a.octave / Math.max(1, p.maxOct)) * (Math.max(1, p.maxMult) - 1);
      var qualityFactor = Math.min(1, a.quality / Math.max(1, p.maxMult));
      var baseRate = 1 + qualityFactor * (octCeiling - 1);
      var phi = (p.phi && a.quality > p.maxMult * CFG.PHI_QUALITY_THRESH) ? CFG.PHI_RATIO : 1.0;
      var ptfB = (p.ptf && a.inPTF) ? ptfConvBonus : 1.0;
      var cipB = p.cip ? (1 + p.cipDemo * 0.12) : 1.0;
      var rate = Math.min(baseRate * phi * ptfB, p.maxMult * (p.phi ? CFG.PHI_RATIO : 1.0));
      var bTax = p.cip ? p.tax * (1 - p.cipDemo * 0.18) : p.tax;
      var progTax = Math.min(CFG.PROG_TAX_MAX, bTax + Math.max(0, (rate - CFG.PROG_PIVOT) * CFG.PROG_RATE));
      var convGain = spend * rate * (1 - progTax) * cipB * incomeShock;
      a.wealth += convGain;
      if (isNaN(a.wealth)) a.wealth = 0;

      if (a.octave < p.maxOct) {
        var Yusd = a.wage * CFG.SIU_TO_USD;
        var cBasicMonthly = (dollarCost * cf) / 12;
        var edcResidual = (p.pth && a.inPTH) ? CFG.FBS_EDC_RESIDUAL_PTH : CFG.FBS_EDC_RESIDUAL_BASE;
        var fbs = Math.max(0, Yusd + p.bu - cBasicMonthly - edcResidual * Yusd);
        var lam = (typeof a.lambda === 'number' && !isNaN(a.lambda)) ? a.lambda : (CFG.FBS_LAMBDA_LO + CFG.FBS_LAMBDA_HI) / 2;
        if (p.cip) lam *= (1 + p.cipDemo * CFG.FBS_CIP_LAMBDA_BOOST);
        var pAdvance = 1 - Math.exp(-lam * fbs);
        if (RNG() < pAdvance) a.octave++;
      }
      if (RNG() < szhPartBoost && !a.inPTF && p.ptf) { a.inPTF = RNG() < p.ptfShare; }
    }
    if (p.pth && a.inPTH) {
      var cfWithoutPTH = cf / 0.65;
      var pthSaving = Math.max(0, simCost * cfWithoutPTH * (1 - 0.65));
      var equityContrib = pthSaving * CFG.PTH_EQUITY_CONTRIB_SHARE;
      a.acreEquity += equityContrib; a.wealth -= equityContrib;
      var ar = 0.030 + RNG() * 0.020 + pthApprBonus;
      var appr = a.acreEquity * ar; a.acreEquity += appr; a.wealth += appr * 0.5;
    }
    if (p.ptf && !a.inPTF && p.ptfShare > 0 && yr > 0) {
      var ap = 0.005 + CFG.PTF_BASS_Q * ptfAdoptFrac;
      if (bleiCheck < CFG.BLEI_PRECARIOUS_MAX) ap += 0.015;
      if (RNG() < ap) a.inPTF = true;
    }
    if (a.wealth < CFG.WEALTH_FLOOR) a.wealth = CFG.WEALTH_FLOOR;
  });
  return totalWageIncome;
}

// ---- calcMetrics(): minimal poverty/median port, verified byte-identical
// logic to v4.2's real calcMetrics() poverty/median lines (no >=0 clamp for
// median -- matches the Run Record #2 port-fidelity finding, re-confirmed
// unchanged in v4.2). Gini/EDC intentionally out of scope (see file header). ----
function calcMetrics(agentSet) {
  var ws = agentSet.map(function (a) { return isNaN(a.wealth) ? 0 : a.wealth; }).sort(function (a, b) { return a - b; });
  var n = ws.length;
  var pov = ws.filter(function (w) { return w < CFG.POVERTY_LINE; }).length / n;
  var med = n % 2 === 0 ? (ws[n / 2 - 1] + ws[n / 2]) / 2 : ws[Math.floor(n / 2)];
  return { pov: pov, med: med };
}

// ---- driver ----
function runScenario(seed, years, automationOn, n) {
  RNG = mulberry32(seed);
  var p = {
    bu: 1200, maxOct: 6, expiry: 1, tax: 0.12, maxMult: 9, partRate: 0.78,
    ptfShare: 0.18, pthUptake: 0.20, szhCoh: 0.72, cipDemo: 0.65,
    phi: true, ptf: true, pth: true, szh: true, cip: true, ccoOn: true, inflRate: 0
  };
  var agents = [];
  for (var i = 0; i < n; i++) agents.push(makeAgent(p));
  var pov = [], wealth = [], wage = [];
  for (var yr = 0; yr < years; yr++) {
    var w = runYear(agents, yr, p, automationOn);
    var m = calcMetrics(agents);
    pov.push(m.pov * 100); wealth.push(m.med); wage.push(w);
  }
  return { pov: pov, wealth: wealth, wage: wage };
}

function mean(a) { return a.reduce(function (x, y) { return x + y; }, 0) / a.length; }
function sd(a) { var m = mean(a); return Math.sqrt(a.reduce(function (s, x) { return s + (x - m) * (x - m); }, 0) / Math.max(1, a.length - 1)); }

var SEEDS = [1, 2, 3, 4, 5, 42, 99, 777];
var YEARS = 25, N = 500;

var finalOn = { pov: [], wealth: [] }, finalOff = { pov: [], wealth: [] };
var year20On = { pov: [], wealth: [] }, year20Off = { pov: [], wealth: [] };
var seriesOn = { pov: [], wealth: [], wage: [] }, seriesOff = { pov: [], wealth: [], wage: [] };

SEEDS.forEach(function (seed) {
  var off = runScenario(seed, YEARS, false, N);
  var on = runScenario(seed, YEARS, true, N);
  finalOff.pov.push(off.pov[off.pov.length - 1]); finalOff.wealth.push(off.wealth[off.wealth.length - 1]);
  finalOn.pov.push(on.pov[on.pov.length - 1]); finalOn.wealth.push(on.wealth[on.wealth.length - 1]);
  year20Off.pov.push(off.pov[19]); year20Off.wealth.push(off.wealth[19]);
  year20On.pov.push(on.pov[19]); year20On.wealth.push(on.wealth[19]);
  seriesOff.pov.push(off.pov); seriesOff.wealth.push(off.wealth); seriesOff.wage.push(off.wage);
  seriesOn.pov.push(on.pov); seriesOn.wealth.push(on.wealth); seriesOn.wage.push(on.wage);
});

console.log('=== v4.2 REAL-JS cross-validation (Node execution of v4.2 population-construction + unchanged runYear/calcMetrics) ===');
console.log('Reference preset, ' + N + ' agents, ' + YEARS + ' years, seeds=' + SEEDS.join(','));
console.log('');
console.log('Year 20 summary:');
console.log('  Automation OFF: poverty% mean=' + mean(year20Off.pov).toFixed(2) + ' sd=' + sd(year20Off.pov).toFixed(2) + '  | median wealth mean=$' + Math.round(mean(year20Off.wealth)));
console.log('  Automation ON : poverty% mean=' + mean(year20On.pov).toFixed(2) + ' sd=' + sd(year20On.pov).toFixed(2) + '  | median wealth mean=$' + Math.round(mean(year20On.wealth)));
console.log('Final-year (yr ' + YEARS + ') summary:');
console.log('  Automation OFF: poverty% mean=' + mean(finalOff.pov).toFixed(2) + ' sd=' + sd(finalOff.pov).toFixed(2) + '  | median wealth mean=$' + Math.round(mean(finalOff.wealth)));
console.log('  Automation ON : poverty% mean=' + mean(finalOn.pov).toFixed(2) + ' sd=' + sd(finalOn.pov).toFixed(2) + '  | median wealth mean=$' + Math.round(mean(finalOn.wealth)));

var rows = ['year,poverty_pct_automation_on,poverty_pct_automation_off,median_wealth_automation_on,median_wealth_automation_off,aggregate_wage_income_pct_of_no_automation_baseline'];
for (var y = 0; y < YEARS; y++) {
  var povOnY = seriesOn.pov.map(function (s) { return s[y]; });
  var povOffY = seriesOff.pov.map(function (s) { return s[y]; });
  var wealthOnY = seriesOn.wealth.map(function (s) { return s[y]; });
  var wealthOffY = seriesOff.wealth.map(function (s) { return s[y]; });
  var wageOnY = seriesOn.wage.map(function (s) { return s[y]; });
  var wageOffY = seriesOff.wage.map(function (s) { return s[y]; });
  var demandPct = (mean(wageOnY) / mean(wageOffY)) * 100;
  rows.push([y + 1, mean(povOnY).toFixed(2), mean(povOffY).toFixed(2), Math.round(mean(wealthOnY)), Math.round(mean(wealthOffY)), demandPct.toFixed(2)].join(','));
}
require('fs').writeFileSync('neec_c14_v42_realjs_yearbyyear.csv', rows.join('\n') + '\n');
console.log('');
console.log('Year-by-year CSV written: neec_c14_v42_realjs_yearbyyear.csv');
console.log('yr25 demand%=' + rows[25].split(',')[5]);
