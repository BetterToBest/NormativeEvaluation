#!/usr/bin/env python3
"""
build_replication_kit.py -- NEEC: a blind replication kit for one target (protocol section 11; D23, D24)
=======================================================================================================
Session 30. A blind replication (decision D2) re-scores one entry of the corpus without sight of its
original scoring. This script builds, for one target, the kit the replicator receives:

  SCORING_PROTOCOL.md        a blind copy of the protocol (decision D24): the passages that report the
                             target's scoring -- its scores, readings, flags, scope class, or the outcome
                             its pilot expects -- are withheld and marked where they stood; a note under
                             the title says so; no rule is changed. Each withheld passage is named by a
                             start and an end anchor (any run of whitespace matches any other), each of
                             which must occur exactly once.
  neec_corpus.json           the corpus (decision D23) with the target withheld; neec_entry.py reads the
                             corpus from it, since the canonical script is not in the kit.
  criteria.json, criteria_schema.json, summary_block_schema.json, neec_entry.py
                             byte copies of the canonical files.
  REPLICATION_BRIEF.md       what to score, what to produce, how to check it, and the rules of blindness.

Then it (1) scans every file of the kit except the brief for the target's names, code and signature
figures, and stops on any hit; (2) runs neec_entry.py's two self-tests inside the kit, where no
canonical script is present; and (3) writes the kit as one archive, stored uncompressed with fixed
timestamps and sorted entries, so that it reproduces byte for byte. It prints every file's MD5.

It does not run the maintainers' baseline -- the original entry validated as a candidate against the
kit's corpus -- which run_all_checks.py runs as its own check.

Usage:   python3 build_replication_kit.py TARGET [INDIR] [OUTDIR]     (defaults: . and out)
         TARGET is a corpus code with a target definition below (the first pilot: OS).
Inputs (pinned by MD5, in INDIR): the files listed in PINS. Writes OUTDIR/neec_replication_kit_TARGET/
and OUTDIR/neec_replication_kit_TARGET.zip. Prints file names only; deterministic.
"""
import hashlib
import importlib.util
import io
import json
import os
import re
import subprocess
import sys
import zipfile

PINS = {
    "SCORING_PROTOCOL.md": "13e382bc",
    "criteria.json": "6542331e",
    "criteria_schema.json": "4aa5c6c6",
    "summary_block_schema.json": "8c0b62e9",
    "neec_entry.py": "6ddd3b0a",
    "neec_corpus.json": "ba3c7f70",
    "build_corpus_file.py": "adad7d3b",
}
COPIED = ("criteria.json", "criteria_schema.json", "summary_block_schema.json", "neec_entry.py")
STAMP = (2026, 9, 19, 0, 0, 0)   # fixed archive timestamp: the kit's build date, never the clock
MARK = "*[Withheld from this blind copy: it reports the scoring of the system under replication.]*"

TARGETS = {
    "OS": dict(
        name="Ostrom-style commons governance",
        gloss=("the self-governance of common-pool resources by the communities that use them, through rules "
               "those communities make, monitor and enforce, in the tradition of Elinor Ostrom's work "
               "(*Governing the Commons*, 1990) and the research that followed it"),
        block=dict(key="Ostrom-Style Commons Governance", code="OSR",
                   display_name="Ostrom-Style Commons Governance",
                   document="NEEC_OstromCommons_replication_scoring.md"),
        # terms that must not occur in any kit file but the brief (case-insensitive), and code patterns
        scan=["ostrom", "commons governance", "1,048,576", "twenty flags", "46.7%"],
        withhold=[
            ("header: the question deferred to the pilot (D18(b))",
             "One question is deferred by decision:", "waits for the pilot replication (section 11).",
             "One question is deferred by decision to the pilot replication (section 11); " + MARK),
            ("3.1: the target among the declared examples of the mechanism class",
             "Islamic finance, Ostrom-style commons governance (the", None,
             "Islamic finance and one example withheld from this blind copy (the"),
            ("3.3: the target among the evaluations whose scope the owner confirmed",
             "Qatar, Islamic finance and Ostrom evaluations.", None,
             "Qatar and Islamic finance evaluations, and in one withheld from this blind copy."),
            ("3.4: decision D18(b), the target's flag register",
             "- (b) Most of Ostrom-style commons governance's twenty flags,",
             "which tests exactly this; the register is reconsidered then.",
             "- (b) " + MARK),
            ("3.5: the worked example (the target's joint readings and scenario)",
             "### 3.5 Worked example: Ostrom-style commons governance",
             "3 failures, tier unchanged), reported but not scored.",
             "### 3.5 Worked example\n\n" + MARK),
            ("6.4: the example comparing two entries' tier robustness",
             "For example, on the corpus as scored and staged in Session",
             "Ostrom's 1,048,576.",
             MARK),
            ("9.2: the example code (the target's) replaced by another entry's",
             "(for example `OS`)", None, "(for example `GEO`)"),
            ("11.6: the pilot this kit serves",
             "6. **The first pilot** re-scores", "`neec_entry_candidate_OS_blind_output.txt`.",
             "6. *[Withheld from this blind copy: it describes the pilot this kit serves.]*"),
            ("13, D21 note: the documents brought to whole percents",
             "In the D14 pass the two documents that displayed one decimal",
             "which checks each old figure against its total before replacing it.",
             MARK),
        ],
    ),
}

BRIEF = """# NEEC blind replication — brief

**What this is.** A blind re-scoring of one system in the NEEC (Normative
Economic Evaluation Criteria) corpus. Its purpose is to test whether an
independent scorer, following the scoring protocol, reaches the same scores
(`SCORING_PROTOCOL.md`, section 11). You are the replicator. The system's
original scoring is not in this kit, and you should not look for it.

## The system to score

**{name}**: {gloss}.

Everything else is yours to decide under the protocol, and to state and
justify: the scope class and population rule (section 3), the evidence
(section 4), the peers (section 5), and the flags, joint readings and
scenarios (section 6).

## What is in this kit

| File | What it is |
|---|---|
| `SCORING_PROTOCOL.md` | the scoring protocol as a blind copy: {nwith} passages that report or refer to this system's original scoring are withheld and marked where they stood{neutral}; every rule is as in the full protocol |
| `criteria.json`, `criteria_schema.json` | the 26 criteria with their 1.0 / 0.5 / 0.0 anchors, and the schema |
| `summary_block_schema.json` | the schema of the summary block your document ends with |
| `neec_entry.py` | the entry verifier (Python 3, standard library only) |
| `neec_corpus.json` | the corpus: the other {ncorpus} scored entries, with their codes, scope classes and 26 scores |
| `REPLICATION_BRIEF.md` | this brief |

## What to produce

One Markdown scoring document, laid out as protocol section 7 requires,
ending with one summary block (section 9). Name it `{document}`. In the block
use:

- `key` and `display_name`: `{key}`
- `code`: `{code}`
- `record`: `documents` your file name; `scored` who scored it and when;
  `structure` `native-v2`
- `scope`: your declaration, with `basis` `stated`
- `peers`: the corpus entries you calibrated against (section 5)

## Checking your block

```
python3 neec_entry.py --candidate {document}
```

It must end with `ALL BLOCKS VALID.` It also prints your peer matrix
(section 5.2); print it before you fix your scores, and reconcile every
difference it marks (5.3). The verifier checks structure and arithmetic, not
whether the evidence supports a score.

## Rules of blindness

1. Consult no NEEC material outside this kit: not the NEEC repository
   (github.com/BetterToBest/NormativeEvaluation) or its site, not the NEEC
   Paper, Report or Visual Suite, and no other account of how NEEC scored this
   system. If you come across such material, stop reading it and say so in
   your reviewer disclosure.
2. Use the evidence section 4 asks for: the founding literature, empirical
   work, implementations, and critical sources from more than one direction.
3. Send your document as it stands when you finish; do not revise it after
   seeing the original scoring.

## Reviewer disclosure

In the reviewer disclosure (section 7.2, item 9), state who or what scored
the entry (for an AI system, the model and the interface), the dates, the
tools used (web search, code execution), any NEEC material you encountered,
and every point where the protocol was ambiguous or silent. Those points are
the most useful result of a pilot: ambiguities become revisions of the
protocol.

---

*Kit built by `build_replication_kit.py` from `SCORING_PROTOCOL.md` (md5
{pmd5}) and `neec_corpus.json` (md5 {cmd5}).*
"""


def md5(data):
    return hashlib.md5(data).hexdigest()[:8]


def anchor(a):
    return re.compile(r"\s+".join(re.escape(t) for t in a.split()))


def once(text, a, what):
    ms = list(anchor(a).finditer(text))
    if len(ms) != 1:
        raise ValueError(f"{what}: anchor occurs {len(ms)} times: {a[:60]!r}")
    return ms[0]


def counts(target):
    """Withheld passages (their replacement says so) and neutralised ones (an example replaced)."""
    marked = sum(1 for w in target["withhold"] if "withheld" in w[3].lower())
    return marked, len(target["withhold"]) - marked


def blind_protocol(text, target, pmd5):
    for label, start, end, new in target["withhold"]:
        s = once(text, start, label)
        t = once(text, end, label) if end else s
        if t.end() < s.start():
            raise ValueError(f"{label}: end anchor before start anchor")
        text = text[:s.start()] + new + text[t.end():]
    title = "# NEEC Scoring Protocol\n"
    if not text.startswith(title):
        raise ValueError("the protocol does not start with its title")
    marked, neutral = counts(target)
    note = (f"\n> **Blind copy for a replication kit.** Generated by `build_replication_kit.py` from\n"
            f"> `SCORING_PROTOCOL.md` (md5 {pmd5}). {marked} passages that report or refer to the scoring\n"
            f"> of the system under replication are withheld and marked where they stood"
            + (f", and {neutral} example{'s' if neutral > 1 else ''} naming it {'are' if neutral > 1 else 'is'} "
               f"replaced by another entry's" if neutral else "") + ";\n> no rule differs from the full protocol.\n")
    return title + note + text[len(title):]


def leaks(text, target):
    low = text.lower()
    hits = [t for t in target["scan"] if t.lower() in low]
    code = re.escape(sorted(k for k, v in TARGETS.items() if v is target)[0])
    hits += [m.group(0) for m in re.finditer(r"[\"`'\[]" + code + r"[\"`'\]]", text)]
    return hits


def main(argv):
    if not argv or argv[0] not in TARGETS:
        print(f"usage: build_replication_kit.py TARGET [INDIR] [OUTDIR]; targets: {', '.join(sorted(TARGETS))}")
        return 2
    code = argv[0]
    indir = argv[1] if len(argv) > 1 else "."
    outdir = argv[2] if len(argv) > 2 else "out"
    target = TARGETS[code]
    print("=" * 96)
    print(f"build_replication_kit.py -- blind replication kit {code} ({target['name']})")
    print("=" * 96)
    raw = {}
    for name, want in PINS.items():
        p = os.path.join(indir, name)
        if not os.path.isfile(p):
            sys.exit(f"ERROR: cannot find {name}")
        raw[name] = open(p, "rb").read()
        if md5(raw[name]) != want:
            sys.exit(f"ERROR: {name} md5 {md5(raw[name])}, expected {want}")
    print("inputs (pinned): " + ", ".join(f"{n} ({m})" for n, m in PINS.items()))
    spec = importlib.util.spec_from_file_location("build_corpus_file", os.path.join(indir, "build_corpus_file.py"))
    BCF = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(BCF)

    kit = {}
    try:
        kit["SCORING_PROTOCOL.md"] = blind_protocol(raw["SCORING_PROTOCOL.md"].decode("utf-8"), target,
                                                    PINS["SCORING_PROTOCOL.md"]).encode("utf-8")
    except ValueError as err:
        sys.exit(f"ERROR: {err}")
    corpus = json.loads(raw["neec_corpus.json"])
    kept = [e for e in corpus["entries"] if e["code"] != code]
    if len(kept) != len(corpus["entries"]) - 1:
        sys.exit(f"ERROR: the corpus has no single entry with code {code}")
    desc = ("A blind replication kit's corpus: the canonical corpus with one entry, the system under replication, "
            "withheld (SCORING_PROTOCOL.md section 11). Each entry's key, short code, display name, scope class "
            "and criterion scores, in the canonical order. Generated by build_replication_kit.py from "
            f"neec_corpus.json (md5 {PINS['neec_corpus.json']}); never edited by hand. Scores: 1.0 pass, 0.5 "
            "partial, 0.0 structural failure; totals, failures and tiers follow by protocol section 2.")
    kit["neec_corpus.json"] = BCF.render(desc, corpus["criteria"], kept).encode("utf-8")
    for name in COPIED:
        kit[name] = raw[name]
    b = target["block"]
    kit["REPLICATION_BRIEF.md"] = BRIEF.format(
        name=target["name"][0].upper() + target["name"][1:], gloss=target["gloss"], nwith=counts(target)[0],
        neutral=(f", and {counts(target)[1]} example code naming it is replaced by another entry's"
                 if counts(target)[1] else ""),
        ncorpus=len(kept), document=b["document"], key=b["key"], code=b["code"],
        pmd5=PINS["SCORING_PROTOCOL.md"], cmd5=PINS["neec_corpus.json"]).encode("utf-8")

    print(f"\nwithheld from the blind copy of SCORING_PROTOCOL.md ({len(target['withhold'])} passages, "
          f"each anchor matched once):")
    for i, (label, *_rest) in enumerate(target["withhold"], 1):
        print(f"  {i}. {label}")
    print(f"corpus: {len(kept)} of {len(corpus['entries'])} entries (the target withheld)")
    scanned = [n for n in sorted(kit) if n != "REPLICATION_BRIEF.md"]
    found = {n: leaks(kit[n].decode("utf-8"), target) for n in scanned}
    nhits = sum(len(h) for h in found.values())
    print(f"leak scan: {len(scanned)} files (every file but the brief), {len(target['scan'])} terms and the code "
          f"{code!r} in quotes, backticks or brackets: {nhits} hits")
    if nhits:
        for n, h in found.items():
            if h:
                print(f"  {n}: {h}")
        return 1

    folder = f"neec_replication_kit_{code}"
    kdir = os.path.join(outdir, folder)
    os.makedirs(kdir, exist_ok=True)
    for name in sorted(kit):
        with open(os.path.join(kdir, name), "wb") as f:
            f.write(kit[name])
    print("\nkit self-test, run inside the kit (no canonical script present):")
    for args in (["--selftest"], ["--selftest", "--candidate"]):
        proc = subprocess.run([sys.executable, "neec_entry.py"] + args, cwd=kdir, capture_output=True)
        for line in proc.stdout.decode("utf-8").splitlines():
            print("  " + line)
        if proc.returncode != 0:
            print(f"  exit status {proc.returncode}: the kit does not work on its own")
            return 1
    print("\nfiles:")
    for name in sorted(kit):
        print(f"  {folder}/{name:28} md5 {md5(kit[name])}  {len(kit[name]):7d} bytes")
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_STORED) as z:
        for name in sorted(kit):
            info = zipfile.ZipInfo(f"{folder}/{name}", date_time=STAMP)
            info.create_system = 3
            info.external_attr = 0o644 << 16
            z.writestr(info, kit[name])
    data = buf.getvalue()
    with open(os.path.join(outdir, folder + ".zip"), "wb") as f:
        f.write(data)
    print(f"\nwrote {folder}.zip (md5 {md5(data)}, {len(data)} bytes; {len(kit)} files, stored, fixed timestamps)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
