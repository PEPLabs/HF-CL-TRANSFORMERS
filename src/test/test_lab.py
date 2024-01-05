import unittest

from src.main.lab import return_positive_statement, return_negative_statement
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


if __name__ == '__main__':
    unittest.main()