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

def knot_hash(ins, ar, cur, skip):
    # ar = list(range(256))
    # ar = list(range(5))

    bw = collections.deque(ar)
    bw.rotate(-cur)
    ar = list(bw)

    for l in ins:
        assert(l < len(ar))
        ar[:l] = ar[:l][::-1]
        bw = collections.deque(ar)
        bw.rotate(-(l + skip))
        # cur = (cur + l + skip) % len(ar)
        cur += l + skip
        ar = list(bw)
        skip += 1

    # We must rewind it
    bw = collections.deque(ar)
    bw.rotate(cur)
    return list(bw), cur, skip

def solve(inp):
    cur = 0
    skip = 0
    anp = [ord(x) for x in inp] + [17, 31, 73, 47, 23]
    # anp = [3, 4, 1, 5, 17, 31, 73, 47, 23]

    ar = list(range(256))
    for i in range(64):
        print(i, cur, skip)
        ar, cur, skip = knot_hash(anp, ar, cur, skip)
   
    # print(ar)
    dense_hash = []
    cur_hash = []
    print(ar)
    for x in ar:
        cur_hash.append(x)
        if len(cur_hash) == 16:
            z = 0
            for y in cur_hash:
                z ^= y

            dense_hash.append(z)
            cur_hash = []

    print(cur_hash)
    wew = ["{:02x}".format(x) for x in dense_hash]
    print(wew)
    wow = "".join(["{:02x}".format(x) for x in dense_hash])
    print(wow)
    assert(len(wow) == 32)
    return wow


# print(knot_hash([3, 4, 1, 5]))
inp = "187,254,0,81,169,219,1,190,19,102,255,56,46,32,2,216"
# inp = "AoC 2017"
# inp = "1,2,3"
# inp = "1,2,4"
# inp = ""

print(solve(inp))
