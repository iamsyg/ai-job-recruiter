# score/qualify.py

from schema.candidate_features_schema import Qualifiers


def qualify_candidate(ps: Qualifiers) -> float:

    score = 0.0

    # ── production ML ── highest weight, JD hard requirement
    if ps.production_ml_confidence > 0:
        score += ps.production_ml_confidence * 0.20
        if ps.production_ml_months >= 36:   score += 0.15
        elif ps.production_ml_months >= 24: score += 0.10
        elif ps.production_ml_months >= 12: score += 0.05

    # ── embedding retrieval ── JD hard requirement
    if ps.embedding_retrieval_confidence > 0:
        score += ps.embedding_retrieval_confidence * 0.20
        if ps.embedding_retrieval_months >= 24: score += 0.12
        elif ps.embedding_retrieval_months >= 12: score += 0.07

    # ── ranking systems ── JD hard requirement (eval frameworks)
    if ps.ranking_confidence > 0:
        score += ps.ranking_confidence * 0.15
        if ps.ranking_months >= 24: score += 0.10
        elif ps.ranking_months >= 12: score += 0.05

    # ── vector DB ── JD hard requirement
    if ps.vector_db_confidence > 0:
        score += ps.vector_db_confidence * 0.15
        if ps.vector_db_months >= 18: score += 0.08
        elif ps.vector_db_months >= 12: score += 0.04

    # ── information retrieval ── strong supporting signal
    if ps.ir_confidence > 0:
        score += ps.ir_confidence * 0.10
        if ps.ir_months >= 24: score += 0.07
        elif ps.ir_months >= 12: score += 0.03

    # ── strong opinions ── soft differentiator, no months bonus
    score += ps.strong_opinions_retrieval_confidence * 0.08

    # ── combo bonus: all three core signals present at meaningful confidence
    has_retrieval_stack = (
        ps.production_ml_confidence >= 0.50
        and ps.embedding_retrieval_confidence >= 0.50
        and ps.ranking_confidence >= 0.50
    )
    if has_retrieval_stack:
        score += 0.15

    return min(score, 1.0)