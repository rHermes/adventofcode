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
# import more_itertools as mit
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

seen = set()
on_right = set()

for line in lines:
    ins, *above = line.split(" -> ")
    name, weight = ins.split(" ")
    weight = int(weight[1:-1])
    seen.add(name)
    if above:
        for ot in above[0].split(", "):
            on_right.add(ot)

print(list(seen-on_right)[0])
