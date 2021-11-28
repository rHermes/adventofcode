import fileinput as fi
import re
import itertools as it
import functools as ft
import string
import collections
import math
import sys
import heapq

# # findall, search, parse
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

# # Input parsing
# INPUT = "".join(fi.input()).rstrip()
# groups = INPUT.split("\n\n")
# lines = list(INPUT.splitlines())

import tqdm
def solve(step):
    Q = collections.deque([0])

    for i in tqdm.trange(1, 50000001):
    # for i in tqdm.trange(1, 2018):
    # for i in range(1, 10):
        Q.rotate(-(step+1))
        Q.appendleft(i)
        # print(i, Q)

    idx = Q.index(0)
    return Q[(idx + 1)%len(Q)]

# print(solve(3)) # test
print(solve(335)) # real
