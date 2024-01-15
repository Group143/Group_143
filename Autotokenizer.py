from transformers import AutoTokenizer
from collections import Counter
 
def count_unique_tokens(file_path, model_name):
    # Load the AutoTokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_name)
 
    # Read the text from the file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
 
    # Tokenize the text
    tokens = tokenizer.tokenize(tokenizer.decode(tokenizer.encode(text, add_special_tokens=False)))
 
    # Count occurrences of each token
    token_counts = Counter(tokens)
 
    return token_counts
 
def get_top_30_tokens(token_counts):
    # Return the top 30 tokens and their counts
    return token_counts.most_common(30)
 
if __name__ == "__main__":
    input_file_path = 'AllText.txt'
 
    model_name = 'bert-base-uncased'
    # 'distilbert-base-uncased'
    #'bert-base-uncased'
 
    # Count unique tokens
    token_counts = count_unique_tokens(input_file_path, model_name)
 
    # Get the top 30 tokens and their counts
    top_30_tokens = get_top_30_tokens(token_counts)
 
    # Print the top 30 tokens and their counts
    print("Top 30 tokens and their counts:")
    for token, count in top_30_tokens:
        print(f"{token}: {count}")