# utils/load_candidates.py

import json
from pathlib import Path

from schema.candidate_schema import CandidateSchema


def load_candidates(file_path: str) -> list[CandidateSchema]:
    """
    Supports both:
    - candidates.jsonl
    - sample_candidates.json
    """

    candidates = []

    path = Path(file_path)

    with open(path, "r", encoding="utf-8") as f:

        if path.suffix.lower() == ".json":
            # JSON array
            data = json.load(f)

            candidates = [
                CandidateSchema.model_validate(item)
                for item in data
            ]

        else:
            # JSONL
            for line in f:
                line = line.strip()

                if not line:
                    continue

                candidates.append(
                    CandidateSchema.model_validate(
                        json.loads(line)
                    )
                )

    return candidates