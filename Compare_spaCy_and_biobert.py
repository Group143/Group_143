# Compare spaCy models
common_entities = set(entities_sci_sm).intersection(entities_bc5cdr)
unique_sci_sm = set(entities_sci_sm) - common_entities
unique_bc5cdr = set(entities_bc5cdr) - common_entities

# Compare spaCy models and BioBERT
common_entities_all = set(entities_sci_sm + entities_bc5cdr).intersection(entities_biobert)
unique_spacy = set(entities_sci_sm + entities_bc5cdr) - common_entities_all
unique_biobert = set(entities_biobert) - common_entities_all

# Check for most common words
def most_common_words(entities, label):
    words = [word for word, _ in entities if label in _]
    return Counter(words).most_common()

# Check the difference
print("Common Entities:", len(common_entities_all))
print("Unique spaCy Entities:", len(unique_spacy))
print("Unique BioBERT Entities:", len(unique_biobert))
print("Most common drugs (spaCy):", most_common_words(entities_sci_sm + entities_bc5cdr, 'DRUG'))
print("Most common diseases (spaCy):", most_common_words(entities_sci_sm + entities_bc5cdr, 'DISEASE'))
print("Most common drugs (BioBERT):", most_common_words(entities_biobert, 'DRUG'))
print("Most common diseases (BioBERT):", most_common_words(entities_biobert, 'DISEASE'))