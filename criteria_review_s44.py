"""criteria_review_s44.py - evidence tables for NEEC_Criteria_Review_s44.md (Session 44).

Reads criteria.json and neec_corpus.json beside this script; changes nothing. Prints:
  1. the implicit weight of each norm N1-N14 under equal criterion weighting;
  2. every quantity scored in more than one Pass Threshold, with the clauses verbatim;
  3. corpus agreement for those criterion pairs against the all-pairs baseline;
  4. Requirement-line figures that differ from the Pass Threshold (protocol 2.3).
Deterministic; prints file names only.
"""
import itertools
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
crit = json.load(open(os.path.join(HERE, "criteria.json"), encoding="utf-8"))["criteria"]
corpus = json.load(open(os.path.join(HERE, "neec_corpus.json"), encoding="utf-8"))["entries"]
C = {c["id"]: c for c in crit}
IDS = [c["id"] for c in crit]
print("Inputs: criteria.json, neec_corpus.json")
print(f"Criteria: {len(IDS)}; corpus entries: {len(corpus)} (vectors in force, before the rescoring pass is applied)\n")

# 1. Implicit norm weights: each criterion carries 1/26 of the total, split equally among its derivation norms.
names, weight, count = {}, {}, {}
for c in crit:
    found = re.findall(r"N(\d+) \(([^)]+)\)", c["definition"]["derivation"])
    norms = sorted({int(n) for n, _ in found})
    for n, label in found:
        names.setdefault(int(n), label.split(" and ")[0] if int(n) == 7 else label)
    for n in norms:
        weight[n] = weight.get(n, 0) + 1 / len(norms)
        count[n] = count.get(n, 0) + 1
print("1. Implicit norm weights under equal criterion weighting (criterion units; total 26)")
print(f"   {'Norm':<32}{'criteria':>9}{'units':>8}{'share':>8}")
for n in sorted(weight, key=lambda k: (-weight[k], k)):
    print(f"   N{n:<3}{names[n]:<28}{count[n]:>9}{weight[n]:>8.2f}{weight[n] / 26:>8.1%}")
missing = [n for n in range(1, 15) if n not in weight]
print(f"   Norms with no criterion: {missing if missing else 'none'}\n")

# 2. Quantities scored in more than one Pass Threshold (clause text located verbatim).
DUPES = [
    ("Wealth Gini", [("C1.2b", "Gini <0.35 for wealth distribution"), ("C4.4", "Gini <0.35 for wealth")]),
    ("Citizen proposals adopted", [("C2.4", "\u226535% citizen proposals adopted"),
                                   ("C4.4", "\u226540% citizen proposals adopted")]),
    ("Carbon reduction by 2030", [("C4.1", "35% carbon reduction by 2030"),
                                  ("C4.2", "Absolute carbon reductions 35-45% by 2030")]),
    ("Resource use against regeneration", [("C4.1", "resource use \u226490% regeneration"),
                                           ("C4.2", "resource extraction \u2264 regeneration")]),
    ("Share of decisions free of coercion", [("C2.1", "\u226570% report genuine autonomy in major life decisions"),
                                             ("C4.5", "residual coercion <10% of decisions")]),
]
print("2. Quantities scored in more than one Pass Threshold")
for label, uses in DUPES:
    print(f"   {label}:")
    for cid, text in uses:
        ok = text in C[cid]["definition"]["pass_threshold"]
        print(f"     {cid:<6}{'located' if ok else 'NOT LOCATED'}: \"{text}\"")
print()

# 3. Corpus agreement for the pairs above, against all 325 criterion pairs.
def agree(a, b):
    return sum(e["vector"][a] == e["vector"][b] for e in corpus) / len(corpus)

allp = [agree(a, b) for a, b in itertools.combinations(IDS, 2)]
base = sum(allp) / len(allp)
print(f"3. Exact score agreement across the {len(corpus)} entries (all {len(allp)} pairs: mean {base:.1%})")
for a, b in sorted({(u[0][0], u[1][0]) for _, u in DUPES}):
    print(f"   {a} / {b}: {agree(a, b):.1%}")
print()

# 4. Requirement-line figures differing from the Pass Threshold (protocol 2.3 asks these be flagged).
GAPS = [("C1.1", "requirement", "95%+ poverty elimination", "\u226590% poverty reduction"),
        ("C1.2a", "requirement", "$70,000+ median household wealth", "\u2265$60,000 median wealth"),
        ("C1.4", "measurement", "maintain poverty <5%, aggregate demand 90-110% baseline",
         "Poverty <8% and aggregate demand >85% baseline")]
print("4. Requirement or measurement figures that differ from the Pass Threshold")
for cid, field, other, pt in GAPS:
    d = C[cid]["definition"]
    src = json.dumps(d, ensure_ascii=False)
    ok1 = other.replace("-", "\u2013") in src or other in src
    ok2 = pt in d["pass_threshold"]
    print(f"   {cid:<6}{field}: \"{other}\" ({'located' if ok1 else 'NOT LOCATED'}) vs Pass Threshold: "
          f"\"{pt}\" ({'located' if ok2 else 'NOT LOCATED'})")
