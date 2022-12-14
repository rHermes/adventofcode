import fileinput as fi
import re
import itertools as it
import functools as ft
import string
import collections as cs
import math
import sys
import heapq
import ast

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
grid = [[c for c in line] for line in lines]
gsz = (len(grid), len(grid[0]))

def compare(l, r):
    ll = isinstance(l, list)
    rr = isinstance(r, list)
    # print("we are comparing: ", l, r)

    if (not ll) and not rr:
        if l < r:
            return -1
        elif r < l:
            return 1
        else:
            return 0

    if ll and not rr:
        r = [r]

    if not ll and rr:
        l = [l]

    for a, b in zip(l, r):
        k = compare(a, b)
        if k != 0:
            return k

    if len(l) < len(r):
        return -1
    elif len(l) > len(r):
        return 1
    else:
        return 0



def solve():
    ans = 0
    lists = [ast.literal_eval(x) for x in lines if x]
    lists.append([[2]])
    lists.append([[6]])
    good = list(sorted(lists, key=ft.cmp_to_key(compare)))

    return (good.index([[2]])+1) * (good.index([[6]]) + 1)




print(solve())
