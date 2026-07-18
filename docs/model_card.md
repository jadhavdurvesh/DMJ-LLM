---
base_model: Qwen/Qwen2.5-1.5B-Instruct
library_name: peft
license: apache-2.0
pipeline_tag: text-generation
language:
- en
tags:
- base_model:adapter:Qwen/Qwen2.5-1.5B-Instruct
- lora
- peft
- sft
- transformers
- trl
- engineering
- arduino
- mechatronics
- electronics
- iot
---

# DMJ LLM v1.0.0 Alpha

DMJ LLM is a custom engineering-focused language model created by **Durvesh Mukund Jadhav** under **DMJ Group**. It's a LoRA fine-tune of Qwen2.5-1.5B-Instruct, specialized for engineering education — Arduino, electronics, electrical engineering, IoT, mechatronics, and programming fundamentals.

This is an early alpha release. See **Limitations** before relying on it for anything beyond experimentation.

## Model Details

- **Base model:** [Qwen/Qwen2.5-1.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct) (Apache 2.0)
- **Method:** LoRA fine-tuning via [PEFT](https://github.com/huggingface/peft)
- **LoRA config:** rank 16, alpha 32, dropout 0.05, applied to all attention and MLP projections (`q_proj`, `k_proj`, `v_proj`, `o_proj`, `gate_proj`, `up_proj`, `down_proj`) across all 28 layers — ~18.5M trainable parameters (~1.2% of the base model)
- **Training data:** 1,418 instruction/response pairs curated across Arduino, C/C++/Python programming, electronics, electrical engineering, IoT, mechatronics, and model-identity examples
- **Training:** 1 epoch, effective batch size 8, linear learning-rate decay from 1.9e-4 to 9e-6, trained on Kaggle's free GPU tier
- **Author:** Durvesh Mukund Jadhav
- **Organization:** [DMJ Group](https://github.com/jadhavdurvesh/DMJ-LLM)

## How to Use

This repo is a LoRA **adapter**, not a standalone model — load it on top of the base model with `peft`:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel
import torch

base_id = "Qwen/Qwen2.5-1.5B-Instruct"
adapter_id = "Durveshjadhav/DMJ-LLM-v1"

tokenizer = AutoTokenizer.from_pretrained(adapter_id)
base_model = AutoModelForCausalLM.from_pretrained(base_id, torch_dtype=torch.bfloat16, device_map="auto")
model = PeftModel.from_pretrained(base_model, adapter_id)

messages = [{"role": "user", "content": "What is Ohm's Law?"}]
inputs = tokenizer.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt").to(model.device)
outputs = model.generate(inputs, max_new_tokens=200)
print(tokenizer.decode(outputs[0][inputs.shape[-1]:], skip_special_tokens=True))
```

## Intended Use

Educational and engineering assistance — explaining concepts and generating code in Arduino, electronics, electrical engineering, IoT, and mechatronics contexts.

## Limitations

- Small training set (1,418 examples) — reasoning depth and topic coverage are limited outside the domains listed above
- Trained for a single epoch with no held-out validation split, so generalization beyond the training data hasn't been measured
- May hallucinate or fall back to generic answers on topics outside its engineering domains
- DMJScript, a custom language by the same author, is not yet supported — planned for a future version
- Distributed as an adapter, not merged weights — requires `peft` and the base model to run

## Links

- **Code & datasets:** [github.com/jadhavdurvesh/DMJ-LLM](https://github.com/jadhavdurvesh/DMJ-LLM)
- **License:** Apache 2.0 (inherited from the base model)
