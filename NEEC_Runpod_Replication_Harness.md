# NEEC Runpod Replication Harness — Session 31

**Status: infrastructure validated and designed; the actual Ostrom pilot
content has NOT been generated yet.** This document is the reference for
whichever session runs it.

## Why this exists

Handoff 30's "Running the pilot (owner)" section offered four ways to get a
blind replicator: an incognito claude.ai chat, Claude Code in an empty
folder, another AI system, or a human scorer. The owner asked Session 31 to
set up a fifth: a Runpod-hosted open-weight model, orchestrated through the
Runpod connector now attached to this account, to keep the pilot off
Claude's own weekly message budget.

## What was validated this session

- **No dedicated infrastructure was created.** `list-endpoints` (owned
  endpoints) returned zero. Everything below uses Runpod's **Public
  Endpoints** — managed, pay-per-token, shared, always-on. There is no pod
  or serverless endpoint of ours to leave running or to tear down. This
  satisfies the owner's "make sure it stops billing" concern by
  construction: nothing was deployed, so nothing idles.
- **Two candidate models, both live and callable:**

  | Endpoint ID | Model | Measured price | Output format |
  |---|---|---|---|
  | `moonshot-kimi` | `kimi-k2.6` (default) | $0.95/M input, $4.00/M output | Clean OpenAI-style `message.content` / `message.reasoning_content` split |
  | `qwen3-32b-awq` | `Qwen/Qwen3-32B-AWQ` | ~$10/M input, ~$10/M output (derived from two calibration calls) | Raw `<think>...</think>` block inline in `tokens[0]`, no separate field — must be parsed |

  **Recommendation: `moonshot-kimi`.** Cheaper on output (the bulk of a
  drafting task), no manual `<think>`-tag stripping, and Kimi K2.6 is the
  stronger model for the kind of multi-source synthesis and academic
  drafting this task needs.
- **Neither endpoint's native `tools` (function-calling) parameter works.**
  Passing an OpenAI-style `tools` array produced no `tool_calls` field on
  either model — on Kimi it just rambled in `content` about whether it had
  a tool (2,127 tokens, $0.0085, for one trivial question) before declining
  to answer. Native tool-calling is not wired up on these public endpoints.
- **A manual marker protocol works cleanly on both models** once the system
  prompt is explicit and directive. Tested end-to-end on Kimi and Qwen3 with
  a throwaway, NEEC-unrelated question (GitHub star count) — search
  request, external fetch, result relay, final answer, all clean:

  ```
  SEARCH: <query>        — model emits this alone when it needs information
  FINAL: <answer>         — model emits this alone when it has enough
  ```

  System prompt template (Kimi; drop the `reasoning_content` framing for
  Qwen3, which has no separate field):

  ```
  You are a research assistant with no live internet access of your own.
  A separate process will run any search you request and give you the raw
  results. When you need current or factual information you do not
  reliably know, respond with ONLY one line of the exact form:
  SEARCH: <query>
  and nothing else in the content field — no explanation, no caveats, no
  alternate text. When you have enough information to answer, respond with
  ONLY one line of the exact form:
  FINAL: <your answer>
  Never fabricate a number or fact you are not sure of; use SEARCH instead.
  ```

  Call shape (Kimi):
  ```json
  {
    "messages": [ {"role":"system","content":"..."}, {"role":"user","content":"..."} ],
    "sampling_params": {"max_tokens": <N>}
  }
  ```
  Response: `output[0].result.choices[0].message.content` (the marker line)
  and `.message.reasoning_content` (its private reasoning — not needed
  downstream, but useful to log for the reviewer disclosure).

- **Session cost for all of the above: ~$0.02** (10 Qwen3 calls + 3 Kimi
  calls, all trivial). $14.98 of the $15 credit is untouched.

## The two roles a Runpod-hosted model cannot fill itself

Neither endpoint has web access or code execution. Both are required by the
brief (`REPLICATION_BRIEF.md` rule 2: "use the evidence section 4 asks for
... founding literature, empirical work, implementations, and critical
sources from more than one direction"; and the verifier check,
`neec_entry.py --candidate`). So the model needs an external process to:

1. **Run its `SEARCH:` queries verbatim** and return raw, unedited results.
2. **Run `neec_entry.py --candidate <its draft>`** and return the verifier's
   output verbatim, so it can fix structural/arithmetic errors before
   sending a final document (per the brief: "print it before you fix your
   scores").

That external process has to be a Claude session with the Runpod connector
(to reach the model) and either `web_search` or a browsing connector (to
search) and code execution (to run the verifier) — none of which a plain
script can do from this container's sandboxed network, which cannot reach
`api.runpod.ai` or the open web at all. So **the harness is not a
standalone script; it is a Claude session, turn by turn, acting as a
disciplined relay between the brief and the Runpod model.**

## D25 (new, proposed — owner decision needed before running the real pilot)

**The methodological wrinkle:** this Session 31 conversation is inside the
NEEC Project, with full access to Ostrom's canonical scoring
(`NEEC_Ostrom_Commons_scoring_scratch.md` and its snapshot) and every
insertion since. If *this* session (or any NEEC-project session) is the one
relaying searches and verifier output to the Runpod model, the relay itself
is not blind — only the replicator model is. That is workable only under a
strict, stated discipline:

- Relay **exactly** what the model asks for — the literal `SEARCH:` query,
  nothing added, nothing substituted.
- Return **raw, unfiltered** results — the top N hits as the search tool
  gives them, not a curated or pre-summarized subset chosen because it
  points toward or away from the canonical score.
- Run the verifier and return its **exact, unedited** output — which the
  brief itself already limits to structure and arithmetic, not evidence
  quality, so this step carries no scoring information regardless of who
  runs it.
- Disclose this arrangement explicitly in the reviewer disclosure (section
  7.2, item 9) that ships with the replication document — "tool executor:
  a Claude session with access to NEEC's own materials, acting only as a
  mechanical search/verifier relay under the stated discipline" — so
  anyone reading the pilot's result can weigh that fact themselves.

**The cleaner alternative:** run the whole loop from a session that has
*no* NEEC memory or project files at all — an incognito claude.ai chat (or
a non-NEEC project) with the Runpod connector added and `web_search`
available. That session would be blind in exactly the way Handoff 30's
first pilot option already was, and the relay-discipline caveat above
would not be needed at all. The only cost is losing this session's already-
loaded context, which does not matter for this task — the whole point of
the blind kit (`neec_replication_kit_OS.zip`) is that it is self-contained.

**Recommendation:** use the clean alternative if convenient. If not (e.g.
the owner wants to keep everything in one thread), the disclosed relay
discipline above is an acceptable, stated compromise — the project's own
practice, per `methodology.md`, is to flag contestable calls rather than
silently resolve them, and this is one.

**Owner to decide:** which of the two, before the real pilot content is
generated. Nothing has been generated yet, so nothing needs to be redone
either way.

## Recommended runbook (whichever session runs it)

1. **Unzip `neec_replication_kit_OS.zip`** (or use the seven
   `replication_kit_OS_*` files already on the mount) in the executing
   session. Upload/attach them there if it's a fresh chat.
2. **Don't paste the whole kit into every model call.** The kit is ~48,000
   tokens combined; at Kimi's rate that's ~$0.20 per turn just to resend it,
   and a multi-turn loop would blow the budget fast. Instead:
   - Give the model the brief in full (it's short, ~1,000 words) plus the
     26 criteria **names only** (not the full anchor text) up front.
   - Let it request specific material the same way it requests a search:
     add a third marker, `READ: <name>` (e.g. `READ: criterion C3.2`,
     `READ: corpus entry GEO`, `READ: protocol section 5`), and answer with
     just that slice, pulled from the local kit files. This mirrors how a
     human replicator would actually work — consulting sections as needed,
     not holding the whole protocol in view at once.
3. **Order of work**, following `SCORING_PROTOCOL.md` section 7's own
   structure: scope declaration (section 3) → evidence and scoring per
   criterion, in batches of 4-6 rather than one at a time → peer selection
   and calibration (section 5, using `neec_corpus.json`'s 22 entries) →
   flags, joint readings, scenarios (section 6) → assemble the full
   document (section 7) → run `neec_entry.py --candidate
   NEEC_OstromCommons_replication_scoring.md`, relay its output, let the
   model reconcile differences (5.3) → reviewer disclosure (7.2 item 9,
   including the D25 relay-discipline note above) → send as final.
4. **Budget guardrail:** stop and check cumulative `cost` fields against a
   **$5 ceiling** for this pilot (leaving $10 of the $15 for other project
   uses); the validated design should land well under that, but Kimi's
   reasoning traces can run long on harder criteria, so track it rather
   than assume it.
5. **Deliverables to bring back to the NEEC Project:** the finished
   `NEEC_OstromCommons_replication_scoring.md` and the final
   `neec_entry.py --candidate` output showing `ALL BLOCKS VALID.` Add both
   as project files; then `compare_replication.py` (already queued in
   Handoff 30) does the real comparison against the canonical Ostrom entry.

## Other uses for the Runpod credit on this project

Flagging for later, not acted on this session: any future blind
replication (if the pilot leads to scoring more systems this way), or bulk
draft-checking passes where a cheap second model is useful as a sanity
check before spending a Claude turn on it. The `neec_c14` cross-validation
and Compassionism Simulation fidelity checks are CPU-bound Python/Node
work already running fine in this session's own sandbox — no GPU or
Runpod benefit there.
