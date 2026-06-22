# score/profile.py

from schema.candidate_features_schema import Profile

def profile_score(profile: Profile) -> float:
    """
    Compute a score for the candidate profile based on various features.
    This is a placeholder implementation and should be replaced with actual scoring logic.
    """
    score = 0.0


    if profile.country_match:
        if profile.location_match:
            score += 0.1
        else:
            if profile.willing_to_relocate:
                score += 0.05
            else:
                score -= 0.2
    else:
        score -= 0.2


    if profile.experience_gap <= 1:
        score += 0.10
    elif profile.experience_gap <= 2:
        score += 0.00
    elif profile.experience_gap <= 4:
        score += -0.10
    else:
        return -0.20


    if profile.employment_eligibility_match:
        score += 0.05
    else:
        score -= 0.1


    return score