from card import Card
from deck import Deck

def main():
    print('Deck of Cards')
    deck = Deck()
    deck.shuffle()

    while deck.length() > 0:
        card = deck.draw_card()
        print(card)

main()
