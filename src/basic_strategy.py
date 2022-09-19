from dataclasses import dataclass
from .game_var import Action, HandType

@dataclass
class BasicStrategy:
    """BasicStrategy."""
    decision_matrix: dict

    def __init__(self) -> None:
        self.decision_matrix = {
            (HandType.PAIR, 1): {2: Action.SPLIT, 3: Action.SPLIT, 4: Action.SPLIT, 5: Action.SPLIT, 6: Action.SPLIT, 7: Action.SPLIT, 8: Action.SPLIT, 9: Action.SPLIT, 10: Action.SPLIT, 1: Action.SPLIT},
            (HandType.PAIR, 10): {2: Action.STAND, 3: Action.STAND, 4: Action.STAND, 5: Action.STAND, 6: Action.STAND, 7: Action.STAND, 8: Action.STAND, 9: Action.STAND, 10: Action.STAND, 1: Action.STAND},
            (HandType.PAIR, 9):  {2: Action.SPLIT, 3: Action.SPLIT, 4: Action.SPLIT, 5: Action.SPLIT, 6: Action.SPLIT, 7: Action.STAND, 8: Action.SPLIT, 9: Action.SPLIT, 10: Action.STAND, 1: Action.STAND},
            (HandType.PAIR, 8): {2: Action.SPLIT, 3: Action.SPLIT, 4: Action.SPLIT, 5: Action.SPLIT, 6: Action.SPLIT, 7: Action.SPLIT, 8: Action.SPLIT, 9: Action.SPLIT, 10: Action.SPLIT, 1: Action.SPLIT},
            (HandType.PAIR, 7): {2: Action.SPLIT, 3: Action.SPLIT, 4: Action.SPLIT, 5: Action.SPLIT, 6: Action.SPLIT, 7: Action.SPLIT, 8: Action.HIT, 9: Action.HIT, 10: Action.HIT, 1: Action.HIT},
            (HandType.PAIR, 6): {2: Action.SPLIT, 3: Action.SPLIT, 4: Action.SPLIT, 5: Action.SPLIT, 6: Action.SPLIT, 7: Action.HIT, 8: Action.HIT, 9: Action.HIT, 10: Action.HIT, 1: Action.HIT},
            (HandType.PAIR, 5): {2: Action.DOUBLEDOWN, 3: Action.DOUBLEDOWN, 4: Action.DOUBLEDOWN, 5: Action.DOUBLEDOWN, 6: Action.DOUBLEDOWN, 7: Action.DOUBLEDOWN, 8: Action.DOUBLEDOWN, 9: Action.DOUBLEDOWN, 10: Action.HIT, 1: Action.HIT},
            (HandType.PAIR, 4): {2: Action.HIT, 3: Action.HIT, 4: Action.HIT, 5: Action.SPLIT, 6: Action.SPLIT, 7: Action.HIT, 8: Action.HIT, 9: Action.HIT, 10: Action.HIT, 1: Action.HIT},
            (HandType.PAIR, 3): {2: Action.SPLIT, 3: Action.SPLIT, 4: Action.SPLIT, 5: Action.SPLIT, 6: Action.SPLIT, 7: Action.SPLIT, 8: Action.HIT, 9: Action.HIT, 10: Action.HIT, 1: Action.HIT},
            (HandType.PAIR, 2): {2: Action.SPLIT, 3: Action.SPLIT, 4: Action.SPLIT, 5: Action.SPLIT, 6: Action.SPLIT, 7: Action.SPLIT, 8: Action.HIT, 9: Action.HIT, 10: Action.HIT, 1: Action.HIT},

            (HandType.SOFT, 20): {2: Action.STAND, 3: Action.STAND, 4: Action.STAND, 5: Action.STAND, 6: Action.STAND, 7: Action.STAND, 8: Action.STAND, 9: Action.STAND, 10: Action.STAND, 1: Action.STAND},
            (HandType.SOFT, 19): {2: Action.STAND, 3: Action.STAND, 4: Action.STAND, 5: Action.STAND, 6: Action.STAND, 7: Action.STAND, 8: Action.STAND, 9: Action.STAND, 10: Action.STAND, 1: Action.STAND},
            (HandType.SOFT, 18): {2: Action.STAND, 3: Action.STAND, 4: Action.STAND, 5: Action.STAND, 6: Action.STAND, 7: Action.STAND, 8: Action.STAND, 9: Action.STAND, 10: Action.STAND, 1: Action.STAND},
            (HandType.SOFT, 17): {2: Action.STAND, 3: Action.STAND, 4: Action.STAND, 5: Action.STAND, 6: Action.STAND, 7: Action.STAND, 8: Action.STAND, 9: Action.STAND, 10: Action.STAND, 1: Action.STAND},
            (HandType.SOFT, 16): {2: Action.STAND, 3: Action.STAND, 4: Action.STAND, 5: Action.STAND, 6: Action.STAND, 7: Action.STAND, 8: Action.STAND, 9: Action.STAND, 10: Action.STAND, 1: Action.STAND},
            (HandType.SOFT, 15): {2: Action.STAND, 3: Action.STAND, 4: Action.STAND, 5: Action.STAND, 6: Action.STAND, 7: Action.STAND, 8: Action.STAND, 9: Action.STAND, 10: Action.STAND, 1: Action.STAND},
            (HandType.SOFT, 14): {2: Action.STAND, 3: Action.STAND, 4: Action.STAND, 5: Action.STAND, 6: Action.STAND, 7: Action.STAND, 8: Action.STAND, 9: Action.STAND, 10: Action.STAND, 1: Action.STAND},
            (HandType.SOFT, 13): {2: Action.STAND, 3: Action.STAND, 4: Action.STAND, 5: Action.STAND, 6: Action.STAND, 7: Action.STAND, 8: Action.STAND, 9: Action.STAND, 10: Action.STAND, 1: Action.STAND},
            (HandType.SOFT, 12): {2: Action.STAND, 3: Action.STAND, 4: Action.STAND, 5: Action.STAND, 6: Action.STAND, 7: Action.STAND, 8: Action.STAND, 9: Action.STAND, 10: Action.STAND, 1: Action.STAND},

            (HandType.HARD, 20): {2: Action.STAND, 3: Action.STAND, 4: Action.STAND, 5: Action.STAND, 6: Action.STAND, 7: Action.STAND, 8: Action.STAND, 9: Action.STAND, 10: Action.STAND, 1: Action.STAND},
            (HandType.HARD, 19): {2: Action.STAND, 3: Action.STAND, 4: Action.STAND, 5: Action.STAND, 6: Action.STAND, 7: Action.STAND, 8: Action.STAND, 9: Action.STAND, 10: Action.STAND, 1: Action.STAND},
            (HandType.HARD, 18): {2: Action.STAND, 3: Action.STAND, 4: Action.STAND, 5: Action.STAND, 6: Action.STAND, 7: Action.STAND, 8: Action.STAND, 9: Action.STAND, 10: Action.STAND, 1: Action.STAND},
            (HandType.HARD, 17): {2: Action.STAND, 3: Action.STAND, 4: Action.STAND, 5: Action.STAND, 6: Action.STAND, 7: Action.STAND, 8: Action.STAND, 9: Action.STAND, 10: Action.STAND, 1: Action.STAND},
            (HandType.HARD, 16): {2: Action.STAND, 3: Action.STAND, 4: Action.STAND, 5: Action.STAND, 6: Action.STAND, 7: Action.HIT, 8: Action.HIT, 9: Action.HIT, 10: Action.HIT, 1: Action.HIT},
            (HandType.HARD, 15): {2: Action.STAND, 3: Action.STAND, 4: Action.STAND, 5: Action.STAND, 6: Action.STAND, 7: Action.HIT, 8: Action.HIT, 9: Action.HIT, 10: Action.HIT, 1: Action.HIT},
            (HandType.HARD, 14): {2: Action.STAND, 3: Action.STAND, 4: Action.STAND, 5: Action.STAND, 6: Action.STAND, 7: Action.HIT, 8: Action.HIT, 9: Action.HIT, 10: Action.HIT, 1: Action.HIT},
            (HandType.HARD, 13): {2: Action.STAND, 3: Action.STAND, 4: Action.STAND, 5: Action.STAND, 6: Action.STAND, 7: Action.HIT, 8: Action.HIT, 9: Action.HIT, 10: Action.HIT, 1: Action.HIT},
            (HandType.HARD, 12): {2: Action.HIT, 3: Action.HIT, 4: Action.STAND, 5: Action.STAND, 6: Action.STAND, 7: Action.HIT, 8: Action.HIT, 9: Action.HIT, 10: Action.HIT, 1: Action.HIT},
            (HandType.HARD, 11): {2: Action.DOUBLEDOWN, 3: Action.DOUBLEDOWN, 4: Action.DOUBLEDOWN, 5: Action.DOUBLEDOWN, 6: Action.DOUBLEDOWN, 7: Action.DOUBLEDOWN, 8: Action.DOUBLEDOWN, 9: Action.DOUBLEDOWN, 10: Action.DOUBLEDOWN, 1: Action.DOUBLEDOWN},
            (HandType.HARD, 10): {2: Action.DOUBLEDOWN, 3: Action.DOUBLEDOWN, 4: Action.DOUBLEDOWN, 5: Action.DOUBLEDOWN, 6: Action.DOUBLEDOWN, 7: Action.DOUBLEDOWN, 8: Action.DOUBLEDOWN, 9: Action.DOUBLEDOWN, 10: Action.HIT, 1: Action.HIT},
            (HandType.HARD, 9): {2: Action.STAND, 3: Action.DOUBLEDOWN, 4: Action.DOUBLEDOWN, 5: Action.DOUBLEDOWN, 6: Action.DOUBLEDOWN, 7: Action.STAND, 8: Action.STAND, 9: Action.STAND, 10: Action.STAND, 1: Action.STAND},
            (HandType.HARD, 8): {2: Action.HIT, 3: Action.HIT, 4: Action.HIT, 5: Action.HIT, 6: Action.HIT, 7: Action.HIT, 8: Action.HIT, 9: Action.HIT, 10: Action.HIT, 1: Action.HIT},
            (HandType.HARD, 7): {2: Action.HIT, 3: Action.HIT, 4: Action.HIT, 5: Action.HIT, 6: Action.HIT, 7: Action.HIT, 8: Action.HIT, 9: Action.HIT, 10: Action.HIT, 1: Action.HIT},
            (HandType.HARD, 6): {2: Action.HIT, 3: Action.HIT, 4: Action.HIT, 5: Action.HIT, 6: Action.HIT, 7: Action.HIT, 8: Action.HIT, 9: Action.HIT, 10: Action.HIT, 1: Action.HIT},
            (HandType.HARD, 5): {2: Action.HIT, 3: Action.HIT, 4: Action.HIT, 5: Action.HIT, 6: Action.HIT, 7: Action.HIT, 8: Action.HIT, 9: Action.HIT, 10: Action.HIT, 1: Action.HIT},
            (HandType.HARD, 4): {2: Action.HIT, 3: Action.HIT, 4: Action.HIT, 5: Action.HIT, 6: Action.HIT, 7: Action.HIT, 8: Action.HIT, 9: Action.HIT, 10: Action.HIT, 1: Action.HIT}
        }

    def decision(self, hand_type, hand_value, dealer_value) -> Action:
        return self.decision_matrix[(hand_type,hand_value)][dealer_value]
