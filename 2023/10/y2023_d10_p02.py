import fileinput as fi
import re
import itertools as it
import functools as ft
import string
import graphlib
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
    G = cs.defaultdict(set)
    Y, X = gsz
    ground = set()
    realground = set()
    notground = set()

    for y in range(0,2*Y):
        for x in range(0, 2*X):
            ground.add((y,x))

    for y in range(Y):
        for x in range(X):
            c = grid[y][x]
            vy, vx = 2*y, 2*x
            east = (vy,vx+1)
            east2 = (vy,vx+2)

            north = (vy-1, vx)
            north2 = (vy-2, vx)

            west = (vy, vx-1)
            west2 = (vy, vx-2)

            south = (vy+1,vx)
            south2 = (vy+2,vx)
           
            # We add everything around here to ground
            # ground.update(((vy+1,vx+1), (vy+1, vx-1), (vy-1, vx+1), (vy-1, vx-1)))

            realground.add((vy,vx))

            if c == ".":
                pass
                # ground.update(((vy,vx), north, south, east, west))
                # realground.add((vy,vx))
            elif c == "F":
                G[(vy,vx)].update((south2, east2))
                # ground.update((west,north))
                notground.update((south, east))
            elif c == "|":
                G[(vy,vx)].update((north2, south2))
                # ground.update((east,west))
                notground.update((south, north))
            elif c == "-":
                G[(vy,vx)].update((east2, west2))
                # ground.update((north,south))
                notground.update((east, west))
            elif c == "L":
                G[(vy,vx)].update((east2, north2))
                # ground.update((west,south))
                notground.update((east, north))
            elif c == "J":
                G[(vy,vx)].update((west2, north2))
                # ground.update((east,south))
                notground.update((west, north))
            elif c == "7":
                G[(vy,vx)].update((west2, south2))
                # ground.update((east,north))
                notground.update((west, south))
            elif c == "S":
                # From my input
                G[(vy,vx)].update((west2, north2))
                notground.update(((vy,vx), west, north))
                starts = [(vy-1,vx-1)]
                sy,sx = vy, vx
                # starts = [(vy+1,vx-1), (vy+1,vx), (vy+1,vx+1), (vy, vx+1), (vy-1, vx+1)]
                # examepl
                # G[(vy,vx)].update((south2, east2))
                # notground.update(((vy,vx), east, south))
                # For example
                # starts = [(vy+1, vx+1)]
                # starts = [(vy-1, vx)]
                # sy, sx = vy+1, vx+1

                # Example 2
                # G[(vy,vx)].update((west2, south2))
                # notground.update((west, south))
                # starts = [(vy+1,vx-1)]
                # sy, sx = vy,vx


    
    # print(ground)
    # print((sy,sx))

    
    cur = cs.deque([(sy,sx)])
    mainloop = set()
    while cur:
        sy, sx = cur.popleft()
        if (sy,sx) in mainloop:
            continue

        mainloop.add((sy,sx))

        for node in G[(sy,sx)]:
            cur.append(node)

    
    print(mainloop)
    
    ground -= notground
    ground -= mainloop
    realground -= mainloop
    realground -= notground

    # for y in range(Y):
    #     for x in range(X):
    #         c = grid[y][x]
    #         vy, vx = 2*y, 2*x
    #         if (vy,vx) in mainloop:
    #             print(c, end="")
    #         else:
    #             print(" ", end="")

        
    #     print()
    # for y in range(2*Y):
    #     for x in range(2*X):
    #         if (y,x) in realground:
    #             print("X", end="")
    #         elif (y, x) in mainloop:
    #             c = grid[y//2][x//2]
    #             print(c, end="")
    #         elif (y, x) in ground:
    #             print("█", end="")
    #         else:
    #             print(" ", end="")

    #     print("")

    # print("WEW: ", realground)
    seen = set()
    cur = cs.deque(starts)
    maxdepth = 0
    while cur:
        sy, sx = cur.popleft()
        if (sy,sx) in seen or (sy,sx) not in ground:
            continue
        
        seen.add((sy,sx))

        east = (sy,sx+1)
        north = (sy-1, sx)
        west = (sy, sx-1)
        south = (sy+1, sx)

        if east in ground:
            cur.append(east)
        if west in ground:
            cur.append(west)
        if north in ground:
            cur.append(north)
        if south in ground:
            cur.append(south)

    # for y in range(2*Y):
    #     for x in range(2*X):
    #         if (y,x) in seen:
    #             print("X", end="")
    #         # elif (y,x) in ground:
    #         #     print("+", end="")
    #         else:
    #             print(" ", end="")

    #     print("")

    for y in range(Y):
        for x in range(X):
            vy, vx = 2*y, 2*x
            c = grid[y][x]
            if (vy,vx) in mainloop:
                print(c, end="")
            else:
                print(".", end="")
        print("")

    # for y in range(Y):
    #     for x in range(X):
    #         vy, vx = 2*y, 2*x
    #         c = grid[y][x]
    #         if (vy,vx) in (seen & realground):
    #             print("X", end="")
    #         else:
    #             print(" ", end="")
    #     print("")
    # print(seen)
    # print(realground)
    
    # print(seen)
    # good = [(y,x) for (y,x) in seen if y % 2 == 0 and x % 2 == 0]
    # good.sort()
    # print(good)
    # return len(good) 
    # # return len([(y,x) for (y,x) in seen if y % 2 == 0 and x % 2 == 0])
    return len(seen & realground)

                



print(solve())
