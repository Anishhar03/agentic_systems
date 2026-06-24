from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from agentic_systems import Document, KeywordVectorStore


docs = [
    Document("LangGraph persists state with checkpointers.", {"id": "1"}),
    Document("RAG retrieves documents before generation.", {"id": "2"}),
    Document("Tool calling lets agents interact with APIs.", {"id": "3"}),
]


if __name__ == "__main__":
    store = KeywordVectorStore()
    store.add_documents(docs)
    for doc, score in store.search("How does graph memory work?", k=2):
        print(score, doc.metadata, doc.text)
