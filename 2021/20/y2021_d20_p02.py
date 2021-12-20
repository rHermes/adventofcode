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
# import more_itertools as mit
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
gsz = (len(grid), len(grid[0]))

def solve():
    inar = [x == "#" for x in groups[0].replace("\n", "")]
    grid = cs.defaultdict(bool) # start with black
    for y, row in enumerate(groups[1].splitlines()):
        for x, c in enumerate(row):
            grid[(y,x)] = c == "#"

    # print(grid)
    switching = inar[0]
    cur = False
    for i in range(50):
        if switching:
            cur = not cur
            print("Round {}: {}".format(i, cur))
            if cur:
                new_grid = cs.defaultdict(lambda: True)
            else:
                new_grid = cs.defaultdict(lambda: False)
            
        else:
            new_grid = cs.defaultdict(lambda: False)

        to_consider = set()
        for (y,x), c in grid.items():
            to_consider.add((y,x))
            for dy, dx in it.product([-1,0,1],[-1,0,1]):
                to_consider.add((y+dy, x+dx))

        for (y,x) in to_consider:
            # Read top row:
            snam = "".join(["01"[grid[(y+dy,x+dx)]] for dy, dx in it.product([-1,0,1],[-1,0,1])])
            nam = int(snam, 2)
            new_grid[(y,x)] = inar[nam]

        grid = new_grid



    return sum(grid.values())


print(solve())
