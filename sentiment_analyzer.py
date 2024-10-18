# sentiment_analyzer.py
import pandas as pd
import os
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    if isinstance(text, str) and text.strip():  # Ensure valid non-empty text
        score = analyzer.polarity_scores(text)['compound']
        return 'Positive' if score > 0.05 else 'Negative' if score < -0.05 else 'Neutral'
    return 'Neutral'  # Default to Neutral for invalid or empty text

def perform_analysis():
    input_file = 'cleaned_comments.csv'
    
    if not os.path.exists(input_file):
        print(f"Error: File '{input_file}' not found.")
        return

    try:
        df = pd.read_csv(input_file)
    except Exception as e:
        print(f"Error reading the CSV file: {e}")
        return

    if df.empty:
        print("No comments available for sentiment analysis.")
        return

    # Apply sentiment analysis function
    df['Sentiment_Label'] = df['Cleaned_Comment'].apply(analyze_sentiment)

    output_file = 'sentiment_results.csv'
    
    try:
        df.to_csv(output_file, index=False)
        print(f"Sentiment analysis saved to {output_file}")
    except Exception as e:
        print(f"Error saving the sentiment results CSV file: {e}")

if __name__ == '__main__':
    perform_analysis()
