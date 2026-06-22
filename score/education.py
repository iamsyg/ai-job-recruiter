# score/education.py

from schema.candidate_features_schema import Education

def education_score(education: Education) -> float:
    """
    Calculate the education score based on the provided Education object.

    Args:
        education (Education): An instance of the Education class containing academic details.

    Returns:
        float: The calculated education score.
    """

    score = 0.0
    
    if education.relevant_grade_category == "unknown":
        score = 0.0
    elif education.relevant_grade_category == "excellent":
        score = 0.10
    elif education.relevant_grade_category == "good":
        score = 0.07
    elif education.relevant_grade_category == "average":
        score = 0.05
    elif education.relevant_grade_category == "poor":
        score = 0.02

    
    if education.relevant_tier == "Unknown":
        score += 0.0
    elif education.relevant_tier == "tier_1":
        score += 0.10
    elif education.relevant_tier == "tier_2":
        score += 0.08
    elif education.relevant_tier == "tier_3":
        score += 0.06
    elif education.relevant_tier == "tier_4":
        score += 0.03


    score += education.max_field_of_study_score * 0.10
    score += education.max_degree_score * 0.05


    if education.has_suspicious_education_dates:
        score -= 0.10
    

    return score