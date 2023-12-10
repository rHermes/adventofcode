import fileinput as fi
import re
import itertools as it
import functools as ft
import string
import graphlib
import collections as cs
import collections.abc as abc
import math
import sys
import heapq

import typing

# findall, search, parse
from parse import *
import more_itertools as mit
# import z3
# import numpy as np
# import lark
# import regex
# import intervaltree as itree
# from bidict import bidict

# print(sys.getrecursionlimit())
sys.setrecursionlimit(6500)

# Debug logging
DEBUG = True
def gprint(*args, **kwargs):
    if DEBUG: print(*args, **kwargs)

positionT = tuple[int,int]
def ortho(y: int, x: int, shape: positionT) -> abc.Iterator[positionT]:
    """Returns all orthagonaly adjacent points, respecting boundary conditions"""
    sy, sx = shape
    if 0 < x: yield (y, x-1)
    if x < sx-1: yield (y, x+1)
    if 0 < y: yield (y-1, x)
    if y < sy-1: yield (y+1, x)

def adj(y: int, x: int, shape: positionT) -> abc.Iterator[positionT]:
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
pos_numbers = [list(map(int, re.findall("[0-9]+", line))) for line in lines]
grid = [[c for c in line] for line in lines]
gsz = (len(grid), len(grid[0]))

def solve():
    G = cs.defaultdict(set)
    Y, X = gsz
    for y in range(Y):
        for x in range(X):
            c = grid[y][x]
            east = (y,x+1)
            north = (y-1, x)
            west = (y, x-1)
            south = (y+1,x)
            if c == ".":
                continue
            elif c == "F":
                G[(y,x)].update((south, east))
            elif c == "|":
                G[(y,x)].update((north, south))
            elif c == "-":
                G[(y,x)].update((east, west))
            elif c == "L":
                G[(y,x)].update((east, north))
            elif c == "J":
                G[(y,x)].update((west, north))
            elif c == "7":
                G[(y,x)].update((west, south))
            elif c == "S":
                # From my input
                G[(y,x)].update((west, north))
                # examepl
                # G[(y,x)].update((south, east))
                sy, sx = y, x

    
    print(G)

    seen = set()
    cur = cs.deque([(sy,sx,0)])
    maxdepth = 0
    while cur:
        sy, sx, depth = cur.popleft()
        if (sy,sx) in seen:
            continue

        maxdepth = max(depth, maxdepth)

        seen.add((sy,sx))

        for (ty,tx) in G[(sy,sx)]:
            cur.append((ty,tx,depth+1))

    return maxdepth

                



print(solve())
