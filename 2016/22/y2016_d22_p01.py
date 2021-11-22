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

nodes = []
for line in lines[2:]:
    nam, sz, used, avail, use = [x for x in line.split(" ") if x]
    sz = int(sz[:-1])
    used = int(used[:-1])
    avail = int(avail[:-1])
    use = int(use[:-1])

    nodes.append((nam, sz, used, avail, use))

ans = 0
for i in range(len(nodes)):
    inam, isz, iused, iavail, iuse = nodes[i]
    if iuse == 0:
        continue
    # for j in range(i+1,len(nodes)):
    for j in range(len(nodes)):
        if i == j:
            continue

        jnam, jsz, jused, javail, juse = nodes[j]
        if iused <= javail or (juse != 0 and jused <= iavail):
            ans += 1


print(ans)
