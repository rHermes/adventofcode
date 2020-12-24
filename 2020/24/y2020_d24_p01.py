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

import redblob


e, se, sw, w, nw, ne = [0,1,2,3,4,5]

dirs = {"e": 0, "se": 1, "sw": 2, "w": 3, "nw": 4, "ne": 5}

def solve(INPUT):
    groups = INPUT.split("\n\n")
    # print(groups[-1])
    lines = list(INPUT.splitlines())

    # print(INPUT)
    # print(groups)


    dd = collections.defaultdict(int)
    for line in lines:
        # print(line)
        a = redblob.Hex(0,0,0)
        # dd[a] += 1
        south = False
        north = False
        for c in line:
            if c == "s":
                south = True
            elif c == "n":
                north = True
            elif c == "e":
                if south:
                    south = False
                    a = redblob.hex_neighbor(a, se)
                    # dd[a] += 1
                elif north:
                    north = False
                    a = redblob.hex_neighbor(a, ne)
                    # dd[a] += 1
                else:
                    a = redblob.hex_neighbor(a, e)
                    # dd[a] += 1
            elif c == "w":
                if south:
                    south = False
                    a = redblob.hex_neighbor(a, sw)
                    # dd[a] += 1
                elif north:
                    north = False
                    a = redblob.hex_neighbor(a, nw)
                    # dd[a] += 1
                else:
                    a = redblob.hex_neighbor(a, w)


        dd[a] += 1
    flipped = 0
    for k, v in dd.items():
        if v % 2:
            flipped += 1
        # print("WOW")
    # print(dd)
    return flipped


INPUT = "".join(fi.input()).rstrip()
print(solve(INPUT))
