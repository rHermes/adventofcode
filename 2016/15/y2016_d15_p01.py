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

discs = []
for line in lines:
    disc, npos, stime, spos = parse("Disc #{:d} has {:d} positions; at time={:d}, it is at position {:d}.", line)
    discs.append((disc, npos, stime, spos))


print(discs)
period = 1
time = 0
for (disc, npos, stime, spos) in discs:
    while (time + disc + spos) % (npos) != 0:
        time += period

    period *= npos


print(time)
