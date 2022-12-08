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
grid = [[int(c) for c in line] for line in lines]
gsz = (len(grid), len(grid[0]))

def scene_score_f(ty, tx):
    my, mx = gsz
    h = grid[ty][tx]

    up_score = 0

    # up
    for y in reversed(range(ty)):
        up_score = ty - y
        if h <= grid[y][tx]:
            break
    # down
    down_score = 0
    for y in range(ty+1,my):
        down_score = y - ty
        if h <= grid[y][tx]:
            break

    #left
    left_score = 0
    for x in reversed(range(tx)):
        left_score = tx - x
        if h <= grid[ty][x]:
            break
    # right
    right_score = 0
    for x in range(tx+1,mx):
        right_score = x - tx
        if h <= grid[ty][x]:
            break

    sc =  right_score * left_score * up_score * down_score
    print("Scene score for ({},{}) with h {} is {} ({} * {} * {} * {})".format(tx, ty, h, sc,
                                                                               up_score, left_score, down_score, right_score))

    return sc




def solve():
    my, mx = gsz
    visible = set()

    best_score = 0
    for ty in range(my):
        for tx in range(mx):
            sc = scene_score_f(ty, tx)
            print("Scene score for ({},{}) with h {} is {}".format(tx, ty, grid[ty][tx], sc))
            best_score = max(best_score, sc)

    return best_score
            
            



print(solve())
