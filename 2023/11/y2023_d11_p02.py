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
gsz = (len(grid), len(grid[0]))

def solve():
    GV = 1000000 - 1
    # we must expand the grid 
    i = 0

    y_expands=[]
    while i < len(grid):
        if all(c == "." for c in grid[i]):
            y_expands.append(i)

        i += 1
   
    x_expands = []
    i = 0
    while i < len(grid[0]):
        if all(row[i] == "." for row in grid):
            x_expands.append(i)
        i += 1
    
    print(y_expands)
    print(x_expands)
    pos = [] 
    for j in range(len(grid)):
        for i in range(len(grid[0])):
            if grid[j][i] == "#":
                pos.append((j,i))

    print(pos)
    real_pos = []
    for (ty,tx) in pos:
        add_x = 0
        add_y = 0
        for dx in x_expands:
            if dx < tx:
                add_x += GV

        for dy in y_expands:
            if dy < ty:
                add_y += GV
        
        print((ty,tx), add_x, add_y, (ty+add_y, tx+add_x))

        real_pos.append((ty+add_y, tx+add_x))


    ans = 0
    while 0 < len(real_pos):
        (ty,tx) = real_pos.pop()
        for (dy,dx) in real_pos:
            ans += abs(tx-dx) + abs(ty-dy)

    return ans




print(solve())
