# scripts/precompute_qualify.py

import numpy as np
from collections import defaultdict

from model.embedding_model import EMBEDDING_MODEL
from utils.load_candidates import load_candidates
from src.extract_qualifying_features import embed_positive_prototypes, extract_positive_signals

candidates = load_candidates(file_path=r"C:\Users\Eternity\Dropbox\Projects\New folder\[PUB] India_runs_data_and_ai_challenge\[PUB] India_runs_data_and_ai_challenge\India_runs_data_and_ai_challenge\candidates.jsonl")
proto_vecs = embed_positive_prototypes(EMBEDDING_MODEL)

# Embed all role descriptions in one batched call — much faster than per-candidate
all_role_texts = []
role_index = []  # (candidate_idx, role_idx)

for c_idx, candidate in enumerate(candidates):
    for r_idx, role in enumerate(candidate.career_history):
        all_role_texts.append(role.description or "")
        role_index.append((c_idx, r_idx))

print(f"Embedding {len(all_role_texts)} role descriptions...")
all_role_vecs = EMBEDDING_MODEL.encode(
    all_role_texts,
    batch_size=128,
    normalize_embeddings=True,
    show_progress_bar=True,
)

# Rebuild per-candidate role embedding lists
candidate_role_vecs = defaultdict(list)
for (c_idx, r_idx), vec in zip(role_index, all_role_vecs):
    candidate_role_vecs[c_idx].append(vec)

out = {}
for c_idx, candidate in enumerate(candidates):
    out[candidate.candidate_id] = extract_positive_signals(
        candidate,
        proto_vecs,
        candidate_role_vecs[c_idx],
    )

np.save("qualifying_features.npy", out, allow_pickle=True)
print("Saved qualifying_features.npy")