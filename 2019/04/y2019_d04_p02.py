import fileinput
from collections import Counter


def solve(lo, hi):
    n = 0
    for x in range(lo, hi+1):
        s = str(x)
        if list(s) == sorted(s) and any(x == 2 for x in Counter(s).values()):
            n += 1
    return n


for line in fileinput.input():
    a, b = [int(x) for x in line.rstrip().split("-")]
    print(solve(a,b))
