from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from copy import deepcopy


@dataclass
class ConversationMemory:
    max_messages: int = 8
    messages: list[dict[str, str]] = field(default_factory=list)

    def add(self, role: str, content: str) -> None:
        self.messages.append({"role": role, "content": content})
        self.messages = self.messages[-self.max_messages:]

    def render(self) -> str:
        return "\n".join(f"{m['role']}: {m['content']}" for m in self.messages)


@dataclass
class LongTermMemory:
    facts: dict[str, dict[str, object]] = field(default_factory=dict)

    def remember(self, key: str, value: str, source: str = "user", confidence: float = 1.0) -> None:
        self.facts[key] = {
            "value": value,
            "source": source,
            "confidence": confidence,
            "stored_at": datetime.now(timezone.utc).isoformat(),
        }

    def recall(self, key: str, default: str = "") -> str:
        item = self.facts.get(key)
        return str(item["value"]) if item else default


@dataclass
class Checkpointer:
    snapshots: dict[str, list[dict[str, object]]] = field(default_factory=dict)

    def save(self, thread_id: str, state: dict[str, object]) -> None:
        self.snapshots.setdefault(thread_id, []).append(deepcopy(state))

    def latest(self, thread_id: str) -> dict[str, object]:
        if thread_id not in self.snapshots or not self.snapshots[thread_id]:
            return {}
        return deepcopy(self.snapshots[thread_id][-1])

    def history(self, thread_id: str) -> list[dict[str, object]]:
        return deepcopy(self.snapshots.get(thread_id, []))
