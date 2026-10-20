#!/usr/bin/env python3
"""
compare_outside.py -- NEEC outside blind review, run r1: the comparison the pre-registration fixed (Session 82, ledger S64)
==========================================================================================================================
Implements PREREG.md (results repository, neec-outside-review/r1/; copy: NEEC_OutsideReview_Prereg_s80.md) sections 2 to 7 and 9
as written. It reads the run's three result files, the kit's unit list, NEEC's corpus and clause records, and prints every table.
It changes no score and no file; Jev never sets a verdict (section 6). Adjudication is Session 83's.

INPUTS (default outside_review_r1/): results/reader.jsonl[.gz], results/jev.jsonl[.gz], results/stage_b.jsonl[.gz], kit_units.jsonl
  (the kit's units.jsonl, 696 reader calls in order). NEEC: neec_corpus_v2.json, neec_corpus_v2_s78_snapshot.json,
  summary_blocks_v2.json (md5s checked against section 1; a mismatch exits 1), clause records from final_pass.owner_state /
  final_state (the rescoring pass, the seven blind groups and the owner's decisions).

READINGS OF THE RULES WHERE THE PRE-REGISTRATION IS SILENT (each is reported, none changes a registered rule)
  R1  NEEC records the status R (out of reach, decision D28(c): the clause is not credited because the mechanism does not govern
      the quantity). Section 2 maps only C, S, U, M. Clause agreement is therefore reported excluding R clauses (the primary
      figure), and again counting an R clause as agreeing with a reader status of short or not_shown (never cleared).
  R2  "Closed-book units (closed_book true)": reported both ways, by the kit's mode (373 units, what the reader was given) and by
      the reader's own closed_book flag (what the reader says it used).
  R3  Jev's choice is compared pass by pass (pass 1, pass 2), and on the clauses where the two passes agree ("stable").
  R4  Jev has no "moot": a reader or NEEC status of moot is left out of Jev comparisons.
  R5  The reader's "closed-book source" clause: a cleared/short/not_shown clause whose source field names closed-book knowledge.

Usage: python3 compare_outside.py [--dir DIR]   (prints the tables; exit 1 if an input does not match the registered md5)
Prints tables and summaries only. Deterministic (bootstrap: seed 80, 10,000 resamples).
"""
import argparse
import collections
import contextlib
import gzip
import hashlib
import io
import json
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

REGISTERED = {"neec_corpus_v2.json": "4a1a26af0b01b6a561364e37a4a409b1",
              "neec_corpus_v2_s78_snapshot.json": "ab3dbc90",
              "summary_blocks_v2.json": "dfb3d89880d4fbba6b8e6c20389288a8"}
MAP = {"C": "cleared", "S": "short", "U": "not_shown", "M": "moot", "R": "R"}
CHOICES = ("cleared", "short", "not_shown")
BOOT_N, BOOT_SEED = 10000, 80
FAILED = []


def md5(path):
    with open(path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()


def need(cond, text):
    if not cond:
        FAILED.append(text)
        print("  FAIL " + text)
    return cond


def jsonl(base, name):
    for p in (os.path.join(base, "results", name + ".jsonl"), os.path.join(base, "results", name + ".jsonl.gz")):
        if os.path.isfile(p):
            op = gzip.open if p.endswith(".gz") else open
            with op(p, "rt", encoding="utf-8") as f:
                return [json.loads(ln) for ln in f if ln.strip()]
    sys.exit(f"ERROR: missing results/{name}.jsonl[.gz] under {base}")


def pct(a, n):
    return "%5.1f%%" % (100.0 * a / n) if n else "   n/a"


def mean(x):
    return sum(x) / len(x) if x else float("nan")


def tier(failures):
    return "Potentially Adequate" if failures <= 2 else ("Partially Adequate" if failures <= 5 else "Structurally Inadequate")


def ranks(totals):
    order = sorted(totals.values(), reverse=True)
    return {k: 1 + sum(1 for x in order if x > v) for k, v in totals.items()}


def boot_diff(a, b):
    rng = random.Random(BOOT_SEED)
    d = sorted(mean(rng.choices(a, k=len(a))) - mean(rng.choices(b, k=len(b))) for _ in range(BOOT_N))
    return d[int(0.025 * BOOT_N)], d[int(0.975 * BOOT_N) - 1]


# ---------------------------------------------------------------------------------------------------------------------
def load_all(base):
    out = {}
    for n, want in REGISTERED.items():
        got = md5(os.path.join(HERE, n))
        if not need(got.startswith(want), f"{n} md5 {got[:8]} equals the registered {want[:8]} (section 1)"):
            print("exit: an input is not the one the pre-registration names")
            sys.exit(1)
    out["corpus"] = json.load(open(os.path.join(HERE, "neec_corpus_v2.json"), encoding="utf-8"))
    out["snap"] = json.load(open(os.path.join(HERE, "neec_corpus_v2_s78_snapshot.json"), encoding="utf-8"))
    out["units"] = [json.loads(ln) for ln in open(os.path.join(base, "kit_units.jsonl"), encoding="utf-8") if ln.strip()]
    out["reader_raw"] = jsonl(base, "reader")
    out["jev_raw"] = jsonl(base, "jev")
    out["stage_raw"] = jsonl(base, "stage_b")
    return out


def neec_clauses():
    import pass_common as pc
    import final_pass as fp
    with contextlib.redirect_stdout(io.StringIO()):
        p = pc.Pass()
        fin = fp.final_state(p)
        own = fp.owner_state(p)
    def flat(u, nu):
        return {k: [MAP[s] for s, _, _ in v["clauses"]] for k, v in {**u, **nu}.items()}
    return flat(own[0], own[2]), flat(fin[0], fin[2])


def g12_codes(first):
    return [c for c in dict.fromkeys(u["code"] for u in first if u["group"] == 2)]


def vectors(d):
    return {e["code"]: dict(e["vector"]) for e in d["entries"]}


# ---------------------------------------------------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default=os.path.join(HERE, "outside_review_r1"))
    base = ap.parse_args().dir
    A = load_all(base)
    corpus, snap = A["corpus"], A["snap"]
    names = {e["code"]: e["display_name"] for e in corpus["entries"]}
    codes = [e["code"] for e in corpus["entries"]]
    vec = vectors(corpus)
    vec0 = vectors(snap)
    vec0["CCO"]["C3.2"] = 0.5            # section 1: decision 58.1 undone
    cids = list(vec["SQ"])
    own_cl, fin_cl = neec_clauses()
    units = A["units"]
    U = {u["unit"]: u for u in units}
    first = [u for u in units if u["group"] != 2.5]

    print("compare_outside.py: NEEC outside blind review, run r1 (PREREG.md sections 2 to 7 and 9)\n")
    print("0. WHAT WAS READ")
    need(len(units) == 696 and len(first) == 667, "kit: 696 reader calls, 667 first readings, 29 repeats")
    need(len(cids) == 29 and len(codes) == 23, "NEEC: 23 systems on 29 criteria")
    diff = [(c, k) for c in codes for k in cids if vec[c][k] != vec0[c][k]]
    print("  NEEC with the owner's decisions differs from NEEC without in %d cells: %s" % (len(diff), ", ".join("%s %s" % x for x in diff)))
    need(len(diff) == 8, "the eight owner-decided units are exactly the cells where the two NEEC standings differ")
    # reader finals
    rd, bad = {}, []
    for ln in A["reader_raw"]:
        if ln.get("status") != "ok":
            continue
        f = ln.get("final") or {}
        u = U.get(ln["unit"])
        cl = f.get("clauses") or []
        valid = (u is not None and f.get("verdict") in (0.0, 0.5, 1.0) and len(cl) == u["clauses"]
                 and [c.get("n") for c in cl] == list(range(1, u["clauses"] + 1))
                 and all(c.get("status") in CHOICES + ("moot",) for c in cl)
                 and (f["verdict"] == 1.0) == all(c["status"] in ("cleared", "moot") for c in cl)
                 and ((f["verdict"] == 0.0) == bool(f.get("zero_basis"))))
        if valid:
            rd[ln["unit"]] = f
        else:
            bad.append(ln["unit"])
    missing = [u["unit"] for u in units if u["unit"] not in rd]
    served = collections.Counter(ln.get("model_requested") for ln in A["reader_raw"] if ln.get("status") == "ok")
    print("  reader: %d of 696 units answered and valid; missing %d %s; invalid %d; model %s; error lines (no answer, retried): %d"
          % (len(rd), len(missing), missing[:5], len(bad), dict(served), sum(1 for ln in A["reader_raw"] if ln.get("status") != "ok")))
    need(len(rd) == 696 and not missing and not bad, "every reader unit answered with a valid FINAL object (nothing missing, nothing imputed)")
    stage = {ln["unit"]: ln for ln in A["stage_raw"] if ln.get("status") == "ok"}
    need(len(stage) == 8, "stage B: 8 of 8 units answered")
    jev = {}
    for ln in A["jev_raw"]:
        if ln.get("status") == "ok":
            jev[(ln["unit"], ln["pass"])] = ln
    jev_units = sorted({k[0] for k in jev})
    need(len(jev_units) == 294 and all((u, 1) in jev and (u, 2) in jev for u in jev_units),
         "Jev: 294 units answered in both passes")
    win = {u for u in jev_units if jev[(u, 1)].get("deviation") == "D63 windowed" or jev[(u, 2)].get("deviation") == "D63 windowed"}
    need(len(win) == 105, "Jev: 105 units read in windows (D63), 189 whole-pack")

    first_units = [u["unit"] for u in first]
    nv = lambda c, k: vec[c][k]
    nv0 = lambda c, k: vec0[c][k]

    def rows(sel, ref):
        """(unit, reader verdict, NEEC verdict) over the selected first-reading units."""
        return [(u["unit"], rd[u["unit"]]["verdict"], ref(u["code"], u["cid"])) for u in sel if u["unit"] in rd]

    def agree_row(label, r):
        n = len(r)
        a = sum(1 for _, x, y in r if x == y)
        up = [x - y for _, x, y in r if x > y]
        dn = [y - x for _, x, y in r if x < y]
        return "  %-34s %4d  %4d  %s   up %3d (0.5:%3d 1.0:%3d)  down %3d (0.5:%3d 1.0:%3d)" % (
            label[:34], n, a, pct(a, n), len(up), sum(1 for z in up if z == 0.5), sum(1 for z in up if z == 1.0),
            len(dn), sum(1 for z in dn if z == 0.5), sum(1 for z in dn if z == 1.0))

    hdr = "  %-34s %4s  %4s  %6s   %s" % ("", "n", "agree", "rate", "direction of the disagreements (reader relative to NEEC)")

    def tables(title, ref):
        print("\n" + title)
        print(hdr)
        print(agree_row("all answered units", rows(first, ref)))
        print("  by priority group")
        for g in (1, 2, 3, 4):
            print(agree_row("group %d" % g, rows([u for u in first if u["group"] == g], ref)))
        print("  by kit mode / by the reader's own closed_book flag (R2)")
        for m in ("sources", "closed-book"):
            print(agree_row("kit mode: " + m, rows([u for u in first if u["mode"] == m], ref)))
        for flag in (True, False):
            print(agree_row("reader closed_book %s" % flag, [r for r in rows(first, ref) if bool(rd[r[0]].get("closed_book")) == flag]))
        print("  by system")
        for c in codes:
            print(agree_row("%s %s" % (c, names[c]), rows([u for u in first if u["code"] == c], ref)))
        print("  by criterion")
        for k in cids:
            print(agree_row(k, rows([u for u in first if u["cid"] == k], ref)))

    print("\n3. PRIMARY OUTCOME: VERDICT AGREEMENT (the reader's first reading of each of the 667 units against NEEC's published verdict)")
    tables("3a. Against NEEC with the owner's decisions (neec_corpus_v2.json)", nv)
    tables("3b. Against NEEC without the owner's decisions (s78 snapshot, CCO C3.2 at 0.5)", nv0)
    print("\n3c. The eight owner-decided units: the reader's blind verdict beside both NEEC readings")
    print("  %-10s %-8s %-8s %-9s %-9s" % ("unit", "reader", "NEEC", "NEEC w/o", "group"))
    owner_units = ["%s|%s" % x for x in diff]
    for un in owner_units:
        u = U[un]
        print("  %-10s %-8s %-8s %-9s %-9s" % (un, rd[un]["verdict"], nv(u["code"], u["cid"]), nv0(u["code"], u["cid"]), u["group"]))

    print("\n3e. Verdict disagreements in groups 1 and 2 (the top five), for adjudication; reader / NEEC (NEEC without the owner's decisions if different)")
    for c in ["CCO"] + [x for x in g12_codes(first) if x != "CCO"]:
        dis = []
        for u in first:
            if u["code"] == c and u["group"] in (1, 2) and rd[u["unit"]]["verdict"] != nv(u["code"], u["cid"]):
                dis.append("%s %s/%s%s" % (u["cid"], rd[u["unit"]]["verdict"], nv(u["code"], u["cid"]),
                                           "" if nv(u["code"], u["cid"]) == nv0(u["code"], u["cid"]) else " (w/o %s)" % nv0(u["code"], u["cid"])))
        print("  %-4s %2d: %s" % (c, len(dis), "; ".join(dis) or "none"))

    # clause agreement
    print("\n3d. Clause agreement (units whose NEEC record has one status per v2.0 clause; elsewhere 'not recorded')")
    rec = []
    notcomp = []
    for u in first:
        k = (u["code"], u["cid"])
        if k in own_cl:
            if len(own_cl[k]) == u["clauses"]:
                rec.append(u["unit"])
            else:
                notcomp.append(u["unit"])
    print("  units with a NEEC clause record: %d of 667 (%d more have a record with another clause count: %s); not recorded: %d"
          % (len(rec), len(notcomp), ",".join(notcomp[:8]), 667 - len(rec) - len(notcomp)))
    cm = collections.Counter()
    uagree = uR = 0
    nR_units = 0
    for un in rec:
        u = U[un]
        ne = own_cl[(u["code"], u["cid"])]
        re_ = [c["status"] for c in rd[un]["clauses"]]
        for a, b in zip(ne, re_):
            cm[(a, b)] += 1
        hasR = "R" in ne
        nR_units += hasR
        if all(a == b for a, b in zip(ne, re_) if a != "R"):
            uagree += 1
        if all(a == b or (a == "R" and b in ("short", "not_shown")) for a, b in zip(ne, re_)):
            uR += 1
    nc = sum(cm.values())
    ncR = sum(v for (a, b), v in cm.items() if a != "R")
    cag = sum(v for (a, b), v in cm.items() if a == b and a != "R")
    cagR = cag + sum(v for (a, b), v in cm.items() if a == "R" and b in ("short", "not_shown"))
    print("  clauses compared: %d (of which NEEC R, out of reach: %d)" % (nc, nc - ncR))
    print("  clause agreement, R excluded (primary):          %d of %d  %s" % (cag, ncR, pct(cag, ncR)))
    print("  clause agreement, R as short/not_shown (R1):      %d of %d  %s" % (cagR, nc, pct(cagR, nc)))
    print("  units with every clause agreeing, R excluded:     %d of %d  %s" % (uagree, len(rec), pct(uagree, len(rec))))
    print("  units with every clause agreeing, R as above:     %d of %d  %s" % (uR, len(rec), pct(uR, len(rec))))
    print("  NEEC status (rows) by reader status (columns)")
    cols = CHOICES + ("moot",)
    print("  %-10s" % "" + "".join("%11s" % c for c in cols))
    for a in ("cleared", "short", "not_shown", "moot", "R"):
        print("  %-10s" % a + "".join("%11d" % cm[(a, b)] for b in cols))
    print("  clause agreement by priority group (R excluded)")
    for g in (1, 2, 3, 4):
        z = [(a, b) for un in rec if U[un]["group"] == g for a, b in zip(own_cl[(U[un]["code"], U[un]["cid"])], [c["status"] for c in rd[un]["clauses"]]) if a != "R"]
        print("    group %d  %4d of %4d  %s" % (g, sum(1 for a, b in z if a == b), len(z), pct(sum(1 for a, b in z if a == b), len(z))))

    # 4 lean
    print("\n4. THE READER'S LEAN: mean(reader verdict - NEEC verdict) over answered units; difference from the calibration set, 95% bootstrap")
    print("   interval (10,000 resamples of units within each set, seed 80). A difference whose interval excludes 0 is a finding for Session 83.")
    d1 = {u["unit"]: rd[u["unit"]]["verdict"] - nv(u["code"], u["cid"]) for u in first}
    d0 = {u["unit"]: rd[u["unit"]]["verdict"] - nv0(u["code"], u["cid"]) for u in first}
    cal = [u["unit"] for u in first if u["group"] == 4]
    need(len(cal) == 387, "calibration set = the 387 group 4 units")
    top5 = sorted(codes, key=lambda c: -sum(vec[c].values()))[:5]
    g12 = sorted({u["code"] for u in first if u["group"] in (1, 2)}, key=lambda c: codes.index(c))
    need(sorted(top5) == sorted(g12), "the top five by total (%s) are the systems of groups 1 and 2 (%s)" % (",".join(top5), ",".join(g12)))
    print("  calibration lean (group 4, 387 units): %+.3f against NEEC with the owner's decisions (identical without: none of the eight is in group 4: %s)"
          % (mean([d1[u] for u in cal]), all(d1[u] == d0[u] for u in cal)))
    print("  %-52s %4s  %8s  %8s  %-20s %s" % ("set", "n", "lean", "diff", "95% interval", "excludes 0"))
    sets = [("CCO-PTF-CIP-SZH (group 1, 29 units)", [u["unit"] for u in first if u["group"] == 1])]
    for c in g12:
        if c != "CCO":
            sets.append(("%s (29 units)" % names[c], [u["unit"] for u in first if u["code"] == c and u["group"] == 2]))
    sets.append(("the eight owner-decided units", owner_units))
    for lab, s in sets:
        for tag, dd in (("", d1), (" [without owner]", d0)):
            if tag and "owner-decided" not in lab and "CCO" not in lab:
                continue
            lo, hi = boot_diff([dd[x] for x in s], [dd[x] for x in cal])
            df = mean([dd[x] for x in s]) - mean([dd[x] for x in cal])
            print("  %-52s %4d  %+8.3f  %+8.3f  [%+.3f, %+.3f]  %s" % ((lab + tag)[:52], len(s), mean([dd[x] for x in s]), df, lo, hi,
                                                                    "YES" if lo > 0 or hi < 0 else "no"))

    # 5 consistency
    print("\n5. THE READER'S OWN CONSISTENCY: CCO-PTF-CIP-SZH's 29 units read twice (the repeat is '#2'; only the first reading enters 3, 4 and 7)")
    pairs = [(u["unit"], u["unit"] + "#2") for u in first if u["group"] == 1]
    va = sum(1 for a, b in pairs if rd[a]["verdict"] == rd[b]["verdict"])
    cl_n = cl_a = cl_u = 0
    for a, b in pairs:
        sa = [c["status"] for c in rd[a]["clauses"]]
        sb = [c["status"] for c in rd[b]["clauses"]]
        cl_n += len(sa)
        cl_a += sum(1 for x, y in zip(sa, sb) if x == y)
        cl_u += sa == sb
    print("  verdict agreement between the two readings: %d of 29  %s" % (va, pct(va, 29)))
    print("  clause-status agreement: %d of %d clauses  %s; units with every clause equal: %d of 29" % (cl_a, cl_n, pct(cl_a, cl_n), cl_u))
    print("  units whose verdict differs: " + (", ".join("%s %s->%s" % (a, rd[a]["verdict"], rd[b]["verdict"]) for a, b in pairs if rd[a]["verdict"] != rd[b]["verdict"]) or "none"))

    # 6 Jev
    print("\n6. JEV (jev-1.13.0): per clause, two passes; pass-to-pass agreement; agreement with the reader's status and with NEEC's")
    print("   Reported apart: the 189 whole-pack units and the 105 units read in windows (D63; windows lean toward not_shown). Jev sets no verdict.")
    jc = {}
    probmis = 0
    for un in jev_units:
        for ps in (1, 2):
            for key, a in jev[(un, ps)]["answers"].items():
                n = int(key.replace("clause", ""))
                jc[(un, ps, n)] = a
                if un not in win:
                    pr = a["probabilities"]
                    if pr[a["choice"]] < max(pr.values()):     # a tie at the printed precision keeps Jev's own choice
                        probmis += 1
    need(probmis == 0, "whole-pack Jev choice is an option held with the highest probability (%d mismatches)" % probmis)
    need(all(a["choice"] in CHOICES for a in jc.values()), "Jev's choices are cleared, short or not_shown")

    def jev_table(label, us):
        us = [u for u in us if u in rd]
        pos = [(u, n) for u in us for n in range(1, U[u]["clauses"] + 1) if (u, 1, n) in jc and (u, 2, n) in jc]
        N = len(pos)
        stable = [(u, n) for u, n in pos if jc[(u, 1, n)]["choice"] == jc[(u, 2, n)]["choice"]]
        print("\n  %s: %d units, %d clauses" % (label, len(us), N))
        print("    Jev's choice, pass 1:  " + "  ".join("%s %d" % (c, sum(1 for u, n in pos if jc[(u, 1, n)]["choice"] == c)) for c in CHOICES)
              + "     pass 2:  " + "  ".join("%s %d" % (c, sum(1 for u, n in pos if jc[(u, 2, n)]["choice"] == c)) for c in CHOICES))
        print("    the two passes agree on %d of %d clauses  %s" % (len(stable), N, pct(len(stable), N)))
        conf = sum(1 for u, n in pos for ps in (1, 2) if jc[(u, ps, n)].get("conflict"))
        if conf:
            print("    clauses with a recorded window conflict (clause-passes): %d" % conf)
        # vs reader
        rdst = lambda u, n: rd[u]["clauses"][n - 1]["status"]
        for ps in (1, 2, "stable"):
            use = stable if ps == "stable" else pos
            pp = 1 if ps == "stable" else ps
            z = [(u, n) for u, n in use if rdst(u, n) != "moot"]
            a = sum(1 for u, n in z if jc[(u, pp, n)]["choice"] == rdst(u, n))
            print("    Jev (%s) with the reader's status:  %d of %d  %s" % (ps if ps == "stable" else "pass %s" % ps, a, len(z), pct(a, len(z))))
        # vs NEEC
        for ps in (1, 2, "stable"):
            use = stable if ps == "stable" else pos
            pp = 1 if ps == "stable" else ps
            z = [(u, n) for u, n in use if (U[u]["code"], U[u]["cid"]) in own_cl and len(own_cl[(U[u]["code"], U[u]["cid"])]) == U[u]["clauses"]
                 and own_cl[(U[u]["code"], U[u]["cid"])][n - 1] not in ("R", "moot")]
            a = sum(1 for u, n in z if jc[(u, pp, n)]["choice"] == own_cl[(U[u]["code"], U[u]["cid"])][n - 1])
            print("    Jev (%s) with NEEC's status (where recorded, R and moot out):  %d of %d  %s"
                  % (ps if ps == "stable" else "pass %s" % ps, a, len(z), pct(a, len(z))))
        # three way on stable clauses with all three recorded
        z = [(u, n) for u, n in stable if (U[u]["code"], U[u]["cid"]) in own_cl and len(own_cl[(U[u]["code"], U[u]["cid"])]) == U[u]["clauses"]
             and own_cl[(U[u]["code"], U[u]["cid"])][n - 1] not in ("R", "moot") and rdst(u, n) != "moot"]
        pat = collections.Counter()
        listing = []
        for u, n in z:
            j = jc[(u, 1, n)]["choice"]
            r_ = rdst(u, n)
            ne = own_cl[(U[u]["code"], U[u]["cid"])][n - 1]
            if j == r_ == ne:
                p_ = "all three agree"
            elif j == r_:
                p_ = "reader = Jev, against NEEC"
                listing.append((u, n, ne, r_, j))
            elif j == ne:
                p_ = "Jev = NEEC, against the reader"
            elif r_ == ne:
                p_ = "reader = NEEC, against Jev"
            else:
                p_ = "all three differ"
            pat[p_] += 1
        print("    reader / Jev / NEEC on %d stable clauses with all three recorded:" % len(z))
        for p_ in ("all three agree", "reader = Jev, against NEEC", "Jev = NEEC, against the reader", "reader = NEEC, against Jev", "all three differ"):
            print("      %-34s %4d  %s" % (p_, pat[p_], pct(pat[p_], len(z))))
        # closed-book cleared
        cbc = [(u, n) for u, n in pos if rdst(u, n) == "cleared" and "closed-book" in rd[u]["clauses"][n - 1].get("source", "").lower()]
        oth = [(u, n) for u, n in pos if rdst(u, n) == "cleared" and (u, n) not in cbc]
        for lab, s in (("reader cleared on a closed-book source (expected to meet not_shown)", cbc), ("reader cleared on the pack (R5)", oth)):
            c_ = collections.Counter(jc[(u, 1, n)]["choice"] for u, n in s)
            print("      %-62s %3d clauses; Jev pass 1: cleared %d, short %d, not_shown %d" % (lab, len(s), c_["cleared"], c_["short"], c_["not_shown"]))
        ns = sum(1 for u, n in pos if jc[(u, 1, n)]["choice"] == "not_shown")
        print("      Jev pass 1 not_shown share: %d of %d  %s" % (ns, N, pct(ns, N)))
        return listing

    whole = [u for u in jev_units if u not in win]
    lw = jev_table("6a. Whole-pack units (189)", whole)
    lx = jev_table("6b. Units read in windows, D63 (105)", sorted(win))
    print("\n  6c. Clauses with a recorded window conflict (D63): unit, pass, clause, choice taken, per-window not listed (kept in jev.jsonl)")
    cf = [(u, ps, n, a["choice"], a["probabilities"]) for (u, ps, n), a in sorted(jc.items()) if a.get("conflict")]
    for u, ps, n, ch, pr in cf:
        print("    %-12s pass %d clause %d  %s" % (u, ps, n, ch))
    print("    total: %d clause-passes in %d units" % (len(cf), len({x[0] for x in cf})))
    print("\n  6d. Clauses where Jev (stable) and the reader agree against NEEC: read first in adjudication (section 6)")
    for lab, ls in (("whole-pack", lw), ("windowed", lx)):
        print("    %s: %d clauses" % (lab, len(ls)))
        for u, n, ne, r_, j in ls:
            print("      %-12s clause %d  NEEC %-9s reader and Jev %s" % (u, n, ne, r_))

    # 7 standing
    print("\n7. THE STANDING, THREE WAYS (totals over 29 criteria; failures = 0.0 verdicts; tier: <=2 Potentially, <=5 Partially Adequate)")
    reader_v = {c: {k: (rd[c + "|" + k]["verdict"] if c + "|" + k in rd else vec[c][k]) for k in cids} for c in codes}
    nmiss = {c: sum(1 for k in cids if c + "|" + k not in rd) for c in codes}
    ok_all = [k for k in cids if all(c + "|" + k in rd for c in codes)]

    def stand(title, v, ks):
        tot = {c: sum(v[c][k] for k in ks) for c in codes}
        fl = {c: sum(1 for k in ks if v[c][k] == 0.0) for c in codes}
        rk = ranks(tot)
        print("\n  " + title)
        print("    %-4s %-40s %6s %5s %-22s" % ("rank", "system", "total", "fail", "tier"))
        for c in sorted(codes, key=lambda c: (rk[c], codes.index(c))):
            print("    %-4d %-40s %6.1f %5d %-22s" % (rk[c], names[c][:40], tot[c], fl[c], tier(fl[c])))
        return tot, fl, rk
    t1 = stand("7.1 NEEC's scores (Session 79 standing)", vec, cids)
    t2 = stand("7.2 NEEC's scores without the owner's decisions", vec0, cids)
    t3 = stand("7.3a The reader's verdicts on the units it answered, NEEC's on the missing (missing per system: %s)"
               % (", ".join("%s %d" % (c, n) for c, n in nmiss.items() if n) or "none"), reader_v, cids)
    t4 = stand("7.3b Totals over the %d criteria every system has answered: the reader" % len(ok_all), reader_v, ok_all)
    t5 = stand("7.3c The same criteria: NEEC" , vec, ok_all)
    first_of = lambda t: sorted(c for c in codes if t[2][c] == 1)
    for lab, t in (("NEEC", t1), ("NEEC without the owner's decisions", t2), ("reader (7.3a)", t3), ("reader, common criteria (7.3b)", t4)):
        print("  first place, %s: %s" % (lab, ", ".join(first_of(t))))
    chg = [c for c in codes if tier(t3[1][c]) != tier(t1[1][c])]
    print("  tier changes, reader against NEEC (7.3a vs 7.1): " + (", ".join("%s %s -> %s" % (c, tier(t1[1][c]), tier(t3[1][c])) for c in chg) or "none"))
    print("  rank changes, reader against NEEC: " + (", ".join("%s %d -> %d" % (c, t1[2][c], t3[2][c]) for c in codes if t1[2][c] != t3[2][c]) or "none"))
    need(abs(t1[0]["CCO"] - 17.5) < 1e-9 and abs(t1[0]["PE"] - 17.0) < 1e-9, "NEEC standing reproduces the ledger: CCO 17.5 first, PE 17.0")

    # 9 stage B
    print("\n9. STAGE B (not blind): the argument for the owner's reading shown to the reader, for the eight owner-decided units; never in 3 to 7")
    print("  %-10s %-8s %-8s %-8s %-9s  %s" % ("unit", "blind", "stage B", "NEEC", "NEEC w/o", "clause statuses blind -> stage B"))
    for un in owner_units:
        sb = stage[un]
        u = U[un]
        bl = [c["status"] for c in rd[un]["clauses"]]
        af = [c["status"] for c in sb["final"]["clauses"]]
        need(sb.get("blind_verdict") == rd[un]["verdict"], "%s: stage B's recorded blind verdict equals the reader's blind verdict" % un)
        print("  %-10s %-8s %-8s %-8s %-9s  %s -> %s" % (un, rd[un]["verdict"], sb["final"]["verdict"], nv(u["code"], u["cid"]), nv0(u["code"], u["cid"]),
                                                      ",".join(bl), ",".join(af)))
    chg = [un for un in owner_units if stage[un]["final"]["verdict"] != rd[un]["verdict"]]
    print("  stage B changed the reader's verdict on %d of 8: %s" % (len(chg), ", ".join(chg) or "none"))

    print("\nSUMMARY: reader %d/696 valid, Jev %d units (%d whole-pack, %d windowed), stage B %d/8; verdict agreement %d of 667 (%s); calibration lean %+.3f; "
          "%d check failures" % (len(rd), len(jev_units), len(whole), len(win), len(stage),
                                  sum(1 for u in first if rd[u["unit"]]["verdict"] == nv(u["code"], u["cid"])),
                                  pct(sum(1 for u in first if rd[u["unit"]]["verdict"] == nv(u["code"], u["cid"])), 667),
                                  mean([d1[u] for u in cal]), len(FAILED)))
    return 1 if FAILED else 0


if __name__ == "__main__":
    sys.exit(main())
