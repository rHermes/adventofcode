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

out_a = set()
out_b = set()

in_a = [x for x in lines]
in_b = [x for x in lines]


j = 0
while len(in_a) > 1:
    ones = [x for x in in_a if x[j] == "1"]
    zeros = [x for x in in_a if x[j] == "0"]
    j += 1
    if len(zeros) > len(ones):
        in_a = zeros
    else:
        in_a = ones

j = 0
while len(in_b) > 1:
    ones = [x for x in in_b if x[j] == "1"]
    zeros = [x for x in in_b if x[j] == "0"]
    j += 1
    if len(ones) < len(zeros):
        in_b = ones
    else:
        in_b = zeros

print(in_a)
print(in_b)
print(int(in_a[0], 2)*int(in_b[0], 2))
