from dataset import load_dataset
from prompts import format_dataset
from trainer import build_model

from transformers import TrainingArguments
from trl import SFTTrainer

dataset = format_dataset(load_dataset())

model, tokenizer = build_model()

args = TrainingArguments(
    output_dir="./tmp",
    per_device_train_batch_size=1,
    do_train=False,
)

trainer = SFTTrainer(
    model=model,
    args=args,
    train_dataset=dataset,
    processing_class=tokenizer,
)

print("Trainer created successfully!")