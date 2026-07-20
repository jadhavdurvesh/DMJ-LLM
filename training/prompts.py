"""
Prompt formatting for DMJ LLM.
"""


def format_prompt(example):
    instruction = example["instruction"].strip()
    user_input = example["input"].strip()
    output = example["output"].strip()

    if user_input:
        user_message = f"{instruction}\n\nInput:\n{user_input}"
    else:
        user_message = instruction

    return {
        "text": (
            "<|im_start|>system\n"
            "You are DMJ LLM, a helpful AI assistant created by DMJ Group.<|im_end|>\n"
            "<|im_start|>user\n"
            f"{user_message}<|im_end|>\n"
            "<|im_start|>assistant\n"
            f"{output}<|im_end|>"
        )
    }


def format_dataset(dataset):
    return dataset.map(format_prompt)