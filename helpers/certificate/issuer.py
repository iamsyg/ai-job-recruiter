# helpers/certificate/issuer.py

import json

certificates_issuer = set()

with open(r"C:\Users\Eternity\Dropbox\Projects\New folder\[PUB] India_runs_data_and_ai_challenge\[PUB] India_runs_data_and_ai_challenge\India_runs_data_and_ai_challenge\candidates.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        candidate = json.loads(line)

        for exp in candidate.get("certifications", []):
            issuer = exp.get("issuer")
            if issuer:
                certificates_issuer.add(issuer.strip())

print(f"Unique certificate issuers: {len(certificates_issuer)}")
print("Unique certificate issuers list:")

for issuer in (certificates_issuer):
    print(f" - {issuer}")



# Unique certificate issuers: 6
# Unique certificate issuers list:
#  - Scrum Alliance
#  - ASQ
#  - Coursera/DeepLearning.AI
#  - DeepLearning.AI
#  - AWS
#  - Google Cloud