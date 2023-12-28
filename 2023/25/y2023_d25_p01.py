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

G = cs.defaultdict(set)
lsp = []
for line in lines:
    src, dsts = line.split(": ")
    dsts = dsts.split(" ")
    for d in dsts:
        G[src].add(d)
        G[d].add(src)
        lsp.append((min(src,d), max(src,d)))

def get_groups(G):
    seen = set()
    groups = []
    while len(seen) < len(G):
        groups.append(set())

        w = None
        for k in G.keys():
            if k not in seen:
                w = k
                break

        Q = cs.deque([w])
        while Q:
            s = Q.pop()

            if s in seen:
                continue
            else:
                seen.add(s)

            groups[-1].add(s)

            for des in G[s]:
                if des not in seen:
                    Q.append(des)

    return groups

def shortest_path(G, a, b):
    seen = set()
    prev = {}
    Q = cs.deque([a])
    seen.add(a)
    while Q:
        s = Q.popleft()

        if s == b:
            pth = []
            cur = s
            while cur != a:
                pth.append(cur)
                cur = prev[cur]

            pth.append(a)
            pth.reverse()
            return pth

        for d in G[s]:
            if d not in seen:
                prev[d] = s
                seen.add(d)
                Q.append(d)
    
    return []


# print("graph G {")
# for s, d in lsp:
#     print(s, "--", d, ";")

# print("}")
# import tqdm
# print(len(lsp))
# lsp.sort()
# print(len(G.keys()))
# print(shortest_path(G, "frs", "xhk"))


def solve(G, A, B, cuts):
    if 3 < len(cuts):
        return None

    # print(cuts)

    p = shortest_path(G, A, B)
    if not p:
        print("WE GOT IT BOYS", cuts)
        return cuts

    for a,b in it.pairwise(p[1:-1]):
        w = cuts + tuple([(a,b)])
        G[a].remove(b)
        G[b].remove(a)
        ls = solve(G, A, B, w)
        G[a].add(b)
        G[b].add(a)

        if ls:
            return ls
            

    return None
    

# print(solve(G, []))

# maxd = 5
# maxa = None
# maxb = None
# maxps = []
# nodes = list(G.keys())

# for i in range(len(nodes)):
#     for j in range(i+1, len(nodes)):
#         a = nodes[i]
#         b = nodes[j]
#         p = shortest_path(G, a,b)

#         if maxd <= len(p):
#             maxd = len(p)
#             maxa = a
#             maxb = b
#             # maxp = p
#             maxps.append((a,b))
#             print(maxa, maxb, maxd)

#     if len(maxps) > 20:
#         break

# maxps = [('zst', 'fnq'), ('zst', 'vdp'), ('zst', 'dzq'), ('zst', 'bjq'), ('zst', 'ddk'), ('zst', 'pkt'), ('zst', 'fpd'), ('zst', 'vsm'), ('zst', 'kqv'), ('mth', 'mqf'), ('mth', 'hhj'), ('mth', 'vnz'), ('mth', 'lxq'), ('mth', 'szf'), ('mth', 'mtv'), ('mth', 'bdh'), ('mth', 'xln'), ('mth', 'qgv'), ('mth', 'mrd'), ('mth', 'svq'), ('mth', 'gpb'), ('mth', 'kxz'), ('mth', 'ncf'), ('mth', 'jvq'), ('mth', 'plt'), ('mth', 'tmn'), ('mth', 'jxk'), ('mth', 'nbb'), ('mth', 'lsv'), ('mth', 'pfz'), ('mth', 'tzs')]

w = solve(G, "zst", "fnq", tuple())

for a,b in w:
    G[a].remove(b)
    G[b].remove(a)

grps = get_groups(G)
print([len(x) for x in grps])
print(len(grps[0])*len(grps[1]))

# maxps = [('rhn', 'frs'), ('xhk', 'frs'), ('frs', 'ntq')]

# # print(maxps)
# for I in range(1,4):
#     heatmap = cs.Counter()
#     for a, b in maxps:
#         print(solve(G, a, b, tuple()))
#         # p = shortest_path(G, a, b)
#         # print(p)
#     break

    # print(heatmap)
    # break
    # pass

# for igno in tqdm.tqdm(it.combinations(lsp, 3), total=6344781530):
#     s = set()
#     a,b,c = igno
#     s.update(a)
#     s.update(b)
#     s.update(c)
#     if len(s) < 6:
#         continue
    

#     for src, d in igno:
#         G[src].remove(d)
#         G[d].remove(src)
    
    
#     groups = get_groups(G)


#     if len(groups) == 2:
#         ws = [len(x) for x in groups]
#         ans = 1
#         for w in ws:
#             ans *= w

#         print(ans)
#         break



#     for src, d in igno:
#         G[src].add(d)
#         G[d].add(src)
