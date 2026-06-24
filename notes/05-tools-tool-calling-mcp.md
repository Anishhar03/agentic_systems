# Tools, Tool Calling, And MCP

Tools turn an LLM application from a text generator into an action system. A tool is a callable capability with a name, description, input schema, output contract, and security policy.

## Tool Calling Flow

```text
user goal -> model decides tool + arguments -> validate arguments -> run tool -> observe result -> model continues
```

Tool calling is powerful because the model can access fresh data, perform calculations, call APIs, query databases, or update external systems. It is risky because a wrong call can leak data or cause side effects.

## Tool Design

A good tool should be narrow, typed, and easy to verify.

- Prefer `search_customer_orders(customer_id)` over `run_sql(query)`.
- Prefer enums and schemas over free text.
- Return structured observations, not long unbounded text.
- Include error codes so the agent can recover.
- Add idempotency keys for write actions.

## Tool Policies

Production agents need policies:

- Allowlist which tools are available for the current user and task.
- Require approval for destructive or external write actions.
- Redact secrets before sending observations to the model.
- Rate-limit expensive tools.
- Log every tool request, arguments, result status, and latency.

## MCP

Model Context Protocol standardizes how tools and resources can be exposed to an AI client. Instead of hardcoding every integration into the application, an MCP server can publish tools, resource access, and schemas. A LangGraph MCP client can list tools, choose a tool, call it with JSON arguments, and feed the observation back into graph state.

MCP is especially useful for enterprise systems because integrations such as Jira, Confluence, GitHub, databases, and internal APIs can be exposed behind one protocol boundary.
