from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from agentic_systems.evals import groundedness


def self_check(question: str, context: str, answer: str) -> dict[str, object]:
    score = groundedness(answer, context)
    return {
        "needs_retry": score < 0.35,
        "groundedness": round(score, 2),
        "decision": "answer" if score >= 0.35 else "retrieve_again",
    }


if __name__ == "__main__":
    context = "Self-RAG checks whether an answer is supported by retrieved evidence."
    answer = "Self-RAG checks support before finalizing the answer."
    print(self_check("What is Self-RAG?", context, answer))
