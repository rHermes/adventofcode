import fileinput as fi
import re
import itertools as it
import functools as ft
import string
import collections as cs
import collections.abc as abc
import math
import sys
import heapq

import typing

# findall, search, parse
from parse import *
import more_itertools as mit
# import z3
# import numpy as np
# import lark
# import regex
# import intervaltree as itree
from bidict import bidict
import tqdm

# print(sys.getrecursionlimit())
sys.setrecursionlimit(6500)

# Debug logging
DEBUG = False
def gprint(*args, **kwargs):
    if DEBUG: print(*args, **kwargs)

positionT = tuple[int,int]
def ortho(y: int, x: int, shape: positionT) -> abc.Iterator[positionT]:
    """Returns all orthagonaly adjacent points, respecting boundary conditions"""
    sy, sx = shape
    if 0 < x: yield (y, x-1)
    if x < sx-1: yield (y, x+1)
    if 0 < y: yield (y-1, x)
    if y < sy-1: yield (y+1, x)

def adj(y: int, x: int, shape: positionT) -> abc.Iterator[positionT]:
    """Returns all points around a point, given the shape of the array"""
    sy, sx = shape
    for dy,dx in it.product([-1,0,1], [-1,0,1]):
        if dy == 0 and dx == 0:
            continue

        py = y + dy
        px = x + dx

        if 0 <= px < sx and 0 <= py < sy:
            yield (py,px)


# Input parsing
INPUT = "".join(fi.input()).rstrip()
groups = INPUT.split("\n\n")
lines = list(INPUT.splitlines())
numbers = [list(map(int, re.findall("-?[0-9]+", line))) for line in lines]
pos_numbers = [list(map(int, re.findall("[0-9]+", line))) for line in lines]
grid = [[c for c in line] for line in lines]
gsz = (len(grid), len(grid[0]))

def solve():
    nums = []

    # orig_spot -> now_spot
    stored = bidict()
    for (i,line) in enumerate(lines):
        nums.append(int(line))
        stored[i] = i
    
    orig_nums = tuple(nums)
    N = len(orig_nums)
    for orig_spot, num in tqdm.tqdm(enumerate(orig_nums), total=len(orig_nums)):
        # now_lineup = [orig_nums[stored.inverse[i]] for i in range(0, len(orig_nums))]
        # gprint(now_lineup)

        if num < 0:
            rem = num
            while rem < 0:
                if stored[orig_spot] == 1: # special case
                    target = N-1
                    my_orig = stored.pop(orig_spot)
                    for i in range(my_orig+1, target+1):
                        adx = stored.inverse[i]
                        stored[adx] -= 1

                    stored[orig_spot] = target

                elif stored[orig_spot] == 0: # special case
                    cur_spot = stored.pop(orig_spot)
                    target_orig = stored.inverse.pop(N-1)
                    stored[target_orig] = cur_spot
                    stored[orig_spot] = N-1

                else:
                    cur_spot = stored.pop(orig_spot)
                    target_orig = stored.inverse.pop(cur_spot-1)
                    stored[target_orig] = cur_spot
                    stored[orig_spot] = cur_spot-1

                
                rem += 1
        elif num == 0:
            pass
        else:
            rem = num
            while 0 < rem:
                if stored[orig_spot] == N-1:
                    cur_spot = stored.pop(orig_spot)
                    for i in reversed(range(1, cur_spot)):
                        adx = stored.inverse[i]
                        stored[adx] += 1

                    stored[orig_spot] = 1

                else:
                    cur_spot = stored.pop(orig_spot)
                    target_orig = stored.inverse.pop(cur_spot+1)
                    stored[target_orig] = cur_spot
                    stored[orig_spot] = cur_spot+1
                # now_lineup = [orig_nums[stored.inverse[i]] for i in range(0, len(orig_nums))]
                # print(now_lineup)



                rem -= 1

        # now_lineup = [orig_nums[stored.inverse[i]] for i in range(0, len(orig_nums))]
        # gprint(now_lineup)
        # gprint("")


    # now_lineup = [orig_nums[stored.inverse[i]] for i in range(0, len(orig_nums))]
    # print(now_lineup)
    pwd = orig_nums.index(0)
    cur_idx_zero = stored[pwd]
    # print(cur_idx_zero)
    # print(orig_nums[stored.inverse[(cur_idx_zero + 1000) % len(orig_nums)]])
    # print(orig_nums[stored.inverse[(cur_idx_zero + 2000) % len(orig_nums)]])
    # print(orig_nums[stored.inverse[(cur_idx_zero + 3000) % len(orig_nums)]])
    ans = sum(orig_nums[stored.inverse[(cur_idx_zero + i) % len(orig_nums)]] for i in [1000, 2000, 3000])
    return ans





print(solve())
