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

regs = collections.defaultdict(int)

for line in lines:
    reg, op, delta, _, op1, rel, op2 = line.split(" ")
    if op == "inc":
        delta = int(delta)
    elif op == "dec":
        delta = -int(delta)
    else:
        raise Exception("WTF!")

    if eval("{} {} {}".format(regs[op1], rel, op2)):
        regs[reg] += delta

print(max(regs.values()))



