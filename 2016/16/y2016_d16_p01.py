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

# for line in lines:
#     gprint(line)

ins = lines[0]

def step(s):
    a = s
    b = a
    b = "".join(reversed(b))
    b = b.replace('1', 'x').replace("0", "1").replace("x", "0")
    return a + "0" + b

def checksum(s):
    a = s
    chk = ""
    for i in range(0, len(s), 2):
        x, y = s[i], s[i+1]
        if x == y:
            chk += "1"
        else:
            chk += "0"

    if len(chk) % 2 == 0:
        return checksum(chk)
    else:
        return chk

def solve(s, n):
    while len(s) < n:
        s = step(s)

    return checksum(s[:n])

print(solve(ins, 272))
