# helpers/education/degree.py

import json

degree = set()

with open(r"C:\Users\Eternity\Dropbox\Projects\New folder\[PUB] India_runs_data_and_ai_challenge\[PUB] India_runs_data_and_ai_challenge\India_runs_data_and_ai_challenge\candidates.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        candidate = json.loads(line)

        for exp in candidate.get("education", []):
            deg = exp.get("degree")
            if deg:
                degree.add(deg.strip())

print(f"Unique degrees: {len(degree)}")
print("Unique degrees list:")

for deg in (degree):
    print(f" - {deg}")



# Unique degrees: 8
# Unique degrees list:
#  - B.Sc
#  - B.Tech
#  - M.Sc
#  - B.E.
#  - M.S.
#  - M.E.
#  - M.Tech
#  - Ph.D