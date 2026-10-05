# Lab 02: Model Comparison, Quotas and Cost

Full steps: [Day 3](../week-01/day-03.md).

## 1. Scenario
A product owner asks which model to use for five typical tasks under a tight budget, and what happens at peak load.

## 2. Objectives
Compare two chat models on latency, tokens and cost; read quota information; handle 429 with retry and backoff; write a model decision matrix.

## 3. AI-103 objectives
D1-01, D1-02, D1-06, D1-07, D1-09, D2-01.

## 4. Prerequisites
[Lab 01](lab-01-foundry-first-call.md).

## 5. Services
Foundry model deployments, quota views, pricing page.

## 6. SDKs
`openai` (through `AIProjectClient.get_openai_client()`), `azure-ai-projects`.

## 7. Duration
75 minutes.

## 8. Resources
A second small-model deployment; `out/model_comparison.csv`.

## 9. Cost and risk
About EUR 0.30. Risk: raising capacity "to avoid 429s"; looping retries without limits.

## 10. Steps
Deploy second model; fill price constants; run 10 calls; read results; view quota; force throttling; add `call_with_retry`.

## 11. Expected result
CSV with tokens, latency, cost per prompt per model; a written matrix in ARCHITECTURE.md; retry handler that survives 429.

## 12. Validation
10 CSV rows; matrix present; forced 429 handled.

## 13. Break/fix
Minimum capacity plus a tight loop to trigger throttling; fix with backoff.

## 14. Common mistakes
Using outdated prices; comparing on one prompt only; ignoring output tokens in cost; infinite retry.

## 15. Troubleshooting
| Symptom | Check |
|---|---|
| No 429 appears | Lower capacity or shorten delays, stay within 40 calls |
| Model unavailable | Region catalog; choose another small model |
| Cost looks wrong | Input vs output price columns |

## 16. Capstone relevance
M1 extension: chosen chat and embedding models and shared retry helper.

## 17. Cleanup
Delete the second deployment if unused; reset capacities to minimum.
