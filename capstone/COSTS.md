# KnowledgeDesk CLI: Costs

Numbers are planning estimates; confirm prices in the portal and Cost Management. Budget rules and the per-resource table are in [COST_TRACKER.md](../COST_TRACKER.md).

## Unit cost model

Cost per request (USD) = $(\text{input tokens} \times P_{in} + \text{output tokens} \times P_{out}) / 10^6$ plus search and service calls.
Planning inputs seen on 2026-10-04: `gpt-5-mini` about $0.25 input and $2.00 output per 1M tokens; `text-embedding-3-small` about $0.022 per 1M tokens. Overwrite with the values you read.

| Request type | Typical input tokens | Typical output tokens | Model cost per 1,000 requests | Other cost |
|---|---|---|---|---|
| Grounded answer (4 chunks) | | | | Search: Free tier, EUR 0 |
| Ticket agent turn (2 tool steps) | | | | None |
| Image question | | | | Image tokens |
| Invoice extraction | | | | Document Intelligence F0 or Content Understanding pay-as-you-go |
| Voice turn | | | | Speech F0 (check minutes) |

Fill the token columns from your own `record_tokens` logs and traces on Days 7, 11 and 20.

## Capacity estimate (Day 12)

50 concurrent users, 1 request per minute each, 1,500 tokens per request: $50 \times 1500 = 75{,}000$ tokens per minute. Compare with the deployment's capacity and quota; decide standard with retry versus provisioned throughput, and what to cache.

| Item | Value |
|---|---|
| Peak TPM needed | |
| Deployment capacity | |
| Quota available | |
| Decision | |

## Cost controls implemented

| Control | Where | Day |
|---|---|---|
| Daily token budget | `common/cost_guard.py` | 1 |
| Retry with limits | `common/retry.py` | 3 |
| Input size cap | safety gate | 18 |
| Token-bucket rate limit | `common/rate_limit.py` | 12 |
| Image cap (10) | `imagegen.py` | 15 |
| Speech minutes cap (60) | `voice.py` | 17 |
| Log Analytics daily cap | Azure portal | 11 |
| Budget alerts | Cost Management | 1 |

## Actuals (fill on Days 7, 14, 20, 21)

| Date | Cumulative EUR | Biggest cost driver | Surprise |
|---|---|---|---|
| | | | |
