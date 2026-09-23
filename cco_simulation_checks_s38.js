'use strict';
/* cco_simulation_checks_s38.js -- NEEC rescoring pass, part (b): two runs of the Compassionism Simulation's
 * own engine, for CCO-PTF-CIP-SZH's C5.3 (clause 1, participation) and C3.4 (clause 4, adjustments).
 *
 * The engine is harness.js from github.com/BetterToBest/compassionism-simulation at commit cd0ceec (v4.15), whose
 * CONTRIBUTING.md confirms it reproduces index.html v4.15's seed-42 regression. This script does not copy or
 * change the engine: it reads harness.js, appends one line exposing functions the file already defines, and
 * loads the result as a module. Run 1 varies only the CCO participation rate in the Full Integration reference
 * preset. Run 2 steps the monthly Basic Unit amount by a factor from the start of year 10 and compares each seed
 * with the unadjusted run. Prices are an exogenous input in this engine, which is why run 2 cannot fail.
 *
 * Usage: node cco_simulation_checks_s38.js [path/to/harness.js]   (default ./harness.js). Deterministic.
 */
const fs = require('fs'), path = require('path'), crypto = require('crypto'), Module = require('module');
const file = path.resolve(process.argv[2] || 'harness.js');
const src = fs.readFileSync(file, 'utf8');
const m = new Module(file, module);
m.filename = file; m.paths = Module._nodeModulePaths(path.dirname(file));
m._compile(src + '\nObject.assign(module.exports, { runYear, calcMetrics, instantiateAgent, makeLatentPopulation, ' +
           'setRNG: function (f) { RNG = f; } });\n', file);
const E = m.exports;
const N = 100;
const md5 = crypto.createHash('md5').update(src).digest('hex');
console.log('Compassionism Simulation engine: harness.js, md5 ' + md5 + ' (compassionism-simulation cd0ceec, v4.15)');
E.CFG.WEALTH_FLOOR = -10000;
const v = E.runScenario(E.FULL_INTEGRATION, 42);
console.log('seed-42 Full Integration 20yr: median BLEI ' + v.bleiMed + ' d, wealth poverty ' + v.pov +
            '%, Gini ' + v.gini + ', System Stability ' + v.stab + '% (documented: 1965 d, 16.6%, 0.534, 88.5%)');
console.log('CCO_MIN_PARTICIPATION = ' + E.CFG.CCO_MIN_PARTICIPATION + ' (read by index.html only to issue a warning)');
function mean(a) { return a.reduce((x, y) => x + y, 0) / a.length; }
function runs(p) { const o = []; for (let s = 1; s <= N; s++) o.push(E.runScenario(p, s)); return o; }

console.log('\nRun 1. Participation, N=' + N + ' seeds (1-' + N + '), 500 agents, 20 years, shock off; means\n');
console.log('| Configuration | Wealth poverty | BLEI poverty | System Stability |');
console.log('|---|---:|---:|---:|');
const base = runs(E.BASELINE);
const row = (name, r) => console.log('| ' + name + ' | ' + mean(r.map(x => x.pov)).toFixed(1) + '% | ' +
  mean(r.map(x => x.bleiPovPct)).toFixed(1) + '% | ' + mean(r.map(x => x.stab)).toFixed(1) + '% |');
row('Baseline (no systems)', base);
const res = {};
for (const rate of [0.30, 0.45, 0.55, 0.78]) {
  res[rate] = runs(Object.assign({}, E.FULL_INTEGRATION, { partRate: rate }));
  row('Full Integration, participation ' + Math.round(rate * 100) + '%' + (rate === 0.78 ? ' (reference)' : ''), res[rate]);
}
console.log('');
for (const rate of [0.30, 0.45]) {
  console.log('Participation ' + Math.round(rate * 100) + '%: wealth poverty below Baseline in ' +
              res[rate].filter((x, i) => x.pov < base[i].pov).length + ' of ' + N + ' seeds; lowest System Stability ' +
              Math.min(...res[rate].map(x => x.stab)) + '%.');
}

function trajectory(p, seed, factor) {
  E.setRNG(E.mulberry32(seed + 700003));
  const agents = E.makeLatentPopulation(p.nAgents).map(l => E.instantiateAgent(l, p));
  E.setRNG(E.mulberry32(seed));
  const pov = [];
  for (let yr = 0; yr < p.years; yr++) {
    const q = yr >= 10 ? Object.assign({}, p, { bu: p.bu * factor }) : p;
    E.runYear(agents, yr, q, { active: false, incomeMultiplier: 1.0, yearsLeft: 0 });
    pov.push(E.calcMetrics(agents, q.ccoOn, q.pth).pov * 100);
  }
  return pov;
}
console.log('\nRun 2. Basic Unit stepped from year 10 and held, reference preset, N=' + N + ' seeds\n');
console.log('| Step | Final wealth poverty, adjusted | Final wealth poverty, unadjusted | Largest one-year excess rise |');
console.log('|---|---:|---:|---:|');
const p = Object.assign({}, E.FULL_INTEGRATION);
for (const f of [0.7, 0.8, 1.2, 1.3]) {
  let worst = -Infinity, end = 0, ref = 0;
  for (let s = 1; s <= N; s++) {
    const a = trajectory(p, s, f), r = trajectory(p, s, 1.0);
    for (let y = 10; y < p.years; y++) worst = Math.max(worst, (a[y] - a[y - 1]) - (r[y] - r[y - 1]));
    end += a[p.years - 1]; ref += r[p.years - 1];
  }
  console.log('| x' + f + ' | ' + (end / N).toFixed(1) + '% | ' + (ref / N).toFixed(1) + '% | ' + worst.toFixed(1) +
              ' points |');
}
