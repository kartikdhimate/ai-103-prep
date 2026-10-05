# KnowledgeDesk CLI: Security

## Principles

1. Keyless by default; exceptions are registered below with a reason and an exit plan.
2. Least privilege: separate roles per identity and narrow scopes.
3. All external content is untrusted: user text, documents, images, audio transcripts, tool results, MCP descriptions.
4. Fail closed when a safety check cannot run.
5. Log decisions, not content.

Diagram: see "Authentication and security flow" in [ARCHITECTURE.md](ARCHITECTURE.md).

## Identity matrix (Day 12)

| Identity | Purpose | Roles | Scope | Notes |
|---|---|---|---|---|
| Developer (you) | Local runs | Azure AI User (confirm name), Cognitive Services User, Search Service Contributor, Search Index Data Contributor/Reader | Resource group | `az login` |
| App (managed identity, target) | Production calls | Only the data-plane roles it needs | Each resource | No Owner/Contributor |
| CI (federated identity, target) | Evaluation and deploy | Model access for evals; deploy rights on app only | Resource group / app | OIDC, no stored secrets |
| Evaluator | Offline scoring | Model access | Foundry resource | Same as CI |

## Key and secret exceptions register

| Service | Why a key is used | Where stored | Exit plan |
|---|---|---|---|
| Azure AI Translator | Lab uses key plus region on the global endpoint | `.env` | Evaluate Entra options in docs |
| Azure AI Speech | SDK lab uses key | `.env` | Use token-based auth with resource ID |
| AI Search (only if Free tier RBAC unavailable) | Fallback | `.env` | Move to RBAC on a paid tier |

## Tool governance (Day 9)

| Tool | Risk | Approval | Max calls per conversation | Allowed inputs | Logged fields |
|---|---|---|---|---|---|
| `search_knowledge` | read | no | 5 | query string | tool, query digest, count |
| `get_ticket_status` | read | no | 5 | ticket ID format | tool, ID |
| `create_ticket` | write | yes | 1 | summary, urgency 1-5 | tool, decision |
| `extract_invoice` | read | no | 3 | files in `data/docs_raw` only | tool, file name, size |
| MCP documentation tool | external read | yes | 3 | allowed tools only | tool, decision |

## Logging rules (Day 11)

Allowed: timestamps, tool names, decisions, token counts, latency, document IDs, evaluator scores, category and severity of blocks. Forbidden: raw prompts or responses by default, PII, secrets, full documents, images, audio. Sensitive-data capture in telemetry stays off.

## Threat model (Day 18)

| Asset | Entry point | Abuse case | Control | Residual risk |
|---|---|---|---|---|
| Ticket store | Agent tool | Unauthorized or repeated writes | Approval, call cap, audit | User approves a malicious request |
| Documents | Retrieved chunks | Indirect injection | Document check, delimiters, policy | Novel phrasing |
| Budget | CLI input | Huge inputs, loops | Input cap, token guard, step limit | Provider-side cost lag |
| Secrets | Prompts, logs | Extraction attempts | No secrets in prompts, log rules | Misconfiguration |
| Users | Images and audio | Embedded instructions | OCR and transcript checks | Adversarial perturbations |

## Responsible AI checklist

- [ ] Guardrail configured on the deployment and tested.
- [ ] Prompt-attack checks on prompts and documents.
- [ ] Output checks and refusal templates.
- [ ] Evaluation of groundedness and safety on a regular sample.
- [ ] Human approval for write actions.
- [ ] Provenance recorded for every answer.
- [ ] AI-generated images are watermarked.
