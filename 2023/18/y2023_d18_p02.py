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


ext = 0
places = [(0,0)]
for line in lines:
    y,x = places[-1]
    dir, me, _ = line.split(" ")
    me = int(me)

    _, _, h = line.split(" ")
    h = h[2:-1]
    me = int(h[:5], base=16)
    dir = h[-1]

    ext += me

    if dir == "3":
        places.append((y+me, x))
    elif dir == "1":
        places.append((y-me, x))
    elif dir == "2":
        places.append((y, x-me))
    elif dir == "0":
        places.append((y, x+me))

assert(places[0] == places[-1])
# print(places)
AREA = 0
for (sy,sx), (dy,dx) in it.pairwise(reversed(places[:-1])):
    # print((sx,sy), (dx,dy))
    AREA += (sy+dy)*(sx-dx)

AREA = AREA // 2

inter = AREA - ext//2 + 1
print(inter)
print(inter + ext)

