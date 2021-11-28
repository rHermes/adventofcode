import fileinput as fi
import itertools as it
import functools as ft
import collections
import operator

import more_itertools as mit

def knot_hash(ins, ar, cur, skip):
    for l in ins:
        ar[:l] = ar[:l][::-1]
        bw = collections.deque(ar)
        bw.rotate(-(l + skip))
        cur += l + skip
        ar = list(bw)
        skip += 1

    return ar, cur, skip

def kn(inp):
    cur = 0
    skip = 0
    anp = [ord(x) for x in inp] + [17, 31, 73, 47, 23]

    ar = list(range(256))
    for i in range(64):
        ar, cur, skip = knot_hash(anp, ar, cur, skip)

    bw = collections.deque(ar)
    bw.rotate(cur)
    ar = list(bw)

    dense_hash = (ft.reduce(operator.xor, g) for g in mit.chunked(ar, 16, strict=True))
    return "".join(map("{:08b}".format, dense_hash))

def solve(inp):
    grid = [kn("{}-{}".format(inp, x)) for x in range(128)]
    ans = 0
    for row in grid:
        ans += sum(x == '1' for x in row)

    return ans


print(solve(next(fi.input()).rstrip()))
