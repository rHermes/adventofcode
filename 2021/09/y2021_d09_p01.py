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
numbers = [list(map(int, re.findall("-?[0-9]+", line))) for line in lines]

def solve(lines):
    wow = collections.defaultdict(lambda: int(10))
    for y,line in enumerate(lines):
        for x, c in enumerate(line):
            wow[(y,x)] = int(c)

    ans = 0
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if all([wow[(y,x)] < wow[(y+dy,x+dx)] for (dy,dx) in [(0,1), (0,-1), (1, 0), (-1,0)]]):
                ans += wow[(y,x)] + 1
    return ans


print(solve(lines))
