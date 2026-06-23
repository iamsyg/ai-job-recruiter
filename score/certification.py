# score/certification.py

from schema.candidate_features_schema import Certification

def certification_score(certification: Certification) -> float:
    """
    Calculate the certification score based on the provided Certification object.

    Args:
        certification (Certification): An instance of the Certification class containing certification details.

    Returns:
        float: The calculated certification score.
    """

    score = 0.0

    if certification.ai_ml_cert_count >= 2:
        score += 0.10
    elif certification.ai_ml_cert_count == 1:
        score += 0.05

    if certification.cloud_cert_count >= 2:
        score += 0.10
    elif certification.cloud_cert_count == 1:
        score += 0.05

    if certification.suspicious_certifications:
        score -= 0.10

    return score