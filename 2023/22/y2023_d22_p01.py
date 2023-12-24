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

bricks = []
for line in lines:
    # gprint(line)
    fir, sec = line.split("~")
    fir = tuple(reversed([int(x) for x in fir.split(",")]))
    sec = tuple(reversed([int(x) for x in sec.split(",")]))
    diff = sum(a != b for a,b in zip(fir,sec))
    if 1 < diff:
        print(line)
    p = [fir, sec]
    p.sort()
    bricks.append(p)

settled = []
bricks.sort(reverse=True)
seen = {}

startPoints = {}
before = cs.defaultdict(set)
after = cs.defaultdict(set)


brickNum = 1
while bricks:
    fir, sec = bricks.pop()
    startPoints[brickNum] = (fir, sec)
    az, ay, ax = fir
    bz, by, bx = sec



    pics = set()
    for z in range(az, bz+1):
        for y in range(min(ay,by), max(ay,by)+1):
            for x in range(min(ax,bx), max(ax,bx)+1):
                pics.add((z,y,x))

    print(pics)
    
    while True:
        keys = set((z-1, y, x) for z, y, x in pics)

        for z, y, x in keys:
            if z <= 0:
                break
            if (z,y,x) in seen:
                break
        else:
            pics = keys
            continue
        
        break

    
    zl = False
    for z,y,x in pics:
        dz = z - 1
        if dz <= 0:
            zl = True
            break

        if (dz,y,x) in seen:
            before[brickNum].add(seen[(dz,y,x)])
            after[seen[(dz,y,x)]].add(brickNum)

    if zl:
        before[brickNum].add(0)
        after[0].add(brickNum)

    for ks in pics:
        seen[ks] = brickNum

    print(pics)
    print("LEL")

    brickNum += 1

print(seen)
print(before)
print(after)


ans = 0
for cur in range(1,brickNum):
    over = after[cur]
    print(cur,over)
    for o in over:
        if len(before[o]) == 1:
            break
    else:
        print(cur)
        ans += 1


print(ans)


