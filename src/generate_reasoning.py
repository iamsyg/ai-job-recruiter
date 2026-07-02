# src/generate_reasoning.py

from schema.candidate_features_schema import CandidateFeatures
from schema.candidate_schema import CandidateSchema


def generate_reasoning(candidate: CandidateSchema, features: CandidateFeatures):

    strengths = []
    concerns = []




# ==================================================== Profile =====================================================

    if not features.profile.country_match:
        concerns.append("Country not matched with job description.")


    if features.profile.willing_to_relocate:
        if not features.profile.location_match:
            concerns.append("Willing to relocate but location not matched with job description.")
    else:
        concerns.append("Not willing to relocate and location not matched with job description.")


    if not features.profile.employment_eligibility_match:
        concerns.append("Not eligible for employment.")


    if candidate.profile.years_of_experience >= 5:
        strengths.append(
            f"{candidate.profile.years_of_experience:.1f} years of professional experience."
        )





# ===================================================== Career History =====================================================

    if features.career_history.has_suspicious_career_dates:
        concerns.append(
            "Career history has suspicious dates."
        )

    if features.career_history.startup_based_experience_months >= 12:
        strengths.append(
            f"Extensive experience in startup-based companies ({features.career_history.startup_based_experience_months} months)."
        )

    if features.career_history.product_based_experience_months >= 12:
        strengths.append(
            f"Extensive experience in product-based companies ({features.career_history.product_based_experience_months} months)."
        )
    else:
        concerns.append(
            "Limited experience in product-based companies."
        )

    if features.career_history.service_based_experience_months >= 48:
        concerns.append(
            f"Extensive experience in service-based companies ({features.career_history.service_based_experience_months} months)."
        )

    if features.career_history.unknown_company_experience_months > 0:
        concerns.append(
            f"Experience in unknown companies ({features.career_history.unknown_company_experience_months} months)."
        )

    if (
        features.career_history.current_ai_ml_title_match
        and features.qualifiers.production_ml_confidence < 0.70
    ):
        strengths.append(
            f"Current role '{candidate.profile.current_title}' is directly relevant."
        )

    if (
        features.career_history.ai_ml_title_ratio >= 0.20
        and features.qualifiers.production_ml_confidence < 0.70
    ):
        strengths.append(
            "Has considerable experience in AI/ML roles."
        )

    if features.career_history.tech_title_ratio >= 0.70:
        strengths.append(
            "Consistent technical career progression."
        )




# ============================================================ CERTIFICATIONS ============================================================

    if features.certifications.ai_ml_cert_count >= 2:
        strengths.append(
            "Has multiple AI/ML certifications."
        )
    
    if features.certifications.cloud_cert_count >= 2:
        strengths.append(
            "Has multiple cloud certifications."
        )

    if features.certifications.suspicious_certifications:
        concerns.append(
            "Certifications appear suspicious."
        )





# ============================================================= Education =============================================================

    if features.education.relevant_grade_category == "excellent":
        strengths.append(
            "Excellent academic performance."
        )

    if features.education.relevant_tier == "unknown":
        concerns.append(
            "Educational institution tier is unknown."
        )

    if features.education.has_suspicious_education_dates:
        concerns.append(
            "Education history has suspicious dates."
        )




# ============================================================ Redrob Signals =======================================================

    if features.redrob_signals.invalid_activity_dates:
        concerns.append(
            "Redrob signals indicate invalid activity dates."
        )

    if features.redrob_signals.since_last_active_days is None:
        concerns.append(
            "Redrob signals indicate no recent activity."
        )
    elif features.redrob_signals.since_last_active_days > 90:
        concerns.append(
            "Redrob signals indicate inactivity for more than 90 days."
        )
    elif features.redrob_signals.since_last_active_days < 30:
        strengths.append(
            "Redrob signals indicate recent activity."
        )

    if not features.redrob_signals.open_to_work_flag:
        concerns.append(
            "Redrob signals indicate not open to work."
        )

    if features.redrob_signals.notice_period_gap > 30:
        concerns.append(
            "Redrob signals indicate a long notice period."
        )

    if features.redrob_signals.work_mode_match is False:
        concerns.append(
            "Redrob signals indicate work mode mismatch."
        )

    if features.redrob_signals.github_linked is False:
        concerns.append(
            "Redrob signals indicate GitHub not linked."
        )
    elif features.redrob_signals.github_activity_score >= 30:
        strengths.append(
            "Redrob signals indicate high GitHub activity."
        )
    else:
        concerns.append(
            "Redrob signals indicate low GitHub activity."
        )

    if features.redrob_signals.has_offer_history:
        if features.redrob_signals.offer_acceptance_rate >= 0.70:
            strengths.append(
                "Redrob signals indicate good offer acceptance history."
            )
    
    if features.redrob_signals.assessment_features:
        strengths.append(
            "Redrob signals indicate candidate has given assessments."
        )

    if not features.redrob_signals.verified_email and not features.redrob_signals.verified_phone and not features.redrob_signals.linkedin_connected:
        concerns.append(
            "Redrob signals indicate unverified contact information."
        )





    
# ============================================================ Disqualifiers ============================================================

    d = features.disqualifiers

    if d.research_only_confidence >= 0.70:
            concerns.append(
                "Experience is primarily research-oriented rather than production-oriented."
            )

    if d.architecture_no_code_confidence >= 0.70:
        concerns.append(
            "Recent experience appears more architectural than hands-on."
        )

    if d.langchain_wrapper_only_confidence >= 0.70:
        concerns.append(
            "AI experience may rely heavily on existing LLM frameworks."
        )

    if d.cv_speech_robotics_without_nlp_confidence >= 0.70:
        concerns.append(
            "Experience is primarily Computer Vision/Speech rather than Retrieval/NLP."
        )

    if d.job_hopper_confidence >= 0.70:
        concerns.append(
            "Frequent short job tenures."
        )





# =========================================================Qualifiers=================================================

    q = features.qualifiers

    if q.production_ml_confidence >= 0.70:
        strengths.append(
            f"Built production ML systems ({q.production_ml_months} months, confidence {q.production_ml_confidence:.0%})."
        )

    if q.ir_confidence >= 0.70:
        strengths.append(
            f"Hands-on experience building information retrieval systems ({q.ir_months} months, confidence {q.ir_confidence:.0%})."
        )

    if q.embedding_retrieval_confidence >= 0.70:
        strengths.append(
            f"Strong experience designing embedding-based retrieval pipelines ({q.embedding_retrieval_months} months, confidence {q.embedding_retrieval_confidence:.0%})."
        )

    if q.vector_db_confidence >= 0.70:
        strengths.append(
            f"Production experience with vector databases ({q.vector_db_months} months, confidence {q.vector_db_confidence:.0%})."
        )

    if q.ranking_confidence >= 0.70:
        strengths.append(
            f"Built ranking/re-ranking systems with verified production experience ({q.ranking_months} months, confidence {q.ranking_confidence:.0%})."
        )

    if q.strong_opinions_retrieval_confidence >= 0.70:
        strengths.append(
            f"Demonstrates strong understanding of retrieval architecture and ranking trade-offs (confidence {q.strong_opinions_retrieval_confidence:.0%})."
        )

    # Bonus when the complete retrieval stack is present
    if (
        q.production_ml_confidence >= 0.70
        and q.embedding_retrieval_confidence >= 0.70
        and q.ranking_confidence >= 0.70
    ):
        strengths.append(
            "Built production-scale search, retrieval, and ranking systems."
        )






# ========================================================= Summary ============================================================

    if len(concerns) <= 3:
        summary = (
            "Excellent overall fit with strong production experience and no major concerns."
        )
    elif len(concerns) <= 5:
        summary = (
            "Strong candidate with a few considerations."
        )
    else:
        summary = (
            "Relevant candidate but several concerns require manual review."
        )

    return {
        "strengths": strengths,
        "concerns": concerns,
        "summary": summary,
    }