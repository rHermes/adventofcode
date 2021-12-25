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
grid = [[c for c in line] for line in lines]
gsz = (len(grid), len(grid[0]))


def solve():
    downs = set()
    rights = set()

    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == '>':
                rights.add((y,x))
            if c == 'v':
                downs.add((y,x))


    my, mx = gsz
    for i in range(100000):
        # print("Step {}".format(i))
        # print(downs)
        # print(rights)

        new_downs = set()
        new_rights = set()

        moved = 0
        for y,x in rights:
            dx = (x+1)%mx
            if (y,dx) not in rights and (y,dx) not in downs:
                new_rights.add((y,dx))
                moved += 1
            else:
                new_rights.add((y,x))

        for y,x in downs:
            dy = (y+1)%my
            if (dy,x) not in new_rights and (dy, x) not in downs:
                new_downs.add((dy,x))
                moved += 1
            else:
                new_downs.add((y,x))

        downs = new_downs
        rights = new_rights
        if moved == 0:
            break
        else:
            print(i, moved)

    return i+1





    for line in lines:
        gprint(line)

print(solve())
