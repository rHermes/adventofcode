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
numbers = [list(map(int, re.findall("[0-9]+", line))) for line in lines]

G = collections.defaultdict(set)

for line in reversed(sorted(lines, key=lambda x: x.split(" ")[-3])):
    pr = line.split(" ")
    a, b = pr[1], pr[-3]
    G[b].add(a)
    if a not in G:
        G[a] = set()

# import graphlib

# ts = graphlib.TopologicalSorter(G)
# print("".join(reversed(list(ts.static_order()))))

print(G)
order = []
seen = set()
while len(G) > len(seen):
    cands = []
    for k, v in G.items():
        if k in seen:
            continue
        
        left = v - seen
        if len(left) == 0:
            cands.append(k)

    print(cands)
    do = sorted(cands)[0]
    print(do)

    # order.insert(0, do)
    order.append(do)
    seen.add(do)

# print("".join(reversed(order)))
print("".join(order))
