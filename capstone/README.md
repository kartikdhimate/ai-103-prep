# KnowledgeDesk CLI: Capstone Overview

**KnowledgeDesk** is a Python CLI assistant for an imaginary company ("Contoso Field Services"). It answers policy questions from documents with citations, creates support tickets with human approval, extracts fields from invoices, describes images safely, analyzes and translates text, and handles short voice interactions. It is a **learning vehicle**: every feature maps to exam objectives. It is not a production product.

## What you build

| Capability | Days | Objectives |
|---|---|---|
| Keyless Foundry client, cost guard | 1-3 | D1-05/09/12, D2-05/06 |
| Prompts, structured output | 4 | D2-13/14 |
| Safety gate | 5, 14, 18 | D1-13/14, D3-14/15 |
| RAG on Azure AI Search | 6-7 | D1-03, D2-02, D5-02 |
| Agent with tools and policy | 8-9 | D2-07/08/09, D1-16 |
| Multi-agent and approvals | 10 | D2-10/11/16 |
| Observability and evaluation | 11 | D2-12/15, D1-10/14/15 |
| Security and CI design | 12 | D1-05/08/12 |
| Document extraction | 13 | D5-04/06/07/08 |
| Vision | 14-15 | D3-01 to D3-16 |
| Text, speech | 16-17 | D4-01 to D4-08 |
| Hardening and demo | 18-20 | cross-domain |

## Commands (final state)

```text
kd ask "<question>"             grounded answer with citations
kd ticket "<request>"           agent with approval for write actions
kd extract <file>               invoice fields with confidence
kd image <file> "<question>"    guarded visual Q and A
kd analyze <file> [--translate fr]
kd voice --file in.wav
kd eval                         retrieval, answer and agent evaluation
kd redteam                      attack suite
```

## Repository layout you create

```text
src/
  common/            config.py, cost_guard.py, retry.py, rate_limit.py
  labs/              one script per lab
  knowledgedesk/     foundry_client, prompts, structured, safety, chunking, search_index,
                     ingest, ingest_docs, retrieve, answer, tools, tool_policy, agent,
                     maf_flow, telemetry, vision, imagegen, text_analysis, voice, evals/
data/                docs, docs_raw, images, eval, redteam
out/                 reports, audit log (gitignored)
```

## Related documents

[ARCHITECTURE](ARCHITECTURE.md) | [REQUIREMENTS](REQUIREMENTS.md) | [TASKS](TASKS.md) | [TESTING](TESTING.md) | [SECURITY](SECURITY.md) | [COSTS](COSTS.md) | [Back to main README](../README.md)

## Rules of the capstone

1. Keyless authentication unless [SECURITY.md](SECURITY.md) lists an exception.
2. Free tiers only; every paid call goes through the cost guard.
3. Every external text, file, image, audio and tool result is untrusted data.
4. Every claim in the docs is backed by a run you did; "not verified" is written where it applies.
