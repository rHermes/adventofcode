import fileinput as fi
import re
import itertools as it
import functools as ft
import string
import collections
import math
import sys
import heapq

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

# Input parsing
INPUT = "".join(fi.input()).rstrip()
groups = INPUT.split("\n\n")
lines = list(INPUT.splitlines())

def strength(bridge):
    return sum(sum(x) for x in bridge)

def solve(comps):
    Q = [(0, 0, frozenset(), 0)]
    al = frozenset(range(len(comps)))

    best_len = 0
    best_ans = 0
    while 0 < len(Q):
        l, score, used, need = heapq.heappop(Q)
        if l < best_len:
            print("WE got a new best ans {} {}".format(l, score))
            best_len = l
            best_ans = score
        elif l == best_len and score < best_ans:
            print("WE got a new best ans {}".format(score))
            best_ans = score

        for i in al - used:
            ca, cb = comps[i]
            if ca == need:
                nneed = cb
            elif cb == need:
                nneed = ca
            else:
                continue

            heapq.heappush(Q, (l - 1, score - (ca + cb), used.union((i,)), nneed))


    return -best_ans

comps = []
for line in lines:
    a, b = map(int,line.split("/"))
    a, b = min(a,b), max(a,b)
    comps.append((a,b))

print(solve(comps))
