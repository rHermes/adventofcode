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

shifts = {a: b for a,b in zip(string.ascii_lowercase, string.ascii_lowercase[1:] + 'a')}
def man_shift(s, n):
    for _ in range(n):
        s = shifts[s]
    return s

@ft.cache
def create_shift(n):
    return {a: man_shift(a, n) for a in string.ascii_lowercase}


ans = 0
for line in lines:
    m  = re.match(r"(.*)-([0-9]+)\[(.*)\]", line)
    
    name, sid, ch = m.groups()
    c = collections.Counter(sorted(name))
    del c["-"]
    ll = ""
    for l, _ in c.most_common(5):
        ll += l

    if ll != ch:
        continue

    real = ""
    shift = create_shift(int(sid) % len(string.ascii_lowercase))
    for k in name:
        if k == "-":
            real += " "
        else:
            real += shift[k]

    if "north" in real:
        print(real, sid)
