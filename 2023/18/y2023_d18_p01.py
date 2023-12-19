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

dug = set([(0,0)])
y,x = 0,0
for line in lines:
    dir, me, _ = line.split(" ")
    me = int(me)
    if dir == "U":
        for _ in range(me):
            y -= 1
            dug.add((y,x))
    elif dir == "D":
        for _ in range(me):
            y += 1
            dug.add((y,x))
    elif dir == "L":
        for _ in range(me):
            x -= 1
            dug.add((y,x))
    elif dir == "R":
        for _ in range(me):
            x += 1
            dug.add((y,x))

print(len(dug))

minx = min(x for _, x in dug)
greds = sorted((y,x) for y, x in dug if x == minx)
# print(greds)
# maxx = max(x for _, x in dug) + 1
# miny = min(y for y, _ in dug) - 1
# maxy = max(y for y, _ in dug) + 1

Q = cs.deque([])
for my,mx in greds:
    if (my,mx+1) not in dug:
        Q.append((my,mx+1))
        break

print(Q)


# my,mx = greds[1]
# my,mx = min(dug, key=lambda p: p[1])
seen = set()
while Q:
    y,x = Q.popleft()
    if (y,x) in seen:
        continue
    else:
        seen.add((y,x))

    
    for ty,tx in [(y-1,x), (y+1, x), (y,x-1), (y,x+1)]:
        if (ty,tx) not in seen and (ty,tx) not in dug:
            Q.appendleft((ty,tx))

print(len(seen))
print(len(seen) + len(dug))

# print(minp)

# ans = 0
# for y in range(miny, maxy+1):
#     inside = False
#     for x in range(minx, maxx+1):
#         p = (y,x)
#         if p in dug:
#             print("#", end="")
#             if not inside:
#                 inside = True
#             else:
#                 ans += 1
#                 inside = False
#         else:
#             if 
#             print(".", end="")

#         ans += inside


#     print("")

# print(ans)

