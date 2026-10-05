# AI-103 Exam Objectives Map

Source: official study guide, skills measured as of April 16, 2026: <https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-103>.
Bullet text is copied from the study guide; the local IDs (`D1-01` ...) are this plan's own and are not Microsoft identifiers.

**Depth** values: `Hands-on` = you build and run it; `Design` = you must reason about it (portal walkthrough, diagram, quiz); `Concept` = costly or access-limited, studied with a minimal or optional demo.
All 64 bullets are **Exam Essential**. Items outside the guide are listed at the end under their own labels.

## Domain weights and day allocation

| Domain | Weight | Days that are primary |
|---|---|---|
| D1 Plan and manage an Azure AI solution | 25-30% | 1, 2, 3, 5, 12 (plus parts of 7, 9, 11) |
| D2 Implement generative AI and agentic solutions | 30-35% | 4, 6, 7, 8, 9, 10, 11 (plus 18) |
| D3 Implement computer vision solutions | 10-15% | 14, 15 (plus 5, 18) |
| D4 Implement text analysis solutions | 10-15% | 16, 17 (plus 4) |
| D5 Implement information extraction solutions | 10-15% | 6, 13 (plus 7, 9) |
| Review | - | 19, 20, 21 |

## D1 Plan and manage an Azure AI solution (25-30%)

| ID | Objective (study guide wording) | Days | Labs | Depth |
|---|---|---|---|---|
| D1-01 | Choose an appropriate model for each task, including large language models (LLMs), small language models, multimodal models, and Foundry Tools | 3, 2 | 02 | Hands-on |
| D1-02 | Choose the appropriate Foundry services for generative tasks, grounding, vector search, agent workflows, or multimodal processing | 3, 9 | 02, 07 | Design |
| D1-03 | Choose an appropriate method for retrieval and indexing | 6, 7 | 05 | Hands-on |
| D1-04 | Choose appropriate memory, tool, and knowledge integration services for agent solutions | 8, 9 | 06, 07 | Hands-on |
| D1-05 | Design Azure infrastructure for AI apps and agent-based solutions | 2, 12 | 01, 10 | Design |
| D1-06 | Choose appropriate deployment options | 3, 12 | 02, 10 | Design |
| D1-07 | Configure model and agent deployments | 2, 3, 8 | 01, 02, 06 | Hands-on |
| D1-08 | Integrate Foundry projects with continuous integration and continuous deployment (CI/CD) pipelines | 12 | 10 | Design |
| D1-09 | Manage quotas, scaling, rate limits, and cost footprints for model and agent workloads | 1, 3, 12 | 00, 02, 10 | Hands-on |
| D1-10 | Monitor model performance, drift, safety events, and grounding quality | 7, 11 | 05, 09 | Hands-on |
| D1-11 | Monitor data ingestion quality, search index health, and relevance performance | 7, 13 | 05, 11 | Hands-on |
| D1-12 | Configure security, including managed identity, private networking, keyless credentials, and role policies | 2, 12 | 01, 10 | Hands-on (keyless, RBAC), Design (private networking) |
| D1-13 | Configure safety filters, guardrails, risk detection, and content moderation | 5, 18 | 04, 16 | Hands-on |
| D1-14 | Apply responsible AI instrumentation, including evaluators, safety evaluations, and explanation tooling | 5, 11 | 04, 09 | Hands-on |
| D1-15 | Implement auditing through trace logging, provenance metadata, and approval workflows | 10, 11, 12 | 08, 09, 10 | Hands-on |
| D1-16 | Govern agent behavior with oversight modes, constraints, and tool-access controls | 9, 10, 18 | 07, 08, 16 | Hands-on |

## D2 Implement generative AI and agentic solutions (30-35%)

| ID | Objective (study guide wording) | Days | Labs | Depth |
|---|---|---|---|---|
| D2-01 | Deploy and consume LLMs, small models, code models, and multimodal models | 2, 3, 4 | 01-03 | Hands-on |
| D2-02 | Implement retrieval-augmented generation (RAG) in an application | 6, 7 | 05 | Hands-on |
| D2-03 | Design workflows, tool-augmented flows, and multistep reasoning pipelines | 4, 8, 10 | 03, 06, 08 | Hands-on |
| D2-04 | Evaluate models and apps, including detecting fabrications, relevance, quality, and safety | 5, 7, 11 | 04, 05, 09 | Hands-on |
| D2-05 | Integrate generative workflows into applications by using Foundry SDKs and connectors | 2, 8 | 01, 06 | Hands-on |
| D2-06 | Configure an application to connect to a Foundry project | 2 | 01 | Hands-on |
| D2-07 | Define agent roles, goals, conversation-tracking approach, and tool schemas | 8 | 06 | Hands-on |
| D2-08 | Build agents that integrate retrieval, function-calling, and conversation memory | 8, 9 | 06, 07 | Hands-on |
| D2-09 | Integrate agent tools, including APIs, knowledge stores, search, content understanding, and custom functions | 9, 13 | 07, 11 | Hands-on |
| D2-10 | Implement orchestrated multi-agent solutions | 10 | 08 | Hands-on |
| D2-11 | Build autonomous or semiautonomous workflows with safeguards and approval flow controls | 10, 18 | 08, 16 | Hands-on |
| D2-12 | Integrate monitoring into deployed agents, evaluate agent behavior, and perform error analysis | 11 | 09 | Hands-on |
| D2-13 | Tune generation behavior, such as prompt engineering and adjusting model parameters | 4, 16 | 03, 14 | Hands-on |
| D2-14 | Implement model reflection, chain-of-thought evaluations, and self-critique loops | 4 | 03 | Hands-on |
| D2-15 | Set up observability by implementing tracing, token analytics, safety signals, and latency breakdowns | 11 | 09 | Hands-on |
| D2-16 | Orchestrate multiple models, flows, or hybrid LLM and rules engines | 10, 18 | 08, 16 | Hands-on |

## D3 Implement computer vision solutions (10-15%)

| ID | Objective (study guide wording) | Days | Labs | Depth |
|---|---|---|---|---|
| D3-01 | Implement a solution that generates images from text prompts and reference media | 15 | 13 | Hands-on |
| D3-02 | Implement a solution that generates videos from text prompts and reference media | 15 | 13 | Concept (optional demo, see cost note) |
| D3-03 | Configure image-editing workflows, including inpainting, mask-based edits, and prompt-driven modifications | 15 | 13 | Hands-on |
| D3-04 | Implement workflows to edit generated videos | 15 | 13 | Concept |
| D3-05 | Select and apply appropriate generation and editing controls provided by the platform | 15 | 13 | Hands-on (image), Concept (video) |
| D3-06 | Build a solution that analyzes visual context by using multimodal models | 14 | 12 | Hands-on |
| D3-07 | Configure apps to produce concise or detailed captions for single or multiple images | 14 | 12 | Hands-on |
| D3-08 | Implement a solution that enables question-answering grounded in visual evidence | 14 | 12 | Hands-on |
| D3-09 | Configure generation of alt-text and extended image descriptions aligned to accessibility guidelines | 14 | 12 | Hands-on |
| D3-10 | Implement visual understanding by configuring Azure Content Understanding in Foundry Tools to extract visual characteristics | 14, 13 | 12, 11 | Hands-on |
| D3-11 | Implement video analysis workflows to process and interpret video segments | 14 | 12 | Hands-on (short clip) or Concept |
| D3-12 | Configure single-task and pro-mode Content Understanding pipelines | 14, 13 | 12, 11 | Design plus Hands-on (single-task) |
| D3-13 | Implement solutions that identify objects, components, or regions within images or video | 14 | 12 | Hands-on |
| D3-14 | Implement filters to classify unsafe or disallowed visual content | 14, 5 | 12, 04 | Hands-on |
| D3-15 | Detect and mitigate indirect prompt injection by using embedded text in images | 14, 18 | 12, 16 | Hands-on |
| D3-16 | Enforce visual policy rules, such as applying watermarks, flagging prohibited symbols, upholding brand usage requirements, and detecting potentially inappropriate content | 14, 15 | 12, 13 | Hands-on (rule check), Design (watermark) |

## D4 Implement text analysis solutions (10-15%)

| ID | Objective (study guide wording) | Days | Labs | Depth |
|---|---|---|---|---|
| D4-01 | Implement solutions to extract entities, topics, summaries, and structured JSON outputs by using generative prompting and Foundry Tools | 16, 4 | 14, 03 | Hands-on |
| D4-02 | Configure detection of sentiment, tone, safety issues, and sensitive content | 16 | 14 | Hands-on |
| D4-03 | Build solutions that translate text by using Azure Translator in Foundry Tools or LLM-powered translation flows | 16 | 14 | Hands-on |
| D4-04 | Customize language model outputs for domain tasks, such as compliance summarization and domain extraction | 16 | 14 | Hands-on |
| D4-05 | Implement workflows to convert speech to text and text to speech for agentic interactions | 17 | 15 | Hands-on |
| D4-06 | Integrate speech as an agent modality, including custom speech models | 17 | 15 | Hands-on (pipeline), Design (custom speech) |
| D4-07 | Enable multimodal reasoning from audio inputs | 17 | 15 | Hands-on or Concept (model access) |
| D4-08 | Translate speech into other languages by using language models and Foundry Tools | 17 | 15 | Hands-on |

## D5 Implement information extraction solutions (10-15%)

| ID | Objective (study guide wording) | Days | Labs | Depth |
|---|---|---|---|---|
| D5-01 | Ingest and index content, such as documents, images, audio, and video | 6, 13 | 05, 11 | Hands-on (documents), Design (audio/video) |
| D5-02 | Configure semantic search, hybrid search, and vector search for grounding | 6, 7 | 05 | Hands-on |
| D5-03 | Implement enrichment by using custom or built-in skills for text, images, and layout | 13, 6 | 11, 05 | Design plus Hands-on (one skill) |
| D5-04 | Configure RAG ingestion flow, including documents and using optical character recognition (OCR) | 13 | 11 | Hands-on |
| D5-05 | Connect retrieval pipelines directly to workflows and agent tools | 9 | 07 | Hands-on |
| D5-06 | Extract information by using multimodal pipelines that combine OCR, layout analysis, and field extraction | 13 | 11 | Hands-on |
| D5-07 | Produce clean, grounded representations to use with agents and RAG by using Content Understanding | 13 | 11 | Hands-on |
| D5-08 | Implement analyzers for generating structured or markdown outputs for downstream reasoning by using Content Understanding | 13 | 11 | Hands-on |

## Topics outside the named bullets

| Topic | Label | Day | Why it is in the plan |
|---|---|---|---|
| Microsoft Agent Framework (agents, tools, sessions, orchestrations) | Supporting Knowledge, AI-500 Foundation | 10 | The guide says "Build agents by using Foundry" and does not name it, but the official AI-103T00 course includes Agent Framework modules and AI-500 names it |
| Model Context Protocol (MCP) tools | Supporting Knowledge, AI-500 Foundation | 9 | Official course module on connecting agents to MCP tools |
| Agent2Agent (A2A) | Optional, AI-500 Foundation | 10 (reading) | Official course module; no hands-on |
| Foundry IQ / agentic retrieval | Supporting Knowledge | 9 | Maps to D1-02/D1-04 reasoning about knowledge integration |
| Microsoft 365 integration, Voice Live agents, hosted agents | Optional | 10, 17 (reading) | Appear in official training; cost and access heavy |
| Python async/await, typing, venvs | Supporting Knowledge | 4, 10 | Required for the SDK and Agent Framework code |
| LangGraph, other frameworks | Optional, AI-500 Foundation | 21 (reading) | AI-500 audience profile mentions it |

Official course used for module selection: <https://learn.microsoft.com/en-us/training/courses/ai-103t00/>. Treat the course as a learning source, not as the exam outline; the study guide is authoritative.
