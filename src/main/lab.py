from transformers import pipeline
from src.utilities.sentiment_utility import get_sentiment, get_lines

# Here, we set up a pipeline for sentiment analysis 
# (ex: whether the text is positive or negative)
classifier = pipeline("sentiment-analysis")

# We pass in this text and get back a list of dictionaries
result = classifier("I've been waiting for a HuggingFace course my whole life.")

# We print the type of the first element in the list. 
# If we had more sentences, we would see more dictionaries in the list.
print(result[0])

# TODO: Make this function return a statement that will be classified as POSITIVE
def return_positive_statement():
    statement = "I love you!"
    return statement

# TODO: Make this function return a statement that will be classified as NEGATIVE
def return_negative_statement():
    statement = "I hate you!"
    return statement

# TODO: Given a path to a file, this function should return a percentage 
# of positive sentences  in the file. Each sentence will end with a period.
# Hint: Look in the utilities folder for helper functions
def get_percentage_positive_sentences(file_path):
    L = get_lines(file_path)
    results = get_sentiment(L)
    count = 0
    for result in results:
        if result['label'] == 'POSITIVE':
            count += 1
    percentage = count / len(results)
    return percentage
