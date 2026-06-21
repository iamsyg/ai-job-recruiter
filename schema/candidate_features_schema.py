# schema/candidate_features_schema.py

from pydantic import BaseModel
from typing import Dict, Literal, List, Tuple


class Profile(BaseModel):
    candidate_id: str
    location_match: bool
    willing_to_relocate: bool
    country_match: bool
    experience_match: bool
    summary_text: str

class CareerHistory(BaseModel):
    career_gap_months: int
    has_suspicious_career_dates: bool
    has_it_engineering_industry: bool

    startup_based_experience: int
    startup_based_experience_ratio: float
    startup_based_experience_months: int

    product_based_experience: int
    product_based_experience_ratio: float
    product_based_experience_months: int

    unknown_company_experience: int
    unknown_company_experience_ratio: float
    unknown_company_experience_months: int

    tech_title_ratio: float
    ai_ml_title_ratio: float

    current_title_match: bool
    current_ai_ml_title_match: bool

class Academics(BaseModel):
    grade_category: str = None
    tier: str = Literal("Tier 1", "Tier 2", "Tier 3", "Unknown")

class Education(BaseModel):
    academics: List[Academics]
    max_field_of_study_score: float
    max_degree_score: float
    has_suspicious_education_dates: bool

class SkillFeatures(BaseModel):
    present: bool
    count: int
    max_duration: int
    avg_duration: float
    max_proficiency: int
    endorsements: int

class Skills(BaseModel):
    skill_features: Dict[str, SkillFeatures]

class Certification(BaseModel):
    ai_ml_cert_count: int
    cloud_cert_count: int

class RedrobSignals(BaseModel):
    profile_completeness_category: str = Literal("excellent", "good", "average", "poor")
    invalid_activity_dates: bool
    since_last_active_days: int | None
    open_to_work_flag: bool
    view_rate: float
    save_rate: float
    recruiter_interest_score: float
    response_score: float
    network_strength: float
    hiring_reliability: Tuple[float, float]
    github_activity_score: float
    github_linked: bool
    notice_period_match: bool
    salary_match: bool | None
    interview_completion_rate: float
    offer_acceptance_rate: float
    has_offer_history: bool
    assessment_features: Dict[str, dict]
    notice_period_days: int
    work_mode_match: bool
    willing_to_relocate: bool
    verified_email: bool
    verified_phone: bool
    linkedin_connected: bool



class CandidateFeatures(BaseModel):

    profile: Profile
    career_history: CareerHistory
    education: Education
    skills: Skills
    certifications: Certification
    redrob_signals: RedrobSignals