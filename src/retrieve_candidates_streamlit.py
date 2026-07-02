# src/retrieve_candidates_streamlit.py

import numpy as np


def retrieve_candidates_streamlit(
    jd_embedding,
    candidate_embeddings,
    candidate_ids,
    bm25_candidate_ids,
    top_k=200,
):

    id_to_index = {
        cid: i
        for i, cid in enumerate(candidate_ids)
    }

    indices = [
        id_to_index[cid]
        for cid in bm25_candidate_ids
        if cid in id_to_index
    ]

    subset = candidate_embeddings[indices]

    scores = subset @ jd_embedding

    order = np.argsort(scores)[::-1]

    return (
        np.array(bm25_candidate_ids)[order][:top_k],
        scores[order][:top_k],
    )