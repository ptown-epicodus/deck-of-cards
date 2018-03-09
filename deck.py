from card import Card

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
        for i in range(self.length()):
            destination.append(source[i])
        self._cards = destination
