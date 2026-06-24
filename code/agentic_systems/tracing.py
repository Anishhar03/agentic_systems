from __future__ import annotations

import time
from contextlib import contextmanager
from dataclasses import dataclass, field


@dataclass
class TraceRecorder:
    events: list[dict[str, object]] = field(default_factory=list)

    @contextmanager
    def span(self, name: str, **metadata: object):
        start = time.perf_counter()
        status = "ok"
        error = None
        try:
            yield
        except Exception as exc:  # pragma: no cover - demo tracing
            status = "error"
            error = repr(exc)
            raise
        finally:
            self.events.append({
                "name": name,
                "status": status,
                "latency_ms": round((time.perf_counter() - start) * 1000, 2),
                "metadata": metadata,
                "error": error,
            })
