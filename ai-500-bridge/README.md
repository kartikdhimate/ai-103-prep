# AI-103 to AI-500 Bridge

AI-500 targets an **expert-level practitioner who designs, builds and optimizes production-ready multi-agent systems** (audience profile in the study guide, last updated 2026-07-16 when checked on 2026-10-04): <https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500>. Exam page: <https://learn.microsoft.com/en-us/credentials/certifications/exams/ai-500/>. Check both for current prerequisites, format and weights before planning.

AI-103 is the associate-level app and agent developer exam. Finishing AI-103 does not cover AI-500, but your capstone gives you a head start.

## AI-500 domains (weights from the study guide)

| Domain | Weight |
|---|---|
| Architect multi-agent solutions | 15-20% |
| Develop multi-agent solutions in Azure | 30-35% |
| Evaluate, optimize and monitor multi-agent solutions | 20-25% |
| Secure, govern and deploy multi-agent solutions | 20-25% |

The audience profile names Microsoft Agent Framework, Model Context Protocol (MCP), RAG and LangGraph as frameworks and standards you should know, plus Azure compute, network, storage and data services, and strong Python.

## What you already have

| AI-500 topic area | AI-103 foundation (day) | Gap to close |
|---|---|---|
| Decompose goals into agents, tools and workflows | Agents and tools (8-10) | Formal design, control loops, human-in-the-loop design, persona and autonomy specs |
| Tool scopes, permissions, authentication | Tool policy, approval (9, 10), identity matrix (12) | On-behalf-of flows, OAuth 2.0, user impersonation, API keys vs identity trade-offs |
| Agent memory and context management | Conversations and sessions (8, 10) | Short vs long-term memory architecture, compaction, context window failure modes, tenant isolation |
| Multi-agent RAG | RAG and extraction (6, 7, 13) | Multi-agent retrieval design, embedding quality, chunking strategy at scale |
| MCP servers and clients | MCP tool use (9) | Building MCP servers (for example on Azure Functions, Logic Apps or API Management), error handling and fallback, tool result validation |
| Orchestration patterns | Sequential workflow and patterns reading (10) | Hub-and-spoke, parallel, peer-to-peer, orchestrator-subagent; caching; spawning and concurrency control; A2A integration; LangChain/LangGraph |
| Evaluation strategies | Evaluators, agent harness (5, 7, 11) | Human review in Foundry, memory/knowledge/tool evals, LLM-as-a-judge frameworks, synthetic data, continuous improvement loops |
| Observability and monitoring | Tracing (11) | Trace correlation across services, drift and quality regression detection, SLAs, chargebacks, alerting |
| Security and guardrails | Safety gate, red team (5, 14, 18) | Multi-intervention guardrails on inputs, tool calls, tool responses and outputs; custom guardrails; AI Red Teaming Agent in Foundry; Key Vault design |
| Deployment and release | CI/CD design (12) | DTAP, blue/green, canary, rollback, IaC testing |
| Fine-tuning strategy | - | Data, frequency, evaluation of tuned models |
| Developer environment and SDLC | Repo and venv (1) | Dev containers, VS Code extensions, AI instructions, dependency management |

## Suggested bridge plan (about 10 sessions, after the exam)

Do not start until you have taken AI-103; sequence matters less than depth.

| Session | Topic | Build |
|---|---|---|
| 1 | Read the AI-500 guide; mark each bullet red/amber/green | Gap sheet |
| 2 | Agent Framework deep dive: orchestrations (concurrent, group chat, handoff, magentic) | Re-implement the capstone flow with handoff |
| 3 | MCP server of your own and tool error handling | Small MCP server exposing ticket tools with validation |
| 4 | Memory architecture and context management | Session vs long-term store with a compaction experiment |
| 5 | Identity: on-behalf-of, OAuth, Key Vault | Design doc plus a managed-identity secret retrieval demo |
| 6 | Guardrail strategy across input, tool call, tool response, output | Extend `safety.py` into four intervention points |
| 7 | Evaluation: LLM-as-a-judge, synthetic data, human review | Judge-calibrated eval set |
| 8 | Monitoring and cost: correlation IDs, drift, chargeback | Dashboard queries and alert rules |
| 9 | Release engineering: DTAP, canary, rollback | Pipeline design with rollback drill |
| 10 | A2A and cross-framework (LangGraph) reading; mock design questions | Written solution architecture |

Official pointers to start from (listed in the AI-500 guide): Microsoft Foundry documentation and the Learn module "Build a multiple-agent workflow automation solution by using Microsoft Agent Framework" (find via the study guide page; title as shown there).

## Labels used in this plan

Items tagged **AI-500 Foundation** in [EXAM_OBJECTIVES.md](../EXAM_OBJECTIVES.md) and in the day files are the on-ramp: Agent Framework, MCP, A2A, multi-agent patterns, approvals, and observability.

[Main README](../README.md) | [Day 21](../week-03/day-21.md)
