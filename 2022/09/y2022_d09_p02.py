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
pos_numbers = [list(map(int, re.findall("[0-9]+", line))) for line in lines]
grid = [[c for c in line] for line in lines]
gsz = (len(grid), len(grid[0]))


def step(H, T):
    hy, hx = H
    oty, otx = T
    ty, tx = T

    py, px = (hy - ty, hx - tx)

    if py == 0:
        if px <= -2:
            tx += px + 1
        elif 2 <= px:
            tx += px - 1
    elif px == 0:
        if py == -2:
            ty += -1
        elif py == 2:
            ty += 1
    elif abs(px) < 2 and abs(py) < 2:
        # We do nothing because we are just touching
        pass
    else:
        if 0 < py:
            ty += 1
            if 0 < px:
                tx += 1
            else:
                tx -= 1
        else:
            ty -= 1
            if 0 < px:
                tx += 1
            else:
                tx -= 1

    return (ty-oty, tx-otx)


def solve():
    places = set()
    places.add((0,0))
    dirs = {"D": (-1, 0), "R": (0, 1), "L": (0, -1), "U": (1, 0)}
    KNOTS = [(0,0) for _ in range(10)]
    for line in lines:
        dir, amnt = line.split(" ")
        orig_delta = dirs[dir]
        amnt = int(amnt)
        for _ in range(amnt):
            H = KNOTS[0]
            dy, dx = orig_delta
            H = (H[0] + dy, H[1] + dx)
            KNOTS[0] = H
            for i in range(1,10):
                H, T = KNOTS[i-1], KNOTS[i]
                dy, dx = step(H, T)
                T = (T[0] + dy, T[1] + dx)
                KNOTS[i] = T

            places.add(KNOTS[9])

    # print(places)
    return len(places)


print(solve())
