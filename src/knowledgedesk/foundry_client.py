from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import OpenAI

from common.config import require
from common.cost_guard import record_tokens
from common.retry import call_with_retry

def get_clients():
    project_client = AIProjectClient(
        credential=DefaultAzureCredential(),
        endpoint=require("AZURE_AI_PROJECT_ENDPOINT")
    )

    return project_client, project_client.get_openai_client()

def get_openai_client():
    openai_endpoint = require("AZURE_OPENAI_ENDPOINT")

    credential = DefaultAzureCredential()

    token_provider = get_bearer_token_provider(
        credential,
        "https://ai.azure.com/.default",
    )

    client = OpenAI(
        base_url=openai_endpoint,
        api_key=token_provider,
    )

    return client

def ask(openai_client, text: str, instructions: str | None = None) -> str:
    response = call_with_retry(lambda: openai_client.responses.create(
        model=require("AZURE_AI_MODEL_DEPLOYMENT"),
        input=text,
        instructions=instructions
    ))

    record_tokens(response.usage.total_tokens)
    return response.output_text