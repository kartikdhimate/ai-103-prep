import json
from pathlib import Path

from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import OpenAI

from common.config import require
from knowledgedesk.retrieve import search
from knowledgedesk.search_index import search_client

MODES = ("keyword", "vector", "hybrid", "semantic")

def load_questions(path: str) -> list[dict]:
    with open(path, "r", encoding="utf-8") as file:
        return [
            json.loads(line)
            for line in file
            if line.strip()
        ]

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

def main():
    current_dir = Path(__file__).resolve().parent
    questions = load_questions((current_dir / "../../data/eval/qa.jsonl").as_posix())
    results = []
    openai_client=get_openai_client()

    for i, item in enumerate(questions, start=1):
        question = item["question"]
        expected_doc_id = str(item["doc_id"])

        for mode in MODES:
            hits = search(
                sc=search_client(),
                openai_client=openai_client,
                query=question,
                mode=mode,
                top=4,
            )

            doc_ids = [str(hit.get("doc_id", "")) for hit in hits]

            top1 = bool(doc_ids) and doc_ids[0] == expected_doc_id
            top4 = expected_doc_id in doc_ids[:4]

            results.append({
                "question_no": i,
                "question": question,
                "mode": mode,
                "top1": top1,
                "top4": top4,
            })

    # Print detailed results.
    print(
        f"\n{'#':<4} {'Mode':<10} {'Top 1':<10} "
        f"{'Top 4':<10} Question"
    )
    print("-" * 110)

    for r in results:
        print(
            f"{r['question_no']:<4} "
            f"{r['mode']:<10} "
            f"{'YES' if r['top1'] else 'NO':<10} "
            f"{'YES' if r['top4'] else 'NO':<10} "
            f"{r['question']}"
        )

    # Print aggregate results.
    print("\nSUMMARY")
    print("-" * 55)
    print(f"{'Mode':<12}{'Top 1 Hits':<15}{'Top 4 Hits':<15}")

    for mode in MODES:
        mode_results = [r for r in results if r["mode"] == mode]
        total = len(mode_results)
        top1_hits = sum(r["top1"] for r in mode_results)
        top4_hits = sum(r["top4"] for r in mode_results)

        print(
            f"{mode:<12}"
            f"{top1_hits}/{total:<13}"
            f"{top4_hits}/{total:<13}"
        )

if __name__ == "__main__":
    main()