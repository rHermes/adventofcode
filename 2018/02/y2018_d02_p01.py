import fileinput
import collections


def solve(ids):
    a, b = 0, 0
    for i in ids:
        s = set(collections.Counter(i).values())
        a += 2 in s
        b += 3 in s
    return a * b

ids = [line.rstrip() for line in fileinput.input()]
print(solve(ids))
