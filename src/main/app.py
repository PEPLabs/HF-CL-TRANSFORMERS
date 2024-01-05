from transformers import pipeline


# This is a simple function that takes a statement from the user and returns a sentiment analysis result
if __name__ == "__main__":
    statement = input("Enter a statement: ")

    classifier = pipeline("sentiment-analysis")

    result = classifier(statement)

    # Print the result in a nice format
    print(f"The statement '{statement}' is {result[0]['label']} with a confidence score of {result[0]['score']}.")