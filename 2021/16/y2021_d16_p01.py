import fileinput as fi
import re
import itertools as it
import functools as ft
import string
import collections as cs
import math
import cmath
import sys
import heapq

# findall, search, parse
from parse import *
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
grid = [[c for c in line] for line in lines]
gsz = (len(grid), len(grid[0]))


def decode(h):
    # print("called decode with {}".format(h))
    oh = h
    ver = int(h[:3],2)
    print(ver)
    h = h[3:]
    typ = int(h[:3],2)
    h = h[3:]

    if typ == 4:
        nums = []
        while h[0] != "0":
            nums.append(h[1:5])
            h = h[5:]

        nums.append(h[1:5])
        h = h[5:]

        nn = "".join(nums)
        gv = int(nn, 2)
        # print(gv)
        return ("literal", ver, gv, h)
    else:
        lty = h[0] == "1"
        h = h[1:]
        if lty:
            subpak = int(h[:11], 2)
            h = h[11:]
            vs = []
            for i in range(subpak):
                kk = decode(h)
                h = kk[-1]
                vs.append(kk)

            return ("op_cnt", ver, subpak, vs, h)
        else:
            npak = int(h[:15], 2)
            h = h[15:]
            kv = h[:npak]
            h = h[npak:]

            vs = []
            vs.append(decode(kv))
            while len(vs[-1][-1]) != 0:
                # print(vs)
                if not "1" in vs[-1][-1]:
                    break
                kk = vs[-1][-1]
                # print(kk)
                vs.append(decode(kk))

            return ("op_len", ver, typ, lty, npak, vs, h)
            




def solve(s):
    # extra 0z at then end?
    h = "".join("{:04b}".format(int(x, 16)) for x in s)
    # print(h)
    return decode(h)






solve(lines[0])
# print(solve(lines[0]))
