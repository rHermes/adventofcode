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

from tqdm import tqdm, trange

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
Y,X = gsz


def north(rocks, stones):
    final_stones = set()
    xs = list(stones)
    xs.sort(reverse=True)
    while xs:
        y,x = xs.pop()

        while 0 < y and (y-1, x) not in final_stones and (y-1, x) not in rocks:
            y -= 1

        final_stones.add((y,x))

    return final_stones

def south(rocks, stones):
    final_stones = set()
    xs = list(stones)
    xs.sort()
    # print(xs)
    while xs:
        y,x = xs.pop()

        while y < Y-1 and (y+1, x) not in final_stones and (y+1, x) not in rocks:
            y += 1

        final_stones.add((y,x))

    return final_stones

def east(rocks, stones):
    final_stones = set()
    xs = [(x, y) for y, x in stones]
    xs.sort()
    # print(xs)
    while xs:
        x,y = xs.pop()

        while x < X-1 and (y, x+1) not in final_stones and (y, x+1) not in rocks:
            x += 1

        final_stones.add((y,x))

    return final_stones

def west(rocks, stones):
    final_stones = set()
    xs = [(x, y) for y, x in stones]
    xs.sort(reverse=True)
    # print(xs)
    while xs:
        x,y = xs.pop()

        while 0 < x and (y, x-1) not in final_stones and (y, x-1) not in rocks:
            x -= 1

        final_stones.add((y,x))

    return final_stones

def print_stones(rocks, stones):
    for y in range(Y):
        for x in range(X):
            # print(y,x)
            p = (y,x)
            if p in stones:
                print("O", end="")
            elif p in rocks:
                print("#", end="")
            else:
                print(".", end="")

        print("")

def hh(stones):
    sig = tuple(sorted(stones))
    sig = hash(sig)
    return sig

G = {}
def cycle(rocks, stones):
    sig = hh(stones)
    if sig in G:
        return G[sig]
   
    # print("=== BEFORE ===")
    # print_stones(rocks, stones)
    stones = north(rocks, stones)
    # print("=== NORTH ===")
    # print_stones(rocks, stones)
    stones = west(rocks, stones)
    # print("=== WEST ===")
    # print_stones(rocks, stones)
    stones = south(rocks, stones)
    # print("=== SOUTH ===")
    # print_stones(rocks, stones)

    stones = east(rocks, stones)
    # print("=== EAST ===")
    # print_stones(rocks, stones)

    G[sig] = stones
    return stones


def solve():
    rocks = set()
    stones = set()
    for y in range(Y):
        for x in range(X):
            c = grid[y][x]
            if c == "O":
                stones.add((y,x))
            if c == "#":
                rocks.add((y,x))
    
    print_stones(rocks, stones)
    print("==")
    seen = {}
    N = 1000000000
    i = 0
    for i in range(N):
        sig = hh(stones)
        if sig in seen:
            # print("WE FOUND A CYCLE")
            # print(i)
            # print(seen[sig])
            break
        else:
            seen[sig] = i

        stones = cycle(rocks, stones)

        # print("After {} cycle:".format(i+1))
        # print_stones(rocks, stones)

    tx = i 
    rest = N - i
    loop_size = i - seen[sig]
    print(loop_size)
    print("Rem:", rest)
    ngood = rest % loop_size
    print(ngood)
    for i in range(ngood):
        # sig = hh(stones)
        # if sig in seen:
        #     # print("WE FOUND A CYCLE")
        #     # print(i)
        #     # print(seen[sig])
        #     break
        # else:
        #     seen[sig] = i
        stones = cycle(rocks, stones)

    # print(i)
    # print(seen)

    # final_stones = north(rocks, stones)
    ans = 0
    for y,x in stones:
        ans += (Y - y)
    return ans
    print(final_stones)

print(solve())
