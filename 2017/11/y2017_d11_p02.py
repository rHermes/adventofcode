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
# import more_itertools as mit
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



di = {
    "n": 0 -1j,
    "ne": 1 -1j,
    "se": 1 + 0j,
    "s": 0 + 1j,
    "sw": -1 + 1j,
    "nw": -1 + 0j,
}
def axial_subtract(a, b):
    return a - b # Hex(a.q - b.q, a.r - b.r)

def axial_distance(a, b):
    vec = axial_subtract(a, b)
    return (abs(vec.real)
          + abs(vec.real + vec.imag)
          + abs(vec.imag)) / 2

def solve(s):
    steps = s.split(",")
    pt = 0+0j
    max_ans = 0
    for stp in steps:
        pt += di[stp]
        max_ans = max(max_ans, axial_distance(pt, 0 + 0j))
    
    return int(max_ans)



for line in lines:
    print(solve(line))
