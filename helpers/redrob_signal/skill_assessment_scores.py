# helpers/redrob_signal/skill_assessment_scores.py

import json
from collections import defaultdict

skill_scores = defaultdict(list)

with open(r"C:\Users\Eternity\Dropbox\Projects\New folder\[PUB] India_runs_data_and_ai_challenge\[PUB] India_runs_data_and_ai_challenge\India_runs_data_and_ai_challenge\candidates.jsonl", "r", encoding="utf-8") as f:

    for line in f:
        candidate = json.loads(line)

        assessments = candidate.get(
            "redrob_signals",
            {}
        ).get(
            "skill_assessment_scores",
            {}
        )

        for skill, score in assessments.items():
            skill_scores[skill].append(score)

for skill in sorted(skill_scores):
    print(
        f"{skill}: "
        f"count={len(skill_scores[skill])}, "
        f"avg={sum(skill_scores[skill])/len(skill_scores[skill]):.2f}"
    )







# ASR: count=1124, avg=52.27
# BM25: count=309, avg=54.79
# BentoML: count=1157, avg=51.58
# CNN: count=1174, avg=51.29
# Computer Vision: count=1111, avg=52.11
# Data Science: count=1147, avg=51.06
# Deep Learning: count=284, avg=55.25
# Diffusion Models: count=1133, avg=51.38
# Elasticsearch: count=285, avg=55.89
# Embeddings: count=327, avg=55.33
# FAISS: count=303, avg=54.81
# Feature Engineering: count=1174, avg=51.95
# Fine-tuning LLMs: count=282, avg=55.06
# Forecasting: count=1167, avg=51.27
# GANs: count=1122, avg=52.78
# Haystack: count=314, avg=56.06
# Hugging Face Transformers: count=319, avg=55.88
# Image Classification: count=1120, avg=51.33
# Information Retrieval: count=343, avg=55.73
# Kubeflow: count=1105, avg=51.10
# LLMs: count=323, avg=54.28
# LangChain: count=295, avg=56.10
# Learning to Rank: count=327, avg=53.83
# LlamaIndex: count=291, avg=56.50
# LoRA: count=320, avg=55.15
# MLOps: count=1159, avg=52.61
# MLflow: count=1085, avg=52.40
# Machine Learning: count=335, avg=55.59
# Milvus: count=340, avg=54.14
# NLP: count=306, avg=53.97
# Object Detection: count=1145, avg=52.22
# OpenCV: count=1155, avg=52.19
# OpenSearch: count=319, avg=56.15
# PEFT: count=341, avg=55.74
# Pinecone: count=325, avg=56.03
# Prompt Engineering: count=312, avg=54.76
# PyTorch: count=340, avg=55.17
# Python: count=312, avg=55.62
# QLoRA: count=329, avg=54.98
# Qdrant: count=336, avg=55.97
# RAG: count=326, avg=55.64
# Recommendation Systems: count=325, avg=54.22
# Reinforcement Learning: count=1124, avg=52.30
# Semantic Search: count=301, avg=55.74
# Sentence Transformers: count=328, avg=55.02
# Speech Recognition: count=1159, avg=51.78
# Statistical Modeling: count=1088, avg=51.62
# TTS: count=1140, avg=52.41
# TensorFlow: count=326, avg=55.32
# Time Series: count=1111, avg=52.24
# Vector Search: count=326, avg=55.27
# Weaviate: count=321, avg=56.06
# Weights & Biases: count=1173, avg=51.99
# YOLO: count=1195, avg=52.02
# pgvector: count=340, avg=53.96
# scikit-learn: count=317, avg=55.39