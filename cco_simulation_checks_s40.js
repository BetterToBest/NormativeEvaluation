'use strict';
/* cco_simulation_checks_s40.js -- NEEC rescoring pass, part (b), third group: runs of the Compassionism
 * Simulation's own engine for CCO-PTF-CIP-SZH's C1.1 (clause 1, base scenario; clause 2, stress testing).
 *
 * The engine is harness.js from github.com/BetterToBest/compassionism-simulation at commit cd0ceec (v4.15), the
 * engine Session 38 pinned (part (b1), decision 3.2). harness.js runs every trajectory with recessions off (its
 * own scope note), so the two recession functions are read verbatim from index.html at the same commit, the
 * in-app model harness.js was extracted from, and appended unchanged; both files are pinned by digest below, and
 * no line of either is altered. The script appends one line exposing functions the files already define and loads
 * the result as a module, as cco_simulation_checks_s38.js did.
 *
 * The runner below mirrors harness.js's runScenario() line for line (population on seed+700003, trajectory on a
 * fresh mulberry32(seed)), with one addition taken from index.html's simulate(): when recessions are on, every
 * trajectory reads the same pre-built recession path (buildRecessionPath on its own seed+700000 stream, "paired
 * shocks"). With recessions off it must reproduce runScenario() exactly; check 2 asserts that on all seeds.
 *
 * Measures: the engine's two documented poverty headcounts, wealth poverty (net wealth below CFG.POVERTY_LINE,
 * $25,000) and BLEI poverty (the Crisis and Precarious runway tiers, under 30 days), and one sensitivity, BLEI
 * Crisis alone (under 7 days), the engine's own lowest tier. Poverty reduction = (Baseline - scenario) / Baseline
 * on seed means, against the paired Baseline at the same year (the model's own counterfactual) and, second,
 * against the population at year 0 before any year runs (NEEC C1.1's measurement protocol: baseline, then 5-year
 * intervals).
 *
 * Usage: node cco_simulation_checks_s40.js [harness.js] [index.html]   (defaults: beside the working directory)
 * Prints file names only. Deterministic.
 */
const fs = require('fs'), path = require('path'), crypto = require('crypto'), Module = require('module');
const hFile = path.resolve(process.argv[2] || 'harness.js');
const iFile = path.resolve(process.argv[3] || 'index.html');
const hSrc = fs.readFileSync(hFile, 'utf8'), iSrc = fs.readFileSync(iFile, 'utf8');
const md5 = s => crypto.createHash('md5').update(s).digest('hex');
const PIN = { harness: '035d1be82ab497e76a234615a04c0ce9', index: '1c8273b13b2c22763a44c051ca7bd882' };
let ok = true;
function check(cond, text) { console.log('  ' + (cond ? 'PASS' : 'FAIL') + ' ' + text); ok = ok && !!cond; }

function extract(src, name) {             // one top-level function, verbatim, by brace matching
  const start = src.indexOf('\nfunction ' + name + '(');
  if (start < 0) throw new Error('function ' + name + ' not found in ' + path.basename(iFile));
  let i = src.indexOf('{', start), d = 0;
  for (; i < src.length; i++) { if (src[i] === '{') d++; else if (src[i] === '}' && --d === 0) break; }
  return src.slice(start + 1, i + 1);
}
const recFns = ['updateRecession', 'buildRecessionPath'].map(n => extract(iSrc, n));
const m = new Module(hFile, module);
m.filename = hFile; m.paths = Module._nodeModulePaths(path.dirname(hFile));
m._compile(hSrc + '\n' + recFns.join('\n') + '\nObject.assign(module.exports, { runYear, calcMetrics, ' +
           'instantiateAgent, makeLatentPopulation, bleiMetrics, buildRecessionPath, ' +
           'setRNG: function (f) { RNG = f; } });\n', hFile);
const E = m.exports;
E.CFG.WEALTH_FLOOR = -10000;             // the shipped default, set as cco_simulation_checks_s38.js set it

console.log('NEEC cco_simulation_checks_s40: CCO-PTF-CIP-SZH C1.1 on the design\'s own engine');
console.log('inputs: ' + path.basename(hFile) + ', ' + path.basename(iFile) + '\n');
console.log('[1] THE ENGINE');
check(md5(hSrc) === PIN.harness, path.basename(hFile) + ' md5 ' + md5(hSrc) + ' (compassionism-simulation cd0ceec, v4.15)');
check(md5(iSrc) === PIN.index, path.basename(iFile) + ' md5 ' + md5(iSrc) + ' (same commit)');
check(recFns.every(f => iSrc.includes(f)), 'updateRecession and buildRecessionPath appended verbatim from ' +
      path.basename(iFile) + ' (' + recFns.map(f => f.length).join(' and ') + ' characters)');
const ref = E.runScenario(E.FULL_INTEGRATION, 42);
check(ref.bleiMed === 1965 && ref.pov === 16.6 && ref.gini === 0.534 && ref.stab === 88.5,
      'seed-42 Full Integration 20yr reproduces the documented regression: median BLEI ' + ref.bleiMed + ' d, wealth ' +
      'poverty ' + ref.pov + '%, Gini ' + ref.gini + ', System Stability ' + ref.stab + '%');

const TOP = p => (p.ccoOn && p.ptf) ? 'Flourishing' : 'Comfortable';
function snap(agents, p) {
  const w = E.calcMetrics(agents, p.ccoOn, p.pth);
  const b = E.bleiMetrics(agents, p.bu, p.ccoOn, p.pth, p.szh, p.szhCoh, p.ptf, TOP(p));
  return { pov: w.pov * 100, blei: (b.tc[0] + b.tc[1]) / b.n * 100, crisis: b.tc[0] / b.n * 100 };
}
function trajectory(p, seed) {            // runScenario() plus index.html's paired recession path
  E.setRNG(E.mulberry32(seed + 700003));
  const agents = E.makeLatentPopulation(p.nAgents).map(l => E.instantiateAgent(l, p));
  const rec = p.shock ? E.buildRecessionPath(p.years, seed) : null;
  E.setRNG(E.mulberry32(seed));
  const out = [snap(agents, p)];
  for (let yr = 0; yr < p.years; yr++) {
    E.runYear(agents, yr, p, rec ? rec[yr] : { active: false, incomeMultiplier: 1.0, yearsLeft: 0 });
    out.push(snap(agents, p));
  }
  return out;                              // out[k] = state after k years; out[0] = before any year runs
}
const N = 100, SEEDS = Array.from({ length: N }, (_, i) => i + 1);
const mean = a => a.reduce((x, y) => x + y, 0) / a.length;

console.log('\n[2] THE RUNNER');
const same = SEEDS.every(s => {
  for (const p of [E.FULL_INTEGRATION, E.BASELINE]) {
    const r = E.runScenario(p, s), t = trajectory(p, s)[p.years];
    if (+t.pov.toFixed(1) !== r.pov || +t.blei.toFixed(1) !== r.bleiPovPct) return false;
  }
  return true;
});
check(same, 'with recessions off the runner reproduces runScenario() on all ' + N + ' seeds, both presets, both measures');

// The engine's shipped Stress Test preset (index.html PRESETS.stress, converted as readParams() converts it)
const STRESS = { bu: 900, maxOct: 4, expiry: 1, tax: 0.18, maxMult: 6, nAgents: 500, partRate: 0.40, years: 20,
  ptfShare: 0.08, pthUptake: 0.10, szhCoh: 0.35, cipDemo: 0.30, phi: true, ptf: true, pth: true, szh: true,
  cip: true, shock: true, automation: true, inflRate: 0.02, ccoOn: true, ptfCap: false };
check(/stress:\{bu:900,oct:4,exp:1,tax:18,mult:6,agents:500,part:40,yrs:20,ptfShare:8,pthUptake:10,szh:35,cip:30,phi:true,ptf:true,pth:true,szh_tog:true,cip_tog:true,shock:true,inflRate:2,automation:true\}/.test(iSrc),
      'the Stress Test preset above is the one ' + path.basename(iFile) + ' ships');
// index.html pairs the Baseline's recessions and automation with the tested run and fixes its inflation at 3% CPI
const baseFor = p => Object.assign({}, E.BASELINE, { shock: p.shock, automation: p.automation });
const SCEN = [
  ['A. Reference (Full Integration), no stress', E.FULL_INTEGRATION],
  ['B1. Reference, recessions on', Object.assign({}, E.FULL_INTEGRATION, { shock: true })],
  ['B2. Reference, AI automation on', Object.assign({}, E.FULL_INTEGRATION, { automation: true })],
  ['B3. Reference, recessions + automation + 2% inflation', Object.assign({}, E.FULL_INTEGRATION,
    { shock: true, automation: true, inflRate: 0.02 })],
  ['C. The engine\'s Stress Test preset', STRESS],
];
const MEAS = [['pov', 'Wealth poverty'], ['blei', 'BLEI poverty'], ['crisis', 'BLEI Crisis (sensitivity)']];
const pct = x => x.toFixed(1) + '%';
const red = (b, s) => b > 0 ? pct((b - s) / b * 100) : 'n/a';
const red0 = (y0, s) => s >= y0 ? 'none (rises from year 0)' : red(y0, s);
const results = {};
console.log('\n[3] POVERTY REDUCTION, N=' + N + ' seeds (1-' + N + '), 500 agents, 20 years; seed means\n');
console.log('| Scenario | Measure | Year 0 | Paired Baseline, yr 20 | Scenario, yr 20 | Reduction vs paired Baseline | Reduction vs year 0 | Seeds clearing the clause vs Baseline |');
console.log('|---|---|---:|---:|---:|---:|---:|---:|');
for (const [name, p] of SCEN) {
  const tb = SEEDS.map(s => trajectory(baseFor(p), s)), ts = SEEDS.map(s => trajectory(p, s));
  results[name] = { tb, ts };
  const thr = p === E.FULL_INTEGRATION ? 0.90 : 0.85;   // clause 1 (base) 90%; clause 2 (stress) 85%
  for (const [k, lab] of MEAS) {
    const y0 = mean(ts.map(t => t[0][k])), b20 = mean(tb.map(t => t[20][k])), s20 = mean(ts.map(t => t[20][k]));
    const hit = SEEDS.filter((_, i) => tb[i][20][k] > 0 && (tb[i][20][k] - ts[i][20][k]) / tb[i][20][k] >= thr).length;
    console.log('| ' + name + ' | ' + lab + ' | ' + pct(y0) + ' | ' + pct(b20) + ' | ' + pct(s20) + ' | ' +
                red(b20, s20) + ' | ' + red0(y0, s20) + ' | ' + hit + ' of ' + N + ' at ' + thr * 100 + '% |');
  }
}
console.log('\n[4] TEMPORAL TRACKING (C1.1 measurement protocol: 5-year intervals), reference preset, seed means\n');
console.log('| Measure | Year 0 | Year 5 | Year 10 | Year 15 | Year 20 | Paired Baseline, yr 5 / 10 / 15 / 20 |');
console.log('|---|---:|---:|---:|---:|---:|---|');
{
  const { tb, ts } = results[SCEN[0][0]];
  for (const [k, lab] of MEAS) {
    const at = (tt, y) => mean(tt.map(t => t[y][k]));
    console.log('| ' + lab + ' | ' + [0, 5, 10, 15, 20].map(y => pct(at(ts, y))).join(' | ') + ' | ' +
                [5, 10, 15, 20].map(y => pct(at(tb, y))).join(' / ') + ' |');
  }
}
// Guard figures: the base-scenario result Session 38 recorded must be reproduced exactly
const A = results[SCEN[0][0]];
check(mean(A.tb.map(t => t[20].pov)).toFixed(1) === '71.4' && mean(A.ts.map(t => t[20].pov)).toFixed(1) === '15.3' &&
      mean(A.tb.map(t => t[20].blei)).toFixed(1) === '70.5' && mean(A.ts.map(t => t[20].blei)).toFixed(1) === '12.6',
      'Session 38\'s run 1 reproduced: Baseline 71.4% / 70.5%, reference 15.3% / 12.6% (wealth / BLEI poverty)');
console.log(ok ? '\nCCO SIMULATION CHECKS S40: ALL CHECKS PASSED.' : '\nCCO SIMULATION CHECKS S40: CHECKS FAILED.');
process.exitCode = ok ? 0 : 1;
