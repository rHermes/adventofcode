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

# state = set(range(0,10))
ranges = []
for line in lines:
    a, b = line.split("-")
    a = int(a)
    b = int(b)
    ranges.append((a,b))

ranges = sorted(ranges)
ans = 0
for l, h in ranges:
    print(ans, l, h)
    if ans < l:
        break
    else:
        ans = max(h+1, ans)

print(ans)
