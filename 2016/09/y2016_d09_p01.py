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
    # s = ""
    s = 0
    i = 0
    while i < len(line):
        if line[i] == "(":
            stop = line[i:].index(")")
            seg = line[i+1:i+stop] 

            sz, times = map(int, seg.split("x"))

            reps = line[i+stop+1:i+stop+1+sz]
            # print(line)
            # print(seg)
            # print(reps)

            s += sz * times
            # for i in range(times):
            #     s += len(reps)

            i += stop+1+sz
        else:
            # s += line[i]
            s += 1
            i += 1

      
    # ans += len(s)
    ans += s
    print(s)

print(ans)
