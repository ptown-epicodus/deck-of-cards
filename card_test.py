import unittest
from card import Card

class TestCard(unittest.TestCase):

    def test_init(self):
        """
        Test that card is successfully created.
        """
        testCard = Card(9, 0)
        self.assertEqual(testCard.number, 9)
        self.assertEqual(testCard.suit, 'Clubs')


if __name__ == '__main__':
    unittest.main()
