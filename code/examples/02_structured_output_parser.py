from pathlib import Path
import sys
import json

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from agentic_systems import FakeLLM


REQUIRED = {"decision", "confidence", "reason"}


def parse_decision(raw: str) -> dict[str, object]:
    data = json.loads(raw)
    missing = REQUIRED - set(data)
    if missing:
        raise ValueError(f"Missing fields: {missing}")
    if not 0 <= float(data["confidence"]) <= 1:
        raise ValueError("confidence must be between 0 and 1")
    return data


if __name__ == "__main__":
    raw = FakeLLM().invoke("Return structured JSON for a route decision")
    print(parse_decision(raw))
