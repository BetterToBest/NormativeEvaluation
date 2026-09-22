import re, sys, json
DOCS = {"GE":"NEEC_Georgism_LVT_scoring_scratch.md","MC":"NEEC_MutualCredit_LETS_scoring_scratch.md",
 "DE":"NEEC_DoughnutEconomics_scoring_scratch.md","UBS":"NEEC_UniversalBasicServices_scoring_scratch.md",
 "SWF":"NEEC_SovereignWealthFundStatism_scoring_scratch.md","CN":"NEEC_StateCapitalism_China_scoring_scratch.md",
 "SG":"NEEC_StateCapitalism_Singapore_scoring_scratch.md","1C":"NEEC_Step1c_Retrofit_C1_2ab_C1_5.md"}
ALIAS = {"CCO":r"CCO", "PE":r"ParEcon|Participatory Economics", "NSD":r"Nordic", "INT":r"\bIntegral\b",
 "DG":r"Degrowth", "MS":r"Market Socialism", "MMT":r"\bMMT\b|Job Guarantee", "MC":r"Mutual Credit|\bLETS\b",
 "UBI":r"\bUBI\b|Universal Basic Income", "SWF":r"\bSWF\b|Sovereign Wealth Fund Statism", "SG":r"Singapore",
 "OS":r"Ostrom", "GE":r"Georgis|Land Value Tax|\bLVT\b", "UBS":r"\bUBS\b|Universal Basic Services",
 "IF":r"Islamic", "FALC":r"\bFALC\b|Fully Automated", "DE":r"Doughnut", "SQ":r"Status Quo", "CN":r"\bChina\b",
 "SC":r"Stakeholder", "CPS":r"\bCPS\b|Centrally Planned", "QA":r"\bQatar", "LM":r"Libertarian|Minarch"}
SELF = {"GE":"GE","MC":"MC","DE":"DE","UBS":"UBS","SWF":"SWF","CN":"CN","SG":"SG","1C":None}
SIG = re.compile(r"\b[01]\.[05]\b|/26|\bfail|\btier\b|Adequate|\bscor|dominat|\btie[sd]?\b|\btied\b|\brank|alongside|\bonly\b|highest|lowest|\bsame\b|\bmatch|\bjoin|\bequal|\bexceed|\babove\b|\bbelow\b|\bhigher\b|\blower\b", re.I)
POS = re.compile(r"\bcorpus\b|\brank|\bdominat|\bties?\b|\btied\b|every other|no other|only (other )?(system|entry)|\b(1[2-9]|2[0-3]) (scored )?systems\b|\b(thirteen|fifteen|seventeen|eighteen|nineteen|twenty)[- ](system|scored)", re.I)
def sentences(text):
    out=[]; lines=text.split("\n"); sec=""; buf=[]; start=None
    def flush():
        nonlocal buf,start
        if buf:
            para=" ".join(buf)
            for s in re.split(r"(?<=[.;:!?])\s+(?=[A-Z(*\"'])", para):
                out.append((start, sec, s.strip()))
        buf=[]; start=None
    for i,l in enumerate(lines,1):
        m=re.match(r"#{2,5}\s+(.*)",l)
        if m: flush(); sec=m.group(1)[:60]; continue
        if not l.strip() or l.startswith("|"):
            flush()
            if l.startswith("|"): out.append((i,sec,l.strip()))
            continue
        if start is None: start=i
        buf.append(l.strip())
    flush(); return out
def scan(code):
    text=open(DOCS[code],encoding="utf-8").read(); res=[]
    for ln,sec,s in sentences(text):
        names=[k for k,p in ALIAS.items() if k!=SELF[code] and re.search(p,s)]
        if (names and SIG.search(s)) or POS.search(s):
            res.append((ln,sec,names,s))
    return res
if __name__=="__main__":
    codes=sys.argv[1:] or list(DOCS)
    for c in codes:
        r=scan(c); print(f"## {c}: {len(r)} candidate sentences")
