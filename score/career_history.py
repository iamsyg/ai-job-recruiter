# score/career_history.py

from schema.candidate_features_schema import CareerHistory

def career_history_score(career_history: CareerHistory) -> float:
    """
    Compute a score for the candidate's career history based on various features.
    This is a placeholder implementation and should be replaced with actual scoring logic.
    """
    score = 0.0

    if career_history.career_gap_months > 3 and career_history.career_gap_months <= 6:
        score -= 0.1
    elif career_history.career_gap_months > 6:
        score -= 0.2
    else:
        score += 0.1

    if career_history.has_suspicious_career_dates:
        score -= 0.2
    else:
        score += 0.2

    if career_history.has_it_engineering_industry:
        score += 0.1
    else:
        score -= 0.1


    if career_history.startup_based_experience_months >= 36:
        score += 0.20
    elif career_history.startup_based_experience_months >= 20:
        score += 0.15
    elif career_history.startup_based_experience_months >= 12:
        score += 0.10

    if career_history.startup_based_experience_ratio >= 0.50:
        score += 0.20
    elif career_history.startup_based_experience_ratio >= 0.20:
        score += 0.10
    elif career_history.startup_based_experience_ratio >= 0.10:
        score += 0.05

    
    if career_history.product_based_experience_months >= 36:
        score += 0.30
    elif career_history.product_based_experience_months >= 24:
        score += 0.25
    elif career_history.product_based_experience_months >= 12:
        score += 0.15

    if career_history.product_based_experience_ratio >= 0.70:
        score += 0.20
    elif career_history.product_based_experience_ratio >= 0.50:
        score += 0.15
    elif career_history.product_based_experience_ratio >= 0.30:
        score += 0.10
    elif career_history.product_based_experience_ratio >= 0.10:
        score += 0.05

    
    if career_history.service_based_experience_months >= 60:
        score -= 0.15
    elif career_history.service_based_experience_months >= 36:
        score -= 0.10
    elif career_history.service_based_experience_months > 24:
        score -= 0.05

    # if career_history.service_based_experience_ratio >= 0.70:
    #     score -= 0.15
    # elif career_history.service_based_experience_ratio >= 0.50:
    #     score -= 0.10
    # elif career_history.service_based_experience_ratio >= 0.30:
    #     score -= 0.05

    if (
        career_history.service_based_experience_ratio >= 0.8
        and career_history.product_based_experience_ratio < 0.1
    ):
        score -= 0.15

    
    if career_history.unknown_company_experience_months >= 96:
        score -= 0.20
    elif career_history.unknown_company_experience_months >= 60:
        score -= 0.15
    elif career_history.unknown_company_experience_months >= 36:
        score -= 0.10
    elif career_history.unknown_company_experience_months >= 12:
        score -= 0.05

    if career_history.unknown_company_experience_ratio >= 0.80:
        score -= 0.20
    elif career_history.unknown_company_experience_ratio >= 0.50:
        score -= 0.15
    elif career_history.unknown_company_experience_ratio >= 0.30:
        score -= 0.10
    elif career_history.unknown_company_experience_ratio >= 0.10:
        score -= 0.05

    
    if career_history.tech_title_ratio >= 0.70:
        score += 0.20
    elif career_history.tech_title_ratio >= 0.50:
        score += 0.15
    elif career_history.tech_title_ratio >= 0.20:
        score += 0.10
    elif career_history.tech_title_ratio >= 0.10:
        score += 0.05

    
    if career_history.ai_ml_title_ratio >= 0.40:
        score += 0.30
    elif career_history.ai_ml_title_ratio >= 0.30:
        score += 0.25
    elif career_history.ai_ml_title_ratio >= 0.20:
        score += 0.20
    elif career_history.ai_ml_title_ratio >= 0.10:
        score += 0.15
    elif career_history.ai_ml_title_ratio >= 0.05:
        score += 0.10

    
    if career_history.current_title_match:
        score += 0.20
    else:
        score -= 0.10
    

    if career_history.current_ai_ml_title_match:
        score += 0.20


    if score > 1.0:
        score = 1.0
    elif score < 0:
        score = 0
    
    return score
    

    