import fileinput as fi
import itertools as it
import collections
import operator
import functools as ft

import more_itertools as mit


def knot_hash(ins, ar, cur, skip):
    bw = collections.deque(ar)
    bw.rotate(-cur)
    ar = list(bw)

    for l in ins:
        ar[:l] = ar[:l][::-1]
        bw = collections.deque(ar)
        bw.rotate(-(l + skip))
        cur += l + skip
        ar = list(bw)
        skip += 1

    bw = collections.deque(ar)
    bw.rotate(cur)
    return list(bw), cur, skip

def solve(inp):
    cur = 0
    skip = 0
    anp = [ord(x) for x in inp] + [17, 31, 73, 47, 23]

    ar = list(range(256))
    for i in range(64):
        ar, cur, skip = knot_hash(anp, ar, cur, skip)

    dense_hash = (ft.reduce(operator.xor, g) for g in mit.chunked(ar, 16, strict=True))
    return "".join(map("{:02x}".format, dense_hash))

print(solve(next(fi.input()).rstrip()))
