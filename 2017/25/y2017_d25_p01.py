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


def parse_state(group):
    lines = [x.strip().split(" ") for x in group.split("\n")]

    name = lines[0][-1][:-1]

    for i in range(1, len(lines), 4):
        # print(lines[i])
        cval = lines[i][-1][:-1] == "1"
        write = lines[i+1][-1][:-1] == "1"
        dx = {"right.": 1, "left.": -1}[lines[i+2][-1]]
        nx = lines[i+3][-1][:-1]
        
        if cval == False:
            ff = (write, dx, nx)
        else:
            rr = (write, dx, nx)


    return (name, ff, rr)

# Input parsing
INPUT = "".join(fi.input()).rstrip()
groups = INPUT.split("\n\n")
lines = list(INPUT.splitlines())


hd = groups[0].split("\n")
strt_state = hd[0].split(" ")[-1][:-1]
goal = int(hd[1].split(" ")[-2])
print(strt_state, goal)


states = {}
for grp in groups[1:]:
    name, ff, rr = parse_state(grp)
    states[name] = (ff, rr)

# print(states)

tape = collections.defaultdict(bool)
c = 0
state = strt_state

for _ in range(goal):
    cval = tape[c]
    nval, dx, state = states[state][cval]
    tape[c] = nval
    c += dx
    # print(c, state)

print(sum(tape.values()))
