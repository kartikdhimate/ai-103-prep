# Lab 00: Setup and Compatibility Gate

Full steps: [Day 1](../week-01/day-01.md). This brief is the structured spec.

## 1. Scenario
You are starting a 21-day Azure AI project on a new machine with a EUR 10-25 budget. Before building anything you must prove the toolchain works and that spending is capped.

## 2. Objectives
Install and verify Azure CLI and Python 3.14; create the resource group and budget alerts; run the SDK compatibility gate; add a local token budget guard.

## 3. AI-103 objectives
D1-09 (cost footprint), D1-05 (infrastructure preparation).

## 4. Prerequisites
Microsoft account with an Azure subscription; Windows PowerShell; Python 3.14; git; VS Code.

## 5. Services
Azure Resource Manager, Cost Management. No AI services yet.

## 6. SDKs
Packages from `requirements-core.txt` and `requirements-extras.txt`, checked by `scripts/compat_check.py`.

## 7. Duration
75 minutes.

## 8. Resources
Resource group `rg-ai103-prep`; three budget alerts. Local: `.venv`, `.env`, `src/common/`.

## 9. Cost and risk
EUR 0. Risk: forgetting that budgets alert but do not stop spend; running scripts in the wrong interpreter.

## 10. Steps
1. Install and sign in with Azure CLI. 2. Create resource group. 3. Create budget with alerts. 4. Create `.venv` and install packages. 5. Run the compatibility gate. 6. Create the config and cost guard modules.

## 11. Expected result
`compat_check.py` reports Tier A packages as OK and a recorded status for each Tier B package; `record_tokens()` stops a script at the daily limit.

## 12. Validation
`az account show`, `az group show`, portal budget view, compat table, guard test (see Day 1, section 11).

## 13. Break/fix
Run without the venv (packages missing); set a tiny token budget and trip the guard.

## 14. Common mistakes
Not reopening the terminal after installing the CLI; using the wrong subscription; committing `.env`; assuming a failing Tier B import means the plan cannot continue.

## 15. Troubleshooting
| Symptom | Check |
|---|---|
| `az` not found | Reopen terminal; check PATH |
| `Activate.ps1` blocked | Execution policy for CurrentUser |
| Import failure on 3.14 | Create the `.venv313` or `.venv311` fallback for that package only |

## 16. Capstone relevance
M0: configuration and cost-guard foundation used by every later script.

## 17. Cleanup
Nothing billable to delete.
