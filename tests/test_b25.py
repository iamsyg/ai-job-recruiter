# tests/test_b25.py

from model.b25 import build_bm25, save_bm25
from utils.load_candidates import load_candidates
from src.extract_jd_features import extract_jd_features
from utils.jd import jd

candidates = load_candidates(r"C:\Users\Eternity\Dropbox\Projects\New folder\[PUB] India_runs_data_and_ai_challenge\[PUB] India_runs_data_and_ai_challenge\India_runs_data_and_ai_challenge\candidates.jsonl")

bm25 = build_bm25(candidates)
save_bm25(bm25)



from model.b25 import load_bm25, retrieve_bm25
from src.build_jd_text import build_jd_text

bm25 = load_bm25()

jd_schema = extract_jd_features(jd())

query = build_jd_text(jd_schema)

candidate_ids, bm25_scores = retrieve_bm25(
    query=query,
    bm25=bm25,
    top_k=1000
)

print(f"Retrieved {len(candidate_ids)} candidates\n")

for cid, score in zip(candidate_ids[:10], bm25_scores[:10]):
    print(cid, round(float(score), 4))