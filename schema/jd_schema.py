# schema/jd_schema.py

from typing import List, Optional
from pydantic import BaseModel, Field

class SalaryRange(BaseModel):
    min: Optional[float] = Field(None, description="Minimum salary range")
    max: Optional[float] = Field(None, description="Maximum salary range")



class ExperienceRange(BaseModel):
    min: Optional[int] = Field(None, description="Minimum experience range")
    max: Optional[int] = Field(None, description="Maximum experience range")



class JDSchema(BaseModel):
    preferred_locations: List[str] = Field(default_factory=list)
    additional_locations: List[str] = Field(default_factory=list)
    relocation_preferred: bool = Field(default=False)

    employment_type: List[str] = Field(default_factory=list)
    work_mode: List[str] = Field(default_factory=list)

    experience_required: ExperienceRange = ExperienceRange()

    must_have_skills: List[str] = Field(default_factory=list)
    preferred_skills: List[str] = Field(default_factory=list)

    role_focus: List[str] = Field(default_factory=list)

    education_requirements: List[str] = Field(default_factory=list)

    company_type_preferences: List[str] = Field(default_factory=list)

    negative_signals: List[str] = Field(default_factory=list)

    notice_period: Optional[int] = Field(default=None)

    salary_range: SalaryRange = SalaryRange()