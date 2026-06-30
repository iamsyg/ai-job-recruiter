# src/retrieve_candidates.py

# from src.generate_jd_embeddings import generate_jd_embeddings


import numpy as np

def retrieve_candidates(jd_embedding: np.ndarray, bm25_candidate_ids: np.ndarray, top_k: int = 200):

    candidate_matrix = np.load("candidate_embeddings.npy")
    candidate_ids = np.load("candidate_ids.npy")

        # candidate_id -> row index
    id_to_index = {
        candidate_id: idx
        for idx, candidate_id in enumerate(candidate_ids)
    }

    # Convert BM25 IDs into embedding row indices
    indices = [
        id_to_index[candidate_id]
        for candidate_id in bm25_candidate_ids
        if candidate_id in id_to_index
    ]


   # Only keep BM25 candidates
    subset_matrix = candidate_matrix[indices]

    # Cosine similarity 
    scores = subset_matrix @ jd_embedding
    
     # Sort descending
    order = np.argsort(scores)[::-1]

    top_candidate_ids = bm25_candidate_ids[order][:top_k]
    top_scores = scores[order][:top_k]

    return top_candidate_ids, top_scores