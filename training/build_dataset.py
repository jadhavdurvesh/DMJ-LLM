import json

data = [
    {
        "instruction": "What is a variable in C?",
        "response": "A variable is a named memory location used to store data."
    },
    {
        "instruction": "What is an array in C?",
        "response": "An array is a collection of elements of the same type stored in contiguous memory."
    },
    {
        "instruction": "What is Ohm's Law?",
        "response": "Ohm's Law states that V = I × R."
    },
    {
        "instruction": "What is Arduino?",
        "response": "Arduino is an open-source microcontroller platform used for electronics and embedded systems projects."
    }
]

with open("datasets/master_dataset.jsonl", "w") as f:
    for item in data:
        f.write(json.dumps(item) + "\n")

print("Dataset created.")