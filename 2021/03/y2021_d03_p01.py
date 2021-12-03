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

x = [[0,0] for _ in range(len(lines[0]))]
for line in lines:
    print(line)
    for i, c in enumerate(line):
        x[i][int(c)] += 1

gamma = ""
epsilon = ""
for a, b in x:
    if a < b:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

print(gamma, int(gamma, 2))
print(epsilon, int(epsilon, 2))

print(int(gamma, 2) * int(epsilon, 2))
