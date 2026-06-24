from __future__ import annotations

import re


EMAIL_RE = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
SECRET_RE = re.compile(r"(?i)(api[_-]?key|token|password)\s*[:=]\s*\S+")


def redact_sensitive(text: str) -> str:
    text = EMAIL_RE.sub("[REDACTED_EMAIL]", text)
    text = SECRET_RE.sub(lambda m: m.group(1) + "=[REDACTED]", text)
    return text


def detect_prompt_injection(text: str) -> bool:
    markers = [
        "ignore previous instructions",
        "developer message",
        "system prompt",
        "exfiltrate",
        "reveal secrets",
    ]
    lowered = text.lower()
    return any(marker in lowered for marker in markers)


def require_allowed_tool(tool_name: str, allowed: set[str]) -> None:
    if tool_name not in allowed:
        raise PermissionError(f"Tool '{tool_name}' is not allowed in this context")
