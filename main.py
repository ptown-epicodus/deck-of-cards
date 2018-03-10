from card import Card
from deck import Deck

def main():
    print('Deck of Cards')
    deck = Deck()

    while deck.length() > 0:
        choice = input("Enter s or d to shuffle or draw: ")
        if choice == 's':
            deck.shuffle()
        elif choice == 'd':
            card = deck.draw_card()
            print(card)
        else:
            print('Choose a valid option.')
    print('The deck is empty.')

main()
