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

def solve(s):
    depth = 1
    i = 0
    in_garbage = False
    score = 0
    group_starts = []
    groups = []
    accum = []
    while i < len(s):
        if s[i] == '!':
            i += 2
            continue

        if in_garbage:
            if s[i] == '>':
                in_garbage = False

            i += 1
            continue

        if s[i] == '<':
            in_garbage = True
            i += 1
            continue

        if s[i] == '{':
            group_starts.append(i)
            i += 1
            continue

        if s[i] == '}':
            wow = group_starts.pop()
            groups.append(((wow, i), s[wow:i+1], len(group_starts)+1))
            i += 1
            continue

        i += 1

    return groups



for line in lines:
    wo = solve(line)
    # print(wo)
    print(sum(x for _, _, x in wo))

