# src/extract_disqualifier_features.py
"""
Precompute-only step. Produces a confidence score [0,1] per candidate per
disqualifier category via embedding similarity, blended with structural
signals where available. Run once over the full candidate pool, cache to
disk as disqualifier_features.npz / .json. NOT called from rank.py.
"""

import numpy as np
from datetime import datetime
from utils.disqualifier_prototypes import PROTOTYPES
from schema.candidate_schema import CandidateSchema

from schema.candidate_features_schema import Disqualifiers

# from src.build_candidate_text import build_candidate_text

from utils.career_title import NON_TECH_TITLES

CONSULTING_FIRMS = {
    "tcs", "infosys", "wipro", "accenture", "cognizant", "capgemini",
    "hcl", "tech mahindra", "mindtree", "ltimindtree",
}

CV_SPEECH_ROBOTICS_SKILLS = {
    "image classification", "object detection", "yolo", "opencv", "cnn", "gans",
    "speech recognition", "tts", "computer vision",
}
NLP_IR_SKILLS = {
    "nlp", "information retrieval", "embeddings", "vector search", "bm25",
    "sentence transformers", "hugging face transformers", "prompt engineering",
}

def _embed_prototypes(model):
    """Embed each prototype group once; return dict[group] -> mean unit vector."""

    proto_vecs = {}
    for group, sentences in PROTOTYPES.items():

        # vecs = model.encode(
        #     sentences, 
        #     normalize_embeddings=True,
        #     show_progress_bar=True,
        # )

        proto_vecs[group] = model.encode(
            sentences,
            normalize_embeddings=True,
            show_progress_bar=True,
        )

        # proto_vecs[group] = vecs.mean(axis=0)
        # proto_vecs[group] /= np.linalg.norm(proto_vecs[group])
    return proto_vecs


# def _candidate_text(candidate: CandidateSchema) -> str:
#     # parts = [candidate.profile.summary or ""]
#     # for role in candidate.career_history:
#     #     parts.append(f"{role.title}. {role.description}")
#     # return "\n".join(parts)
#     return build_candidate_text(candidate)


def _months_since(date_str: str) -> float:
    d = datetime.strptime(date_str, "%Y-%m-%d")
    return (datetime.now() - d).days / 30.0


def _job_hopper_confidence(candidate: CandidateSchema) -> float:
    """Structural — average tenure + count of sub-18-month stints, scaled to [0,1]."""

    SHORT_STINT_THRESHOLD = 18
    SAFE_AVG_TENURE  = 27

    roles = candidate.career_history

    if len(roles) < 2:
        return 0.0
    
    durations = [r.duration_months for r in roles]
    avg_tenure = sum(durations) / len(durations)
    short_stints = sum(1 for d in durations if d < SHORT_STINT_THRESHOLD)
    short_ratio = short_stints / len(roles)

    # confidence rises as avg tenure drops below ~24mo and short-stint ratio rises
    tenure_signal = max(0.0, min(1.0, (SAFE_AVG_TENURE - avg_tenure) / SHORT_STINT_THRESHOLD))
    stint_signal = short_ratio
    return round(0.5 * tenure_signal + 0.5 * stint_signal, 3)


def _architecture_no_code_structural(candidate: CandidateSchema) -> float:
    """Structural assist: current role is senior-sounding by title-tier proxy + long tenure
    without hands-on skill duration growth recently. Kept light; embeddings carry most weight."""

    current = next((r for r in candidate.career_history if r.is_current), None)

    if not current:
        return 0.0
    
    title = current.title.lower()
    senior_markers = ("lead", "architect", "principal", "head", "director", "manager")

    if any(m in title for m in senior_markers) and current.duration_months >= 18:
        return 0.4
    
    return 0.0


def extract_disqualifier_features(candidate: CandidateSchema, proto_vecs: dict, candidate_embedding) -> dict:

    CONF_THRESHOLDS = {
        # (floor, ceil)
        # floor = ~P75 of full population (above noise, below signal)
        # ceil  = ~P95 (clearly matching the disqualifier)
        "research_only":              (0.51, 0.56),
        "architecture_no_code":       (0.57, 0.62),
        "langchain_wrapper_only":     (0.59, 0.65),
        "cv_speech_robotics_only":    (0.58, 0.65),
        "nlp_ir_exposure":            (0.53, 0.61),  # positive signal, same logic
    }

    sim = {
        group: float((candidate_embedding @ proto_vecs[group].T).max())
        for group in proto_vecs
    }

    if candidate.candidate_id == "CAND_0007411":
        print("Disqualifier sims for CAND_0007411")
        print(sim["research_only"])
        print("\n \n \n")


    # cosine sims for short prototype-vs-document text typically land ~0.1–0.5;
    # rescale relative to the production_shipped baseline so scores are comparable
    def conf(group: str, sim_val: float) -> float:
        floor, ceil = CONF_THRESHOLDS[group]

        if group == "research_only" and candidate.candidate_id == "CAND_0007411":

            print(f"research_only sim: {sim_val}, floor: {floor}, ceil: {ceil}")
            value = (sim[group] - floor) / (ceil - floor)
            print(group, sim[group], value)
            
        return round(max(0.0, min(1.0, (sim_val - floor) / (ceil - floor))), 3)

    research_conf    = conf("research_only", sim["research_only"])
    arch_conf        = max(conf("architecture_no_code", sim["architecture_no_code"]), _architecture_no_code_structural(candidate))
    langchain_conf   = conf("langchain_wrapper_only",  sim["langchain_wrapper_only"])

    cv_sim   = conf("cv_speech_robotics_only", sim["cv_speech_robotics_only"])
    nlp_sim  = conf("nlp_ir_exposure", sim["nlp_ir_exposure"])
    cv_without_nlp_conf = round(max(0.0, cv_sim - nlp_sim), 3)

    job_hop_conf = _job_hopper_confidence(candidate)

    return Disqualifiers(
        research_only_confidence=research_conf,
        architecture_no_code_confidence=arch_conf,
        langchain_wrapper_only_confidence=langchain_conf,
        cv_speech_robotics_without_nlp_confidence=cv_without_nlp_conf,
        job_hopper_confidence=job_hop_conf,
    )

    # return {

    #     "research_similarity": sim["research_only"],
    #     "architecture_similarity": sim["architecture_no_code"],
    #     "langchain_similarity": sim["langchain_wrapper_only"],
    #     "cv_similarity": sim["cv_speech_robotics_only"],
    #     "nlp_ir_similarity": sim["nlp_ir_exposure"],

    #     "research_only_confidence": research_conf,
    #     "architecture_no_code_confidence": arch_conf,
    #     "langchain_wrapper_only_confidence": langchain_only_conf,
    #     "cv_speech_robotics_without_nlp_confidence": cv_without_nlp_conf,
    #     "job_hopper_confidence": job_hop_conf,
    # }