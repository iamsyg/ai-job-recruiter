# helpers/career_title_list.py

import json

titles = set()

with open(r"C:\Users\Eternity\Dropbox\Projects\New folder\[PUB] India_runs_data_and_ai_challenge\[PUB] India_runs_data_and_ai_challenge\India_runs_data_and_ai_challenge\candidates.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        title = json.loads(line)

        for exp in title.get("career_history", []):
            title = exp.get("title")
            if title:
                titles.add(title.strip())

print(f"Unique titles: {len(titles)}")
print("Unique titles list:")

for t in (titles):
    print(f" - {t}")








# Unique titles: 48
# Unique titles list:
#  - Graphic Designer
#  - Analytics Engineer
#  - Senior Software Engineer (ML)
#  - Content Writer
#  - Software Engineer
#  - NLP Engineer
#  - .NET Developer
#  - Applied ML Engineer
#  - Senior NLP Engineer
#  - Search Engineer
#  - Business Analyst
#  - Senior ML Engineer — Search & Ranking
#  - Lead AI Engineer
#  - Project Manager
#  - Customer Support
#  - AI Research Engineer
#  - Cloud Engineer
#  - Recommendation Systems Engineer
#  - Computer Vision Engineer
#  - Mobile Developer
#  - DevOps Engineer
#  - Marketing Manager
#  - Junior ML Engineer
#  - Java Developer
#  - Senior Data Scientist
#  - Data Analyst
#  - Staff Machine Learning Engineer
#  - AI Specialist
#  - Civil Engineer
#  - Senior Machine Learning Engineer
#  - Senior Applied Scientist
#  - HR Manager
#  - Backend Engineer
#  - Data Engineer
#  - Senior Data Engineer
#  - Full Stack Developer
#  - AI Engineer
#  - ML Engineer
#  - Data Scientist
#  - Machine Learning Engineer
#  - Frontend Engineer
#  - Senior Software Engineer
#  - Accountant
#  - QA Engineer
#  - Sales Executive
#  - Senior AI Engineer
#  - Mechanical Engineer
#  - Operations Manager