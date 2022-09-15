from collections import defaultdict
import unittest
from src.game_var import Card
from src.shoe import Shoe

class TestShoe(unittest.TestCase):
    def setUp(self):
        self.one_deck_shoe = Shoe(1)
        self.eight_deck_shoe = Shoe(8)
        self.base_num_each_card = 4
        self.seen_cards = set()
        self.exp_card_dist = 1.0/13.0

    def tearDown(self):
        self.seen_cards = set()

    def test_init_deck(self):
        one_deck_cards, eight_deck_cards = defaultdict(int), defaultdict(int)
        for card in self.one_deck_shoe.default_deck:
            one_deck_cards[card] += 1
        for card in self.eight_deck_shoe.default_deck:
            eight_deck_cards[card] += 1

        for card in one_deck_cards:
            assert one_deck_cards[card] == self.base_num_each_card, f'Number of card({card}), {one_deck_cards[card]} does not match the expected number, {self.base_num_each_card} (one deck shoe)'
        for card in eight_deck_cards:
            assert eight_deck_cards[card] == self.base_num_each_card * 8, f'Number of card({card}), {eight_deck_cards[card]} does not match the expected number, {self.base_num_each_card * 8} (eight deck shoe)'

        print('test_init_deck - passed')

    def test_valid_cut_depth(self):
        one_cut = self.one_deck_shoe.cut_depth
        eight_cut = self.eight_deck_shoe.cut_depth
        len_one_deck = len(self.eight_deck_shoe.default_deck)
        len_eight_deck = len(self.eight_deck_shoe.default_deck)

        assert 0 <= one_cut < len_one_deck, f'Cut depth({one_cut}) not in the range of the deck(0-{len_one_deck}) (one deck shoe)'
        assert 0 <= eight_cut < len_eight_deck, f'Cut depth({eight_cut}) not in the range of the deck(0-{len_eight_deck}) (eight deck shoe)'

        print('test_valid_cut_depth - passed')

    def test_hit_card_range(self):
        while len(self.seen_cards) != len(Card):
            card = self.one_deck_shoe.hit()
            assert card in Card, f'Card({card}) is not a valid card({Card}) (one deck shoe)'
            self.seen_cards.add(card)
        self.seen_cards = set()

        while len(self.seen_cards) != len(Card):
            card = self.eight_deck_shoe.hit()
            assert card in Card, f'Card({card}) is not a valid card({Card}) (eight deck shoe)'
            self.seen_cards.add(card)

        print('test_hit_card_range - passed')
    
    def test_hit_reshuffle(self):
        for _ in range(len(Card) * self.base_num_each_card):
            self.one_deck_shoe.hit()
            deck_depth = self.one_deck_shoe.num_rem_cards
            assert deck_depth > self.one_deck_shoe.cut_depth, f'Deck at depth({deck_depth}) did not reshuffle at cut depth({self.one_deck_shoe.cut_depth}) (one deck shoe)'
        
        for _ in range(8 * len(Card) * self.base_num_each_card):
            self.eight_deck_shoe.hit()
            deck_depth = self.eight_deck_shoe.num_rem_cards
            assert deck_depth > self.eight_deck_shoe.cut_depth, f'Deck at depth({deck_depth}) did not reshuffle at cut depth({self.eight_deck_shoe.cut_depth}) (eight deck shoe)'

        print('test_hit_reshuffle - passed')
    
    def test_hit_card_dist(self, iterations=1000000, epsilon=1E-3):
        one_deck_card_dist, eight_deck_card_dist = defaultdict(int), defaultdict(int)
        for _ in range(iterations):
            one_deck_card_dist[self.one_deck_shoe.hit()] += 1
            eight_deck_card_dist[self.eight_deck_shoe.hit()] += 1

        for card in Card:
            dist = one_deck_card_dist[card] / iterations
            assert dist > self.exp_card_dist - epsilon and dist < self.exp_card_dist + epsilon, f'Card({card}) dist({dist}) not in bounds of the expected dist({self.exp_card_dist}) with epsilon {epsilon} (one deck shoe)'
            dist = eight_deck_card_dist[card] / iterations
            assert dist > self.exp_card_dist - epsilon and dist < self.exp_card_dist + epsilon, f'Card({card}) dist({dist}) not in bounds of the expected dist({self.exp_card_dist}) with epsilon {epsilon} (eight deck shoe)'

        print('test_hit_card_dist - passed')

if __name__ == '__main__':
    unittest.main()
