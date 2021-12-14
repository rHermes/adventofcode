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
grid = [[c for c in line] for line in lines]

rules = {}
for line in groups[1].splitlines():
    a, b = line.split(" -> ")
    rules[a] = b

goal = groups[0]

have = cs.defaultdict(int)
for x,y in mit.pairwise(goal):
    have[x+y] += 1

have = {k: v for k, v in have.items()}

occur = cs.defaultdict(int)
for x in goal:
    occur[x] += 1 

print(have)
print(occur)
for i in range(40):
    new_have = cs.defaultdict(int)
    for key, val in have.items():
        np = rules[key]
        occur[np] += val
        new_have[key[0] + np] += val
        new_have[np + key[1]] += val


    have = {k:v for k, v in new_have.items()}

    print("after step",i,":",occur)

# ans = cs.defaultdict(int)
# for k, v in have.items():
#     ans[k[0]] += v

# ans[goal[0]] += 1
# ans[goal[-1]] += 1

print(occur)
print(max(occur.values())-min(occur.values()))