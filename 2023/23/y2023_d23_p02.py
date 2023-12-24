import fileinput as fi
import re
import itertools as it
import functools as ft
import string
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
Y,X = gsz

START = (0,0)
STARTX = 0
END = (Y,0)
for x in range(X):
    if grid[0][x] == ".":
        STARTX = x
        START = (0, x)
    if grid[Y-1][x] == ".":
        END = (Y-1,x)

ans = 0

# Let's find all intersections
intersections = set([START, END])
for y in range(1,Y-1):
    for x in range(1,X-1):
        if grid[y][x] == "#":
            continue

        good = 0
        good += grid[y-1][x] != "#"
        good += grid[y+1][x] != "#"
        good += grid[y][x-1] != "#"
        good += grid[y][x+1] != "#"

        if 3 <= good:
            intersections.add((y,x))

print(intersections)

G = {}
for ST in intersections:
    G[ST] = {}
    seen = set()
    Q = cs.deque([(ST,0)])
    while Q:
        (cy, cx), steps = Q.popleft()
        if (cy,cx) in seen:
            continue
        else:
            seen.add((cy,cx))

        if (cy,cx) != ST and (cy,cx) in intersections:
            if (cy,cx) in G[ST]:
                print("WTF")

            G[ST][(cy,cx)] = steps
            continue
    
        # print(gv)
        west = (cy, cx-1)
        if 0 < cx and grid[cy][cx-1] != "#":
            Q.append((west, steps+1))

        east = (cy, cx+1)
        if cx < X-1 and grid[cy][cx+1] != "#":
            Q.append((east, steps+1))

        north = (cy-1, cx)
        if 0 < cy and grid[cy-1][cx] != "#":
            Q.append((north, steps+1))

        south = (cy+1, cx)
        if cy < Y-1 and  grid[cy+1][cx] != "#":
            Q.append((south, steps+1))

print(G)


Q = [(START, frozenset(), 0)]
while Q:
    (cy,cx), prev, steps = Q.pop()
    if (cy,cx) == END:
        if ans < steps:
            ans = steps
            print("New best: ", ans)

        continue

    gv = prev | frozenset([(cy,cx)])

    for dst, cost in G[(cy,cx)].items():
        if dst not in gv:
            Q.append((dst, gv, steps + cost))

    # print(Q)
# Because we skipped the first step
print(ans)
