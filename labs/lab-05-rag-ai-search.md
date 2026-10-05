# Lab 05: RAG on Azure AI Search (Build and Measure)

Full steps: [Day 6](../week-01/day-06.md) (build) and [Day 7](../week-01/day-07.md) (measure).

## 1. Scenario
Employees ask policy questions about a document set. Answers must cite sources, refuse unknowns, and be measured for retrieval and grounding quality.

## 2. Objectives
Design an index with text, vector and semantic configuration; chunk, embed and upload; compare keyword, vector, hybrid and semantic search; produce cited answers; compute hit@k and MRR; run groundedness and relevance evaluators; build an index health report.

## 3. AI-103 objectives
D1-03, D1-10, D1-11, D2-02, D2-04, D5-01, D5-02, D5-03 (concept).

## 4. Prerequisites
[Lab 04](lab-04-safety-and-guardrails.md); embedding deployment; Search RBAC roles.

## 5. Services
Azure AI Search (Free), embedding model deployment, chat model, evaluators.

## 6. SDKs
`azure-search-documents`, `openai`, `azure-ai-evaluation`, `azure-identity`.

## 7. Duration
Day 6: 270 minutes. Day 7: 270 minutes.

## 8. Resources
Search service (Free), index `kd-chunks`, embedding deployment, 8 sample documents, 10 evaluation questions.

## 9. Cost and risk
About EUR 0.80 across both days. Risks: choosing a paid Search tier; re-embedding repeatedly; vector dimension mismatch; stale index data.

## 10. Steps
Create service and roles; deploy embeddings; create corpus and eval set; chunk; build index; ingest with result checks; query four modes; grounded answer; metrics; evaluators; health report; top-k experiment; monitoring design.

## 11. Expected result
Index populated; metrics table for four modes; answers with citations; evaluator scores; health report; written monitoring plan.

## 12. Validation
Document count matches chunk count; all uploads succeeded; unknown questions refused; hit@4 recorded for all modes.

## 13. Break/fix
Dimension mismatch; missing permission; chunk size 3000; stale data; weakened prompt hallucination; zero-result query.

## 14. Common mistakes
Not checking upload results; mixing embedding models; chunking without overlap; judging only by eyeballing answers.

## 15. Troubleshooting
| Symptom | Check |
|---|---|
| 403 on upload | `Search Index Data Contributor` role or key |
| Dimension error | Field dimensions (1536) vs model |
| Semantic query error | Semantic configuration name and tier support |
| Empty vector results | Embeddings stored; `fields` name; `k_nearest_neighbors` |

## 16. Capstone relevance
M4 and M5: the retrieval backbone and its evaluation set.

## 17. Cleanup
Delete experimental indexes; keep the main index; confirm Free tier.
