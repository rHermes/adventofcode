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

for line in lines:
    # gprint(line)

    hypers = regex.sub("\[[a-z]*\]", " ", line)
    ins = " ".join(regex.findall("\[([a-z]*)\]", line))
    

    for match in regex.findall(r"([a-z])([a-z])\1", hypers, overlapped=True):
        a, b = match
        if a == b:
            continue

        # if re.search("\[[a-z]*" + b + a +b + "[a-z]*\]", ins):
        if re.search("[a-z]*" + b + a +b + "[a-z]*", ins):
            break
    else:
        continue

    print(line)


