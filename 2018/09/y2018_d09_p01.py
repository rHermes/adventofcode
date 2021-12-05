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
# INPUT = "".join(fi.input()).rstrip()
# groups = INPUT.split("\n\n")
# lines = list(INPUT.splitlines())
# numbers = [list(map(int, re.findall("[0-9]+", line))) for line in lines]

# for line in lines:
#     gprint(line)

def solve(players, last):
    q = collections.deque([0])
    # print("-", q)
    ps = [0 for _ in range(players)]
    for i in range(1, last+1):

        if i % 23 == 0:
            play = (i-1) % players
            ps[play] += i
            q.rotate(7)
            ps[play] += q.popleft()
        else:
            q.insert(2, i)
            q.rotate(max(-i,-2))

        # wk = q.index(0)
        # q.rotate(-wk)
        # print(i, q)
        # q.rotate(wk)



    return max(ps)

print(solve(479, 71035)) # Real

# print(solve(9,25)) # example?

assert(solve(10, 1618) == 8317)
