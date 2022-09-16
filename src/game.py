from dataclasses import dataclass
from shoe import Shoe
from hand import Hand
from player import Player
from .game_var import Card, Action, HandType


@dataclass
class Game:
    """Game."""
    dealer: Hand
    dealer_shown: Card
    players: list
    
    def __init__(self) -> None:
        pass

    def play_round(self) -> None:
        pass

    def deal(self) -> None:
        pass

    def evaluate(self) -> None:
        pass

    def __str__(self) -> str:
        pass
