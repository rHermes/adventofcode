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


# Input parsing
INPUT = "".join(fi.input()).rstrip()
groups = INPUT.split("\n\n")
lines = list(INPUT.splitlines())
numbers = [list(map(int, re.findall("-?[0-9]+", line))) for line in lines]

def solve(lines):
    ans = 0
    goods = []
    for line in lines:
        xline = line
        nline = line.replace("()","").replace("[]", "").replace("{}", "").replace("<>", "")
        while nline != line:
            line = nline
            nline = line.replace("()","").replace("[]", "").replace("{}", "").replace("<>", "")

        if any(x in line for x in ")]>}"):
            for i in range(len(line)):
                if line[i] in ")]>}":
                    ans += {")": 3, "]": 57, "}": 1197, ">": 25137}[line[i]]
                    break
        else:
            goods.append(line)

    ans = 0
    # print(goods)
    scores = []
    for line in goods:
        score = 0
        for c in reversed(line):
            score *= 5
            score += {"(": 1, "[": 2, "{": 3, "<": 4}[c]

        scores.append(score)
    
    import statistics

    return statistics.median(scores)


print(solve(lines))
