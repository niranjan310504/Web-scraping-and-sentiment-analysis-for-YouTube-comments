# cleaner.py
import pandas as pd
import re
import os

def clean_comment(text):
    if isinstance(text, str):  # Ensure it's a string before processing
        text = text.lower()
        text = re.sub(r'http\S+|www\S+', '', text)  # Remove URLs
        text = re.sub(r'[^a-zA-Z\s]', '', text)     # Remove non-alphabetic characters
        text = re.sub(r'\s+', ' ', text).strip()    # Normalize whitespace
    else:
        text = ""  # Handle non-string values (e.g., NaN)
    return text

def clean_comments():
    input_file = 'youtube_comments.csv'
    
    if not os.path.exists(input_file):
        print(f"Error: File '{input_file}' not found.")
        return

    try:
        df = pd.read_csv(input_file)
    except Exception as e:
        print(f"Error reading the CSV file: {e}")
        return

    # Remove rows where 'Comment' is NaN or an empty string
    df = df.dropna(subset=['Comment']).reset_index(drop=True)
    
    if df.empty:
        print("No valid comments to clean.")
        return
    
    # Apply cleaning function
    df['Cleaned_Comment'] = df['Comment'].apply(clean_comment)

    output_file = 'cleaned_comments.csv'
    
    try:
        df.to_csv(output_file, index=False)
        print(f"Cleaned comments saved to {output_file}")
    except Exception as e:
        print(f"Error saving the cleaned CSV file: {e}")

if __name__ == '__main__':
    clean_comments()
