# Resources

Status column: **200** = URL returned HTTP 200 on 2026-10-04 when this plan was built. **Catalog** = module slug returned by the Microsoft Learn catalog for the official AI-103T00 course. **Verify** = from memory of official material, not link-checked; search for the title if the link fails.
No third-party tutorials are listed; prefer official docs, and treat anything else with caution.

## Exam and policy

| Resource | Link | Status |
|---|---|---|
| AI-103 study guide (skills measured) | <https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-103> | 200 |
| Short link to the same guide | <https://aka.ms/AI103-StudyGuide> | Verify |
| Official course AI-103T00 | <https://learn.microsoft.com/en-us/training/courses/ai-103t00/> | Catalog |
| Exam sandbox (experience the interface) | <https://go.microsoft.com/fwlink/?linkid=2226877> | Verify |
| Retake policy | <https://learn.microsoft.com/en-us/credentials/support/retake-policy> | Verify |
| Exam duration and experience | <https://learn.microsoft.com/en-us/credentials/support/exam-duration-exam-experience> | Verify |
| Exam scoring reports | <https://learn.microsoft.com/en-us/credentials/certifications/exam-scoring-reports> | Verify |
| Practice assessment | Find it from the study guide page ("Practice Assessment" link) | Verify |
| AI-500 study guide | <https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500> | 200 |

## Official learning paths and modules (Microsoft Learn)

Base: `https://learn.microsoft.com/en-us/training/`. Paths are under `paths/<slug>/`, modules under `modules/<slug>/`.

| Path | Slug | Modules used by this plan (slug) |
|---|---|---|
| Develop generative AI apps | `develop-generative-ai-apps` | `prepare-azure-ai-development` (Day 1-2), `model-catalog-evaluate` (3), `foundry-sdk` (2), `use-generative-ai-tools` (4), `optimize-generative-ai-model-performance` (4, 7), `responsible-ai-studio` (5) |
| Develop AI agents on Azure | `develop-ai-agents-azure` | `develop-ai-agents-azure-vs-code` (8), `build-agent-with-custom-tools` (8), `connect-agent-to-mcp-tools` (9), `introduction-foundry-iq` (9), `build-agent-workflows-microsoft-foundry` (10), `develop-ai-agent-with-semantic-kernel` (10, content covers Agent Framework per catalog), `orchestrate-semantic-kernel-multi-agent-solution` (10), `discover-agents-with-a2a` (10 reading), `integrate-foundry-agent-with-m365` (optional) |
| Develop language solutions | `develop-language-solutions-azure-ai` | `analyze-text-ai-language` (16), `develop-text-analysis-agent-language-mcp` (16), `translate-text-speech` (17), `create-speech-enabled-apps` (17), `develop-generative-ai-audio-apps` (17), `develop-speech-agent-speech-mcp` (17 optional), `develop-voice-live-agent` (optional) |
| Insight from visual data | `insight-visual-data` | `develop-generative-ai-vision-apps` (14), `generate-images-azure-openai` (15), `generate-video-with-foundry` (15), `analyze-images-with-content-understanding` (14), `analyze-content-ai` (13), `analyze-content-ai-api` (13), `extract-data-with-document-intelligence` (13), `ai-knowldge-mining` (6, 13; the slug is spelled this way in the catalog) |

Module durations in the catalog range from about 33 to 131 minutes. This plan assigns **parts** of modules; do not try to complete every unit.

## Foundry and models

| Topic | Link | Status |
|---|---|---|
| Foundry documentation home | <https://learn.microsoft.com/en-us/azure/foundry/> | 200 |
| Install CLI and SDK (Python 3.10+) | <https://learn.microsoft.com/en-us/azure/foundry/how-to/develop/install-cli-sdk> | 200 |
| Responses API | <https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/responses> | 200 |
| Structured outputs | <https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/structured-outputs> | 200 |
| Embeddings | <https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/embeddings> | 200 |
| Deployment types | <https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/deployment-types> | 200 |
| Quotas and limits | <https://learn.microsoft.com/en-us/azure/foundry/openai/quotas-limits> | 200 |
| Vision-enabled chat | <https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/gpt-with-vision> | 200 |
| Image generation | <https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/dall-e> | 200 |
| Role-based access control | <https://learn.microsoft.com/en-us/azure/foundry/concepts/rbac-foundry> | 200 |
| Private link | <https://learn.microsoft.com/en-us/azure/foundry/how-to/configure-private-link> | 200 |
| Guardrails overview | <https://learn.microsoft.com/en-us/azure/foundry/guardrails/guardrails-overview> | 200 |
| Observability | <https://learn.microsoft.com/en-us/azure/foundry/concepts/observability> | 200 |
| Built-in evaluators | <https://learn.microsoft.com/en-us/azure/foundry/concepts/built-in-evaluators> | 200 |
| Python evaluation samples | <https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/ai/azure-ai-projects/samples/evaluations/README.md> | 200 |

## Agents

| Topic | Link | Status |
|---|---|---|
| Foundry agents overview | <https://learn.microsoft.com/en-us/azure/foundry/agents/overview> | 200 |
| Function calling tool | <https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/function-calling> | 200 |
| MCP tool | <https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/model-context-protocol> | 200 |
| Microsoft Agent Framework overview | <https://learn.microsoft.com/en-us/agent-framework/overview/> | 200 |
| Agent Framework agents | <https://learn.microsoft.com/en-us/agent-framework/agents/> | 200 |
| Function tools | <https://learn.microsoft.com/en-us/agent-framework/agents/tools/function-tools> | 200 |
| Workflows | <https://learn.microsoft.com/en-us/agent-framework/workflows/> | 200 |
| Agent Framework repository | <https://github.com/microsoft/agent-framework> | 200 |
| Model Context Protocol | <https://modelcontextprotocol.io> | 200 |
| Lab repo (agents) | <https://github.com/MicrosoftLearning/mslearn-ai-agents> | 200 |

## Search and extraction

| Topic | Link | Status |
|---|---|---|
| What is Azure AI Search | <https://learn.microsoft.com/en-us/azure/search/search-what-is-azure-search> | 200 |
| Vector search | <https://learn.microsoft.com/en-us/azure/search/vector-search-overview> | 200 |
| Hybrid search | <https://learn.microsoft.com/en-us/azure/search/hybrid-search-overview> | 200 |
| Semantic ranking | <https://learn.microsoft.com/en-us/azure/search/semantic-search-overview> | 200 |
| Agentic retrieval | <https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-overview> | 200 |
| Skills and enrichment | <https://learn.microsoft.com/en-us/azure/search/cognitive-search-concept-intro> | 200 |
| Document layout skill | <https://learn.microsoft.com/en-us/azure/search/cognitive-search-skill-document-intelligence-layout> | 200 |
| Service limits (Free tier) | <https://learn.microsoft.com/en-us/azure/search/search-limits-quotas-capacity> | 200 |
| Search security overview | <https://learn.microsoft.com/en-us/azure/search/search-security-overview> | 200 |
| Search RBAC | <https://learn.microsoft.com/en-us/azure/search/search-security-rbac> | 200 |
| Document Intelligence overview | <https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/overview> | 200 |
| Layout model | <https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/prebuilt/layout> | 200 |
| Content Understanding overview | <https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/overview> | 200 |
| CU documents / images / video | `.../content-understanding/document/overview`, `.../image/overview`, `.../video/overview` (same base as above) | 200 |
| CU prebuilt analyzers | <https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/concepts/prebuilt-analyzers> | 200 |
| CU analyzer reference | <https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/concepts/analyzer-reference> | 200 |
| CU REST quickstart | <https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/quickstart/use-rest-api> | 200 |
| CU pricing explainer | <https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/pricing-explainer> | 200 |
| Search + OpenAI sample app | <https://github.com/Azure-Samples/azure-search-openai-demo> | 200 |
| Search Python samples | <https://github.com/Azure-Samples/azure-search-python-samples> | 200 |
| Lab repo (information extraction) | <https://github.com/MicrosoftLearning/mslearn-ai-information-extraction> | 200 |

## Safety, language, speech, vision

| Topic | Link | Status |
|---|---|---|
| Content Safety overview | <https://learn.microsoft.com/en-us/azure/ai-services/content-safety/overview> | 200 |
| Text quickstart | <https://learn.microsoft.com/en-us/azure/ai-services/content-safety/quickstart-text> | 200 |
| Harm categories | <https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/harm-categories> | 200 |
| Jailbreak / prompt attack detection | <https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection> | 200 |
| Language service | <https://learn.microsoft.com/en-us/azure/ai-services/language-service/overview> | 200 |
| Sentiment | <https://learn.microsoft.com/en-us/azure/ai-services/language-service/sentiment-opinion-mining/overview> | 200 |
| PII detection | <https://learn.microsoft.com/en-us/azure/ai-services/language-service/personally-identifiable-information/overview> | 200 |
| Translator text translation | <https://learn.microsoft.com/en-us/azure/ai-services/translator/text-translation/overview> | 200 |
| Speech overview | <https://learn.microsoft.com/en-us/azure/ai-services/speech-service/overview> | 200 |
| Speech to text quickstart | <https://learn.microsoft.com/en-us/azure/ai-services/speech-service/get-started-speech-to-text> | 200 |
| Text to speech quickstart | <https://learn.microsoft.com/en-us/azure/ai-services/speech-service/get-started-text-to-speech> | 200 |
| Speech translation | <https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-translation> | 200 |
| Custom speech | <https://learn.microsoft.com/en-us/azure/ai-services/speech-service/custom-speech-overview> | 200 |
| Authentication for AI services | <https://learn.microsoft.com/en-us/azure/ai-services/authentication> | 200 |
| Lab repo (language) | <https://github.com/MicrosoftLearning/mslearn-ai-language> | 200 |
| Lab repo (vision) | <https://github.com/MicrosoftLearning/mslearn-ai-vision> | 200 |

## Azure platform and Python

| Topic | Link | Status |
|---|---|---|
| Install Azure CLI on Windows | <https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-windows> | 200 |
| Azure SDK for Python authentication | <https://learn.microsoft.com/en-us/azure/developer/python/sdk/authentication/overview> | 200 |
| Azure RBAC overview | <https://learn.microsoft.com/en-us/azure/role-based-access-control/overview> | 200 |
| Create budgets | <https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets> | 200 |
| Azure Monitor OpenTelemetry | <https://learn.microsoft.com/en-us/azure/azure-monitor/app/opentelemetry-enable> | 200 |
| Key Vault overview | <https://learn.microsoft.com/en-us/azure/key-vault/general/overview> | 200 |
| Azure SDK Python version policy | <https://github.com/Azure/azure-sdk-for-python/blob/main/doc/python_version_support_policy.md> | 200 |

## Pricing pages (read, then confirm in your portal)

| Service | Link | Status |
|---|---|---|
| Azure OpenAI / model pricing | <https://azure.microsoft.com/en-us/pricing/details/azure-openai/> | 200 |
| AI Search | <https://azure.microsoft.com/en-us/pricing/details/search/> | 200 |
| Document Intelligence | <https://azure.microsoft.com/en-us/pricing/details/ai-document-intelligence/> | 200 |
| Speech | <https://azure.microsoft.com/en-us/pricing/details/cognitive-services/speech-services/> | 200 |
| Translator | <https://azure.microsoft.com/en-us/pricing/details/cognitive-services/translator/> | 200 |
| Content Safety | <https://azure.microsoft.com/en-us/pricing/details/cognitive-services/content-safety/> | Verify (read earlier, timed out in the bulk check) |

## Python for a .NET developer (official)

Use the official Python tutorial (<https://docs.python.org/3/tutorial/>) and the `asyncio` docs (<https://docs.python.org/3/library/asyncio.html>) for reference; Day 4 gives the C# mapping you need. Both are standard documentation pages, not link-checked here.
