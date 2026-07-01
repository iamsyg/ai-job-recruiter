# score/disqualifiers.py

from schema.candidate_features_schema import Disqualifiers

def disqualifier_penalty_multiplier(flags: Disqualifiers) -> float:
    """Returns a multiplier in (0, 1] applied to final_feature_score."""
    penalty = 0.0
    penalty += flags.research_only_confidence * 0.35
    penalty += flags.architecture_no_code_confidence * 0.25
    penalty += flags.langchain_wrapper_only_confidence * 0.30
    penalty += flags.cv_speech_robotics_without_nlp_confidence * 0.20
    penalty += flags.job_hopper_confidence * 0.15

    # if flags["consulting_only_disqualified"]:
    #     penalty += 0.6  # hard rule from JD, near-disqualifying

    multiplier = max(0.05, 1.0 - penalty)
    return multiplier