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


def get_dims(parts):
    minx = parts[0][0][0]
    maxx = minx
    miny = parts[0][0][1]
    maxy = miny

    for (x,y), _ in parts[1:]:
        minx = min(x, minx)
        maxx = max(x, maxx)
        miny = min(y, miny)
        maxy = max(y, maxy)

    return (minx, miny), (maxx, maxy)

def step(parts):
    return [((x+dx, y+dy), (dx, dy)) for (x,y), (dx,dy) in parts]

def print_parts(parts):
    (minx,miny), (maxx,maxy) = get_dims(parts)

    seen = set((x,y) for (x,y), _ in parts)
    for y in range(miny,maxy+1):
        for x in range(minx,maxx+1):
            if (x,y) in seen:
                print("#", end="")
            else:
                print(" ", end="")

        print("")



def solve(parts):
    # print("Initialy")
    # print_parts(parts)

    i = 1
    (minx,miny), (maxx,maxy) = get_dims(parts)
    prev_area = (maxx-minx) * (maxy - miny)
    while True:
        nparts = step(parts)
        (minx,miny), (maxx,maxy) = get_dims(nparts)
        area = (maxx-minx) * (maxy - miny)

        if prev_area < area:
            break

        parts = nparts
        prev_area = area
        print("After {} seconds: {}".format(i, area))
        i += 1

    print_parts(parts)

parts = [((x,y), (dx,dy)) for (x,y,dx,dy) in numbers]
# print(solve((parts)))
solve((parts))
