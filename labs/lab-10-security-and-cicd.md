# Lab 10: Security, Networking Design, CI/CD Gate and Capacity

Full steps: [Day 12](../week-02/day-12.md).

## 1. Scenario
Security review before production: who can call what, how traffic is isolated, how releases are gated, and what happens at peak load.

## 2. Objectives
Audit role assignments and secrets; design a private-network topology; build an evaluation gate and CI workflow skeleton; size capacity and add rate limiting.

## 3. AI-103 objectives
D1-05, D1-06, D1-08, D1-09, D1-12, D1-15.

## 4. Prerequisites
[Lab 09](lab-09-tracing-and-evaluation.md).

## 5. Services
Azure RBAC, private link (design only), GitHub Actions (design), Key Vault (concept), quotas.

## 6. SDKs
`azure-identity`; Azure CLI; standard library for the gate and limiter.

## 7. Duration
75 minutes.

## 8. Resources
None deployed. Documents: identity matrix, network diagram, workflow YAML, capacity calculation.

## 9. Cost and risk
EUR 0. Risk: designs that cannot work on the Free Search tier go unnoticed.

## 10. Steps
List roles; scan for secrets; draw network design; write `gate.py` and workflow; calculate TPM; implement a token bucket limiter.

## 11. Expected result
Completed identity matrix; network diagram with endpoints and DNS; gate script that exits non-zero on a bad score; rate limiter in use.

## 12. Validation
See Day 12 section 11.

## 13. Break/fix
Planted secret; over-broad role analysis; failing gate.

## 14. Common mistakes
Owner for apps; keys in CI secrets when OIDC is possible; ignoring DNS for private endpoints; no evaluation threshold.

## 15. Troubleshooting
| Symptom | Check |
|---|---|
| Gate cannot find scores | Metric key names in `rag_eval.json` |
| `az role assignment list` empty | Scope and permission to read assignments |
| Action fails in CI | Federated credential subject and role |

## 16. Capstone relevance
M9: security and deployment design with a working gate.

## 17. Cleanup
None; confirm `.env` is untracked.
