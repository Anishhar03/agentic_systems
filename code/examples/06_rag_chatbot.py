from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from agentic_systems import Document, FakeLLM, KeywordVectorStore


KNOWLEDGE = [
    Document("Agentic AI uses a loop of plan, act, observe, and evaluate.", {"source": "notes"}),
    Document("RAG retrieves relevant context and passes it to the model.", {"source": "notes"}),
    Document("LangGraph is useful for stateful workflows and human-in-the-loop.", {"source": "notes"}),
]


def answer(question: str) -> str:
    store = KeywordVectorStore()
    store.add_documents(KNOWLEDGE)
    docs = store.search(question, k=2)
    context = "\n".join(doc.text for doc, _ in docs)
    return FakeLLM().invoke(f"Answer using context:\n{context}\nQuestion:{question}")


if __name__ == "__main__":
    print(answer("What does RAG add to an agent?"))
