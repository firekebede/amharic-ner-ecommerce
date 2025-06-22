# Amharic NER for Ethiopian E-Commerce Messages

This project focuses on Named Entity Recognition (NER) for Amharic text collected from Ethiopian Telegram e-commerce channels. It includes data collection, preprocessing, annotation in CoNLL format, model fine-tuning, and comparison.

## Tasks
- 🔁 Data Ingestion from Telegram
- 🧹 Preprocessing Amharic text
- 🏷️ CoNLL Annotation for Product, Price, Location
- 🤖 Model Fine-Tuning and Evaluation

## Folder Structure
amharic-ner-ecommerce/
│
├── data/
│   ├── raw/                    # Raw messages from Telegram (JSON or TXT)
│   ├── processed/              # Cleaned & structured text
│   └── labeled/                # CoNLL format labeled data
│
├── notebooks/                 # Jupyter notebooks for EDA, experiments
│
├── scripts/
│   ├── telegram_scraper.py    # Script to scrape Telegram messages
│   ├── preprocess.py          # Text preprocessing logic
│   └── label_helper.py        # Optional labeling interface/code
│
├── models/                    # Fine-tuned NER models
│
├── results/                   # Evaluation outputs, plots, comparisons
│
├── README.md
├── requirements.txt           # List of Python dependencies
└── .gitignore
