# Glossary

Terms are grouped by topic. ".NET:" gives a rough analogy; analogies are approximate.

## Platform

| Term | Meaning |
|---|---|
| Microsoft Foundry | Azure's platform for building AI apps and agents: models, agents, evaluations, guardrails, tracing |
| Foundry resource | The Azure resource (AI Services kind) that holds model deployments and project(s). .NET: like a storage account that exposes several APIs |
| Foundry project | A workspace under the resource that groups agents, files, connections, evaluations. Has its own endpoint |
| Project endpoint | `https://<resource>.services.ai.azure.com/api/projects/<project>`; the one URL `AIProjectClient` needs |
| Deployment | A named instance of a model you call by name (not by model id). .NET: a registered service with a name |
| Deployment type | Global / Data Zone / Regional Standard, Provisioned, Batch etc.; controls data location, throughput and pricing model |
| TPM / RPM | Tokens per minute / requests per minute rate limits on a deployment (quota is per subscription, region and model) |
| Foundry Tools | Collective name used in the study guide for service APIs such as Vision, Language, Speech, Translator, Content Understanding, Document Intelligence |
| Responses API | OpenAI-style API used by Foundry (`responses.create`) for text, tools and conversations |
| Prompt agent | A Foundry agent defined by model, instructions and tools, stored as a versioned definition |
| Hosted agent | Code you containerize or package (for example with Agent Framework) and run in Foundry |
| Microsoft Agent Framework (MAF) | Open-source SDK (`agent-framework`) for building agents and multi-agent workflows in Python/.NET |
| MCP | Model Context Protocol: an open protocol for exposing tools and data to agents |
| A2A | Agent2Agent protocol: agents discovering and calling each other |
| Toolbox | Foundry's catalog of built-in agent tools (for example web search, file search, code interpreter, MCP) |
| Foundry IQ / agentic retrieval | Knowledge-base style retrieval where a model plans sub-queries over Azure AI Search sources |

## Identity and security

| Term | Meaning |
|---|---|
| Entra ID | Azure identity provider. .NET: Azure AD / Microsoft identity platform |
| Keyless / token auth | Calling Azure services with an Entra token instead of an API key |
| `DefaultAzureCredential` | Credential chain (env, managed identity, Azure CLI, ...). Convenient locally; prefer a specific credential in production |
| Managed identity | An Entra identity attached to an Azure resource; no secret to store |
| RBAC | Role-based access control; you need a **data-plane** role (for example Cognitive Services User, Search Index Data Contributor) to call APIs, not only Owner |
| Private endpoint / private link | Gives a service a private IP in your VNet and lets you disable public access |
| Prompt injection (direct / indirect) | Instructions hidden in user input (direct) or in retrieved documents/images (indirect, XPIA) that try to hijack the model |
| Prompt Shields | Content Safety feature that detects prompt-attack patterns |
| Guardrails / content filters | Configurable risk detection applied to model inputs and outputs in Foundry |

## Retrieval

| Term | Meaning |
|---|---|
| RAG | Retrieval-augmented generation: fetch relevant content, put it in the prompt, answer with citations |
| Chunk | A slice of a document (typically hundreds of tokens) stored as one search record |
| Embedding | Numeric vector representing meaning; compared with cosine similarity |
| Vector / keyword / hybrid search | Similarity on embeddings / BM25 text match / both fused (RRF) |
| Semantic ranker | A re-ranking model in Azure AI Search that reorders top results by meaning |
| HNSW | Approximate nearest neighbor index used for vector search |
| Skillset / indexer | Azure AI Search pipeline pieces: indexer pulls data, skillset enriches (OCR, split, embed) |
| Grounding | Constraining answers to supplied evidence |
| Groundedness | Evaluator score: does the answer stay within the retrieved context |

## Evaluation and operations

| Term | Meaning |
|---|---|
| Evaluator | Scorer for outputs (groundedness, relevance, coherence, fluency, safety, tool call accuracy, ...) |
| Trace / span | One operation in a request path (OpenTelemetry). .NET: `Activity` |
| OpenTelemetry (OTel) | Vendor-neutral telemetry standard; exported to Application Insights |
| Drift | Quality or behavior changes over time as inputs, data or models change |
| Red teaming | Deliberately attacking your system to find failures |
| Human-in-the-loop (HITL) / approval | A person approves risky tool calls before they run |

## Python for .NET developers

| Term | .NET analogy |
|---|---|
| venv (`.venv`) | Per-project NuGet restore + SDK pin |
| `pip` / `uv` | NuGet / dotnet tool; `uv` is a faster pip |
| `requirements.txt` | `PackageReference` list |
| `.env` + `python-dotenv` | `appsettings.Development.json` / user secrets |
| Type hints | Static types, but not enforced at runtime |
| `pydantic.BaseModel` | A DTO with validation and JSON schema generation |
| `async def` / `await` | `async Task` / `await`; but you must start the loop with `asyncio.run(...)` |
| `Annotated[str, Field(description=...)]` | Attribute with metadata on a parameter |
| Decorator (`@tool`) | Attribute plus wrapper in one |
| Context manager (`with`) | `using` |
