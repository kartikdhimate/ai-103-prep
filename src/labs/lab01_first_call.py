from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential

from common.config import require
from common.cost_guard import record_tokens

project_client = AIProjectClient(
    endpoint=require("AZURE_AI_PROJECT_ENDPOINT"),
    credential=DefaultAzureCredential(),
)

openai_client = project_client.get_openai_client()

response = openai_client.responses.create(
    model=require("AZURE_AI_MODEL_DEPLOYMENT"),
    input="In two sentences, what is a resource group in Azure?",
)

print(response.output_text)
print(f"Input tokens: {response.usage.input_tokens}, Output tokens: {response.usage.output_tokens}")
record_tokens(response.usage.total_tokens)