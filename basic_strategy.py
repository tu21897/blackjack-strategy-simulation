from dataclasses import dataclass
from enum import Enum, auto
from game_var import Action, HandType, Card

class HVal(Enum):
    HARD21 = auto()
    HARD20 = auto()
    HARD19 = auto()
    HARD18 = auto()
    HARD17 = auto()
    HARD16 = auto()
    HARD15 = auto()
    HARD14 = auto()
    HARD13 = auto()
    HARD12 = auto()
    HARD11 = auto()
    HARD10 = auto()
    HARD9 = auto()
    HARD8 = auto()
    HARD7 = auto()
    HARD6 = auto()
    HARD5 = auto()
    SOFT21 = auto()
    SOFT20 = auto()
    SOFT19 = auto()
    SOFT18 = auto()
    SOFT17 = auto()
    SOFT16 = auto()
    SOFT15 = auto()
    SOFT14 = auto()
    SOFT13 = auto()
    PAIRA = auto()
    PAIR10 = auto()
    PAIR9 = auto()
    PAIR8 = auto()
    PAIR7 = auto()
    PAIR6 = auto()
    PAIR5 = auto()
    PAIR4 = auto()
    PAIR3 = auto()
    PAIR2 = auto()
    BLACKJACK = auto()

@dataclass
class BasicStrategy:
    hard = {(HVal.HARD21, HandType.HARD, Card.TWO): Action.STAND}
    pass


def main():
    return 1

if __name__ == "__main__":
    main()