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

def adj(z: int, y: int, x: int, shape: positionT) -> abc.Iterator[positionT]:
    """Returns all points around a point, given the shape of the array"""
    sz, sy, sx = shape
    for dz,dy,dx in it.product([-1,0,1], [-1,0,1], [-1,0,1]):
        if dz== 0 and dy == 0 and dx == 0:
            continue
        
        pz = z + dz
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

def adj(z: int, y: int, x: int):
    for dz,dy,dx in it.product([-1,0,1], [-1,0,1], [-1,0,1]):
        if dz== 0 and dy == 0 and dx == 0:
            continue
        
        pz = z + dz
        py = y + dy
        px = x + dx

        yield (pz, py,px)

def solve():
    cubes = set()
    for line in lines:
        x, y, z = map(int,line.split(","))
        cubes.add((z,y,x))

    ans = 0
    for (z ,y ,x) in cubes:
        ans += 6
        ans -= (z+1, y, x) in cubes
        ans -= (z-1, y, x) in cubes
        ans -= (z, y+1, x) in cubes
        ans -= (z, y-1, x) in cubes
        ans -= (z, y, x+1) in cubes
        ans -= (z, y, x-1) in cubes

    return ans

print(solve())