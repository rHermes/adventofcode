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
Y, X= (len(grid), len(grid[0]))


def solve(y, x, dy, dx):
    seen = set()
    dups = set()
    beams = [((y,x,dy,dx))]
    while beams:
        y, x, dy, dx = beams.pop()
        if (y,x,dy,dx) in dups:
            continue
        else:
            dups.add((y,x,dy,dx))

        seen.add((y,x))

        c = grid[y][x]
        if c == ".":
            ty, tx = y + dy, x + dx
            if 0 <= tx < X and 0 <= ty < Y:
                beams.append((ty,tx,dy,dx))
        elif c == "/":
            if dx == 1:
                dy, dx = -1, 0
            elif dx == -1:
                dy, dx = 1, 0
            elif dy == 1:
                dy, dx = 0, -1
            elif dy == -1:
                dy, dx = 0, 1
            else:
                print("BIG PROBLEM")
            ty, tx = y + dy, x + dx
            if 0 <= tx < X and 0 <= ty < Y:
                beams.append((ty,tx,dy,dx))
        elif c == "\\":
            if dx == 1:
                dy, dx = 1, 0
            elif dx == -1:
                dy, dx = -1, 0
            elif dy == 1:
                dy, dx = 0, 1
            elif dy == -1:
                dy, dx = 0, -1
            else:
                print("BIG PROBLEM")

            ty, tx = y + dy, x + dx
            if 0 <= tx < X and 0 <= ty < Y:
                beams.append((ty,tx,dy,dx))
        elif c == "|":
            if dx == 1 or dx == -1:
                dy, dx = 1, 0
                ty, tx = y + dy, x + dx
                if 0 <= tx < X and 0 <= ty < Y:
                    beams.append((ty,tx,dy,dx))

                dy, dx = -1, 0
                ty, tx = y + dy, x + dx
                if 0 <= tx < X and 0 <= ty < Y:
                    beams.append((ty,tx,dy,dx))

            elif dy == 1 or dy == -1:
                ty, tx = y + dy, x + dx
                if 0 <= tx < X and 0 <= ty < Y:
                    beams.append((ty,tx,dy,dx))
            else:
                print("BIG PROBLEM")

        elif c == "-":
            if dy == 1 or dy == -1:
                dy, dx = 0, 1
                ty, tx = y + dy, x + dx
                if 0 <= tx < X and 0 <= ty < Y:
                    beams.append((ty,tx,dy,dx))

                dy, dx = 0, -1
                ty, tx = y + dy, x + dx
                if 0 <= tx < X and 0 <= ty < Y:
                    beams.append((ty,tx,dy,dx))

            elif dx == 1 or dx == -1:
                ty, tx = y + dy, x + dx
                if 0 <= tx < X and 0 <= ty < Y:
                    beams.append((ty,tx,dy,dx))
            else:
                print("BIG PROBLEM")

        else:
            print("We have a problem!")

    return len(seen)

ans = 0
print(solve(0, 3, 1, 0))
for x in range(X):
    ans = max(ans, solve(0, x, 1, 0))
    ans = max(ans, solve(Y-1, x, -1, 0))

for y in range(Y):
    ans = max(ans, solve(y, 0, 0, 1))
    ans = max(ans, solve(y, X-1, 0, -1))

print(ans)
