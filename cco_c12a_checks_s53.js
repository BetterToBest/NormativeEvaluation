'use strict';
/* cco_c12a_checks_s53.js -- NEEC rescoring pass, stage 2, group 2.2 (C1.2a Wealth Building for Resilience): the
 * design's C1.2a on its published model, the Compassionism Simulation at 5a7a7b1 (v4.20), the pin frozen for v2.0
 * (decision 52.9; reading 3.10 of NEEC_Rescoring_s51.md).
 *
 * The engine is loaded exactly as cco_simulation_checks_s51.js loads it: harness.js and index.html at 5a7a7b1 pinned
 * by digest, one appended line exposing functions harness.js already defines, no line of either file altered. The
 * runner mirrors runScenario() (population on seed+700003, recessions on seed+700000, the trajectory on
 * mulberry32(seed)); check [2] asserts that it reproduces runScenario()'s year-20 median wealth and wealth poverty on
 * every seed of every scenario used, before any table is trusted.
 *
 * The quantity. v2.0's clause: >=$60,000 net-wealth accumulation over 20 years for 70%+ of participants, in constant
 * 2019 US dollars at PPP (reading 3.1 of NEEC_Rescoring_s53.md: at least 70% of participants each accumulate the
 * figure; the median is reported beside it). Accumulation = an agent's net worth at year 20 minus its net worth at
 * adoption (year 0, before any year runs). Net worth is read two ways: the engine's `wealth` alone, the figure the
 * engine reports; and `wealth` plus `acreEquity`, the design's PTF/PTH acre equity, which v2.0's measurement field
 * names. The second overstates by the appreciation the engine credits both to acre equity and, in part, to wealth
 * (PTH_APPR_CONSERVE false, logged by the simulation at v4.16). BU balances, which expire, are not counted.
 * Price basis: the engine's dollars are 2023 US dollars (BASE_DAILY_COST from BLS CES 2023, WAGE_TO_USD from CPS
 * ASEC 2023; CONTRIBUTING.md at 5a7a7b1, calibration table), constant in the reference run (inflRate 0). The bar is
 * $60,000 x CPI-U 2023 / CPI-U 2019 (BLS series CUUR0000SA0, annual averages 304.702 and 255.657); the United States
 * is the PPP numeraire. Runs with inflation are deflated by the headline rate, (1 + inflRate)^20; the engine's
 * effective rate is lower where PTF and PTH damp it, so this understates their real wealth (stated, not corrected).
 * Saving: the share of 20 years' cash income (wage income plus CCO conversion proceeds) that ends as net worth.
 *
 * Usage: node cco_c12a_checks_s53.js [harness.js] [index.html]   (defaults: beside the working directory)
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
           'buildRecessionPath, medianOf, setRNG: function (f) { RNG = f; } });\n', hFile);
const E = m.exports, C = E.CFG;
const FI = E.FULL_INTEGRATION, ADV = E.ADVERSE_REFERENCE;

console.log('NEEC cco_c12a_checks_s53: CCO-PTF-CIP-SZH\'s C1.2a on the design\'s own engine, v4.20');
console.log('inputs: ' + path.basename(hFile) + ', ' + path.basename(iFile) + '\n');
console.log('[1] THE ENGINE AND THE BAR');
check(md5(hSrc) === PIN.harness, path.basename(hFile) + ' md5 ' + md5(hSrc) + ' (compassionism-simulation 5a7a7b1, v4.20)');
check(md5(iSrc) === PIN.index && /VERSION:'4\.20'/.test(iSrc), path.basename(iFile) + ' md5 ' + md5(iSrc) +
      ' (same commit; META.VERSION 4.20)');
const CPI = { 2019: 255.657, 2023: 304.702 };
const BAR = 60000 * CPI[2023] / CPI[2019];
check(FI.inflRate === 0 && ADV.inflRate === 0.02 && Math.round(BAR) === 71510,
      'the reference run (Full Integration) holds prices constant (inflRate 0) and the Adverse Environment runs at 2%; ' +
      'the bar, $60,000 in 2019 dollars, is $' + Math.round(BAR) + ' in the engine\'s 2023 dollars');

// ---- the runner ----------------------------------------------------------------------------------------------------
const nw = (a, acres) => (isNaN(a.wealth) ? 0 : a.wealth) + (acres ? (+a.acreEquity || 0) : 0);
function traj(p, seed) {                 // runScenario(), keeping each agent's net worth at year 0 and year 20
  E.setRNG(E.mulberry32(seed + 700003));
  const agents = E.makeLatentPopulation(p.nAgents).map(l => E.instantiateAgent(l, p));
  const w0 = agents.map(a => nw(a, false)), n0 = agents.map(a => nw(a, true));
  const rec = p.shock ? E.buildRecessionPath(p.years, seed) : null;
  E.setRNG(E.mulberry32(seed));
  let cash = 0;
  for (let yr = 0; yr < p.years; yr++) {
    E.runYear(agents, yr, p, rec ? rec[yr] : { active: false, incomeMultiplier: 1.0, yearsLeft: 0 });
    agents.forEach(a => { const w = +a.yrWageUSD, c = +a.yrConvUSD; cash += (isNaN(w) ? 0 : w) + (isNaN(c) ? 0 : c); });
  }
  const defl = Math.pow(1 + (p.inflRate || 0), p.years);
  const acc = agents.map((a, i) => nw(a, false) / defl - w0[i]), accA = agents.map((a, i) => nw(a, true) / defl - n0[i]);
  const mt = E.calcMetrics(agents, p.ccoOn, p.pth);
  const dN = agents.reduce((s, a, i) => s + nw(a, true) - n0[i], 0);
  return { acc, accA, med: mt.med, pov: mt.pov * 100, save: dN / cash, inPTH: agents.filter(a => a.inPTH).length };
}
const N = 500, SEEDS = Array.from({ length: N }, (_, i) => i + 1);
const mean = a => a.reduce((x, y) => x + y, 0) / a.length;
const q = (xs, f) => { const s = xs.slice().sort((x, y) => x - y), h = (s.length - 1) * f, l = Math.floor(h);
                       return s[l] + (s[Math.min(l + 1, s.length - 1)] - s[l]) * (h - l); };
const SC = { FI: FI, BFm: E.baselineFor(FI, true), ADV: ADV, BAm: E.baselineFor(ADV, true) };
const NAME = { FI: 'Reference (Full Integration), 0%', BFm: 'Baseline, matched (0%)', ADV: 'Adverse Environment, 2%',
               BAm: 'Baseline, matched to Adverse (2%)' };
const R = {}, RS = {};
for (const k of Object.keys(SC)) { R[k] = SEEDS.map(s => traj(SC[k], s)); RS[k] = SEEDS.map(s => E.runScenario(SC[k], s)); }

console.log('\n[2] THE RUNNER (N = ' + N + ' seeds, 1-' + N + ', 500 agents)');
const bad = [];
for (const k of Object.keys(SC)) SEEDS.forEach((s, i) => {
  if (Math.round(R[k][i].med) !== RS[k][i].wealth || +R[k][i].pov.toFixed(1) !== RS[k][i].pov) bad.push(k + ' seed ' + s);
});
check(!bad.length, 'the runner reproduces runScenario()\'s year-20 median wealth and wealth poverty on all ' + N +
      ' seeds of all ' + Object.keys(SC).length + ' scenarios (' + Object.keys(SC).join(', ') + ')' +
      (bad.length ? ' [' + bad.slice(0, 3).join('; ') + ']' : ''));

console.log('\n[3] C1.2a: 20-YEAR NET-WEALTH ACCUMULATION, 2019 DOLLARS (seed means; the bar is $60,000)');
console.log('| Scenario | Net worth read as | Share accumulating >=$60,000 | Seeds at 70% or more | Median accumulation | ' +
            '30th percentile | Saving share of cash income |');
console.log('|---|---|---:|---:|---:|---:|---:|');
const to19 = x => x * CPI[2019] / CPI[2023];
const usd = x => (x < 0 ? '-$' : '$') + Math.round(Math.abs(x)).toLocaleString('en-US');
const T = {};
for (const k of Object.keys(SC)) for (const [lab, f] of [['wealth (the engine\'s figure)', 'acc'],
                                                          ['wealth + acre equity', 'accA']]) {
  const sh = R[k].map(r => r[f].filter(v => v >= BAR).length / r[f].length * 100);
  const row = { share: mean(sh), seeds70: sh.filter(v => v >= 70).length, med: to19(mean(R[k].map(r => q(r[f], 0.5)))),
                p30: to19(mean(R[k].map(r => q(r[f], 0.3)))), save: mean(R[k].map(r => r.save)) * 100 };
  T[k + ':' + f] = row;
  console.log('| ' + NAME[k] + ' | ' + lab + ' | ' + row.share.toFixed(1) + '% | ' + row.seeds70 + ' of ' + N + ' | ' +
              usd(row.med) + ' | ' + usd(row.p30) + ' | ' + (f === 'acc' ? row.save.toFixed(1) + '%' : '') + ' |');
}
const fi = T['FI:acc'], fiA = T['FI:accA'], bf = T['BFm:acc'];
check(fi.share >= 70 && fiA.share >= fi.share,
      'in the reference run ' + fi.share.toFixed(1) + '% of agents accumulate $60,000 (2019) or more on the engine\'s ' +
      'wealth, ' + fiA.share.toFixed(1) + '% with acre equity; the median accumulation is ' + usd(fi.med) + ' and the 30th ' +
      'percentile ' + usd(fi.p30) + ' (2019 dollars)');
check(bf.share < 70 && fi.share - bf.share > 30,
      'the matched Baseline (no CCO, PTF, PTH, SZH or CIP; 0%) does not clear: ' + bf.share.toFixed(1) + '% accumulate ' +
      '$60,000, median ' + usd(bf.med) + '; the design adds ' + (fi.share - bf.share).toFixed(1) + ' points to the share');
const ry = (function () { const st = hSrc.indexOf('\nfunction runYear('); return hSrc.slice(st, hSrc.indexOf('\nfunction ', st + 5)); })();
check(/a\.wealth\+=annualWageUSD-costUSD;/.test(ry) && fi.save > 5 * 5.6,
      'runYear() adds wage income less the basket\'s cost to wealth (a.wealth+=annualWageUSD-costUSD), so an agent ' +
      'saves every dollar above its basket: agents keep ' + fi.save.toFixed(1) + '% of 20 years\' cash income as net worth ' +
      'in the reference run (' + bf.save.toFixed(1) + '% in the matched Baseline, where many draw wealth down), more than ' +
      'five times the US personal saving rate of 3.4% to 5.6% in 2022-2025 (BEA, FRED series PSAVERT)');
const ad = T['ADV:acc'];
console.log('  NOTE Adverse Environment: ' + ad.share.toFixed(1) + '% accumulate $60,000 (2019) on the engine\'s wealth, ' +
            ad.seeds70 + ' of ' + N + ' seeds at 70% or more; median ' + usd(ad.med) + ' (C1.2a has no stress clause)');
console.log(ok ? '\nCCO C1.2a SIMULATION CHECKS: ALL PASSED.' : '\nCCO C1.2a SIMULATION CHECKS: SOME FAILED.');
process.exit(ok ? 0 : 1);
