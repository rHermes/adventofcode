import fileinput as fi

import re
import itertools as it
import functools as ft

import more_itertools as mit

import math

import collections

import z3

import numpy as np

import string

# findall
# search
# parse
from parse import *

from tqdm import tqdm


def trans(s, n):
    v = 1
    for l in range(n):
        v = (v * s) % 20201227
    return v

# def solve(a, b, M=20201227):
#     v = 1
#     i = 0
#     while v != a and v != b:
#         v = (v*v) % M
#         i += 1

#     if v == a:
#         return pow(b,i,M)
#     else:
#         return pow(a,i,M)

def solve(INPUT):
    groups = INPUT.split("\n\n")
    # print(groups[-1])
    lines = list(INPUT.splitlines())
    
    card = 12232269
    door = 19452773
    for n in tqdm(range(20201227+10)):
        k = pow(7, n, 20201227)
        # print(n, k)
        if k == card:
            print("Card is ", n)
            return pow(door, n, 20201227)
            # card_l = n
        elif k == door:
            print("Door is ", n)
            return pow(card, n, 20201227)

    return None


INPUT = "".join(fi.input()).rstrip()
print(solve(INPUT))
# card = 12232269
# door = 19452773

# print(solve(card,door))
