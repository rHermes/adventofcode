import fileinput as fi
# import re
# import itertools as it
# import functools as ft
# import string
# import collections
# import math
# import sys

# # findall, search, parse
# from parse import *
# import more_itertools as mit
# import z3
# import numpy as np
# import lark
# import regex

# print(sys.getrecursionlimit())
# sys.setrecursionlimit(6500)

# Debug logging
DEBUG = True
def gprint(*args, **kwargs):
    if DEBUG: print(*args, **kwargs)

# # Input parsing
# INPUT = "".join(fi.input()).rstrip()
# groups = INPUT.split("\n\n")
# lines = list(INPUT.splitlines())

def solve(n):
    elves = [x+1 for x in range(n)]

    idx = 0
    while len(elves) > 3:
        if len(elves) % 1000 == 0:
            print(len(elves))

        # next val
        vali = elves[(idx + 1) % len(elves)]
        adx = (idx + len(elves)//2) % len(elves)
        # print("{} removes {}".format(elves[idx], elves[adx]))
        # idx = (idx + 1) % len(elves)
        del elves[adx]
        idx = elves.index(vali)
        # idx = (idx + 1) % len(elves)

    # print(elves, idx)
    return elves[(idx-1) % len(elves)]

    # return elves[0]



# print(solve(5))
# print(solve(3001330))
# print(solve(3001330))
for i in range(1,100):
    print("{}: {}".format(i, solve(i)))
