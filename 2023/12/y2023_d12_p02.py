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

def valid(s, nums):
    if "?" in s:
        print("We shouldn't be trying to validate this")
        return False

    groups = [len(x) for x in s.split(".") if x]
    return groups == nums

def nways_brute(s, nums):

    # print("NW: ", s, nums)
    unknowns = s.count("?")
    bangs = s.count("#")
    if unknowns == 0:
        return int(valid(s, nums))
    elif sum(nums) < bangs:
        return 0
    elif sum(nums) == bangs:
        return int(valid(s.replace("?", "."), nums))
    elif sum(nums) == unknowns + bangs:
        return int(valid(s.replace("?", "#"), nums))
    elif s.startswith("#" * (nums[0]+1)):
        return 0

    
    valid_ways = 0
    i = s.index("?")
    valid_ways += nways(s[:i] + "#" + s[(i+1):], nums)
    valid_ways += nways(s[:i] + "." + s[(i+1):], nums)

    return valid_ways


def ways_to_work(s, nums):
    pass


G = {}
def nways(s, nums):
    global G
    # We need some new ways to prune the tree.
    groups = [x for x in s.split(".") if x]

    
    
    nams = list(nums)
    # We do some easy work here, removing first and last blocks if it doesn't work
    while groups and nams and "?" not in groups[0]:
        g = groups[0]
        n = nams[0]
        if len(g) == n:
            groups.pop(0)
            nams.pop(0)
        else:
            return 0

    while groups and nams and "#" in groups[0]:
        g = groups[0]
        n = nams[0]
        bangs = g.count("#")

        if len(g) == n:
            groups.pop(0)
            nams.pop(0)
        else:
            break
    

    while groups and nams and "?" not in groups[-1]:
        if len(groups[-1]) == nams[-1]:
            groups.pop()
            nams.pop()
        else:
            return 0

    while groups and nams and "#" in groups[-1]:
        g = groups[-1]
        n = nams[-1]
        bangs = g.count("#")

        if len(g) == n:
            groups.pop()
            nams.pop()
        else:
            break

    if not groups:
        return 1

    if not nams:
        k = ".".join(groups)
        if "#" in k:
            return 0
        else:
            return 1
    
    # if len(groups) == len(nams):
    #     print("We have the same")
    # elif len(groups) < len(nams):
    #     print("We have more numbers than groups")
    # else:
    #     print("We have more groups than numbers")

    nss = ".".join(groups)
    wk = max(nams)
    if "#"*(wk+1) in nss:
        # print("we skipped")
        return 0

    sig = (nss, tuple(nams))
    if sig in G:
        # print("cache hit")
        return G[sig]

    # print(groups, nams)
    # print(nss, nams)
    # print(nss, nams)
    
    gways = nways_brute(nss, nams)

    G[sig] = gways
    return gways

def solve(line):
    print(line)
    s, nu = line.split()
    N = 5
    new_s = "?".join([s] * N)
    new_nu = ",".join([nu] * N)
    nums = tuple(int(x) for x in new_nu.split(","))
    # print(new_s, nums)
    ways = nways(new_s, nums)
    print(ways)
    return ways

    
ans = 0
for line in lines:

    ans += solve(line)

print(ans)

