# Lab 04: Content Safety, Guardrails and Evaluators

Full steps: [Day 5](../week-01/day-05.md).

## 1. Scenario
A public-facing assistant must refuse harmful content, resist hidden instructions in documents, and be measurable for answer groundedness.

## 2. Objectives
Analyze text for harm; call prompt-attack detection; configure a Foundry guardrail; run a groundedness evaluator; tune thresholds.

## 3. AI-103 objectives
D1-13, D1-14, D2-04, D3-14 (text preview).

## 4. Prerequisites
[Lab 03](lab-03-prompting-and-structured-output.md).

## 5. Services
Azure AI Content Safety (F0), Foundry guardrails, evaluators.

## 6. SDKs
`azure-ai-contentsafety`, `azure-ai-evaluation`, `httpx` (REST for prompt attack check), `azure-identity`.

## 7. Duration
75 minutes.

## 8. Resources
Content Safety F0; custom guardrail on a deployment.

## 9. Cost and risk
EUR 0 for Content Safety (5,000 text records per month on Free); about EUR 0.20 evaluator tokens. Risk: loops that exhaust the free quota.

## 10. Steps
Create resource and role; analyze text; shield prompt REST call; guardrail test; groundedness scoring; threshold table; build `safety.py`.

## 11. Expected result
Categories with severities; attack flagged for the poisoned document; blocked response from the guardrail; two groundedness scores that differ in the expected direction.

## 12. Validation
Outputs recorded; threshold table with rationale; `safety.py` blocks the poisoned document.

## 13. Break/fix
Indirect injection through context; threshold tuning with false positives and misses.

## 14. Common mistakes
Checking only user input; trusting model-based scores as truth; failing open on service errors.

## 15. Troubleshooting
| Symptom | Check |
|---|---|
| 401/403 | Role and custom-subdomain endpoint |
| REST 400 | Path, body and api-version on the jailbreak-detection page |
| Evaluator errors | Config keys, endpoint form, package version; use `.venv311` |

## 16. Capstone relevance
M3: safety gate on input, documents, outputs (fail closed).

## 17. Cleanup
Keep Content Safety F0; remove or document the strict guardrail.
