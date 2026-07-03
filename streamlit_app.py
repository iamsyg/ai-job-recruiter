# streamlit_app.py

import os, tempfile, pandas as pd, streamlit as st
from utils.load_candidates import load_candidates
from src.pipeline_streamlit import run_pipeline_streamlit
import traceback

st.set_page_config(page_title="AI Job Recruiter", layout="wide")
st.title("🤖 AI Job Recruiter")

uploaded = st.file_uploader(
    "Upload candidate file (.json or .jsonl)",
    type=["json", "jsonl"],
)

if uploaded:
    # FIX: preserve original suffix so load_candidates branches correctly
    original_suffix = os.path.splitext(uploaded.name)[-1]  # ".json" or ".jsonl"

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=original_suffix,          # was hardcoded ".jsonl"
    ) as tmp:
        tmp.write(uploaded.read())
        temp_path = tmp.name

    if st.button("Rank Candidates", type="primary"):
        try:
            with st.spinner("Ranking candidates..."):
                candidates = load_candidates(temp_path)
                try:
                    results = run_pipeline_streamlit(candidates)
                except Exception:
                    st.code(traceback.format_exc())
                    st.stop()
        except Exception as e:
            st.error(f"Error while ranking candidates:\n\n{e}")
        else:
            st.success(f"Successfully ranked {len(results)} candidates.")
            rows = []
            for rank, r in enumerate(results[:100], start=1):
                reasoning = r["reasoning"]
                strengths = reasoning["strengths"][:2]
                concerns  = reasoning["concerns"][:1]
                text = "; ".join(strengths)
                if concerns:
                    text += ". Concern: " + concerns[0]
                rows.append({
                    "candidate_id": r["candidate_id"],
                    "rank":         rank,
                    "score":        r["final_score"],
                    "reasoning":    text,
                })
            df = pd.DataFrame(rows)
            st.dataframe(df, use_container_width=True, hide_index=True)
            st.download_button(
                label="⬇ Download Submission CSV",
                data=df.to_csv(index=False).encode("utf-8"),
                file_name="submission.csv",
                mime="text/csv",
            )
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)