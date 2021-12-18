import fileinput as fi
import re
import itertools as it
import functools as ft
import string
import collections as cs
import math
import sys
import heapq
from copy import deepcopy

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


# Input parsing
INPUT = "".join(fi.input()).rstrip()
groups = INPUT.split("\n\n")
lines = list(INPUT.splitlines())
numbers = [list(map(int, re.findall("-?[0-9]+", line))) for line in lines]
grid = [[c for c in line] for line in lines]
gsz = (len(grid), len(grid[0]))

# list, val, dir
def add_on(w, x, d):
    lef = d == "left"

    a, b = w
    al = isinstance(a, list)
    bl = isinstance(b, list)

    if lef:
        # left
        if al:
            add_on(a, x, d)
        else:
            w[0] += x
    else:
        # Right
        if bl:
            add_on(b, x, d)
        else:
            w[1] += x

    

def explodes(w, depth=0):
    a, b = w
    al = isinstance(a, list)
    bl = isinstance(b, list)

    if depth == 3 and (al or bl):
        # print("We should explode")
        # print(w)
        if al:
            l, r = a[0], a[1]
            w[0] = 0

            if not bl:
                w[1] += r
            else:
                add_on(w[1], r, 'left')
            r = None

            return (l,r)
        else:
            assert(bl)

            l, r = b[0], b[1]
            w[1] = 0

            if not al:
                w[0] += l
            else:
                add_on(w[0], l, 'right')
            l = None

            return (l, r)
        
        raise Exception("Not supposed to happen")

    
    if al:
        kk = explodes(a, depth+1)
        if kk is not None:
            l, r = kk
            if l is not None:
                assert(r is None)
                return (l,r)

            if r is not None:
                assert(l is None)

                if bl:
                    add_on(b, r, 'left')
                else:
                    w[1] += r

                return (None, None)

            return (None, None)

    if bl:
        kk = explodes(b, depth+1)
        if kk is not None:
            l, r = kk
            if r is not None:
                assert(l is None)
                return (l,r)

            if l is not None:
                assert(r is None)

                if al:
                    add_on(a, l, 'right')
                else:
                    w[0] += l

                return (None, None)

            return (None, None)

    return None

def splits(w):
    a, b = w
    al = isinstance(a, list)
    bl = isinstance(b, list)

    if al:
        k = splits(a)
        if k:
            return True
    else:
        if 9 < a:
            l =a//2
            r = int(math.ceil(a/2))
           # print("We should split!")
            # print(w)
            # print(l, r)
            w[0] = [l, r]
            return True

    if bl:
        k = splits(b)
        if k:
            return True
    else:
        if 9 < b:
            l =b//2
            r = int(math.ceil(b/2))
            # print("We should split!")
            # print(w)
            # print(l, r)
            w[1] = [l, r]
            return True
    
    return False




def sadd(a, b):
    return [a,b]


def reduce(w):
    # We repetedly do both
    while True:
        k = explodes(w,0)
        if k is not None:
            continue

        k = splits(w)
        if k:
            continue

        break

def mag(w):
    ans = 0
    a, b = w
    al = isinstance(a, list)
    bl = isinstance(b, list)
    if al:
        ans += 3*mag(a)
    else:
        ans += 3*a

    if bl:
        ans += 2*mag(b)
    else:
        ans += 2*b

    return ans



def solve():
    ans = eval(lines[0])
    reduce(ans)

    for line in lines[1:]:
        w = eval(line)
        ans = sadd(ans, w)
        reduce(ans)
        print(ans)

    return ans

ww = solve()
print(ww)
print(mag(ww))
