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

P = [x for x in "abcdefghijklmnop"]
# P = [x for x in "abcde"]

moves = lines[0].split(",")

import tqdm
cache = {}


def check_loop(cache, src):
    cur = src
    if cur not in cache:
        return False

    cur = cache[cur]
    while cur in cache:
        if cur == src:
            return True
        cur = cache[cur]

    return False


N = 1000000000
i = 0
while i < N:
    ll = "".join(P)
    if ll in cache:
        P = list(cache[ll])
        i += 1
        continue

    for move in moves:
        if move[0] == "s":
            Q = collections.deque(P)
            Q.rotate(int(move[1:]))
            P = list(Q)
        elif move[0] == "p":
            a, b = move[1], move[3]
            ai, bi = P.index(a), P.index(b)
            P[ai], P[bi] = P[bi], P[ai]
        elif move[0] == "x":
            ai, bi = map(int, move[1:].split("/"))
            P[ai], P[bi] = P[bi], P[ai]
        else:
            raise Exception("SOMETHIGN IS WRONG")

    cache[ll] = "".join(P)
    i += 1
    if not check_loop(cache, "".join(P)):
        continue

    src = "".join(P)
    cur = src
    sz = 1
    while cache[cur] != src:
        sz += 1
        cur = cache[cur]

    m = (N-i) // sz
    i += m*sz

print("".join(P))
