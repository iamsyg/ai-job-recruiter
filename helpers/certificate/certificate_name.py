# helpers/certificate/certificate_name.py

import json

certificates_name = set()

with open(r"C:\Users\Eternity\Dropbox\Projects\New folder\[PUB] India_runs_data_and_ai_challenge\[PUB] India_runs_data_and_ai_challenge\India_runs_data_and_ai_challenge\candidates.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        candidate = json.loads(line)

        for exp in candidate.get("certifications", []):
            name = exp.get("name")
            if name:
                certificates_name.add(name.strip())

print(f"Unique certificates: {len(certificates_name)}")
print("Unique certificates list:")

for certificate in (certificates_name):
    print(f" - {certificate}")




# Unique certificates: 8
# Unique certificates list:
#  - LangChain for LLM Application Development
#  - Six Sigma Green Belt
#  - Deep Learning Specialization
#  - AWS Certified Machine Learning Specialty
#  - Scrum Master Certified
#  - AWS Certified Cloud Practitioner
#  - Google Cloud Professional ML Engineer
#  - NLP Specialization