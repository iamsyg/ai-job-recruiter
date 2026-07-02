# src/rerank.py

from schema.candidate_features_schema import CandidateFeatures

from src.extract_candidate_features import (
    extract_career_history_features,
    extract_skills_features,
    extract_education_features,
    extract_profile_features,
    extract_certification_features,
    extract_language_features,
    extract_redrob_signals,
)

from score.final_score import final_feature_score, normalize

from src.generate_reasoning import generate_reasoning

import numpy as np


def rerank_candidates(
    candidate_ids,
    embedding_score_map,
    bm25_score_map,
    candidate_map,
    jd_schema,
    qualifier_map,
    disqualifier_map,
):
    """
    Rerank retrieved candidates using handcrafted features.

    Returns:
        List[dict]
    """

    results = []

    bm25_min = min(bm25_score_map.values())
    bm25_max = max(bm25_score_map.values())

    # disqualifier_map = np.load(
    #     "disqualifier_features.npy",
    #     allow_pickle=True,
    # ).item()

    # qualifier_map = np.load(
    #     "qualifying_features.npy",
    #     allow_pickle=True,
    # ).item()

    for candidate_id in candidate_ids:

        candidate = candidate_map[candidate_id]

        features = CandidateFeatures(

            career_history=extract_career_history_features(candidate),

            skills=extract_skills_features(candidate),

            education=extract_education_features(candidate),

            profile=extract_profile_features(
                candidate=candidate,
                jd_features=jd_schema,
            ),

            certifications=extract_certification_features(candidate),

            is_english_proficient=extract_language_features(candidate),

            redrob_signals=extract_redrob_signals(candidate, jd_features=jd_schema),

            disqualifiers=disqualifier_map[candidate_id],

            qualifiers=qualifier_map[candidate_id]
        )

        feature_score = final_feature_score(features)

        if (
            not features.profile.location_match
            and not features.profile.willing_to_relocate
        ):
            feature_score *= 0.60

        embedding_score = float(
            embedding_score_map[candidate_id]
        )

        bm25_score = normalize(
            bm25_score_map[candidate_id],
            bm25_min,
            bm25_max
        )

        reasoning = generate_reasoning(
            candidate=candidate,
            features=features,
        )

        final_score = (
            embedding_score * 0.40 +
            bm25_score * 0.15 +
            feature_score * 0.45
        )

        # if candidate_id in {
        #     "CAND_0007411",
        #     "CAND_0088025",
        #     "CAND_0011687",
        # }:
        #     print(candidate_id)
        #     print(features.disqualifiers)
        #     print(feature_score)

        #     print("\n \n \n")

        results.append(
            {
                "candidate_id": candidate_id,
                "embedding_score": round(embedding_score, 3),
                "bm25_score": round(bm25_score, 3),
                "feature_score": round(feature_score, 3),
                "final_score": round(final_score, 3),
                "reasoning": reasoning,
            }
        )

    results.sort(
        key=lambda x: (-x["final_score"], x["candidate_id"])
    )

    return results