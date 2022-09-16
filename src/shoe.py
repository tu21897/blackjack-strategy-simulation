from dataclasses import dataclass
from random import random, randint
from .game_var import Card

@dataclass
class Shoe:
    """Shoe."""
    cut_range: tuple
    cut_depth: int
    default_deck: list
    remaining_cards: list
    num_total_cards: int
    num_rem_cards: int

    def __init__(self, num_decks, default_num_each_card=4, cut_start=5/8, cut_end=7/8) -> None:
        num_each_card = num_decks * default_num_each_card
        self.default_deck = []
        for card in Card:
            for _ in range(num_each_card):
                self.default_deck.append(card)

        self.num_total_cards = len(self.default_deck)
        self.cut_range = int(self.num_total_cards * cut_start), int(self.num_total_cards * cut_end)
        self.shuffle_deck()

    def hit(self) -> Card:
        card = self.remaining_cards.pop(int(self.num_rem_cards * random()))
        self.num_rem_cards -= 1
        if self.num_rem_cards <= self.cut_depth:
            self.shuffle_deck()

        return card

    def shuffle_deck(self) -> None:
        self.num_rem_cards = self.num_total_cards
        self.cut_depth = randint(self.cut_range[0], self.cut_range[1])
        self.remaining_cards = self.default_deck.copy()
