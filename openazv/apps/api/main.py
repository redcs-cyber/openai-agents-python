"""OPENAZV API application."""

from __future__ import annotations

from fastapi import FastAPI

from core.memory.causal.pipeline import build_context_pack
from core.orchestration.parallel import run_parallel_tasks
from core.orchestration.schemas import ParallelTaskRequest, RagQueryRequest

app = FastAPI(title="OPENAZV Orchestrator", version="0.1.0")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "openazv-api"}


@app.post("/openazv/tasks/parallel")
def parallel_tasks(payload: ParallelTaskRequest) -> dict:
    return run_parallel_tasks(payload)


@app.post("/openazv/rag/query")
def rag_query(payload: RagQueryRequest) -> dict:
    return build_context_pack(payload.question, payload.max_hops)
