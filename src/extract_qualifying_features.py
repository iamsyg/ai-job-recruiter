# src/extract_qualifying_features.py
"""
Precompute-only. For each candidate, embeds each career role description
and attributes role duration_months to each domain when similarity
exceeds the threshold. Produces boolean flags + verified months from
actual work history, not self-reported skill durations.
"""

import numpy as np
from schema.candidate_schema import CandidateSchema
from utils.positive_signal_prototypes import POSITIVE_PROTOTYPES

# (floor, ceil)
CONF_THRESHOLDS = {
    "production_ml":             (0.55, 0.65),
    "information_retrieval":     (0.54, 0.64),
    "ranking_systems":           (0.55, 0.65),
    "vector_db":                 (0.56, 0.66),
    "embedding_retrieval":       (0.55, 0.65),
    "strong_opinions_retrieval": (0.52, 0.62),
}


def embed_positive_prototypes(model):
    return {
        group: model.encode(
            sentences,
            normalize_embeddings=True,
        )
        for group, sentences in POSITIVE_PROTOTYPES.items()
    }


def confidence(sim: float, floor: float, ceil: float) -> float:
    """
    Convert cosine similarity into [0,1].
    """
    return round(
        max(
            0.0,
            min(
                1.0,
                (sim - floor) / (ceil - floor),
            ),
        ),
        3,
    )


def extract_positive_signals(
    candidate: CandidateSchema,
    proto_vecs: dict,
    role_embeddings: list[np.ndarray],
):

    domain_months = {
        group: 0
        for group in POSITIVE_PROTOTYPES
    }

    domain_confidence = {
        group: 0.0
        for group in POSITIVE_PROTOTYPES
    }

    for role, role_vec in zip(candidate.career_history, role_embeddings):

        for group, pvecs in proto_vecs.items():

            sim = float(
                (role_vec @ pvecs.T).max()
            )

            floor, ceil = CONF_THRESHOLDS[group]

            conf = confidence(
                sim,
                floor,
                ceil,
            )

            # keep highest confidence observed
            domain_confidence[group] = max(
                domain_confidence[group],
                conf,
            )

            # only verified experience contributes months
            if conf >= 0.60:
                domain_months[group] += role.duration_months

    return {

        "production_ml_confidence": domain_confidence["production_ml"],
        "production_ml_months": domain_months["production_ml"],


        "ir_confidence": domain_confidence["information_retrieval"],
        "ir_months": domain_months["information_retrieval"],


        "ranking_confidence": domain_confidence["ranking_systems"],
        "ranking_months": domain_months["ranking_systems"],


        "vector_db_confidence": domain_confidence["vector_db"],
        "vector_db_months": domain_months["vector_db"],


        "embedding_retrieval_confidence": domain_confidence["embedding_retrieval"],
        "embedding_retrieval_months": domain_months["embedding_retrieval"],


        "strong_opinions_retrieval_confidence":  domain_confidence["strong_opinions_retrieval"],
        "strong_opinions_retrieval_months": domain_months["strong_opinions_retrieval"],
    }