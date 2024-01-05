from transformers import pipeline

# Here, we set up a pipeline for sentiment analysis (ex: whether the text is positive or negative)
classifier = pipeline("sentiment-analysis")

# We pass in this text and get back a list of dictionaries
result = classifier("I've been waiting for a HuggingFace course my whole life.")

# We print the type of the first element in the list. If we had more sentences, we would see more dictionaries in the list.
print(result[0])

# TODO: Make this function return a statement that will be classified as POSITIVE
def return_positive_statement():
    statement = ""
    return statement

# TODO: Make this function return a statement that will be classified as NEGATIVE
def return_negative_statement():
    statement = ""
    return statement

