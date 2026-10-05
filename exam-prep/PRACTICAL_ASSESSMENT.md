# Practical Assessment (Day 20)

A timed, closed-notes check of whether you can reproduce key patterns. Allowed: your own capstone code and the official documentation links in [RESOURCES.md](../RESOURCES.md). Not allowed: search engines, AI assistants, forums. Total 135 minutes: Part A 25, Part B 75, Part C 35.

Score yourself immediately after each part with the rubric. Record the result in [WEAK_AREAS.md](WEAK_AREAS.md) and the Day 20 progress entry.

## Part A: Design scenarios (25 min, 5 min each)

Answer in 6-10 lines each, with a small diagram when helpful.

| # | Scenario | Evidence of mastery |
|---|---|---|
| A1 | A public sector client needs a Q&A assistant over 20,000 PDFs. Data must not leave the EU and no keys are allowed. Design ingestion, retrieval, identity and network. | Layout/OCR, chunking, hybrid + semantic, managed identity, private endpoints, region choice, monitoring of ingestion |
| A2 | The assistant can create refunds. Design controls so one malicious document cannot trigger one. | Untrusted data handling, approval, allowlist, limits, audit, evaluation of attacks |
| A3 | Costs doubled after launch. List five investigations and five mitigations. | Token logs, per-feature cost, model choice, caching, batch, limits, alerts |
| A4 | Choose between a Language-service pipeline and an LLM for classifying 10 million short texts per month; justify. | Determinism, cost, schema flexibility, latency, privacy |
| A5 | Describe a release process for a prompt change in an agent. | Versioned agents, offline evals, red-team regression, staged rollout, rollback |

## Part B: Hands-on tasks (75 min)

Use your repository. Each task has a time box; stop at the box and note what is missing.

| # | Task | Box | Done when |
|---|---|---|---|
| B1 | From a clean shell, authenticate keylessly and print a model answer with token usage | 8 | Output shown; no key used |
| B2 | Query the index in hybrid and semantic modes for a given question and print top 3 with scores | 10 | Both modes return results |
| B3 | Produce a cited answer and a refusal for two supplied questions | 10 | Citation format correct; refusal for the unknown question |
| B4 | Define a new function tool (`get_invoice_total(file)`) with schema, policy entry and a test call | 12 | Tool called by the agent; policy enforced |
| B5 | Add approval for a write tool and demonstrate approve and reject | 10 | Both paths logged |
| B6 | Run content safety on a given text and a poisoned document; show decisions | 8 | Document blocked before model |
| B7 | Extract fields from a provided invoice and flag low confidence | 10 | Fields plus confidence; review flag |
| B8 | Run the retrieval metrics and the red-team summary | 7 | Tables printed |

## Part C: Troubleshoot a broken environment (35 min)

Have a friend or your past self apply 5 or more of these faults without telling you which (or apply them a day earlier and avoid reading the diff):

| # | Fault | Typical symptom |
|---|---|---|
| C1 | Data-plane role removed from the Foundry resource | 403 on model calls |
| C2 | `AZURE_AI_MODEL_DEPLOYMENT` set to a wrong name | Deployment not found |
| C3 | Search index vector dimension changed | Upload error / bad results |
| C4 | Content Safety endpoint uses the wrong host | Auth or not found |
| C5 | Tool schema field renamed but not the function | Argument errors |
| C6 | Application Insights connection string altered | No telemetry |
| C7 | Policy allowlist missing a tool | Agent says it cannot use search |
| C8 | `.env` missing `AZURE_SEARCH_INDEX` | Config error |
| C9 | Translator region omitted | 401 |
| C10 | Image file too large | API error |

Record time to diagnose and fix each fault.

## Rubric

| Part | Points | Scoring |
|---|---|---|
| A (5 scenarios x 6) | 30 | 6 = correct pattern with named controls; 4 = mostly right, a gap; 2 = partial; 0 = wrong |
| B (8 tasks x 6) | 48 | 6 = done within box; 4 = done with doc lookup beyond box; 2 = partial; 0 = not done |
| C (5 faults x 4) | 20 | 4 = fixed within 7 minutes; 2 = fixed later; 0 = not fixed |
| Process | 2 | Used only allowed resources |
| **Total** | **100** | |

Interpretation (this plan's own targets): 85+ strong; 70-84 acceptable with remediation of failed items; below 70 extend preparation. Map each lost point to an objective ID and add it to [WEAK_AREAS.md](WEAK_AREAS.md).
