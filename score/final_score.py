# score/final_score.py

from score.career_history import career_history_score
from score.skills import skills_score
from score.education import education_score
from score.profile import profile_score
from score.certification import certification_score
from score.language import language_score
from score.redrob_signals import redrob_signals_score
from score.disqualifiers import disqualifier_penalty_multiplier
from score.qualify import qualify_candidate

from schema.candidate_features_schema import CandidateFeatures

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


def final_feature_score(features: CandidateFeatures):

    is_honeypot_suspect = (
        features.career_history.has_suspicious_career_dates
        or features.education.has_suspicious_education_dates
        or features.redrob_signals.invalid_activity_dates
        or features.certifications.suspicious_certifications
    )

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
        certification_score(features.certifications),
        0.0,
        0.20
    )

    language = normalize(
        language_score(features.is_english_proficient),
        0,
        0.10
    )

    redrob = normalize(
        redrob_signals_score(features.redrob_signals),
        -0.8,
        1.67
    )

    qualify = qualify_candidate(features.qualifiers)

    final = (
        career   * 0.25 +
        skills   * 0.20 +
        qualify  * 0.20 +  
        redrob   * 0.15 +
        education * 0.10 +
        profile  * 0.05 +
        certification * 0.03 +
        language * 0.02
    )

    if is_honeypot_suspect:
        final *= 0.20

    # if hasattr(features, "disqualifiers"):
    #     final *= disqualifier_penalty_multiplier(features.disqualifiers)
    #     # item 1.7: discount self-reported production claims when unverifiable
    #     final *= (1.0 - 0.5 * features.disqualifiers["verifiability_discount"])

    final *= disqualifier_penalty_multiplier(features.disqualifiers)

    return final