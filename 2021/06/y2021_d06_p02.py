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
numbers = [list(map(int, re.findall("-?[0-9]+", line))) for line in lines]


def solve(s):
    l = collections.defaultdict(int)
    for k in s:
        l[k] += 1

    for i in range(256):
        print(i, len(s))
        ll = collections.defaultdict(int)
        for k, v in l.items():
            if k == 0:
                ll[6] += v
                ll[8] += v
            else:
                ll[k-1] += v

        
        # new_fish = []
        # for x in s:
        #     x -= 1
        #     if x == -1:
        #         new_fish.append(6)
        #         new_fish.append(8)
        #     else:
        #         new_fish.append(x)

        l = ll

    return sum(l.values())

nums = numbers[0]
print(solve(nums))

