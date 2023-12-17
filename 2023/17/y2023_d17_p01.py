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
Y, X = gsz

import heapq

prev = {}
cost = cs.defaultdict(lambda: 10000000000000000000000000)
cost[(0,0,0,1,0)] = 0
cost[(0,0,1,0,0)] = 0

Q = [ (0, 0,0,0,1,0), (0, 0,0,1,0,1) ]

heapq.heapify(Q)

taken = set()
ans = 100000000000000000000000000
while Q:
    kst, y, x, dy, dx, steps = heapq.heappop(Q)
    sig = (y, x, dy, dx, steps) 
    if sig in taken:
        continue
    else:
        taken.add(sig)

    if (y,x) == (Y-1,X-1):
        if kst < ans:
            ans = kst
            print(ans)
            break

    # print(kst)
    
    pos = []
    if steps < 2:
        pos.append((y+dy, x+dx, dy,dx, steps+1))

    for ay, ax in [(-1,0), (1,0), (0,-1), (0,1)]:
        # We don't turn completly around
        if ay == -dy or ax == -dx or (ay,ax) == (dy,dx):
            continue

        pos.append((y+ay,x+ax,ay,ax,0))

    for ty, tx, tdy, tdx, tsteps in pos:
        if 0 <= ty < Y and 0 <= tx < X: #  and (ty,tx,dy,dx,steps+1) not in cost:
            wk = cost[sig] + int(grid[ty][tx])
            heapq.heappush(Q, (wk, ty, tx, tdy, tdx, tsteps))

            if wk < cost[(ty,tx,tdy,tdx,tsteps)]:
                cost[(ty,tx,tdy,tdx,tsteps)] = wk
                prev[(ty,tx,tdy,tdx,tsteps)] = sig






# goody = set([(0,0)])
# print(sig)
# cur = sig
# # print(prev)
# print(prev[sig])
# while cur in prev:
#     goody.add((cur[0], cur[1]))
#     cur = prev[cur]
#     # print(cur)

# print(goody)

# for y in range(Y):
#     for x in range(X):
#         if (y,x) in goody:
#             print(".", end="")
#         else:
#             print(grid[y][x], end="")
#     print()
    

# print(cost)
