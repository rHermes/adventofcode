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

def snafu_to_int(sn: str) -> int:
    ans = 0
    k = 1
    dix = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
    for c in reversed(sn):
        val = dix[c]
        ans += k*val
        k *= 5

    return ans

import z3
def int_to_snafu(a: int) -> str:
    s = z3.Solver()
    # Try to express through ten
    places = []
    for i in range(1, 100):
        zk = z3.FreshInt("p")
        s.add(-2 <= zk, zk <= 2)
        places.append(zk)

        s.push()

        k = 1
        ww = 0
        for place in places:
            ww += place * k
            k *= 5

        # print(ww)
        s.add(ww == a)

        if s.check() == z3.sat:
            m = s.model()
            wk = "" 
            dix = {2: "2", 1: "1", 0: "0", -1: "-", -2: "="} 
            for place in places:
                ps = m[place].as_long()
                wk = dix[ps] + wk

            return wk
                

        s.pop()
        
    
    return "Its not possible"

        
        

def solve():
    su  = 0
    for line in lines:
        snaf = snafu_to_int(line)
        su += snaf
        print(line, snaf)

    print(su)
    snfo = int_to_snafu(su)
    # print(snafu_to_int(snfo))
    return snfo

print(solve())
