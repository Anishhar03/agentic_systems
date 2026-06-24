from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from agentic_systems import Graph, START, END


def improve(state):
    attempts = int(state.get("attempts", 0)) + 1
    quality = 0.4 + attempts * 0.25
    return {"attempts": attempts, "quality": quality, "draft": f"draft v{attempts}"}


graph = Graph()
graph.add_node("improve", improve)
graph.add_node("finish", lambda s: {"answer": s["draft"]})
graph.add_edge(START, "improve")
graph.add_conditional_edges("improve", lambda s: "done" if s["quality"] >= 0.85 else "retry", {
    "retry": "improve",
    "done": "finish",
})
graph.add_edge("finish", END)


if __name__ == "__main__":
    print(graph.run({"question": "Write a reliable answer"}))
