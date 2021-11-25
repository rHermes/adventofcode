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
INPUT = "".join(fi.input()).rstrip()
groups = INPUT.split("\n\n")
lines = list(INPUT.splitlines())
import copy
def solve(banks):
    banks = copy.deepcopy(banks)
    seen = set()
    
    step = 0

    while True:
        # print(step, banks)
        tb = tuple(banks)
        if tb in seen:
            break
        else:
            seen.add(tb)

        a_max = 0
        i_idx = 0
        for i, a in enumerate(banks):
            if a_max < a:
                a_max = a
                i_idx = i
        
        k = banks[i_idx]
        banks[i_idx] = 0

        while k > 0:
            i_idx = (i_idx + 1) % len(banks)
            banks[i_idx] += 1
            k -= 1
       
        step += 1
        

    # print(step, banks)
    return step


banks = [int(x) for x in lines[0].split("\t")]
print(solve(banks))
