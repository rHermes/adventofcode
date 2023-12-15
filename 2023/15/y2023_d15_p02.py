import fileinput as fi
import re
import itertools as it
import functools as ft
import string
import collections as cs
import collections.abc as abc
import math
import sys
import heapq

import typing

# findall, search, parse
from parse import *
import more_itertools as mit
# import z3
# import numpy as np
# import lark
# import regex
# import intervaltree as itree
# from bidict import bidict

# print(sys.getrecursionlimit())
sys.setrecursionlimit(6500)

# Debug logging
DEBUG = True
def gprint(*args, **kwargs):
    if DEBUG: print(*args, **kwargs)

positionT = tuple[int,int]
def ortho(y: int, x: int, shape: positionT) -> abc.Iterator[positionT]:
    """Returns all orthagonaly adjacent points, respecting boundary conditions"""
    sy, sx = shape
    if 0 < x: yield (y, x-1)
    if x < sx-1: yield (y, x+1)
    if 0 < y: yield (y-1, x)
    if y < sy-1: yield (y+1, x)

def adj(y: int, x: int, shape: positionT) -> abc.Iterator[positionT]:
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
pos_numbers = [list(map(int, re.findall("[0-9]+", line))) for line in lines]
grid = [[c for c in line] for line in lines]
gsz = (len(grid), len(grid[0]))


parts = INPUT.split(",")


def hashit(s):
    cur = 0
    for c in s:
        a = ord(c)
        cur += a
        cur *= 17
        cur %= 256
    return cur


boxes = [[] for _ in range(256)]

ans = 0
for part in parts:
    print(part)
    if "=" in part:
        label, val = part.split("=")
        val = int(val)
        h = hashit(label)

        k = boxes[h]
        print("B=", k)
        
        for i in range(len(k)):
            l, v = k[i]
            if l == label:
                k[i] = (l,val)
                break
        else:
            k.append((label, val))

        print("A=", k)
        boxes[h] = k
    elif "-" in part:
        label = part[:-1]
        h = hashit(label)

        k = boxes[h]
        print("B-", k)
        for i in range(len(k)):
            l, v = k[i]
            if l == label:
                k.pop(i)
                break

        print("A-", k)
        boxes[h] = k

ans = 0
for (i,box) in enumerate(boxes, start=1):
    for (k, v) in enumerate(box, start=1):
        print(v[0], i * k * v[1])
        ans += i * k * v[1]
print(ans)

