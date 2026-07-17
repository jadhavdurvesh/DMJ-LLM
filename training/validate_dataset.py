import json

FILE = "datasets/final_dataset.jsonl"

count = 0
errors = 0

with open(FILE, "r", encoding="utf-8") as f:

    for line_num, line in enumerate(f, start=1):

        try:
            data = json.loads(line)

            if "instruction" not in data:
                print(f"Missing instruction at line {line_num}")
                errors += 1

            if "response" not in data:
                print(f"Missing response at line {line_num}")
                errors += 1

            count += 1

        except Exception as e:
            print(f"Invalid JSON at line {line_num}: {e}")
            errors += 1

print("\nValidation Complete")
print(f"Valid entries: {count}")
print(f"Errors found: {errors}")