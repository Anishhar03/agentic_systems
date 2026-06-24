from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from agentic_systems import Document, split_text


SAMPLE = """
Agentic systems combine models, tools, memory, and control flow.
Retrieval augmented generation adds external knowledge.
Human review is important for high-risk actions.
"""


if __name__ == "__main__":
    chunks = split_text(SAMPLE, chunk_size=80, overlap=10)
    docs = [Document(text=chunk, metadata={"source": "sample", "chunk": str(i)}) for i, chunk in enumerate(chunks)]
    for doc in docs:
        print(doc)
