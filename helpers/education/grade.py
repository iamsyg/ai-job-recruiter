# helpers/education/grade.py

from collections import Counter
import json

cgpa_counter = Counter()
percentage_counter = Counter()
other_counter = Counter()

with open(r"C:\Users\Eternity\Dropbox\Projects\New folder\[PUB] India_runs_data_and_ai_challenge\[PUB] India_runs_data_and_ai_challenge\India_runs_data_and_ai_challenge\candidates.jsonl", "r", encoding="utf-8") as f:

    for line in f:
        candidate = json.loads(line)

        for edu in candidate.get("education", []):

            grade = edu.get("grade")

            if not grade:
                continue

            grade = str(grade).strip().lower()

            if "%" in grade:
                percentage_counter[grade] += 1

            elif "cgpa" in grade or "/10" in grade:
                cgpa_counter[grade] += 1

            else:
                other_counter[grade] += 1

print("\n=== CGPA ===")
for grade, count in cgpa_counter.most_common():
    print(f"{grade}: {count}")

print("\n=== PERCENTAGE ===")
for grade, count in percentage_counter.most_common():
    print(f"{grade}: {count}")

print("\n=== OTHER ===")
for grade, count in other_counter.most_common():
    print(f"{grade}: {count}")