# Agentic Systems

In-depth Agentic AI study repository based on these playlists:

- [Agentic AI using LangGraph](https://www.youtube.com/playlist?list=PLKnIA16_RmvYsvB8qkUQuJmJNuiCUJFPL)
- [LangChain for Beginners / GenAI using LangChain](https://www.youtube.com/playlist?list=PL8n_RR1gqRmycHk4pYlQPYd2RoqE5fHCF)

This repo contains original, playlist-aligned notes, runnable educational code, project blueprints, interview preparation, and a PDF study guide.

## What Is Inside

- `notes/`: deep concept notes for Agentic AI, LangChain, LangGraph, workflows, tools, RAG, memory, observability, human-in-the-loop, and production architecture.
- `video-notes/`: video-by-video notes for all 46 extracted playlist videos.
- `code/`: dependency-light Python examples that demonstrate chains, parsers, retrieval, graph workflows, memory, tool calling, MCP-style tool discovery, CRAG, Self-RAG, and tracing.
- `projects/`: project blueprints for a blog research agent, resume chat, SQLite memory chatbot, and Streamlit chatbot.
- `interview-prep/`: interview questions, system design notes, and practice exercises.
- `pdf/Agentic_Systems_Study_Guide.pdf`: concise printable study guide.
- `pdf/Agentic_Systems_Masterclass.pdf`: expanded beginner-to-advanced instructor-style PDF covering foundations, frameworks, RAG, tools, memory, production, and interviews.

## Quick Start

```bash
cd code
python examples/07_langgraph_sequential.py
python examples/13_tool_calling_agent.py
python examples/16_self_rag_pipeline.py
```

The core examples do not require API keys. They use a deterministic fake LLM and small local utilities so you can understand the architecture before plugging in a real provider.

## How To Study

1. Read `notes/00-agentic-ai-roadmap.md`.
2. Read the LangChain notes before the LangGraph notes if you are new to the ecosystem.
3. Run one code example after every workflow note.
4. Use `video-notes/` as a checklist while watching the playlists.
5. Use `interview-prep/questions.md` for revision.

## Important Note

These are original study notes generated from public playlist metadata and official framework documentation. They are not a transcript dump. Use them beside the videos for revision and implementation practice.
