import fileinput as fi
import re
import itertools as it
import functools as ft
import string
import collections
import math
import sys

# findall, search, parse
# from parse import *
# import more_itertools as mit
# import z3
# import numpy as np
# import lark
# import regex

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

ins = 0

regs = {"a": 0, "b": 0, "c": 0, "d": 0}

while ins < len(lines):
    # print(ins, regs)
    ops = lines[ins].split()

    if ops[0] == "cpy":
        x, y = ops[1], ops[2]
        if x.isnumeric():
            regs[y] = int(x)
        else:
            regs[y] = regs[x]

        ins += 1

    elif ops[0] == "inc":
        regs[ops[1]] += 1
        ins += 1
    elif ops[0] == "dec":
        regs[ops[1]] -= 1
        ins += 1
    elif ops[0] == "jnz":
        if ops[1].isnumeric():
            val = int(ops[1])
        else:
            val = regs[ops[1]]

        if val != 0:
            ins += int(ops[2])
        else:
            ins += 1

    else:
        raise Exception("SOMETHING MUST BE WRONG")



print(regs)


