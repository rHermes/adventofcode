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
    taken = set()

    start_point = (0, 500)

    for line in lines:
        wks = line.split(" -> ")
        wks = [tuple(reversed(tuple(map(int, x.split(","))))) for x in wks]

        py, px = wks[0]
        for (cy, cx) in wks[1:]:
            if py == cy:
                for x in range(min(px,cx),max(px,cx)+1):
                    taken.add((py, x))
            else:
                for y in range(min(py,cy),max(py,cy)+1):
                    taken.add((y, px))

            py, px = cy, cx

    maxy = max(y for y, _ in taken)

    ans = 0
    while True:
        sy, sx = start_point
        while sy+1 < maxy+2:
            if (sy+1,sx) not in taken:
                sy += 1
            elif (sy+1,sx-1) not in taken:
                sy += 1
                sx -= 1
            elif (sy+1,sx+1) not in taken:
                sy += 1
                sx += 1
            else:
                break
        
        if (sy,sx) == start_point:
            break
        ans += 1
        taken.add((sy,sx))

    return ans + 1


print(solve())
