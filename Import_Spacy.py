import spacy

# Load the spaCy models
nlp_sci_sm = spacy.load("en_core_sci_sm")
nlp_bc5cdr = spacy.load("en_ner_bc5cdr_md")

# Function to extract entities
def extract_entities(text, model):
    doc = model(text)
    entities = [(X.text, X.label_) for X in doc.ents if X.label_ in ['DRUG', 'DISEASE']]
    return entities

# Read the .txt file
with open("output.txt", "r") as file:
    text = file.read()

# Extract entities using spaCy models
entities_sci_sm = extract_entities(text, nlp_sci_sm)
entities_bc5cdr = extract_entities(text, nlp_bc5cdr)