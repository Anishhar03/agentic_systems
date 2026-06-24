def search_docs(question: str) -> list[str]:
    return ["doc: agentic systems need state"]


def search_tickets(question: str) -> list[str]:
    return ["ticket: tool failures need retries"]


def fan_in(results: list[list[str]]) -> list[str]:
    merged = []
    for part in results:
        merged.extend(part)
    return merged


if __name__ == "__main__":
    question = "How do I debug an agent?"
    evidence = fan_in([search_docs(question), search_tickets(question)])
    print({"question": question, "evidence": evidence})
