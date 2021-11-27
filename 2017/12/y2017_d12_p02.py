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

G = {}
for line in lines:
    src, dsts = line.split(" <-> ")
    G[int(src)] = [int(x) for x in dsts.split(", ")]

# print(G)

def solve(G, src):
    Q = collections.deque([src])
    seen = set()

    while len(Q) > 0:
        w = Q.popleft()
        if w in seen:
            continue
        else:
            seen.add(w)

        for x in G[w]:
            Q.append(x)

    return seen

not_seen = set(G.keys())

groups = []
while len(not_seen) > 0:
    src = list(not_seen)[0]
    grp = solve(G, src)
    not_seen -= grp
    groups.append(grp)

print(len(groups))
