# schema/candidate_features_schema.py

from pydantic import BaseModel
from typing import Dict, Literal, List, Tuple


class Profile(BaseModel):
    candidate_id: str
    location_match: bool
    willing_to_relocate: bool
    country_match: bool
    # experience_match: bool
    experience_gap: float
    employment_eligibility_match: bool
    summary_text: str

class CareerHistory(BaseModel):
    career_gap_months: int
    has_suspicious_career_dates: bool
    has_it_engineering_industry: bool

    # startup_based_experience: int
    startup_based_experience_ratio: float
    startup_based_experience_months: int

    # product_based_experience: int
    product_based_experience_ratio: float
    product_based_experience_months: int

    # service_based_experience: int
    service_based_experience_ratio: float
    service_based_experience_months: int

    # unknown_company_experience: int
    unknown_company_experience_ratio: float
    unknown_company_experience_months: int

    tech_title_ratio: float
    ai_ml_title_ratio: float

    current_title_match: bool
    current_ai_ml_title_match: bool

class Education(BaseModel):

    relevant_field_of_study_score: float
    relevant_degree_score: float
    relevant_grade_category: str
    relevant_tier: str
    has_suspicious_education_dates: bool

class SkillFeatures(BaseModel):
    present: bool
    count: int
    max_duration: int
    avg_duration: float
    max_proficiency: int   # [1-4] based on PROFICIENCY_MAP
    endorsements: int

class Skills(BaseModel):
    skill_features: Dict[str, SkillFeatures]

class Certification(BaseModel):
    ai_ml_cert_count: int
    cloud_cert_count: int
    suspicious_certifications: bool

class Language(BaseModel):
    is_english_proficient: bool

class RedrobSignals(BaseModel):
    profile_completeness_category: Literal["excellent", "good", "average", "poor", "unknown"]
    invalid_activity_dates: bool
    since_last_active_days: int | None
    open_to_work_flag: bool

    view_rate: float
    save_rate: float
    save_without_view_anomaly: bool
    recruiter_interest: float
    # response_score: float
    recruiter_response_rate: float
    avg_response_time_hours: float

    connection_count: int
    endorsements_received: int

    # hiring_reliability: Tuple[float, float]

    notice_period_gap: int
    salary_gap: int | None

    work_mode_match: bool
    # willing_to_relocate: bool

    github_activity_score: float
    github_linked: bool

    interview_completion_rate: float
    offer_acceptance_rate: float
    has_offer_history: bool

    assessment_features: Dict[str, dict]
    
    verified_email: bool
    verified_phone: bool
    linkedin_connected: bool

class Disqualifiers(BaseModel):
    research_only_confidence: float
    architecture_no_code_confidence: float
    langchain_wrapper_only_confidence: float
    cv_speech_robotics_without_nlp_confidence: float
    job_hopper_confidence: float

class Qualifiers(BaseModel):

    production_ml_confidence: float
    production_ml_months: int

    ir_confidence: float
    ir_months: int

    ranking_confidence: float
    ranking_months: int

    vector_db_confidence: float
    vector_db_months: int

    embedding_retrieval_confidence: float
    embedding_retrieval_months: int
    
    strong_opinions_retrieval_confidence:  float
    strong_opinions_retrieval_months: int

class CandidateFeatures(BaseModel):

    profile: Profile
    career_history: CareerHistory
    education: Education
    skills: Skills
    certifications: Certification
    is_english_proficient: Language
    redrob_signals: RedrobSignals
    disqualifiers: Disqualifiers
    qualifiers: Qualifiers
