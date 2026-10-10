from azure.ai.evaluation import GroundednessEvaluator, AzureOpenAIModelConfiguration
from azure.identity import DefaultAzureCredential

from common.config import require

config = AzureOpenAIModelConfiguration(
    azure_endpoint=require("AZURE_AI_PROJECT_ENDPOINT").split("/api/projects/")[0],
    azure_deployment=require("AZURE_AI_MODEL_DEPLOYMENT")
)
groundness = GroundednessEvaluator(model_config=config, credential=DefaultAzureCredential(), is_reasoning_model=True)
context = "Azure AI Search Free tier allows 3 indexes and 50 MB of storage."
print(groundness(query="How many indexes on the Free tier?", context=context, response="Three indexes."))
print("-"*20)
print(groundness(query="How many indexes on the Free tier?", context=context, response="Ten indexes and unlimited storage."))