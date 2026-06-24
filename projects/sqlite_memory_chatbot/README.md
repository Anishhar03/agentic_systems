# SQLite Memory Chatbot

## Goal

Persist conversation state and long-term memories in SQLite.

## Tables

- conversations: thread id, user id, created_at, updated_at.
- messages: thread id, role, content, created_at.
- checkpoints: thread id, graph_state_json, created_at.
- memories: user id, key, value, source, confidence, created_at.

## Notes

Use a checkpointer for graph state and a separate store for durable facts. Do not mix raw chat logs with curated long-term memory.
