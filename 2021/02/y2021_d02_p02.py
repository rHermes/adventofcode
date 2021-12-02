import fileinput as fi
import re
import itertools as it
import functools as ft
import string
import collections
import math
import sys
import heapq

# findall, search, parse
# from parse import *
import more_itertools as mit
# import z3
# import numpy as np
# import lark
# import regex
# import intervaltree as itree

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
numbers = [list(map(int, re.findall("[0-9]+", line))) for line in lines]


hor = 0
dep = 0
aim = 0
for line in lines:
    d, b = line.split(" ")
    if d == "forward":
        hor += int(b)
        dep += aim * int(b)
    elif d == "down":
        # dep += int(b)
        aim += int(b)
    elif d == "up":
        # dep -= int(b)
        aim -= int(b)
    # print(d, b, hor, dep, aim)

print(hor * dep)
