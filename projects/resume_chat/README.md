# Resume Chat

## Goal

Build a document Q&A system over a resume, similar to a small ChatGPT-style resume assistant.

## Workflow

1. Load resume PDF or Markdown.
2. Split into chunks by section.
3. Index chunks in a vector store.
4. Retrieve relevant chunks for user questions.
5. Generate grounded answers with citations.
6. Refuse answers not supported by the resume.

## Interview Angle

The important part is not the UI. The important part is grounding: every answer must come from the resume content. The system should not invent experience, dates, employers, or skills.
