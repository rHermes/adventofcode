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

def step(s):
    x = []
    ss = [False] + s + [False]
    for i in range(1,len(s)+1):
        a, b, c = ss[i-1], ss[i], ss[i+1]
        is_trap = [
            a and b and (not c),
            b and c and (not a),
            (not a) and (not b) and c,
            (not b) and (not c) and a,
        ]

        x.append(any(is_trap))

    return x


ins = ['^' == x for x in lines[0]]

# print(ins)
ans = 0
for _ in range(400000):
    ans += sum(not x for x in ins)
    ins = step(ins)

print(ans)
# for line in lines:
#     gprint(line)
