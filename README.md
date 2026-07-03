# 🤖 AI Job Recruiter
### Redrob Hackathon – Intelligent Candidate Discovery & Ranking Challenge

An AI-powered candidate ranking system that combines **BM25 retrieval**, **semantic embeddings**, and **feature-based reranking** to identify the best candidates for a given Job Description.

---

## Features

- BM25 lexical retrieval
- Semantic candidate retrieval using BGE embeddings
- Rule-based feature engineering
- Behavioral signal analysis
- Candidate reranking
- Automatic reasoning generation
- Streamlit demo application
- CSV generation compatible with the Redrob Hackathon submission format

---

# Architecture

```
                 Job Description
                        │
                        ▼
             Feature Extraction (LLM)
                        │
                        ▼
              Structured JD Features
                        │
        ┌───────────────┴───────────────┐
        ▼                               ▼
   BM25 Query                    JD Embedding
        │                               │
        ▼                               ▼
  BM25 Candidate Set          Embedding Similarity
        └───────────────┬───────────────┘
                        ▼
               Candidate Retrieval
                        ▼
           Feature Engineering Layer
                        ▼
       ┌────────────────────────────────┐
       │ Skills                         │
       │ Career History                 │
       │ Education                      │
       │ Certifications                 │
       │ Languages                      │
       │ Location                       │
       │ Redrob Behavioral Signals      │
       │ Qualifying Signals             │
       │ Disqualifying Signals          │
       └────────────────────────────────┘
                        ▼
                 Final Score
                        ▼
                 Ranked Candidates
                        ▼
             CSV Submission Output
```

---

# Scoring Formula

The final score combines three components:

```
Final Score =
0.40 × Embedding Score
+ 0.15 × BM25 Score
+ 0.45 × Feature Score
```

The feature score includes:

- Skill matching
- Career progression
- Experience
- Education
- Certifications
- Language proficiency
- Relocation preference
- Redrob behavioral signals
- Qualifying signals
- Disqualifying signals

---

# Tech Stack

- Python 3.13
- Streamlit
- Sentence Transformers (BGE)
- Rank-BM25
- Google Gemini
- NumPy
- Pandas
- Pydantic

---

# Repository Structure

```
.
├── model/
├── schema/
├── score/
├── src/
├── utils/
├── streamlit_app.py
├── main.py
├── requirements.txt
├── validate_submission.py
└── README.md
```

---

# Installation

Clone the repository.

```bash
git clone https://github.com/iamsyg/ai-job-recruiter
cd ai-job-recruiter
```

Create a virtual environment.

```bash
python -m venv .venv
```

Activate it.

Windows

```bash
.venv\Scripts\activate
```

Linux/Mac

```bash
source .venv/bin/activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file.

```
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

---

# Running the Streamlit App

```bash
streamlit run streamlit_app.py
```

Upload:

- `sample_candidates.json`
- or `candidates.jsonl`

The application will generate:

- Ranked candidates
- Submission CSV

---

# Running the Ranking Pipeline

Generate the final submission CSV.

```bash
python main.py
```

---

# Validate Submission

Before uploading to the hackathon portal:

```bash
python validate_submission.py submission.csv
```

If valid:

```
Submission is valid.
```

---

# Compute Constraints

Designed to satisfy the Redrob Hackathon requirements.

- CPU only
- No external API calls during ranking
- ≤16 GB RAM
- ≤5 minutes ranking stage

LLM usage is restricted to preprocessing and feature extraction.

---

# Methodology

The ranking system uses a hybrid retrieval architecture.

### Stage 1 — BM25 Retrieval

Lexical search retrieves the most relevant candidates based on the job description.

### Stage 2 — Semantic Retrieval

Candidates are embedded using the BAAI BGE embedding model and ranked by cosine similarity.

### Stage 3 — Feature Engineering

Each candidate is evaluated on multiple handcrafted features:

- Skills
- Career history
- Education
- Certifications
- Languages
- Location
- Redrob behavioral signals
- Qualifiers
- Disqualifiers

### Stage 4 — Final Ranking

The final score is computed using weighted retrieval and feature scores, followed by deterministic tie-breaking using Candidate ID.

---

# Streamlit Demo

The deployed Streamlit application allows users to:

- Upload candidate files
- Execute the ranking pipeline
- Preview the top-ranked candidates
- Download a submission-ready CSV

---

# Reproducibility

Run the complete pipeline using:

```bash
python main.py
```

or launch the interactive demo:

```bash
streamlit run streamlit_app.py
```

---

# AI Tools Used

- ChatGPT (architecture discussion, debugging, code review)

No hosted LLM APIs are used during the ranking stage.

---

# Author

**Swayam Gupta**

GitHub:
https://github.com/iamsyg

Streamlit:
https://ai-job-recruiter-bnceabwk62qnmkty5ch6x4.streamlit.app/

---

# License

This project was developed for the Redrob Intelligent Candidate Discovery & Ranking Challenge.