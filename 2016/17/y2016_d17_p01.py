import fileinput as fi
import re
import itertools as it
import functools as ft
import string
import collections
import math
import sys

# findall, search, parse
from parse import *
import more_itertools as mit
import z3
import numpy as np
import lark
import regex

import hashlib
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


import heapq

def solve(s):
    Q = collections.deque()

    Q.append(((0,0), ""))

    seen = set()
    dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    dirsl = "UDLR"
    while len(Q) > 0:
        (px, py), pth = Q.popleft()
        # print((px, py), pth)

        if (px, py) == (3, 3):
            return pth

        if pth in seen:
            continue
        seen.add(pth)


        hsh = hashlib.md5((s + pth).encode("latin1")).hexdigest()[:4]

        for i, x in enumerate(hsh):
            dx, dy = dirs[i]
            if x in "bcdef" and 0 <= px + dx < 4 and 0 <= py + dy < 4:
                Q.append(((px + dx, py + dy), pth + dirsl[i]))



# print(solve("hijkl"))
# print(solve("ihgpwlah"))
print(solve("edjrjqaa"))

