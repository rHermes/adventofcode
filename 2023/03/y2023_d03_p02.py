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

nums = []
Y, X = gsz

current_number = 0
has_symbol = set()

wd = cs.defaultdict(list)
for j in range(Y):
    for i in range(X):
        c = grid[j][i]

        # put test here
        if not c.isdigit():
            if current_number != 0 and 0 < len(has_symbol):
                for sy,sx in has_symbol:
                    wd[(sy,sx)].append(current_number)
                # nums.append(current_number)

            current_number = 0
            has_symbol = set()
            continue

        current_number = current_number * 10 + int(c)

        for ty,tx in adj(j, i, gsz):
            tc = grid[ty][tx]
            if (not tc.isdigit()) and tc == "*":
                has_symbol.add((ty,tx))


    # put test here
    if current_number != 0 and has_symbol:
        for sy,sx in has_symbol:
            wd[(sy,sx)].append(current_number)
        # nums.append(current_number)

    current_number = 0
    has_symbol = set()

ans = 0
for (ty,tx), its in wd.items():
    if len(its) != 2:
        continue

    ans += its[0] * its[1]
print(ans)
# print(wd)
