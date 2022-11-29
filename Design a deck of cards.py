import random

class Card:
    
    def __init__(self, suite, val) -> None:
        self.suite = suite
        self.value = val
    
    def show_card(self) -> None:
        print((self.suite, self.value))


class Deck:

    def __init__(self) -> None:
        self.cards = []

        for suite in ['Club', 'Diamond', 'Heart', 'Spade']:
            for val in range(1, 14):
                self.cards.append(Card(suite, val))

    def show_cards(self) -> None:
        for card in self.cards:
            card.show_card()

    def shuffle_deck(self) -> None:
        print('Shuffling-------------------------')
        random.shuffle(self.cards)
