import pandas as pd
from datasets import Dataset, DatasetDict

def load_conll_data(path):
    with open(path, encoding='utf-8') as f:
        lines = f.readlines()

    sentences, labels = [], []
    tokens, ner_tags = [], []

    for line in lines:
        line = line.strip()
        if not line:
            if tokens:
                sentences.append(tokens)
                labels.append(ner_tags)
                tokens, ner_tags = [], []
        else:
            token, tag = line.rsplit(" ", 1)
            tokens.append(token)
            ner_tags.append(tag)

    if tokens:
        sentences.append(tokens)
        labels.append(ner_tags)

    return Dataset.from_dict({"tokens": sentences, "ner_tags": labels})

def prepare_dataset(path):
    dataset = load_conll_data(path)
    split = dataset.train_test_split(test_size=0.2, seed=42)
    return DatasetDict({"train": split["train"], "test": split["test"]})

