# src/build_candidate_text.py

from schema.candidate_schema import CandidateSchema


def build_candidate_text(candidate: CandidateSchema) -> str:

    parts = []

    profile = candidate.profile

    parts.append(profile.headline or "")
    parts.append(profile.summary or "")

    for role in candidate.career_history:
        parts.append(role.title)
        parts.append(role.description)

    for skill in candidate.skills:
        parts.append(skill.name)

    # print(parts)

    return "\n".join(parts)