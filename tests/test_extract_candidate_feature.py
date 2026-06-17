# tests/test_extract_candidate_feature.py

import json

from src.extract_candidate_features import extract_candidate_features
from schema.candidate_schema import CandidateSchema

jd_features = {'preferred_locations': ['Pune', 'Noida'], 'additional_locations': ['Hyderabad', 'Mumbai', 'Delhi NCR'], 'relocation_preferred': True, 'employment_type': ['Full-time'],'work_mode': ['Hybrid'], 'experience_required': {'min': 5, 'max': 9}, 'must_have_skills': ['Production experience with embeddings-based retrieval systems', 'Production experience with vector databases', 'Python', 'Ranking system evaluation design', 'NDCG', 'MRR', 'MAP', 'A/B testing', 'Modern Machine Learning systems', 'LLMs', 'End-to-end Ranking Systems', 'End-to-end Search Systems', 'End-to-end Recommendation Systems'], 'preferred_skills': ['LLM fine-tuning', 'Learning-to-rank models', 'HR Tech', 'Recruiting Tech', 'Marketplace products', 'Distributed Systems', 'Large-scale inference optimization', 'Open-source contributions in AI/ML'], 'role_focus': ['Intelligencelayer development', 'Ranking system development', 'Retrieval system development', 'Matching system development', 'Candidate-Job Description matching', 'AI architecture'], 'education_requirements': [], 'company_type_preferences': ['Product company'], 'negative_signals': ['Pure research background without production deployment', 'AI experience primarily from recent LangChain/OpenAI projects without pre-LLM ML production experience', 'No production code written in last 18 months due to architecture/tech lead roles', 'Frequent job switching (every 1.5 years)', 'Title-chasing', 'Over-reliance on frameworks (lack of systems thinking)', 'Exclusive consulting firm background(e.g., TCS, Infosys)', 'Primary expertise in Computer Vision, Speech, or Robotics without significant NLP/IR exposure', 'Work entirely on closed-source proprietary systems for 5+ years without external validation'], 'notice_period': 30, 'salary_range': {'min': None, 'max': None}}

with open(r"C:\Users\Eternity\Dropbox\Projects\New folder\[PUB] India_runs_data_and_ai_challenge\[PUB] India_runs_data_and_ai_challenge\India_runs_data_and_ai_challenge\sample_candidates.json", "r", encoding="utf-8") as f:
    candidates_json = json.load(f)

candidates = [
    CandidateSchema.model_validate(candidate)
    for candidate in candidates_json
]

features = [
    extract_candidate_features(candidate, jd_features)
    for candidate in candidates
]

print(features[0])