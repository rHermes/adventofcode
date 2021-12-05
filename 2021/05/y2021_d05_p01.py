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

def solve(lines):
    board = collections.defaultdict(int)

    for line in lines:
        numbers = list(map(int, re.findall("[0-9]+", line)))
        x1,y1, x2, y2 = numbers


        

        if x1 == x2:
            for y in range(min(y1,y2), max(y1,y2)+1):
                board[(x1,y)] += 1
        elif y1 == y2:
            for x in range(min(x1,x2), max(x1,x2)+1):
                board[(x,y1)] += 1


    ans = 0
    for v in board.values():
        if v > 1:
            ans += 1

    return ans

print(solve(lines))
