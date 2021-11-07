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

a = np.full((1000,1000), False)

for line in lines:
    w = line.split(" ")
    p1, p2 = w[-3], w[-1]
    pa, pb = map(int, p1.split(","))
    ja, jb = map(int, p2.split(","))
    ja = ja+1
    jb = jb+1


    if line.startswith("toggle "):
        a[pb:jb, pa:ja] = ~a[pb:jb, pa:ja]
    elif line.startswith("turn on"):
        a[pb:jb, pa:ja] = True
    elif line.startswith("turn off"):
        a[pb:jb, pa:ja] = False

print(a.sum())
