from card import Card
from random import randint

class Deck:
    def __init__(self):
        cards = []
        for value in range(1, 14):
            for suit in range(4):
                new_card = Card(value, suit)
                cards.append(new_card)

        self._cards = cards

    def length(self):
        return len(self._cards)

    def shuffle(self):
        source = self._cards.copy()
        destination = []
        while len(source) > 0:
            l = randint(0, len(source) - 1)
            card = source[l]
            destination.append(card)
            source.remove(card)

        self._cards = destination
