import csv
import time

from common.cost_guard import record_tokens
from knowledgedesk.foundry_client import get_clients, ask

# USD per 1M tokens (input, output). Copy from the pricing page; these are example values.
MODELS = {"gpt-5-mini": (0.25, 2.00), "gpt-5-nano": (0.05, 0.40)}
PROMPTS = [
    "Classify the sentiment (positive/neutral/negative): 'The invoice was late again.'",
    "Summarize in one sentence: Azure AI Search supports keyword, vector and hybrid queries.",
    "Extract the date and amount as JSON: 'Paid 120 EUR on 2026-03-14.'",
    "Explain the difference between a resource and a project in two bullets.",
    "Write a polite two-sentence reply to a customer asking for a refund.",
]

_, client = get_clients()
rows = []
for model, (price_in, price_out) in MODELS.items():
    for prompt in PROMPTS:
        start = time.perf_counter()
        r = client.responses.create(model=model, input=prompt)
        seconds = time.perf_counter() - start
        record_tokens(r.usage.total_tokens)
        cost = (r.usage.input_tokens * price_in + r.usage.output_tokens * price_out) / 1_000_000
        rows.append([model, prompt[:30], r.usage.input_tokens, r.usage.output_tokens, round(seconds, 2), round(cost, 6)])

with open("out/model_comparison.csv", "w", newline="") as f:
    csv.writer(f).writerows([["model", "prompt", "in_tok", "out_tok", "seconds", "usd"], *rows])
for row in rows:
    print(row)
