import re
import csv
from collections import Counter

def count_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().lower()  # Read the text and convert to lowercase

        # Use regex to extract words (ignoring non-alphabetic characters)
        words = re.findall(r'\b\w+\b', text)

        # Count occurrences of each word
        word_counts = Counter(words)

    return word_counts

def write_to_csv(word_counts, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Word', 'Count']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write CSV header
        writer.writeheader()

        # Write the top 30 words and their counts to the CSV file
        for word, count in word_counts.most_common(30):
            writer.writerow({'Word': word, 'Count': count})

if __name__ == "__main__":
    # Replace 'your_text_file.txt' with the path to your text file
    input_file_path = 'AllText.txt'

    # Replace 'output_file.csv' with the desired CSV file name
    output_csv_file = 'output_file.csv'

    # Count occurrences of words
    word_counts = count_words(input_file_path)

    # Write the top 30 words and their counts to a CSV file
    write_to_csv(word_counts, output_csv_file)

    print("Top 30 words and their counts have been written to", output_csv_file)
