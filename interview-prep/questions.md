# Agentic AI Interview Questions

        ## 1. What is Agentic AI?

Agentic AI wraps an LLM in a runtime that can maintain state, choose actions, call tools, observe results, evaluate progress, and recover. It is goal-oriented rather than only output-oriented.

## 2. How is Agentic AI different from Generative AI?

Generative AI produces content from a prompt. Agentic AI executes a task loop with planning, tools, memory, state transitions, and stopping conditions.

## 3. When would you use LangChain?

Use LangChain for model abstraction, prompts, tools, structured output, parsers, retrieval, runnables, and a higher-level agent harness.

## 4. When would you use LangGraph?

Use LangGraph when you need explicit state, graph control flow, conditional routing, persistence, human-in-the-loop, streaming, subgraphs, or long-running workflows.

## 5. What is state in LangGraph?

State is the shared object passed between graph nodes. Nodes read state and return updates; edges decide which node runs next.

## 6. What is a checkpointer?

A checkpointer persists thread-scoped graph state so the workflow can resume, inspect history, support human approval, or recover from failure.

## 7. What is the difference between short-term and long-term memory?

Short-term memory is scoped to the current thread or run. Long-term memory stores durable facts across threads, such as preferences or project knowledge.

## 8. How does tool calling work?

The model or workflow selects a tool and arguments, application code validates them, runs the tool, and feeds the observation back into state.

## 9. Why is RAG important?

RAG grounds answers in external documents, reducing reliance on model memory and allowing answers over private or fresh knowledge.

## 10. What is CRAG?

Corrective RAG grades retrieved documents and corrects weak retrieval through query rewriting, fallback search, or retry before answering.

## 11. What is Self-RAG?

Self-RAG adds reflection around retrieval and generation: decide whether retrieval is needed, grade relevance, check support, and retry or abstain.

## 12. How do you observe an agent?

Trace model calls, tool calls, retriever results, state transitions, route decisions, latency, cost, errors, and evaluator scores.

## 13. How do you make agents safe?

Use scoped tools, validation, allowlists, human approval for side effects, secret redaction, permission-aware retrieval, tracing, and fail-closed policies.

## 14. What is HITL?

Human-in-the-loop pauses execution for approval, correction, or clarification and then resumes from persisted state.

## 15. What failure modes do agents have?

Wrong routing, bad retrieval, hallucination, parser failure, tool failure, infinite loops, stale memory, prompt injection, and unapproved side effects.
