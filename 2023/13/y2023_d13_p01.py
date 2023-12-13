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


def solve(grp):
    grid = [[c for c in line] for line in group.splitlines()]
    Y, X = (len(grid), len(grid[0]))
    
    # print("")
    # for row in grid:
    #     print("".join(row))

    # We check vertical.
    for y in range(1,Y):
        up = y-1
        down = y

        while 0 <= up and down < Y:
            uprow = grid[up]
            drow = grid[down]

            if uprow != drow:
                break

            # We advance
            up -= 1
            down += 1
        else:
            print("We found a horizontal split at", (y-1) + 1)
            # print(grid[y-1])
            return y * 100
            break

    # We check vertical.
    for x in range(1,X):
        left = x-1
        right = x

        while 0 <= left and right < X:
            lcol = [grid[y][left] for y in range(Y)]
            rcol = [grid[y][right] for y in range(Y)]

            if lcol != rcol:
                break

            # We advance
            left -= 1
            right += 1
        else:
            print("We found a vertical split at", (x-1) + 1)
            return x

            break


    print("found no splits")
    return 0

ans = 0
for group in groups:
    ans += solve(group)
print(ans)
