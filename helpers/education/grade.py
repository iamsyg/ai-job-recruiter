# helpers/education/grade.py

import json

cgpa_count = 0
percentage_count = 0
other_count = 0

with open(r"C:\Users\Eternity\Dropbox\Projects\New folder\[PUB] India_runs_data_and_ai_challenge\[PUB] India_runs_data_and_ai_challenge\India_runs_data_and_ai_challenge\candidates.jsonl", "r", encoding="utf-8") as f:

    for line in f:
        candidate = json.loads(line)

        for edu in candidate.get("education", []):

            grade = edu.get("grade")

            if not grade:
                continue

            grade = str(grade).strip().lower()

            if "%" in grade:
                percentage_count += 1

            elif "cgpa" in grade or "/10" in grade or "gpa" in grade:
                cgpa_count += 1

            else:
                other_count += 1

print(f"CGPA grades: {cgpa_count}")
print(f"Percentage grades: {percentage_count}")
print(f"Other grades: {other_count}")