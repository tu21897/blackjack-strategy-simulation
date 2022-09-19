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
    ACE = 1, 1
    TWO = 2, 2
    THREE = 3, 3
    FOUR = 4, 4
    FIVE = 5, 5
    SIX = 6, 6
    SEVEN = 7, 7
    EIGHT = 8, 8
    NINE = 9, 9
    TEN = 10, 10
    JACK = 11, 10
    QUEEN = 12, 10
    KING = 13, 10
