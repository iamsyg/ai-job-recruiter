# main.py

from dotenv import load_dotenv
load_dotenv()

from utils.jd import jd
from utils.load_candidates import load_candidates

from src.extract_jd_features import extract_jd_features
from src.build_jd_text import build_jd_text
from src.build_candidate_text import build_candidate_text

from model.b25 import build_bm25, save_bm25, load_bm25, retrieve_bm25

from model.embedding_model import EMBEDDING_MODEL

from src.generate_jd_embeddings import generate_jd_embeddings
# from src.generate_candidate_embeddings import generate_candidate_embeddings
from src.retrieve_candidates import retrieve_candidates

from src.rerank_candidates import rerank_candidates

import csv
import numpy as np

job_description = jd()
candidates = load_candidates(file_path=r"C:\Users\Eternity\Dropbox\Projects\New folder\[PUB] India_runs_data_and_ai_challenge\[PUB] India_runs_data_and_ai_challenge\India_runs_data_and_ai_challenge\candidates.jsonl")

jd_schema = extract_jd_features(jd_text=job_description)
jd_text = build_jd_text(jd=jd_schema)

candidate_map = {
    c.candidate_id: c
    for c in candidates
}

# ============================================================== BM25 ==============================================================

bm25, candidate_ids = build_bm25(candidates, save=True)
save_bm25(bm25)
# loaded_bm25 = load_bm25()

bm25_candidate_ids, bm25_scores = retrieve_bm25(
    query=jd_text,
    bm25=bm25,
    candidate_ids=candidate_ids,
    top_k=1000
)

# ============================================================= Embedding =============================================================


jd_embedding = generate_jd_embeddings(jd=jd_schema, EMBEDDING_MODEL=EMBEDDING_MODEL)

# candidate_embeddings, candidate_ids = generate_candidate_embeddings(candidates=candidates, EMBEDDING_MODEL=EMBEDDING_MODEL)

candidate_ids, embedding_scores = retrieve_candidates(
    jd_embedding=jd_embedding,
    bm25_candidate_ids=bm25_candidate_ids,
    top_k=200
)

# candidate = candidate_map[candidate_id]

bm25_score_map = dict(
    zip(bm25_candidate_ids, bm25_scores)
)

embedding_score_map = dict(
    zip(candidate_ids, embedding_scores)
)

disqualifier_map = np.load(
    "disqualifier_features.npy",
    allow_pickle=True,
).item()

qualifier_map = np.load(
    "qualifying_features.npy",
    allow_pickle=True,
).item()

results = rerank_candidates(
    candidate_ids=candidate_ids,
    embedding_score_map=embedding_score_map,
    bm25_score_map=bm25_score_map,
    candidate_map=candidate_map,
    jd_schema=jd_schema,
    qualifier_map=qualifier_map,
    disqualifier_map=disqualifier_map,
)

print(f"BM25 retrieved {len(bm25_candidate_ids)} candidates")
print(f"result: {results[:10]}")


TOP_K = 100

with open("riyuzaki.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    writer.writerow([
        "candidate_id",
        "rank",
        "score",
        "reasoning"
    ])

    for rank, r in enumerate(results[:TOP_K], start=1):

        reasoning = r["reasoning"]

        # convert reasoning dict -> 1-2 sentence string
        strengths = reasoning["strengths"][:2]
        concerns = reasoning["concerns"][:1]

        text = ""

        if strengths:
            text += "; ".join(strengths)

        if concerns:
            text += ". Concern: " + concerns[0]

        writer.writerow([
            r["candidate_id"],
            rank,
            round(r["final_score"], 6),
            text
        ])