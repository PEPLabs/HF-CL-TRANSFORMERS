from transformers import pipeline

from src.main.lab import get_percentage_positive_sentences

# This is a simple function that takes a statement 
# from the user and returns a sentiment analysis result
def test_statement():
    statement = input("Enter a statement: ")

    classifier = pipeline("sentiment-analysis")

    result = classifier(statement)

    # Print the result in a nice format
    print(f"The statement '{statement}' is {result[0]['label']} with a confidence score of {result[0]['score']}.")

# This is a simple function that takes a file name from 
# the user and returns a percentage of positive sentences in the file
def test_percentage(): 
    filen = input("Enter a file name: ")
    filen = "resources/" + filen.strip()

    print(f"The percentage of positive sentences in {filen} is {get_percentage_positive_sentences(filen)}.")

if __name__ == "__main__":
    choice = input("Enter 1 to test a statement, 2 to test a file: ")
    if choice == '1':
        test_statement()
    elif choice == '2':
        test_percentage()
    else:
        print("Invalid choice.")
   