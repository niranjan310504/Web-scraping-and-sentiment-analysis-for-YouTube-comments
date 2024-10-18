# main.py
from extractor import extract_comments
from cleaner import clean_comments
from sentiment_analyzer import perform_analysis
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.widgets import Button

def close_event(event):
    plt.close()

def visualize_overall_sentiment():
    # Load the sentiment results
    df = pd.read_csv('sentiment_results.csv')

    # Overall sentiment distribution
    sentiment_counts = df['Sentiment_Label'].value_counts()

    # Create a figure with two subplots: one for the bar chart and one for the pie chart
    fig, (ax_bar, ax_pie) = plt.subplots(1, 2, figsize=(16, 6))

    # Bar chart for sentiment distribution
    sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, palette='viridis', ax=ax_bar)
    ax_bar.set_title('Sentiment Distribution')
    ax_bar.set_xlabel('Sentiment')
    ax_bar.set_ylabel('Number of Comments')

    # Pie chart for sentiment distribution
    ax_pie.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('viridis'))
    ax_pie.set_title('Sentiment Distribution Pie Chart')

    # Add a close button
    ax_button = plt.axes([0.85, 0.01, 0.1, 0.05])  # Position of the button [left, bottom, width, height]
    btn = Button(ax_button, 'Close Plot')
    btn.on_clicked(close_event)

    plt.tight_layout()
    plt.show()

def main():
    # print("Extracting comments...")
    # extract_comments("https://www.youtube.com/watch?v=stZpNO-ygh8")

    # print("Cleaning comments...")
    # clean_comments()

    # print("Analyzing sentiment...")
    # perform_analysis()

    print("Visualizing overall sentiment...")
    visualize_overall_sentiment()

if __name__ == '__main__':
    main()
