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

def create_map(lines):
    m = []
    robot = None
    points = {}
    for y, line in enumerate(lines):
        row = []
        for x, c in enumerate(line):
            if c == '#':
                row.append(False)
            else:
                row.append(True)

            if c not in '.#':
                if c == "0":
                    robot = (x,y)
                else:
                    points[int(c)] = (x,y)

        m.append(row)

    return (m, robot, points)

def best_path(M, src, dst):
    f = lambda p: abs(dst[0] - p[0]) + abs(dst[1] - p[1])
    Q = [(0 + f(src), 0, src)]


    seen = set()
    while len(Q) > 0:
        _, depth, (px,py) = heapq.heappop(Q)
        if (px,py) == dst:
            return depth

        if (px,py) in seen:
            continue
        else:
            seen.add((px,py))

        for dx, dy in [(0,1), (0, -1), (1, 0), (-1, 0)]:
            tx, ty = px + dx, py + dy

            if M[ty][tx]:
                heapq.heappush(Q,(depth + 1 + f((tx,ty)), depth + 1, (tx,ty)))

def optimal_it(G, src, seen, cost=0):
    # print("Called with: {}, {}, {}".format(src, seen, cost))
    tried = 0
    min_cost = 1000000000000000000000000
    min_pth = None
    for (a, b), dcost in G.items():
        if a != src:
            continue

        if b in seen:
            continue

        ocost, opth = optimal_it(G, b, seen + (b,), cost=cost+dcost)
        tried += 1
        if ocost < min_cost:
            min_cost = ocost
            min_pth = opth


    if tried == 0:
        return cost, seen
    else:
        return min_cost, min_pth


M, robot, points = create_map(lines)

# print(robot)
# print(points)
points[0] = robot

G = {}
for (an, ap), (bn, bp) in it.combinations(points.items(), 2):
    bp = best_path(M, ap, bp)
    G[(an,bn)] = bp
    G[(bn,an)] = bp
    # print("The best path from {} to {} is: {}".format(an, bn, bp))

print(optimal_it(G, 0, (0,)))
