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

import networkx as nx
def solve():
    my, mx = gsz
    for y in range(my):
        for x in range(mx):
            if grid[y][x] == "S":
                start = (y, x)
                grid[y][x] = "a"
            if grid[y][x] == "E":
                end = (y, x)
                grid[y][x] = "z"
    
    print("Start: {}, End: {}".format(start, end))

    G = nx.DiGraph()
    dm = {}

    for y in range(my):
        for x in range(mx):
            dm[(y,x)] = len(dm) + 1
            G.add_node(dm[(y,x)])

    for y in range(my):
        for x in range(mx):
            c = ord(grid[y][x]) - ord('a')
            for (ly,lx) in ortho(y,x,gsz):
                pc = ord(grid[ly][lx]) - ord('a')
                if (pc - c) <= 1:
                    G.add_edge(dm[(y,x)], dm[(ly,lx)])
                    # G.add_edge(dm[(ly,lx)], dm[(y,x)])
    
    print(G)
    w = nx.shortest_path(G, dm[start], dm[end])
    print(w)
    return w



    seen = set()
    Q = cs.deque([(start,)])
    mx = 0
    while Q:
        path = Q.popleft()
        py,px = path[-1]
        c = ord(grid[py][px]) - ord('a')
        seen.add((py,px))


        

        if (py,px) == end:
            return path
            # return len(path)

        for (ly,lx) in ortho(py,px,gsz):
            pc = ord(grid[ly][lx]) - ord('a')
            if pc - c <= 1 and (ly,lx) not in seen:
                Q.append(path + ((ly,lx),))


            



print(len(solve()) - 1)
