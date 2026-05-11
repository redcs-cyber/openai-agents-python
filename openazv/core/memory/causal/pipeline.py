"""NeuroCausal retrieval skeleton for OPENAZV."""

from __future__ import annotations


def build_context_pack(question: str, max_hops: int = 2) -> dict:
    semantic_hits = [
        {"chunk_id": "c1", "score": 0.92, "text": "A event related to B."},
        {"chunk_id": "c2", "score": 0.88, "text": "B may trigger C under load."},
    ]
    causal_chain = [
        {"from": "A", "edge": "CAUSES", "to": "B", "confidence": 0.83},
        {"from": "B", "edge": "INDICATES", "to": "C", "confidence": 0.79},
    ][:max_hops]
    return {
        "engine": "openazv-neurocausal-rag",
        "question": question,
        "semantic_hits": semantic_hits,
        "causal_chain": causal_chain,
        "answer": "OPENAZV: Muhtemel zincir A -> B -> C. Önce B doğrulanmalı.",
    }
