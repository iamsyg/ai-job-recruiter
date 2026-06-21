# utils/skills/skill_names.py

SKILL_TAXONOMY = {
    
    "retrieval": {
        "embeddings",
        "sentence transformers",
        "vector representations",
        "semantic search",
        "vector search",
        "information retrieval",
        "information retrieval systems",
        "bm25",
        "rag",
    },

    "vector_db": {
        "pinecone",
        "qdrant",
        "weaviate",
        "milvus",
        "faiss",
        "pgvector",
    },

    "search_ranking": {
        "ranking systems",
        "learning to rank",
        "search infrastructure",
        "search backend",
        "search & discovery",
        "indexing algorithms",
        "content matching",
        "recommendation systems",
    },

    "llm": {
        "llms",
        "prompt engineering",
        "langchain",
        "llamaindex",
        "haystack",
    },

    "fine_tuning": {
        "lora",
        "qlora",
        "peft",
        "fine-tuning llms",
        "model adaptation",
    },

    "nlp": {
        "natural language processing",
        "nlp",
        "text encoders",
    },

    "ml": {
        "machine learning",
        "deep learning",
        "pytorch",
        "tensorflow",
        "scikit-learn",
        "feature engineering",
    },

    "mlops": {
        "mlops",
        "kubeflow",
        "mlflow",
        "weights & biases",
        "bentoml",
    },

    "data": {
        "spark",
        "airflow",
        "kafka",
        "databricks",
        "apache beam",
        "apache flink",
        "data pipelines",
        "workflow orchestration",
    },

    "python_backend": {
        "python",
        "fastapi",
        "flask",
        "django",
    },

    "cloud": {
        "aws",
        "gcp",
        "azure",
        "docker",
        "kubernetes",
        "terraform",
    }
}


PROFICIENCY_MAP = {
    "beginner": 1,
    "intermediate": 2,
    "advanced": 3,
    "expert": 4,
}