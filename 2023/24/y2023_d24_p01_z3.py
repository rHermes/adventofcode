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
import z3
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

stones = []
for line in lines:
    pre, pos = line.split(" @ ")
    pre = [int(x) for x in pre.split(", ")]
    pos = [int(x) for x in pos.split(", ")]
    stones.append((pre,pos))


def collide(A, B, mini, maxi):
    (ax, ay, az), (avx, avy, avz) = A
    (bx, by, bz), (bvx, bvy, bvz) = B

    so = z3.Solver()
    s = z3.Real("s")
    t = z3.Real("t")

    AX = ax + avx*s
    AY = ay + avy*s

    BX = bx + bvx*t
    BY = by + bvy*t

    so.add(mini <= AX, AX <= maxi)
    so.add(mini <= AY, AY <= maxi)

    so.add(mini <= BX, BX <= maxi)
    so.add(mini <= BY, BY <= maxi)

    so.add(0 <= s)
    so.add(0 <= t)

    so.add(AX == BX, AY == BY)

    if so.check() == z3.sat:
        # print("It can be done")
        return True
    else:
        return False

MINI = 7
MINI = 200000000000000
MAXI = 27
MAXI = 400000000000000
ans = 0
for i in range(len(stones)):
    print(i, len(stones))
    for j in range(i+1, len(stones)):
        a = stones[i]
        b = stones[j]
        
        ans += collide(a, b, MINI, MAXI)

print(ans)
