import unittest
from deck import Deck

class TestDeck(unittest.TestCase):

    def test_init(self):
        """
        Test that deck is successfully created.
        """
        test_deck = Deck()
        self.assertEqual(test_deck.length(), 52)

    def test_shuffle(self):
        """
        Test that shuffling does not change size of deck
        """
        test_deck = Deck()
        first_length = test_deck.length()
        test_deck.shuffle()
        second_length = test_deck.length()

        self.assertEqual(first_length, second_length)


if __name__ == '__main__':
    unittest.main()
