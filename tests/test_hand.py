from collections import defaultdict
import unittest
from src.game_var import Card, HandType
from src.shoe import Shoe
from src.hand import Hand

class TestHand(unittest.TestCase):
    def setUp(self):
        self.shoe = Shoe(8)

    def tearDown(self):
        pass

    def test_all_init_hands(self, default_bet=1.0):
        types = defaultdict(int)
        for first_card in Card:
            for second_card in Card:
                hand = Hand(first_card, second_card, default_bet)
                types[hand.hand_type] += 1

        assert types[HandType.BLACKJACK] == 8
        assert types[HandType.PAIR] == 25
        assert types[HandType.SOFT] == 16
        assert types[HandType.HARD] == 120

if __name__ == '__main__':
    unittest.main()
