import json
from pathlib import Path

from datasets import Dataset

from config import DATASET_PATH


def load_dataset():
    """
    Load the DMJ dataset from JSONL.
    """

    dataset_path = Path(DATASET_PATH)

    if not dataset_path.exists():
        raise FileNotFoundError(f"Dataset not found: {dataset_path}")

    records = []

    with open(dataset_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            item = json.loads(line)

            records.append(
                {
                    "instruction": str(item.get("instruction", "")).strip(),
                    "input": str(item.get("input", "")).strip(),
                    "output": str(item.get("output", "")).strip(),
                }
            )

    if len(records) == 0:
        raise ValueError("Dataset is empty.")

    print(f"Loaded {len(records)} samples")

    return Dataset.from_list(records)


if __name__ == "__main__":
    dataset = load_dataset()

    print(dataset)
    print(dataset[0])