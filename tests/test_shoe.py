from collections import defaultdict
import pytest
from src.game_var import Card
from src.shoe import Shoe

@pytest.fixture
def setup() -> None:
    pytest.one_deck_shoe = Shoe(1)
    pytest.eight_deck_shoe = Shoe(8)
    pytest.base_num_each_card = 4
    pytest.seen_cards = set()
    pytest.exp_card_dist = 1.0/13.0

@pytest.fixture
def teardown() -> None:
    pytest.seen_cards = set()

def test_init_deck(setup) -> None:
    one_deck_cards, eight_deck_cards = defaultdict(int), defaultdict(int)
    for card in pytest.one_deck_shoe.default_deck:
        one_deck_cards[card] += 1
    for card in pytest.eight_deck_shoe.default_deck:
        eight_deck_cards[card] += 1

    for card in one_deck_cards:
        assert one_deck_cards[card] == pytest.base_num_each_card, f'Number of card({card}), {one_deck_cards[card]} does not match the expected number, {pytest.base_num_each_card} (one deck shoe)'
    for card in eight_deck_cards:
        assert eight_deck_cards[card] == pytest.base_num_each_card * 8, f'Number of card({card}), {eight_deck_cards[card]} does not match the expected number, {pytest.base_num_each_card * 8} (eight deck shoe)'

    print('test_init_deck - passed')

def test_valid_cut_depth(setup) -> None:
    one_cut = pytest.one_deck_shoe.cut_depth
    eight_cut = pytest.eight_deck_shoe.cut_depth
    len_one_deck = len(pytest.eight_deck_shoe.default_deck)
    len_eight_deck = len(pytest.eight_deck_shoe.default_deck)

    assert 0 <= one_cut < len_one_deck, f'Cut depth({one_cut}) not in the range of the deck(0-{len_one_deck}) (one deck shoe)'
    assert 0 <= eight_cut < len_eight_deck, f'Cut depth({eight_cut}) not in the range of the deck(0-{len_eight_deck}) (eight deck shoe)'

    print('test_valid_cut_depth - passed')

def test_hit_card_range(setup) -> None:
    while len(pytest.seen_cards) != len(Card):
        card = pytest.one_deck_shoe.hit()
        assert card in Card, f'Card({card}) is not a valid card({Card}) (one deck shoe)'
        pytest.seen_cards.add(card)
    pytest.seen_cards = set()

    while len(pytest.seen_cards) != len(Card):
        card = pytest.eight_deck_shoe.hit()
        assert card in Card, f'Card({card}) is not a valid card({Card}) (eight deck shoe)'
        pytest.seen_cards.add(card)

    print('test_hit_card_range - passed')

def test_hit_reshuffle(setup) -> None:
    for _ in range(len(Card) * pytest.base_num_each_card):
        pytest.one_deck_shoe.hit()
        deck_depth = pytest.one_deck_shoe.num_rem_cards
        assert deck_depth > pytest.one_deck_shoe.cut_depth, f'Deck at depth({deck_depth}) did not reshuffle at cut depth({pytest.one_deck_shoe.cut_depth}) (one deck shoe)'
    
    for _ in range(8 * len(Card) * pytest.base_num_each_card):
        pytest.eight_deck_shoe.hit()
        deck_depth = pytest.eight_deck_shoe.num_rem_cards
        assert deck_depth > pytest.eight_deck_shoe.cut_depth, f'Deck at depth({deck_depth}) did not reshuffle at cut depth({pytest.eight_deck_shoe.cut_depth}) (eight deck shoe)'

    print('test_hit_reshuffle - passed')

def test_hit_card_dist(setup, iterations=1000000, epsilon=1E-3) -> None:
    one_deck_card_dist, eight_deck_card_dist = defaultdict(int), defaultdict(int)
    for _ in range(iterations):
        one_deck_card_dist[pytest.one_deck_shoe.hit()] += 1
        eight_deck_card_dist[pytest.eight_deck_shoe.hit()] += 1

    for card in Card:
        dist = one_deck_card_dist[card] / iterations
        assert dist > pytest.exp_card_dist - epsilon and dist < pytest.exp_card_dist + epsilon, f'Card({card}) dist({dist}) not in bounds of the expected dist({pytest.exp_card_dist}) with epsilon {epsilon} (one deck shoe)'
        dist = eight_deck_card_dist[card] / iterations
        assert dist > pytest.exp_card_dist - epsilon and dist < pytest.exp_card_dist + epsilon, f'Card({card}) dist({dist}) not in bounds of the expected dist({pytest.exp_card_dist}) with epsilon {epsilon} (eight deck shoe)'

    print('test_hit_card_dist - passed')
