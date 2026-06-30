# score/final_score.py

from score.career_history import career_history_score
from score.skills import skills_score
from score.education import education_score
from score.profile import profile_score
from score.certification import certification_score
from score.language import language_score
from score.redrob_signals import redrob_signals_score


def normalize(score: float, minimum: float, maximum: float) -> float:
    """
    Normalize a score to [0,1].
    """
    value = (score - minimum) / (maximum - minimum)

    if value < 0:
        return 0.0

    if value > 1:
        return 1.0

    return value


def final_feature_score(features):

    career = normalize(
        career_history_score(features.career_history),
        0,
        1
    )

    skills = normalize(
        skills_score(features.skills),
        0.0,
        1.623
    )

    education = normalize(
        education_score(features.education),
        0.125,
        0.375
    )

    profile = normalize(
        profile_score(features.profile),
        -0.25,
        0.25
    )

    certification = normalize(
        certification_score(features.certification),
        0.0,
        0.20
    )

    language = normalize(
        language_score(features.language),
        0,
        0.10
    )

    redrob = normalize(
        redrob_signals_score(features.redrob_signals),
        -0.6,
        1.67
    )

    final = (
        career * 0.35 +
        skills * 0.25 +
        redrob * 0.15 +
        education * 0.12 +
        profile * 0.08 +
        certification * 0.05 +
        language * 0.02
    )

    return final