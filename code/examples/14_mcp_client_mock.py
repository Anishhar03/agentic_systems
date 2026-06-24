from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from agentic_systems.tools import default_registry


class MockMCPClient:
    def __init__(self):
        self.registry = default_registry()

    def list_tools(self):
        return self.registry.list_tools()

    def call_tool(self, name: str, arguments: dict):
        return self.registry.call(name, **arguments)


if __name__ == "__main__":
    client = MockMCPClient()
    print(client.list_tools())
    print(client.call_tool("calculator", {"expression": "40+2"}))
