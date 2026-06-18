# helpers/education/field_of_study.py

import json

field_of_study = set()

with open(r"C:\Users\Eternity\Dropbox\Projects\New folder\[PUB] India_runs_data_and_ai_challenge\[PUB] India_runs_data_and_ai_challenge\India_runs_data_and_ai_challenge\candidates.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        candidate = json.loads(line)

        for exp in candidate.get("education", []):
            fos = exp.get("field_of_study")
            if fos:
                field_of_study.add(fos.strip())

print(f"Unique field of study: {len(field_of_study)}")
print("Unique field of study list:")

for fos in (field_of_study):
    print(f" - {fos}")




# Unique field of study: 16
# Unique field of study list:
#  - Statistics
#  - Information Technology
#  - Chemical Engineering
#  - Mathematics
#  - Computer Science
#  - Machine Learning
#  - Commerce
#  - Artificial Intelligence
#  - Physics
#  - Electronics
#  - Data Science
#  - Electrical Engineering
#  - MBA
#  - Civil Engineering
#  - Computer Engineering
#  - Mechanical Engineering