# utils/load_candidates.py

import json
from pathlib import Path
from schema.candidate_schema import CandidateSchema


def load_candidates(file_path: str) -> list[CandidateSchema]:
    path = Path(file_path)

    with open(path, "r", encoding="utf-8") as f:
        raw = f.read().strip()

    # FIX: detect format from content, not just suffix
    # A JSON array starts with '['; JSONL starts with '{'
    if raw.startswith("["):
        data = json.loads(raw)
        return [CandidateSchema.model_validate(item) for item in data]

    # JSONL — one JSON object per line
    candidates = []
    for line in raw.splitlines():
        line = line.strip()
        if not line:
            continue
        candidates.append(CandidateSchema.model_validate(json.loads(line)))

    return candidates