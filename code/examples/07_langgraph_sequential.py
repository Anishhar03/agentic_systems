from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from agentic_systems import Graph, START, END


graph = Graph()
graph.add_node("classify", lambda s: {"intent": "rag" if "document" in s["question"] else "general"})
graph.add_node("draft", lambda s: {"draft": f"Intent={s['intent']}; answer prepared"})
graph.add_node("validate", lambda s: {"answer": s["draft"], "valid": True})
graph.add_edge(START, "classify")
graph.add_edge("classify", "draft")
graph.add_edge("draft", "validate")
graph.add_edge("validate", END)


if __name__ == "__main__":
    print(graph.run({"question": "How do documents help RAG?"}))
