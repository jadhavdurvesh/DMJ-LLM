from trainer import build_model

model, tokenizer = build_model()

print()

print(model.__class__.__name__)

print(tokenizer.__class__.__name__)