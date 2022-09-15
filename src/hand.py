from dataclasses import dataclass
from .game_var import Card, Action, HandType

@dataclass
class Hand:
    """Hand."""
    hand_type: HandType
    hand_value: int
    bet_size: float
    stand: bool

    def __init__(self, card_one, card_two, bet_size, split=False, max_hand_value=21, ace_add_val=10) -> None:
        self.stand = False
        self.max_hand_value = max_hand_value
        self.ace_add_val = ace_add_val
        self.ace = card_one == Card.ACE or card_two == Card.ACE
        self.hand_value = card_one.value[1] + card_two.value[1] + ace_add_val if self.ace else card_one.value[1] + card_two.value[1]
        self.soft_value = self.hand_value - ace_add_val if self.ace else self.hand_value
        self.bet_size = bet_size
        if self.hand_value == max_hand_value:
            self.stand = True
            if not split:
                self.hand_type = HandType.BLACKJACK
            else:
                self.hand_type = HandType.HARD
        elif card_one.value[1] == card_two.value[1]:
            self.hand_type = HandType.PAIR
        elif self.ace:
            self.hand_type = HandType.SOFT
        else:
            self.hand_type = HandType.HARD

    def __str__(self) -> str:
        return f"{self.hand_value}, {self.hand_type}, {self.bet_size}"

    def apply_action(self, action, card=None) -> None:
        if action == Action.HIT:
            self.soft_value += card.value[1]
            if card == Card.ACE and self.hand_type != HandType.SOFT or self.hand_type == HandType.SOFT:
                self.ace = True
                temp = self.soft_value + self.ace_add_val
                self.hand_value = temp if temp <= self.max_hand_value else self.soft_value
                self.hand_type = HandType.SOFT if temp < self.max_hand_value else HandType.HARD
            else:
                self.hand_value = self.soft_value

            if self.hand_value > self.max_hand_value:
                self.hand_type = HandType.BUST
                self.stand = True
            elif self.hand_value == self.max_hand_value:
                self.hand_type = HandType.HARD
                self.stand = True
        elif action == Action.STAND:
            self.stand = True
        else:
            self.stand = True
            self.bet_size += self.bet_size
            temp = self.hand_value + card.value[1]
            if self.hand_type == HandType.SOFT:
                self.hand_value = temp if temp <= self.max_hand_value else self.soft_value + card.value[1]
            else:
                self.hand_value = temp

            if self.hand_value > self.max_hand_value:
                self.hand_type = HandType.BUST
            else:
                self.hand_type = HandType.HARD
