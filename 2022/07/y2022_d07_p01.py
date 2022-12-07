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


# Input parsing
INPUT = "".join(fi.input()).rstrip()
groups = INPUT.split("\n\n")
lines = list(INPUT.splitlines())
numbers = [list(map(int, re.findall("-?[0-9]+", line))) for line in lines]
pos_numbers = [list(map(int, re.findall("[0-9]+", line))) for line in lines]
grid = [[c for c in line] for line in lines]
gsz = (len(grid), len(grid[0]))

def solve():
    kv = {}
    dir =  []
    i = 0
    while i < len(lines):
        w = lines[i].split(" ")
        i += 1
        if w[1] == "cd":
            if w[2] == "/":
                dir = []
            elif w[2] == "..":
                dir = dir[:-1]
            else:
                dir.append(w[2])
        else:
            while i < len(lines) and not lines[i].startswith("$ "):
                sz, name = lines[i].split(" ")
                i += 1
                if sz == "dir":
                    continue
                    
                sz = int(sz)
                fn = "/" + "/".join(dir + [name])
                kv[fn] = ("/" + "/".join(dir), sz)


    print(kv)
    szes = cs.defaultdict(int)
    keys = kv.keys()
    kks = sorted(keys, key=lambda x: len(x.split("/")), reverse=True)
    print(kks)
    for key in kks:
        root, sz = kv[key]
        print(root, sz)
        szes["/"] += sz
        if root == "/":
            continue

        lv = root.split("/")
        lv = lv[1:]

        cur_pth = ""
        for part in lv:
            cur_pth += "/" + part
            szes[cur_pth] += sz



    ans = 0
    for k, v in szes.items():
        if 100000 < v:
            continue
        ans += v

    return ans





print(solve())
