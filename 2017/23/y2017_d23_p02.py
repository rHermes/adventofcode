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



def solve():
    regs = {x: 0 for x in "abcdefgh"}
    regs["a"] = 1
    # set b 57
    # set c b
    # jnz a 2
    # jnz 1 5
    # mul b 100
    # sub b -100000
    # set c b
    # sub c -17000
    # set f 1
    # set d 2
    # set e 2
    # set g d
    # mul g e
    # sub g b
    # jnz g 2
    # set f 0
    # sub e -1
    # set g e
    # sub g b
    # jnz g -8
    # sub d -1
    # set g d
    # sub g b
    # jnz g -13
    # jnz f 2
    # sub h -1
    # set g b
    # sub g c
    # jnz g 2
    # jnz 1 3
    # sub b -17
    # jnz 1 -23






def reg_or_val(regs, x):
    if x.isalpha():
        return regs[x]
    else:
        return int(x)

regs = collections.defaultdict(int)

# regs = {"a": 0, "b": 0, "c": 0, ""}
regs = {x: 0 for x in "abcdefgh"}
regs["a"] = 1

ans = 0
i = 0
while 0 <= i < len(lines):
    parts = lines[i].split(" ")

    if i == 8:
        print(i, regs)

    if parts[0] == "set":
        regs[parts[1]] = reg_or_val(regs, parts[2])

    elif parts[0] == "sub":
        regs[parts[1]] = regs[parts[1]] - reg_or_val(regs, parts[2])

    elif parts[0] == "mul":
        regs[parts[1]] = regs[parts[1]] * reg_or_val(regs, parts[2])

    elif parts[0] == "jnz":
        if 0 != reg_or_val(regs, parts[1]):
            i += reg_or_val(regs, parts[2])
            continue
    else:
        raise Exception("Unknown operator: {}".format(parts[0]))

    i += 1

print(ans)
