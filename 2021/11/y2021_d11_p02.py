import fileinput as fi
import re
import itertools as it
import functools as ft
import string
import collections
import math
import sys
import heapq

# findall, search, parse
# from parse import *
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

# Returns a
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

octo = [[int(c) for c in line] for line in lines]

def step(octo):
    noc = [[x + 1 for x in row] for row in octo]
    seen = set()
    while True:
        no_flash = True
        for y in range(10):
            for x in range(10):
                if noc[y][x] > 9 and (y,x) not in seen:
                    no_flash = False
                    seen.add((y,x))
                    for (y,x) in adj(y, x, (10,10)):
                        noc[y][x] += 1
                    
        if no_flash:
            break

    for (y,x) in seen:
        noc[y][x] = 0

    return (noc, len(seen))


noc = octo
for i in it.count(1):
    noc, flashes = step(noc)
    if flashes == 100:
        break
    
print(i)
