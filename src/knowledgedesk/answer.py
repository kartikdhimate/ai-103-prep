from knowledgedesk.foundry_client import ask, get_clients, get_openai_client
from knowledgedesk.retrieve import search
from knowledgedesk.prompts import system_instructions
from knowledgedesk.search_index import search_client

def answer(sc, search_openai_client, openai_client, query : str) -> None:
    # fetch source data using index search
    sources = search(sc, search_openai_client, query)

    if not sources:
        print("Answer: I do not know.")
        print("\nSources: None")
        return

    # delimit the sources
    formatted_sources = []
    for i, source in enumerate(sources, start=1):
        formatted_sources.append(
            f"[{i}]\n"
            f"Title: {source.get('title', '')}\n"
            f"Document ID: {source.get('doc_id', '')}\n"
            f"Chunk number: {source.get('chunk_no', '')}\n"
            f"Content: {source.get('content', '')}"
        )

    sources_text = "\n\n-----SOURCE SEPARATOR-----\n\n".join(formatted_sources)

    # pass the question and delimited sources to model
    prompt = (
        f"Question: \n{query}\n\n"
        f"Sources:\n"
        f"<<BEGIN SOURCES>>\n"
        f"{sources_text}\n"
        f"<<END SOURCES>>"
    )

    answer = ask(openai_client, prompt, system_instructions)

    # print the answer and sources
    print("Answer:")
    print(answer)

    print("\nSources:")
    for i, source in enumerate(sources, start=1):
        print(f"\n[{i}] {source.get('title', 'Untitled')}")
        print(f"Document ID: {source.get('doc_id', '')}")
        print(f"Chunk number: {source.get('chunk_no', '')}")
        print(f"Content:\n{source.get('content', '')}")
        print(f"{'-'*10}")

if __name__=="__main__":
    _, openai_client = get_clients()
    sc = search_client()
    search_openai_client = get_openai_client()

    answer(sc, search_openai_client, openai_client, "what type of leaves does an employee get?")