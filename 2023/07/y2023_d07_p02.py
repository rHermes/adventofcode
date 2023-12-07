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


trans = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "T": 10,
        "J": 1,
        "Q": 12,
        "K": 13,
        "A": 14
        }


def solve():
    scores = []
    for line in lines:
        hand, bid = line.split(" ")
        bid = int(bid)
        g = cs.Counter(hand)
        spec = 0
        if "J" in g:
            spec = g["J"]
            del g["J"]
            if g:
                w = g.most_common(1)[0][0]
                g[w] += spec
            else:
                g["A"] = 5


        score = 0

        if len(g.keys()) == 5:
            score = 1
        elif len(g.keys()) == 4:
            score = 2
        elif len(g.keys()) == 3:
            wl = list(g.values())
            wl.sort(reverse=True)
            if wl[0] == 3:
                score = 4
            else:
                score = 3
        elif len(g.keys()) == 2:
            wl = list(g.values())
            wl.sort()
            if wl[0] == 1:
                score = 6
            else:
                score = 5
        else:
            score = 7

        nh = tuple(trans[c] for c in hand)
        scores.append((score, nh, hand, bid))
    
    scores.sort()

    ans = 0
    for i, (score, nh, hand, bid) in enumerate(scores, start=1):
        ans += i * bid
    return ans

    

print(solve())
