#!/usr/bin/env python3
"""
Independent re-verification of the Doughnut Economics and Universal Basic
Services score vectors against their own scratch documents' stated totals,
before either is spliced into any canonical file. Per this project's own
methodology.md: "Programmatic verification over visual checking."
"""

ALL_CRITS = ['C1.1','C1.2a','C1.2b','C1.3','C1.4','C1.5'] + \
            [f'C{d}.{i}' for d in range(2, 6) for i in range(1, 6)]
D1_CRITS = ['C1.1','C1.2a','C1.2b','C1.3','C1.4','C1.5']

# Transcribed criterion-by-criterion from NEEC_DoughnutEconomics_scoring_scratch.md's own prose
DOUGHNUT = {
    'C1.1':0.5,'C1.2a':0.0,'C1.2b':0.0,'C1.3':0.5,'C1.4':0.0,'C1.5':0.0,
    'C2.1':0.0,'C2.2':0.0,'C2.3':0.5,'C2.4':0.5,'C2.5':1.0,
    'C3.1':0.5,'C3.2':0.5,'C3.3':0.5,'C3.4':1.0,'C3.5':0.5,
    'C4.1':1.0,'C4.2':1.0,'C4.3':0.5,'C4.4':0.0,'C4.5':0.0,
    'C5.1':0.5,'C5.2':0.5,'C5.3':1.0,'C5.4':0.5,'C5.5':0.5,
}
DOUGHNUT_PUBLISHED = {'D1':1.0,'D2':2.0,'D3':3.0,'D4':2.5,'D5':3.0,'Total':11.5}

# Transcribed from NEEC_UniversalBasicServices_scoring_scratch.md's own prose
# (matches verify_ubs.py's own UBS dict exactly)
UBS = {
    'C1.1':0.5,'C1.2a':0.0,'C1.2b':0.0,'C1.3':0.5,'C1.4':0.5,'C1.5':0.0,
    'C2.1':0.5,'C2.2':0.5,'C2.3':0.5,'C2.4':0.5,'C2.5':1.0,
    'C3.1':0.5,'C3.2':0.5,'C3.3':0.5,'C3.4':1.0,'C3.5':0.5,
    'C4.1':0.5,'C4.2':0.5,'C4.3':0.5,'C4.4':0.5,'C4.5':0.5,
    'C5.1':1.0,'C5.2':0.5,'C5.3':1.0,'C5.4':0.5,'C5.5':0.5,
}
UBS_PUBLISHED = {'D1':1.5,'D2':3.0,'D3':3.0,'D4':2.5,'D5':3.5,'Total':13.5}

def check(name, vec, published):
    assert len(vec) == 26, f"{name}: vector has {len(vec)} criteria, not 26"
    d1 = sum(vec[c] for c in D1_CRITS)
    d2 = sum(vec[f'C2.{i}'] for i in range(1,6))
    d3 = sum(vec[f'C3.{i}'] for i in range(1,6))
    d4 = sum(vec[f'C4.{i}'] for i in range(1,6))
    d5 = sum(vec[f'C5.{i}'] for i in range(1,6))
    total = d1+d2+d3+d4+d5
    fails = sum(1 for c in ALL_CRITS if vec[c]==0.0)
    tier = 'Potentially Adequate' if fails < 3 else ('Partially Adequate' if fails <= 5 else 'Structurally Inadequate')
    print(f"--- {name} ---")
    print(f"  D1={d1}/6  D2={d2}/5  D3={d3}/5  D4={d4}/5  D5={d5}/5   Total={total}/26 ({round(total/26*100)}%)")
    print(f"  vs scratch doc's own stated: D1={published['D1']} D2={published['D2']} D3={published['D3']} "
          f"D4={published['D4']} D5={published['D5']} Total={published['Total']}")
    ok = (abs(d1-published['D1'])<1e-9 and abs(d2-published['D2'])<1e-9 and abs(d3-published['D3'])<1e-9
          and abs(d4-published['D4'])<1e-9 and abs(d5-published['D5'])<1e-9 and abs(total-published['Total'])<1e-9)
    print(f"  Domain/total match: {'PASS' if ok else 'FAIL <<<<<'}")
    print(f"  Failures: {fails} -- {[c for c in ALL_CRITS if vec[c]==0.0]}  -> Tier: {tier}")
    print()
    return ok, total, fails, tier

ok1, *_ = check("Doughnut Economics", DOUGHNUT, DOUGHNUT_PUBLISHED)
ok2, *_ = check("Universal Basic Services", UBS, UBS_PUBLISHED)

if ok1 and ok2:
    print("BOTH VECTORS INDEPENDENTLY RE-VERIFIED CLEAN. Safe to insert.")
else:
    raise SystemExit("MISMATCH FOUND -- do not insert until resolved.")
