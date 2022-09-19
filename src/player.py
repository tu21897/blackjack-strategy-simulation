from dataclasses import dataclass
from .hand import Hand
from .game_var import Action, Card, HandType
from .shoe import Shoe
from .basic_strategy import BasicStrategy

@dataclass
class Player:
    """Player."""
    hands: list
    splitnum: int
    base_bet: int
    shoe: Shoe
    strategy: BasicStrategy

    def __init__(self, hand, base_bet, shoe, strategy) -> None:
        self.hands = []
        self.hands.append(hand)
        self.base_bet = base_bet
        self.splitnum = 0
        self.shoe = shoe
        self.strategy = strategy

    def play(self, dealer_value) -> None:
        active = [self.hands.pop()]
        while active:
            hand = active.pop()
            split = False
            while not hand.stand:
                decision = self.dec(dealer_value, hand)
                if decision == Action.SPLIT:
                    active.extend(self.split(hand))
                    split = True
                    break
                elif decision == Action.STAND:
                    hand.apply_action(decision)
                else:
                    hand.apply_action(decision, self.shoe.hit())
            if split:
                continue
            self.hands.append(hand)

    def dec(self, dealer_value, hand) -> Action:
        h_type = hand.hand_type
        if hand.hand_type == HandType.PAIR:
            if self.splitnum >= 3:
                h_type = HandType.HARD
                h_val = hand.hand_value
            else:
                h_val = hand.hand_value // 2
        else:
            h_val = hand.hand_value
        return self.strategy.decision(h_type, h_val, dealer_value)

    def split(self, hand) -> list:
        self.splitnum += 1
        split_card = Card((hand.hand_value // 2, hand.hand_value // 2))
        return Hand(split_card, self.shoe.hit(), self.base_bet, split=True), Hand(split_card, self.shoe.hit(), self.base_bet, split=True)

    def __str__(self) -> str:
        return f'{self.hands}, {self.splitnum}, {self.base_bet}'
