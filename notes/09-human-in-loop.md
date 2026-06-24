# Human In The Loop

Human-in-the-loop means the agent can pause, expose state, ask for approval or correction, and resume. This is essential when decisions are high impact, ambiguous, irreversible, or require domain judgement.

## Common HITL Patterns

- Approval: human approves a tool action before it runs.
- Review and edit: human edits the draft or state.
- Clarification: human supplies missing information.
- Escalation: agent hands off when confidence is low.
- Audit: human reviews traces after execution.

## What To Show The Human

Do not show only "Approve?" Show the relevant state:

- Goal.
- Proposed action.
- Tool name and arguments.
- Evidence used.
- Risk level.
- Expected side effect.
- Reversal plan if applicable.

## Resuming Safely

On resume, the system should use a stable thread id and checkpoint. Side effects before an interrupt must be idempotent or avoided. For example, draft before interrupt, send after approval. If the graph retries, it should not send the same email twice.

## Interview Answer

"I use HITL when the model is making a high-impact decision or triggering side effects. The graph pauses at an interrupt, persists state, exposes a structured approval payload, receives human input, and resumes from the checkpoint. This gives safety without losing automation."
