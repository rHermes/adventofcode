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

def myabs(x):
    return z3.If(x>=0, x,-x)

def solve():
    cannot = set()
    beacons = set()
    s = z3.Solver()
    tx, ty = z3.Ints("tx ty")
    minb = 0
    maxb = 4000000
    s.add(minb <= tx)
    s.add(minb <= ty)
    s.add(tx <= maxb)
    s.add(ty <= maxb)


    for line in lines:
        sx,sy,bx,by = parse("Sensor at x={:d}, y={:d}: closest beacon is at x={:d}, y={:d}", line)
        
        mandist = abs(bx - sx) + abs(by - sy)
        s.add((myabs(tx - sx) + myabs(ty - sy)) > mandist)

    print(s.check())
    m = s.model()
    vx = m[tx].as_long()
    vy = m[ty].as_long()
    return vx * 4000000 + vy
        

print(solve())
