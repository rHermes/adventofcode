import fileinput as fi
import re
import itertools as it
import functools as ft
import string
import collections as cs
import math
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
# from bidict import bidict

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


def step(x,y, dx, dy):
    if dx < 0:
        ndx = dx+1
    elif dx > 0:
        ndx = dx-1
    else:
        ndx = dx
    return (x+dx, y+dy,ndx, dy-1)

def try_vec(xmin,xmax,ymin,ymax, dx, dy):
    x, y = 0, 0
    max_y = 0
    found = False
    while ymin <= y and x <= xmax:
        max_y = max(max_y, y)
        if ymin <= y <= ymax and xmin <= x <= xmax:
            return max_y
        else:
            x, y, dx, dy = step(x, y, dx, dy)

    return None
        

def solve(xmin,xmax,ymin,ymax):
    max_al = 0
    good = 0
    for dx in range(0, xmax+1):
        for dy in range(-600, 600):
            al = try_vec(xmin,xmax,ymin,ymax,dx,dy)
            if al is not None:
                good += 1
                print(dx, dy, al)
                max_al = max(max_al, al)

    return good
    return max_al

# print(solve(20,30,-10,-5)) # example
print(solve(135,155,-102,-78)) # my input
