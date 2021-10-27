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

ans = 0
for line in lines:
    m  = re.match(r"(.*)-([0-9]+)\[(.*)\]", line)
    if m is None:
        print("WARN: ", line)
        continue
    
    name, sid, ch = m.groups()
    c = collections.Counter(sorted(name))
    del c["-"]
    ll = ""
    for l, _ in c.most_common(5):
        ll += l

    if ll != ch:
        continue
    
    ans += int(sid)

print(ans)

