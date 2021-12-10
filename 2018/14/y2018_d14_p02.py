import fileinput as fi
import re
import itertools as it
import functools as ft
import string
import collections
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

# Returns a
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

import tqdm

def solve(n):
    w = [3, 7]
    a = 0
    b = 1

    needle = n

    added = 0
    i = 0
    stack = "37"
    for wow in tqdm.tqdm(it.count()):
    # while True:
        # print(i, w)
        c = w[a] + w[b]
        digits = [int(x) for x in str(c)]
        w.extend(digits)
        stack += str(c)

        ak = stack.find(needle, -len(n))
        if ak > -1:
            # return ak + len(stack) + 10
            return ak


        a = (a + w[a] + 1) % len(w)
        b = (b + w[b] + 1) % len(w)
        i += 1
        added += len(digits)

    return "".join(lop)

   
    


# assert(solve("51589") == 9)
# assert(solve("92510") == 18)
# # print(solve(9))
# print(solve("59414"))
print(solve("652601"))
