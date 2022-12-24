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
    mapp =  groups[0].splitlines()
    path = groups[1]
    
    # print(mapp)
    maxy = len(mapp) + 2
    maxx = max(len(x) for x in mapp) + 2

    board = []
    for _ in range(maxy):
        board.append([" " for _ in range(maxx)])

    for y in range(maxy-2):
        l = mapp[y]
        for x in range(len(l)):
            i = l[x]
            board[y+1][x+1] = i

    for line in board:
        print(line)
    
    start_pos = (1, 0)
    for x in range(maxx):
        if board[1][x] == ".":
            start_pos = (1, x)
            break

    print(start_pos)
    
    left_rot = {"U": "L", "R": "U", "D": "R", "L": "D"}
    right_rot = {"U": "R", "R": "D", "D": "L", "L": "U"}
    delta = {"U": (-1,0), "D": (1,0), "R": (0,1), "L": (0,-1)}
    pos = start_pos
    dir = "R"
    for steps, rot in re.findall(r"([0-9]+)(R|L)?", path):
        steps = int(steps)
        print(steps, rot)
        
        dy, dx = delta[dir]
        for _ in range(steps):
            py, px = pos
            ny, nx = py + dy, px + dx
            next_tile = board[ny][nx]
            if next_tile == " ":
                # we must find the actual next tile
                if dy != 0:
                    # we just go to opposite direction
                    ny = py
                    while board[ny-dy][nx] != " ":
                        ny -= dy
                else:
                    # we just go to opposite direction
                    nx = px
                    while board[ny][nx-dx] != " ":
                        nx -= dx

                next_tile = board[ny][nx]

            if next_tile == "#":
                break
            else:
                pos = (ny, nx)


        
        if rot == "L":
            dir = left_rot[dir]
        elif rot == "R":
            dir = right_rot[dir]

    
    cost = {"R": 0, "D": 1, "L": 2, "U": 3}
    print(pos, dir)
    return 1000 * pos[0] + 4*pos[1] + cost[dir]






print(solve())
