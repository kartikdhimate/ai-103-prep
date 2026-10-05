# Lab 11: Document Extraction (Document Intelligence, Content Understanding, Enrichment)

Full steps: [Day 13](../week-02/day-13.md).

## 1. Scenario
The corpus now includes invoices, a report with tables and scanned images. You must extract text, layout and fields reliably and index them for RAG.

## 2. Objectives
Run layout and invoice analysis; run Content Understanding analyzers and compare; ingest layout-aware chunks; handle low-confidence extraction; design a skillset pipeline; expose extraction as a governed tool.

## 3. AI-103 objectives
D5-01, D5-03, D5-04, D5-06, D5-07, D5-08, D2-09, D1-11, D3-10, D3-12.

## 4. Prerequisites
[Lab 10](lab-10-security-and-cicd.md); populated Search index.

## 5. Services
Azure AI Document Intelligence (F0), Azure Content Understanding (on the Foundry resource), Azure AI Search.

## 6. SDKs
`azure-ai-documentintelligence`, `azure-ai-contentunderstanding==1.1.0`, `azure-search-documents`.

## 7. Duration
270 minutes.

## 8. Resources
DI F0; default model mappings for Content Understanding; sample files (max 15 pages); optional temporary storage.

## 9. Cost and risk
About EUR 1.00 for Content Understanding. Risks: large files, F0 page limits, sensitive documents.

## 10. Steps
Resources and defaults; sample files with truth data; DI layout and invoice; CU analyzers; analyzer concepts; layout-aware ingestion; skillset design; extraction tool with policy.

## 11. Expected result
Markdown with tables; invoice fields with confidence; comparison table; new chunks retrievable; low-confidence documents flagged.

## 12. Validation
See Day 13 section 11.

## 13. Break/fix
Auth failure; degraded scan; page limit; missing CU defaults.

## 14. Common mistakes
Ignoring confidence; assuming F0 processes every page; sending real personal documents; unpinned CU package.

## 15. Troubleshooting
| Symptom | Check |
|---|---|
| 401/403 | Custom-subdomain endpoint, role |
| CU errors about models | Default model deployments mapped |
| Empty markdown | Output format parameter, file type |
| Pre-release API surprises | CU package pinned to 1.1.0 |

## 16. Capstone relevance
M10: document ingestion pipeline and extraction tool.

## 17. Cleanup
Delete temporary storage and sensitive samples; keep DI F0.
