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
from parse import *
import more_itertools as mit
import z3
import numpy as np
import lark
import regex
import intervaltree as itree

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

def solve(S):
    ans = 0
    for d in sorted(S.keys()):
        r = S[d]
        t = d
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

        if p == 0:
            ans += r * d
        # print("at sec {} we are at {} and the scanner is at {}".format(t, d, p))
    return ans

print(solve(scanners))
