from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from agentic_systems.tracing import TraceRecorder


if __name__ == "__main__":
    trace = TraceRecorder()
    with trace.span("retrieve", query="agent memory"):
        documents = ["memory uses checkpointers and stores"]
    with trace.span("generate", docs=len(documents)):
        answer = "Memory is split into short-term and long-term storage."
    print(answer)
    print(trace.events)
