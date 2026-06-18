# utils/skills/skill_names.py

SKILL_TAXONOMY = {
    
    "retrieval": {
        "Embeddings",
        "Sentence Transformers",
        "Vector Representations",
        "Semantic Search",
        "Vector Search",
        "Information Retrieval",
        "Information Retrieval Systems",
        "BM25",
        "RAG",
    },

    "vector_db": {
        "Pinecone",
        "Qdrant",
        "Weaviate",
        "Milvus",
        "FAISS",
        "pgvector",
    },

    "search_ranking": {
        "Ranking Systems",
        "Learning to Rank",
        "Search Infrastructure",
        "Search Backend",
        "Search & Discovery",
        "Indexing Algorithms",
        "Content Matching",
        "Recommendation Systems",
    },

    "llm": {
        "LLMs",
        "Prompt Engineering",
        "LangChain",
        "LlamaIndex",
        "Haystack",
    },

    "fine_tuning": {
        "LoRA",
        "QLoRA",
        "PEFT",
        "Fine-tuning LLMs",
        "Model Adaptation",
    },

    "nlp": {
        "Natural Language Processing",
        "NLP",
        "Text Encoders",
    },

    "ml": {
        "Machine Learning",
        "Deep Learning",
        "PyTorch",
        "TensorFlow",
        "scikit-learn",
        "Feature Engineering",
    },

    "mlops": {
        "MLOps",
        "Kubeflow",
        "MLflow",
        "Weights & Biases",
        "BentoML",
    },

    "data": {
        "Spark",
        "Airflow",
        "Kafka",
        "Databricks",
        "Apache Beam",
        "Apache Flink",
        "Data Pipelines",
        "Workflow Orchestration",
    },

    "python_backend": {
        "Python",
        "FastAPI",
        "Flask",
        "Django",
    },

    "cloud": {
        "AWS",
        "GCP",
        "Azure",
        "Docker",
        "Kubernetes",
        "Terraform",
    }
}


PROFICIENCY_MAP = {
    "beginner": 1,
    "intermediate": 2,
    "advanced": 3,
    "expert": 4,
}