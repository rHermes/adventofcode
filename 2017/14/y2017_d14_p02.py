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


def solve_p2(G, src):
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

def solva(G):
    not_seen = set(G.keys())

    groups = 0
    while len(not_seen) > 0:
        src = list(not_seen)[0]
        not_seen -= solve_p2(G, src)
        groups += 1

    return groups

def solve(inp):
    grid = [kn("{}-{}".format(inp, x)) for x in range(128)]

    G = {}
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == "0":
                continue

            deltas = []
            if 0 < x:
                deltas.append((-1, 0))
            if x < (len(row)-1):
                deltas.append((1, 0))

            if 0 < y:
                deltas.append((0, -1))
            if y < (len(grid)-1):
                deltas.append((0, 1))
        
            neigh = []
            for dx, dy in deltas:
                tx, ty = x + dx, y + dy
                if grid[ty][tx] == "1":
                    neigh.append((tx,ty))

            G[(x,y)] = neigh
                    

    return solva(G) 


inp = "oundnydw" # real
# inp = "flqrgnkx" # test
print(solve(inp))
