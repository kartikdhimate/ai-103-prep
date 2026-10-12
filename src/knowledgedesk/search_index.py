import os

from azure.core.credentials import AzureKeyCredential
from azure.identity import DefaultAzureCredential
from azure.search.documents import SearchClient
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import (
    HnswAlgorithmConfiguration,
    SearchField,
    SearchFieldDataType,
    SearchIndex,
    SemanticConfiguration,
    SemanticField,
    SemanticPrioritizedFields,
    SemanticSearch,
    VectorSearch,
    VectorSearchProfile,
)

from common.config import require


def credential():
    key = os.getenv("AZURE_SEARCH_API_KEY")
    return AzureKeyCredential(key) if key else DefaultAzureCredential()


def build_index(name: str, dims: int = 1536) -> SearchIndex:
    S = SearchFieldDataType
    return SearchIndex(
        name=name,
        fields=[
            SearchField(name="id", type=S.String, key=True, filterable=True),
            SearchField(name="doc_id", type=S.String, filterable=True, facetable=True),
            SearchField(name="title", type=S.String, searchable=True),
            SearchField(name="content", type=S.String, searchable=True),
            SearchField(name="chunk_no", type=S.Int32, filterable=True, sortable=True),
            SearchField(
                name="embedding",
                type=S.Collection(S.Single),
                searchable=True,
                vector_search_dimensions=dims,
                vector_search_profile_name="vec-profile",
            ),
        ],
        vector_search=VectorSearch(
            algorithms=[HnswAlgorithmConfiguration(name="hnsw")],
            profiles=[VectorSearchProfile(name="vec-profile", algorithm_configuration_name="hnsw")],
        ),
        semantic_search=SemanticSearch(
            configurations=[
                SemanticConfiguration(
                    name="sem",
                    prioritized_fields=SemanticPrioritizedFields(
                        title_field=SemanticField(field_name="title"),
                        content_fields=[SemanticField(field_name="content")],
                    ),
                )
            ]
        ),
    )


def index_client() -> SearchIndexClient:
    return SearchIndexClient(require("AZURE_SEARCH_ENDPOINT"), credential())


def search_client() -> SearchClient:
    return SearchClient(require("AZURE_SEARCH_ENDPOINT"), require("AZURE_SEARCH_INDEX"), credential())

# Execute the following once to build index
# index_client().create_or_update_index(build_index(require("AZURE_SEARCH_INDEX")))