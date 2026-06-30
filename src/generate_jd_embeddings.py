# src/generate_jd_embeddings.py

from src.build_jd_text import build_jd_text
from schema.jd_schema import JDSchema

# from model.embedding_model import EMBEDDING_MODEL

def generate_jd_embeddings(jd: JDSchema, EMBEDDING_MODEL):

    jd_text = build_jd_text(jd=jd)

    jd_embedding = EMBEDDING_MODEL.encode(
        jd_text,
        normalize_embeddings=True
    )

    return jd_embedding