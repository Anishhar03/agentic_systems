# LangGraph Foundations

LangGraph is a low-level orchestration framework for stateful agent workflows. The central idea is simple: define a state schema, define nodes that transform state, connect nodes with edges, and compile the graph into an executable runtime.

## Graph Terms

- State: the shared data object carried through the graph.
- Node: a function that reads state and returns updates.
- Edge: a transition from one node to another.
- Conditional edge: routing logic that picks the next node based on current state.
- START and END: special boundaries of the graph.
- Reducer: merge logic for combining state updates, especially for message lists or parallel branches.
- Checkpointer: persistence for thread-scoped graph state.
- Store: long-term application memory outside one graph thread.
- Interrupt: a controlled pause that waits for external input before resuming.

## Why Graphs Are Useful

Agentic systems become hard to reason about when the loop is hidden inside one while-loop prompt. A graph makes the control flow explicit. You can inspect the state at every node, test each node independently, add checkpoints, and route errors to recovery nodes.

## State Design

Good state design is the heart of LangGraph. State should contain the minimum durable information needed to continue the task. Avoid dumping every raw prompt and document into state. Separate:

- working state: current question, draft, retrieved docs, selected tool, pending approval.
- execution metadata: attempts, trace id, timestamps, latency, errors.
- memory references: user id, thread id, document ids, vector store keys.
- final output: answer, citations, confidence, next steps.

## Node Design

Nodes should be idempotent when possible. If a node sends an email, creates a ticket, charges money, or writes to a database, guard it with an approval node or a de-duplication key. This matters because durable systems can retry after failure.

## Conditional Routing

Conditional routing is where LangGraph becomes more than a chain. The router may inspect confidence, missing fields, tool results, policy status, or evaluator output. This enables patterns like:

- answer directly if confidence is high.
- retrieve if context is missing.
- ask human if the action is risky.
- retry if output is invalid.
- stop if max iterations is reached.
