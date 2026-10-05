# KnowledgeDesk CLI: Tasks and Milestones

Check items off as you complete them. Milestone IDs match [TRACKER.md](../TRACKER.md).

## Milestones

| ID | Day | Tasks | Done |
|---|---|---|---|
| M0 | 1 | Create `src/common/config.py`, `cost_guard.py`; `.env`; venv; compat gate result | [ ] |
| M1 | 2-3 | `foundry_client.py` with `get_clients()` and `ask()`; `retry.py`; model decision matrix | [ ] |
| M2 | 4 | `prompts.py` (grounded system prompt), `structured.py` (`Ticket`, `Critique`) | [ ] |
| M3 | 5 | `safety.py`: input, documents, output; fail closed; threshold table | [ ] |
| M4 | 6 | `chunking.py`, `search_index.py`, `ingest.py`, `retrieve.py` | [ ] |
| M5 | 7 | `answer.py`, eval set, `retrieval_eval.py`, `index_health.py`, evaluator run | [ ] |
| M6 | 8-9 | `tools.py`, `agent.py`, tool loop, `tool_policy.py`, audit log | [ ] |
| M7 | 10 | `maf_flow.py`: approval, sequential workflow, rules router | [ ] |
| M8 | 11 | `telemetry.py`, `agent_eval.py`, provenance | [ ] |
| M9 | 12 | Identity matrix, network design, `gate.py`, `rate_limit.py`, CI workflow text | [ ] |
| M10 | 13 | `ingest_docs.py`, `extract_invoice`, ingestion-quality report | [ ] |
| M11 | 14-15 | `vision.py`, image guard, `imagegen.py` (optional) | [ ] |
| M12 | 16-17 | `text_analysis.py`, `voice.py` | [ ] |
| M13 | 18 | `redteam.py`, attack and benign sets, fixes, report | [ ] |
| M14 | 20 | Demo run, docs finalized | [ ] |

## CI workflow skeleton (Day 12)

Paste the workflow text from Day 12 here after you adapt it to your repository (verify action versions and secrets in your own GitHub settings):

```yaml
# paste here
```

## Demo script (write on Day 19, run on Day 20)

| Minute | Action | Expected result |
|---|---|---|
| 0-2 | `kd ask` a policy question | Cited answer |
| 2-3 | `kd ask` an unanswerable question | Refusal |
| 3-5 | `kd ticket` with a create request | Approval prompt, ticket created after approval |
| 5-6 | Inject an instruction through a document | Blocked or not executed |
| 6-7 | `kd image` with the poisoned image | Blocked before the model |
| 7-8 | `kd extract` on an invoice | Fields with confidence |
| 8-9 | Show a trace and the audit log | Spans and decisions visible |
| 9-10 | `kd eval` and `kd redteam` summaries | Metrics table |

## Definition of done for the capstone

- [ ] All milestones M0-M14 checked.
- [ ] All FR rows in [REQUIREMENTS.md](REQUIREMENTS.md) have a test result in [TESTING.md](TESTING.md).
- [ ] No secrets in the repository; exceptions listed in [SECURITY.md](SECURITY.md).
- [ ] [COSTS.md](COSTS.md) shows actual spend.
- [ ] Architecture diagrams match the code.
