# helpers/skills/name.py

import json

skills = set()

with open(r"C:\Users\Eternity\Dropbox\Projects\New folder\[PUB] India_runs_data_and_ai_challenge\[PUB] India_runs_data_and_ai_challenge\India_runs_data_and_ai_challenge\candidates.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        candidate = json.loads(line)

        for exp in candidate.get("skills", []):
            skill = exp.get("name")
            if skill:
                skills.add(skill.strip())

print(f"Unique skills: {len(skills)}")
print("Unique skills list:")

for skill in (skills):
    print(f" - {skill}")




# Unique skills: 133
# Unique skills list:
#  - LoRA
#  - Pinecone
#  - Tailwind
#  - Semantic Search
#  - Vector Search
#  - Docker
#  - Ranking Systems
#  - PEFT
#  - LangChain
#  - Tally
#  - Apache Beam
#  - Node.js
#  - Sentence Transformers
#  - PyTorch
#  - Angular
#  - PowerPoint
#  - gRPC
#  - Photoshop
#  - SQL
#  - Scrum
#  - Time Series
#  - Vector Representations
#  - Six Sigma
#  - CI/CD
#  - OpenCV
#  - Text Encoders
#  - CSS
#  - CNN
#  - GANs
#  - OpenSearch
#  - Marketing
#  - Hugging Face Transformers
#  - Microservices
#  - HTML
#  - Java
#  - Statistical Modeling
#  - Databricks
#  - RAG
#  - GraphQL
#  - YOLO
#  - Illustrator
#  - Search Infrastructure
#  - Spring Boot
#  - Data Science
#  - Reinforcement Learning
#  - Rust
#  - Search Backend
#  - Qdrant
#  - FAISS
#  - FastAPI
#  - Weaviate
#  - Accounting
#  - TTS
#  - ETL
#  - SEO
#  - JavaScript
#  - Elasticsearch
#  - Vue.js
#  - Search & Discovery
#  - REST APIs
#  - Airflow
#  - Milvus
#  - Next.js
#  - Sales
#  - Prompt Engineering
#  - Machine Learning
#  - dbt
#  - QLoRA
#  - Fine-tuning LLMs
#  - React
#  - Recommendation Systems
#  - Workflow Orchestration
#  - Agile
#  - Kubeflow
#  - Kafka
#  - SAP
#  - Diffusion Models
#  - Redis
#  - Spark
#  - Figma
#  - pgvector
#  - PostgreSQL
#  - BigQuery
#  - Python
#  - Deep Learning
#  - Azure
#  - Kubernetes
#  - Webpack
#  - Excel
#  - Data Pipelines
#  - Redux
#  - Feature Engineering
#  - Speech Recognition
#  - MLOps
#  - Open-source ML libraries
#  - Embeddings
#  - Document Processing
#  - Go
#  - ASR
#  - Natural Language Processing
#  - Computer Vision
#  - Content Writing
#  - Model Adaptation
#  - TensorFlow
#  - Forecasting
#  - Haystack
#  - Object Detection
#  - Hadoop
#  - Image Classification
#  - Information Retrieval Systems
#  - MLflow
#  - BM25
#  - Salesforce CRM
#  - Learning to Rank
#  - GCP
#  - Terraform
#  - LlamaIndex
#  - Django
#  - Project Management
#  - NLP
#  - Content Matching
#  - BentoML
#  - Weights & Biases
#  - MongoDB
#  - Snowflake
#  - LLMs
#  - TypeScript
#  - Apache Flink
#  - Indexing Algorithms
#  - Flask
#  - AWS
#  - Information Retrieval
#  - scikit-learn