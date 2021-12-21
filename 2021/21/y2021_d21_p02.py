import fileinput as fi
import itertools as it
import functools as ft
import collections as cs

# Calculate the posibilities, sum, number of combs with this sum
POSES = list(cs.Counter(map(sum,it.product(range(1,4),repeat=3))).items())

@ft.cache
def win(p1, p2, s1, s2, turn_p1):
    assert(s1 < 21 and s2 < 21)

    w1, w2 = 0, 0
    for forward, count in POSES:
        if turn_p1:
            pp1 = (p1 + forward) % 10
            ss1 = s1 + pp1 + 1
            if 21 <= ss1:
                ww1, ww2 = 1, 0
            else:
                ww1, ww2 = win(pp1, p2, ss1, s2, False)
        else:
            pp2 = (p2 + forward) % 10
            ss2 = s2 + pp2 + 1
            if 21 <= ss2:
                ww1, ww2 = 0, 1
            else:
                ww1, ww2 = win(p1, pp2, s1, ss2, True)

        w1, w2 = w1 + ww1*count, w2 + ww2*count

    return w1, w2


def solve(p1, p2):
    w1, w2 = win(p1-1, p2-1, 0, 0, True)
    return max(w1, w2)


p1, p2 = [int(line.split()[-1]) for line in fi.input()]

print(solve(p1, p2))
