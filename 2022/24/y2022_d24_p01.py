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


posT = tuple[int,int]
breeze = tuple[int,int,tuple[int,int]]
breezes = frozenset[breeze]

step_cache = {}
def step_bliz(blizs: breezes) -> breezes:
    my, mx = gsz

    if blizs in step_cache:
        return step_cache[blizs]

    nblizs = set()
    for y,x,(dy,dx) in blizs:
        ny, nx = y + dy, x + dx
        if ny == 0:
            nblizs.add((my-2, nx, (dy,dx)))
        elif ny == my-1:
            nblizs.add((1, nx, (dy,dx)))
        elif nx == 0:
            nblizs.add((ny, mx-2, (dy,dx)))
        elif nx == mx-1:
            nblizs.add((ny, 1, (dy,dx)))
        else:
            nblizs.add((ny, nx, (dy,dx)))

    ans =  frozenset(nblizs)
    step_cache[blizs] = ans
    return ans



def best(start_pos: posT, end_pos: posT, start_blizs: breezes):
    my, mx = gsz

    h = lambda p: abs(p[0]-end_pos[0]) + abs(p[1]-end_pos[1])

    # Q = cs.deque([(start_pos, start_blizs, 0)])
    Q = [(h(start_pos) + 0, 0, start_pos, start_blizs)]
    seen = set()
    while Q:
        _, steps, pos, blizs = heapq.heappop(Q)
        if (pos, blizs) in seen:
            continue
            # print("BIG MISTAKE")
            # return -1

        seen.add((pos, blizs))

        nblizs = step_bliz(blizs)
        blizpos = frozenset((y,x) for (y,x,_) in nblizs)
        for dy,dx in [(0,0), (-1,0), (1,0), (0,1), (0,-1)]:
            ny, nx = pos[0] + dy, pos[1] + dx
            if (ny,nx) == end_pos:
                return steps + 1

            if (not (ny,nx) == start_pos) and (ny == 0 or ny == my-1 or nx == 0 or nx == mx-1):
                continue

            if (ny,nx) not in blizpos and ((ny,nx),nblizs) not in seen:
                # Q.append(((ny,nx), nblizs, steps + 1))
                heapq.heappush(Q, (steps + h((ny,nx)), steps + 1, (ny,nx), nblizs))
                # seen.add(((ny,nx), nblizs))
                
    return -1



def solve():
    my, mx = gsz
    start_pos = (0, 0)
    for x,c  in enumerate(grid[0]):
        if c == ".":
            start_pos = (0, x)
            break
    print(start_pos)

    end_pos = (0, 0)
    for x,c in enumerate(grid[-1]):
        if c == ".":
            end_pos = (my-1, x)
            break
    print(end_pos)

    blizs = set()
    for y in range(1,my-1):
        for x in range(1,mx-1):
            c = grid[y][x]
            if c == ">":
                blizs.add((y,x,(0, 1)))
            elif c == "<":
                blizs.add((y,x,(0, -1)))
            elif c == "^":
                blizs.add((y,x,(-1, 0)))
            elif c == "v":
                blizs.add((y,x,(1, 0)))
            elif c== ".":
                continue
            else:
                print("BIG MISTAKE")
                return -1

    # print(blizs)
    return best(start_pos, end_pos, frozenset(blizs))


            


        

print(solve())
