'use strict';
/* cco_sim_v56_checks_s57.js -- NEEC rescoring pass, group 2.5 (Session 57): CCO-PTF-CIP-SZH's simulation-dependent units
 * re-read on the design's published model at v5.6.0.
 *
 * The engine is harness.js from github.com/BetterToBest/compassionism-simulation at d10ed6e (v5.6.0), which reads its
 * engine out of index.html at the same commit (one copy since v5.3). This script does not copy or change the engine: it
 * loads harness.js as a module, builds the v5.6 release row and its no-programme run exactly as `node harness.js testbed
 * 500 release ref,adv,st --v54 --snab --slope` builds them (the release section's stepSection), adds the H1 row (every
 * dollar the Source pays backed by new output, a = 1, the other end of the backing sweep), and reads the adults through
 * the engine's own reporting hook (setRepHook), which draws no random number and changes no state. Before any table is
 * read it checks that the engine block is the v5.6 release's (its SHA-256 is in the release file's manifest) and that it
 * reproduces the v5.6 release's published figures for every row it uses, in every environment.
 *
 * What it reports (the units of NEEC_Rescoring_s57.md):
 *  [3] C1.1  the Societal Poverty Line (v2.0's indicator) on the engine's disposable income per adult, with and without the
 *            in-kind value of price cuts, at year 0 and year 20, and the largest reduction on any measure the engine reports;
 *  [4] C1.2a the share of adults, and of participants, whose net wealth with Acre Equity reaches $60,000 in 2019 dollars
 *            ($60,000 x CPI-U 2025 / CPI-U 2019, annual averages 321.943 and 255.657, BLS) by year 20;
 *  [5] C1.2b the wealth Gini at year 20 (the engine's giniW: debts as zero, x n/(n-1)), with Acre Equity added;
 *  [6] C1.3  housing distress windows, as cco_c13_checks_s54.js defined them: an adult is in distress in a year when cash
 *            income plus start-of-year savings cannot cover the year's cost (the engine's housingDistressOf rule, per
 *            adult); the share passing each 5-year window with no year of distress, inside and outside Public Trust Housing;
 *  [7] C3.2  programme inflation (the engine's endoAnn, the basket index's annual rise from the programme) and the price
 *            level at year 20, at a = 0 (the release row) and a = 1;
 *  [8] C3.3  the Adverse environment (recessions, an automation wave and 2% outside inflation) against the Reference
 *            environment on the same seeds: the degradation of four functions the engine measures, at year 20;
 *  [9] C3.4  the adjustment run of cco_simulation_checks_s38.js repeated: the monthly Basic Unit is multiplied by 0.7,
 *            0.8, 1.2 or 1.3 from the start of year 10 and held, Reference environment, at a = 0 and a = 1, each seed
 *            compared with the unadjusted run. COLLAPSE IS DEFINED BEFORE THE RUN: a seed collapses after an adjustment if,
 *            in any year from year 10, the share of adults below the cost of living exceeds the unadjusted run's by 10
 *            points or more, or the year's rise in the price level exceeds the unadjusted run's by 10 points or more, or
 *            any reported value is not finite.
 * N = 500 seeds (1 to 500), 500 adults, 20 years; figures are seed means unless stated.
 *
 * Usage: node cco_sim_v56_checks_s57.js run HARNESS LO HI OUT.json   runs seeds LO..HI and writes their per-seed summaries
 *        node cco_sim_v56_checks_s57.js report HARNESS OUT1.json ...   merges the parts (seeds paired, so splitting changes no
 *                                                                       figure) and prints the checks and tables
 * The run takes about 40 seconds a seed on one core (17 runs a seed); four parts of 125 seeds run side by side in about
 * 90 minutes. The report prints file names, checks and tables only. Deterministic.
 */
const fs = require('fs'), path = require('path'), crypto = require('crypto');
const MODE = process.argv[2], hFile = path.resolve(process.argv[3]);
if (MODE !== 'run' && MODE !== 'report') { console.error('usage: run HARNESS LO HI OUT.json | report HARNESS OUT.json ...'); process.exit(2); }
const H = require(hFile);
const md5 = f => crypto.createHash('md5').update(fs.readFileSync(f)).digest('hex');
let fails = 0;
function check(ok, text) { console.log((ok ? 'PASS  ' : 'FAIL  ') + text); if (!ok) fails++; }

// ---- [1] the engine -----------------------------------------------------------------------------------------------
console.log('[1] THE ENGINE');
const iFile = path.join(path.dirname(hFile), 'index.html'), man = H.runManifest();
console.log('harness.js md5 ' + md5(hFile).slice(0, 8) + ', index.html md5 ' + md5(iFile).slice(0, 8) + ', commit ' + man.commit.slice(0, 7) +
            (man.dirty ? ' (dirty)' : ''));
const REL = { harness: 'bed37dfc44ebea534098903eeaba8332c9c9837be1043eec615da7679449eedb',
              block: '973e7ce472d159cdcd17fe2cb38d0fc9b4c604bc1db641e3298ef513155136da' };
check(man.harnessSha256 === REL.harness && man.engineBlockSha256 === REL.block,
      'harness.js and the engine block in index.html are the v5.6 release\'s (data/releases/v5.6.json, meta.manifest: ' +
      'harnessSha256 ' + REL.harness.slice(0, 8) + ', engineBlockSha256 ' + REL.block.slice(0, 8) + ', release commit 5bf5bcc)');
const C = H.CFG;
check(C.POVERTY_LINE === 25000 && C.LIVING_WAGE_ANNUAL === 49370 && H.FULL_INTEGRATION.nAgents === 500 && H.FULL_INTEGRATION.years === 20,
      'constants read from source: wealth line $25,000, living-wage basket $49,370, 500 adults, 20 years');

// ---- the runner ---------------------------------------------------------------------------------------------------
const CPI = { 2019: 255.657, 2025: 321.943 }, BAR = 60000 * CPI[2025] / CPI[2019];
const SPL = { floor: 3.00 * 365, intercept: 1.30 * 365, slope: 0.5 };   // 2021 PPP $/day (Foster et al. 2025), as s51
const splLine = med => Math.max(SPL.floor, SPL.intercept + SPL.slope * med);
const FACT = [0.7, 0.8, 1.2, 1.3], STEP = 10;
const mean = a => a.reduce((s, x) => s + x, 0) / a.length;
const median = a => { const v = a.slice().sort((x, y) => x - y), h = (v.length - 1) / 2; return (v[Math.floor(h)] + v[Math.ceil(h)]) / 2; };
const share = (xs, f) => xs.filter(f).length / xs.length * 100;
const ginW = xs => H.giniOfArr(xs) * xs.length / (xs.length - 1);
const ENVS = { ref: ['Reference', H.FULL_INTEGRATION], adv: ['Adverse', H.ADVERSE_REFERENCE], st: ['Stress Test', H.STRESS_TEST] };
const SNALL = { abawd: true, slope: true }, SC = H.SPEND_SOURCED;

function study(env, adjust, lo, hi) {
  const P = Object.assign({}, ENVS[env][1]), PR = H.tbPresets(P), rows = H.releaseRowsV54(SC);
  const rel = rows.find(r => r.j === 'release'), h1 = rows.find(r => r.j === 'h1');
  const base = { sc: SC, so: H.REL_V52_STUDY, hh: rel.v.hh, sg: true, g: H.ACCT_V53, em: true, fb: true, v54: rel.v.v54 };
  const spec = [['base', null, 1], ['rel', rel, 1], ['h1', h1, 1]];
  if (adjust) FACT.forEach(f => { spec.push(['rel' + f, rel, f]); spec.push(['h1' + f, h1, f]); });
  const cfgs = spec.map(([, r]) => r ? H.n1Row(PR, 'framework', r.v) : Object.assign({ p: PR.baseline() }, base));
  cfgs.forEach(c => { c.p = Object.assign({}, c.p); c.sn = Object.assign({}, SNALL); });
  const bu0 = cfgs.map(c => c.p.bu), out = spec.map(() => []);
  let done = 0, cur = null;
  H.setRepHook(function (agents, yr, T, lf) {
    const i = done % cfgs.length, f = spec[i][2];
    if (yr === 0) cur = { yr: [], dis: [], pth: agents.map(a => a.inPTH ? 1 : 0) };
    const disp = agents.map(a => (+a._tbDisp || 0) / lf), ext = agents.map(a => (+a._tbExt || 0) / lf);
    const dis = agents.map(a => { const inc = (+a.yrWageUSD || 0) + (+a.yrConvUSD || 0) + (+a.yrSSUSD || 0), w = +a.yrWealthStartUSD || 0;
                                  return inc + Math.max(0, w) < (+a.yrCostUSD || 0) ? 1 : 0; });
    const y = { lf: lf, f0: share(agents, a => (a._tbGap || 0) > 0), pov: share(agents, a => a.wealth < C.POVERTY_LINE * lf),
                spl: share(disp, v => v < splLine(median(disp))), splX: share(ext, v => v < splLine(median(ext))), splMed: median(disp),
                disM: mean(dis) * 100 };
    cur.dis[yr] = dis;
    if (yr === T - 1) {
      const w = agents.map(a => a.wealth / lf), we = agents.map(a => (a.wealth + (+a.acreEquity || 0)) / lf), part = agents.map(a => !!a.inCCO);
      const win = sel => [0, 5, 10, 15].map(st => { let ok = 0, m = 0;          // per agent: a whole 5-year window with no year of distress
        for (let j = 0; j < cur.pth.length; j++) { if (!sel(j)) continue; m++; let d = 0; for (let q = st; q < st + 5; q++) d += cur.dis[q][j]; if (!d) ok++; }
        return m ? ok / m * 100 : null; });
      Object.assign(y, { giniW: ginW(agents.map(a => a.wealth)), giniWE: ginW(we), medW: median(we),
                         bar: share(we, v => v >= BAR), barNoAE: share(w, v => v >= BAR), part: share(part, v => v),
                         barPart: we.filter((v, k) => part[k]).length ? share(we.filter((v, k) => part[k]), v => v >= BAR) : 0,
                         win: { all: win(() => true), inP: win(j => cur.pth[j] === 1), outP: win(j => cur.pth[j] === 0), pthS: mean(cur.pth) * 100 } });
    }
    cur.yr[yr] = y;
    if (f !== 1 && yr === STEP - 1) cfgs[i].p.bu = bu0[i] * f;                 // from the start of year 10
    if (yr === T - 1) { cfgs[i].p.bu = bu0[i]; out[i].push(cur.yr); done++; }
  });
  let R;
  try { R = H.tbStudy(cfgs, hi, P, Object.assign({ fin: 'tax', aT: 0, a: 0, X: 0, sc: SC }, H.REL_V52_STUDY), lo); }
  finally { H.setRepHook(null); }
  const o = {};
  spec.forEach(([k], i) => { o[k] = { s: {}, t: out[i] }; KEYS.forEach(q => { o[k].s[q] = Array.from(R[i]._s[q]); }); });
  return o;
}
const KEYS = ['pov', 'fgt0PY', 'bOAPy', 'endoAnn', 'pLev20'];

if (MODE === 'run') {
  const lo = +process.argv[4], hi = +process.argv[5], S = {};
  for (const e of Object.keys(ENVS)) S[e] = study(e, e === 'ref', lo, hi);
  fs.writeFileSync(process.argv[6], JSON.stringify({ lo: lo, hi: hi, manifest: man, S: S }));
  console.log('wrote ' + process.argv[6] + ' (seeds ' + lo + '-' + hi + ')');
  process.exit(fails ? 1 : 0);
}
const PARTS = process.argv.slice(4).map(f => JSON.parse(fs.readFileSync(f, 'utf8'))).sort((x, y) => x.lo - y.lo);
check(PARTS.every((x, i) => (i === 0 ? x.lo === 1 : x.lo === PARTS[i - 1].hi + 1) && x.manifest.engineBlockSha256 === REL.block),
      'the parts cover seeds 1-' + PARTS[PARTS.length - 1].hi + ' in order, each from the same engine block');
const N = PARTS[PARTS.length - 1].hi, S = {};
for (const e of Object.keys(ENVS)) { S[e] = {};
  for (const k of Object.keys(PARTS[0].S[e])) {
    const s = {}; KEYS.forEach(q => { s[q] = [].concat(...PARTS.map(x => x.S[e][k].s[q])); });
    const R = { _s: s }; KEYS.forEach(q => { R[q] = mean(s[q]); });
    S[e][k] = { R: R, t: [].concat(...PARTS.map(x => x.S[e][k].t)) }; } }
const at = (e, k, yr, f) => mean(S[e][k].t.map(t => t[yr === 'end' ? t.length - 1 : yr][f]));

// ---- [2] reproduction of the v5.6 release ----------------------------------------------------------------------------
console.log('\n[2] REPRODUCTION OF THE v5.6 RELEASE (data/releases/v5.6.json: panels.20 and backing; values as published)');
const PUB = { ref: { base: [32.7, 49.2], rel: [44.4, 19.5, 50.8, 0.4917], h1: [8.7, 14.4, 0.1] },
              adv: { base: [45.1, 66.0], rel: [80.9, 31.1, 60.9], h1: [22.6, 33.1, 0.1] },
              st: { base: [45.1, 66.0], rel: [76.3, 52.8, 27.4], h1: [36.1, 52.6, 0.0] } };
if (N === 500) for (const e of Object.keys(PUB)) {
  const P = PUB[e], r = k => S[e][k].R;
  const ok = (+r('base').pov.toFixed(1) === P.base[0] && +r('base').fgt0PY.toFixed(1) === P.base[1] &&
              ['rel', 'h1'].every(k => +r(k).pov.toFixed(1) === P[k][0] && +r(k).fgt0PY.toFixed(1) === P[k][1] &&
                                        +(r(k).endoAnn * 100).toFixed(1) === P[k][2]) &&
              (e !== 'ref' || +at('ref', 'rel', 'end', 'giniW').toFixed(4) === P.rel[3]) &&
              Math.abs(at(e, 'rel', 'end', 'pov') - r('rel').pov) < 1e-6);
  check(ok, ENVS[e][0] + ': too little wealth, below the cost of living and programme inflation for the no-programme run, the release ' +
        'row (a = 0) and H1 (a = 1) equal the published figures' + (e === 'ref' ? '; the wealth Gini at year 20, 0.4917, likewise' : '') +
        '; the hook\'s own count of too little wealth equals the engine\'s');
}
else console.log('(skipped: run with 500 seeds to compare with the release)');

const p1 = x => x.toFixed(1), red = (a, b) => (a - b) / a * 100;
const ROWN = { base: 'No program (today\'s safety net)', rel: 'Compassionism, release row (a = 0)', h1: 'Compassionism, H1 (a = 1)' };

// ---- [3] C1.1 ---------------------------------------------------------------------------------------------------------
console.log('\n[3] C1.1: THE SOCIETAL POVERTY LINE (2021 PPP: max($3.00, $1.30 + 0.5 x median) a day; disposable income per adult, ' +
            'year-0 dollars; X = with the in-kind value of price cuts)');
console.log('| Environment | Run | SPL, year 0 | SPL, year 20 | Reduction from year 0 | SPL X, year 20 | Below the cost of living, year 20 | Median disposable income, year 20 |');
console.log('|---|---|---:|---:|---:|---:|---:|---:|');
for (const e of Object.keys(ENVS)) for (const k of ['base', 'rel', 'h1'])
  console.log('| ' + ENVS[e][0] + ' | ' + ROWN[k] + ' | ' + p1(at(e, k, 0, 'spl')) + '% | ' + p1(at(e, k, 'end', 'spl')) + '% | ' +
              p1(red(at(e, k, 0, 'spl'), at(e, k, 'end', 'spl'))) + '% | ' + p1(at(e, k, 'end', 'splX')) + '% | ' +
              p1(at(e, k, 'end', 'f0')) + '% | $' + Math.round(at(e, k, 'end', 'splMed')).toLocaleString('en-US') + ' |');
const vsB = (e, k, f) => red(at(e, 'base', 'end', f), at(e, k, 'end', f));
console.log('\nReductions against the paired no-programme run at year 20 (release row; H1):');
for (const e of Object.keys(ENVS))
  console.log('- ' + ENVS[e][0] + ': SPL ' + p1(vsB(e, 'rel', 'spl')) + '%; ' + p1(vsB(e, 'h1', 'spl')) + '%. SPL X ' + p1(vsB(e, 'rel', 'splX')) + '%; ' +
              p1(vsB(e, 'h1', 'splX')) + '%. Below the cost of living (person-years, the release\'s measure) ' +
              p1(red(S[e].base.R.fgt0PY, S[e].rel.R.fgt0PY)) + '%; ' + p1(red(S[e].base.R.fgt0PY, S[e].h1.R.fgt0PY)) +
              '%. Below 30 days of basic living ' + p1(red(S[e].base.R.bOAPy, S[e].rel.R.bOAPy)) + '%; ' + p1(red(S[e].base.R.bOAPy, S[e].h1.R.bOAPy)) + '%.');
const best = Math.max(...['rel', 'h1'].map(k => Math.max(vsB('ref', k, 'spl'), vsB('ref', k, 'splX'), red(S.ref.base.R.fgt0PY, S.ref[k].R.fgt0PY),
                                                          red(S.ref.base.R.bOAPy, S.ref[k].R.bOAPy))));
check(best < 90, 'Reference: no reduction above reaches 90% (largest ' + p1(best) + '%)');

// ---- [4] C1.2a --------------------------------------------------------------------------------------------------------
console.log('\n[4] C1.2a: NET WEALTH WITH ACRE EQUITY AT YEAR 20, AGAINST $60,000 IN 2019 DOLLARS ($' + Math.round(BAR).toLocaleString('en-US') +
            ' in the engine\'s year-0 dollars, 2025)');
console.log('| Environment | Run | Adults at the bar | Without Acre Equity | Participants at the bar | Participants | Seeds with 70% of participants at the bar | Median net wealth |');
console.log('|---|---|---:|---:|---:|---:|---:|---:|');
for (const e of Object.keys(ENVS)) for (const k of ['base', 'rel', 'h1']) {
  const t = S[e][k].t.map(x => x[x.length - 1]);
  console.log('| ' + ENVS[e][0] + ' | ' + ROWN[k] + ' | ' + p1(mean(t.map(x => x.bar))) + '% | ' + p1(mean(t.map(x => x.barNoAE))) + '% | ' +
              (k === 'base' ? '-' : p1(mean(t.map(x => x.barPart))) + '%') + ' | ' + (k === 'base' ? '-' : p1(mean(t.map(x => x.part))) + '%') + ' | ' +
              (k === 'base' ? '-' : t.filter(x => x.barPart >= 70).length + ' of ' + t.length) + ' | $' + Math.round(mean(t.map(x => x.medW))).toLocaleString('en-US') + ' |');
}

// ---- [5] C1.2b --------------------------------------------------------------------------------------------------------
console.log('\n[5] C1.2b: THE WEALTH GINI AT YEAR 20 (debts as zero, x n/(n-1), as the engine reports it)');
console.log('| Environment | Run | Gini | With Acre Equity | Seeds below 0.35 |');
console.log('|---|---|---:|---:|---:|');
for (const e of Object.keys(ENVS)) for (const k of ['base', 'rel', 'h1']) {
  const t = S[e][k].t.map(x => x[x.length - 1]);
  console.log('| ' + ENVS[e][0] + ' | ' + ROWN[k] + ' | ' + mean(t.map(x => x.giniW)).toFixed(3) + ' | ' + mean(t.map(x => x.giniWE)).toFixed(3) + ' | ' +
              t.filter(x => x.giniW < 0.35).length + ' of ' + t.length + ' |');
}

// ---- [6] C1.3 ---------------------------------------------------------------------------------------------------------
console.log('\n[6] C1.3: ADULTS PASSING A 5-YEAR WINDOW WITH NO YEAR OF DISTRESS (years 1-5 ... 16-20; PTH = Public Trust Housing)');
console.log('| Environment | Run | Years 1-5 | 6-10 | 11-15 | 16-20 | Lowest | In PTH (share; lowest window) | Outside PTH, lowest window |');
console.log('|---|---|---:|---:|---:|---:|---:|---:|---:|');
const winOf = (t, g) => [0, 1, 2, 3].map(w => mean(t.map(r => r[r.length - 1].win[g][w]).filter(x => x !== null)));
for (const e of Object.keys(ENVS)) for (const k of ['base', 'rel', 'h1']) {
  const t = S[e][k].t, all = winOf(t, 'all'), inP = winOf(t, 'inP'), outP = winOf(t, 'outP'), pthS = mean(t.map(r => r[r.length - 1].win.pthS));
  console.log('| ' + ENVS[e][0] + ' | ' + ROWN[k] + ' | ' + all.map(p1).join('% | ') + '% | ' + p1(Math.min(...all)) + '% | ' +
              (k === 'base' ? '-' : p1(pthS) + '%; ' + p1(Math.min(...inP)) + '%') + ' | ' + (k === 'base' ? '-' : p1(Math.min(...outP)) + '%') + ' |');
}

// ---- [7] C3.2 ---------------------------------------------------------------------------------------------------------
console.log('\n[7] C3.2: PROGRAMME INFLATION (the basket index\'s annual rise from the programme) AND THE PRICE LEVEL AT YEAR 20');
console.log('| Environment | Outside inflation | Run | Programme inflation a year | Price level, year 20 (median over seeds) | Seeds at or under 3% |');
console.log('|---|---:|---|---:|---:|---:|');
for (const e of Object.keys(ENVS)) for (const k of ['rel', 'h1']) {
  const r = S[e][k].R;
  console.log('| ' + ENVS[e][0] + ' | ' + ((ENVS[e][1].inflRate || 0) * 100) + '%' + ' | ' + ROWN[k] + ' | ' +
              p1(r.endoAnn * 100) + '% | ' + median(Array.from(r._s.pLev20)).toFixed(2) + ' | ' + Array.from(r._s.endoAnn).filter(x => x <= 0.03).length + ' of ' + N + ' |');
}

// ---- [8] C3.3 ---------------------------------------------------------------------------------------------------------
console.log('\n[8] C3.3: THE ADVERSE ENVIRONMENT AGAINST THE REFERENCE, YEAR 20, SAME SEEDS (degradation = fall in the share, % of the Reference share)');
console.log('| Run | Function (share of adults at year 20) | Reference | Adverse | Degradation | Stress Test | Degradation |');
console.log('|---|---|---:|---:|---:|---:|---:|');
const FN = [['Not below the cost of living', t => 100 - t.f0], ['Above the Societal Poverty Line', t => 100 - t.spl],
            ['Not in housing distress', t => 100 - t.disM], ['Above the wealth line (six months of costs)', t => 100 - t.pov]];
for (const k of ['rel', 'h1']) for (const [lab, f] of FN) {
  const v = e => mean(S[e][k].t.map(r => f(r[r.length - 1])));
  console.log('| ' + ROWN[k] + ' | ' + lab + ' | ' + p1(v('ref')) + '% | ' + p1(v('adv')) + '% | ' + p1(red(v('ref'), v('adv'))) + '% | ' +
              p1(v('st')) + '% | ' + p1(red(v('ref'), v('st'))) + '% |');
}

// ---- [9] C3.4 ---------------------------------------------------------------------------------------------------------
console.log('\n[9] C3.4: THE BASIC UNIT STEPPED FROM YEAR ' + STEP + ' AND HELD, REFERENCE, EACH SEED AGAINST THE UNADJUSTED RUN');
console.log('| Backing | Step | Below the cost of living, year 20: adjusted / unadjusted | Price level, year 20 (median): adjusted / unadjusted | ' +
            'Largest excess rise, cost of living (points) | Largest excess price rise (points) | Seeds collapsing |');
console.log('|---|---|---:|---:|---:|---:|---:|');
for (const k of ['rel', 'h1']) for (const f of FACT) {
  const A = S.ref[k + f].t, U = S.ref[k].t; let wC = -Infinity, wP = -Infinity, col = 0;
  A.forEach((a, s) => { let c = false;
    for (let y = STEP; y < a.length; y++) {
      const dc = a[y].f0 - U[s][y].f0, dp = (a[y].lf / a[y - 1].lf - U[s][y].lf / U[s][y - 1].lf) * 100;
      wC = Math.max(wC, dc); wP = Math.max(wP, dp);
      if (!(isFinite(a[y].f0) && isFinite(a[y].lf)) || dc >= 10 || dp >= 10) c = true;
    }
    if (c) col++; });
  console.log('| ' + (k === 'rel' ? 'a = 0 (release row)' : 'a = 1 (H1)') + ' | x' + f + ' | ' + p1(at('ref', k + f, 'end', 'f0')) + '% / ' + p1(at('ref', k, 'end', 'f0')) + '% | ' +
              median(A.map(r => r[r.length - 1].lf)).toFixed(2) + ' / ' + median(U.map(r => r[r.length - 1].lf)).toFixed(2) + ' | ' +
              wC.toFixed(1) + ' | ' + wP.toFixed(1) + ' | ' + col + ' of ' + A.length + ' |');
}

console.log('\nSUMMARY: ' + (fails ? fails + ' check(s) failed' : 'all checks pass') + '; ' + N + ' seeds.');
process.exitCode = fails ? 1 : 0;
