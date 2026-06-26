# model/embedding_model.py


from sentence_transformers import SentenceTransformer

EMBEDDING_MODEL = SentenceTransformer(
    "BAAI/bge-base-en-v1.5"
)