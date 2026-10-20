#!/usr/bin/env python3
"""
outside_kit_check.py -- NEEC: the outside review's leak check (Session 80; plan section 3, "Checks before launch")
=================================================================================================================
Builds every prompt the runner would send, with the runner's own functions (outside_review_runner.build_messages
for the 696 blind reader calls, jev_request for the Jev states), and scans what the reader sees. Any hit fails.

  everywhere a reader or Jev looks (instructions, rules, criterion, system, pack):
    tier      a tier name
    record    NEEC, its records, scripts, sessions, ledger or summary blocks
    owner     the author's name or address
    marker    a withheld-text marker (the Ostrom pilot leaked through one: protocol 11.2, R8)
    stageb    any sentence of a stage B argument (those are shown only after the blind reading is pushed)
    record also counts a NEEC session number anywhere but the design's own documents
  in the rules, the criterion and the instructions:
    system    a scored system's name or a distinctive name of its design (they are dropped from the rules and the
              criterion); a system file may name only its own system
  in the source pack:
    verdict   a verdict, a clause status or a flag in NEEC's words, or a score next to a criterion id
  structure: every unit's prompt carries its own criterion and system and nothing else's; no pack file is a cache
    note or index; the stage B files exist only for the eight owner-decided units.

  python3 outside_kit_check.py              scan the kit; print counts, never text
  python3 outside_kit_check.py --negative   plant one leak of each kind in a copy of the kit and show each caught
"""
import json
import os
import re
import shutil
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import outside_review_runner as rr  # noqa: E402
import outside_kit as ok  # noqa: E402

CORPUS = {e["code"]: e["display_name"] for e in
          json.load(open(os.path.join(HERE, "neec_corpus_v2_s79_snapshot.json")))["entries"]}

EVERYWHERE = {
    "tier": re.compile(r"Potentially Adequate|Partially Adequate|Structurally Inadequate"),
    "record": re.compile(r"NEEC|Normative Econ\w* Evaluation|Rescoring|Blind ?Review|OwnerDecisions|FinalApplication|"
                         r"Handoff|STATE\.md|pass_common|rescoring_s\d|blind_s\d|apply_\w+\.py|owner_s\d|"
                         r"close call|summary block|evidence_cache"),
    "owner": re.compile(r"\bDuke\b|Duke\s*Johnson|Duke\.?\s*T\.?\s*James|james@gmail|Johnson\s*(&|and)\s*Claude", re.I),
    "marker": re.compile(r"withheld|\[redacted\]|redacted|blind copy|omitted from this|\[removed\]", re.I),
}
SYSTEM = re.compile("|".join(ok.SYSTEM_WORDS + [re.escape(n) for n in CORPUS.values()]))
VERDICT = re.compile(r"\bverdicts?\b[^.\n]{0,30}\b(0\.0|0\.5|1\.0)\b|\bclause \d+[^.\n]{0,20}\b(cleared|short|"
                     r"not shown)\b|\bflag(ged)? toward\b|\b(scored?|scores|scoring) (at )?(0\.0|0\.5|1\.0)\b|"
                     r"\bC[1-5]\.\d[ab]?\b[^\n.;]{0,40}?\b(0\.0|0\.5|1\.0)\b", re.I)
# NEEC's sessions, in what NEEC wrote or cached (a design's own documents may number their own sessions)
SESSION = re.compile(r"\bSessions? \d")


def stage_b_sentences(kit):
    out = []
    for n in sorted(os.listdir(os.path.join(kit, "stage_b"))):
        t = rr.text(kit, "stage_b/" + n).split("\n", 2)[2]
        out += [s.strip() for s in re.split(r"(?<=[.;])\s+", t) if len(s.strip()) > 40]
    return sorted(set(out))


def scan(kit):
    """{kind: set of places}, and stats."""
    hits = {}

    def hit(kind, where):
        hits.setdefault(kind, set()).add(where)

    units = [json.loads(l) for l in open(os.path.join(kit, "units.jsonl"))]
    sb = stage_b_sentences(kit)
    rules = rr.text(kit, "prompt/protocol.md")
    instr = rr.text(kit, "prompt/instructions.md")
    seen_static = set()
    longest = 0
    for u in units:
        msgs = rr.build_messages(kit, u)
        user = msgs[1]["content"]
        longest = max(longest, len(user) + len(msgs[0]["content"]))
        crit = rr.text(kit, "criteria/%s.md" % u["cid"])
        sysf = rr.text(kit, "systems/%s.md" % u["code"])
        pack = rr.pack_text(kit, u) if u["files"] else ""
        if crit.strip() not in user or sysf.strip() not in user or (pack and pack not in user):
            hit("structure", u["unit"] + " prompt does not carry its own materials")
        for other in set(CORPUS) - {u["code"]}:
            if "# %s\n" % CORPUS[other] in user:
                hit("structure", u["unit"] + " carries another system's file")
        if any(re.match(r"C\d\.\d[ab]?__(sources_s\d+|notes|index)", f) for f in u["files"]):
            hit("structure", u["unit"] + " pack holds a cache note")
        whole = msgs[0]["content"] + "\n" + user
        for kind, rx in EVERYWHERE.items():
            if rx.search(whole):
                hit(kind, u["unit"])
        if any(s in whole for s in sb):
            hit("stageb", u["unit"])
        for name, t in (("instructions", instr), ("rules", rules), ("criteria/" + u["cid"], crit)):
            if name not in seen_static:
                seen_static.add(name)
                if SYSTEM.search(t):
                    hit("system", name)
        if any(CORPUS[o] in sysf for o in CORPUS if o != u["code"]):
            hit("system", "systems/" + u["code"])
        neec_text = "\n".join([msgs[0]["content"], rules, crit, sysf] + [rr.text(kit, "files/%s.txt" % f)
                                                                         for f in u["files"]
                                                                         if not f.startswith("design__")])
        if SESSION.search(neec_text):
            hit("record", u["unit"] + " (session)")
        if pack and VERDICT.search(pack):
            hit("verdict", u["unit"])
        if u["mode"] == "sources" and not u["unit"].endswith("#2"):
            body, cut, k = rr.jev_request(kit, u, crit, "jev-1.13.0", 200000)
            state = json.dumps(body, ensure_ascii=False)
            for kind, rx in EVERYWHERE.items():
                if rx.search(state):
                    hit(kind, "jev " + u["unit"])
            if any(s in state for s in sb):
                hit("stageb", "jev " + u["unit"])
    sbf = sorted(os.listdir(os.path.join(kit, "stage_b")))
    if len(sbf) != 8:
        hit("structure", "stage_b holds %d files, not 8" % len(sbf))
    return hits, {"prompts": len(units), "jev_states": sum(1 for u in units if u["mode"] == "sources"
                                                             and not u["unit"].endswith("#2")),
                  "longest_chars": longest}


KINDS = ["tier", "record", "owner", "marker", "stageb", "system", "verdict", "structure"]


def report(hits):
    for k in KINDS:
        print("  %-9s %d" % (k, len(hits.get(k, ()))))


def negative():
    """Plant one leak of each kind in a copy of the kit; each must be caught, and only where planted."""
    kit = os.path.join(HERE, "outside_kit")
    units = [json.loads(l) for l in open(os.path.join(kit, "units.jsonl"))]
    pu = next(u for u in units if u["code"] == "SQ" and u["files"])
    fid = pu["files"][0]
    design = next(u for u in units if u["code"] == "CCO" and any(f.startswith("design__") for f in u["files"]))
    dfid = next(f for f in design["files"] if f.startswith("design__"))
    sb = stage_b_sentences(kit)[0]
    plants = [
        ("verdict", "files/%s.txt" % fid, "\nVerdict: C2.5 scored 1.0, clause 2 short.\n"),
        ("tier", "criteria/C4.4.md", "\nThis system is Structurally Inadequate.\n"),
        ("record", "prompt/protocol.md", "\nSee NEEC_Rescoring_s65.md, Session 65.\n"),
        ("owner", "files/%s.txt" % dfid, "\nCorresponding Author: Duke Johnson\n"),
        ("stageb", "files/%s.txt" % fid, "\n" + sb + "\n"),
        ("marker", "systems/MS.md", "\n(one example withheld from this blind copy)\n"),
        ("system", "criteria/C2.2.md", "\nParticipatory Economics shows this.\n"),
    ]
    fails = 0
    for kind, rel, add in plants:
        with tempfile.TemporaryDirectory() as d:
            k2 = os.path.join(d, "kit")
            shutil.copytree(kit, k2)
            with open(os.path.join(k2, rel), "a", encoding="utf-8") as f:
                f.write(add)
            hits, _ = scan(k2)
            caught = kind in hits
            others = sorted(k for k in hits if k != kind)
            print("%s  planted %-8s in %-28s caught: %s; other kinds hit: %s" % (
                "PASS" if caught and not others else "FAIL", kind, rel.split("/")[0] + "/...", caught,
                ", ".join(others) or "none"))
            fails += not (caught and not others)
    print("SUMMARY: %d of %d planted leaks caught alone; %d failed" % (len(plants) - fails, len(plants), fails))
    return 1 if fails else 0


def main(argv):
    if argv[:1] == ["--negative"]:
        return negative()
    hits, st = scan(os.path.join(HERE, "outside_kit"))
    print("outside kit: %d blind reader prompts and %d Jev states built by the runner's own functions; longest "
          "prompt %d characters" % (st["prompts"], st["jev_states"], st["longest_chars"]))
    report(hits)
    n = sum(len(v) for v in hits.values())
    print("SUMMARY: %s (%d hits)" % ("PASS, no leak found" if not n else "FAIL", n))
    return 1 if n else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
