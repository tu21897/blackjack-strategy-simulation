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

    assert types[HandType.BLACKJACK] == 8, f'Number of {HandType.BLACKJACK} in initial hands invalid, {types[HandType.BLACKJACK]}'
    assert types[HandType.PAIR] == 25, f'Number of {HandType.PAIR} in initial hands invalid, {types[HandType.PAIR]}'
    assert types[HandType.SOFT] == 16, f'Number of {HandType.SOFT} in initial hands invalid, {types[HandType.SOFT]}'
    assert types[HandType.HARD] == 120, f'Number of {HandType.HARD} in initial hands invalid, {types[HandType.HARD]}'

    assert Hand(Card.ACE, Card.TEN, pytest.default_bet, split=True).hand_type == HandType.HARD, f'{HandType.BLACKJACK} after split'
    assert Hand(Card.ACE, Card.JACK, pytest.default_bet, split=True).hand_type == HandType.HARD, f'{HandType.BLACKJACK} after split'
    assert Hand(Card.ACE, Card.QUEEN, pytest.default_bet, split=True).hand_type == HandType.HARD, f'{HandType.BLACKJACK} after split'
    assert Hand(Card.ACE, Card.KING, pytest.default_bet, split=True).hand_type == HandType.HARD, f'{HandType.BLACKJACK} after split'

    print('test_init_hands - passed')

def test_action_error(setup):
    hand = Hand(Card.ACE, Card.ACE, pytest.default_bet)
    for _ in range(9):
        hand.apply_action(Action.HIT, Card.ACE)
    with pytest.raises(AssertionError):
        hand.apply_action(Action.HIT, Card.ACE)

    for card in (Card.TEN, Card.JACK, Card.QUEEN, Card.KING):
        hand = Hand(Card.ACE, card, pytest.default_bet)
        assert hand.hand_type == HandType.BLACKJACK, f'Invalid hand type ({hand.hand_type}) on black jack'
        assert hand.stand, f'Active hand on {HandType.BLACKJACK}'
        with pytest.raises(AssertionError):
            hand.apply_action(Action.HIT, Card.ACE)

    hand = Hand(Card.TEN, Card.TEN, pytest.default_bet)
    hand.apply_action(Action.HIT, Card.TEN)
    assert hand.hand_type == HandType.BUST, f'Invalid hand type ({hand.hand_type}) on bust'
    assert hand.stand, f'Active hand on {HandType.BUST}'
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
            assert not hand.stand, f'{Card.ACE} not minimizing with hand value greater than 21'

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
                assert hand.stand, f'Invalid value of hand.stand on {Action.STAND}'

    for card in Card:
        hand = Hand(card, Card.ACE, pytest.default_bet)
        if hand.hand_type != HandType.BLACKJACK:
            hand.apply_action(Action.STAND)
            assert hand.hand_value == Card.ACE.value[1] + 10 + card.value[1], f'Hand value of soft hand ({hand.hand_value} is not maxed on {Action.STAND})'

    print('test_stand - passed')

def test_bust(setup):
    for card in Card:
        if card != Card.ACE:
            hand = Hand(Card.TEN, Card.TEN, pytest.default_bet)
            hand.apply_action(Action.HIT, card)
            assert hand.hand_type == HandType.BUST, f'Invalid hand type ({hand.hand_type}) on bust'
            assert hand.stand, f'Active hand on {HandType.BUST}'

    hand = Hand(Card.SIX, Card.SIX, pytest.default_bet)
    assert hand.hand_type == HandType.PAIR, f'Invalid hand type ({hand.hand_type}) on pair'
    assert not hand.stand, f'Inactive hand on {HandType.PAIR}'
    hand.apply_action(Action.HIT, Card.SIX)
    assert hand.hand_type == HandType.HARD, f'Invalid hand type ({hand.hand_type}) on pair'
    assert not hand.stand, f'Inactive hand on {HandType.HARD}'
    hand.apply_action(Action.HIT, Card.SIX)
    assert hand.hand_type == HandType.BUST, f'Invalid hand type ({hand.hand_type}) on bust'
    assert hand.stand, f'Active hand on {HandType.BUST}'

    for first_card in Card:
        for second_card in Card:
            hand = Hand(first_card, second_card, pytest.default_bet)
            if hand.stand:
                continue
            while not hand.stand:
                hand.apply_action(Action.HIT, Card.EIGHT)
            assert (hand.hand_value > 21 and hand.hand_type == HandType.BUST) or (hand.hand_value == 21 and hand.hand_type == HandType.HARD), 'Hand type and value mismatch on ending hands'

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
                assert hand.stand, f'Active hand on {Action.DOUBLEDOWN}'
                assert hand.bet_size == pytest.default_bet * 2.0, f'Bet size {hand.bet_size} did not double on {Action.DOUBLEDOWN}'
    
    hand = Hand(Card.SIX, Card.SIX, pytest.default_bet)
    hand.apply_action(Action.HIT, Card.SIX)
    hand.apply_action(Action.DOUBLEDOWN, Card.SIX)
    assert hand.stand, f'Active hand on {Action.DOUBLEDOWN}'
    assert hand.hand_type == HandType.BUST, f'Invalid hand type ({hand.hand_type}) on bust'
    assert hand.bet_size == pytest.default_bet * 2.0, f'Bet size {hand.bet_size} did not double on {Action.DOUBLEDOWN}'

    print('test_doubledown - passed')

def test_bet(setup):
    assert Hand(Card.FIVE, Card.FIVE, -322.0).bet_size == -322.0, 'Bet size mismatch with initial bet size'
    assert Hand(Card.FIVE, Card.FIVE, 322.0).bet_size == 322.0, 'Bet size mismatch with initial bet size'
    assert Hand(Card.FIVE, Card.FIVE, 1.123).bet_size == 1.123, 'Bet size mismatch with initial bet size'

    print('test_bet - passed')
