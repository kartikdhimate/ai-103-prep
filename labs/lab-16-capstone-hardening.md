# Lab 16: Capstone Hardening and Red Team

Full steps: [Day 18](../week-03/day-18.md).

## 1. Scenario
Before demoing the assistant, security asks for evidence that attacks across text, documents, images, audio and tools are handled without blocking legitimate users.

## 2. Objectives
Write a threat model; build an attack suite and benign set; measure attack success and over-refusal; fix with layered controls; add regression gating.

## 3. AI-103 objectives
D1-13, D1-16, D2-11, D2-16, D3-15.

## 4. Prerequisites
Labs 00-15 where available; at least the text, document and tool paths.

## 5. Services
All capstone services (Content Safety, Search, agent, Speech, Vision as built).

## 6. SDKs
As used by the capstone; standard library for the runner.

## 7. Duration
75 minutes.

## 8. Resources
`data/redteam/attacks.jsonl`, `benign.jsonl`, `out/redteam_report.json`.

## 9. Cost and risk
About EUR 0.50. Risks: running huge inputs (cost abuse tests) against paid services; storing attack payloads with sensitive data.

## 10. Steps
Threat model; attack suite; run and measure; fix and re-run; rules-first ordering; report; add to gate.

## 11. Expected result
Report with ASR and over-refusal by category; targets met or residual risk documented.

## 12. Validation
See Day 18 section 11.

## 13. Break/fix
Over-blocking threshold; regression after prompt change; log leakage.

## 14. Common mistakes
Only testing text input; no benign set; no regression gate; logging raw attacks.

## 15. Troubleshooting
| Symptom | Check |
|---|---|
| ASR unstable between runs | Run each case 3 times; count any success |
| Benign prompts blocked | Threshold and rules |
| Runner slow or costly | Cap input sizes; skip expensive channels in CI |

## 16. Capstone relevance
M13: defensible security posture and test evidence.

## 17. Cleanup
Delete throwaway agents and versions.
