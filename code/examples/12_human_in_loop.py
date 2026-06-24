from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from agentic_systems import Checkpointer


def propose_action(state):
    state["pending_action"] = {
        "tool": "send_email",
        "to": "mentor@example.com",
        "body": "Please review my agent design.",
        "risk": "external_write",
    }
    state["status"] = "waiting_for_approval"
    return state


if __name__ == "__main__":
    cp = Checkpointer()
    thread_id = "approval-demo"
    state = propose_action({"goal": "ask mentor for review"})
    cp.save(thread_id, state)
    print("Paused:", cp.latest(thread_id))
    approved = cp.latest(thread_id)
    approved["human_decision"] = "approved"
    approved["status"] = "ready_to_execute"
    print("Resumed:", approved)
