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

def reg_or_val(regs, x):
    if x.isalpha():
        return regs[x]
    else:
        return int(x)

regs = collections.defaultdict(int)

# regs = {"a": 0, "b": 0, "c": 0, ""}
regs = {x: 0 for x in "abcdefgh"}
print(regs)

ans = 0
i = 0
while 0 <= i < len(lines):
    parts = lines[i].split(" ")

    if parts[0] == "set":
        regs[parts[1]] = reg_or_val(regs, parts[2])

    elif parts[0] == "sub":
        regs[parts[1]] = regs[parts[1]] - reg_or_val(regs, parts[2])

    elif parts[0] == "mul":
        ans += 1
        regs[parts[1]] = regs[parts[1]] * reg_or_val(regs, parts[2])

    elif parts[0] == "jnz":
        if 0 != reg_or_val(regs, parts[1]):
            i += reg_or_val(regs, parts[2])
            continue
    else:
        raise Exception("Unknown operator: {}".format(parts[0]))

    i += 1

print(ans)
