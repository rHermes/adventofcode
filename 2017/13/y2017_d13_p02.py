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
# import more_itertools as mit
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

scanners = {}
for line in lines:
    a, b = map(int, line.split(": "))
    scanners[a] = b

def fast_solve(S, f):
    ans = 0
    for d in sorted(S.keys()):
        r = S[d]
        # q = r*2
        t = d + f
        p = 0
        p = (t) % ((r-1)*2)
        if p == 0:
            return False
            # ans += r * d
        # print("at sec {} we are at {} and the scanner is at {}".format(t, d, p))
    return True

def solve(S, f):
    for d in sorted(S.keys()):
        r = S[d]
        t = d + f
        p = 0
        on_up = True
        for _ in range(t):
            if on_up:
                p += 1
                if p == r-1:
                    on_up = False
            else:
                p -= 1
                if p == 0:
                    on_up = True

        # x x x
        # 0
        #   1
        #     2
        #   3
        # 4
        # p_fast = (t) % ((r-1)*2)
        # if p != p_fast:
        #     print("Offset: {}, Depth: {}, Radius: {}, Time: {}, S: {}, F: {}".format(f, d, r, t, p, p_fast))
        #     for y in range(t):
        #         print("{}: {}".format(y, (y) % ((r-1)*2)))

        # assert(p == p_fast)

        if p == 0:
            return False
        # print("at sec {} we are at {} and the scanner is at {}".format(t, d, p))
    return True

import tqdm
for f in tqdm.trange(10000000000000000):
# for f in range(10000000000000000):
    # assert(solve(scanners, f) == fast_solve(scanners, f))
    if fast_solve(scanners, f):
        print(f)
        break
    
# print(solve(scanners))
