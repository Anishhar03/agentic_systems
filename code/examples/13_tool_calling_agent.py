from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from agentic_systems.tools import default_registry
from agentic_systems.guardrails import require_allowed_tool


def run_agent(goal: str):
    registry = default_registry()
    allowed = {"calculator", "blog_outline"}
    if "outline" in goal:
        tool_name = "blog_outline"
        require_allowed_tool(tool_name, allowed)
        return registry.call(tool_name, topic="Agentic AI")
    tool_name = "calculator"
    require_allowed_tool(tool_name, allowed)
    return registry.call(tool_name, expression="(10 + 5) * 2")


if __name__ == "__main__":
    print(run_agent("calculate capacity"))
    print(run_agent("make outline"))
