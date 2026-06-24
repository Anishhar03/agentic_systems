from __future__ import annotations


def keyword_relevance(answer: str, expected_keywords: list[str]) -> float:
    lowered = answer.lower()
    if not expected_keywords:
        return 1.0
    hits = sum(1 for keyword in expected_keywords if keyword.lower() in lowered)
    return hits / len(expected_keywords)


def groundedness(answer: str, context: str) -> float:
    answer_terms = {term for term in answer.lower().split() if len(term) > 4}
    context_terms = set(context.lower().split())
    if not answer_terms:
        return 0.0
    return len(answer_terms & context_terms) / len(answer_terms)
