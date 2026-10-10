from azure.ai.contentsafety import ContentSafetyClient
from azure.ai.contentsafety.models import AnalyzeTextOptions
from azure.identity import DefaultAzureCredential
import httpx

from common.config import require
from knowledgedesk.structured import Decision

def check_user_input(input: str) -> Decision:
    client = ContentSafetyClient(require("CONTENT_SAFETY_ENDPOINT"), DefaultAzureCredential())
    result = client.analyze_text(AnalyzeTextOptions(text=input))
    categories = [(c.category, int(c.severity)) for c in result.categories_analysis]
    for category, severity in categories:
        if severity > 2:
            return Decision(allowed=False,reason=category,categories=categories)

    return Decision(allowed=True,reason="Ok",categories=categories)

def check_output(text: str) -> Decision:
    return check_user_input(text)

def check_document(userPrompt: str, documentTexts: list[str]):
    token = DefaultAzureCredential().get_token("https://cognitiveservices.azure.com/.default").token
    url = require("CONTENT_SAFETY_ENDPOINT").rstrip("/") + "/contentsafety/text:shieldPrompt"
    body = {
        "userPrompt": userPrompt,
        "documents": documentTexts,
    }
    respose = httpx.post(url, params={"api-version": "2024-09-01"}, json=body, headers={"Authorization": f"Bearer {token}"})
    data = respose.json()

    attack_detected = (
        data.get("userPromptAnalysis", {}).get("attackDetected", False)
        or any(d.get("attackDetected", False) for d in data.get("documentsAnalysis", []))
    )

    return Decision(allowed=attack_detected, reason= "jailbreak-detected" if attack_detected else "", categories=None)