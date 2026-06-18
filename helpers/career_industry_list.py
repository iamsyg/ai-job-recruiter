# helpers/career_industry_list.py

import json

industries = set()

with open(r"C:\Users\Eternity\Dropbox\Projects\New folder\[PUB] India_runs_data_and_ai_challenge\[PUB] India_runs_data_and_ai_challenge\India_runs_data_and_ai_challenge\candidates.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        candidate = json.loads(line)

        for exp in candidate.get("career_history", []):
            industry = exp.get("industry")
            if industry:
                industries.add(industry.strip())

print(f"Unique industries: {len(industries)}")
print("Unique industries list:")

for industry in (industries):
    print(f" - {industry}")




# Unique industries: 24
# Unique industries list:
#  - AI Services
#  - Consumer Electronics
#  - Food Delivery
#  - Media
#  - HealthTech
#  - AI/ML
#  - Conglomerate
#  - Insurance Tech
#  - E-commerce
#  - IT Services
#  - Fintech
#  - Voice AI
#  - Paper Products
#  - Conversational AI
#  - Internet
#  - Manufacturing
#  - AdTech
#  - EdTech
#  - Gaming
#  - Software
#  - Transportation
#  - Consulting
#  - HealthTech AI
#  - SaaS