# src/extract_candidate_features.py

from schema.candidate_schema import CandidateSchema

def extract_candidate_features(candidate: CandidateSchema):

    skills = [s.name for s in candidate.skills]

    career_text = "\n".join(
        role.description
        for role in candidate.career_history
    )

    summary_text = candidate.profile.summary

    profile = {
        "candidate_id": candidate.candidate_id,
        "location": candidate.profile.location,
        "country": candidate.profile.country,
        "experience": candidate.profile.years_of_experience,
        "summary_text": summary_text,
    }

    career_history = [
        {

            "title": role.title,
            "start_date": role.start_date,
            "end_date": role.end_date,
            "duration_months": role.duration_months,
            "is_current": role.is_current,
            "industry": role.industry,
            "company_size": role.company_size,
            "description": role.description,
        }
        for role in candidate.career_history
    ]

    education_history = [
            {
                "degree": edu.degree,
                "field_of_study": edu.field_of_study,
                "start_date": edu.start_year,
                "end_date": edu.end_year,
                "grade": edu.grade,
                "tier": edu.tier,
            }
            for edu in candidate.education
    ]
    

    skills = [
            {
                "name": skill.name,
                "proficiency": skill.proficiency,
                "endorsements": skill.endorsements,
                "duration_months": skill.duration_months,
            }
            for skill in candidate.skills
    ]
    

    certifications = [
            {
                "name": cert.name,
                "issuer": cert.issuer,
                "year": cert.year,
            }
            for cert in candidate.certifications
    ]
    

    redrob_signals = {
        "profile_completeness_score": candidate.redrob_signals.profile_completeness_score,
        "signup_date": candidate.redrob_signals.signup_date,
        "last_active_date": candidate.redrob_signals.last_active_date,
        "open_to_work_flag": candidate.redrob_signals.open_to_work_flag,
        "recruiter_response_rate": candidate.redrob_signals.recruiter_response_rate,
        "avg_response_time_hours": candidate.redrob_signals.avg_response_time_hours,
        "skill_assessment_scores": candidate.redrob_signals.skill_assessment_scores,
        "notice_period_days": candidate.redrob_signals.notice_period_days,
        "expected_salary_range_inr_lpa": candidate.redrob_signals.expected_salary_range_inr_lpa,
        "preferred_work_mode": candidate.redrob_signals.preferred_work_mode,
        "willing_to_relocate": candidate.redrob_signals.willing_to_relocate,
        "github_activity_score": candidate.redrob_signals.github_activity_score,
        "interview_completion_rate": candidate.redrob_signals.interview_completion_rate,
        "verified_email": candidate.redrob_signals.verified_email,
        "verified_phone": candidate.redrob_signals.verified_phone,
        "linkedin_connected": candidate.redrob_signals.linkedin_connected,


        # Check for the internship keyword in the career history to identify if the candidate has internship experience
        "has_internship_experience": any(
            "intern" in role.title.lower() or "internship" in role.description.lower()
            for role in candidate.career_history
        ),

        "job_count": any(
            "intern" not in role.title.lower() and "internship" not in role.description.lower()
            for role in candidate.career_history 
        )   
    }

    return {
        "profile": profile,
        "career_history": career_history,
        "education_history": education_history,
        "skills": skills,
        "certifications": certifications,
        "redrob_signals": redrob_signals,
    }