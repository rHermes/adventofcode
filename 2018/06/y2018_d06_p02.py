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

# Input parsing
INPUT = "".join(fi.input()).rstrip()
groups = INPUT.split("\n\n")
lines = list(INPUT.splitlines())
numbers = [list(map(int, re.findall("[0-9]+", line))) for line in lines]


def get_dims(pts):
    vl = list(pts.keys())
    # WE figure out the dimensions
    min_x = vl[0][0]
    max_x = min_x
    min_y = vl[0][1]
    max_y = min_y

    for x, y in vl[1:]:
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)

    return ((min_x, min_y), (max_x, max_y))

def solve(pts):
    (min_x, min_y), (max_x, max_y) = get_dims(pts)
    offset = 32
    offset = 10000

    ans = 0
    for y in range(min_y-offset, max_y+offset+1):
        for x in range(min_x-offset, max_x+offset+1):
            s = 0
            for px, py in pts.keys():
                s += abs(px - x) + abs(py - y)
                if s >= offset:
                    break
            else:
                ans += 1

    return ans



pts = {tuple(x): str(y) for x, y in zip(numbers, it.count())}
# solve(pts)
print(solve(pts))
