SUITS = ('Clubs', 'Spades', 'Hearts', 'Diamonds')

class Card:
    def __init__(self, number, suit):
        self._number = number
        self._suit = SUITS[suit]

    @property
    def number(self):
        return self._number

    @property
    def suit(self):
        return self._suit
