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
    lowpoints = []
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if all([wow[(y,x)] < wow[(y+dy,x+dx)] for (dy,dx) in [(0,1), (0,-1), (1, 0), (-1,0)]]):
                lowpoints.append((y,x))

    basins = {}
    for (y,x) in lowpoints:
        Q = collections.deque([(y,x)])
        seen = set()

        while len(Q) > 0:
            y, x = Q.popleft()
            if (y,x) in seen:
                continue
            else:
                seen.add((y,x))

            for (py,px) in [(y+dy,x+dx) for (dy,dx) in [(0,1), (0,-1), (1, 0), (-1,0)]]:
                if wow[(py,px)] < 9:
                    Q.append((py,px))

        basins[(y,x)] = len(seen)

    wow = sorted(basins.values())
    return wow[-1] * wow[-2] * wow[-3]

print(solve(lines))
