from __future__ import annotations

import math
import re
from collections import Counter
from dataclasses import dataclass


TOKEN_RE = re.compile(r"[a-zA-Z0-9_]+")


@dataclass
class Document:
    text: str
    metadata: dict[str, str]


def tokenize(text: str) -> list[str]:
    return [match.group(0).lower() for match in TOKEN_RE.finditer(text)]


def split_text(text: str, chunk_size: int = 500, overlap: int = 80) -> list[str]:
    if chunk_size <= overlap:
        raise ValueError("chunk_size must be greater than overlap")
    chunks: list[str] = []
    start = 0
    while start < len(text):
        chunks.append(text[start:start + chunk_size].strip())
        start += chunk_size - overlap
    return [chunk for chunk in chunks if chunk]


class KeywordVectorStore:
    """Small cosine-similarity store using token counts instead of embeddings."""

    def __init__(self) -> None:
        self.documents: list[Document] = []
        self.vectors: list[Counter[str]] = []

    def add_documents(self, docs: list[Document]) -> None:
        for doc in docs:
            self.documents.append(doc)
            self.vectors.append(Counter(tokenize(doc.text)))

    def search(self, query: str, k: int = 3) -> list[tuple[Document, float]]:
        qv = Counter(tokenize(query))
        scored = [(doc, self._cosine(qv, dv)) for doc, dv in zip(self.documents, self.vectors)]
        scored.sort(key=lambda item: item[1], reverse=True)
        return scored[:k]

    @staticmethod
    def _cosine(left: Counter[str], right: Counter[str]) -> float:
        if not left or not right:
            return 0.0
        common = set(left) & set(right)
        dot = sum(left[token] * right[token] for token in common)
        left_norm = math.sqrt(sum(value * value for value in left.values()))
        right_norm = math.sqrt(sum(value * value for value in right.values()))
        return dot / (left_norm * right_norm) if left_norm and right_norm else 0.0
