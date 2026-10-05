# Lab 03: Prompting, Structured Output, Self-Critique and Async

Full steps: [Day 4](../week-01/day-04.md).

## 1. Scenario
Support tickets arrive as free text. You must classify them into a typed object, improve summaries with a bounded critique loop, and run calls concurrently.

## 2. Objectives
Write structured instructions; parse into a Pydantic model; implement generate-critique-revise with limits; demonstrate async concurrency; observe parameter support differences.

## 3. AI-103 objectives
D2-13, D2-14, D2-03, D2-01, D4-01.

## 4. Prerequisites
[Lab 02](lab-02-model-comparison-and-cost.md).

## 5. Services
Foundry model deployment (Responses API).

## 6. SDKs
`openai`, `pydantic`, standard library `asyncio`.

## 7. Duration
75 minutes.

## 8. Resources
None.

## 9. Cost and risk
About EUR 0.20. Risk: unbounded critique loops.

## 10. Steps
Prompt variants; `responses.parse` with `Ticket`; critique loop with `Critique`; async gather demo; parameter experiment.

## 11. Expected result
Typed `Ticket` objects, critique log with scores, concurrency timing difference, notes on rejected parameters.

## 12. Validation
Object fields valid; loop ends within two revisions; gather about 1 s vs 3 s.

## 13. Break/fix
`temperature` on a reasoning model; out-of-schema value; missing `await`.

## 14. Common mistakes
Believing structured output guarantees correctness; forgetting `asyncio.run`; unbounded loops.

## 15. Troubleshooting
| Symptom | Check |
|---|---|
| Parameter rejected | Error text; model family rules |
| Parse fails | Schema and instructions; handle refusal |
| "coroutine never awaited" | Missing `await` |

## 16. Capstone relevance
M2: `prompts.py` and `structured.py`.

## 17. Cleanup
None.
