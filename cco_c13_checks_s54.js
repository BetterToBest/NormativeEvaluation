'use strict';
/* cco_c13_checks_s54.js -- NEEC rescoring pass, stage 2, group 2.3 (C1.3 Housing Security): the design's C1.3 on its
 * published model, the Compassionism Simulation at 5a7a7b1 (v4.20), the pin frozen for v2.0 (decision 52.9; reading
 * 3.10 of NEEC_Rescoring_s51.md).
 *
 * The engine is loaded exactly as cco_c12a_checks_s53.js loads it: harness.js and index.html at 5a7a7b1 pinned by
 * digest, one appended line exposing functions harness.js already defines, no line of either file altered. The runner
 * mirrors runScenario() (population on seed+700003, recessions on seed+700000, the trajectory on mulberry32(seed));
 * check [2] asserts that it reproduces runScenario()'s year-20 housing distress, median wealth and wealth poverty on
 * every seed of every scenario used, before any table is trusted.
 *
 * The quantity. v2.0's C1.3 has two clauses: >=88% housing stability over 5-year periods (participants keeping their
 * housing without involuntary displacement by foreclosure, eviction or unaffordable rent increases), and housing costs
 * <=30% of disposable income for a household at 80% of the regional median household disposable income. The engine
 * models no housing tenure, rent, eviction or housing-cost line (CONTRIBUTING.md at 5a7a7b1, the extreme-poverty
 * overlay), so it computes neither clause. Its nearest measure is housing distress (v4.18, housingDistressOf()): an
 * agent is in distress in a year when its cash income (wage plus CCO conversion) plus the savings it holds at the start
 * of the year cannot cover that year's living-wage basket at the prices it faces. This runner reports, per agent, the
 * share that passes a whole 5-year window (years 1-5, 6-10, 11-15, 16-20) with no year of distress: a proxy for
 * clause 1 that counts distress as displacement and counts no other cause of a move. It also reports the reach of
 * Public Trust Housing (PTH), the design's decommodified housing, and the same proxy inside and outside it.
 *
 * Usage: node cco_c13_checks_s54.js [harness.js] [index.html]   (defaults: beside the working directory)
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

const m = new Module(hFile, module);
m.filename = hFile; m.paths = Module._nodeModulePaths(path.dirname(hFile));
m._compile(hSrc + '\nObject.assign(module.exports, { runYear, calcMetrics, instantiateAgent, makeLatentPopulation, ' +
           'buildRecessionPath, medianOf, housingDistressOf, setRNG: function (f) { RNG = f; } });\n', hFile);
const E = m.exports;
const FI = E.FULL_INTEGRATION, ADV = E.ADVERSE_REFERENCE;

console.log('NEEC cco_c13_checks_s54: CCO-PTF-CIP-SZH\'s C1.3 on the design\'s own engine, v4.20');
console.log('inputs: ' + path.basename(hFile) + ', ' + path.basename(iFile) + '\n');
console.log('[1] THE ENGINE AND WHAT IT MODELS');
check(md5(hSrc) === PIN.harness, path.basename(hFile) + ' md5 ' + md5(hSrc) + ' (compassionism-simulation 5a7a7b1, v4.20)');
check(md5(iSrc) === PIN.index && /VERSION:'4\.20'/.test(iSrc), path.basename(iFile) + ' md5 ' + md5(iSrc) +
      ' (same commit; META.VERSION 4.20)');
const hd = (function () { const st = hSrc.indexOf('\nfunction housingDistressOf('); return hSrc.slice(st, hSrc.indexOf('\nfunction ', st + 5)); })();
check(/inc\+Math\.max\(0,w\)<\(\+a\.yrCostUSD\|\|0\)/.test(hd) && !/tenure|rent|evict/i.test(hd),
      'housingDistressOf() counts an agent whose cash income plus start-of-year savings falls short of its basket; it ' +
      'reads no tenure, rent or eviction');
check(FI.pth && FI.pthUptake === 0.20 && ADV.pthUptake === 0.20,
      'Public Trust Housing is on in the reference run with an uptake of ' + FI.pthUptake * 100 + '% of agents (the same in ' +
      'the Adverse Environment)');

// ---- the runner ----------------------------------------------------------------------------------------------------
const distressed = a => ((+a.yrWageUSD || 0) + (+a.yrConvUSD || 0) + Math.max(0, +a.yrWealthStartUSD || 0)) < (+a.yrCostUSD || 0);
const WIN = [[0, 5], [5, 10], [10, 15], [15, 20]];
function traj(p, seed) {                 // runScenario(), keeping each agent's distress in every year
  E.setRNG(E.mulberry32(seed + 700003));
  const agents = E.makeLatentPopulation(p.nAgents).map(l => E.instantiateAgent(l, p));
  const rec = p.shock ? E.buildRecessionPath(p.years, seed) : null;
  E.setRNG(E.mulberry32(seed));
  const D = agents.map(() => []);
  for (let yr = 0; yr < p.years; yr++) {
    E.runYear(agents, yr, p, rec ? rec[yr] : { active: false, incomeMultiplier: 1.0, yearsLeft: 0 });
    agents.forEach((a, i) => D[i].push(distressed(a)));
  }
  const mt = E.calcMetrics(agents, p.ccoOn, p.pth);
  const pth = agents.map(a => !!a.inPTH);
  const clean = (sel, w) => { const ix = agents.map((_, i) => i).filter(sel);
    return ix.length ? ix.filter(i => !D[i].slice(w[0], w[1]).some(x => x)).length / ix.length : null; };
  return { dEnd: E.housingDistressOf(agents) * 100, med: mt.med, pov: mt.pov * 100,
           annual: D[0].map((_, y) => D.filter(d => d[y]).length / D.length),
           win: WIN.map(w => clean(() => true, w)), winP: WIN.map(w => clean(i => pth[i], w)),
           winN: WIN.map(w => clean(i => !pth[i], w)), pth: pth.filter(x => x).length / pth.length };
}
const N = 500, SEEDS = Array.from({ length: N }, (_, i) => i + 1);
const mean = a => a.reduce((x, y) => x + y, 0) / a.length;
const SC = { FI: FI, BFm: E.baselineFor(FI, true), ADV: ADV, BAm: E.baselineFor(ADV, true) };
const NAME = { FI: 'Reference (Full Integration), 0%', BFm: 'Baseline, matched (0%)', ADV: 'Adverse Environment, 2%',
               BAm: 'Baseline, matched to Adverse (2%)' };
const R = {}, RS = {};
for (const k of Object.keys(SC)) { R[k] = SEEDS.map(s => traj(SC[k], s)); RS[k] = SEEDS.map(s => E.runScenario(SC[k], s)); }

console.log('\n[2] THE RUNNER (N = ' + N + ' seeds, 1-' + N + ', 500 agents)');
const bad = [];
for (const k of Object.keys(SC)) SEEDS.forEach((s, i) => {
  if (R[k][i].dEnd !== RS[k][i].distress || Math.round(R[k][i].med) !== RS[k][i].wealth ||
      +R[k][i].pov.toFixed(1) !== RS[k][i].pov) bad.push(k + ' seed ' + s);
});
check(!bad.length, 'the runner reproduces runScenario()\'s year-20 housing distress, median wealth and wealth poverty ' +
      'on all ' + N + ' seeds of all ' + Object.keys(SC).length + ' scenarios (' + Object.keys(SC).join(', ') + ')' +
      (bad.length ? ' [' + bad.slice(0, 3).join('; ') + ']' : ''));

console.log('\n[3] C1.3, CLAUSE 1, ON THE ENGINE\'S NEAREST MEASURE: AGENTS WITH NO YEAR OF HOUSING DISTRESS IN A 5-YEAR ' +
            'WINDOW (seed means)');
console.log('| Scenario | Agents | Years 1-5 | Years 6-10 | Years 11-15 | Years 16-20 | Lowest window | Seeds at 88% or more, years 16-20 |');
console.log('|---|---|---:|---:|---:|---:|---:|---:|');
const pc = x => (x * 100).toFixed(1) + '%';
const T = {};
for (const k of Object.keys(SC)) for (const [lab, f] of [['all', 'win'], ['in PTH', 'winP'], ['outside PTH', 'winN']]) {
  if (f !== 'win' && !SC[k].pth) continue;
  const rows = R[k].map(r => r[f]).filter(w => w.every(x => x !== null));
  const w = WIN.map((_, j) => mean(rows.map(r => r[j])));
  const s88 = rows.filter(r => r[3] >= 0.88).length;
  T[k + ':' + f] = { w: w, low: Math.min(...w), s88: s88, n: rows.length };
  console.log('| ' + NAME[k] + ' | ' + lab + ' | ' + w.map(pc).join(' | ') + ' | ' + pc(Math.min(...w)) + ' | ' + s88 +
              ' of ' + rows.length + ' |');
}
const fi = T['FI:win'], bf = T['BFm:win'], fp = T['FI:winP'], fn = T['FI:winN'], ad = T['ADV:win'];
const pthShare = mean(R.FI.map(r => r.pth));
check(Math.abs(pthShare - 0.20) < 0.02, 'Public Trust Housing holds ' + pc(pthShare) + ' of agents in the reference run ' +
      '(seed mean); the other ' + pc(1 - pthShare) + ' are housed as the Baseline houses them');
check(fi.low < 0.88 && fi.w[3] > bf.w[3],
      'reference run: ' + pc(fi.w[3]) + ' of agents pass years 16-20 with no year of distress against ' + pc(bf.w[3]) +
      ' in the matched Baseline; the lowest window is ' + pc(fi.low) + ', under 88%');
check(fp.w[3] > fn.w[3], 'inside Public Trust Housing ' + pc(fp.w[3]) + ' pass years 16-20 with no year of distress; ' +
      'outside it ' + pc(fn.w[3]));
console.log('  NOTE Adverse Environment: ' + pc(ad.w[3]) + ' of agents pass years 16-20 with no year of distress, ' +
            'against ' + pc(T['BAm:win'].w[3]) + ' in its matched Baseline (C1.3 names resistance to market volatility)');
const yd = R.FI[0].annual.map((_, y) => mean(R.FI.map(r => r.annual[y])));
console.log('  NOTE reference run, share of agents in distress by year (seed means): ' +
            yd.map((x, y) => 'y' + (y + 1) + ' ' + pc(x)).join(', '));

console.log('\n[4] C1.3, CLAUSE 2');
check(!/housingCost|rentUSD|HOUSING_SHARE/.test(hSrc),
      'the engine carries no housing-cost line: the basket (LIVING_WAGE_ANNUAL) is one sum, which PTH membership scales ' +
      'by 0.65 as a whole, so housing costs as a share of disposable income at 80% of the median are not computed');
console.log(ok ? '\nCCO C1.3 SIMULATION CHECKS: ALL PASSED.' : '\nCCO C1.3 SIMULATION CHECKS: SOME FAILED.');
process.exit(ok ? 0 : 1);
