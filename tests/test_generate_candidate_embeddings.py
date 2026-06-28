# tests/test_generate_candidate_embeddings.py

from src.generate_candidate_embeddings import generate_candidate_embeddings
from schema.candidate_schema import CandidateSchema
import json

candidates = []

with open(
    r"C:\Users\Eternity\Dropbox\Projects\New folder\[PUB] India_runs_data_and_ai_challenge\[PUB] India_runs_data_and_ai_challenge\India_runs_data_and_ai_challenge\candidates.jsonl",
    "r",
    encoding="utf-8",
) as f:

    for line in f:
        candidates.append(
            CandidateSchema.model_validate(
                json.loads(line)
            )
        )

generate_candidate_embeddings(candidates)