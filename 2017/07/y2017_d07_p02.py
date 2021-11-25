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
# import more_itertools as mit
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


G = {}
W = {}

seen = set()
on_right = set()

for line in lines:
    ins, *above = line.split(" -> ")
    name, weight = ins.split(" ")
    weight = int(weight[1:-1])
    seen.add(name)
    W[name] = weight
    if above:
        G[name] = above[0].split(", ")
        for w in above[0].split(", "):
            on_right.add(w)
    else:
        G[name] = []

def sum_weight(G, W, node, WS):
    if node in WS:
        return WS[node]

    ans = W[node] + sum(sum_weight(G, W, x, WS) for x in G[node])
    WS[node] = ans
    return ans

root = list(seen-on_right)[0]

# print(sum_weight(G, W, root, WS))

def solve(G, W, WS, root):
    counts = {}
    nds = {x: sum_weight(G, W, x, WS) for x in G[root]}
    # print(root, nds)
    counts = {}
    for k, v in nds.items():
        if v not in counts:
            counts[v] = 0

        counts[v] += 1

    if len(counts) == 1:
        return None

    assert(len(counts) == 2)

    bad_w = 0
    good_w = 0
    for k, v in counts.items():
        if v == 1:
            bad_w = k
        else:
            good_w = k

    bad_node = None
    for k, v in nds.items():
        if v == bad_w:
            bad_node = k
            break

    # print(bad_node)
    dn = solve(G, W, WS, bad_node)
    if dn == None:
        # we are the bad node
        # print(root, bad_w, good_w, good_w - bad_w, W[bad_node] + (good_w - bad_w))
        return W[bad_node] + (good_w - bad_w)
    else:
        return dn

WS = {}
print(solve(G, W, WS, root))
