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

# (y,x)
shapes = [
        ((0, 0), (0,1), (0, 2), (0,3)),
        ((0, 1), (1,0), (1,1), (1,2), (2,1)),
        ((0, 0), (0, 1), (0, 2), (1,2), (2,2)),
        ((0, 0), (1, 0), (2, 0), (3, 0)),
        ((0, 0), (0, 1), (1, 0), (1, 1)),
]

def hits(world, shape):
    for (y,x) in shape:
        if x == -1 or x == 7 or (y,x) in world:
            return True

    return False



def solve():
    sequence = it.cycle(lines[0])

    world = set([(0, x) for x in range(0,7)])
    tallest = 0
    for shp, _ in zip(it.cycle(shapes), range(2022)):
        relpos = (tallest+4, 2)
        shp = tuple((y+relpos[0], x+relpos[1]) for y,x in shp)

        for s in sequence:
            if s == '>':
                delta = (0, 1)
            else:
                delta = (0, -1)
                
            pos_new = tuple((y+delta[0], x+delta[1]) for y,x in shp)
            if not hits(world, pos_new):
                shp = pos_new

            # Move down
            pos_new = tuple((y-1, x) for y,x in shp)
            if hits(world, pos_new):
                world.update(shp)
                tallest = max(tallest, max(y for y,_ in shp))
                print(tallest)
                break
            else:
                shp = pos_new

    return tallest

print(solve())
