'use strict';
/* cco_simulation_checks_s51.js -- NEEC rescoring pass, stage 2, group 2.1: runs of the Compassionism Simulation's
 * engine at v4.20 for CCO-PTF-CIP-SZH's units that rest on the design's modelling: C1.1 (class I: the Societal
 * Poverty Line, the reference run and the stress run), C1.2b (the wealth Gini), C1.4 (Paper v1.4 Appendix G's
 * protocol, Run Record #4), C3.3 (the one compound scenario the engine runs) and C3.1 (coverage).
 *
 * The engine is harness.js from github.com/BetterToBest/compassionism-simulation at commit 5a7a7b1 (v4.20), the
 * version the owner announced on 2026-09-26 and the one github.io serves; index.html at the same commit is pinned by
 * digest for its presets and its two recession functions, which v4.17 ported into harness.js verbatim (checked
 * below). No line of either file is altered: the script appends one line exposing functions harness.js already
 * defines and loads the result as a module, as cco_simulation_checks_s40.js did.
 *
 * The runner below mirrors harness.js's runScenario() line for line (population on seed+700003, the recession path
 * on its own seed+700000 stream, the trajectory on mulberry32(seed)) and records the population at chosen years; the
 * functions runScenario() calls between years draw no random number. Check 2 asserts that it reproduces
 * runScenario() exactly, on every seed and every scenario used, before any table is trusted.
 *
 * Measures. The engine's own (v4.17-v4.18): wealth poverty (net wealth below $25,000), BLEI poverty (under 30 days
 * of runway), relative income poverty (cash income below 60% of the scenario's median; cash income = wage income
 * after the income shock + CCO conversion proceeds), the same with the in-kind value of cost relief added, basket
 * poverty net and gross, housing distress and the extreme-poverty overlay. One computed here from the engine's own
 * per-agent cash income: the World Bank Societal Poverty Line, C1.1's v2.0 indicator, max($3.00, $1.30 + 50% of the
 * median) a day in 2021 PPP dollars (Foster et al., World Bank Policy Research Working Paper 11137, June 2025,
 * section 3.4.1), applied to the engine's single-adult agents at a year's 365 days in the engine's dollars (the
 * United States is the PPP numeraire), with the in-kind variant as a sensitivity. Poverty reduction is taken as
 * v2.0's C1.1 calculation states it, against the rate at the adoption year (year 0, before any year runs), and,
 * second, against the paired Baseline at year 20, as Session 40's record read it.
 *
 * Usage: node cco_simulation_checks_s51.js [harness.js] [index.html]   (defaults: beside the working directory)
 * Prints file names only. Deterministic.
 */
const fs = require('fs'), path = require('path'), crypto = require('crypto'), Module = require('module');
const hFile = path.resolve(process.argv[2] || 'harness.js');
const iFile = path.resolve(process.argv[3] || 'index.html');
const hSrc = fs.readFileSync(hFile, 'utf8'), iSrc = fs.readFileSync(iFile, 'utf8');
const md5 = s => crypto.createHash('md5').update(s).digest('hex');
const PIN = { harness: 'fe6fa4a3f82a2d572c5e6914cc2345f2', index: 'c333b6326b95586515743dba6647ca2a' };
let ok = true;
function check(cond, text) { console.log('  ' + (cond ? 'PASS' : 'FAIL') + ' ' + text); ok = ok && !!cond; }

function extract(src, name) {             // one top-level function, verbatim, by brace matching
  const start = src.indexOf('\nfunction ' + name + '(');
  if (start < 0) return null;
  let i = src.indexOf('{', start), d = 0;
  for (; i < src.length; i++) { if (src[i] === '{') d++; else if (src[i] === '}' && --d === 0) break; }
  return src.slice(start + 1, i + 1);
}
const m = new Module(hFile, module);
m.filename = hFile; m.paths = Module._nodeModulePaths(path.dirname(hFile));
m._compile(hSrc + '\nObject.assign(module.exports, { runYear, calcMetrics, instantiateAgent, makeLatentPopulation, ' +
           'bleiMetrics, incomeBasketMetrics, incomeBasketYear0, housingDistressOf, housingDistressYear0, ' +
           'extremePovertyOf, buildRecessionPath, medianOf, setRNG: function (f) { RNG = f; } });\n', hFile);
const E = m.exports, C = E.CFG;
const FI = E.FULL_INTEGRATION, ADV = E.ADVERSE_REFERENCE, ST = E.STRESS_TEST, HA = E.HIGH_AUTOMATION;

console.log('NEEC cco_simulation_checks_s51: CCO-PTF-CIP-SZH on the design\'s own engine, v4.20');
console.log('inputs: ' + path.basename(hFile) + ', ' + path.basename(iFile) + '\n');
console.log('[1] THE ENGINE');
check(md5(hSrc) === PIN.harness, path.basename(hFile) + ' md5 ' + md5(hSrc) + ' (compassionism-simulation 5a7a7b1, v4.20)');
check(md5(iSrc) === PIN.index && /VERSION:'4\.20'/.test(iSrc), path.basename(iFile) + ' md5 ' + md5(iSrc) +
      ' (same commit; META.VERSION 4.20)');
const recSame = ['updateRecession', 'buildRecessionPath'].every(n => extract(hSrc, n) && extract(hSrc, n) === extract(iSrc, n));
check(recSame, 'updateRecession and buildRecessionPath in ' + path.basename(hFile) + ' are the page\'s, character for ' +
      'character (v4.17 ported them; Session 40 had to append them)');
const ref = E.runScenario(FI, 42);
check(ref.bleiMed === 1975 && ref.bleiPovPct === 13.2 && ref.wealth === 570661 && ref.pov === 15.8 &&
      ref.gini === 0.518 && ref.stab === 88.8,
      'seed-42 Full Integration 20yr reproduces v4.20\'s documented regression: median BLEI ' + ref.bleiMed + ' d, BLEI ' +
      'poverty ' + ref.bleiPovPct + '%, median wealth $' + ref.wealth + ', wealth poverty ' + ref.pov + '%, Gini ' +
      ref.gini + ', System Stability ' + ref.stab + '%');
const preset = (s, key) => { const x = s.match(new RegExp('\\n\\s*' + key + ':\\{([^}]*)\\}')); return x ? x[1] : null; };
const asPage = p => 'bu:' + p.bu + ',oct:' + p.maxOct + ',exp:' + p.expiry + ',tax:' + Math.round(p.tax * 100) + ',mult:' +
  p.maxMult + ',agents:' + p.nAgents + ',part:' + Math.round(p.partRate * 100) + ',yrs:' + p.years + ',ptfShare:' +
  Math.round(p.ptfShare * 100) + ',pthUptake:' + Math.round(p.pthUptake * 100) + ',szh:' + Math.round(p.szhCoh * 100) +
  ',cip:' + Math.round(p.cipDemo * 100) + ',phi:' + p.phi + ',ptf:' + p.ptf + ',pth:' + p.pth + ',szh_tog:' + p.szh +
  ',cip_tog:' + p.cip + ',shock:' + p.shock + ',inflRate:' + Math.round(p.inflRate * 100) + ',automation:' + p.automation;
check([['reference', FI], ['adverse', ADV], ['stress', ST], ['hiAI', HA]].every(([k, p]) => preset(iSrc, k) === asPage(p)),
      'harness.js\'s Full Integration, Adverse Environment, Stress Test and High Automation are the page\'s presets ' +
      '(reference, adverse, stress, hiAI), field for field');
check(C.WEALTH_FLOOR === -10000 && C.LIVING_WAGE_ANNUAL === 49370 && C.AI_DISPLACEMENT_RATE_1 === 0.012 &&
      C.AI_DISPLACEMENT_RATE_2 === 0.022 && C.AI_DISPLACEMENT_YEAR_1 === 5 && C.AI_DISPLACEMENT_YEAR_2 === 15 &&
      /popAIDisp=Math\.min\(0\.10,popAIDisp\);/.test(extract(hSrc, 'runYear')) && C.TARGET_GINI === 0.25,
      'constants read from source: WEALTH_FLOOR -$10,000, LIVING_WAGE_ANNUAL $49,370, AI displacement 0.012 a year from ' +
      'year 5 and 0.022 from year 15, capped at 0.10 in runYear(); TARGET_GINI 0.25 (a constant, not an output)');

// ---- the runner --------------------------------------------------------------------------------------------------
const SPL = { floor: 3.00 * 365, intercept: 1.30 * 365, slope: 0.5 };   // 2021 PPP $/day, a year of 365 days
const splLine = med => Math.max(SPL.floor, SPL.intercept + SPL.slope * med);
const TOP = p => (p.ccoOn && p.ptf) ? 'Flourishing' : 'Comfortable';
const share = (xs, f) => xs.filter(f).length / xs.length * 100;
function snap(agents, p, y, d0) {
  let inc, ext, ib, bl;
  if (y === 0) {
    inc = agents.map(a => Math.max(isNaN(a.wage) ? 0 : a.wage, 0) * 12 * C.WAGE_TO_USD); ext = inc;
    ib = E.incomeBasketYear0(agents);
    bl = E.bleiMetrics(agents, 0, false, false, false, 0, false);           // policy-neutral, as v4.17 reads year 0
  } else {
    inc = agents.map(a => { const w = +a.yrWageUSD, c = +a.yrConvUSD; return (isNaN(w) ? 0 : w) + (isNaN(c) ? 0 : c); });
    ext = agents.map((a, i) => inc[i] + Math.max(0, (+a.yrBasketUSD || 0) - (+a.yrCostUSD || 0)));
    ib = E.incomeBasketMetrics(agents);
    bl = E.bleiMetrics(agents, p.bu, p.ccoOn, p.pth, p.szh, p.szhCoh, p.ptf, TOP(p));
  }
  const d = y === 0 ? E.housingDistressYear0(agents) : E.housingDistressOf(agents);
  const lc = splLine(E.medianOf(inc)), lx = splLine(E.medianOf(ext));
  const mN = E.calcMetrics(agents), mE = E.calcMetrics(agents, p.ccoOn, p.pth);
  return {
    spl: share(inc, v => v < lc), splX: ext.filter(v => v < lx).length / ext.length * 100,
    rel: ib.incPov, relX: ib.incPovExt, bsk: ib.basketPov, bskG: ib.basketPovGross,
    pov: mN.pov * 100, blei: (bl.tc[0] + bl.tc[1]) / bl.n * 100,
    dis: d * 100, ep: E.extremePovertyOf(d, y === 0 ? d : d0, y === 0 ? 'year0' : p).total * 100,   // per 10,000
    giniP: mN.gini, giniE: mE.gini, med: mE.med, cash: inc.reduce((s, v) => s + v, 0),
    wage: (y === 0 ? inc : agents.map(a => +a.yrWageUSD || 0)).reduce((s, v) => s + v, 0),
    part: share(agents, a => a.inCCO), splMed: E.medianOf(inc)
  };
}
function traj(p, seed, marks) {           // runScenario(), recording the population at the years in marks
  E.setRNG(E.mulberry32(seed + 700003));
  const agents = E.makeLatentPopulation(p.nAgents).map(l => E.instantiateAgent(l, p));
  const d0 = E.housingDistressYear0(agents);
  const out = { 0: snap(agents, p, 0, d0) };
  const rec = p.shock ? E.buildRecessionPath(p.years, seed) : null;
  E.setRNG(E.mulberry32(seed));
  for (let yr = 0; yr < p.years; yr++) {
    E.runYear(agents, yr, p, rec ? rec[yr] : { active: false, incomeMultiplier: 1.0, yearsLeft: 0 });
    if (marks.includes(yr + 1)) out[yr + 1] = snap(agents, p, yr + 1, d0);
  }
  return out;
}
const N = 500, SEEDS = Array.from({ length: N }, (_, i) => i + 1);
const mean = a => a.reduce((x, y) => x + y, 0) / a.length;
const M5 = [0, 5, 10, 15, 20], M25 = [0, 5, 10, 15, 20, 25];
const FI25 = Object.assign({}, FI, { years: 25 });
const RUNS = {
  FI: [FI25, M25], HA: [HA, M25], BF: [E.baselineFor(FI), M5], BFm: [E.baselineFor(FI, true), M5],
  ADV: [ADV, M5], BA: [E.baselineFor(ADV), M5], BAm: [E.baselineFor(ADV, true), M5], ST: [ST, M5]
};
const R = {};
for (const k of Object.keys(RUNS)) R[k] = SEEDS.map(s => traj(RUNS[k][0], s, RUNS[k][1]));

console.log('\n[2] THE RUNNER (N = ' + N + ' seeds, 1-' + N + ', 500 agents)');
const SC = { FI: FI, HA: HA, BF: E.baselineFor(FI), BFm: E.baselineFor(FI, true), ADV: ADV, BA: E.baselineFor(ADV),
             BAm: E.baselineFor(ADV, true), ST: ST };
const RS = {};
for (const k of Object.keys(SC)) RS[k] = SEEDS.map(s => E.runScenario(SC[k], s));
const f1 = x => +x.toFixed(1);
let bad = [];
for (const k of Object.keys(SC)) {
  const y = SC[k].years;
  SEEDS.forEach((s, i) => {
    const r = RS[k][i], t = R[k][i][y], t0 = R[k][i][0];
    const same = f1(t.pov) === r.pov && f1(t.blei) === r.bleiPovPct && +t.giniE.toFixed(3) === r.gini &&
      Math.round(t.med) === r.wealth && f1(t.rel) === r.incPov && f1(t.relX) === r.incPovExt && f1(t.bsk) === r.basketPov &&
      f1(t.bskG) === r.basketPovGross && Math.abs(t.dis - r.distress) < 1e-9 && Math.abs(t.ep / 100 - r.epTotal) < 1e-9 &&
      f1(t0.pov) === r.yearZero.pov && f1(t0.blei) === r.yearZero.bleiPovNeutral && f1(t0.rel) === r.yearZero.incPov &&
      f1(t0.bsk) === r.yearZero.basketPov && Math.abs(t0.dis - r.yearZero.distress) < 1e-9;
    if (!same) bad.push(k + ' seed ' + s);
  });
}
check(!bad.length, 'the runner reproduces runScenario() on all ' + N + ' seeds of all ' + Object.keys(SC).length +
      ' scenarios (' + Object.keys(SC).join(', ') + '): final-year wealth and BLEI poverty, EDC-adjusted Gini, median ' +
      'wealth, the four income and basket measures, housing distress and extreme poverty, and the year-0 figures' +
      (bad.length ? ' [' + bad.slice(0, 3).join('; ') + ']' : ''));
check(!/p\.years/.test(extract(hSrc, 'runYear')) && JSON.stringify(E.baselineFor(ST)) === JSON.stringify(E.baselineFor(ADV)),
      'Full Integration is run once, for 25 years, and read at year 20 as well: runYear() does not read the horizon, and ' +
      'the check above compares its year 20 with the 20-year runScenario(); the Stress Test\'s Baseline is the Adverse ' +
      'Environment\'s (recessions and automation mirrored, 3% CPI)');
// v4.20's documented N = 500 figures (CONTRIBUTING.md, v4.20 Release Notes), from runScenario() as harness.js averages them
const mr = (k, f) => mean(RS[k].map(r => r[f]));
const red = (b, s) => (b - s) / b * 100;
const fiY0pov = mean(RS.FI.map(r => r.yearZero.pov)), fiY0blei = mean(RS.FI.map(r => r.yearZero.bleiPovNeutral));
check(mr('FI', 'pov').toFixed(2) === '15.27' && mr('FI', 'bleiPovPct').toFixed(2) === '12.43' &&
      Math.round(mr('FI', 'wealth')) === 528624 && Math.round(mr('FI', 'bleiMed')) === 1834 &&
      mr('HA', 'pov').toFixed(2) === '29.16' && mr('HA', 'bleiPovPct').toFixed(2) === '26.65' &&
      Math.round(mr('HA', 'wealth')) === 340928 && Math.round(mr('HA', 'bleiMed')) === 1196 &&
      mr('ADV', 'pov').toFixed(2) === '38.42' && mr('ADV', 'bleiPovPct').toFixed(2) === '34.92' &&
      Math.round(mr('ADV', 'wealth')) === 169911 && Math.round(mr('ADV', 'bleiMed')) === 606 &&
      mr('ST', 'pov').toFixed(2) === '61.18' && mr('ST', 'bleiPovPct').toFixed(2) === '59.14',
      'v4.20\'s automation sweep reproduced (seeds 1-500, means of runs): Full Integration 15.27% / 12.43% / $528,624 / ' +
      '1,834 d; High Automation 29.16% / 26.65% / $340,928 / 1,196 d; Adverse Environment 38.42% / 34.92% / $169,911 / ' +
      '606 d; Stress Test 61.18% / 59.14% (wealth poverty / BLEI poverty / median wealth / median BLEI)');
check(red(mr('BF', 'pov'), mr('FI', 'pov')).toFixed(1) === '78.6' && red(mr('BFm', 'pov'), mr('FI', 'pov')).toFixed(1) === '69.7' &&
      red(fiY0pov, mr('FI', 'pov')).toFixed(1) === '59.6' && red(mr('BF', 'bleiPovPct'), mr('FI', 'bleiPovPct')).toFixed(1) === '82.4' &&
      red(mr('BFm', 'bleiPovPct'), mr('FI', 'bleiPovPct')).toFixed(1) === '74.6' && fiY0blei.toFixed(1) === '10.3' &&
      red(mr('BF', 'basketPov'), mr('FI', 'basketPov')).toFixed(1) === '87.9' &&
      mean(RS.FI.map(r => r.yearZero.basketPov)).toFixed(1) === '66.3',
      'v4.20\'s refreshed headline reproduced: wealth poverty 78.6% below the shipped Baseline, 69.7% below the matched ' +
      'one, 59.6% below year 0; BLEI poverty 82.4% and 74.6%, ending above its year-0 10.3%; net basket poverty 87.9% ' +
      'below the shipped Baseline, the highest; 66.3% start in basket poverty');

// ---- tables ------------------------------------------------------------------------------------------------------
const P = x => x.toFixed(1) + '%';
const at = (k, y, f) => mean(R[k].map(t => t[y][f]));
const redS = (b, s) => { const r = red(b, s); return r < 0 ? 'none (' + P(-r) + ' higher)' : P(r); };
const MEAS = [['spl', 'Societal Poverty Line, cash income'], ['splX', 'Societal Poverty Line, incl. in-kind relief'],
  ['rel', 'Relative income poverty (60% of median), cash'], ['relX', 'Relative income poverty, incl. in-kind relief'],
  ['bsk', 'Basket poverty, net'], ['bskG', 'Basket poverty, gross'], ['pov', 'Wealth poverty'],
  ['blei', 'BLEI poverty'], ['ep', 'Extreme poverty (per 10,000)']];
const fmt = (f, x) => f === 'ep' ? x.toFixed(1) : P(x);
console.log('\n[3] C1.1: POVERTY REDUCTION ON THE ENGINE\'S MEASURES AND THE SOCIETAL POVERTY LINE (seed means)\n');
console.log('| Scenario | Measure | Year 0 | Year 20 | Reduction vs year 0 | Seeds clearing the clause vs year 0 | Paired Baseline (3% CPI), yr 20 | Reduction vs paired Baseline |');
console.log('|---|---|---:|---:|---:|---:|---:|---:|');
const C11 = [['Reference (Full Integration)', 'FI', 'BF', 90], ['Stress: Adverse Environment', 'ADV', 'BA', 85],
             ['Stress: the Stress Test preset', 'ST', 'BA', 85]];
const best = {};
for (const [name, k, b, thr] of C11) {
  for (const [f, lab] of MEAS) {
    const y0 = at(k, 0, f), y20 = at(k, 20, f), b20 = at(b, 20, f);
    const hit = R[k].filter(t => t[0][f] > 0 && red(t[0][f], t[20][f]) >= thr).length;
    best[k + f] = Math.max(red(y0, y20), red(b20, y20));
    console.log('| ' + name + ' | ' + lab + ' | ' + fmt(f, y0) + ' | ' + fmt(f, y20) + ' | ' + redS(y0, y20) + ' | ' + hit +
                ' of ' + N + ' at ' + thr + '% | ' + fmt(f, b20) + ' | ' + redS(b20, y20) + ' |');
  }
}
const fiBest = Math.max(...MEAS.map(([f]) => best['FI' + f])), advBest = Math.max(...MEAS.map(([f]) => best['ADV' + f]));
check(fiBest < 90 && advBest < 85 && red(at('FI', 0, 'spl'), at('FI', 20, 'spl')) < 90 &&
      red(at('ADV', 0, 'spl'), at('ADV', 20, 'spl')) < 85,
      'no measure reaches 90% in the reference run against either comparator (largest ' + P(fiBest) + ') or 85% in the ' +
      'Adverse Environment (largest ' + P(advBest) + '); on the Societal Poverty Line the reference run gives ' +
      redS(at('FI', 0, 'spl'), at('FI', 20, 'spl')) + ' against year 0');
console.log('\nThe reference run at the measurement protocol\'s 5-year intervals (seed means):\n');
console.log('| Measure | Year 0 | Year 5 | Year 10 | Year 15 | Year 20 |');
console.log('|---|---:|---:|---:|---:|---:|');
for (const [f, lab] of MEAS.filter(([f]) => ['spl', 'splX', 'rel', 'bsk', 'pov'].includes(f)))
  console.log('| ' + lab + ' | ' + M5.map(y => fmt(f, at('FI', y, f))).join(' | ') + ' |');
const splMed0 = mean(R.FI.map(t => t[0].splMed)), splMed20 = mean(R.FI.map(t => t[20].splMed));
console.log('\nMedian cash income, reference run: $' + Math.round(splMed0).toLocaleString('en-US') + ' at year 0, $' +
            Math.round(splMed20).toLocaleString('en-US') + ' at year 20 (seed means); the Societal Poverty Line is $' +
            Math.round(splLine(splMed0)).toLocaleString('en-US') + ' and $' + Math.round(splLine(splMed20)).toLocaleString('en-US') +
            ' a year.');

console.log('\n[4] C1.2b: THE WEALTH GINI (seed means)\n');
console.log('| Scenario | Gini | Year 0 | Year 10 | Year 20 | Seeds below 0.35 at year 20 |');
console.log('|---|---|---:|---:|---:|---:|');
const G = [['Reference (Full Integration)', 'FI'], ['Baseline (3% CPI)', 'BF']];
for (const [name, k] of G) {
  for (const [f, lab] of [['giniE', 'EDC-adjusted (the engine\'s KPI)'], ['giniP', 'net wealth, negatives at zero']])
    console.log('| ' + name + ' | ' + lab + ' | ' + [0, 10, 20].map(y => at(k, y, f).toFixed(3)).join(' | ') + ' | ' +
                R[k].filter(t => t[20][f] < 0.35).length + ' of ' + N + ' |');
}
check(at('FI', 20, 'giniE') > 0.35 && at('FI', 20, 'giniP') > 0.35 && !R.FI.some(t => t[20].giniE < 0.35 || t[20].giniP < 0.35),
      'the reference run\'s wealth Gini at year 20 is ' + at('FI', 20, 'giniE').toFixed(3) + ' (EDC-adjusted) and ' +
      at('FI', 20, 'giniP').toFixed(3) + ' (net wealth): no seed is below 0.35 on either');

console.log('\n[5] C1.4: PAPER v1.4 APPENDIX G\'s PROTOCOL, RUN RECORD #4 (v4.20)\n');
let capYr = -1, r2yr = -1, r2val = 0;
for (let yr = 0; yr < 25; yr++) {
  let d = 0;
  if (yr >= C.AI_DISPLACEMENT_YEAR_2) d = C.AI_DISPLACEMENT_RATE_1 * (C.AI_DISPLACEMENT_YEAR_2 - C.AI_DISPLACEMENT_YEAR_1) +
    C.AI_DISPLACEMENT_RATE_2 * (yr - C.AI_DISPLACEMENT_YEAR_2 + 1);
  else if (yr >= C.AI_DISPLACEMENT_YEAR_1) d = C.AI_DISPLACEMENT_RATE_1 * (yr - C.AI_DISPLACEMENT_YEAR_1 + 1);
  if (capYr < 0 && d >= 0.10) capYr = yr;
  if (r2yr < 0 && yr >= C.AI_DISPLACEMENT_YEAR_2) { r2yr = yr; r2val = d; }
}
check(capYr === 13 && r2yr === 15 && r2val > 0.10,
      'the population displacement rate reaches its 0.10 cap in simulated year ' + capYr + ' (0-indexed); the year-15 ' +
      'branch computes ' + r2val.toFixed(3) + ' when it starts, already above the cap, so AI_DISPLACEMENT_RATE_2 still ' +
      'moves no output (Run Records #1 to #3 found the same); the channel slows wage growth by at most 0.10 x each ' +
      'agent\'s automationRisk a year and displaces no hours');
console.log('\n| Year | Full Integration, automation off: SPL poverty (cash / in-kind) | High Automation: SPL poverty (cash / in-kind) | Wealth poverty, off / on | Basket poverty (net), off / on | Aggregate wage income, on / off | Aggregate cash income, on / off |');
console.log('|---:|---:|---:|---:|---:|---:|---:|');
for (const y of [5, 10, 15, 20, 25]) {
  console.log('| ' + y + ' | ' + P(at('FI', y, 'spl')) + ' / ' + P(at('FI', y, 'splX')) + ' | ' + P(at('HA', y, 'spl')) + ' / ' +
              P(at('HA', y, 'splX')) + ' | ' + P(at('FI', y, 'pov')) + ' / ' + P(at('HA', y, 'pov')) + ' | ' +
              P(at('FI', y, 'bsk')) + ' / ' + P(at('HA', y, 'bsk')) + ' | ' + P(at('HA', y, 'wage') / at('FI', y, 'wage') * 100) +
              ' | ' + P(at('HA', y, 'cash') / at('FI', y, 'cash') * 100) + ' |');
}
const haSpl25 = at('HA', 25, 'spl'), haCash25 = at('HA', 25, 'cash') / at('FI', 25, 'cash') * 100;
const haMin = Math.min(...['spl', 'splX', 'rel', 'bsk', 'pov', 'blei'].map(f => at('HA', 25, f)));
console.log('\nHigh Automation at year 25, seed means: lowest headcount across the SPL, relative, basket, wealth and BLEI ' +
            'measures ' + P(haMin) + '; seeds with SPL poverty (cash) below 8%: ' + R.HA.filter(t => t[25].spl < 8).length +
            ' of ' + N + '.');
check(haMin >= 8 && haCash25 < 85,
      'at the engine\'s closest analogue to C1.4\'s scenarios, milder than the 30% scenario, every documented poverty ' +
      'measure and the SPL are at or above 8% at year 25 (SPL ' + P(haSpl25) + '), and aggregate cash income falls to ' +
      P(haCash25) + ' of the automation-off run');

console.log('\n[6] C3.3: THE COMPOUND ADVERSE ENVIRONMENT (recessions + AI automation + 2% inflation) AT THE REFERENCE SETTINGS\n');
console.log('| Core function (share of the population) | Year | Full Integration, no shock | Adverse Environment | Degradation |');
console.log('|---|---:|---:|---:|---:|');
const FN = [['spl', 'above the Societal Poverty Line (cash income)'], ['splX', 'above the SPL, incl. in-kind relief'],
            ['pov', 'above the wealth-poverty line'], ['bsk', 'out of basket poverty (net)'],
            ['dis', 'not in housing distress (the nearest measure to housing stability)']];
const deg = {};
for (const [f, lab] of FN) for (const y of [10, 20]) {
  const a = 100 - at('FI', y, f), b = 100 - at('ADV', y, f);
  deg[f + y] = (a - b) / a * 100;
  console.log('| ' + lab + ' | ' + y + ' | ' + P(a) + ' | ' + P(b) + ' | ' + P(deg[f + y]) + ' |');
}
const over = FN.filter(([f]) => deg[f + 20] >= 20).map(([, l]) => l.split(' (')[0]);
check(deg.spl20 < 20 && deg.splX20 < 20 && deg.dis20 >= 20,
      'in the one compound scenario the engine runs, the poverty function on C3.3\'s own line (the SPL) degrades by ' +
      P(deg.spl20) + ' at year 20, under 20%, and the nearest measure to housing stability by ' + P(deg.dis20) +
      ', 20% or more; the functions degraded by 20% or more at year 20 are: ' + over.join('; '));

console.log('\n[7] C3.1: COVERAGE AT THE REFERENCE SETTINGS\n');
const part0 = at('FI', 0, 'part'), part20 = at('FI', 20, 'part');
console.log('CCO participants, the agents who receive Basic Units: ' + P(part0) + ' of the population at year 0 and ' + P(part20) +
            ' at year 20 (seed means; participation rate 78%).');
check(part20 < 90, 'the share receiving the design\'s benefit is below 90% at the reference settings (' + P(part20) + ')');

console.log(ok ? '\nCCO SIMULATION CHECKS S51: ALL CHECKS PASSED.' : '\nCCO SIMULATION CHECKS S51: CHECKS FAILED.');
process.exitCode = ok ? 0 : 1;
