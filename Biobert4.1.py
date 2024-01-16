from transformers import AutoTokenizer, AutoModelForTokenClassification
import torch

# Load the BioBERT model and tokenizer
model_name = "monologg/biobert_v1.1_pubmed"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForTokenClassification.from_pretrained(model_name)

# Function to extract entities
def extract_biobert_entities(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding="max_length", max_length=512)
    outputs = model(**inputs)
    logits = outputs.logits
    predicted_labels = torch.argmax(logits, dim=-1)
    entities = []
    for start, end, label in zip(predicted_labels.tolist()[0], predicted_labels.tolist()[1], predicted_labels.tolist()[2]):
        if start == 1 and end == len(text.split()) - 1:
            continue
        if label == 3:  # Change this to the appropriate label for drugs and diseases in BioBERT
            entities.append((text.split()[start - 1:end], 'DRUG' if label == 3 else 'DISEASE'))
    return entities

# Extract entities using BioBERT
entities_biobert = extract_biobert_entities(text)