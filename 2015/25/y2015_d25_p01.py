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

# for line in lines:
#     gprint(line)

max_y = 1
x = 1
l = 20151125
while True:
    y = max_y
    x = 1
    max_y += 1

    while y > 0:
        if y == 3010 and x == 3019:
            print(l)
            sys.exit(1)

        y -=1
        x += 1
        l *= 252533
        l = l % 33554393
