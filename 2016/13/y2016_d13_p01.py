import fileinput as fi
import re
import itertools as it
import functools as ft
import string
import collections
import math
import sys

# findall, search, parse
# from parse import *
# import more_itertools as mit
# import z3
# import numpy as np
# import lark
# import regex

import heapq

# print(sys.getrecursionlimit())
sys.setrecursionlimit(6500)

# Debug logging
DEBUG = True
def gprint(*args, **kwargs):
    if DEBUG: print(*args, **kwargs)

# # Input parsing
# INPUT = "".join(fi.input()).rstrip()
# groups = INPUT.split("\n\n")
# lines = list(INPUT.splitlines())

def is_open(x, y, c):
    w = x*x + 3*x + 2*x*y + y + y*y
    w += c
    bits = sum(z == "1" for z in bin(w)[2:])
    return bits % 2 == 0

start = (1, 1)
goal = (31, 39)

c = 1362


def pos_moves(pos):
    px, py = pos
    
    pas = [(px+1, py), (px, py+1)]
    if px > 0:
        pas.append((px-1, py))

    if py > 0:
        pas.append((px, py-1))


    return pas




def solve(c, start, stop):
    sx, sy = start
    gx, gy = stop

    Q = [(0, start)]

    seen = set([start])
    while len(Q) > 0:
        depth, (px, py) = heapq.heappop(Q)

        if (px, py) == stop:
            return depth

        for nx, ny in pos_moves((px, py)):
            if (nx, ny) not in seen and is_open(nx, ny, c):
                heapq.heappush(Q, (depth+1, (nx, ny)))
                seen.add((nx, ny))






    
    return -1

# print(solve(10, (1,1), (7,4)))
print(solve(c, start, goal))
# for line in lines:
#     gprint(line)
