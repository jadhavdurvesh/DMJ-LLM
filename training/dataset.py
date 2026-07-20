import json
from pathlib import Path
from datasets import Dataset

from config import DATASET_PATH


def load_dataset():
    """
    Load the DMJ dataset from JSONL.
    """

    if not Path(DATASET_PATH).exists():
        raise FileNotFoundError(f"Dataset not found: {DATASET_PATH}")

    records = []

    with open(DATASET_PATH, "r", encoding="utf-8") as file:
        for line in file:
            if not line.strip():
                continue

            item = json.loads(line)

            records.append(
                {
                    "instruction": item.get("instruction", ""),
                    "input": item.get("input", ""),
                    "output": item.get("output", ""),
                }
            )

    print(f"Loaded {len(records)} samples")

    return Dataset.from_list(records)


if __name__ == "__main__":
    dataset = load_dataset()

    print(dataset)

    print(dataset[0])