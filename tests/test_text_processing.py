import unittest
from my_awesome_lib.text_processing import reverse_text, is_palindrome

class TestTextProcessing(unittest.TestCase):
    def test_reverse_text(self):
        #Test odwracania tekstu.
        self.assertEqual(reverse_text("abc"), "cba")
        self.assertEqual(reverse_text("Python"), "nohtyP")

    def test_is_palindrome(self):
        #Test sprawdzania palindromów.#
        self.assertTrue(is_palindrome("radar"))
        self.assertTrue(is_palindrome("madam"))
        self.assertFalse(is_palindrome("hello"))

if __name__ == "__main__":
    unittest.main()