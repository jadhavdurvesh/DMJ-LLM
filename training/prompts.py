"""
Prompt formatting for DMJ LLM.
"""


SYSTEM_PROMPT = (
    "You are DMJ LLM, a helpful AI assistant created by DMJ Group."
)


def format_prompt(example):
    instruction = str(example.get("instruction", "")).strip()
    user_input = str(example.get("input", "")).strip()
    output = str(example.get("output", "")).strip()

    if user_input:
        user_message = f"{instruction}\n\nInput:\n{user_input}"
    else:
        user_message = instruction

    text = (
        "<|im_start|>system\n"
        f"{SYSTEM_PROMPT}<|im_end|>\n"
        "<|im_start|>user\n"
        f"{user_message}<|im_end|>\n"
        "<|im_start|>assistant\n"
        f"{output}<|im_end|>"
    )

    return {
        "text": text
    }


def format_dataset(dataset):
    return dataset.map(
        format_prompt,
        remove_columns=dataset.column_names,
    )