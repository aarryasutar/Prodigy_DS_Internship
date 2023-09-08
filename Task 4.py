import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset (replace 'your_dataset.csv' with the actual dataset file)
data = pd.read_csv('your_dataset.csv')

# Assuming your dataset has a 'text' column with the social media posts
tweets = data['text']

# Download NLTK data (if not already downloaded)
nltk.download('vader_lexicon')

# Initialize the VADER sentiment analyzer
sid = SentimentIntensityAnalyzer()

# Create a function to get sentiment scores
def get_sentiment(text):
    sentiment = sid.polarity_scores(text)
    return sentiment['compound']  # Compound score represents overall sentiment

# Apply sentiment analysis to each tweet and store the results in a new column
data['sentiment_score'] = data['text'].apply(get_sentiment)

# Plot the sentiment distribution
sns.histplot(data['sentiment_score'], bins=30, kde=True)
plt.xlabel('Sentiment Score')
plt.ylabel('Frequency')
plt.title('Sentiment Distribution')
plt.show()
# Assuming you have a 'timestamp' column in your dataset
data['timestamp'] = pd.to_datetime(data['timestamp'])

# Group by timestamp and calculate the mean sentiment score per time period (e.g., day)
sentiment_over_time = data.groupby(data['timestamp'].dt.date)['sentiment_score'].mean()

# Plot sentiment trends over time
plt.figure(figsize=(12, 6))
sentiment_over_time.plot()
plt.xlabel('Date')
plt.ylabel('Average Sentiment Score')
plt.title('Sentiment Trends Over Time')
plt.show()

from wordcloud import WordCloud

# Separate positive and negative tweets based on sentiment score
positive_tweets = data[data['sentiment_score'] > 0]['text'].str.cat(sep=' ')
negative_tweets = data[data['sentiment_score'] < 0]['text'].str.cat(sep=' ')

# Create word clouds
positive_wordcloud = WordCloud(width=800, height=400).generate(positive_tweets)
negative_wordcloud = WordCloud(width=800, height=400).generate(negative_tweets)

# Plot word clouds
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(positive_wordcloud, interpolation='bilinear')
plt.title('Positive Sentiment Word Cloud')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(negative_wordcloud, interpolation='bilinear')
plt.title('Negative Sentiment Word Cloud')
plt.axis('off')

plt.show()
