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


import heapq
max_depth = 0

def hash_state(target, nodes):
    things = tuple(sorted((x, y, sz, used, avail) for (x,y), (sz, used,avail) in nodes.items()))
    things = target + things
    return things
    # if things in seen:
    #     dl = seen[things]
    #     if dl < depth:
    #         return None

    # seen[things] = depth

def solve(nodes, target, limits):
    max_x, max_y = limits
    Q = [(target[0] + target[1], 0, target, ())]

    max_depth = 0
    seen = set()
    seen_targets = set()
    while len(Q) > 0:
        # Transform the grid
        score, depth, target, moves = heapq.heappop(Q)
        
        if depth > max_depth:
            max_depth = depth
            print("New max depth: {}".format(max_depth))

        if target not in seen_targets:
            print("We saw target {} for the first time at depth: {}".format(target, depth))
            seen_targets.add(target)
        if target == (0, 0):
            return depth

        revert = {}
        # print(moves)
        for (sx, sy), (dx, dy) in moves:
            if (sx,sy) not in revert:
                revert[(sx,sy)] = nodes[(sx,sy)]

            if (dx, dy) not in revert:
                revert[(dx, dy)] = nodes[(dx,dy)]

            ssz, sused, savail = nodes[(sx,sy)]
            dsz, dused, davail = nodes[(dx,dy)]

            nodes[(sx, sy)] = (ssz, 0, ssz)
            nodes[(dx, dy)] = (dsz, dused + sused, davail - sused)

        do = True
        hh = hash(hash_state(target, nodes))
        if hh in seen:
            do = False
        else:
            seen.add(hh)

            

        for (px, py), (sz, used, avail) in nodes.items():
            if not do:
                break

            if used == 0:
                continue

            for (dx, dy) in [(0,1), (0,-1), (1,0), (-1,0)]:
                gx, gy = px + dx, py + dy
                if not (0 <= gx <= max_x and 0 <= gy <= max_y):
                    continue
                # if (gx, gy) not in nodes:

                gsz, gused, gavail = nodes[(gx, gy)]

                if used > gavail:
                    continue
            
                # Ok, potential candidate
                if (px, py) == target:
                    # heapq.heappush(Q, (depth + 1 + gx + gy, depth + 1, (gx, gy), moves + (((px, py), (gx, gy)),)))
                    heapq.heappush(Q, (0, depth + 1, (gx, gy), moves + (((px, py), (gx, gy)),)))
                else:
                    # heapq.heappush(Q, (depth + 1 + target[0] + target[1], depth + 1, target, moves + (((px, py), (gx, gy)),)))
                    heapq.heappush(Q, (0, depth + 1, target, moves + (((px, py), (gx, gy)),)))

    
        # revert board
        for (x, y), (sz, used, avail) in revert.items():
            nodes[(x,y)] = (sz, used, avail)







target_x = 0
max_y = 0
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
    max_y = max(max_y, y)
    nodes[(x,y)] = (sz, used, avail) 

# print(target_x)
# print(nodes)
print(solve(nodes, (target_x, 0), (target_x, max_y)))
