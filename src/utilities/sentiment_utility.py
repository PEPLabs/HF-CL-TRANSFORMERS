from transformers import pipeline

def get_sentiment(text):
    sentiment_classifier = pipeline('sentiment-analysis')
    return sentiment_classifier(text)