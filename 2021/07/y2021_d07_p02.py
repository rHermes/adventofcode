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


def subsolve():
    pass


def solve(nums):
    ans = 1000000000000000
    best_i = 0
    for i in range(min(nums), max(nums)+1):
        print(i)
        w = sum(sum(range(1,abs(i - x)+1)) for x in nums)
        if w < ans:
            ans = w
            best_i = i

    return (ans, best_i)


print(solve(list(map(int,lines[0].split(",")))))
