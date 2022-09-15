from time import perf_counter
import shoe as s
import hand as h
import cProfile
import pstats
from game_var import Card, Action, HandType

def main():
    shoe = s.Shoe(8)
    start = perf_counter()
    with cProfile.Profile() as pr:
        for _ in range(10):
            hand = h.Hand(shoe.hit(), shoe.hit(), 1.0)
            while not hand.stand:
                print(hand)
                hand.apply_action(Action.HIT, shoe.hit())
                print(hand, '\n')
            print(8 * '\n')
    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()
    end = perf_counter()
    print(end - start)

if __name__ == "__main__":
    main()