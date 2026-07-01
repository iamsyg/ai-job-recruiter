# score/redrob_signals.py

from schema.candidate_features_schema import RedrobSignals

def redrob_signals_score(redrob_signals: RedrobSignals) -> float:
    """
    Calculate the redrob signals score based on the provided list of signals.

    Args:
        signals (list): A list of redrob signals.

    Returns:
        float: The calculated redrob signals score.
    """
    
    score = 0.0

    if redrob_signals.profile_completeness_category == "excellent":
        score += 0.05
    elif redrob_signals.profile_completeness_category == "good":
        score += 0.03
    elif redrob_signals.profile_completeness_category == "average":
        score += 0.01
    elif redrob_signals.profile_completeness_category == "poor":
        score -= 0.02


    if redrob_signals.invalid_activity_dates:
        score -= 0.10

    if redrob_signals.since_last_active_days is None:
        score -= 0.10
    elif redrob_signals.since_last_active_days < 30:
        score += 0.10
    elif redrob_signals.since_last_active_days < 60:
        score += 0.05
    elif redrob_signals.since_last_active_days < 90:
        score += 0.02
    else:
        score -= 0.05

    
    if redrob_signals.open_to_work_flag:
        score += 0.10
    else:
        score -= 0.05


    if redrob_signals.view_rate > 3:
        score += 0.20
    elif redrob_signals.view_rate > 1:
        score += 0.15
    elif redrob_signals.view_rate > 0.7:
        score += 0.10
    elif redrob_signals.view_rate > 0.4:
        score += 0.05


    if not redrob_signals.save_without_view_anomaly:
        if redrob_signals.save_rate > 0.5:
            score += 0.20
        elif redrob_signals.save_rate > 0.3:
            score += 0.10
        elif redrob_signals.save_rate > 0.1:
            score += 0.05

    else:
        score -= 0.15


    
    if redrob_signals.recruiter_interest > 30:
        score += 0.20
    elif redrob_signals.recruiter_interest > 20:
        score += 0.17
    elif redrob_signals.recruiter_interest > 15:
        score += 0.15
    elif redrob_signals.recruiter_interest > 10:
        score += 0.13
    elif redrob_signals.recruiter_interest > 5:
        score += 0.10


    if redrob_signals.recruiter_response_rate >= 0.70:
        score += 0.20
    elif redrob_signals.recruiter_response_rate >= 0.50:
        score += 0.15
    elif redrob_signals.recruiter_response_rate >= 0.30:
        score += 0.10
    elif redrob_signals.recruiter_response_rate >= 0.10:    
        score += 0.05
    elif redrob_signals.avg_response_time_hours > 96:
        score -= 0.10
    

    if redrob_signals.avg_response_time_hours <= 24:
        score += 0.10
    elif redrob_signals.avg_response_time_hours <= 48:
        score += 0.05
    elif redrob_signals.avg_response_time_hours <= 72:
        score += 0.02
    else:
        score -= 0.05

    if redrob_signals.connection_count > 500:
        score += 0.10
    elif redrob_signals.connection_count > 300: 
        score += 0.07
    elif redrob_signals.connection_count > 100:
        score += 0.05

    
    if redrob_signals.endorsements_received > 50:
        score += 0.10
    elif redrob_signals.endorsements_received > 30:
        score += 0.07
    elif redrob_signals.endorsements_received > 10:
        score += 0.05

    
    if redrob_signals.notice_period_gap == 0:
        score += 0.12
    elif redrob_signals.notice_period_gap < 15:
        score += 0.10
    elif redrob_signals.notice_period_gap < 30:
        score += 0.05
    elif redrob_signals.notice_period_gap < 60:
        score -= 0.05
    else:
        score -= 0.10


    if redrob_signals.salary_gap is not None:
        if redrob_signals.salary_gap < 1:
            score += 0.10
        elif redrob_signals.salary_gap < 3:
            score += 0.05
        elif redrob_signals.salary_gap < 5:
            score -= 0.05
        else:
            score -= 0.10

    
    if redrob_signals.work_mode_match:
        score += 0.10
    elif redrob_signals.work_mode_match is False:
        score -= 0.05


    if redrob_signals.github_linked:

        if redrob_signals.github_activity_score > 50:
            score += 0.20
        elif redrob_signals.github_activity_score > 30:
            score += 0.15
        elif redrob_signals.github_activity_score > 10:
            score += 0.10
        else:
            score -= 0.05

    else:
        score -= 0.20


    if redrob_signals.interview_completion_rate > 0.8:
        score += 0.10
    elif redrob_signals.interview_completion_rate > 0.5:
        score += 0.05
    elif redrob_signals.interview_completion_rate < 0.3:
        score -= 0.05
    

    if redrob_signals.has_offer_history:
        if redrob_signals.offer_acceptance_rate > 0.8:
            score += 0.10
        elif redrob_signals.offer_acceptance_rate > 0.5:
            score += 0.05
        elif redrob_signals.offer_acceptance_rate > 0.2:
            score += 0.02
        else:
            score -= 0.05


    IMPORTANT_ASSESSMENTS = {
        "retrieval",
        "vector_db",
        "search_ranking",
        "llm",
        "ml"
    }

    if redrob_signals.assessment_features:

        for assessment, features in redrob_signals.assessment_features.items():

            if assessment not in IMPORTANT_ASSESSMENTS:
                continue

            # avg_score = features["avg_score"]

            # if avg_score >= 80:
            #     score += 0.10

            # elif avg_score >= 50:
            #     score += 0.05

            # elif avg_score > 0 and avg_score < 30:
            #     score -= 0.05

            max_score = features["max_score"]

            if max_score >= 80:
                score += 0.10

            elif max_score >= 50:
                score += 0.05

            elif max_score > 0 and max_score < 30:
                score -= 0.05
    

    if redrob_signals.verified_email:
        score += 0.02

    if redrob_signals.verified_phone:
        score += 0.02

    if redrob_signals.linkedin_connected:
        score += 0.02

    if not redrob_signals.verified_email and not redrob_signals.verified_phone and not redrob_signals.linkedin_connected:
        score -= 0.15

    return score

    