# Workflow Patterns

Agentic systems are easier to design when you recognize recurring workflow shapes. The playlist covers sequential, parallel, conditional, and iterative workflows; these are the building blocks for most production agents.

## Sequential Workflow

A sequential workflow is a pipeline: step A, then B, then C. It is best when order is fixed and each step depends on the previous output.

Example: classify ticket -> retrieve policy -> draft response -> validate response -> send to human.

Strengths: predictable, testable, easy to trace. Weakness: slow if independent steps could run in parallel.

## Parallel Workflow

A parallel workflow fans out independent work and then merges results. This is useful for research agents, multi-source retrieval, multi-criteria evaluation, or generating multiple drafts.

Example: search docs, search tickets, search web, and search database at the same time; merge the evidence before answering.

Key design issue: define merge semantics. Do you concatenate, rank, vote, deduplicate, or ask an evaluator to synthesize?

## Conditional Workflow

A conditional workflow routes based on state. For example, if retrieval confidence is low, ask a clarifying question; if confidence is medium, retrieve more; if confidence is high, answer.

Conditional routing should be explicit and observable. Log the route decision and the features used to make it.

## Iterative Workflow

Iterative workflows loop until a condition is met. Examples include ReAct agents, self-reflection, query rewriting, CRAG, Self-RAG, and planner-executor systems.

Every loop needs:

- a clear progress signal.
- a maximum iteration limit.
- a way to detect repeated failure.
- state summaries to prevent context bloat.
- final fallback behavior.

## Choosing The Pattern

Start deterministic. If the path is known, use a chain. If work is independent, use parallel branches. If decisions depend on evidence, use conditional routing. If the system must improve over multiple attempts, use an iterative loop with strict stopping rules.
