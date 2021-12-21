import fileinput as fi
import re
import itertools as it
import functools as ft
import string
import collections as cs
import math
import sys
import heapq
import operator

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
sys.setrecursionlimit(7500)

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

@ft.cache
def win(p1, p2, s1, s2, turn_p1):
    # print("called with:", p1, p2, s1, s2, turn_p1)
    assert(not (s1 >= 21 and s2 >= 21))
    if s1 >= 21:
        return (1, 0)
    if s2 >= 21:
        return (0, 1)

    w1, w2 = 0, 0
    for a in range(3):
        for b in range(3):
            for c in range(3):
                gv = a + b + c + 3
                if turn_p1:
                    pp1 = (p1 + gv) % 10
                    ss1 = s1 + pp1 + 1
                    pp2 = p2
                    ss2 = s2
                else:
                    pp2 = (p2 + gv) % 10
                    ss2 = s2 + pp2 + 1
                    pp1 = p1
                    ss1 = s1

                ww1, ww2 = win(pp1, pp2, ss1, ss2, not turn_p1)
                w1 += ww1
                w2 += ww2
                

    return w1, w2


def solve(p1,p2):
    w1, w2 = win(p1-1, p2-1, 0, 0, True)
    print(w1, w2)
    return max(w1,w2)


# print("test", solve(4,8)) # test
print(solve(2,8)) # real
wk = win.cache_info()
print(f"Hits {wk.hits}, Misses: {wk.misses}, Ratio: {wk.hits/(wk.hits+wk.misses) * 100:0.2f}")
