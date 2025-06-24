import json

# Load the cleaned data
with open("../data/processed/messages_cleaned.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Define entity options
entity_options = {
    "1": "B-Product",
    "2": "I-Product",
    "3": "B-LOC",
    "4": "I-LOC",
    "5": "B-PRICE",
    "6": "I-PRICE",
    "0": "O"
}

def label_message(message):
    tokens = message.strip().split()
    labeled_lines = []

    print("\n--- Message to Label ---")
    print(" ".join(tokens))
    print("------------------------")
    print("Use:")import os
import pandas as pd

# Path to your labeled CoNLL-format .txt file
input_path = "../data/labeled/labeled_telegram_product_price_location.txt"
output_path = "../data/labeled/labeled_telegram_ner.csv"

# Read and parse the file
with open(input_path, "r", encoding="utf-8") as f:
    lines = f.read().strip().split("\n")

sentences = []
tokens, labels = [], []

for line in lines:
    if line.strip() == "":
        if tokens:
            sentences.append((tokens, labels))
            tokens, labels = [], []
    else:
        parts = line.strip().split()
        if len(parts) == 2:
            token, label = parts
            tokens.append(token)
            labels.append(label)

# Ensure last sentence is added
if tokens:
    sentences.append((tokens, labels))

# Create DataFrame
csv_data = []
for i, (tokens, labels) in enumerate(sentences):
    for token, label in zip(tokens, labels):
        csv_data.append({"sentence_id": i, "token": token, "label": label})

df = pd.DataFrame(csv_data)
df.to_csv(output_path, index=False, encoding="utf-8")

print(f"✅ CSV saved to {output_path}")

    for k, v in entity_options.items():
        print(f"{k}: {v}")
    print("------------------------")

    for token in tokens:
        print(f"\nToken: {token}")
        label = input("Enter label (0-6): ").strip()
        label_tag = entity_options.get(label, "O")
        labeled_lines.append(f"{token} {label_tag}")

    return labeled_lines

# Output file
output_file = "../data/labeled/ner_conll_labels.txt"

# Label N messages
N = 5  # Change this to 30–50 later
with open(output_file, "w", encoding="utf-8") as out_f:
    for i in range(N):
        msg = data[i]["Cleaned_Message"]
        try:
            labeled = label_message(msg)
            for line in labeled:
                out_f.write(line + "\n")
            out_f.write("\n")  # blank line between messages
        except KeyboardInterrupt:
            print("Labeling interrupted.")
            break

print(f"\n✅ {N} messages labeled and saved to: {output_file}")
