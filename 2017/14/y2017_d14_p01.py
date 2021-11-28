import fileinput as fi
import re
import itertools as it
import functools as ft
import string
import collections
import math
import sys
import heapq
import operator

# findall, search, parse
# from parse import *
import more_itertools as mit
# import z3
# import numpy as np
# import lark
# import regex
# import intervaltree as itree

# print(sys.getrecursionlimit())
sys.setrecursionlimit(6500)

# Debug logging
DEBUG = True
def gprint(*args, **kwargs):
    if DEBUG: print(*args, **kwargs)

# # Input parsing
# INPUT = "".join(fi.input()).rstrip()
# groups = INPUT.split("\n\n")
# lines = list(INPUT.splitlines())

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

def kn(inp):
    cur = 0
    skip = 0
    anp = [ord(x) for x in inp] + [17, 31, 73, 47, 23]

    ar = list(range(256))
    for i in range(64):
        ar, cur, skip = knot_hash(anp, ar, cur, skip)

    dense_hash = (ft.reduce(operator.xor, g) for g in mit.chunked(ar, 16, strict=True))
    return "".join(map("{:08b}".format, dense_hash))

def solve(inp):
    grid = [kn("{}-{}".format(inp, x)) for x in range(128)]
    ans = 0
    for row in grid:
        ans += sum(x == '1' for x in row)

    return ans


inp = "oundnydw" # real
# inp = "flqrgnkx" # test
print(solve(inp))
