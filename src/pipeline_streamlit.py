# src/pipeline_streamlit.py

from collections import defaultdict

from utils.jd import jd

from src.extract_jd_features import extract_jd_features
from src.build_jd_text import build_jd_text

from model.embedding_model import EMBEDDING_MODEL
from model.b25 import build_bm25, retrieve_bm25

from src.generate_jd_embeddings import generate_jd_embeddings
from src.build_candidate_text import build_candidate_text

from src.retrieve_candidates_streamlit import retrieve_candidates_streamlit
from src.rerank_candidates import rerank_candidates

from src.extract_qualifying_features import (
    embed_positive_prototypes,
    extract_positive_signals,
)

from src.extract_disqualifier_features import (
    extract_disqualifier_features,
    _embed_prototypes,
)


def run_pipeline_streamlit(candidates):

    job_description = jd()

    jd_schema = extract_jd_features(job_description)

    jd_text = build_jd_text(jd_schema)

    candidate_map = {
        c.candidate_id: c
        for c in candidates
    }

    # ---------------- BM25 ----------------

    bm25, candidate_ids = build_bm25(candidates)

    bm25_candidate_ids, bm25_scores = retrieve_bm25(
        query=jd_text,
        bm25=bm25,
        candidate_ids=candidate_ids,
        top_k=min(1000, len(candidates))
    )

    # ---------------- JD embedding ----------------

    jd_embedding = generate_jd_embeddings(
        jd_schema,
        EMBEDDING_MODEL,
    )

    # ---------------- Candidate embeddings ----------------

    candidate_texts = [
        build_candidate_text(c)
        for c in candidates
    ]

    candidate_embeddings = EMBEDDING_MODEL.encode(
        candidate_texts,
        batch_size=32,
        normalize_embeddings=True,
    )

    candidate_ids, embedding_scores = retrieve_candidates_streamlit(
        jd_embedding=jd_embedding,
        candidate_embeddings=candidate_embeddings,
        candidate_ids=candidate_ids,
        bm25_candidate_ids=bm25_candidate_ids,
        top_k=min(200, len(candidate_ids)),
    )

    # ---------------- Role embeddings ----------------

    role_texts = []
    role_owner = []

    for idx, candidate in enumerate(candidates):

        for role in candidate.career_history:

            role_texts.append(role.description or "")

            role_owner.append(idx)

    role_embeddings = EMBEDDING_MODEL.encode(
        role_texts,
        batch_size=64,
        normalize_embeddings=True,
    )

    candidate_role_embeddings = defaultdict(list)

    for idx, vec in zip(role_owner, role_embeddings):
        candidate_role_embeddings[idx].append(vec)

    # ---------------- Qualifiers ----------------

    proto_vecs = embed_positive_prototypes(
        EMBEDDING_MODEL
    )

    qualifier_map = {}

    for idx, candidate in enumerate(candidates):

        qualifier_map[candidate.candidate_id] = extract_positive_signals(
            candidate,
            proto_vecs,
            candidate_role_embeddings[idx],
        )

    # ---------------- Disqualifiers ----------------

    negative_proto = _embed_prototypes(
        EMBEDDING_MODEL
    )

    disqualifier_map = {}

    for idx, candidate in enumerate(candidates):

        disqualifier_map[candidate.candidate_id] = extract_disqualifier_features(
            candidate,
            negative_proto,
            candidate_role_embeddings[idx],
        )

    bm25_score_map = dict(
        zip(
            bm25_candidate_ids,
            bm25_scores,
        )
    )

    embedding_score_map = dict(
        zip(
            candidate_ids,
            embedding_scores,
        )
    )

    results = rerank_candidates(
        candidate_ids=candidate_ids,
        embedding_score_map=embedding_score_map,
        bm25_score_map=bm25_score_map,
        candidate_map=candidate_map,
        jd_schema=jd_schema,
        qualifier_map=qualifier_map,
        disqualifier_map=disqualifier_map,
    )

    return results