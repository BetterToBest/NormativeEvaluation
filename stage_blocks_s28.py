#!/usr/bin/env python3
"""
stage_blocks_s28.py -- NEEC Session 28: decisions D17 and D18(a) applied to the staged summary blocks
====================================================================================================
Session 27 generated the 23 summary blocks (build_summary_blocks.py) and
staged them in summary_blocks_s27.json. In Session 28 the project owner took
decisions D16 to D19. Two of them change a block:

  D17  The fifteen entries that declare no scope class take the classes the
       owner assigned (SCORING_PROTOCOL.md, section 3.1). Their scope.basis
       changes from "proposed" to "assigned", and scope.source cites the
       protocol line that assigns the class.
  D18(a)  Singapore's C1.5 flag ("citizen-and-PR-only population scope") is
       also inside its citizens-and-PRs scenario. It leaves the flag register
       and stays in the scenario; the default joint readings (the extremes of
       the register, D16(ii)) are recomputed from the remaining flags.

D16 needs no change here: the staged blocks were already encoded under it.
D18(b) (Ostrom) is deferred to the pilot replication; D19 concerns
criteria.json. Nothing else in any block changes, and this is asserted: every
block is compared field by field with its Session 27 version, and only the
fields listed above may differ.

Inputs, found beside this script or in the working directory:
  summary_blocks_s27.json   pinned by MD5 (the Session 27 staging)
  SCORING_PROTOCOL.md       the three class lines of section 3.1 are parsed and
                            asserted, not pinned: a later rewording of those
                            lines makes this script fail, as it should
  neec_entry.py             validates every block and supplies the enumeration
  the canonical script and neec_scores.csv (loaded by neec_entry.py)
Output: summary_blocks_s28.json, in the layout of the Session 27 file.

Usage:  python3 stage_blocks_s28.py
Exit status 0 only if every assertion holds and all 23 blocks validate.
Prints file names only; deterministic.
"""
import contextlib
import hashlib
import importlib.util
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
S27 = "summary_blocks_s27.json"
S27_MD5 = "3c30499b"
OUT = "summary_blocks_s28.json"
PROTOCOL = "SCORING_PROTOCOL.md"
CLASS_OF_LINE = {"Configured national economy": "configured_national_economy",
                 "Mechanism": "mechanism", "Comprehensive system": "comprehensive_system"}
D18A = {"code": "SG", "criterion": "C1.5", "reading": "citizen-and-PR-only population scope"}


def locate(name):
    for d in (HERE, os.getcwd()):
        p = os.path.join(d, name)
        if os.path.isfile(p):
            return p
    sys.exit(f"ERROR: cannot find {name}")


def fail(msg):
    print(f"FAIL: {msg}")
    sys.exit(1)


spec = importlib.util.spec_from_file_location("neec_entry", locate("neec_entry.py"))
NE = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(NE)

raw = open(locate(S27), "rb").read()
if hashlib.md5(raw).hexdigest()[:8] != S27_MD5:
    fail(f"{S27} is not the Session 27 staging (md5 {hashlib.md5(raw).hexdigest()[:8]}, expected {S27_MD5})")
before = json.loads(raw.decode("utf-8"))
blocks = json.loads(raw.decode("utf-8"))
by_code = {b["code"]: b for b in blocks}
print("stage_blocks_s28.py -- decisions D17 and D18(a) applied to the staged summary blocks")
print(f"input: {S27} (md5 {S27_MD5}, {len(blocks)} blocks); canonical corpus: {len(NE.SCORES)} systems")

# ------------------------------------------------------------------ D17
text = open(locate(PROTOCOL), encoding="utf-8").read()
m = re.search(r"^### 3\.1 .*?(?=^### 3\.2 )", text, re.S | re.M)
if not m:
    fail("section 3.1 not found in the protocol")
lines = [l[2:] for l in m.group(0).split("\n") if l.startswith("- ") and l[2:].split(":")[0] in CLASS_OF_LINE]
if len(lines) != 3:
    fail(f"expected three class lines in protocol 3.1, found {len(lines)}")
assigned = {}
for line in lines:
    label, names = line.split(": ", 1)
    if not names.endswith("."):
        fail(f"class line does not end with a full stop: {line!r}")
    for name in names[:-1].split(", "):
        if name in assigned:
            fail(f"{name} is assigned twice")
        assigned[name] = (CLASS_OF_LINE[label], line)
proposed = {b["key"] for b in blocks if b["scope"]["basis"] == "proposed"}
if set(assigned) != proposed:
    fail(f"protocol 3.1 names {sorted(set(assigned) ^ proposed)} differently from the proposed blocks")
print(f"\nD17  protocol 3.1 assigns {len(assigned)} classes; they are exactly the {len(proposed)} blocks staged as 'proposed'")
for b in blocks:
    if b["key"] not in assigned:
        continue
    cls, line = assigned[b["key"]]
    if b["scope"]["class"] != cls:
        fail(f"{b['key']}: staged class {b['scope']['class']} differs from the assigned {cls}")
    b["scope"] = {"class": cls, "basis": "assigned",
                  "source": {"file": PROTOCOL, "locator": "3.1", "phrase": line}}
    print(f"  [{b['code']:4s}] {cls:28s} proposed -> assigned")

# ------------------------------------------------------------------ D18(a)
sg = by_code[D18A["code"]]
old_flags = sg["flags"]
out = [f for f in old_flags if f["criterion"] == D18A["criterion"]]
if len(out) != 1 or out[0]["reading"] != D18A["reading"] or out[0].get("tracks"):
    fail("Singapore's C1.5 flag is not the registered population-scope flag")
if any(f.get("tracks") == D18A["criterion"] for f in old_flags):
    fail("another flag tracks Singapore's C1.5")
scope_scen = [x for x in sg["scenarios"] if x["kind"] == "scope"]
if len(scope_scen) != 1 or scope_scen[0]["changes"].get(D18A["criterion"]) not in out[0]["alternatives"]:
    fail("Singapore's scope scenario does not carry the flag's alternative for C1.5")
e_before = NE.enumerate_register(sg)
d_before = NE.d13(sg)
sg["flags"] = [f for f in old_flags if f["criterion"] != D18A["criterion"]]
v = sg["vector"]
up, down = NE.extremes(sg)
new_readings = []
for r in sg["joint_readings"]:
    if r["basis"] == "extremes":
        ch = up if r["id"] == "up" else down
        r = dict(r, resolve={c: ch[c] for c in NE.CRITS if c in ch}, result=NE.result(NE.applied(v, ch)))
    new_readings.append(r)
if [r["basis"] for r in new_readings] != ["scored", "extremes", "extremes"]:
    fail("Singapore's joint readings are not the scored reading and the two extremes")
sg["joint_readings"] = new_readings
e_after = NE.enumerate_register(sg)
d_after = NE.d13(sg)


def enum_line(e):
    tiers = "; ".join(f"{NE.TIER_ABBR[t]} {n}" for t, n in e["by_tier"].items())
    return (f"{e['combinations']:,} combinations; {tiers}; keep scored tier {100 * e['keep_share']:.1f}%")


def d13_line(d):
    return (f"reach {'/'.join(NE.TIER_ABBR[t] for t in d['reach'])}; "
            f"span {NE.fmt(d['span_points'])} points / {d['span_failures']} failures")


print(f"\nD18(a)  [SG] {sg['key']}: C1.5 leaves the flag register (reading: {D18A['reading']});")
print(f"        it stays in the scope scenario '{scope_scen[0]['id']}' (C1.5 -> {NE.fmt(scope_scen[0]['changes']['C1.5'])})")
print(f"  flags:        {len(old_flags)} -> {len(sg['flags'])}")
print(f"  enumeration:  {enum_line(e_before)}")
print(f"            ->  {enum_line(e_after)}")
for r0, r1 in zip(before[[b['code'] for b in before].index('SG')]["joint_readings"], sg["joint_readings"]):
    if r0 != r1:
        a, b = r0["result"], r1["result"]
        print(f"  reading {r1['id']:5s}  {NE.fmt(a['total'])}/26 {a['failures']} failures -> "
              f"{NE.fmt(b['total'])}/26 {b['failures']} failures ({b['tier']})")
print(f"  D13:          {d13_line(d_before)}")
print(f"            ->  {d13_line(d_after)}")
assert e_after["keep_share"] == e_before["keep_share"], "D18(a) changed the enumeration share"
assert d_after["reach"] == d_before["reach"], "D18(a) changed the reach"

# ------------------------------------------------------------------ nothing else changed; every block valid
expected = {b["code"]: ({"scope"} if b["key"] in assigned else set()) for b in blocks}
expected["SG"] = {"flags", "joint_readings"}
for b0, b1 in zip(before, blocks):
    changed = {k for k in b1 if b0.get(k) != b1.get(k)} | {k for k in b0 if k not in b1}
    if changed != expected[b1["code"]]:
        fail(f"[{b1['code']}] changed fields {sorted(changed)}, expected {sorted(expected[b1['code']])}")
errors = {b["code"]: NE.validate(b) for b in blocks}
bad = {k: e for k, e in errors.items() if e}
if bad:
    fail(f"blocks failing validation: {bad}")
n_changed = sum(1 for c in expected if expected[c])
print(f"\nChanged blocks: {n_changed} (D17 {len(assigned)}, D18(a) 1); unchanged: {len(blocks) - n_changed}. "
      f"All {len(blocks)} blocks validate.")
body = "[\n" + ",\n".join("  " + NE.dump_block(b).replace("\n", "\n  ") for b in blocks) + "\n]\n"
if json.loads(body) != blocks:
    fail("the written layout does not round-trip")
with open(os.path.join(os.getcwd(), OUT), "w", encoding="utf-8") as fh:
    fh.write(body)
print(f"wrote {OUT}  md5 {hashlib.md5(body.encode('utf-8')).hexdigest()}")
