# Lab 14: Text Analysis and Translation

Full steps: [Day 16](../week-03/day-16.md).

## 1. Scenario
Customer emails and compliance notes must be analyzed for sentiment, entities, PII and risk, and translated for regional teams.

## 2. Objectives
Use the Language service and an LLM for analysis and compare; redact PII before generation; build a domain compliance summarizer; translate with Translator and an LLM and compare.

## 3. AI-103 objectives
D4-01, D4-02, D4-03, D4-04, D2-13.

## 4. Prerequisites
[Lab 13](lab-13-image-generation-and-editing.md) (or skip if no image model); [Lab 03](lab-03-prompting-and-structured-output.md).

## 5. Services
Azure AI Language, Azure AI Translator (F0), Foundry model.

## 6. SDKs
`azure-ai-textanalytics`, `azure-ai-translation-text` (`to_language` parameter), `openai`, `pydantic`.

## 7. Duration
75 minutes.

## 8. Resources
Language resource; Translator F0.

## 9. Cost and risk
About EUR 0.20. Risks: PII leaking into prompts or logs; Translator key handling (documented exception).

## 10. Steps
Create resources; Language SDK calls; LLM structured analysis; compliance summarizer; translation comparison.

## 11. Expected result
Sentiment and redacted text; comparison table; scored compliance summaries; translation comparison.

## 12. Validation
See Day 16 section 11.

## 13. Break/fix
PII to model; oversized input; Translator auth error.

## 14. Common mistakes
Redacting after generation; ignoring document size limits; using the old `to` parameter name; storing the Translator key in code.

## 15. Troubleshooting
| Symptom | Check |
|---|---|
| 401 from Translator | Key, region header, endpoint |
| Language SDK 403 | Role and endpoint form |
| Poor translation of domain terms | Glossary in the LLM prompt |

## 16. Capstone relevance
M12 part 1: `kd analyze` command.

## 17. Cleanup
Keep F0 resources until Day 21.
