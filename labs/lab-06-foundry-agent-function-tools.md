# Lab 06: Foundry Agent with Function Tools

Full steps: [Day 8](../week-02/day-08.md).

## 1. Scenario
A support assistant must look up and create tickets by calling functions, remember a conversation, and be versioned for rollout.

## 2. Objectives
Define a prompt agent with instructions and function tools; implement the tool-call loop with a step limit; track conversation state; create and list agent versions.

## 3. AI-103 objectives
D2-07, D2-08, D2-03, D2-05, D1-04, D1-07.

## 4. Prerequisites
[Lab 05](lab-05-rag-ai-search.md) and wrappers from earlier labs.

## 5. Services
Foundry Agent Service (prompt agents), Responses API conversations.

## 6. SDKs
`azure-ai-projects` (models `PromptAgentDefinition`, `FunctionTool`), `openai`.

## 7. Duration
75 minutes.

## 8. Resources
Agent `kd-agent` (versions); local `out/tickets.json`.

## 9. Cost and risk
About EUR 0.30. Risk: runaway loops; tools with side effects without approval.

## 10. Steps
Write tools; define agent; run loop; test memory with a conversation ID; create second version; document the sequence.

## 11. Expected result
Status question uses the status tool; create request writes a ticket; a new conversation forgets earlier context; multiple versions listed.

## 12. Validation
See Day 8 section 11.

## 13. Break/fix
Schema mismatch; forced error loop; tool-choice error caused by a vague description.

## 14. Common mistakes
Missing `required`; returning exceptions instead of errors to the model; unlimited loop; relying on prose to restrict write tools.

## 15. Troubleshooting
| Symptom | Check |
|---|---|
| Tool never called | Description and instructions |
| Arguments invalid | Schema and `strict` setting |
| Agent client call fails | Quickstart for current call shape (`agent_name`, conversation) |

## 16. Capstone relevance
M6 part 1: agent and loop.

## 17. Cleanup
Delete extra versions if desired; keep the agent.
