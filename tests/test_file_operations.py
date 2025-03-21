import unittest
import os
from my_awesome_lib.file_operations import read_file, FileWriter

class TestFileOperations(unittest.TestCase):
    TEST_FILENAME = "test_file.txt"

    def setUp(self):
        #Tworzy plik testowy przed każdym testem.
        with open(self.TEST_FILENAME, "w", encoding="utf-8") as f:
            f.write("Hello, world!")

    def tearDown(self):
        #Usuwa plik testowy po każdym teście.
        if os.path.exists(self.TEST_FILENAME):
            os.remove(self.TEST_FILENAME)

    def test_read_file(self):
        #Sprawdza poprawność odczytu pliku.
        content = read_file(self.TEST_FILENAME)
        self.assertEqual(content, "Hello, world!")

    def test_write_file(self):
        #Sprawdza poprawność zapisu do pliku.
        FileWriter.write_file(self.TEST_FILENAME, "Python is awesome!")
        content = read_file(self.TEST_FILENAME)
        self.assertEqual(content, "Python is awesome!")

if __name__ == "__main__":
    unittest.main()
