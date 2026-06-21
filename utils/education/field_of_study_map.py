# utils/education/field_of_study_map.py

FIELD_OF_STUDY_SCORE = {
    # Direct matches
    "artificial intelligence": 1.00,
    "machine learning": 1.00,
    "data science": 0.95,
    "computer science": 0.95,
    "computer engineering": 0.90,
    "information technology": 0.90,

    # Related engineering
    "electronics": 0.80,
    "electrical engineering": 0.70,
    "mathematics": 0.65,
    "statistics": 0.65,
    "physics": 0.60,

    # Adjacent engineering
    "mechanical engineering": 0.30,
    "chemical engineering": 0.30,
    "civil engineering": 0.25,

    # Non-technical
    "commerce": 0.05,
    "mba": 0.05,
}