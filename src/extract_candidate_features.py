# src/extract_candidate_features.py

from datetime import datetime

from schema.candidate_schema import CandidateSchema

from utils.company_type_mapping import COMPANY_TYPE_MAP, STARTUP_SIZES
from utils.career_industry_mapping import IT_ENGINEERING_INDUSTRIES, IT_INDUSTRY_KEYWORDS
from utils.career_title import TECH_TITLES, AI_ML_TITLES, TECH_TITLE_KEYWORDS, AI_ML_TITLE_KEYWORDS

from utils.education.field_of_study_map import FIELD_OF_STUDY_SCORE
from utils.education.degree import DEGREE_SCORE

from utils.skills.skill_names import SKILL_TAXONOMY, PROFICIENCY_MAP

from utils.certificates.certificates import CLOUD_CERT_KEYWORDS, AI_ML_CERT_KEYWORDS, CLOUD_CERTS, AI_ML_CERTS

from utils.redrob_signals.skill_assessment_taxonomy import SKILL_ASSESSMENT_TAXONOMY

def is_tech_title(title: str) -> bool:

    title = title.strip().lower()

    if title in TECH_TITLES:
        return True

    return any(
        keyword in title
        for keyword in TECH_TITLE_KEYWORDS
    )


def is_ai_ml_title(title: str) -> bool:

    title = title.strip().lower()

    if title in AI_ML_TITLES:
        return True

    return any(
        keyword in title
        for keyword in AI_ML_TITLE_KEYWORDS
    )


def is_it_industry(industry: str) -> bool:

    industry = industry.strip().lower()

    if industry in IT_ENGINEERING_INDUSTRIES:
        return True

    return any(
        keyword in industry
        for keyword in IT_INDUSTRY_KEYWORDS
    )





def categorize_grade(grade):

    if grade is None:
        return "unknown"

    grade = str(grade).strip().lower()

    try:
      
        if grade[0] >= "8":
            return "excellent"
        elif grade[0] >= "7":
            return "good"
        elif grade[0] >= "6":
            return "average"
        else:
            return "poor"

    except ValueError:
        return "unknown"








def extract_candidate_features(candidate: CandidateSchema, jd_features):

    # skills = [s.name for s in candidate.skills]

    career_text = "\n".join(
        role.description
        for role in candidate.career_history
    )

    summary_text = candidate.profile.summary

    # =================================================== PROFILE ================================

    candidate_city = candidate.profile.location.split(",")[0].strip().lower()

    location_match = any(
        candidate_city == loc.lower()
        for loc in (
            jd_features["preferred_locations"] +
            jd_features["additional_locations"]
        )
    )

    # print(f"candidate matches location: {location_match} - candidate city: {candidate_city}")

    experience_match = (
        jd_features["experience_required"]["min"]
        <= candidate.profile.years_of_experience
        <= jd_features["experience_required"]["max"]
    )

    country_match = (
        candidate.profile.country.lower() == "india"
    )

    profile = {
        "candidate_id": candidate.candidate_id,
        "location_match": location_match,
        "willing_to_relocate": candidate.redrob_signals.willing_to_relocate,
        "country_match": country_match,
        "experience_match": experience_match,
        "summary_text": summary_text,
    }

    # =================================================== CAREER HISTORY ================================

    startup_based_experience = sum(
        1
        for role in candidate.career_history
        if role.company_size in STARTUP_SIZES
    )

    start_based_experience_months = sum(
        role.duration_months
        for role in candidate.career_history
        if role.company_size in STARTUP_SIZES
    )

    start_up_based_experience_ratio = startup_based_experience / len(candidate.career_history) if len(candidate.career_history) > 0 else 0

    product_based_experience = sum(
        1
        for role in candidate.career_history
        if COMPANY_TYPE_MAP.get(role.company.strip().lower()) == "product"
    )

    product_based_experience_months = sum(
        role.duration_months
        for role in candidate.career_history
        if COMPANY_TYPE_MAP.get(role.company.strip().lower()) == "product"
    )

    product_based_experience_ratio = product_based_experience / len(candidate.career_history) if len(candidate.career_history) > 0 else 0

    service_based_experience = sum(
        1
        for role in candidate.career_history
        if COMPANY_TYPE_MAP.get(role.company.strip().lower()) == "service"
    )

    service_based_experience_months = sum(
        role.duration_months
        for role in candidate.career_history
        if COMPANY_TYPE_MAP.get(role.company.strip().lower()) == "service"
    )

    service_based_experience_ratio = service_based_experience / len(candidate.career_history) if len(candidate.career_history) > 0 else 0

    unknown_company_experience = sum(
        1
        for role in candidate.career_history
        if COMPANY_TYPE_MAP.get(role.company.strip().lower()) == "unknown"
    )

    unknown_company_experience_months = sum(
        role.duration_months
        for role in candidate.career_history
        if COMPANY_TYPE_MAP.get(role.company.strip().lower()) == "unknown"
    )

    unknown_company_experience_ratio = unknown_company_experience / len(candidate.career_history) if len(candidate.career_history) > 0 else 0

    career_gap_months = 0

    roles = sorted (
        candidate.career_history,
        key=lambda x: datetime.strptime(x.start_date, "%Y-%m-%d"),
    )

    for i in range(len(roles) - 1):

        prev_role = roles[i]
        next_role = roles[i + 1]

        if prev_role.end_date and next_role.start_date:

            prev_end = datetime.strptime(
                prev_role.end_date,
                "%Y-%m-%d"
            )

            next_start = datetime.strptime(
                next_role.start_date,
                "%Y-%m-%d"
            )

            gap_days = (next_start - prev_end).days

            # print(f"Gap between {prev_role.title} and {next_role.title}: {gap_days} days")

            if gap_days > 30:
                career_gap_months += gap_days // 30
    
    # print(f"Total career gap in months: {career_gap_months}")

    suspicious_career_date_records = any(
        (
            role.start_date is None and role.end_date is not None
        )
        or
        (
            role.start_date is None and role.end_date is None
        )
        for role in candidate.career_history
    )

    # Less weightage than tech_industry_months
    has_it_engineering_industry = any(
        is_it_industry(role.industry)
        for role in candidate.career_history
    )

    tech_title_months = sum(
        role.duration_months
        for role in candidate.career_history
        if is_tech_title(role.title)
    )

    total_experience_months = sum(
        role.duration_months
        for role in candidate.career_history
    )

    tech_title_ratio = tech_title_months / total_experience_months if total_experience_months > 0 else 0

    current_title_match = is_tech_title(
        candidate.profile.current_title
    )

    ai_ml_title_months = sum(
        role.duration_months
        for role in candidate.career_history
        if is_ai_ml_title(role.title)
    )

    total_tech_experience_months = tech_title_months

    ai_ml_title_ratio = ai_ml_title_months / total_tech_experience_months if total_tech_experience_months > 0 else 0

    current_ai_ml_title_match = is_ai_ml_title(
        candidate.profile.current_title
    )

    # NOTE: match if career industry and career title is aligned with description or not (ON HOLD)

    career_history = {

            "career_gap_months": career_gap_months,
            "has_suspicious_career_dates": suspicious_career_date_records,

            "has_it_engineering_industry": has_it_engineering_industry,
            # "tech_industry_months": tech_industry_months,

            "start_up_based_experience": startup_based_experience,
            "startup_based_experience_ratio": start_up_based_experience_ratio,
            "startup_based_experience_months": start_based_experience_months,

            "product_based_experience": product_based_experience,
            "product_based_experience_ratio": product_based_experience_ratio,
            "product_based_experience_months": product_based_experience_months,

            # Penalize service based experience if more than 50% of total experience is service based

            "service_based_experience": service_based_experience,
            "service_based_experience_ratio": service_based_experience_ratio,
            "service_based_experience_months": service_based_experience_months,

            "unknown_company_experience": unknown_company_experience,
            "unknown_company_experience_ratio": unknown_company_experience_ratio,
            "unknown_company_experience_months": unknown_company_experience_months, 

            # =====================================================================================

            "tech_title_ratio": tech_title_ratio,
            "ai_ml_title_ratio": ai_ml_title_ratio,

            "current_title_match": current_title_match,
            "current_ai_ml_title_match": current_ai_ml_title_match,
        }
    
    # print(f"Candidate {candidate.candidate_id} - Career features: {career_history}")

    # ================================================== EDUCATION ================================

    suspicious_education_date_records = any(
        (
            edu.start_year is None and edu.end_year is not None
        )
        or
        (
            edu.start_year is None and edu.end_year is None
        )
        for edu in candidate.education
    )

    max_field_of_study_score = max(
    (
            FIELD_OF_STUDY_SCORE.get(
                edu.field_of_study.split().lower(),
                0.0
            )
            for edu in candidate.education
        ),
        default=0.0
    )

    max_degree_score = max(
        (
            DEGREE_SCORE.get(
                edu.degree.lower(),
                0.0
            )
            for edu in candidate.education
        ),
        default=0.0
    )

    academics = [
        {
            "grade_category": categorize_grade(edu.grade),
            "tier": edu.tier,
        }
        for edu in candidate.education
    ]

    education = {
        "academics": academics,
        "max_field_of_study_score": max_field_of_study_score,
        "max_degree_score": max_degree_score,
        "has_suspicious_education_dates": suspicious_education_date_records,
    }

    # print(f"Candidate {candidate.candidate_id} - Education: {education}")
    
    # ================================================= SKILLS ================================

    skill_features = {}

    for group, taxonomy_skills in SKILL_TAXONOMY.items():

        matched = [
            s
            for s in candidate.skills
            if s.name.strip().lower() in taxonomy_skills
        ]

        skill_features[group] = {
            "present": len(matched) > 0,
            "count": len(matched),
            "max_duration": max(
                (s.duration_months for s in matched),
                default=0
            ),
            "avg_duration": (
                sum(s.duration_months for s in matched) / len(matched)
                if matched else 0
            ),
            "max_proficiency": max(
                (
                    PROFICIENCY_MAP[s.proficiency]
                    for s in matched
                ),
                default=0
            ),
            "endorsements": sum(
                s.endorsements
                for s in matched
            ),
        }

    skills = {
        "skill_features": skill_features
    }

    # print(f"Candidate {candidate.candidate_id} - Skills: {skills}")
    
    # ==================================================== CERTIFICATIONS ============================================

    ai_ml_cert_count = 0
    cloud_cert_count = 0

    for cert in candidate.certifications:

        cert_name = cert.name.strip().lower()

        # Exact match
        if cert_name in AI_ML_CERTS:
            ai_ml_cert_count += 1

        elif any(
            keyword in cert_name
            for keyword in AI_ML_CERT_KEYWORDS
        ):
            ai_ml_cert_count += 1

        # Exact match
        if cert_name in CLOUD_CERTS:
            cloud_cert_count += 1

        elif any(
            keyword in cert_name
            for keyword in CLOUD_CERT_KEYWORDS
        ):
            cloud_cert_count += 1

    certification = {
        "ai_ml_cert_count": ai_ml_cert_count,
        "cloud_cert_count": cloud_cert_count,
    }

    # print(f"Candidate {candidate.candidate_id} - Certifications: {certification_features}")


    # ==================================================== REDROB SIGNALS ============================================

    profile_completeness_score = candidate.redrob_signals.profile_completeness_score

    if profile_completeness_score >= 90:
        profile_completeness_category = "excellent"
    elif profile_completeness_score >= 75:
        profile_completeness_category = "good"
    elif profile_completeness_score >= 50:
        profile_completeness_category = "average"
    else:
        profile_completeness_category = "poor"

    signup = datetime.strptime(
        candidate.redrob_signals.signup_date,
        "%Y-%m-%d"
    )

    last_active = datetime.strptime(
        candidate.redrob_signals.last_active_date,
        "%Y-%m-%d"
    )

    invalid_activity_dates = signup > last_active

    if invalid_activity_dates:
        since_last_active_days = None
    else:
        since_last_active_days = (datetime.now() - last_active).days

    profile_views_received_30d = candidate.redrob_signals.profile_views_received_30d
    search_appearance_30d = candidate.redrob_signals.search_appearance_30d
    saved_by_recruiters_30d = candidate.redrob_signals.saved_by_recruiters_30d

    view_rate = (
        profile_views_received_30d /
        max(search_appearance_30d, 1)
    )

    save_rate = (
        saved_by_recruiters_30d /
        max(profile_views_received_30d, 1)
    )

    recruiter_interest_score = save_rate

    recruiter_response_rate = candidate.redrob_signals.recruiter_response_rate
    avg_response_time_hours = candidate.redrob_signals.avg_response_time_hours

    response_score = (
        recruiter_response_rate *
        (1 / max(avg_response_time_hours, 1))
    )

    connection_count = candidate.redrob_signals.connection_count
    endorsements_received = candidate.redrob_signals.endorsements_received

    network_strength = (
        connection_count +
        endorsements_received
    )

    interview_completion_rate = candidate.redrob_signals.interview_completion_rate
    offer_acceptance_rate = candidate.redrob_signals.offer_acceptance_rate

    hiring_reliability = (
        interview_completion_rate,
        offer_acceptance_rate
    )

    github_activity_score = max(
        candidate.redrob_signals.github_activity_score,
        0
    )

    github_linked = candidate.redrob_signals.github_activity_score != -1

    notice_period_match = (
        candidate.redrob_signals.notice_period_days
        <= jd_features["notice_period"] or 30
    )

    jd_salary_max = jd_features["salary_range"]["max"] 

    candidate_min = (
        candidate.redrob_signals.expected_salary_range_inr_lpa.min
    )

    # candidate_max = (
    #     candidate.redrob_signals
    #     .expected_salary_range_inr_lpa["max"]
    # )

    if jd_salary_max is None:
        salary_match = None
    else:
        salary_match = (
            candidate_min <= jd_salary_max
        )

    interview_completion_rate = candidate.redrob_signals.interview_completion_rate
    offer_acceptance_rate = max(
        candidate.redrob_signals.offer_acceptance_rate,
        0
    )
    has_offer_history = (
        candidate.redrob_signals.offer_acceptance_rate != -1
    )

    assessment_features = {}

    scores = (
        candidate.redrob_signals
        .skill_assessment_scores
    )

    for group, taxonomy_skills in SKILL_ASSESSMENT_TAXONOMY.items():

        matched_scores = [
            score
            for skill, score in scores.items()
            if skill in taxonomy_skills
        ]

        assessment_features[group] = {
            "count": len(matched_scores),

            "avg_score": (
                sum(matched_scores) / len(matched_scores)
                if matched_scores else 0
            ),

            "max_score": max(
                matched_scores,
                default=0
            ),

            "has_assessment": len(matched_scores) > 0,
        }

    work_mode_match = jd_features["work_mode"] == candidate.redrob_signals.preferred_work_mode

    redrob_signals = {
        "profile_completeness_category": profile_completeness_category,
        # "signup_date": candidate.redrob_signals.signup_date,
        # "last_active_date": candidate.redrob_signals.last_active_date,
        "invalid_activity_dates": invalid_activity_dates,
        "since_last_active_days": since_last_active_days,
        "open_to_work_flag": candidate.redrob_signals.open_to_work_flag,
        "view_rate": view_rate,
        "save_rate": save_rate,
        "recruiter_interest_score": recruiter_interest_score,
        "response_score": response_score,
        "network_strength": network_strength,
        "hiring_reliability": hiring_reliability,
        "github_activity_score": github_activity_score,
        "github_linked": github_linked,
        "notice_period_match": notice_period_match,
        "salary_match": salary_match,
        "interview_completion_rate": interview_completion_rate,
        "offer_acceptance_rate": offer_acceptance_rate,
        "has_offer_history": has_offer_history,
        "assessment_features": assessment_features,
        # "recruiter_response_rate": candidate.redrob_signals.recruiter_response_rate,
        # "avg_response_time_hours": candidate.redrob_signals.avg_response_time_hours,
        # "skill_assessment_scores": candidate.redrob_signals.skill_assessment_scores,
        "notice_period_days": candidate.redrob_signals.notice_period_days,
        # "expected_salary_range_inr_lpa": candidate.redrob_signals.expected_salary_range_inr_lpa,
        "work_mode_match": work_mode_match,
        "willing_to_relocate": candidate.redrob_signals.willing_to_relocate,
        "verified_email": candidate.redrob_signals.verified_email,
        "verified_phone": candidate.redrob_signals.verified_phone,
        "linkedin_connected": candidate.redrob_signals.linkedin_connected, 
    }

    # print(f"Candidate {candidate.candidate_id} - Redrob signals: {redrob_signals}")

    return {
        "profile": profile,
        "career_history": career_history,
        "education": education,
        "skills": skills,
        "certifications": certification,
        "redrob_signals": redrob_signals,
    }