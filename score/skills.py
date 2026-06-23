# score/skills.py

from schema.candidate_features_schema import Skills

GROUP_WEIGHTS = {

    # MUST HAVE
    "retrieval": 0.25,
    "vector_db": 0.20,
    "search_ranking": 0.25,
    "python_backend": 0.20,

    # IMPORTANT
    "ml": 0.15,
    "nlp": 0.15,
    "llm": 0.10,

    # NICE TO HAVE
    "fine_tuning": 0.08,
    "mlops": 0.05,
    "cloud": 0.03,
    "data": 0.03,
}



def skills_score(skills: Skills) -> float:
    """
    Calculate the skills score based on the provided Skills object.

    Args:
        skills (Skills): An instance of the Skills class containing skill details.

    Returns:
        float: The calculated skills score.
    """
    

    score = 0.0

    for group, feature in skills.skill_features.items():

        if not feature.present:
            continue

        group_score = 0.0
        weight = GROUP_WEIGHTS.get(group, 0.0)

        # Presence
        group_score += 0.20

        if feature.count >= 3:
            group_score += 0.20
        elif feature.count >= 2:
            group_score += 0.15
        elif feature.count >= 1:
            group_score += 0.10

        # Experience duration
        if feature.avg_duration >= 24:
            group_score += 0.30
        elif feature.avg_duration >= 15:
            group_score += 0.25
        elif feature.avg_duration >= 10:
            group_score += 0.20
        elif feature.avg_duration >= 6:
            group_score += 0.10

        # Proficiency
        group_score += (
            feature.max_proficiency / 4
        ) * 0.20

        # Endorsements
        if feature.endorsements >= 20:
            group_score += 0.10
        elif feature.endorsements >= 10:
            group_score += 0.05

        score += group_score * weight


    retrieval = skills.skill_features["retrieval"].present
    vector_db = skills.skill_features["vector_db"].present
    search = skills.skill_features["search_ranking"].present


    if retrieval and vector_db and search:
        score += 0.30
    elif retrieval and vector_db:
        score += 0.15
    elif retrieval and search:
        score += 0.15
    elif vector_db and search:
        score += 0.15


    return score
    