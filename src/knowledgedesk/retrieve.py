from azure.search.documents.models import VectorizedQuery

from common.config import require
from common.cost_guard import record_tokens


def search(sc, openai_client, query: str, mode: str = "hybrid", top: int = 4) -> list[dict]:
    kwargs = {"top": top, "select": ["id", "doc_id", "title", "content", "chunk_no"]}
    if mode in ("keyword", "hybrid", "semantic"):
        kwargs["search_text"] = query
    if mode in ("vector", "hybrid", "semantic"):
        emb = openai_client.embeddings.create(model=require("AZURE_AI_EMBEDDING_DEPLOYMENT"), input=[query])
        record_tokens(emb.usage.total_tokens)
        kwargs["vector_queries"] = [
            VectorizedQuery(vector=emb.data[0].embedding, k_nearest_neighbors=50, fields="embedding")
        ]
    if mode == "semantic":
        kwargs.update(query_type="semantic", semantic_configuration_name="sem")
    return [dict(r) for r in sc.search(**kwargs)]
