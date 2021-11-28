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

regs = collections.defaultdict(int)

i = 0
while 0 <= i < len(lines):
    parts = lines[i].split(" ")

    if parts[0] == "snd":
        print("PLAY {}".format(regs[parts[1]]))
        i += 1
    elif parts[0] == "set":
        if parts[2].isalpha():
            val = regs[parts[2]]
        else:
            val = int(parts[2])

        regs[parts[1]] = val
        i += 1

    elif parts[0] == "add":
        if parts[2].isalpha():
            val = regs[parts[2]]
        else:
            val = int(parts[2])

        regs[parts[1]] = regs[parts[1]] + val

        i += 1

    elif parts[0] == "mul":
        if parts[2].isalpha():
            val = regs[parts[2]]
        else:
            val = int(parts[2])

        regs[parts[1]] = regs[parts[1]] * val

        i += 1

    elif parts[0] == "mod":
        if parts[2].isalpha():
            val = regs[parts[2]]
        else:
            val = int(parts[2])

        regs[parts[1]] = regs[parts[1]] % val

        i += 1

    elif parts[0] == "rcv":
        if parts[1].isalpha():
            val = regs[parts[1]]
        else:
            val = int(parts[1])

        if val != 0:
            print("RECOVERED!")
            break

        i += 1

    elif parts[0] == "jgz":
        if parts[1].isalpha():
            a = regs[parts[1]]
        else:
            a = int(parts[1])

        if parts[2].isalpha():
            b = regs[parts[2]]
        else:
            b = int(parts[2])

        if 0 < a:
            i += b
        else:
            i += 1
    else:
        print(parts)
        raise Exception("ERROR")
