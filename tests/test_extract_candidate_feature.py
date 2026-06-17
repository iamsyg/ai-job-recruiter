# tests/test_extract_candidate_feature.py

import json

from src.extract_candidate_features import extract_candidate_features
from schema.candidate_schema import CandidateSchema

with open(r"C:\Users\Eternity\Dropbox\Projects\New folder\[PUB] India_runs_data_and_ai_challenge\[PUB] India_runs_data_and_ai_challenge\India_runs_data_and_ai_challenge\sample_candidates.json", "r", encoding="utf-8") as f:
    candidates_json = json.load(f)

candidates = [
    CandidateSchema.model_validate(candidate)
    for candidate in candidates_json
]

features = [
    extract_candidate_features(candidate)
    for candidate in candidates
]

print(features[0])