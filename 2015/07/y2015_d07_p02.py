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


def solve(G, wire, cache):
    if wire in cache:
        return cache[wire]

    xs = G[wire]

    if len(xs) == 1:
        if xs[0].isnumeric():
            ans = np.uint16(xs[0])
        else:
            ans = solve(G, xs[0], cache)
    elif len(xs) == 2:
        ans = ~solve(G, xs[1], cache)
    elif len(xs) == 3:
        l, op, r = xs
        if l.isnumeric():
            l = np.uint16(l)
        else:
            l = solve(G, l, cache)

        if r.isnumeric():
            r = np.uint16(r)
        else:
            r = solve(G, r, cache)

        if op == "AND":
            ans = l & r
        elif op == "OR":
            ans = l | r
        elif op == "LSHIFT":
            ans = l << r
        elif op == "RSHIFT":
            ans = l >> r
        else:
            raise Exception("DOOO: " + " ".join(xs))

    else:
        raise Exception("NOOO: " + " ".join(xs))

    cache[wire] = ans
    return ans


rights = {}
for line in lines:
    l, r = line.split(" -> ")
    rights[r] = l.split(" ")

b = solve(rights, "a", {})
rights["b"] = [str(b)]
print(solve(rights, "a", {}))
