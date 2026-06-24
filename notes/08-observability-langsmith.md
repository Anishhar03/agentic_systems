# Observability And LangSmith

Agentic systems need observability because failures are often hidden inside intermediate steps. The final answer may be wrong because retrieval failed, a parser repaired bad JSON incorrectly, a router chose the wrong branch, a tool timed out, or a loop stopped too early.

## What To Trace

- User input and sanitized prompt.
- Model calls, parameters, latency, token usage, and response.
- Tool calls, arguments, output, error status, and latency.
- Retriever queries, returned document ids, scores, and metadata.
- Graph node transitions and state updates.
- Human approvals, edits, and rejected actions.
- Evaluator scores and regression results.

## Metrics

- Task success rate.
- Tool success and failure rate.
- Retrieval precision at k.
- Faithfulness or groundedness.
- Hallucination rate.
- Average cost per task.
- P95 latency.
- Human escalation rate.
- Retry count and loop iterations.

## Evaluation

Evaluation should exist before production. Build a small golden dataset of realistic tasks and expected properties. For RAG, include questions with known source documents. For agents, include tool-call expectations, route expectations, and safety constraints.

## Debugging With Traces

A trace should let you answer:

- What did the agent know when it made this decision?
- Which tool did it call and why?
- Did retrieval return the right evidence?
- Did the model ignore evidence?
- Was the final answer validated?
- Where did latency and cost accumulate?
