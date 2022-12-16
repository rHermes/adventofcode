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
from bidict import bidict

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

cache = {}
def best(valves, remaining, open: tuple[str], node):
    if remaining == 0:
        return 0

    if (remaining, open, node) in cache:
        return cache[(remaining, open, node)]

    rate, cango = valves[node]

    pos = []
    if not (rate == 0 or node in open):
        pos.append((remaining-1)*rate + best(valves, remaining - 1, open + (node,), node))

    for nnode in cango:
        pos.append(best(valves, remaining - 1, open, nnode))

    cache[(remaining, open, node)] = max(pos)
    return max(pos)









def solve():
    valves = {}
    for line in lines:
        name, rate, _, _, _, leads = parse("Valve {} has flow rate={:d}; {} {} to {} {}", line)
        leads = leads.split(", ")
        valves[name] = (rate, leads)

    return best(valves, 30, (), "AA")



print(solve())
