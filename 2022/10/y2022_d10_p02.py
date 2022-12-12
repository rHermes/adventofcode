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

def draw(cycle, reg, canvas):
    y = (cycle-1) // 40
    x = (cycle-1) % 40

    if reg - 1 <= x <= reg + 1:
        canvas[y][x] = '#'


def solve():
    reg = 1
    ans = 0
    cycle = 1
    above = False
    canvas = [[' ' for _ in range(40)] for _ in range(6)]
    pos = 0
    for line in lines:
        parts = line.split(" ")
        draw(cycle, reg, canvas)

        if parts[0] == "addx":
            cycle += 1
            draw(cycle, reg, canvas)
            reg += int(parts[1])
            cycle += 1
        else:
            cycle += 1

        draw(cycle, reg, canvas)

    strs = ["".join(row) for row in canvas]
    return "\n".join(strs)



print(solve())