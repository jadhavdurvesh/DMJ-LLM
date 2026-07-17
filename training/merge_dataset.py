import json
import os

DATASET_DIR = "datasets"
OUTPUT_FILE = os.path.join(DATASET_DIR, "final_dataset.jsonl")

seen = set()
total = 0
unique = 0

with open(OUTPUT_FILE, "w", encoding="utf-8") as outfile:

    for filename in os.listdir(DATASET_DIR):

        if not filename.endswith(".jsonl"):
            continue

        if filename == "final_dataset.jsonl":
            continue

        filepath = os.path.join(DATASET_DIR, filename)

        print(f"Reading {filename}...")

        with open(filepath, "r", encoding="utf-8") as infile:

            for line in infile:

                total += 1

                try:
                    item = json.loads(line)

                    key = (
                        item.get("instruction", "").strip(),
                        item.get("response", "").strip()
                    )

                    if key not in seen:
                        seen.add(key)
                        outfile.write(
                            json.dumps(item, ensure_ascii=False) + "\n"
                        )
                        unique += 1

                except Exception as e:
                    print(f"Error in {filename}: {e}")

print("\nMerge Complete")
print(f"Total entries: {total}")
print(f"Unique entries: {unique}")
print(f"Saved to: {OUTPUT_FILE}")