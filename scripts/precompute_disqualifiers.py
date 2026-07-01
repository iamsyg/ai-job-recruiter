# scripts/precompute_disqualifiers.py

"""
Run once, offline, before ranking. Produces disqualifier_features.json
keyed by candidate_id. Loaded read-only by rank.py — no embedding calls
happen during the timed ranking step.
"""
import json
from model.embedding_model import EMBEDDING_MODEL
from src.extract_disqualifier_features import _embed_prototypes, extract_disqualifier_features
from utils.load_candidates import load_candidates

import numpy as np

candidates = load_candidates(file_path=r"C:\Users\Eternity\Dropbox\Projects\New folder\[PUB] India_runs_data_and_ai_challenge\[PUB] India_runs_data_and_ai_challenge\India_runs_data_and_ai_challenge\candidates.jsonl")

# embed_fn = lambda text: EMBEDDING_MODEL.encode(text, normalize_embeddings=True)

candidate_embeddings = np.load("candidate_embeddings.npy")
candidate_ids = np.load("candidate_ids.npy")

embedding_map = {
    str(candidate_id): embedding
    for candidate_id, embedding in zip(candidate_ids, candidate_embeddings)
}

proto_vecs = _embed_prototypes(EMBEDDING_MODEL)

out = {}
for candidate in candidates:
    out[candidate.candidate_id] = extract_disqualifier_features(
        candidate,
        proto_vecs,
        embedding_map[candidate.candidate_id],
    )

np.save(
    "disqualifier_features.npy",
    out,
    allow_pickle=True,
)