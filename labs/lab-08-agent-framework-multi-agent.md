# Lab 08: Microsoft Agent Framework, Multi-Agent and Approvals

Full steps: [Day 10](../week-02/day-10.md).

## 1. Scenario
A support flow must research an answer, write it with citations, and pause for human approval before creating tickets, while cheap deterministic rules handle simple lookups.

## 2. Objectives
Build an `Agent` with tools and sessions; require tool approval and handle it; compose a sequential workflow; add a rules-first router; read about A2A.

## 3. AI-103 objectives
D2-10, D2-11, D2-16, D2-03, D1-15, D1-16. Label: framework is Supporting Knowledge; concepts are Exam Essential; AI-500 Foundation.

## 4. Prerequisites
[Lab 07](lab-07-agent-knowledge-and-mcp.md); `agent-framework` installed.

## 5. Services
Foundry model via `FoundryChatClient`.

## 6. SDKs
`agent-framework` (`Agent`, `tool`, `Message`, `agent_framework.foundry`, `agent_framework.orchestrations`), `azure-identity`, `pydantic`.

## 7. Duration
75 minutes.

## 8. Resources
None.

## 9. Cost and risk
About EUR 0.50. Risk: multi-agent flows multiply token use.

## 10. Steps
Hello agent with session; approval round trip; sequential workflow; hybrid router; A2A notes.

## 11. Expected result
Two-turn session memory; ticket creation pauses until approval; workflow prints the writer output; router skips model calls for rule-matched queries.

## 12. Validation
See Day 10 section 11.

## 13. Break/fix
Missing `await`; approval mode set to never require; pipeline propagates a hallucinated fact.

## 14. Common mistakes
Calling `agent.run` outside an event loop; forgetting the session; assuming more agents improve quality; leaving approval off.

## 15. Troubleshooting
| Symptom | Check |
|---|---|
| Import error | `pip show agent-framework`, optional `agent-framework-foundry` |
| Auth errors | Same role as Day 2 |
| Approval never requested | `approval_mode` on the tool |

## 16. Capstone relevance
M7: multi-agent flow with approval and routing.

## 17. Cleanup
None.
