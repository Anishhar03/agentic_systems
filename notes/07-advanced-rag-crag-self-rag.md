# Corrective RAG And Self-RAG

Advanced RAG techniques add feedback loops around retrieval and generation. The goal is to reduce hallucination and improve answer grounding.

## Corrective RAG

Corrective RAG, often called CRAG, evaluates whether retrieved documents are good enough. If retrieval is weak, the system can rewrite the query, retrieve again, use a fallback source, or ask for clarification.

A CRAG graph usually has:

- retrieve node.
- grade-documents node.
- transform-query node.
- fallback-search node.
- generate node.
- answer-grade node.

The key insight is that retrieval is not automatically trusted. Retrieved documents become evidence only after grading.

## Self-RAG

Self-RAG makes the generation step reflective. The system decides whether retrieval is needed, checks whether passages support the answer, and judges whether the final answer addresses the question.

A practical Self-RAG loop:

1. Decide if retrieval is required.
2. Retrieve candidate passages.
3. Grade relevance of each passage.
4. Generate answer from supported passages.
5. Check answer support and completeness.
6. Retry or abstain if the answer is unsupported.

## Design Tradeoffs

CRAG and Self-RAG improve reliability but add latency and cost. Use them when correctness matters: legal, medical, finance, compliance, customer support, production incident response, or interview-grade technical explanations.

For low-risk creative tasks, simple RAG may be enough. For high-risk tasks, pair advanced RAG with citations, evaluator traces, and human escalation.
