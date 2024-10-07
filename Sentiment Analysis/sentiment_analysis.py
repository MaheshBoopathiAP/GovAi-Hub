from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(complaint):
    sentiment_scores = analyzer.polarity_scores(complaint)
    sentiment_score = sentiment_scores['compound']
    sentiment = 'Positive' if sentiment_score > 0 else 'Negative' if sentiment_score < 0 else 'Neutral'
    return sentiment_score, sentiment
