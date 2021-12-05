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
numbers = [list(map(int, re.findall("-?[0-9]+", line))) for line in lines]

def parse_input(groups):
    world = set()
    _, b = groups[0].split(": ")
    for i, x in enumerate(b):
        if x == '#':
            world.add(i)

    trans = collections.defaultdict(bool)
    for pw in groups[1].splitlines():
        a, b = pw.split(" => ")
        a = tuple(x == '#' for x in a)
        b = b == '#'
        trans[a] = b

    return world, trans

def step(world, trans):
    consider = set()
    for p in world:
        consider.update(range(p-2,p+3))

    nworld = set()
    for p in consider:
        pat = tuple(x in world for x in range(p-2,p+3))
        if trans[pat]:
            nworld.add(p)

    return nworld

world, trans = parse_input(groups)
# print(world, trans)
for i in range(20):
    world = step(world, trans)

print(sum(world))
