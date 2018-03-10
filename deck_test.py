import unittest
from deck import Deck
from card import Card

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

    def test_draw(self):
        """
        Test that drawing card removes it from deck
        """
        test_deck = Deck()
        first_length = test_deck.length()
        test_deck.draw_card()
        second_length = test_deck.length()

        self.assertEqual(first_length, second_length + 1)

    def test_draw_card(self):
        """
        Test that draw_card returns a Card instance
        """
        test_deck = Deck()
        test_card = test_deck.draw_card()

        self.assertTrue(isinstance(test_card, Card))


if __name__ == '__main__':
    unittest.main()
