import unittest

from src.main.lab import return_positive_statement, return_negative_statement, get_percentage_positive_sentences
from src.utilities.sentiment_utility import get_sentiment

class TestSentiment(unittest.TestCase):
    def test_positive_sentiment(self):
        response = get_sentiment(return_positive_statement())
        self.assertEqual(response[0]['label'], 'POSITIVE')
        self.assertGreaterEqual(response[0]['score'], 0.8)
    
    def test_negative_sentiment(self):
        response = get_sentiment(return_negative_statement())
        self.assertEqual(response[0]['label'], 'NEGATIVE')
        self.assertGreaterEqual(response[0]['score'], 0.8)
    
    def test_positive_percentage(self):
        percentage = get_percentage_positive_sentences('resources/review1.txt')
        self.assertGreaterEqual(percentage, 0.5)

    def test_negative_percentage(self):
        percentage = get_percentage_positive_sentences('resources/review2.txt')
        self.assertLessEqual(percentage, 0.5)

    def test_neutral_percentage(self):
        percentage = get_percentage_positive_sentences('resources/review3.txt')
        self.assertGreaterEqual(percentage, 0.3)
        self.assertLessEqual(percentage, 0.7)



if __name__ == '__main__':
    unittest.main()