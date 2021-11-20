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
    elves = [(x,1) for x in range(n)]
    
    idx = 0
    while True:
        # print(idx)
        nm, pres = elves[idx]
        if pres == 0:
            idx = (idx + 1) % n
            continue

        adx = (idx + 1) % n
        adx = (idx + 1) % n
        while adx != idx:
            # print(wow)
            # print(adx)
            anm, apres = elves[adx]
            if apres == 0:
                adx = (adx + 1) % n
                continue

            elves[idx] = (nm, pres+apres)
            elves[adx] = (anm, 0)
            break
        else:
            return 1+nm

        idx = (idx + 1) % n




print(solve(5))
print(solve(3001330))
