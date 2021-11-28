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
from parse import *
import more_itertools as mit
import z3
import numpy as np
import lark
import regex
import intervaltree as itree

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

GEN_A_FAC = 16807
GEN_B_FAC = 48271

MOD = 2147483647

def step(cur, fac):
    return (cur*fac) % MOD

def comp(a, b):
    mask = 0b1111_1111_1111_1111
    return (a & mask) == (b & mask)

def gen_a(cur):
    while True:
        cur = (cur*GEN_A_FAC) % MOD
        if cur % 4 == 0:
            yield cur

def gen_b(cur):
    while True:
        cur = (cur*GEN_B_FAC) % MOD
        if cur % 8 == 0:
            yield cur


import tqdm
def solve(a, b):
    ga = gen_a(a)
    gb = gen_b(b)
    cnt = 0
    for i, ac, bc in zip(tqdm.trange(5_000_000), ga, gb):
        if comp(ac, bc):
            cnt += 1

    return cnt






# print(solve(65, 8921)) # test
print(solve(699, 124)) # real
