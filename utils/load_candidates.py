# utils/load_candidates.py

from schema.candidate_schema import CandidateSchema
import json

candidates = []

def load_candidates(file_path: str) -> list[CandidateSchema]:

    with open(
        file_path,
        encoding="utf-8",
    ) as f:

        for line in f:
            candidates.append(
                CandidateSchema.model_validate(
                    json.loads(line)
                )
            )

    return candidates

    