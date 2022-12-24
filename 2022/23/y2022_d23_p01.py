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

def print_grid(taken, miny=None, maxy=None, minx=None, maxx=None):
    if miny is None:
        miny = min(y for y,x in taken)
    if maxy is None:
        maxy = max(y for y,x in taken)
    if minx is None:
        minx = min(x for y,x in taken)
    if maxx is None:
        maxx = max(x for y,x in taken)

    for y in range(miny,maxy+1):
        for x in range(minx, maxx+1):
            if (y,x) in taken:
                print("#", end="")
            else:
                print(".", end="")
        print("")

    

def solve():
    my, mx = gsz
    taken = set()
    for y in range(my):
        for x in range(mx):
            if grid[y][x] == "#":
                taken.add((y,x))

    dirs = [
        ((-1,0), (-1,1), (-1, -1)),
        ((1,0), (1,1), (1,-1)),
        ((0,-1), (-1, -1), (1, -1)),
        ((0,1), (-1, 1), (1, 1))
    ]
    print(my,mx)

    print("== Initial State ==")
    print_grid(taken, miny=0, maxy=my-1, minx=0, maxx=mx-1)
    
    for iround in range(1,10+1):
        moving = set()

        for ty,tx in taken:
            if (ty, tx) in moving:
                continue

            for dy,dx in it.product([-1,0,1], [-1,0,1]):
                if dy == 0 and dx == 0:
                    continue
                py = ty + dy
                px = tx + dx
                
                if (py,px) in taken:
                    moving.add((py,px))
                    moving.add((ty,tx))
        
        props = cs.defaultdict(set)
        for (ty, tx) in moving:
            for pm, am, bm in dirs:
                if any((ty + dy, tx + dx) in taken for (dy,dx) in (pm, am, bm)):
                    continue

                iy, ix = ty + pm[0], tx + pm[1]
                props[(iy,ix)].add((ty,tx))
                break

        first = dirs.pop(0)
        dirs.append(first)
        # print(dirs)

        # We now try
        for new_pos, origs in props.items():
            if 1 < len(origs):
                continue

            # print(taken)
            oldpos = list(origs)[0]
            # print(oldpos)
            taken.remove(oldpos)
            taken.add(new_pos)

        print("")
        print("== End of Round {} ==".format(iround))
        print_grid(taken, miny=0, maxy=my-1, minx=0, maxx=mx-1)


    miny = min(y for y,x in taken)
    maxy = max(y for y,x in taken)
    minx = min(x for y,x in taken)
    maxx = max(x for y,x in taken)

    total = (maxy-miny+1)*(maxx-minx+1)
    empty = total - len(taken)
    return empty

            


        
                
    

print(solve())
