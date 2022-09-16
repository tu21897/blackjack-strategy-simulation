from dataclasses import dataclass
from .hand import Hand
from .game_var import Action

@dataclass
class Player:
    """Player."""
    hands: list
    splitnum: int
    base_bet: int

    def __init__(self, hand, base_bet) -> None:
        pass

    def play(self, dealer_card, hand) -> None:
        pass

    def decision(self, dealer_card, hand) -> Action:
        pass

    def split(self) -> None:
        pass

    def __str__(self) -> str:
        pass

    def is_active(self) -> bool:
        pass
