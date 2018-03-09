import unittest
from deck import Deck

class TestDeck(unittest.TestCase):

    def test_init(self):
        """
        Test that deck is successfully created.
        """
        test_deck = Deck()
        self.assertEqual(test_deck.length(), 52)


if __name__ == '__main__':
    unittest.main()
