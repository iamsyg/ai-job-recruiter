# utils/disqualifier_prototypes.py
"""
Prototype sentences for each disqualifier category. Candidate text gets
embedded once and compared via cosine similarity — this gives a continuous
confidence score per category instead of a boolean keyword hit.
"""

PROTOTYPES = {
    "research_only": [
        "Conducted academic research with publications, no production deployment experience.",
        "PhD research role focused on novel algorithms, never shipped to real users.",
        "Research scientist at a university lab, work was theoretical and experimental, not productionized.",
        "My work has been entirely on closed-source proprietary systems, no production-facing engineering.",
        "Published papers on machine learning algorithms with no production engineering experience.",
        "Academic researcher developing novel deep learning methods evaluated only on benchmark datasets.",
        "Focused on experimentation, literature review, and model evaluation rather than production systems.",
        "Research assistant building experimental NLP models for publications.",
        "Implemented algorithms for academic conferences instead of commercial applications.",
        "Worked on theoretical optimization and statistical learning with no engineering ownership.",
    ],
    "architecture_no_code": [
        "Moved into an architecture or tech lead role and no longer writes production code.",
        "I now spend my time on design documents, reviews, and high-level technical direction rather than coding.",
        "As a principal engineer I mentor others and review designs; my own hands-on coding has dropped off.",
        "Senior technical leadership role focused on strategy, with minimal day-to-day implementation work.",

        "Responsible for technical architecture and engineering strategy instead of implementation.",
        "Led multiple engineering teams while rarely contributing production code.",
        "Spent most of the time mentoring engineers rather than writing software.",
        "Owned platform architecture while implementation was delegated to other engineers.",
    ],
    "langchain_wrapper_only": [
        "Built a chatbot by calling the OpenAI API through LangChain, no underlying ML or retrieval engineering.",
        "My AI experience is recent projects wiring together hosted LLM APIs with prompt templates.",
        "Used GPT-4 and LangChain to build demos; my background before this was entirely non-technical.",
        "Followed LangChain tutorials to build a RAG demo, no production-scale retrieval or ranking work.",

        "Built AI assistants using hosted LLM APIs without implementing retrieval algorithms.",
        "Created RAG chatbots using existing frameworks rather than designing retrieval pipelines.",
        "Used LangChain, Pinecone, and OpenAI APIs to assemble chatbot applications.",
        "Developed AI applications by combining third-party LLM services.",
        "Fine-tuned prompts but did not build ranking or embedding pipelines.",
    ],
    "cv_speech_robotics_only": [
        "Computer vision engineer working on object detection and image classification models.",
        "Speech recognition and text-to-speech systems engineer, no NLP or text retrieval work.",
        "Robotics engineer building perception and control systems for autonomous machines.",

        "Built image segmentation and computer vision pipelines.",
        "Worked on OCR and image classification systems.",
        "Developed speech-to-text and text-to-speech models.",
        "Built wake-word detection and speaker recognition systems.",
        "Worked on robotics perception and SLAM algorithms.",
        "Implemented reinforcement learning for robot navigation.",
    ],
    "nlp_ir_exposure": [
        "Built search, retrieval, or ranking systems over text data using embeddings or NLP techniques.",
        "Worked on information retrieval, semantic search, or natural language understanding in production.",

        "Designed semantic search systems using dense vector embeddings.",
        "Built document retrieval pipelines with BM25 and vector search.",
        "Developed large-scale search ranking systems.",
        "Implemented recommendation algorithms using embeddings.",
        "Built retrieval-augmented generation systems with custom retrieval logic.",
        "Optimized search relevance using learning-to-rank techniques.",
    ],
    # "production_shipped": [
    #     "Shipped a ranking, search, or recommendation system to real users at meaningful scale in production.",
    #     "Owned an end-to-end ML system serving live traffic with measurable business impact.",
    # ],
}