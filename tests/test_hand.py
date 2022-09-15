from collections import defaultdict
import pytest
from src.game_var import Card, HandType, Action
from src.hand import Hand

@pytest.fixture
def setup():
    pass

@pytest.fixture
def teardown():
    pass

def test_init_hands(setup, default_bet=1.0):
    types = defaultdict(int)
    for first_card in Card:
        for second_card in Card:
            hand = Hand(first_card, second_card, default_bet)
            types[hand.hand_type] += 1

    assert types[HandType.BLACKJACK] == 8
    assert types[HandType.PAIR] == 25
    assert types[HandType.SOFT] == 16
    assert types[HandType.HARD] == 120

    print('test_init_hands - passed')

def test_actions(setup, default_bet=1.0):
    hand = Hand(Card.ACE, Card.ACE, default_bet)
    for _ in range(9):
        hand.apply_action(Action.HIT, Card.ACE)

    print('test_actions - passed')

# def test_actions(self, default_bet=1.0):
#     hand = Hand(Card.ACE, Card.ACE, default_bet)
#     hand.apply_action(Action.DOUBLEDOWN, Card.EIGHT)
#     hand.apply_action(Action.STAND, Card.EIGHT)
#     hand.apply_action(Action.HIT, Card.EIGHT)
