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
grid = [[int(c) for c in line] for line in lines]

def solve():
    sz = (len(grid)*5, len(grid[0])*5)
    dst = (sz[0]-1, sz[1]-1)
    Q = [(0, 0, 0)]

    seen = set()
    while len(Q) > 0:
        risk, y, x = heapq.heappop(Q)
        print(risk, y, x)
        if (y,x) in seen:
            continue
        else:
            seen.add((y,x))

        if (y,x) == dst:
            return risk

        for ny,nx in ortho(y, x, sz):
            ly = ny // len(grid)
            gy = ny % len(grid)

            lx = nx // len(grid[0])
            gx = nx % len(grid[0])

            val = grid[gy][gx]
            for i in range(lx+ly):
                val += 1
                if val >= 10:
                    val = 1

            heapq.heappush(Q, (val + risk, ny, nx))
        

    return 0

print(solve())
