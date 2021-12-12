import fileinput as fi
import re
import itertools as it
import functools as ft
import string
import collections as cs
import math
import sys
import heapq

# findall, search, parse
from parse import *
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

def ortho(y, x, shape):
    """Returns all orthagonaly adjacent points, respecting boundary conditions"""
    sy, sx = shape
    if 0 < x: yield (y, x-1)
    if x < sx-1: yield (y, x+1)
    if 0 < y: yield (y-1, x)
    if y < sy-1: yield (y+1, x)

def adj(y, x, shape):
    """Returns all points around a point, given the shape of the array"""
    sy, sx = shape
    for dy,dx in it.product([-1,0,1], [-1,0,1]):
        if dy == 0 and dx == 0:
            continue

        py = y + dy
        px = x + dx

        if 0 <= px < sx and 0 <= py < sy:
            yield (py,px)


# Input parsing
INPUT = "".join(fi.input()).rstrip()
groups = INPUT.split("\n\n")
lines = list(INPUT.splitlines())
numbers = [list(map(int, re.findall("-?[0-9]+", line))) for line in lines]
grid = [[c for c in line] for line in lines]


def rek(G, pth, seen):
    pths = set()

    src = pth[-1]
    for w in G[src]:
        if w == "start":
            continue

        if w == "end":
            pths.add(pth + ("end",))
            continue

        if w in seen:
            continue



        nseen = frozenset(seen)
        if w.islower():
            nseen = seen | frozenset((w,))



        pths.update(rek(G, (pth + (w,)), nseen))

    
    return pths




def solve():
    G = cs.defaultdict(set)
    for line in lines:
        a, b = line.split("-")
        G[a].add(b)
        G[b].add(a)

    return rek(G, ("start",), frozenset(["start"]))

print(len(solve()))
