#!/usr/bin/env python3
"""
build_evidence.py -- NEEC per-system evidence reports (Session 68, decision 68.1)
=================================================================================
The site's Evidence section for a system used to link only to the long scoring documents (Report v1.6, 285 KB, for thirteen
entries; a 48-72 KB scoring document for each of the other ten), so a reader had to find the section for one criterion by
hand. This script writes one short report per system, evidence/<code>.md, and an index, evidence/index.md. Each report has one
section per criterion (29 per system) that gives:

  * the v2.0 score, and the published (v1) score where the pass changed it;
  * for a unit the rescoring pass read (496 of the 667 cells, including the 69 units of the three new criteria): one row per
    clause of the criterion's v2.0 Pass Threshold, with its status (cleared, short, not shown, out of reach, moot), the
    reading and its source, each data file in evidence_cache/ linked;
  * the close call registered for the unit (summary_blocks_v2.json), the pass's note, and the reason for a 0.0;
  * direct links, to the line, to the published rationale in the long scoring document and to the unit's section of the
    rescoring record that read it.

Nothing in a report is typed by hand or newly judged. Every score, clause reading, source, flag and note is read from the
files the pass already holds (criteria.json, neec_corpus_v2.json, summary_blocks_v2.json, neec_scores_v2.csv, the pass's
parts through pass_common.py). A cell no part of the pass read says so and links to its published rationale. Scores change
only through the pass; this script changes none.

Usage: python3 build_evidence.py           write evidence/ (the index and 23 reports)
       python3 build_evidence.py --check   rebuild in memory and compare with evidence/ on disk (exit 1 on any difference);
                                           also checks the report's scores against the corpus, every unit's verdict against
                                           the corpus, the totals against the blocks, and that every link target exists
Prints file names and summaries only. Deterministic.
"""
import csv
import io
import json
import os
import re
import sys
from contextlib import redirect_stdout
from urllib.parse import quote

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import pass_common as pc  # noqa: E402

OUTDIR = "evidence"
WORD = {1.0: "pass", 0.5: "partial", 0.0: "structural failure"}
CLASS_GLOSS = {"W": "wording, commentary or disclosure only", "D": "clauses deleted only",
               "I": "indicator named for an unchanged clause and bar", "M": "bar, measure or clause restated",
               "N": "new criterion", "U": "unchanged"}


def jload(name):
    with open(os.path.join(HERE, name), encoding="utf-8") as f:
        return json.load(f)


def fmt(x):
    return f"{x:.1f}"


def slug(code):
    return code.lower()


def anchor(cid):
    return cid.lower().replace(".", "-")


def part_label(tag):
    return ("group " + tag.strip("()")) if re.fullmatch(r"\(2\.\d+\)", tag) else ("decision " + tag if tag in ("48.3", "58.1") else "part " + tag)


class Ctx:
    """Everything the reports read, loaded once."""

    def __init__(self):
        with redirect_stdout(io.StringIO()):
            self.p = pc.Pass()
        self.last = self.p.mods[-1]
        self.crit = jload("criteria.json")
        self.cfg = jload(os.path.join("site", "config.json"))
        self.corpus = jload("neec_corpus_v2.json")
        self.blocks = {b["code"]: b for b in jload("summary_blocks_v2.json")}
        self.repo = self.cfg["site"]["repo"]
        self.base = self.cfg["site"]["base_url"]
        self.cmap = {c["id"]: c for c in self.crit["criteria"]}
        self.domains = self.crit["domains"]
        self.order = [c for d in self.domains for c in d["criteria"]]
        self.entries = {e["code"]: e for e in self.corpus["entries"]}
        with open(os.path.join(HERE, "neec_scores_v2.csv"), encoding="utf-8", newline="") as f:
            self.csv = {r["system"]: r for r in csv.DictReader(f)}
        # every unit of the pass, with the part that read it last
        self.units = dict(self.p.merged)
        self.part = dict(self.p.part_of)
        for k in self.last.NEW_UNITS:
            self.units[k] = self.last.NEW_UNITS[k]
            self.part[k] = self.last.TAG
        self.parts = {tag: (mod, path, sess) for (tag, mod, path, sess), m in zip(pc.PARTS, self.p.mods)}
        self.mod_of = dict(zip([t for t, _, _, _ in pc.PARTS], self.p.mods))
        self.sess = {t: s for t, _, _, s in pc.PARTS}
        # evidence_cache files: (directory, name) and the names that are unique across directories
        self.cache = {}
        for r, _, fs in os.walk(os.path.join(HERE, "evidence_cache")):
            for fn in fs:
                self.cache[(os.path.basename(r), fn)] = True
        names = {}
        for (d, fn) in self.cache:
            names.setdefault(fn, []).append(d)
        self.cache_name = {fn: ds[0] for fn, ds in names.items() if len(ds) == 1}
        self.rec_heads = {}
        self.docs = {}
        self.dangling = []
        self.links = 0

    def blob(self, path, line=None):
        u = f"{self.repo}/blob/main/{quote(path)}"
        return u + (f"?plain=1#L{line}" if line else "")

    def record_line(self, rec, code, crit):
        """Line of the heading '#### <code> <crit> ...' in a rescoring record (the first), or None."""
        if rec not in self.rec_heads:
            heads = {}
            with open(os.path.join(HERE, rec), encoding="utf-8") as f:
                for i, line in enumerate(f, 1):
                    m = re.match(r"^#+ \**([A-Z]+) (C\d\.\d[a-z]?)\b", line)
                    if m and (m.group(1), m.group(2)) not in heads:
                        heads[(m.group(1), m.group(2))] = i
            self.rec_heads[rec] = heads
        return self.rec_heads[rec].get((code, crit))

    def rationale(self, code, crit):
        """(file, line, heading) of the published rationale, for the 26 published criteria."""
        return self.last.rat_head(code, crit)

    def doc_lines(self, fn):
        if fn not in self.docs:
            with open(os.path.join(HERE, fn), encoding="utf-8") as f:
                self.docs[fn] = f.read().split("\n")
        return self.docs[fn]

    def published_rationale(self, code, crit):
        """(file, line, label, text, more) of the published rationale. In Report v1.6 the criterion's heading line carries
        it ('#### **C1.1 Name: 0.5** text'). In an entry's scoring document it is the first paragraph that opens
        '**Rationale', or, where none does, the paragraph after the '*Pass threshold' line, under the criterion's heading;
        more is True where further paragraphs of the section follow it. text is None where no such paragraph is found."""
        fn, ln, head = self.rationale(code, crit)
        lines = self.doc_lines(fn)
        if fn == "NEEC_Report_v1_6.md":
            m = re.match(r"^#+\s*\**(?P<label>[^*]*?)\*\*\s*(?P<body>.*)$", lines[ln - 1])
            assert m, f"{fn} line {ln}: not a rationale heading"
            return fn, ln, m.group("label").strip(), m.group("body").strip() or None, False
        sec, cur = [], []
        for line in lines[ln:]:
            if line.startswith("#"):
                break
            if line.strip():
                cur.append(line.strip())
            elif cur:
                sec.append(" ".join(cur))
                cur = []
        if cur:
            sec.append(" ".join(cur))
        k = next((i for i, q in enumerate(sec) if q.startswith("**Rationale")), None)
        if k is None:
            k = next((i + 1 for i, q in enumerate(sec) if q.startswith("*Pass threshold")), None)
            if k is not None and k >= len(sec):
                k = None
        if k is None:
            return fn, ln, head, None, False
        return fn, ln, head, re.sub(r"^\*\*Rationale[^*]*\*\*\s*", "", sec[k]) or None, k + 1 < len(sec)


REF = re.compile(r"(?:evidence_cache/(?P<d>[\w.\-]+)/)?(?P<f>[\w\-]+\.(?:json|csv))\b"
                 r"|(?P<doc>(?:NEEC_[\w]+|SCORING_PROTOCOL)\.md), line (?P<ln>\d+)")


def cap(s):
    s = str(s).strip()
    return s[:1].upper() + s[1:]


def esc(s):
    s = re.sub(r"\s+", " ", str(s)).strip()
    return re.sub(r"<(?=[A-Za-z/!?])", "&lt;", s.replace("|", "\\|"))


def linked(ctx, s):
    """Escape a text and link the evidence_cache data files and 'file.md, line N' references it names."""
    s = esc(s)

    def sub(m):
        if m.group("doc"):
            doc, ln = m.group("doc"), int(m.group("ln"))
            if not os.path.isfile(os.path.join(HERE, doc)):
                ctx.dangling.append(doc)
                return m.group(0)
            ctx.links += 1
            return f"[{m.group(0)}]({ctx.blob(doc, ln)})"
        d, f = m.group("d"), m.group("f")
        if d is None:
            d = ctx.cache_name.get(f)
            if d is None:
                return m.group(0)
        if (d, f) not in ctx.cache:
            ctx.dangling.append(f"evidence_cache/{d}/{f}")
            return m.group(0)
        ctx.links += 1
        return f"[`{f}`]({ctx.blob('evidence_cache/' + d + '/' + f)})"

    return REF.sub(sub, s)


def ranks(ctx):
    totals = sorted((ctx.blocks[c]["summary"]["total"] for c in ctx.blocks), reverse=True)
    return {c: (totals.index(ctx.blocks[c]["summary"]["total"]) + 1, totals.count(ctx.blocks[c]["summary"]["total"]) > 1)
            for c in ctx.blocks}


def cell(ctx, code, crit, stats):
    """The lines of one criterion's section in one system's report."""
    c = ctx.cmap[crit]
    v = ctx.entries[code]["vector"][crit]
    pub = ctx.p.vec[code].get(crit)
    unit = ctx.units.get((code, crit))
    rev = c["revision"]["cls"]
    out = [f'<a id="{anchor(crit)}"></a>', f'### {crit} {c["name"]}: {fmt(v)} ({WORD[v]})', ""]
    if unit is not None:
        assert unit["verdict"] == v, f"{code} {crit}: the unit's verdict {unit['verdict']} is not the corpus score {v}"
        tag = ctx.part[(code, crit)]
        sess = ctx.sess[tag]
        if pub is None:
            stats["new"] += 1
            prov = (f"New in v2.0: scored for the first time in {part_label(tag)} (Session {sess}), "
                    f"on a unit of the three new criteria.")
        else:
            stats["read"] += 1
            prov = (f"Read by the rescoring pass in {part_label(tag)} (Session {sess}). Published (v1) score {fmt(pub)}; "
                    f"v2.0 score {fmt(v)}" + (": changed." if pub != v else ": unchanged."))
    else:
        assert pub is not None and pub == v, f"{code} {crit}: held cell's score differs from the published one"
        stats["held"] += 1
        prov = (f"No unit of the rescoring pass reads this cell. The published score stands: {fmt(v)}. "
                f"The reading behind it is the published rationale linked below.")
    out += [f"*{prov}*", ""]
    out += [f'Criterion in v2.0: class {rev} ({CLASS_GLOSS[rev]}). Pass Threshold: '
            f'{esc(c["definition"]["pass_threshold"])}.', ""]
    if unit is not None:
        defs = c["definition"]["clauses"]
        cl = unit["clauses"]
        if len(cl) == len(defs):
            out += ["| # | Clause (v2.0) | Status | Reading | Source |", "|---|---|---|---|---|"]
            for i, ((st, txt, src), d) in enumerate(zip(cl, defs), 1):
                out.append(f"| {i} | {esc(d)} | {pc.STATUS[st]} | {linked(ctx, txt)} | {linked(ctx, src)} |")
        else:
            stats["structure"] += 1
            out += [f"*The unit was read in {part_label(ctx.part[(code, crit)])} on its {len(cl)} clauses then in force; "
                    f"v2.0 states {len(defs)}: " + "; ".join(esc(d) for d in defs) + ".*", "",
                    "| # | Status | Reading | Source |", "|---|---|---|---|"]
            for i, (st, txt, src) in enumerate(cl, 1):
                out.append(f"| {i} | {pc.STATUS[st]} | {linked(ctx, txt)} | {linked(ctx, src)} |")
        out.append("")
    flags = [f for f in ctx.blocks[code]["flags"] if f["criterion"] == crit]
    for f in flags:
        stats["flag"] += 1
        alt = " or ".join(fmt(a) for a in f["alternatives"])
        rd = f.get("reading") or ""
        dup = bool(unit is not None and unit["note"] and esc(unit["note"]) == esc(rd))
        rd = ("The reading that supports it is in the record linked below." if rd in ("", "see the pass record")
              else cap(linked(ctx, rd)))
        out += [f"**Close call.** Scored {fmt(f['scored'])}; a reasonable scorer could set {alt}. {rd}", ""]
    if unit is not None and unit["note"] and not (flags and dup):
        out += [f"**Note.** {cap(linked(ctx, unit['note']))}", ""]
    if unit is not None and unit.get("zero"):
        out += [f"**Why 0.0 stands (protocol 2.1).** {cap(linked(ctx, unit['zero']))}", ""]
    refs = []
    if unit is not None:
        tag = ctx.part[(code, crit)]
        rec = getattr(ctx.mod_of[tag], "RECORD", None)
        if rec:
            ln = ctx.record_line(rec, code, crit)
            if ln:
                refs.append(f"Pass record: [{rec}, line {ln}]({ctx.blob(rec, ln)})")
                stats["recline"] += 1
            else:
                refs.append(f"Pass record: [{rec}]({ctx.blob(rec)})")
        else:
            script = ctx.parts[tag][1]
            refs.append(f"Applied by decision {tag}: [{script}]({ctx.blob(script)})")
    if refs:
        out += ["  \n".join(refs), ""]
    if pub is not None:
        fn, ln, label, text, more = ctx.published_rationale(code, crit)
        stats["rat"] += 1
        head = (f"**Published (v1) rationale**, under the heading \"{esc(label)}\" at "
                f"[{fn}, line {ln}]({ctx.blob(fn, ln)})")
        if text:
            stats["rattext"] += 1
            out += [head + ":", "", "> " + esc(text) + (" *(The section continues at the link.)*" if more else ""), ""]
        else:
            out += [head + " (no rationale paragraph under it; read the section there).", ""]
    return out


def report(ctx, code, rk, stats):
    e = ctx.entries[code]
    b = ctx.blocks[code]
    s = b["summary"]
    row = ctx.csv[e["display_name"]]
    info = ctx.cfg["scope_classes"][e["scope_class"]]
    n = len(ctx.order)
    rank, tied = rk[code]
    out = [f'# {e["display_name"]} ({code}): evidence report', "",
           "> Generated by `build_evidence.py` from the rescoring pass and the published records; never edit by hand. "
           "The v2.0 scores are provisional until Report and Paper v2.0.", "",
           f'**v2.0 score:** {fmt(s["total"])} of {fmt(float(n))} ({row["total_percent"]}), {s["failures"]} structural '
           f'failure{"s" if s["failures"] != 1 else ""}, {s["tier"]}. Rank {rank}{" (tied)" if tied else ""} of '
           f'{len(ctx.blocks)} on equal weights.', "",
           f'**Kind:** {esc(info["label"])}: {esc(info["gloss"])}.', ""]
    note = ctx.cfg["systems"][code].get("note")
    if note:
        out += [f"**About the name:** {esc(note)}", ""]
    if code == ctx.cfg["site"]["author_design"]:
        out += [f"**Disclosure:** designed by Duke Johnson, one of NEEC's two authors. "
                f"[How the project handles this]({ctx.base}method.html#disclosure).", ""]
    docs = ", ".join(f"[{d}]({ctx.blob(d)})" for d in b["record"]["documents"])
    out += [f"**Site page:** [systems/{slug(code)}.html]({ctx.base}systems/{slug(code)}.html). "
            f"**All systems:** [index](index.md). **Source scoring documents (the full v1 text):** {docs}.", "",
            "## How to read this report", "",
            "Each criterion has one section, linked from the table below. A section gives the score (1.0 pass, 0.5 partial, "
            "0.0 structural failure), then one row per clause of the criterion's v2.0 Pass Threshold: its status "
            "(cleared, short, not shown, out of reach, or moot), the reading, and the source, with each data file in "
            "`evidence_cache/` linked. Two links at the foot of a section go straight to the line: the pass record that "
            "read the unit, and the published (v1) rationale in the long scoring document. A cell the pass did not read "
            "says so and keeps its published rationale. Close calls are scores a reasonable scorer could set differently.", "",
            "## Contents", ""]
    body = []
    for d in ctx.domains:
        ds = s[d["id"]]
        mx = sum(1.0 for _ in d["criteria"])
        out += [f'**{d["id"][1:]}. {esc(d["name"])}: {fmt(ds)} of {fmt(mx)}**', "",
                "| Criterion | Score | Basis |", "|---|---|---|"]
        body += [f'## Domain {d["id"][1:]}: {esc(d["name"])}', ""]
        for crit in d["criteria"]:
            v = e["vector"][crit]
            unit = ctx.units.get((code, crit))
            pub = ctx.p.vec[code].get(crit)
            if unit is None:
                basis = "held at the published score"
            elif pub is None:
                basis = f"new in v2.0, scored in {part_label(ctx.part[(code, crit)])}"
            else:
                basis = (f"read in {part_label(ctx.part[(code, crit)])}"
                         + (f", changed from {fmt(pub)}" if pub != v else ""))
            if any(f["criterion"] == crit for f in b["flags"]):
                basis += "; close call"
            out.append(f'| [{crit} {esc(ctx.cmap[crit]["name"])}](#{anchor(crit)}) | {fmt(v)} | {basis} |')
            body += cell(ctx, code, crit, stats)
        out.append("")
    return "\n".join(out + body).rstrip("\n") + "\n"


def index(ctx, rk):
    tiers = {t["name"]: i for i, t in enumerate(ctx.crit["tiers"])}
    codes = sorted(ctx.blocks, key=lambda c: (tiers[ctx.blocks[c]["summary"]["tier"]], -ctx.blocks[c]["summary"]["total"],
                                              ctx.cfg["systems"][c]["short"].lower()))
    out = ["# NEEC evidence reports", "",
           "> Generated by `build_evidence.py`; never edit by hand. The v2.0 scores are provisional until Report and Paper v2.0.",
           "",
           "One report per scored system. Each has a section for every one of the 29 criteria with the score, the reading of "
           "each clause of the Pass Threshold, the source (data files in `evidence_cache/` linked), the close call if any, and "
           "direct links to the line of the published rationale and of the rescoring record. The full v1 text stays in the "
           "scoring documents named at the head of each report.", "",
           f"Site: [{ctx.base}]({ctx.base}). Method and disclosure: [{ctx.base}method.html]({ctx.base}method.html).", "",
           "| System | Code | Total | Failures | Tier | Rank (equal weights) |", "|---|---|---|---|---|---|"]
    for c in codes:
        s = ctx.blocks[c]["summary"]
        rank, tied = rk[c]
        out.append(f'| [{esc(ctx.entries[c]["display_name"])}]({slug(c)}.md) | `{c}` | {fmt(s["total"])} | '
                   f'{s["failures"]} | {s["tier"]} | {rank}{" (tied)" if tied else ""} |')
    return "\n".join(out) + "\n"


def build():
    ctx = Ctx()
    rk = ranks(ctx)
    stats = dict(new=0, read=0, held=0, flag=0, structure=0, recline=0, rat=0, rattext=0)
    files = {}
    for code in ctx.entries:
        files[f"{OUTDIR}/{slug(code)}.md"] = report(ctx, code, rk, stats)
    files[f"{OUTDIR}/index.md"] = index(ctx, rk)
    # totals in the corpus equal the blocks' (the reports show the blocks' totals; the sections show the corpus' scores)
    for code, e in ctx.entries.items():
        t = sum(e["vector"][c] for c in ctx.order)
        assert abs(t - ctx.blocks[code]["summary"]["total"]) < 1e-9, f"{code}: corpus total {t} differs from the blocks'"
    return ctx, files, stats


def main():
    check = "--check" in sys.argv[1:]
    ctx, files, stats = build()
    cells = len(ctx.entries) * len(ctx.order)
    assert stats["new"] + stats["read"] + stats["held"] == cells, "every cell has a section"
    problems = []
    if ctx.dangling:
        problems.append("links to files that do not exist: " + ", ".join(sorted(set(ctx.dangling))))
    out = os.path.join(HERE, OUTDIR)
    if check:
        on_disk = {}
        if os.path.isdir(out):
            for fn in sorted(os.listdir(out)):
                on_disk[f"{OUTDIR}/{fn}"] = open(os.path.join(out, fn), encoding="utf-8", newline="").read()
        for k in sorted(set(files) | set(on_disk)):
            if files.get(k) != on_disk.get(k):
                problems.append(f"{k}: " + ("missing on disk" if k not in on_disk else
                                            "not generated" if k not in files else "differs from what the script generates"))
    else:
        os.makedirs(out, exist_ok=True)
        for k, text in files.items():
            with open(os.path.join(HERE, k), "w", encoding="utf-8", newline="") as f:
                f.write(text)
    print(f"{'CHECK' if check else 'WROTE'} {len(files)} files in {OUTDIR}/: the index and {len(files) - 1} system reports")
    print(f"  {cells} criterion sections: {stats['read']} read by the pass, {stats['new']} new in v2.0, {stats['held']} held at the published score")
    print(f"  {stats['flag']} close calls shown; {stats['rat']} published rationales linked by line, {stats['rattext']} quoted; "
          f"{stats['recline']} of {stats['read'] + stats['new']} pass units linked to their record's line")
    print(f"  {stats['structure']} units shown on the clause structure they were read on (it differs from v2.0's)")
    print(f"  {ctx.links} links to data files and to documents by line; {len(set(ctx.dangling))} dangling")
    if problems:
        for pr in problems:
            print("  FAIL " + pr)
        sys.exit(1)
    print("EVIDENCE REPORTS " + ("CHECKED." if check else "WRITTEN."))


if __name__ == "__main__":
    main()
