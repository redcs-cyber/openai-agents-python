"""Shared OPENAZV orchestration schemas."""

from __future__ import annotations

from pydantic import BaseModel, Field


class TaskSpec(BaseModel):
    task_id: str
    agent_type: str
    prompt: str
    priority: int = Field(default=5, ge=1, le=10)
    timeout_s: int = Field(default=120, ge=1, le=3600)


class ParallelTaskRequest(BaseModel):
    tasks: list[TaskSpec]


class RagQueryRequest(BaseModel):
    question: str
    max_hops: int = Field(default=2, ge=1, le=5)
