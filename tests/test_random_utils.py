import unittest
from my_awesome_lib.random_utils import shuffle_list  # Upewnij się, że ten import istnieje!

class TestRandomUtils(unittest.TestCase):
    def test_shuffle_list(self):
        # Test mieszania listy.
        items = [1, 2, 3, 4, 5]
        shuffled = shuffle_list(items[:])
        self.assertCountEqual(shuffled, items)  # Sprawdza, czy są te same elementy

if __name__ == "__main__":
    unittest.main()