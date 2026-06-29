# src/build_jd_text.py

from schema.jd_schema import JDSchema


def build_jd_text(jd: JDSchema) -> str:

    parts = []

    parts.extend(jd.must_have_skills)
    parts.extend(jd.preferred_skills)
    parts.extend(jd.role_focus)
    parts.extend(jd.company_type_preferences)
    parts.extend(jd.education_requirements)

    return "\n".join(parts)