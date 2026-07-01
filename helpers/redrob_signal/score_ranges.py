# helpers/redrob_signal/score_ranges.py

from utils.load_candidates import load_candidates

from score.career_history import career_history_score
from score.skills import skills_score
from score.education import education_score
from score.profile import profile_score
from score.certification import certification_score
from score.language import language_score
from score.redrob_signals import redrob_signals_score

from src.extract_candidate_features import extract_career_history_features, extract_skills_features, extract_redrob_signals, extract_certification_features, extract_education_features, extract_language_features, extract_profile_features

from utils.jd import jd
from src.extract_jd_features import extract_jd_features




candidates = load_candidates(
    r"C:\Users\Eternity\Dropbox\Projects\New folder\[PUB] India_runs_data_and_ai_challenge\[PUB] India_runs_data_and_ai_challenge\India_runs_data_and_ai_challenge\candidates.jsonl"
)

career_scores = []
skills_scores = []
education_scores = []
profile_scores = []
certification_scores = []
language_scores = []
redrob_scores = []

jd = extract_jd_features(jd_text=jd())

for candidate in candidates:

    career = extract_career_history_features(candidate)
    career_scores.append(
        career_history_score(career)
    )

    skill = extract_skills_features(candidate)
    skills_scores.append(
        skills_score(skill)
    )

    edu = extract_education_features(candidate)
    education_scores.append(
        education_score(edu)
    )

    prof = extract_profile_features(
        candidate=candidate,
        jd_features=jd
    )
    profile_scores.append(
        profile_score(prof)
    )

    cert = extract_certification_features(candidate)
    certification_scores.append(
        certification_score(cert)
    )

    lang = extract_language_features(candidate)
    language_scores.append(
        language_score(lang)
    )

    red = extract_redrob_signals(candidate, jd_features=jd)
    redrob_scores.append(
        redrob_signals_score(red)
    )



print("\nScore ranges\n")

print(f"Career        : {min(career_scores):.3f} -> {max(career_scores):.3f}")
print(f"Skills        : {min(skills_scores):.3f} -> {max(skills_scores):.3f}")
print(f"Education     : {min(education_scores):.3f} -> {max(education_scores):.3f}")
print(f"Profile       : {min(profile_scores):.3f} -> {max(profile_scores):.3f}")
print(f"Certification : {min(certification_scores):.3f} -> {max(certification_scores):.3f}")
print(f"Language      : {min(language_scores):.3f} -> {max(language_scores):.3f}")
print(f"Redrob        : {min(redrob_scores):.3f} -> {max(redrob_scores):.3f}")



# Score ranges

# Career        : 0.000 -> 1.000
# Skills        : 0.000 -> 1.623
# Education     : 0.125 -> 0.375
# Profile       : -0.250 -> 0.250
# Certification : 0.000 -> 0.200
# Language      : 0.100 -> 0.100
# Redrob        : -0.800 -> 1.670