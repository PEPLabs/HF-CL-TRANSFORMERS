from transformers import pipeline

# This function takes some text and returns a sentiment analysis result
def get_sentiment(text):
    sentiment_classifier = pipeline('sentiment-analysis')
    return sentiment_classifier(text)

# This function takes a file name and returns a list of lines in the file
def get_lines(filen):
    with open(filen, 'r') as f:
        return f.readlines()