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


def cell_power(n, x, y):
    rack_id = x + 10
    
    power = rack_id * y
    power += n
    power *= rack_id

    p = (power // 100) % 10
    return p - 5

def solve(n):
    grid = [[cell_power(n, x+1, y+1) for x in range(300)] for y in range(300)]
    best = -100000
    best_pt = (-1000, -1000)
    for y in range(300-3):
        for x in range(300-3):
            pw = sum(grid[y + dy][x + dx] for (dx, dy) in [(0,0), (1,0), (2,0), (0,1), (1,1), (2,1), (0,2), (1,2), (2,2)])
            # print(x, y, pw)
            if best < pw:
                best = pw
                best_pt = (x+1,y+1)


    return best_pt

assert(cell_power(8, 3, 5) == 4)
# print(solve(18)) # test
print(solve(6303)) # real
