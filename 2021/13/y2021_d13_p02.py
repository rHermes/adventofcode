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

def solve():
    dots = frozenset([tuple([int(x) for x in line.split(",")]) for line in groups[0].splitlines()])
    for line in groups[1].splitlines():
        d, w = line.split()[-1].split("=")
        w = int(w)

        newdots = set()
        for x,y in dots:
            if d == 'y':
                nx = x
                if y < w:
                    ny = y
                else:
                    ny = w - (y - w)
            else:
                ny = y
                if x < w:
                    nx = x
                else:
                    nx = w - (x - w)

            
            newdots.add((nx,ny))

        dots = frozenset(newdots)

    return dots

dats = solve()

maxx = max(x for x,y in dats)
maxy = max(y for x,y in dats)

for y in range(0, maxy+1):
    for x in range(0, maxx+1):
        if (x,y) in dats:
            print("█", end="")
        else:
            print(" ", end="")
    print("")
