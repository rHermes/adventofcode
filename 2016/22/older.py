import fileinput as fi
import re
import itertools as it
import functools as ft
import string
import collections
import math
import sys

# findall, search, parse
from parse import *
import more_itertools as mit
import z3
import numpy as np
import lark
import regex
import intervaltree as itree

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


max_depth = 0

def solve(nodes, target, seen, depth=0):
    global max_depth
    if target == (0, 0):
        print("We have a solution")
        return 1

    # if depth > max_depth:
    #     max_depth = depth
    #     print("We reached new max depth {}".format(max_depth))

    # Depth limit
    if depth > 10:
        return None

    things = tuple(sorted((x, y, sz, used, avail) for (x,y), (sz, used,avail) in nodes.items()))
    things = target + things
    if things in seen:
        dl = seen[things]
        if dl < depth:
            return None

    seen[things] = depth


    

    min_ans = None
    for (px, py), (sz, used, avail) in nodes.items():
        if used == 0:
            continue

        for (dx, dy) in [(0,1), (0,-1), (1,0), (-1,0)]:
            gx, gy = px + dx, py + dy
            if (gx, gy) not in nodes:
                continue

            gsz, gused, gavail = nodes[(gx, gy)]

            if used > gavail:
                continue

            # Ok we have a potentail candidate, we must modify then try again
            nodes[(px, py)] = (sz, 0, sz)
            nodes[(gx, gy)] = (gsz, gused + used, gavail - used)
            if (px, py) == target:
                pans = solve(nodes, (gx, gy), seen, depth=depth+1)
            else:
                pans = solve(nodes, target, seen, depth=depth+1)

            nodes[(gx, gy)] = (gsz, gused, gavail)
            nodes[(px, py)] = (sz, used, avail)

            if not pans:
                continue

            if not min_ans:
                min_ans = pans
            else:
                if min_ans > pans:
                    min_ans = pans


    if min_ans:
        # seen[things] = 1 + min_ans
        return 1 + min_ans
    else:
        # seen[things] = None
        return None


target_x = 0
nodes = {}
for line in lines[2:]:
    nam, sz, used, avail, use = [x for x in line.split(" ") if x]
    _, x, y = nam.split("-")
    x = int(x[1:])
    y = int(y[1:])
    sz = int(sz[:-1])
    used = int(used[:-1])
    avail = int(avail[:-1])
    use = int(use[:-1])

    target_x = max(target_x, x)
    nodes[(x,y)] = (sz, used, avail) 

# print(target_x)
# print(nodes)
print(solve(nodes, (target_x, 0), {}) - 1)
