from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable


START = "__start__"
END = "__end__"
State = dict[str, object]
Node = Callable[[State], State]
Router = Callable[[State], str]


@dataclass
class Graph:
    """Tiny graph runtime that mirrors LangGraph concepts for learning."""

    nodes: dict[str, Node] = field(default_factory=dict)
    edges: dict[str, str] = field(default_factory=dict)
    conditional_edges: dict[str, tuple[Router, dict[str, str]]] = field(default_factory=dict)

    def add_node(self, name: str, fn: Node) -> None:
        self.nodes[name] = fn

    def add_edge(self, source: str, target: str) -> None:
        self.edges[source] = target

    def add_conditional_edges(self, source: str, router: Router, routes: dict[str, str]) -> None:
        self.conditional_edges[source] = (router, routes)

    def run(self, state: State, max_steps: int = 25) -> State:
        current = self.edges.get(START)
        trace: list[str] = list(state.get("trace", []))
        steps = 0
        while current and current != END:
            steps += 1
            if steps > max_steps:
                raise RuntimeError(f"Graph exceeded max_steps={max_steps}; check loop stopping rules")
            if current not in self.nodes:
                raise KeyError(f"Unknown graph node: {current}")
            trace.append(current)
            update = self.nodes[current](state)
            state.update(update)
            state["trace"] = trace
            if current in self.conditional_edges:
                router, routes = self.conditional_edges[current]
                route = router(state)
                state["last_route"] = route
                current = routes[route]
            else:
                current = self.edges.get(current, END)
        trace.append(END)
        state["trace"] = trace
        return state
