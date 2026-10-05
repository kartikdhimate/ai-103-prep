# Cost Tracker

Budget: **EUR 10-25 total**. Planning estimate: about EUR 8; expected range EUR 8-15 with mistakes; hard stop EUR 25.
All numbers below are planning estimates, not quotes. Prices change by region and date. Confirm the rate in the portal's pricing tier screen and in Cost Management before creating anything billable.

## Rules

1. Free tier first. Create every resource in **one resource group** (`rg-ai103-prep`) so one delete removes everything.
2. Create the budget alerts on [Day 1](week-01/day-01.md) before any other resource. Azure budgets send alerts; they do **not** stop spending.
3. Never create a billable AI Search tier (Basic and above). They bill hourly while they exist. Use Free only; the Basic exercise is a design discussion.
4. Models: deploy `gpt-5-mini` for chat and `text-embedding-3-small` for embeddings (cheapest sensible choices; confirm availability in your region). Set a deployment capacity (TPM) at the minimum that works.
5. Every script reads `DAILY_TOKEN_BUDGET` and stops when exceeded ([Day 1](week-01/day-01.md)).
6. Turn off or avoid Foundry playground evaluations unless the day asks for them; the study notes show they bill on consumption and may be on by default. Check the Foundry observability page: <https://learn.microsoft.com/en-us/azure/foundry/concepts/observability>.
7. After every day, fill the ledger at the bottom and delete anything marked "delete today".

## Alert plan

| Alert | Threshold | Action |
|---|---|---|
| Budget 1 | EUR 10 actual | Review the ledger; skip all Optional items |
| Budget 2 | EUR 15 actual | Stop Content Understanding, image and video work; read instead of run |
| Budget 3 | EUR 20 actual | Stop all non-essential calls; finish with free-tier resources only |
| Hard stop | EUR 25 | Delete the resource group (the exam does not require resources) |

Setup guide: <https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets>.

## Resource plan

| Resource | Tier | Created | Expected cost | Verified free-tier fact (2026-10-04, pricing pages) | Main risk | Delete when |
|---|---|---|---|---|---|---|
| Foundry resource and project | Standard, pay per use | Day 2 | EUR 0 standing | - | Forgotten deployments with big capacity | Day 21 |
| `gpt-5-mini` deployment | Global Standard | Day 2 | about EUR 2-4 total | Listed at $0.25 input / $2 output per 1M tokens (estimate) | Loops that retry forever; large prompts | Day 21 |
| `text-embedding-3-small` | Global Standard | Day 6 | under EUR 0.50 | Listed at about $0.022 per 1M tokens | Re-embedding the corpus repeatedly | Day 21 |
| Azure AI Search | **Free** | Day 6 | EUR 0 | Free: 1 per subscription, 50 MB, 3 indexes; may be removed after inactivity | Choosing Basic by accident | Day 21 |
| Content Safety | **F0** | Day 5 | EUR 0 | 5,000 text records/month; usage stops at the limit | Prompt Shields calls in loops | Day 21 |
| Document Intelligence | **F0** | Day 13 | EUR 0 | 500 pages/month free | F0 page limit on large PDFs | Day 21 |
| Content Understanding | Pay as you go | Day 13 | about EUR 1-2 | No free tier found; pricing explainer is linked in [RESOURCES](RESOURCES.md) | Large files, video; needs model deployments | Day 21 |
| Vision (Image Analysis) | F0 if shown, else minimal | Day 14 | EUR 0-0.2 | Not verified; check portal | Confusing F0 vs S1 | Day 21 |
| Language (Text Analytics) | F0 if shown | Day 16 | EUR 0-0.2 | Free tier not verified; check portal | Same | Day 21 |
| Translator | **F0** | Day 16 | EUR 0 | 2 million characters/month | - | Day 21 |
| Speech | **F0** | Day 17 | EUR 0 | 5 audio hours/month standard real-time STT | Batch is not covered by F0 | Day 21 |
| Image generation (`gpt-image-1-mini` or what you have access to) | Pay per token | Day 15 | EUR 0.5-1 | Listed image output at about $8 per 1M tokens (estimate) | Many high-quality large images | Day 21 |
| Video generation | Pay per use | Never by default | EUR 0 (concept only) | Price unit not verified | Cost and access | - |
| Application Insights and Log Analytics | Pay as you go | Day 11 | under EUR 0.50 | Not verified | Verbose traces with prompt content | Day 21 |
| Storage account (sample files) | Standard LRS | Day 13 | under EUR 0.10 | - | Leaving public access on | Day 21 |

## Expected spend by day (planning estimate)

| Day | Expected EUR | Day | Expected EUR | Day | Expected EUR |
|---|---|---|---|---|---|
| 1 | 0 | 8 | 0.3 | 15 | 1.0 |
| 2 | 0.1 | 9 | 0.4 | 16 | 0.2 |
| 3 | 0.3 | 10 | 0.5 | 17 | 0.3 |
| 4 | 0.2 | 11 | 0.7 | 18 | 0.5 |
| 5 | 0.2 | 12 | 0.1 | 19 | 0 |
| 6 | 0.3 | 13 | 1.0 | 20 | 0.5 |
| 7 | 0.5 | 14 | 1.0 | 21 | 0 |

Sum: about EUR 8.1.

## Ledger (fill in)

Read actuals in Azure Portal -> Cost Management -> Cost analysis, filtered to your resource group. Data can lag by hours.

| Day | Resources touched | Estimated EUR | Actual EUR | Cumulative EUR | Notes / surprises |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |
| 6 | | | | | |
| 7 | | | | | |
| 8 | | | | | |
| 9 | | | | | |
| 10 | | | | | |
| 11 | | | | | |
| 12 | | | | | |
| 13 | | | | | |
| 14 | | | | | |
| 15 | | | | | |
| 16 | | | | | |
| 17 | | | | | |
| 18 | | | | | |
| 19 | | | | | |
| 20 | | | | | |
| 21 | | | | | |

## Emergency deletion

```powershell
az group delete --name rg-ai103-prep --yes --no-wait
```

Deleting a Foundry/AI Services resource can leave it in a soft-deleted state that holds the name and quota; use the portal's purge option when you need the name back (check the current docs for the purge command).
