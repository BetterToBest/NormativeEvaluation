#!/usr/bin/env python3
"""
display_names.py -- NEEC: the one display-name mapping for the generators of the current state (Session 84, ledger S69, D68)
==========================================================================================================================
The owner renamed the scored entry CCO-PTF-CIP-SZH to CCO-PTF-PTH-SZH-CIP (ledger D68, decision 84.5): PTH (Public Trust
Housing) is already read in the entry's units, so the name is corrected, not the scope. The records of Sessions 1 to 83 keep the
old name, and so do the generators that rebuild them (their outputs are those records). The generators of the current state
(apply_owner_s84.py: the corpus, the CSV and the site's blocks; build_evidence.py: the evidence reports; build_site.py: the
site and its visual suite) take every displayed name from here. An entry's `key` and `code` are identifiers and do not change.

  DISPLAY        {code: the name shown now}, for the entries whose name changed
  OLD            {code: the name the records before Session 84 use}
  rename(s)      the string with every old name replaced by the name shown now, except where 'formerly ' precedes it (the
                 entry's note on the site names its earlier name that way)
  rename_obj(o)  the same through a JSON value, leaving `key` fields (identifiers) as they are
  keep_quotes(s) rename(s) for a Markdown text, leaving quoted lines ('> ') and the published-rationale heading lines alone:
                 a quotation of a published document keeps its words

No main; nothing is printed. Deterministic.
"""
import re

DISPLAY = {"CCO": "CCO-PTF-PTH-SZH-CIP"}
OLD = {"CCO": "CCO-PTF-CIP-SZH"}


def rename(s):
    for code, old in OLD.items():
        s = re.sub(r"(?<!formerly )" + re.escape(old), DISPLAY[code], s)
    return s


def rename_obj(o):
    if isinstance(o, dict):
        return {k: (v if k == "key" else rename_obj(v)) for k, v in o.items()}
    if isinstance(o, list):
        return [rename_obj(v) for v in o]
    return rename(o) if isinstance(o, str) else o


def keep_quotes(s):
    return "\n".join(ln if ln.startswith("> ") or ln.startswith("**Published (v1) rationale**") else rename(ln)
                     for ln in s.split("\n"))
