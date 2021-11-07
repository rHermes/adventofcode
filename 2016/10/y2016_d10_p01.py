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

bots = collections.defaultdict(list)

insts = collections.defaultdict(list)

for line in lines:
    # Get all the ones with values
    if line.startswith("value"):
        prts = line.split(" ")
        bots[int(prts[-1])].append(int(prts[1]))

    if line.startswith("bot"):
        prts = line.split(" ")
        insts[int(prts[1])].append(" ".join(prts[2:]))


while True:
    for bot, val in bots.items():
        if len(val) == 2:
            break
    else:
        break
        # raise Error("WTF!")

    # print(bot)

    low, high = min(val), max(val)

    if low == 17 and high == 61:
        print("WE GOT IT", bot)
        break

    assert(len(insts[bot]) == 1)

    for inst in insts[bot]:
        things = parse("gives low to {} and high to {}", inst)
        # print(things)

        lty, ln = things[0].split(" ")
        ln = int(ln)

        rty, rn = things[1].split(" ")
        rn = int(rn)

        # print("Bot {} gives {} to {} and {} to {}".format(bot, low, lty, high, rty))

        if lty == "bot":
            bots[ln].append(low)

        if rty == "bot":
            bots[rn].append(high)

    
    bots[bot] = []

    

# print(bots)
# print(insts)
