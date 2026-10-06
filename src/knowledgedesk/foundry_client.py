from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential

from common.config import require
from common.cost_guard import record_tokens

def get_clients():
    project_client = AIProjectClient(
        credential=DefaultAzureCredential(),
        endpoint=require("AZURE_AI_PROJECT_ENDPOINT")
    )

    return project_client, project_client.get_openai_client()

def ask(openai_client, text: str, instructions: str | None = None) -> str:
    response = openai_client.responses.create(
        model=require("AZURE_AI_MODEL_DEPLOYMENT"),
        input=text,
        instructions=instructions
    )

    record_tokens(response.usage.total_tokens)
    return response.output_text