# Lab 07: Agent Knowledge, MCP Tools and Tool-Access Policy

Full steps: [Day 9](../week-02/day-09.md).

## 1. Scenario
The assistant must answer policy questions from your index, optionally use a remote documentation tool, and never perform risky actions without approval.

## 2. Objectives
Add a search tool; enforce a code-level tool policy with approval, limits and audit; connect an MCP tool with approval; compare native search tool vs function wrapper.

## 3. AI-103 objectives
D2-08, D2-09, D5-05, D1-02, D1-04, D1-16.

## 4. Prerequisites
[Lab 06](lab-06-foundry-agent-function-tools.md); populated index.

## 5. Services
Foundry agents (function and MCP tools), Azure AI Search, a remote MCP server.

## 6. SDKs
`azure-ai-projects` (`MCPTool`, `FunctionTool`), `azure-search-documents`, `openai`.

## 7. Duration
75 minutes.

## 8. Resources
Updated `kd-agent` version; optional `kd-mcp-agent`; `out/audit.jsonl`.

## 9. Cost and risk
About EUR 0.40. Risks: untrusted MCP servers; tool-output injection.

## 10. Steps
Wrap retrieval as tool; update instructions; implement `authorize()`; wire audit log; create MCP agent with `require_approval`; compare native Search tool in the portal.

## 11. Expected result
Cited answers via search; approval prompt for `create_ticket`; MCP approve and reject paths work.

## 12. Validation
See Day 9 section 11.

## 13. Break/fix
Injected instruction in tool output; over-restrictive allowlist; MCP approval rejected.

## 14. Common mistakes
Policy only in prose; not logging denials; trusting MCP descriptions; not limiting tools with `allowed_tools`.

## 15. Troubleshooting
| Symptom | Check |
|---|---|
| Agent ignores search | Tool description and instructions |
| MCP call fails | Server URL, tool list, approval item shape |
| Policy blocks everything | `POLICY` keys vs tool names |

## 16. Capstone relevance
M6: agent with knowledge and governed tools.

## 17. Cleanup
Delete `kd-mcp-agent` if unused.
