from typing import Callable


class Runnable:
    def __init__(self, fn: Callable):
        self.fn = fn

    def invoke(self, value):
        return self.fn(value)

    def then(self, next_fn: Callable):
        return Runnable(lambda value: next_fn(self.invoke(value)))


pipeline = (
    Runnable(lambda q: q.strip().lower())
    .then(lambda q: {"question": q, "length": len(q)})
    .then(lambda data: f"Question '{data['question']}' has {data['length']} characters")
)


if __name__ == "__main__":
    print(pipeline.invoke("  What is Agentic AI?  "))
