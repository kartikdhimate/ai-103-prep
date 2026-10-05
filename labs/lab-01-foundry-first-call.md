# Lab 01: Foundry Project, Keyless Authentication and First Call

Full steps: [Day 2](../week-01/day-02.md).

## 1. Scenario
Your team needs a minimal Python client that calls a model in a Foundry project without any API key.

## 2. Objectives
Create a Foundry project and a `gpt-5-mini` deployment; assign a data-plane role; call the Responses API with `AIProjectClient` and `DefaultAzureCredential`; wrap it for reuse.

## 3. AI-103 objectives
D1-05, D1-07, D1-12, D2-01, D2-05, D2-06.

## 4. Prerequisites
[Lab 00](lab-00-setup-and-compat-gate.md) complete; role assignment rights on the resource.

## 5. Services
Microsoft Foundry (resource, project, model deployment), Entra ID, Azure RBAC.

## 6. SDKs
`azure-ai-projects` (2.x), `azure-identity`, `openai`, `python-dotenv`.

## 7. Duration
75 minutes.

## 8. Resources
Foundry resource and project; `gpt-5-mini` deployment (Global Standard, minimum capacity); role assignment.

## 9. Cost and risk
About EUR 0.10. Risks: over-provisioned capacity; leaving a key in `.env`; confusing deployment name with model name.

## 10. Steps
Create project; deploy model; assign role; set endpoint in `.env`; run first-call script; build `get_clients()` and `ask()`.

## 11. Expected result
A printed answer with token counts and recorded usage.

## 12. Validation
Script output; role assignment listing; no keys in files.

## 13. Break/fix
Remove the role (403); wrong deployment name (not found); wrong subscription.

## 14. Common mistakes
Owner role assumed to be enough; copying the wrong endpoint form; SDK 1.x examples used with 2.x.

## 15. Troubleshooting
| Symptom | Check |
|---|---|
| 401/403 | Data-plane role, wait a few minutes, `az account show` |
| Not found | Deployment name and project endpoint |
| Import errors | Venv active, `azure-ai-projects>=2.3.0` |

## 16. Capstone relevance
M1: `knowledgedesk/foundry_client.py` is the single entry point to models.

## 17. Cleanup
Keep project and deployment for later weeks.
