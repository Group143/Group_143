import csv
import glob
import os

# Define a function to convert a CSV file to a text file
def csv_to_txt(csv_file, txt_file):
    # Open the CSV file in read mode
    with open(csv_file, 'r') as f:
        # Use the DictReader to read the CSV file and store the rows as dictionaries
        reader = csv.DictReader(f)
        rows = [row for row in reader]

    # Open the text file in write mode
    with open(txt_file, 'w') as f:
        # Write each row as a string to the text file
        for row in rows:
            f.write(str(row) + '\n')

# Define the directory path where the CSV files are located
dir_path = 'C:\\Users\\Ramu\\Downloads\\Assignment 2\\'

# Use glob to find all CSV files in the directory
csv_files = glob.glob(os.path.join(dir_path, '*.csv'))

# Loop through each CSV file
for csv_file in csv_files:
    # Extract the filename without the extension
    filename = os.path.splitext(os.path.basename(csv_file))[0]

    # Construct the path to the text file
    txt_file = os.path.join(dir_path, filename + '.txt')

    # Call the csv_to_txt function to convert the CSV file to a text file
    csv_to_txt(csv_file, txt_file)