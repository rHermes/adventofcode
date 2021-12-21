import fileinput as fi
import itertools as it
import functools as ft
import collections as cs

DICE_SIDES = 3
NUMBER_OF_DICE = 3
WINNING_SCORE = 21
BOARD_SIZE = 10

def get_combs(dice):
    assert(0 <= dice)

    if dice == 0:
        return cs.Counter({0: 1})
    if dice == 1:
        return cs.Counter({k: 1 for k in range(1, DICE_SIDES+1)})

    c = cs.Counter()
    for forward, count in get_combs(dice-1).items():
        c.update({forward+n: count for n in range(1, DICE_SIDES+1)})

    return c

POSES = list(get_combs(NUMBER_OF_DICE).items())

@ft.cache
def win(p1, p2, s1, s2):
    w1, w2 = 0, 0
    for forward, count in POSES:
        p1_ = (p1 + forward) % BOARD_SIZE
        s1_ = s1 + p1_ + 1
        if s1_ >= WINNING_SCORE:
            ww1, ww2 = 1, 0
        else:
            ww2, ww1 = win(p2, p1_, s2, s1_)

        w1, w2 = w1 + ww1*count, w2 + ww2*count

    return w1, w2


def solve(p1, p2):
    w1, w2 = win(p1-1, p2-1, 0, 0)
    return max(w1, w2)


p1, p2 = [int(line.split()[-1]) for line in fi.input()]
print(solve(p1, p2))
