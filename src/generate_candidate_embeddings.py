# src/generate_candidate_embeddings.py

import numpy as np

from src.build_candidate_text import build_candidate_text
from schema.candidate_schema import CandidateSchema


def generate_candidate_embeddings(candidates: list[CandidateSchema], EMBEDDING_MODEL):

    texts = []
    candidate_ids = []

    for candidate in candidates:

        text = build_candidate_text(candidate)

        texts.append(text)
        candidate_ids.append(candidate.candidate_id)

    embeddings = EMBEDDING_MODEL.encode(
        texts,
        batch_size=64,
        normalize_embeddings=True,
        show_progress_bar=True
    )

    np.save(
        "candidate_embeddings.npy",
        embeddings
    )

    np.save(
        "candidate_ids.npy",
        candidate_ids
    )

    return embeddings, candidate_ids

# embeddings = model.encode(texts)



from model.embedding_model import EMBEDDING_MODEL


def generate_candidate_embedding(candidate):
    """
    Generate embedding for a single candidate.
    """

    text = build_candidate_text(candidate)

    embedding = EMBEDDING_MODEL.encode(
        text,
        normalize_embeddings=True,
        show_progress_bar=True
    )

    return embedding