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

def solve(p1,p2):
    # We shift
    p1 -= 1
    p2 -= 1

    s1 = 0
    s2 = 0
    dice = 0

    turn_p1 = True
    rolls = 0
    while s1 < 1000 and s2 < 1000:
        print(rolls, p1, p2, s1, s2)
        a = dice + 1
        dice = (dice + 1) % 100
        b = dice + 1
        dice = (dice + 1) % 100
        c = dice + 1
        dice = (dice + 1) % 100
        rolls += 3

        if turn_p1:
            p1 = (p1 + a + b + c) % 10
            s1 += p1 + 1
        else:
            p2 = (p2 + a + b + c) % 10
            s2 += p2 + 1

        turn_p1 = not turn_p1

    if p1 < p2:
        return s1 * rolls
    else:
        return s2 * rolls



# print("test", solve(4,8)) # test
print(solve(2,8)) # real
