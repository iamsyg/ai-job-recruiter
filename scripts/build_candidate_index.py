# scripts/build_candidate_index.py

from src.generate_candidate_embeddings import generate_candidate_embeddings
from utils.load_candidates import load_candidates

candidates = load_candidates(file_path=r"C:\Users\Eternity\Dropbox\Projects\New folder\[PUB] India_runs_data_and_ai_challenge\[PUB] India_runs_data_and_ai_challenge\India_runs_data_and_ai_challenge\candidates.jsonl")

generate_candidate_embeddings(candidates)

print("Candidate embeddings generated.")


