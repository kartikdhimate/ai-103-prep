# Domain Review

Use on Days 19-21. Cover the right-hand column and answer from memory. Weights: D1 25-30%, D2 30-35%, D3 10-15%, D4 10-15%, D5 10-15%. Objective IDs are in [EXAM_OBJECTIVES.md](../EXAM_OBJECTIVES.md). Verify service names and limits on the live docs; products change.

## D1 Plan and manage an Azure AI solution

| Situation | Typical answer |
|---|---|
| Predictable high throughput and latency | Provisioned throughput deployment |
| Large offline job, cost matters, latency does not | Batch-style deployment |
| Data must stay in a geography | Data zone or regional deployment type |
| App on Azure should not hold secrets | Managed identity plus a data-plane role |
| CI pipeline must call Azure without secrets | OIDC federated workload identity |
| Block public access to a Foundry resource | Private endpoint, private DNS, disable public network access |
| 429 responses | Retry with backoff, raise capacity/quota, spread load, cache, smaller model |
| Cost overrun risk | Budget alerts, token limits, caching, smaller model, batch |
| Detect groundedness decline over time | Evaluators on sampled traffic with alerts |
| Index health | Document counts vs source, failed uploads, freshness, storage, zero-result rate |
| Restrict what an agent can do | Allowlist, least-privilege tools, approval for writes, limits, audit |
| Audit an answer later | Trace logs plus provenance metadata plus approval records |
| Content moderation | Guardrails/filters, Content Safety, prompt-attack detection |
| Which model | Match modality, reasoning need, latency, cost and region availability |

Traps: Owner is not a data-plane role; budgets alert but do not stop spend; model name is not deployment name; Free Search lacks private endpoints.

## D2 Implement generative AI and agentic solutions

| Situation | Typical answer |
|---|---|
| Answers from private documents | RAG with citations and refusal when evidence is missing |
| Model must call APIs | Function/tool calling with JSON-schema tools |
| Remember across turns | Conversation ID or session; long-term memory is a separate store |
| Guarantee JSON shape | Structured outputs with a schema (shape, not truth) |
| Reduce fabrication | Grounding, citations, refusal rule, evaluators, retrieval fixes |
| Improve drafts | Bounded generate-critique-revise loop |
| Find the slow step | Tracing with spans, latency breakdown |
| Several roles with different tools | Multi-agent orchestration (sequential, concurrent, handoff, group chat, magentic) |
| Pause before a risky tool | Tool approval mode and approval workflow |
| Cheap and predictable routing | Deterministic rules first, LLM for ambiguity |
| Evaluate agent behavior | Tool call accuracy, task adherence/completion, error analysis |
| Connect an app to Foundry | Project endpoint plus credential through the SDK |
| Tune generation | Prompt design, token limits, reasoning effort (reasoning models), sampling controls where supported |

Traps: structured output does not verify facts; more agents is not automatically better; tool policy must be in code.

## D3 Implement computer vision solutions

| Situation | Typical answer |
|---|---|
| Describe an image flexibly | Multimodal model |
| Boxes, tags, OCR at low cost | Image Analysis features |
| Fields and descriptions from images or video | Content Understanding analyzers |
| Edit only part of an image | Mask-based inpainting (transparent area marks the region) |
| Change the whole image by instruction | Prompt-only edit |
| Text to video | Asynchronous job; cost by duration/resolution; access may be gated |
| Alt text | Short, purposeful; extended description for complex images |
| Answers grounded in image | Require evidence; allow "not visible" |
| Injection hidden in an image | OCR the image, run prompt-attack checks on the text |
| Brand or symbol rules | Application policy checks (structured LLM check or classifier) |
| Mark generated images | Visible watermark plus provenance metadata |

Traps: embedded text is untrusted; generation guardrails do not enforce your brand rules.

## D4 Implement text analysis solutions

| Situation | Typical answer |
|---|---|
| Sentiment at scale, fixed output | Language service |
| Custom schema or domain wording | LLM with structured output and examples |
| Find and redact PII | Language PII detection before generation |
| Bulk translation | Translator service |
| Translation where tone and context matter | LLM translation with glossary |
| Speech to text, text to speech | Speech service |
| Domain vocabulary and accents | Custom speech (measure with word error rate) |
| Translate speech | Speech translation, or STT then translation then TTS |
| Reason over tone in audio | Audio-capable multimodal model (transcript loses tone) |
| Voice agent | Speech adapters around the same agent, safety on transcript |

Traps: redacting after generation; ignoring free-tier hour limits.

## D5 Implement information extraction solutions

| Situation | Typical answer |
|---|---|
| Exact codes and names | Keyword (BM25) |
| Meaning and paraphrase | Vector |
| Both | Hybrid (fusion) |
| Reorder top results by meaning | Semantic ranker |
| Multi-hop questions over sources | Agentic retrieval |
| OCR, layout, tables | Document Intelligence layout or Content Understanding |
| Standard forms | Prebuilt Document Intelligence models |
| Custom schema across mixed media | Content Understanding analyzers |
| Bulk enrichment into an index | Indexer plus skillset (layout, split, embed) |
| Clean markdown for agents | Layout/CU markdown output, chunk by headings |
| Low-confidence fields | Human review path, confidence thresholds |
| Index uploads fail silently | Inspect per-document results |

Traps: dimension mismatch; Free tier limits (size, indexes, skillsets); not checking page limits on F0.

## Scenario drill (answer before opening the details)

1. A bank requires that no key can ever leave the platform for model calls from an Azure-hosted API. What do you use?
2. A nightly job summarizes 5 million records and results are needed next morning at the lowest cost. Which deployment approach?
3. A deployment returns 429 at peak but is idle at night. Give two non-purchase mitigations and one purchase option.
4. A security team wants proof that a CI release did not reduce groundedness. What do you add to the pipeline?
5. Your agent can create tickets. How do you stop it creating them because a retrieved document said so?
6. Users report fluent but wrong answers with valid citations. Which layer first?
7. You need typed JSON from a model for downstream code. What do you configure and what must you still check?
8. Two specialists (research, writer) must hand off work. Which pattern, and when would you rather use a single agent?
9. A trace shows 8 seconds in one span. How do you find whether it is the model, the search or a tool?
10. A marketing app must change only the background of a product image. Which workflow?
11. A user uploads a screenshot containing hidden instructions. Where do you block it?
12. You need object locations (boxes) cheaply and repeatedly. Which service?
13. Generated images must be marked as AI-made. Which two measures?
14. Customer emails contain phone numbers; you want an LLM summary. In what order?
15. Regional teams need 2 million short strings translated consistently every month. Which service?
16. A call center bot must understand domain jargon better than the default recognizer. What do you evaluate?
17. Exact part numbers fail in your vector-only search. What changes?
18. Invoices come as scans, and totals sometimes read wrong. What do you add to the extraction pipeline?
19. A Free Search service must be reached privately from a VNet. Is that possible?
20. Which two settings help prevent a PDF pipeline from silently skipping pages on a free tier?

<details><summary>Answers</summary>

1. Managed identity with RBAC (Entra token), keys disabled. 2. Batch-style deployment type, small model, short prompts. 3. Retry with backoff and caching/queueing; purchase provisioned throughput or higher quota. 4. An evaluation gate with thresholds (groundedness, safety) in CI. 5. Treat tool results as untrusted, enforce approval and allowlist in code, check documents with prompt-attack detection. 6. Data layer (stale or wrong source), then retrieval/prompt. 7. Structured outputs with a schema; still validate content. 8. Sequential or handoff; single agent when one set of instructions and tools covers the task. 9. Inspect child spans and attributes (model call, search call, tool call). 10. Mask-based inpainting. 11. OCR the image, prompt-attack check on extracted text, before the model. 12. Image Analysis (objects). 13. Visible watermark and provenance metadata. 14. Detect and redact PII first, then summarize. 15. Translator service. 16. Custom speech and word error rate. 17. Hybrid search (keyword plus vector), possibly semantic ranking. 18. Confidence thresholds and a human review route (also better scans). 19. No, the Free tier does not support private endpoints. 20. Verify page limits on the tier and compare processed pages to the source page count, failing loudly on mismatch.

</details>
