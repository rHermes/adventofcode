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

from tqdm import tqdm

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



phases = []
for g in groups[1:]:
    rgs = []
    for x in list(g.splitlines())[1:]:
        tr, sr, lr = map(int, x.split(" "))
        rgs.append((sr, tr, lr))

    phases.append(rgs)


grps_seeds = numbers[0]
seeds = []
num_seeds = 0

# print(num_seeds)

s = z3.Solver()
# s = z3.Optimize()

zans = z3.Int("zans") 

goods = []
for start, l in mit.chunked(grps_seeds, 2):
    goods.append(z3.And(start <= zans, zans <= (start + l)))

s.add(z3.Or(goods))

location = zans
for phase in phases:
    # We are in a phase
    temp = location
    sexpr = temp
    for sr, tr, lr in phase:
        sexpr = z3.If(
            z3.And(sr <= temp, temp <= sr + lr),
            tr + (temp - sr),
            sexpr
        )

    location = sexpr


fl = z3.Int("fl")

s.add(fl == location)
# print(location)
while s.check() == z3.sat:
    # print("wow")
    m = s.model()
    print(m[zans], m[fl])
    s.add(location < m[fl].as_long())

