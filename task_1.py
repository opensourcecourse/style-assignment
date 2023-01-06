# A simple code to build decks.

import numpy as np
import random


class Carddeck:
    '''
    A class for managing a deck of playing cards.
    '''

    def setupDeck(self, includeJokers):
        """Setup the deck, return a list of str for each card. 🃏"""
        suites = ["♣", "♠", "♥", "♦"]
        names = [str(x) for x in list(range(2, 11)) + ['J', 'Q', 'K', 'A']]
        out = []
        for suit in suites:
            for name in names:
                out.append(f"{name} {suit}")
        return out

    def __init__(self, includeJokers=False):
        self.deck = self.setupDeck(includeJokers=includeJokers)

    def shuffle(self):
        random.shuffle(self.deck)

    def draw_(self, num):
        """Draw a number of cards."""
        out = []
        for x in range(num):
            out.append(self.deck.pop(-1))
        return out

    def Put_Back(self, card_list):
        # put cards back into the deck.
        for card in card_list:
            self.deck.append(card)


if __name__ == "__main__":
    # simple tests for deck class
    deck = Carddeck()
    # test drawing cards
    cards = deck.draw_(5)
    for card in cards:
        assert card not in deck.deck
    # test putting the cards back
    deck.Put_Back(cards)
    assert deck.deck[-len(cards):] == cards
    # test shuffling
    deck.shuffle()
    assert deck.deck[-len(cards):] != cards
    # test joker in deck when requested
    deck = Carddeck(includeJokers=True)
    assert "🃏" in deck.deck
