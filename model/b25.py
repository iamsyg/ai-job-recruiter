# model/bm25.py

import pickle
import re

import numpy as np
from rank_bm25 import BM25Okapi

from schema.candidate_schema import CandidateSchema
from src.build_candidate_text import build_candidate_text


def tokenize(text: str) -> list[str]:
    """Lowercase and remove punctuation."""
    return re.findall(r"\b\w+\b", text.lower())


def build_bm25(candidates: list[CandidateSchema], save: bool = False) -> BM25Okapi:
    """
    Build BM25 index from candidate documents.
    """

    documents = [
        build_candidate_text(candidate)
        for candidate in candidates
    ]

    tokenized_documents = [
        tokenize(doc)
        for doc in documents
    ]

    candidate_ids = np.array(
        [candidate.candidate_id for candidate in candidates]
    )

    if save:
        np.save("candidate_ids.npy", candidate_ids)

    bm25 = BM25Okapi(tokenized_documents)

    return bm25, candidate_ids


def save_bm25(bm25: BM25Okapi, path: str = "bm25.pkl") -> None:
    """
    Save BM25 index.
    """

    with open(path, "wb") as f:
        pickle.dump(bm25, f)


def load_bm25(path: str = "bm25.pkl") -> BM25Okapi:
    """
    Load BM25 index.
    """

    with open(path, "rb") as f:
        return pickle.load(f)


def retrieve_bm25(
    query: str,
    bm25: BM25Okapi,
    candidate_ids,
    top_k: int = 1000,
):
    """
    Retrieve Top-K candidates using BM25.
    """

    tokens = tokenize(query)

    scores = bm25.get_scores(tokens)

    # candidate_ids = np.load("candidate_ids.npy")

    k = min(top_k, len(scores))

    top_idx = np.argpartition(scores, -k)[-k:]
    top_idx = top_idx[np.argsort(scores[top_idx])[::-1]]

    top_candidate_ids = candidate_ids[top_idx]
    top_scores = scores[top_idx]

    return top_candidate_ids, top_scores