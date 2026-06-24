from __future__ import annotations

import ast
import operator
from dataclasses import dataclass
from typing import Any, Callable


SAFE_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
}


@dataclass
class Tool:
    name: str
    description: str
    fn: Callable[..., Any]

    def run(self, **kwargs: Any) -> Any:
        return self.fn(**kwargs)


class ToolRegistry:
    def __init__(self) -> None:
        self.tools: dict[str, Tool] = {}

    def register(self, tool: Tool) -> None:
        self.tools[tool.name] = tool

    def list_tools(self) -> list[dict[str, str]]:
        return [{"name": tool.name, "description": tool.description} for tool in self.tools.values()]

    def call(self, name: str, **kwargs: Any) -> Any:
        if name not in self.tools:
            raise KeyError(f"Tool not allowed or not registered: {name}")
        return self.tools[name].run(**kwargs)


def safe_calculator(expression: str) -> float:
    def eval_node(node: ast.AST) -> float:
        if isinstance(node, ast.Expression):
            return eval_node(node.body)
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return float(node.value)
        if isinstance(node, ast.BinOp) and type(node.op) in SAFE_OPERATORS:
            return SAFE_OPERATORS[type(node.op)](eval_node(node.left), eval_node(node.right))
        if isinstance(node, ast.UnaryOp) and type(node.op) in SAFE_OPERATORS:
            return SAFE_OPERATORS[type(node.op)](eval_node(node.operand))
        raise ValueError("Unsupported expression")

    tree = ast.parse(expression, mode="eval")
    return eval_node(tree)


def default_registry() -> ToolRegistry:
    registry = ToolRegistry()
    registry.register(Tool("calculator", "Evaluate a safe arithmetic expression", safe_calculator))
    registry.register(Tool("blog_outline", "Create a simple technical blog outline", lambda topic: [
        f"Why {topic} matters",
        "Architecture",
        "Implementation steps",
        "Failure modes",
        "Interview summary",
    ]))
    return registry
