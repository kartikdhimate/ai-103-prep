from azure.ai.contentsafety import ContentSafetyClient
from azure.ai.contentsafety.models import AnalyzeTextOptions
from azure.identity import DefaultAzureCredential

from common.config import require

client = ContentSafetyClient(require("CONTENT_SAFETY_ENDPOINT"), DefaultAzureCredential())
for text in ["Have a great day!", "I will hurt you badly."]:
    result = client.analyze_text(AnalyzeTextOptions(text=text))
    print(text, [(c.category, c.severity) for c in result.categories_analysis])
