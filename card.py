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

    def __str__(self):
        number = self._number
        if number == 1:
            number = 'A'
        elif number == 11:
            number = 'J'
        elif number == 12:
            number = 'Q'
        elif number == 13:
            number = 'K'

        return "Card({0} of {1})".format(str(number), self._suit)

    def __repr__(self):
        return str(self)
