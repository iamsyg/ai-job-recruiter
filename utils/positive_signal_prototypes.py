# utils/positive_signal_prototypes.py

POSITIVE_PROTOTYPES = {
    "production_ml": [
        "Deployed machine learning models to production serving real users.",
        "Owned end-to-end ML pipeline from training to serving live traffic.",
        "Maintained and monitored production ML systems with real business impact.",
        "Shipped ML models that handled real-world queries at scale.",
        "Built production ML infrastructure for a product used by customers.",
        "Responsible for training, deploying, and iterating ML systems in production.",
    ],
    "information_retrieval": [
        "Built information retrieval systems over large text corpora.",
        "Designed and implemented document retrieval pipelines for search.",
        "Worked on search relevance and document ranking for text retrieval.",
        "Developed hybrid retrieval combining sparse and dense methods.",
        "Built BM25 or TF-IDF based retrieval systems at scale.",
        "Implemented semantic search over large document collections.",
    ],
    "ranking_systems": [
        "Built learning-to-rank models for search or recommendation.",
        "Designed ranking pipelines using XGBoost, LightGBM, or neural rankers.",
        "Owned ranking layer for a search or discovery product.",
        "Implemented and evaluated ranking models using NDCG, MRR, or MAP.",
        "Built re-ranking systems combining multiple signals for relevance.",
        "Designed offline evaluation frameworks to measure ranking quality.",
    ],
    "vector_db": [
        "Used Pinecone, Weaviate, Qdrant, Milvus, or FAISS for vector storage.",
        "Built and maintained vector database infrastructure for semantic search.",
        "Managed embedding indexes with refresh, versioning, and rollback.",
        "Operated OpenSearch or Elasticsearch with dense vector search.",
        "Handled vector index scaling, sharding, and latency optimization.",
    ],
    "embedding_retrieval": [
        "Built embedding-based retrieval using sentence transformers or dense encoders.",
        "Fine-tuned or selected embedding models for retrieval quality.",
        "Deployed dense retrieval systems using BGE, E5, or OpenAI embeddings.",
        "Designed hybrid retrieval combining BM25 with dense vector recall.",
        "Handled embedding drift, index refresh, and retrieval regression in production.",
        "Built ANN search pipelines over millions of embeddings.",
    ],
    "strong_opinions_retrieval": [
        "Has clear opinions about when to use hybrid versus dense retrieval.",
        "Evaluated trade-offs between sparse BM25 and dense embedding retrieval.",
        "Designed evaluation frameworks to compare offline and online retrieval metrics.",
        "Reasoned about when to fine-tune embeddings versus use off-the-shelf models.",
        "Made architectural decisions about retrieval pipeline design based on production learnings.",
        "Chose between approximate nearest neighbor libraries based on latency and recall trade-offs.",
    ],
}