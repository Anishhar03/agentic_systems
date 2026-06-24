from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from agentic_systems import Graph, START, END


graph = Graph()
graph.add_node("grade", lambda s: {"confidence": 0.35 if "unknown" in s["question"] else 0.91})
graph.add_node("retrieve", lambda s: {"context": "retrieved context", "confidence": 0.78})
graph.add_node("answer", lambda s: {"answer": f"Answer with confidence {s['confidence']}"})
graph.add_edge(START, "grade")
graph.add_conditional_edges("grade", lambda s: "retrieve" if s["confidence"] < 0.7 else "answer", {
    "retrieve": "retrieve",
    "answer": "answer",
})
graph.add_edge("retrieve", "answer")
graph.add_edge("answer", END)


if __name__ == "__main__":
    print(graph.run({"question": "unknown production error"}))
