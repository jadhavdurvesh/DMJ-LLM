from transformers import TrainingArguments

from trl import SFTTrainer

from config import (
    OUTPUT_DIR,
    LOG_DIR,
)

from dataset import load_dataset
from prompts import format_dataset
from trainer import build_model

from model_config import (
    EPOCHS,
    LEARNING_RATE,
    TRAIN_BATCH_SIZE,
    GRADIENT_ACCUMULATION_STEPS,
    WEIGHT_DECAY,
    LR_SCHEDULER,
    WARMUP_RATIO,
    SAVE_STRATEGY,
    SAVE_STEPS,
    SAVE_TOTAL_LIMIT,
    LOGGING_STEPS,
)


def main():
    print("\nLoading dataset...")
    dataset = load_dataset()

    print("\nFormatting prompts...")
    dataset = format_dataset(dataset)

    print("\nLoading model...")
    model, tokenizer = build_model()

    print("\nCreating training arguments...")

    training_args = TrainingArguments(
        output_dir=str(OUTPUT_DIR),
        overwrite_output_dir=True,

        num_train_epochs=EPOCHS,

        per_device_train_batch_size=TRAIN_BATCH_SIZE,

        gradient_accumulation_steps=GRADIENT_ACCUMULATION_STEPS,

        learning_rate=LEARNING_RATE,

        weight_decay=WEIGHT_DECAY,

        warmup_ratio=WARMUP_RATIO,

        lr_scheduler_type=LR_SCHEDULER,

        logging_steps=LOGGING_STEPS,

        save_strategy=SAVE_STRATEGY,

        save_steps=SAVE_STEPS,

        save_total_limit=SAVE_TOTAL_LIMIT,

        report_to="none",

        fp16=True,
    )

    print("\nCreating trainer...")

   trainer = SFTTrainer(
    model=model,
    args=training_args,
    train_dataset=dataset,
    processing_class=tokenizer,
)

    print("\nStarting training...\n")

    trainer.train()

    print("\nSaving model...")

    trainer.save_model(str(OUTPUT_DIR))

    tokenizer.save_pretrained(str(OUTPUT_DIR))

    print("\nTraining complete!")


if __name__ == "__main__":
    main()