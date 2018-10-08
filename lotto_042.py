import sys
import random

NUM_RANGE = range(1, 48)
DRAW_SIZE = 6
NUM_TRIALS = 1000000


def draw():
    def gen_nums(): return set(random.sample(NUM_RANGE, DRAW_SIZE))

    nums = gen_nums()
    while len(nums) < DRAW_SIZE:
        nums = gen_nums()

    return nums


def calc_odds(wins):

    odds = {}

    for k, v in wins.items():
        if v == 0:
            odds[k] = "?"
        else:
            odds[k] = NUM_TRIALS // v

    return odds


def main():
    user_nums = set(int(x) for x in sys.argv[1:])

    wins = {k: 0 for k in range(3, 7)}
    for _ in range(NUM_TRIALS):
        drawn_nums = draw()
        matches = len(user_nums & drawn_nums)
        if matches >= 3:
            wins[matches] += 1

    odds = calc_odds(wins)

    len_max_wins = max([len(str(v)) for v in wins.values()])

    for matches in odds:
        print("Match {}'s : {:>{}} ({} to 1)".format(
            matches, wins[matches], len_max_wins, odds[matches]))


if __name__ == '__main__':
    main()