# score/language.py

from schema.candidate_features_schema import Language

def language_score(language: Language) -> float:

    """
    Calculate the language score based on the provided Language object.

    Args:
        language (Language): An instance of the Language class containing language proficiency details.

    Returns:
        float: The calculated language score.
    """

    score = 0.0

    if language.is_english_proficient:
        score += 0.10
    else:
        score += 0.0

    return score