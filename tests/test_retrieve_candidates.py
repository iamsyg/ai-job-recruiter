# tests/test_retrieve_candidates.py

import json
import numpy as np

from schema.candidate_schema import CandidateSchema
from src.generate_jd_embeddings import generate_jd_embeddings
from src.extract_jd_features import extract_jd_features
from src.retrieve_candidates import retrieve_candidates
from utils.jd import jd


# ------------------------
# Load candidates
# ------------------------

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


# ------------------------
# Generate candidate embeddings (Run once)
# ------------------------

# generate_candidate_embeddings(candidates)

print(np.load("candidate_embeddings.npy").shape)


# ------------------------
# Generate JD embedding
# ------------------------

jd_schema = extract_jd_features(jd())

jd_embedding = generate_jd_embeddings(jd_schema)


# ------------------------
# Retrieve candidates
# ------------------------

candidate_ids, scores = retrieve_candidates(jd_embedding)

print("Top 10 candidates\n")

for cid, score in zip(candidate_ids[:10], scores[:10]):
    print(cid, round(float(score), 4))