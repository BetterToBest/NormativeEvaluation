#!/usr/bin/env python3
"""
NEEC C1.4 Simulation Cross-Validation — Reference Implementation
==================================================================
Companion tool to NEEC Paper Appendix G. Re-derives the automation-relevant
mechanics of the compassionism-simulation (index.html) from source, for
cross-checking C1.4 (Automation Resilience) claims against actual sim
behavior, without needing a browser.

THIS IS AN INDEPENDENT RE-IMPLEMENTATION, NOT THE ACTUAL JAVASCRIPT.
Before treating its output as authoritative, cross-check against the real
tool's own CSV export (Research Export button -> downloadCSV()) per
Appendix G.4 Step 4. Discrepancies should be assumed until checked.
As of this update, a second, stronger check is also available: running the
literally-extracted v4.1 mechanics under Node.js (see the companion
neec_c14_v41_realjs_check.js in this project's materials), which was used to
validate THIS Python port before it was treated as trustworthy for Run
Record #2 (Appendix G.7) -- see that run record for the comparison.

v4.1 UPDATE (this revision): retargeted from v3.9 to v4.1. This was NOT a
small parameter tweak -- the intervening v4.0 revision (the simulation's
largest to date) changed five mechanisms this script depends on: octave
advancement (fixed-probability -> FBS-gated), CCO conversion-rate ceiling
(quality-only -> octave-and-quality), the SZH/PTF synergy bonus (plain-linear
in coherence -> network-density-gated via szhTheta()), PTH Acre Equity
(appreciation-only -> adds a payment-to-equity contribution), and PTF
adoption (distress-only -> adds a Bass 1969 imitation term). None of these
were optional to skip: all five sit inside runYear() and materially change
the wealth/poverty trajectory (see Run Record #2 for the before/after
numbers). The v3.9-targeting functions are RETAINED below, renamed with a
_v39 suffix, specifically so this comparison is reproducible by a future
reader rather than only asserted in the run record's prose.

HOW TO RE-RUN THIS AGAINST A NEW SIMULATION VERSION (Appendix G.4):
  1. Diff this file's CFG dict and the *_v41 functions below against the new
     index.html's <script> block (search for the same constant/function
     names). Update anything that changed; rename the current _v41 functions
     to _v(old) and add fresh _v(new) functions, exactly as this revision
     kept _v39 alongside _v41, so the next diff has a same-session comparison
     baseline too.
  2. Re-run cap_saturation_check() first -- it's pure arithmetic, cheap, and
     catches "inert parameter" bugs like the v3.9 AI_DISPLACEMENT_RATE_2
     finding without needing a stochastic run. (Unaffected by the v4.0/v4.1
     mechanism changes -- popAIDisp's own logic is untouched since v3.9; see
     Run Record #2.)
  3. grep the new source for every CFG.* constant name to catch dead/unused
     constants before they're assumed load-bearing (this is how the
     SZH_PTF_BONUS finding below was caught and re-confirmed for v4.1).
  4. Re-run cross_validate() and log a new entry in Appendix G.7.
  5. Note the sim's META.VERSION and changelog delta in your run record.

Usage:
    python3 neec_c14_crossvalidation.py
"""
import random, math, statistics, csv, sys

# ---------------------------------------------------------------------------
# CONSTANTS — copied verbatim from index.html's CFG object. RE-VERIFY THESE
# against the current source before relying on any output below.
# Source constants confirmed for: v4.1 (August 2026). Cross-checked against
# v3.9 (CFG_V39 below): every constant shared between the two versions is
# byte-identical (WAGE_*, AI_DISPLACEMENT_*, SIM_COST_SCALE, BASE_DAILY_COST,
# POVERTY_LINE, PHI_*, PROG_*, WEALTH_FLOOR, SZH_ALL_RESIDENTS/SZH_PTF_BONUS)
# -- see Run Record #2 for the full side-by-side.
# ---------------------------------------------------------------------------
CFG = dict(
    WAGE_BASE_GROWTH=0.010, WAGE_BLEI_BONUS=0.008, WAGE_OCTAVE_BONUS=0.003,
    WAGE_MEDIAN_SIU=35, POVERTY_LINE=25000, SIM_COST_SCALE=1500,
    BASE_DAILY_COST=68.33, CCO_PTH_DAILY_COST=31.67,
    AI_Y1=5, AI_Y2=15, AI_R1=0.012, AI_R2=0.022,
    BLEI_PRECARIOUS_MAX=30, PROG_PIVOT=3.0, PROG_RATE=0.040, PROG_TAX_MAX=0.75,
    SZH_ALL=0.06, SZH_PTF_BONUS=0.05,  # SZH_PTF_BONUS: present in CFG, confirmed UNUSED by any
                                        # v4.1 formula (grep-verified — see Run Record #2, finding #2).
                                        # Kept here only because it's genuinely still in the real CFG object.
    WEALTH_FLOOR=-10000, PHI_RATIO=1.618, PHI_QUALITY_THRESH=0.70,
    # --- v4.0/v4.1 additions (not present in the v3.9 CFG this script used to target) ---
    SZH_THETA_THRESHOLD=0.55, SZH_THETA_MAX_COH=0.90, SZH_THETA_MAX=0.25,
    FBS_LAMBDA_LO=0.001, FBS_LAMBDA_HI=0.008,
    FBS_EDC_RESIDUAL_BASE=0.12, FBS_EDC_RESIDUAL_PTH=0.025,
    FBS_CIP_LAMBDA_BOOST=0.20,
    PTH_EQUITY_CONTRIB_SHARE=0.25,
    PTF_BASS_Q=0.05,
)
CFG['SIU_TO_USD'] = (CFG['BASE_DAILY_COST'] * 365) / CFG['SIM_COST_SCALE']  # v4.0 addition; ~16.627

SIM_VERSION_CHECKED = "4.1"        # update when re-verifying constants
SIM_VERSION_PREVIOUSLY_CHECKED = "3.9"  # what this script targeted before this revision


def popAIDisp(yr, automation_on):
    """Population-wide automation wage-growth drag. UNCHANGED between v3.9
    and v4.1 -- verified by direct text comparison of both versions' source
    during this revision, not assumed. Verify the branch logic and the
    Math.min(0.10, ...) cap are still present in whatever version you're
    checking next -- this is the exact mechanism the RATE_2-is-inert finding
    depends on, and it has now been re-confirmed twice (v3.9 and v4.1)."""
    if not automation_on:
        return 0.0
    if yr >= CFG['AI_Y2']:
        d = CFG['AI_R1']*(CFG['AI_Y2']-CFG['AI_Y1']) + CFG['AI_R2']*(yr-CFG['AI_Y2']+1)
    elif yr >= CFG['AI_Y1']:
        d = CFG['AI_R1']*(yr-CFG['AI_Y1']+1)
    else:
        d = 0.0
    return min(0.10, d)


def cap_saturation_check(years=25, automation_on=True, verbose=True):
    """Appendix G.4 Step 3: pure-arithmetic check for inert parameters.
    Returns the first year the cap is reached, and whether the
    'acceleration' branch (yr >= AI_Y2) ever produces a value below the cap
    (if it never does, that branch's distinct rate constant is inert).
    Re-run against v4.1: identical result to v3.9, since popAIDisp is
    unchanged (see docstring above)."""
    first_capped_year = None
    accel_branch_ever_uncapped = False
    for yr in range(years):
        raw = None
        if yr >= CFG['AI_Y2']:
            raw = CFG['AI_R1']*(CFG['AI_Y2']-CFG['AI_Y1']) + CFG['AI_R2']*(yr-CFG['AI_Y2']+1)
            if raw < 0.10:
                accel_branch_ever_uncapped = True
        elif yr >= CFG['AI_Y1']:
            raw = CFG['AI_R1']*(yr-CFG['AI_Y1']+1)
        val = popAIDisp(yr, automation_on)
        if verbose:
            flag = " <- CAP HIT" if (raw is not None and raw >= 0.10 and first_capped_year is None) else ""
            print(f"  yr {yr:2d}: raw={raw if raw is not None else 0:.4f}  capped={val:.4f}{flag}")
        if raw is not None and raw >= 0.10 and first_capped_year is None:
            first_capped_year = yr
    return dict(first_capped_year=first_capped_year,
                acceleration_branch_ever_matters=accel_branch_ever_uncapped)


def lognormal(rng, mu, sigma):
    return rng.lognormvariate(mu, sigma)


def beta_sample(rng, a, b):
    return rng.betavariate(a, b)


# ===========================================================================
# v3.9-TARGETING FUNCTIONS (legacy — retained verbatim from the prior version
# of this script, renamed with _v39, so the mechanism diff below is something
# a reader can literally re-run and compare, not just take on faith).
# ===========================================================================

def agent_blei_v39(a, bu, ccoOn, pthOn):
    liquid = max(0.0, a['wealth']*0.20)
    gamma = 0.20 if (ccoOn and a['inCCO']) else 0.12
    buFood = bu*(990/1200) if (ccoOn and a['inCCO'] and bu > 0) else 0.0
    baseCost = CFG['CCO_PTH_DAILY_COST'] if (ccoOn and a['inCCO'] and pthOn and a['inPTH']) else CFG['BASE_DAILY_COST']
    dc = max(baseCost, 0.1)
    return (liquid + gamma*max(a['wage'], 0.1) + buFood)/dc  # NOTE: v3.9 never converted wage (SIU) to
                                                               # USD here -- the pre-v4.0 unit-mixing issue
                                                               # index.html's own v4.0 changelog documents.


def make_agents_v39(rng, n, p):
    agents = []
    for _ in range(n):
        inCCO = p['ccoOn'] and rng.random() < p['partRate']
        inPTF = p['ptf'] and rng.random() < p['ptfShare']
        inPTH = p['pth'] and rng.random() < p['pthUptake']
        qN = (1 - p['cipDemo']*0.5) if p['cip'] else 1.0
        agents.append(dict(
            wealth=lognormal(rng, 10.5, 1.2),
            wage=lognormal(rng, 3.5, 0.5),
            octave=int(beta_sample(rng, 2, 5)*p['maxOct']),
            quality=min(p['maxMult'], max(0.0, lognormal(rng, math.log(p['maxMult']*0.5), 0.4)*qN)),
            automationRisk=0.2 + rng.random()*0.8,
            inCCO=inCCO, inPTF=inPTF, inPTH=inPTH,
            buBalance=0.0, acreEquity=5000.0 if inPTH else 0.0,
        ))
    return agents


def run_year_v39(rng, agents, yr, p, automation_on):
    disp = popAIDisp(yr, automation_on)
    ptfConvBonus = 1.30 if not (p['szh'] and p['ptf']) else 1.30 + (p['szhCoh']-0.50)*0.35
    pthApprBonus = p['szhCoh']*0.01 if p['szh'] else 0.0
    szhPartBoost = p['szhCoh']*0.04 if (p['szh'] and p['ccoOn']) else 0.0
    advRate = 0.08 + (p['cipDemo']*0.04 if p['cip'] else 0.0)
    simCost = CFG['SIM_COST_SCALE']

    total_wage_income = 0.0
    for a in agents:
        if math.isnan(a['wealth']):
            a['wealth'] = 0.0
        if a['wage'] <= 0:
            a['wage'] = 1.0
        blei = agent_blei_v39(a, p['bu'], p['ccoOn'], p['pth'])
        wg = CFG['WAGE_BASE_GROWTH']
        if blei > CFG['BLEI_PRECARIOUS_MAX']:
            drFactor = 1/(1+0.5*max(0.0, a['wage']/CFG['WAGE_MEDIAN_SIU']-1))
            wg += CFG['WAGE_BLEI_BONUS']*max(0.1, drFactor)
        wg += a['octave']*CFG['WAGE_OCTAVE_BONUS']
        if p['cip']:
            wg += p['cipDemo']*0.005
        wg -= disp*(a['automationRisk'] or 0.5)
        a['wage'] = max(a['wage']*0.80, a['wage']*(1+wg))
        total_wage_income += a['wage']*12

        cf = 1.0
        if p['ptf'] and a['inPTF']:
            cf *= (1 - (0.12 + p['szhCoh']*0.04 if p['szh'] else 0.12))
        if p['pth'] and a['inPTH']:
            cf *= 0.65
        if p['ccoOn'] and a['inCCO'] and p['bu'] > 0:
            cf *= 0.80
        a['wealth'] += a['wage']*12 - simCost*cf

        if p['ccoOn'] and a['inCCO']:
            decay = 0.0 if p['expiry'] < 2 else 0.7
            a['buBalance'] = min(a['buBalance']*decay + p['bu'], p['bu']*3)
            spend = a['buBalance']*(0.60+rng.random()*0.30)
            a['buBalance'] -= spend
            if p['cip'] and rng.random() < p['cipDemo']*0.15:
                a['quality'] = min(p['maxMult'], a['quality']+0.1)
            baseRate = 1 + (a['quality']/p['maxMult'])*(p['maxMult']-1)
            phi = CFG['PHI_RATIO'] if (p['phi'] and a['quality'] > p['maxMult']*CFG['PHI_QUALITY_THRESH']) else 1.0
            ptfB = ptfConvBonus if (p['ptf'] and a['inPTF']) else 1.0
            cipB = (1+p['cipDemo']*0.12) if p['cip'] else 1.0
            rate = min(baseRate*phi*ptfB, p['maxMult']*(CFG['PHI_RATIO'] if p['phi'] else 1.0))
            bTax = p['tax']*(1-p['cipDemo']*0.18) if p['cip'] else p['tax']
            progTax = min(CFG['PROG_TAX_MAX'], bTax + max(0.0, (rate-CFG['PROG_PIVOT'])*CFG['PROG_RATE']))
            a['wealth'] += spend*rate*(1-progTax)*cipB
            if blei > CFG['BLEI_PRECARIOUS_MAX'] and rng.random() < advRate and a['octave'] < p['maxOct']:
                a['octave'] += 1
            if rng.random() < szhPartBoost and not a['inPTF'] and p['ptf']:
                a['inPTF'] = rng.random() < p['ptfShare']

        if p['pth'] and a['inPTH']:
            ar = 0.030 + rng.random()*0.020 + pthApprBonus
            appr = a['acreEquity']*ar
            a['acreEquity'] += appr
            a['wealth'] += appr*0.5

        if p['ptf'] and not a['inPTF'] and p['ptfShare'] > 0 and yr > 0:
            ap = 0.005 + (0.015 if blei < CFG['BLEI_PRECARIOUS_MAX'] else 0.0)
            if rng.random() < ap:
                a['inPTF'] = True

        if a['wealth'] < CFG['WEALTH_FLOOR']:
            a['wealth'] = CFG['WEALTH_FLOOR']

    return total_wage_income


def calc_metrics_v39(agents):
    """ORIGINAL v3.9-script version. NOTE (port-fidelity finding, this
    revision): this clamps wealth to >=0 before computing the median. The
    real index.html — in both the v3.9 era and v4.1 today — does NOT apply
    that clamp for the median (only for the separate Gini/net-wealth total).
    Retained AS-ORIGINALLY-WRITTEN here for an apples-to-apples re-run of the
    legacy script; the corrected convention is in calc_metrics_v41 below and
    should be treated as authoritative going forward. See Run Record #2,
    finding #4."""
    ws = sorted(max(0.0, a['wealth']) for a in agents)
    n = len(ws)
    pov = sum(1 for a in agents if a['wealth'] < CFG['POVERTY_LINE'])/n
    med = ws[n//2] if n % 2 else (ws[n//2-1]+ws[n//2])/2
    return dict(pov=pov, med=med)


def run_scenario_v39(seed, years, automation_on, n=500, preset='reference'):
    rng = random.Random(seed)
    p = dict(bu=1200, maxOct=6, expiry=1, tax=0.12, maxMult=9, partRate=0.78,
             ptfShare=0.18, pthUptake=0.20, szhCoh=0.72, cipDemo=0.65,
             phi=True, ptf=True, pth=True, szh=True, cip=True, ccoOn=True)
    agents = make_agents_v39(rng, n, p)
    demand_series, pov_series, wealth_series = [], [], []
    for yr in range(years):
        demand = run_year_v39(rng, agents, yr, p, automation_on)
        m = calc_metrics_v39(agents)
        demand_series.append(demand)
        pov_series.append(m['pov']*100)
        wealth_series.append(m['med'])
    return demand_series, pov_series, wealth_series


# ===========================================================================
# v4.1-TARGETING FUNCTIONS (current — faithful re-derivation of index.html's
# actual runYear()/makeAgent()/agentBLEI()/szhTheta()/calcMetrics() as of
# the v4.1 source in this project's files. Cross-validated against a literal
# Node.js execution of the extracted JS — see Run Record #2 for the
# comparison and neec_c14_v41_realjs_check.js for that script.)
# ===========================================================================

def szh_theta(coh):
    """v4.0 addition. Network-density-gated SZH/PTF synergy coefficient.
    NOTE (re-confirmed for v4.1, not assumed): every call site in index.html
    passes szhCoh (the Zone Coherence Index slider, 0-0.95) to this function
    — never the actual simulated PTF adoption fraction the code separately
    computes elsewhere (ptfAdoptFrac, used only for the Bass diffusion term).
    This means the mechanism the v4.0/v4.1 changelog and in-app Assumptions
    panel describe as '0 below 55% PTF density, scaling to 0.25 at 90%+
    density' is actually gated on a user-set coherence slider, not on
    simulated density. See Run Record #2, finding #3."""
    if math.isnan(coh):
        coh = 0.0
    if coh < CFG['SZH_THETA_THRESHOLD']:
        return 0.0
    return min(CFG['SZH_THETA_MAX'],
                (coh - CFG['SZH_THETA_THRESHOLD']) / (CFG['SZH_THETA_MAX_COH'] - CFG['SZH_THETA_THRESHOLD']) * CFG['SZH_THETA_MAX'])


def agent_blei_v41(a, bu_alloc, cco_on, pth_on, szh_on, szh_coh, ptf_on):
    liquid = max(0.0, a['wealth'] * 0.20)
    gamma = 0.20 if (cco_on and a['inCCO']) else 0.12
    m_inc = max(a['wage'] if not math.isnan(a['wage']) else 1.0, 0.1) * CFG['SIU_TO_USD']  # v4.0: SIU->USD fix
    bu_food = bu_alloc * (990/1200) if (cco_on and a['inCCO'] and bu_alloc > 0) else 0.0
    szh_d = szh_coh * CFG['SZH_ALL'] if szh_on else 0.0
    if szh_on and ptf_on and a['inPTF']:
        szh_d += szh_theta(szh_coh) * 0.20
    base_cost = CFG['CCO_PTH_DAILY_COST'] if (cco_on and a['inCCO'] and pth_on and a['inPTH']) else CFG['BASE_DAILY_COST']
    dc = max(base_cost * (1 - szh_d), 0.1)
    r = (liquid + gamma*m_inc + bu_food) / dc
    if math.isnan(r) or math.isinf(r):
        return 0.0
    return max(0.0, r)


def make_agent_v41(rng, p):
    inCCO = p['ccoOn'] and rng.random() < p['partRate']
    inPTF = p['ptf'] and rng.random() < p['ptfShare']
    inPTH = p['pth'] and rng.random() < p['pthUptake']
    qN = (1 - p['cipDemo']*0.5) if p['cip'] else 1.0
    maxOct = p.get('maxOct', 1) or 1
    maxMult = p.get('maxMult', 1) or 1
    return dict(
        wealth=lognormal(rng, 10.5, 1.2),
        wage=lognormal(rng, 3.5, 0.5),
        octave=int(beta_sample(rng, 2, 5) * maxOct),
        quality=min(maxMult, max(0.0, lognormal(rng, math.log(maxMult*0.5), 0.4) * qN)),
        automationRisk=0.2 + rng.random()*0.8,
        lam=CFG['FBS_LAMBDA_LO'] + rng.random()*(CFG['FBS_LAMBDA_HI']-CFG['FBS_LAMBDA_LO']),  # v4.0 addition
        inCCO=inCCO, inPTF=inPTF, inPTH=inPTH,
        buBalance=0.0, acreEquity=5000.0 if inPTH else 0.0,
    )


def make_agents_v41(rng, n, p):
    return [make_agent_v41(rng, p) for _ in range(n)]


def run_year_v41(rng, agents, yr, p, automation_on):
    """Faithful re-derivation of v4.1's runYear(). Shock/recession plumbing
    omitted (popShock hardcoded to 1.0) since the Reference preset this
    protocol uses has shock=false by default — matching what recSt.active
    would evaluate to anyway, and matching this script's own established
    scope (Appendix G.4 Step 4 doesn't call for shock scenarios)."""
    pthApprBonus = p['szhCoh']*0.01 if p['szh'] else 0.0
    szhThetaVal = szh_theta(p['szhCoh']) if p['szh'] else 0.0
    ptfConvBonus = 1.30 + (szhThetaVal if (p['szh'] and p['ptf']) else 0.0)
    szhPartBoost = szhThetaVal*0.16 if (p['szh'] and p['ccoOn']) else 0.0
    inflRate = p.get('inflRate', 0.0) or 0.0
    if p['ptf'] and inflRate > 0:
        inflRate *= (1 - p['ptfShare']*0.5)
    if p['pth'] and inflRate > 0:
        inflRate *= 0.90
    simCost = CFG['SIM_COST_SCALE'] * (1+inflRate)**yr
    dollarCost = CFG['BASE_DAILY_COST']*365*(1+inflRate)**yr
    popShock = 1.0  # Reference preset: shock off

    ptfAdoptFrac = 0.0
    if p['ptf'] and p['ptfShare'] > 0:
        ptfCount = sum(1 for a in agents if a['inPTF'])
        ptfAdoptFrac = ptfCount / max(1, len(agents))

    disp = popAIDisp(yr, automation_on)
    total_wage_income = 0.0

    for a in agents:
        if math.isnan(a['wealth']):
            a['wealth'] = 0.0
        if math.isnan(a['wage']) or a['wage'] <= 0:
            a['wage'] = 1.0
        agentVar = 0.90 + rng.random()*0.20
        incomeShock = popShock * agentVar
        bleiCheck = agent_blei_v41(a, p['bu'], p['ccoOn'], p['pth'], p['szh'], p['szhCoh'], p['ptf'])
        wg = CFG['WAGE_BASE_GROWTH']
        if bleiCheck > CFG['BLEI_PRECARIOUS_MAX']:
            drFactor = 1/(1+0.5*max(0.0, a['wage']/CFG['WAGE_MEDIAN_SIU']-1))
            wg += CFG['WAGE_BLEI_BONUS']*max(0.1, drFactor)
        wg += a['octave']*CFG['WAGE_OCTAVE_BONUS']
        if p['cip']:
            wg += p['cipDemo']*0.005
        wg -= disp*(a['automationRisk'] or 0.5)
        a['wage'] = max(a['wage']*0.80, a['wage']*(1+wg))
        if math.isnan(a['wage']):
            a['wage'] = 1.0
        total_wage_income += a['wage']*12

        cf = 1.0
        if p['ptf'] and a['inPTF']:
            cf *= (1 - (0.12 + p['szhCoh']*0.04 if p['szh'] else 0.12))
        if p['pth'] and a['inPTH']:
            cf *= 0.65
        if p['ccoOn'] and a['inCCO'] and p['bu'] > 0:
            cf *= 0.80
        a['wealth'] += a['wage']*12*incomeShock - simCost*cf
        if math.isnan(a['wealth']):
            a['wealth'] = 0.0

        if p['ccoOn'] and a['inCCO']:
            decay = 0.0 if p['expiry'] < 2 else 0.7
            a['buBalance'] = min(a['buBalance']*decay + p['bu'], p['bu']*3)
            spend = a['buBalance']*(0.60+rng.random()*0.30)
            a['buBalance'] -= spend
            if p['cip'] and rng.random() < p['cipDemo']*0.15:
                a['quality'] = min(p['maxMult'], a['quality']+0.1)
            # v4.0: octave now governs conversion-rate CAPACITY; quality modulates
            # the realised rate within that ceiling (was: quality/maxMult alone).
            octCeiling = 1 + (a['octave']/max(1, p['maxOct']))*(max(1, p['maxMult'])-1)
            qualityFactor = min(1.0, a['quality']/max(1, p['maxMult']))
            baseRate = 1 + qualityFactor*(octCeiling-1)
            phi = CFG['PHI_RATIO'] if (p['phi'] and a['quality'] > p['maxMult']*CFG['PHI_QUALITY_THRESH']) else 1.0
            ptfB = ptfConvBonus if (p['ptf'] and a['inPTF']) else 1.0
            cipB = (1+p['cipDemo']*0.12) if p['cip'] else 1.0
            rate = min(baseRate*phi*ptfB, p['maxMult']*(CFG['PHI_RATIO'] if p['phi'] else 1.0))
            bTax = p['tax']*(1-p['cipDemo']*0.18) if p['cip'] else p['tax']
            progTax = min(CFG['PROG_TAX_MAX'], bTax + max(0.0, (rate-CFG['PROG_PIVOT'])*CFG['PROG_RATE']))
            convGain = spend*rate*(1-progTax)*cipB*incomeShock
            a['wealth'] += convGain
            if math.isnan(a['wealth']):
                a['wealth'] = 0.0

            # v4.0: FBS-gated octave advancement (was: fixed-probability advRate).
            if a['octave'] < p['maxOct']:
                Yusd = a['wage']*CFG['SIU_TO_USD']
                cBasicMonthly = (dollarCost*cf)/12
                edcResidual = CFG['FBS_EDC_RESIDUAL_PTH'] if (p['pth'] and a['inPTH']) else CFG['FBS_EDC_RESIDUAL_BASE']
                fbs = max(0.0, Yusd + p['bu'] - cBasicMonthly - edcResidual*Yusd)
                lam = a.get('lam', (CFG['FBS_LAMBDA_LO']+CFG['FBS_LAMBDA_HI'])/2)
                if p['cip']:
                    lam *= (1+p['cipDemo']*CFG['FBS_CIP_LAMBDA_BOOST'])
                pAdvance = 1 - math.exp(-lam*fbs)
                if rng.random() < pAdvance:
                    a['octave'] += 1

            if rng.random() < szhPartBoost and not a['inPTF'] and p['ptf']:
                a['inPTF'] = rng.random() < p['ptfShare']

        if p['pth'] and a['inPTH']:
            # v4.0 addition: a share of the annual PTH cost SAVING now routes
            # into Acre Equity (illiquid) instead of landing entirely as
            # liquid relief. Re-routes an already-counted saving; not new
            # wealth. (Was: appreciation-only.)
            cfWithoutPTH = cf/0.65
            pthSaving = max(0.0, simCost*cfWithoutPTH*(1-0.65))
            equityContrib = pthSaving*CFG['PTH_EQUITY_CONTRIB_SHARE']
            a['acreEquity'] += equityContrib
            a['wealth'] -= equityContrib
            ar = 0.030 + rng.random()*0.020 + pthApprBonus
            appr = a['acreEquity']*ar
            a['acreEquity'] += appr
            a['wealth'] += appr*0.5

        if p['ptf'] and not a['inPTF'] and p['ptfShare'] > 0 and yr > 0:
            # v4.0 addition: Bass (1969) imitation term based on current
            # adoption share, alongside the pre-existing distress bump.
            ap = 0.005 + CFG['PTF_BASS_Q']*ptfAdoptFrac
            if bleiCheck < CFG['BLEI_PRECARIOUS_MAX']:
                ap += 0.015
            if rng.random() < ap:
                a['inPTF'] = True

        if a['wealth'] < CFG['WEALTH_FLOOR']:
            a['wealth'] = CFG['WEALTH_FLOOR']

    return total_wage_income


def calc_metrics_v41(agents):
    """CORRECTED convention (this revision — see Run Record #2, finding #4):
    matches index.html's actual calcMetrics(), which does NOT clamp wealth
    to >=0 before computing the median (only the separate Gini/net-wealth
    total does that). Poverty and median both use raw (NaN-guarded but
    otherwise unclamped) wealth, exactly as the real function does."""
    ws = sorted(0.0 if math.isnan(a['wealth']) else a['wealth'] for a in agents)
    n = len(ws)
    pov = sum(1 for w in ws if w < CFG['POVERTY_LINE']) / n
    med = ws[n//2] if n % 2 else (ws[n//2-1]+ws[n//2])/2
    return dict(pov=pov, med=med)


def run_scenario_v41(seed, years, automation_on, n=500, preset='reference'):
    rng = random.Random(seed)
    p = dict(bu=1200, maxOct=6, expiry=1, tax=0.12, maxMult=9, partRate=0.78,
             ptfShare=0.18, pthUptake=0.20, szhCoh=0.72, cipDemo=0.65,
             phi=True, ptf=True, pth=True, szh=True, cip=True, ccoOn=True, inflRate=0.0)
    agents = make_agents_v41(rng, n, p)
    demand_series, pov_series, wealth_series = [], [], []
    for yr in range(years):
        demand = run_year_v41(rng, agents, yr, p, automation_on)
        m = calc_metrics_v41(agents)
        demand_series.append(demand)
        pov_series.append(m['pov']*100)
        wealth_series.append(m['med'])
    return demand_series, pov_series, wealth_series


# ===========================================================================
# CROSS-VALIDATION DRIVER
# ===========================================================================

def cross_validate(seeds=(1, 2, 3, 4, 5, 42, 99, 777), years=25, n=500, target='v41'):
    """Appendix G.4 Step 4-5: run Reference preset with/without automation,
    across multiple seeds, and check against NEEC's C1.4/C1.1 thresholds.
    target='v41' (default) uses the current mechanics; target='v39' re-runs
    the legacy mechanics for direct comparison (both share the same seeds,
    n, years, and preset so the delta is attributable to the mechanism
    changes, not a changed experimental setup)."""
    run_scenario = run_scenario_v41 if target == 'v41' else run_scenario_v39
    print(f"\n=== NEEC C1.4 cross-validation | target={target} | sim constants checked against v{SIM_VERSION_CHECKED} ===")
    print(f"Reference preset, {n} agents, {years} years, seeds={seeds}\n")

    results = {'on': {'pov': [], 'wealth': [], 'demand': []}, 'off': {'pov': [], 'wealth': [], 'demand': []}}
    for seed in seeds:
        for key, automation_on in [('on', True), ('off', False)]:
            d, p, w = run_scenario(seed=seed, years=years, automation_on=automation_on, n=n)
            results[key]['pov'].append(p[-1])
            results[key]['wealth'].append(w[-1])
            results[key]['demand'].append(d[-1])

    for key, label in [('off', 'Automation OFF'), ('on', 'Automation ON')]:
        pov = results[key]['pov']
        wealth = results[key]['wealth']
        print(f"{label} (yr {years}): poverty% per seed = {[round(x,1) for x in pov]}")
        print(f"  mean={statistics.mean(pov):.2f}%  sd={statistics.stdev(pov):.2f}%  "
              f"vs. C1.4 threshold <8% -> {'PASS' if statistics.mean(pov) < 8 else 'FAIL'}  "
              f"vs. C1.1 headline 98% elimination -> {'consistent' if statistics.mean(pov) < 2 else 'NOT consistent'}")
        print(f"  median wealth mean=${statistics.mean(wealth):,.0f}")
    demand_ratio = statistics.mean(results['on']['demand']) / statistics.mean(results['off']['demand']) * 100
    print(f"\nAggregate wage income (demand proxy), automation ON as % of OFF baseline, yr {years}: {demand_ratio:.1f}%  "
          f"vs. C1.4 threshold >85% -> {'PASS' if demand_ratio > 85 else 'FAIL'}")
    print()
    return results


def year_by_year_csv(path, seeds=(1, 2, 3, 4, 5, 42, 99, 777), years=25, n=500, target='v41'):
    """Produces a year-by-year CSV matching the schema of
    neec_c14_crossvalidation_run1_v3.9_results.csv (year, poverty% on/off,
    median wealth on/off, aggregate-demand % of no-automation baseline),
    averaged (mean) across the given seeds for each year. This averaging
    convention is stated explicitly here because the run-1 CSV's own
    generation method wasn't fully reconstructable from the pre-v4.1 script
    alone -- see Run Record #2 for the caveat."""
    run_scenario = run_scenario_v41 if target == 'v41' else run_scenario_v39
    series = {'on': {'pov': [], 'wealth': [], 'demand': []}, 'off': {'pov': [], 'wealth': [], 'demand': []}}
    for seed in seeds:
        for key, automation_on in [('on', True), ('off', False)]:
            d, p, w = run_scenario(seed=seed, years=years, automation_on=automation_on, n=n)
            series[key]['pov'].append(p)
            series[key]['wealth'].append(w)
            series[key]['demand'].append(d)
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['year', 'poverty_pct_automation_on', 'poverty_pct_automation_off',
                          'median_wealth_automation_on', 'median_wealth_automation_off',
                          'aggregate_wage_income_pct_of_no_automation_baseline'])
        for y in range(years):
            pov_on_y = statistics.mean(s[y] for s in series['on']['pov'])
            pov_off_y = statistics.mean(s[y] for s in series['off']['pov'])
            wealth_on_y = statistics.mean(s[y] for s in series['on']['wealth'])
            wealth_off_y = statistics.mean(s[y] for s in series['off']['wealth'])
            demand_on_y = statistics.mean(s[y] for s in series['on']['demand'])
            demand_off_y = statistics.mean(s[y] for s in series['off']['demand'])
            demand_pct = demand_on_y / demand_off_y * 100 if demand_off_y else float('nan')
            writer.writerow([y+1, round(pov_on_y, 2), round(pov_off_y, 2),
                              round(wealth_on_y), round(wealth_off_y), round(demand_pct, 2)])
    print(f"Wrote {path}")


if __name__ == '__main__':
    print("=== Step 3 of protocol: cap-saturation / inert-parameter check (shared by v3.9 and v4.1) ===")
    result = cap_saturation_check(years=25, automation_on=True)
    print(f"\nFirst year cap is hit: {result['first_capped_year']}")
    print(f"Does the acceleration (yr>=AI_Y2) branch ever produce an UNCAPPED value "
          f"(i.e., does AI_DISPLACEMENT_RATE_2 ever matter)? "
          f"{'YES' if result['acceleration_branch_ever_matters'] else 'NO — inert parameter'}")

    print("\n\n########## LEGACY v3.9 MECHANICS (re-run fresh, for direct comparison) ##########")
    cross_validate(target='v39')

    print("\n\n########## CURRENT v4.1 MECHANICS ##########")
    cross_validate(target='v41')

    print("\n\n########## Writing year-by-year CSV (v4.1 mechanics) ##########")
    year_by_year_csv('neec_c14_crossvalidation_run2_v4.1_results.csv', target='v41')
