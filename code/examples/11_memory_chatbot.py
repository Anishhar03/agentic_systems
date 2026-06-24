from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from agentic_systems import Checkpointer, ConversationMemory, LongTermMemory


if __name__ == "__main__":
    short = ConversationMemory()
    long = LongTermMemory()
    checkpoints = Checkpointer()
    thread_id = "user-123-thread-1"

    short.add("user", "My name is Anish and I am learning Agentic AI")
    long.remember("name", "Anish", source="conversation")
    state = {"messages": short.messages, "known_name": long.recall("name")}
    checkpoints.save(thread_id, state)

    print(short.render())
    print(checkpoints.latest(thread_id))
