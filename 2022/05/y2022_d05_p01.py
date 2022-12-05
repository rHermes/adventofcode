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

def solve():
    desc = groups[0].splitlines()
    stacks = []
    for i, c in enumerate(desc[-1]):
        if c not in "123456789":
            continue

        lw = []
        for l in desc[:-1]:
            k = l[i]
            if k not in "[ ]":
                lw.append(k)

        # print(i, c)
        # print(lw)
        stacks.append(lw)

    # print(stacks)
    numbers = [list(map(int, re.findall("[0-9]+", line))) for line in groups[1].splitlines()]
    for (amt, src, dst) in numbers:
        print("BEFORE: ", stacks)
        orig = stacks[src-1]
        our, left = orig[:amt], orig[amt:]
        stacks[src-1] = left
        stacks[dst-1] = list(reversed(our)) + stacks[dst-1]
        print("AFTER: ", stacks)

    return "".join(x[0] for x in stacks)
    

print(solve())
