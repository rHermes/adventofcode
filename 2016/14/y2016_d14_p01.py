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

import hashlib

# print(sys.getrecursionlimit())
sys.setrecursionlimit(6500)

# Debug logging
DEBUG = True
def gprint(*args, **kwargs):
    if DEBUG: print(*args, **kwargs)

# # Input parsing
# INPUT = "".join(fi.input()).rstrip()
# groups = INPUT.split("\n\n")
# lines = list(INPUT.splitlines())

cands = [(0, "ø") for x in range(1000)]
keys = []
for line in fi.input():
    idx, hsh = line.rstrip().split(" ")
    idx = int(idx)
    # print(idx)

    for i, (adx, cand) in enumerate(cands):
        if cand in hsh:
            keys.append((adx, hsh))
            cands[i] = (0, "ø")
            print(adx, cand)
            # break
            

    cands.pop(0)
    for i in range(len(hsh)-2):
        if hsh[i] == hsh[i+1] == hsh[i+2]:
            cands.append((idx, hsh[i] + hsh[i] + hsh[i] + hsh[i] + hsh[i]))
            break
    else:
        cands.append((0, "ø"))
        continue
