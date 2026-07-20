from dataset import load_dataset
from prompts import format_dataset

dataset = load_dataset()

dataset = format_dataset(dataset)

print(dataset[0]["text"])