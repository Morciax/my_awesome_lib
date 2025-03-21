import unittest
from my_awesome_lib.data_utils import count_words, DataAnalyzer

class TestDataUtils(unittest.TestCase):
    def test_count_words(self):
        #Test liczenia słów w tekście.
        self.assertEqual(count_words("Hello world"), 2)
        self.assertEqual(count_words("Python is great"), 3)
        self.assertEqual(count_words(""), 0)

    def test_unique_words(self):
        #Test liczenia unikalnych słów.
        analyzer = DataAnalyzer("Python Python AI AI AI")
        self.assertEqual(analyzer.unique_words(), 2)

if __name__ == "__main__":
    unittest.main()
