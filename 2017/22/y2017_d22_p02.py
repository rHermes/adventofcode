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

CLEAN = 0
WEAK = 1
INFE = 2
FLAG = 3

dirs = "NESW"

dir_delta = {
    "N": (0, -1),
    "E": (1, 0),
    "S": (0, +1),
    "W": (-1, 0)
}

def step(M, c, d):
    pass

def print_map(M):
    min_x = min(x for (x, y), c in M.items() ) #if c)
    max_x = max(x for (x, y), c in M.items() ) #if c)
    min_y = min(y for (x, y), c in M.items() ) #if c)
    max_y = max(y for (x, y), c in M.items() ) #if c)

    for y in range(min_y, max_y+1):
        for x in range(min_x, max_x+1):
            print("{}".format(".#"[M[(x,y)]]), end="")
        print("")


def solve(M, c, d):
    x, y = c
    ans = 0
    for i in range(10000000):
        # print(i)
        # print_map(M)
        # print()
        c = M[(x, y)]
        if c == INFE:
            # print("Turning right from {} to ".format(d), end="")
            d = dirs[(dirs.index(d)+1)%len(dirs)]
            # print("{}.".format(d))
        elif c == WEAK:
            ans += 1
        elif c == FLAG:
            d = dirs[(dirs.index(d)+2)%len(dirs)]
        elif c ==  CLEAN:
            # print("Turning left from {} to ".format(d), end="")
            d = dirs[(dirs.index(d)-1)%len(dirs)]
            # print("{}.".format(d))
        
        M[(x,y)] = (M[(x,y)] + 1) % 4

        # print(d)
        dx, dy = dir_delta[d]
        x, y = x + dx, y + dy
        # print("We are now at ({}, {})".format(x,y))

    # print_map(M)

    return ans


        
M = collections.defaultdict(bool)
for (y, line) in enumerate(lines):
    for (x, c) in enumerate(line):
        if c == '#':
            M[(x,y)] = INFE

x, y = (x+1)//2, (y+1)//2
d = "N"
print(solve(M, (x,y), d))
