# Lab 15: Speech and Audio

Full steps: [Day 17](../week-03/day-17.md).

## 1. Scenario
A voice interface to the assistant: speech in, safe answer, speech out, with translation as an option.

## 2. Objectives
Synthesize and recognize speech; build a speech pipeline around the agent; translate speech; evaluate custom speech and audio reasoning options.

## 3. AI-103 objectives
D4-05, D4-06, D4-07, D4-08.

## 4. Prerequisites
[Lab 14](lab-14-text-analysis-and-translation.md); safety gate from [Lab 04](lab-04-safety-and-guardrails.md).

## 5. Services
Azure AI Speech (F0), Foundry agent or model.

## 6. SDKs
`azure-cognitiveservices-speech` (no declared Python versions; use `.venv313` if the Day 1 gate failed).

## 7. Duration
75 minutes.

## 8. Resources
Speech F0; local WAV files.

## 9. Cost and risk
EUR 0 to 0.30. Risks: exceeding the free recognition hours; storing voice recordings; key-based auth exception.

## 10. Steps
Create resource; TTS then STT; voice pipeline with latency table; speech translation; audio reasoning and custom speech notes.

## 11. Expected result
`hello.wav` recognized correctly; `reply.wav` from the pipeline; translation output; written notes.

## 12. Validation
See Day 17 section 11.

## 13. Break/fix
Bad audio; wrong region; free-tier minutes guard; transcript injection.

## 14. Common mistakes
Unsupported audio format; no safety check on the transcript; ignoring cancellation details; exceeding F0 quota unknowingly.

## 15. Troubleshooting
| Symptom | Check |
|---|---|
| `NoMatch` | Audio format and content |
| `Canceled` | `cancellation_details` for auth or region |
| Import error | Fallback `.venv313` |

## 16. Capstone relevance
M12 part 2: `kd voice` command.

## 17. Cleanup
Keep Speech F0 until Day 21; delete recordings if desired.
