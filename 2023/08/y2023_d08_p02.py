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

nodes = {}
def solve():
    for line in groups[1].splitlines():
        n, b, a = parse("{} = ({}, {})", line)
        nodes[n] = (b, a)
    
    current = "AAA"
    current = [n for n in nodes.keys() if n[-1] == "A"]
    print(current)
    
    wew = []
    # We want to know the intervals of all types.
    for cur in current:
        print("Detecting cycle", cur)
        wit = it.cycle(groups[0].strip())
        to_z = 0

        for c in wit:
            if cur[-1] == "Z":
                break

            if c == "R":
                cur = nodes[cur][1]
            else:
                cur = nodes[cur][0]

            to_z += 1
        
        print("It takes {} steps to get to first z.".format(to_z))
        again_z = 0

        for c in wit:
            if c == "R":
                cur = nodes[cur][1]
            else:
                cur = nodes[cur][0]

            again_z += 1
            
            if cur[-1] == "Z":
                break
    
    
        print("It takes {} steps to get to repeat z.".format(to_z))
        wew.append(to_z)
    
    import math
    return math.lcm(*wew)



print(solve())
