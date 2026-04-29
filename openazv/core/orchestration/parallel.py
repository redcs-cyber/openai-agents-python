"""Simple parallel task runner for OPENAZV."""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from time import perf_counter

from core.orchestration.schemas import ParallelTaskRequest, TaskSpec


def _execute_task(task: TaskSpec) -> dict:
    return {
        "task_id": task.task_id,
        "agent_type": task.agent_type,
        "status": "ok",
        "confidence": 0.75,
        "summary": f"OPENAZV agent '{task.agent_type}' completed task.",
    }


def run_parallel_tasks(payload: ParallelTaskRequest) -> dict:
    started = perf_counter()
    with ThreadPoolExecutor(max_workers=max(1, len(payload.tasks))) as pool:
        results = list(pool.map(_execute_task, payload.tasks))
    elapsed_ms = round((perf_counter() - started) * 1000, 2)
    return {
        "engine": "openazv-parallel",
        "count": len(results),
        "elapsed_ms": elapsed_ms,
        "results": results,
    }
