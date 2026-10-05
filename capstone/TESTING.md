# KnowledgeDesk CLI: Testing

## Test layers

| Layer | What | Tooling | When |
|---|---|---|---|
| Unit | chunker, router rules, tool policy, cost guard, rate limiter (no network) | `pytest` (add with `pip install pytest`) | every change |
| Contract | tool schemas match functions; Pydantic models parse sample JSON | `pytest` | every change |
| Retrieval eval | hit@1, hit@4, MRR over `qa.jsonl` | `evals/retrieval_eval.py` | after ingest or index changes |
| Answer eval | groundedness, relevance | `azure-ai-evaluation` runner | after prompt, model or data changes |
| Agent eval | tool choice, args, must/must-not text | `evals/agent_eval.py` | after agent changes |
| Red team | attack success rate, over-refusal | `evals/redteam.py` | before demo; as a gate |
| Gate | thresholds that fail the build | `evals/gate.py` | CI design (Day 12) |

LLM-judged scores are signals, not truth; spot-check a sample by hand each time.

## Requirement test matrix

| Requirement | Test | Result |
|---|---|---|
| FR-01 | No API key variable needed for model calls | |
| FR-02 | Unknown question returns refusal; known question cites a source | |
| FR-03 | Four modes return results for the same query | |
| FR-04 | Invalid enum value is handled | |
| FR-05 | Poisoned document and image blocked before model call | |
| FR-06 | `create_ticket` requires approval | |
| FR-07 | Disallowed tool denied; log line written | |
| FR-08 | PDF with table becomes markdown chunks | |
| FR-09 | Low-confidence invoice flagged | |
| FR-10 | Poisoned image blocked | |
| FR-11 | PII not present in model input | |
| FR-12 | Voice round trip works | |
| FR-13 | Trace with token attributes exists | |
| FR-14 | Provenance record per answer | |
| FR-15 | Evaluation commands run | |

## RAG monitoring plan (Day 7)

| Signal | How measured | Threshold | Action |
|---|---|---|---|
| Rolling groundedness mean | evaluator on a daily sample | below 4 | investigate retrieval and prompts |
| Zero-result rate | count of empty searches | above 5% | review chunking and synonyms |
| Ingestion failures | failed uploads per run | any | stop and fix |
| Index storage | `get_index_statistics` | above 80% of tier | prune or upgrade |
| Latency p95 | traces | above target | check model and search spans |

## Agent evaluation and error taxonomy (Day 11)

| Category | Count | Example | Fix |
|---|---|---|---|
| Wrong tool | | | |
| Bad arguments | | | |
| No tool when needed | | | |
| Hallucinated data | | | |
| Wrong refusal | | | |
| Unsafe output | | | |

## Red-team results (Day 18)

| Category | Attempts | Successes | Over-refusal | Mitigation | Residual risk |
|---|---|---|---|---|---|
| Direct override | | | | | |
| Instruction extraction | | | | | |
| Indirect: document | | | | | |
| Indirect: image | | | | | |
| Indirect: audio | | | | | |
| Tool abuse | | | | | |
| Exfiltration | | | | | |
| PII | | | | | |
| Cost abuse | | | | | |
| Benign set | | | | | |

## Regression rule

Any change to prompts, models, tool descriptions, thresholds or chunking requires re-running retrieval eval, agent eval and the red-team suite before the change is accepted.
