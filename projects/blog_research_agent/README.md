# Blog Research Agent

## Goal

Build an agent that plans, researches, outlines, drafts, critiques, and revises a technical blog.

## Architecture

```mermaid
flowchart LR
  Goal[Blog goal] --> Planner[Planner]
  Planner --> Research[Research tools]
  Research --> Evidence[Evidence store]
  Evidence --> Outline[Outline node]
  Outline --> Draft[Draft node]
  Draft --> Critic[Critic evaluator]
  Critic -->|revise| Draft
  Critic -->|approve| Final[Final article]
```

## State

- topic
- audience
- constraints
- search_queries
- evidence
- outline
- draft
- critique
- iteration_count
- final_article

## Production Notes

Add citations, source quality scoring, duplicate detection, max iterations, and human review before publishing.
