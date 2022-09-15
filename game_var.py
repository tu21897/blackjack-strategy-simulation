from enum import Enum, auto

class Action(Enum):
    """Actions."""
    STAND = auto()
    HIT = auto()
    DOUBLEDOWN = auto()
    SPLIT = auto()
    SURRENDER = auto()

class HandType(Enum):
    """Hand types."""
    SOFT = auto()
    HARD = auto()
    BLACKJACK = auto()
    PAIR = auto()
    BUST = auto()

class Card(Enum):
    """Cards."""
    ACE = auto(), 1
    TWO = auto(), 2
    THREE = auto(), 3
    FOUR = auto(), 4
    FIVE = auto(), 5
    SIX = auto(), 6
    SEVEN = auto(), 7
    EIGHT = auto(), 8
    NINE = auto(), 9
    TEN = auto(), 10
    JACK = auto(), 10
    QUEEN = auto(), 10
    KING = auto(), 10
