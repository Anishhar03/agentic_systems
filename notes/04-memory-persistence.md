# Memory, Persistence, And Time Travel

LLMs do not remember by themselves between calls. A stateless model only sees the current prompt. Memory is an application responsibility: you decide what to store, where to store it, when to retrieve it, and how to summarize it.

## Short-Term Memory

Short-term memory is thread-scoped. It preserves the current conversation, graph state, tool observations, drafts, and pending actions. In LangGraph, this is commonly handled through checkpointers. A checkpointer lets a graph resume from a specific thread id.

Use short-term memory for:

- conversation continuity.
- resuming after errors.
- human-in-the-loop approvals.
- time travel debugging.
- iterative loops where previous attempts matter.

## Long-Term Memory

Long-term memory is cross-thread. It stores durable facts such as user preferences, reusable summaries, learned entities, project details, or application knowledge. It should be intentionally curated. Storing every message forever creates privacy, cost, and quality problems.

Types of long-term memory:

- Semantic memory: facts about the user or domain.
- Episodic memory: important events and decisions.
- Procedural memory: instructions and learned preferences.
- Knowledge memory: documents, tickets, pages, or indexed repositories.

## Time Travel

Time travel means inspecting or replaying previous graph states. It is useful for debugging agent behavior: you can see why a router chose a path, why a tool was called, what state existed before an error, and how a different human decision would change the outcome.

## Memory Quality Rules

- Store only useful information.
- Attach source, timestamp, and confidence.
- Separate user-provided facts from model-inferred facts.
- Make deletion and correction possible.
- Do not let memory silently override current user instructions.
