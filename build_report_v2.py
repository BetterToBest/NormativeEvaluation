#!/usr/bin/env python3
"""
build_report_v2.py -- NEEC Report v2.0 Part I: the generated scorecards, one domain at a time (Session 84, ledger S41)
===================================================================================================================
Decision 52.8 (W7): Report v2.0 Part I is generated from the per-unit readings carried into the corpus, not retyped. This
script writes the generated parts of NEEC_Report_v2_0_Part_I.md, between its '<!-- generated:NAME -->' and
'<!-- /generated -->' markers; the prose between them (each domain's account of what moved and why) is written by hand
and never touched here.

  standing   the 23 entries on the 29 criteria: total, domain sums, failures, tier, and the change from v1's 26 criteria
  D1 .. D5   per domain, per criterion: the threshold, the count of each score in v1 and in v2.0, then one entry per
             system in the order of the standing: its v2.0 score and v1 score, each clause's status and reading (or, for a
             cell no unit of v2.0 read, the published v1 rationale, quoted), the reason for a 0.0, the close call, and a
             link to the system's evidence report, where every source is given
  counts     per domain: cells read in v2.0, held, moved up, moved down, close calls (the prose cites these)

Everything is read through build_evidence.Ctx (the pass, the blind groups, the owner's decisions, the adjudication and
Session 84's layer, final_pass.settled_state()); every displayed name through display_names.py. Scores change only through
the pass; this script changes none.

Usage: python3 build_report_v2.py           write the generated parts
       python3 build_report_v2.py --check   rebuild them in memory and compare with the file (exit 1 on any difference)
Prints the file name and a summary only. Deterministic.
"""
import io
import os
import re
import sys
from contextlib import redirect_stdout

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_evidence as be  # noqa: E402
import display_names as dn  # noqa: E402
import pass_common as pc  # noqa: E402

DOC = "NEEC_Report_v2_0_Part_I.md"
GEN = re.compile(r"(<!-- generated:(\w+) -->\n)(.*?)(<!-- /generated -->)", re.S)
WORD = {1.0: "pass", 0.5: "partial", 0.0: "structural failure"}


def context():
    with redirect_stdout(io.StringIO()):
        ctx = be.Ctx()
    return ctx


def name(ctx, code):
    return ctx.entries[code]["display_name"]


def standing_order(ctx):
    tot = {c: sum(e["vector"].values()) for c, e in ctx.entries.items()}
    order = list(ctx.entries)
    return sorted(order, key=lambda c: (-tot[c], order.index(c))), tot


def plain(s):
    """A reading as prose: the evidence report's links are not repeated here."""
    return be.esc(s).replace("\n", " ")


def entry(ctx, code, crit, stats):
    v = ctx.entries[code]["vector"][crit]
    pub = ctx.p.vec[code].get(crit)
    unit = ctx.units.get((code, crit))
    c = ctx.cmap[crit]
    link = f"evidence/{be.slug(code)}.md#{be.anchor(crit)}"
    was = "new in v2.0" if pub is None else (f"v1 {be.fmt(pub)}" + ("" if pub == v else f", {'up' if v > pub else 'down'}"))
    out = [f"**{be.esc(name(ctx, code))}: {be.fmt(v)}** ({was}). [Evidence]({link})", ""]
    if pub is not None and v != pub:
        stats["up" if v > pub else "down"] += 1
    if unit is None:
        stats["held"] += 1
        fn, ln, label, text, more = ctx.published_rationale(code, crit)
        out += ["Held at the published score; no unit of v2.0 read it. The v1 rationale:", ""]
        out += ([f"> {be.esc(text)}" + (" *(continues in the scoring document)*" if more else ""), ""] if text
                else [f"*(No rationale paragraph under the v1 heading; {fn}, line {ln}.)*", ""])
    else:
        stats["read"] += 1
        defs = c["definition"]["clauses"]
        rows = []
        for i, (st, txt, _src) in enumerate(unit["clauses"], 1):
            label = be.esc(defs[i - 1]) if len(unit["clauses"]) == len(defs) else f"clause {i}"
            rows.append(f"{i}. *{label}*: {pc.STATUS[st]}. {plain(txt)}")
        out += rows + [""]
        if unit.get("zero"):
            out += [f"Why 0.0 stands: {plain(unit['zero'])}", ""]
        how = ctx.read_in(code, crit) if (code, crit) in ctx.pass_part else None
        if how:
            out += [f"Read in {how}.", ""]
        elif ctx.prev_part.get((code, crit)) == ctx.adj.TAG:
            out += [f"Read in the adjudication of the outside review (Session {ctx.adj.SESSION}){ctx.s84_in(code, crit)}.", ""]
        else:
            out += [f"Read in Session {ctx.s84.SESSION}{ctx.s84_in(code, crit)}.", ""]
    for f in [f for f in ctx.blocks[code]["flags"] if f["criterion"] == crit]:
        stats["flag"] += 1
        rd = f.get("reading") or ""
        rd = "" if rd in ("", "see the pass record") else " " + be.cap(plain(rd))
        out += [f"Close call: a reasonable scorer could set {' or '.join(be.fmt(a) for a in f['alternatives'])}.{rd}", ""]
    return out


def domain(ctx, d, order):
    stats = dict(read=0, held=0, up=0, down=0, flag=0)
    out = []
    for crit in d["criteria"]:
        c = ctx.cmap[crit]
        v2 = [ctx.entries[k]["vector"][crit] for k in order]
        v1 = [ctx.p.vec[k].get(crit) for k in order]
        dist = lambda xs: ", ".join(f"{sum(1 for x in xs if x == s)} at {be.fmt(s)}" for s in (1.0, 0.5, 0.0))
        out += [f"### {crit} {be.esc(c['name'])}", "",
                f"Pass Threshold (v2.0): {be.esc(c['definition']['pass_threshold'])}. Revision class "
                f"{c['revision']['cls']} ({be.CLASS_GLOSS[c['revision']['cls']]}).", "",
                f"v2.0: {dist(v2)}." + (f" v1: {dist(v1)}." if None not in v1 else " New in v2.0."), ""]
        for code in order:
            out += entry(ctx, code, crit, stats)
    return "\n".join(out).rstrip("\n"), stats


def build(ctx):
    order, tot = standing_order(ctx)
    gen = {}
    rows = ["| Rank | Entry | Total of 29 | " + " | ".join(f"D{i + 1}" for i in range(len(ctx.domains)))
            + " | Failures | Tier | v1 (of 26) |", "|---:|---|---:|" + "---:|" * len(ctx.domains) + "---:|---|---:|"]
    rk = pc.ranks(tot)
    for code in order:
        b = ctx.blocks[code]["summary"]
        v1 = sum(ctx.p.vec[code].values())
        rows.append(f"| {rk[code]} | {be.esc(name(ctx, code))} | {be.fmt(tot[code])} | "
                    + " | ".join(be.fmt(b[d["id"]]) for d in ctx.domains)
                    + f" | {b['failures']} | {b['tier']} | {be.fmt(v1)} |")
    gen["standing"] = "\n".join(rows)
    counts = []
    for d in ctx.domains:
        text, st = domain(ctx, d, order)
        gen[d["id"]] = text
        counts.append(f"| {d['id'][1:]}. {be.esc(d['name'])} | {len(d['criteria']) * len(order)} | {st['read']} | {st['held']} | "
                      f"{st['up']} | {st['down']} | {st['flag']} |")
    gen["counts"] = "\n".join(["| Domain | Cells | Read in v2.0 | Held | Up from v1 | Down from v1 | Close calls |",
                               "|---|---:|---:|---:|---:|---:|---:|"] + counts)
    return {k: dn.keep_quotes(v) for k, v in gen.items()}


def main():
    path = os.path.join(HERE, DOC)
    if not os.path.isfile(path):
        sys.exit(f"ERROR: missing {DOC}")
    gen = build(context())
    old = open(path, encoding="utf-8").read()
    names = {m.group(2) for m in GEN.finditer(old)}
    missing = sorted(set(gen) - names)
    new = GEN.sub(lambda m: m.group(1) + gen[m.group(2)] + "\n" + m.group(4) if m.group(2) in gen else m.group(0), old)
    if "--check" in sys.argv[1:]:
        ok = new == old and not missing and names <= set(gen)
        print(f"{DOC}: {len(names)} generated parts ({', '.join(sorted(names))}) "
              + ("equal what the script generates" if ok else "differ from what the script generates")
              + (f"; missing: {', '.join(missing)}" if missing else ""))
        return 0 if ok else 1
    if new != old:
        open(path, "w", encoding="utf-8").write(new)
        print(f"  wrote the generated parts of {DOC}")
    print(f"  {len(names)} generated parts; {len(gen) - len(names & set(gen))} of the script's not in the file")
    return 0


if __name__ == "__main__":
    sys.exit(main())
