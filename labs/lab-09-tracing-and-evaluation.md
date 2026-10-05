# Lab 09: Tracing, Telemetry and Agent Evaluation

Full steps: [Day 11](../week-02/day-11.md).

## 1. Scenario
Users report slow and sometimes wrong answers. You need traces, token and latency analytics, an evaluation harness for the agent, and provenance for auditing.

## 2. Objectives
Export OpenTelemetry spans to Application Insights; add custom spans and attributes; use framework tracing locally; evaluate agent cases; classify failures; record provenance.

## 3. AI-103 objectives
D2-12, D2-15, D1-10, D1-14, D1-15, D2-04.

## 4. Prerequisites
[Lab 08](lab-08-agent-framework-multi-agent.md).

## 5. Services
Application Insights, Azure Monitor, Foundry evaluators.

## 6. SDKs
`azure-monitor-opentelemetry`, `opentelemetry-sdk`, `agent_framework.observability`, `azure-ai-evaluation` (optional).

## 7. Duration
75 minutes.

## 8. Resources
Application Insights (workspace-based) with a daily cap; `data/eval/agent_cases.jsonl`.

## 9. Cost and risk
About EUR 0.70. Risks: sensitive data in telemetry; verbose spans; evaluation billing.

## 10. Steps
Create Application Insights; init exporter; wrap stages in spans; console exporters for framework spans; agent harness; failure table; provenance record.

## 11. Expected result
10 traces with child spans; per-case pass/fail; error table; provenance JSON per answer.

## 12. Validation
See Day 11 section 11.

## 13. Break/fix
Wrong connection string; injected slow tool; sensitive-data check.

## 14. Common mistakes
Enabling sensitive-data capture; mixing exporters in one process; no daily cap; evaluating only happy paths.

## 15. Troubleshooting
| Symptom | Check |
|---|---|
| No telemetry | Connection string; console exporter proves spans exist |
| Spans in unexpected table | Query `dependencies`, `requests`, `traces` |
| Evaluator errors | Package version and endpoint config |

## 16. Capstone relevance
M8: observability and evaluation pipeline.

## 17. Cleanup
Keep Application Insights until Day 21 with the cap.
