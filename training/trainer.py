import torch

from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
)

from peft import (
    LoraConfig,
    get_peft_model,
)

from model_config import (
    MODEL_NAME,
    LORA_R,
    LORA_ALPHA,
    LORA_DROPOUT,
    LORA_BIAS,
    TARGET_MODULES,
)


def load_tokenizer():
    print(f"Loading tokenizer: {MODEL_NAME}")

    tokenizer = AutoTokenizer.from_pretrained(
        MODEL_NAME,
        trust_remote_code=True,
    )

    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    tokenizer.padding_side = "right"

    return tokenizer


def load_model():
    print(f"Loading model: {MODEL_NAME}")

    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        torch_dtype=torch.float16,
        device_map="auto",
        trust_remote_code=True,
    )

    model.config.use_cache = False

    return model


def get_lora_config():
    return LoraConfig(
        r=LORA_R,
        lora_alpha=LORA_ALPHA,
        lora_dropout=LORA_DROPOUT,
        bias=LORA_BIAS,
        target_modules=TARGET_MODULES,
        task_type="CAUSAL_LM",
    )


def build_model():
    tokenizer = load_tokenizer()

    model = load_model()

    peft_config = get_lora_config()

    model = get_peft_model(model, peft_config)

    model.print_trainable_parameters()

    return model, tokenizer, peft_config