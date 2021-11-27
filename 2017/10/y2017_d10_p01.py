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

# Input parsing
# INPUT = "".join(fi.input()).rstrip()
# groups = INPUT.split("\n\n")
# lines = list(INPUT.splitlines())

def knot_hash(ins):
    ar = list(range(256))
    # ar = list(range(5))
    c = 0
    skip = 0
    cur = 0
    for l in ins:
        ar[:l] = ar[:l][::-1]
        bw = collections.deque(ar)
        bw.rotate(-(l + skip))
        cur += l + skip
        ar = list(bw)
        skip += 1

    # We must rewind it
    bw = collections.deque(ar)
    bw.rotate(cur)
    return list(bw)

# print(knot_hash([3, 4, 1, 5]))
al = knot_hash([187,254,0,81,169,219,1,190,19,102,255,56,46,32,2,216])
print(al)
print(al[0] * al[1])
# for line in lines:
#     gprint(line)
