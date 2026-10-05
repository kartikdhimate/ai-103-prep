# KnowledgeDesk CLI: Requirements

## Functional requirements

| ID | Requirement | Day | Objectives |
|---|---|---|---|
| FR-01 | The CLI authenticates with Entra ID (no model keys) | 2 | D1-12 |
| FR-02 | Answers to policy questions cite source documents and refuse when evidence is missing | 6-7 | D2-02 |
| FR-03 | Search supports keyword, vector, hybrid and semantic modes selectable by flag | 6 | D5-02 |
| FR-04 | Structured outputs for tickets and critiques validate against Pydantic models | 4 | D2-13 |
| FR-05 | Safety gate checks user input, retrieved documents, images and transcripts; it fails closed | 5, 14 | D1-13 |
| FR-06 | An agent can read ticket status and search; creating a ticket requires explicit approval | 8-10 | D2-11 |
| FR-07 | Tool calls are limited by an allowlist, per-tool call caps and an audit log | 9 | D1-16 |
| FR-08 | Documents (PDF, image) are converted to layout-aware chunks and indexed | 13 | D5-04 |
| FR-09 | Invoice extraction returns vendor, date, total and confidence; low confidence is flagged | 13 | D5-06 |
| FR-10 | Image questions run through safety and OCR-injection checks before the model | 14 | D3-15 |
| FR-11 | Text analysis redacts PII before generation and supports translation | 16 | D4-01 to D4-04 |
| FR-12 | Voice mode converts speech to text, answers, and returns synthesized speech | 17 | D4-05 |
| FR-13 | Every request emits a trace with token and latency attributes | 11 | D2-15 |
| FR-14 | Every answer has provenance metadata | 11 | D1-15 |
| FR-15 | Evaluation commands report retrieval, groundedness and agent tool accuracy | 7, 11 | D2-04 |

## Non-functional requirements

| ID | Requirement | Target |
|---|---|---|
| NFR-01 | Cost | Daily token budget enforced; total prep under EUR 25 |
| NFR-02 | Latency | Grounded answer p95 under 15 s (measure; adjust target to your results) |
| NFR-03 | Quality | Groundedness mean at or above 4 on the eval set; hit@4 at or above 0.8 |
| NFR-04 | Safety | Red-team attack success under 10%; over-refusal under 10% |
| NFR-05 | Privacy | No raw prompts, PII or secrets in telemetry or logs |
| NFR-06 | Reliability | Retry with backoff on 429; bounded loops |
| NFR-07 | Maintainability | Single config module; secrets only in `.env` |

## Supported inputs and limits

| Input | Supported | Limit used in this plan |
|---|---|---|
| Markdown/text | yes | 500 words per sample document |
| PDF | yes via layout | at most 5 pages per file (Free-tier limits and cost; verify service limits) |
| Images | PNG, JPEG | resize to max 1024 px; size limits per service docs |
| Audio | WAV (PCM) | short clips (under 30 s), stay under 60 minutes of recognition for the whole plan |
| Video | concept only | optional 30 s clip if budget allows |

## Out of scope

Web or mobile front ends, multi-tenant data isolation, fine-tuning, production deployment, real customer data.

## Acceptance

All FR rows have a passing check in [TESTING.md](TESTING.md); NFR targets measured and recorded; demo script from [TASKS.md](TASKS.md) runs end to end.
