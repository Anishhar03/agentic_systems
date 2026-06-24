# LangChain Foundations

LangChain is best understood as a composition layer for LLM applications. It gives you abstractions for models, prompts, messages, tools, structured outputs, parsers, retrieval components, and runnable pipelines.

## Core Components

- Model: a provider-independent interface to chat models, completion models, or embedding models.
- Message: a structured record such as system, human, assistant, or tool message.
- Prompt: a reusable template that prepares instructions and context.
- Structured output: a way to force model responses into a schema like JSON or Pydantic.
- Output parser: a component that validates and transforms model text into typed data.
- Chain: a sequence of steps where the output of one step becomes input to the next.
- Runnable: a composable execution unit that supports invoke, batch, stream, and composition.
- Tool: a callable function with a description and schema that a model or workflow can use.
- Retriever: a component that returns relevant documents for a query.

## Why Runnables Matter

Runnables are important because they standardize execution. A prompt, model, parser, retriever, lambda transform, or branch can all behave like a runnable. That makes pipelines easier to test, stream, batch, trace, and replace.

A typical chain looks like:

```text
user question -> prompt template -> model -> parser -> typed answer
```

A richer retrieval chain looks like:

```text
user question -> retriever -> context formatter -> prompt -> model -> answer parser
```

## Prompt Engineering For Agentic Systems

Agentic prompts should not only say "be helpful." They should define the role, available tools, constraints, output schema, stopping rules, and escalation policy. Good prompts reduce ambiguity before runtime logic begins.

A practical structure:

- Identity: what the agent is responsible for.
- Context: facts, documents, user profile, prior state.
- Tools: what each tool does and when to use it.
- Policy: what is allowed, what requires approval, what is forbidden.
- Output contract: JSON schema, bullet format, citations, confidence score, or action plan.
- Failure behavior: what to do when context is missing, a tool fails, or the answer is uncertain.

## Structured Output And Parsers

Free-form text is hard to test and hard to route. Structured output lets downstream code reliably read fields such as decision, confidence, entities, next_action, citations, or tool_request. In production, never assume the model complied. Parse, validate, repair when safe, and fail closed for risky actions.

## LangChain vs LangGraph

Use LangChain when you want a compact harness around models, prompts, tools, retrieval, and a common agent loop. Use LangGraph when you need explicit state, branching, checkpointing, human review, time travel, subgraphs, or durable long-running workflows.
