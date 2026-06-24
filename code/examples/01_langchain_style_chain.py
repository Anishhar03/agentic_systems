from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from agentic_systems import FakeLLM


def prompt_template(topic: str) -> str:
    return f"Explain {topic} in three bullet points."


def parse_bullets(text: str) -> list[str]:
    return [line.strip("- ") for line in text.splitlines() if line.strip()]


if __name__ == "__main__":
    llm = FakeLLM()
    response = llm.invoke(prompt_template("agentic AI"))
    print(parse_bullets(response))
