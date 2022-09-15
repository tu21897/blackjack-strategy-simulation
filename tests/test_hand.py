from collections import defaultdict
import pytest
from src.game_var import Card, HandType, Action
from src.hand import Hand

@pytest.fixture
def setup():
    pytest.default_bet = 1.0

def test_init_hands(setup):
    types = defaultdict(int)
    for first_card in Card:
        for second_card in Card:
            hand = Hand(first_card, second_card, pytest.default_bet)
            types[hand.hand_type] += 1

    assert types[HandType.BLACKJACK] == 8
    assert types[HandType.PAIR] == 25
    assert types[HandType.SOFT] == 16
    assert types[HandType.HARD] == 120

    print('test_init_hands - passed')

def test_action_error(setup):
    hand = Hand(Card.ACE, Card.ACE, pytest.default_bet)
    for _ in range(9):
        hand.apply_action(Action.HIT, Card.ACE)
    assert hand.stand
    assert hand.hand_type == HandType.HARD
    with pytest.raises(AssertionError):
        hand.apply_action(Action.HIT, Card.ACE)

    for card in (Card.TEN, Card.JACK, Card.QUEEN, Card.KING):
        hand = Hand(Card.ACE, card, pytest.default_bet)
        assert hand.stand
        assert hand.hand_type == HandType.BLACKJACK
        with pytest.raises(AssertionError):
            hand.apply_action(Action.HIT, Card.ACE)

    hand = Hand(Card.TEN, Card.TEN, pytest.default_bet)
    hand.apply_action(Action.HIT, Card.TEN)
    assert hand.stand
    assert hand.hand_type == HandType.BUST
    with pytest.raises(AssertionError):
        hand.apply_action(Action.HIT, Card.TEN)
    with pytest.raises(AssertionError):
        hand.apply_action(Action.DOUBLEDOWN, Card.TEN)
    with pytest.raises(AssertionError):
        hand.apply_action(Action.STAND, Card.TEN)

    print('test_action_error - passed')

def test_hit(setup):
    for card in Card:
        if card != Card.ACE:
            hand = Hand(Card.ACE, Card.ACE, pytest.default_bet)
            for _ in range(8):
                hand.apply_action(Action.HIT, Card.ACE)
            hand.apply_action(Action.HIT, card)
            assert not hand.stand

    for first_card in Card:
        for second_card in Card:
            hand = Hand(first_card, second_card, pytest.default_bet)
            if hand.hand_type != HandType.BLACKJACK:
                hand.apply_action(Action.HIT, Card.SIX)

    print('test_hit - passed')

def test_stand(setup):
    for first_card in Card:
        for second_card in Card:
            hand = Hand(first_card, second_card, pytest.default_bet)
            if hand.hand_type == HandType.BLACKJACK:
                with pytest.raises(AssertionError):
                    hand.apply_action(Action.STAND)
            else:
                hand.apply_action(Action.STAND)
                assert hand.stand

    for card in Card:
        hand = Hand(card, Card.ACE, pytest.default_bet)
        if hand.hand_type != HandType.BLACKJACK:
            hand.apply_action(Action.STAND)
            assert hand.hand_value == Card.ACE.value[1] + 10 + card.value[1]

    print('test_stand - passed')

def test_bust(setup):
    for card in Card:
        if card != Card.ACE:
            hand = Hand(Card.TEN, Card.TEN, pytest.default_bet)
            hand.apply_action(Action.HIT, card)
            assert hand.stand
            assert hand.hand_type == HandType.BUST

    hand = Hand(Card.SIX, Card.SIX, pytest.default_bet)
    assert not hand.stand
    assert hand.hand_type == HandType.PAIR
    hand.apply_action(Action.HIT, Card.SIX)
    assert not hand.stand
    assert hand.hand_type == HandType.HARD
    hand.apply_action(Action.HIT, Card.SIX)
    assert hand.stand
    assert hand.hand_type == HandType.BUST

    for first_card in Card:
        for second_card in Card:
            hand = Hand(first_card, second_card, pytest.default_bet)
            if hand.stand:
                continue
            while not hand.stand:
                hand.apply_action(Action.HIT, Card.EIGHT)
            assert (hand.hand_value > 21 and hand.hand_type == HandType.BUST) or (hand.hand_value == 21 and hand.hand_type == HandType.HARD)

    print('test_bust - passed')

def test_doubledown(setup):
    for first_card in Card:
        for second_card in Card:
            hand = Hand(first_card, second_card, pytest.default_bet)
            if hand.hand_type == HandType.BLACKJACK:
                with pytest.raises(AssertionError):
                    hand.apply_action(Action.DOUBLEDOWN, Card.TWO)
            else:
                hand.apply_action(Action.DOUBLEDOWN, Card.TWO)
                assert hand.stand
                assert hand.bet_size == pytest.default_bet * 2.0
    
    hand = Hand(Card.SIX, Card.SIX, pytest.default_bet)
    assert not hand.stand
    assert hand.hand_type == HandType.PAIR
    assert hand.bet_size == pytest.default_bet
    hand.apply_action(Action.HIT, Card.SIX)
    assert not hand.stand
    assert hand.hand_type == HandType.HARD
    assert hand.bet_size == pytest.default_bet
    hand.apply_action(Action.DOUBLEDOWN, Card.SIX)
    assert hand.stand
    assert hand.hand_type == HandType.BUST
    assert hand.bet_size == pytest.default_bet * 2.0

    print('test_doubledown - passed')
