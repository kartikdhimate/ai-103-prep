from pathlib import Path

from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import OpenAI

from common.config import require
from knowledgedesk.chunking import chunk_text
from knowledgedesk.search_index import search_client
from common.cost_guard import record_tokens

BATCH_SIZE = 16
DOCUMENTS_DIR = "../../data"

def ingest_file(path: str | Path, embeddings_client, embedding_deployment: str) -> int:
    path = Path(path)
    text = path.read_text(encoding="utf-8")

    chunks = chunk_text(text=text)

    if not chunks:
        print(f"Skipping empty file: {path}")
        return 0

    doc_id = path.stem
    title = path.name

    search = search_client()

    file_tokens = 0
    failed_uploads = 0

    for batch_start in range(0, len(chunks), BATCH_SIZE):
        batch = chunks[batch_start : batch_start + BATCH_SIZE]

        response = embeddings_client.embeddings.create(
            model=embedding_deployment,
            input=batch,
        )

        batch_tokens = response.usage.total_tokens
        file_tokens += batch_tokens

        daily_total = record_tokens(batch_tokens)

        print(
            f"Embedded {len(batch)} chunks from {path}. "
            f"Batch tokens: {batch_tokens}. "
            f"Daily total: {daily_total}."
        )

        # Preserve the order of chunks and their embeddings.
        embeddings = sorted(
            response.data,
            key=lambda item: item.index,
        )

        docs = [
            {
                "id": f"{doc_id}-{batch_start + i}",
                "doc_id": doc_id,
                "title": title,
                "content": chunk,
                "chunk_no": batch_start + i,
                "embedding": embedding.embedding,
            }
            for i, (chunk, embedding) in enumerate(
                zip(batch, embeddings)
            )
        ]

        results = search.upload_documents(documents=docs)

        for result in results:
            if not result.succeeded:
                failed_uploads += 1
                print(
                    f"Upload failed for document {result.key}: "
                    f"{result.error_message}"
                )

    print(
        f"Completed {path}: "
        f"{len(chunks)} chunks, "
        f"{file_tokens} embedding tokens, "
        f"{failed_uploads} failed uploads."
    )

    return file_tokens

def main() -> None:
    openai_endpoint = require("AZURE_OPENAI_ENDPOINT")
    embedding_deployment = require("AZURE_AI_EMBEDDING_DEPLOYMENT")

    credential = DefaultAzureCredential()

    token_provider = get_bearer_token_provider(
        credential,
        "https://ai.azure.com/.default",
    )

    embeddings_client = OpenAI(
        base_url=openai_endpoint,
        api_key=token_provider,
    )

    # Collect Markdown file paths into a list.
    current_dir = Path(__file__).resolve().parent
    data_dir = (current_dir / DOCUMENTS_DIR).resolve()
    files = sorted(data_dir.rglob("*.md"))

    if not files:
        print(f"No Markdown files found in {DOCUMENTS_DIR}")
        return

    print(f"Found {len(files)} Markdown files.")

    total_tokens = 0
    processed_files = 0

    for file in files:
        try:
            tokens = ingest_file(
                path=file,
                embeddings_client=embeddings_client,
                embedding_deployment=embedding_deployment,
            )

            total_tokens += tokens
            processed_files += 1
        except RuntimeError as exc:
            if "Daily token budget exceeded" in str(exc):
                print(f"Stopping ingestion: {exc}")
                raise

            print(f"Failed to ingest {file}: {exc}")
        except Exception as exc:
            print(f"Failed to ingest {file}: {exc}")

        print(f"Processed {processed_files} files.")
        print(f"Tokens consumed in this run: {total_tokens}")  

if __name__ == "__main__":
    main()
