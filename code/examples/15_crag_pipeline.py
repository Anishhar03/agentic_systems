from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from agentic_systems import Document, KeywordVectorStore


docs = [
    Document("Corrective RAG grades retrieved documents before answering.", {"id": "crag"}),
    Document("Cooking pasta requires boiling water.", {"id": "pasta"}),
]


def grade(score: float) -> str:
    return "good" if score >= 0.2 else "rewrite"


if __name__ == "__main__":
    store = KeywordVectorStore()
    store.add_documents(docs)
    query = "How does corrective RAG improve retrieval?"
    doc, score = store.search(query, k=1)[0]
    route = grade(score)
    print({"top_doc": doc.metadata, "score": score, "route": route})
