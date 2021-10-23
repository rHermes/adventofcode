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

INPUT = "".join(fi.input()).rstrip()

groups = INPUT.split("\n\n")
# print(groups[-1])
lines = list(INPUT.splitlines())


def get_combs(left, n, tabs=0):
    # print("{}called with {} {}".format(" "*tabs, left, n))
    if n == 1:
        yield [left]
        return


    for x in range(left+1):
        for y in get_combs(left-x, n-1, tabs=tabs+1):
            yield [x] + y


def calc_score(times, ings):
    s = [0 for _ in ings[0]]
    for time, ing in zip(times, ings):
        for i in range(len(s)):
            s[i] += time*ing[i]

    l = 1
    for xx in s:
        l *= max(xx,0)

    return l



# print(lines)
xs = []
for line in lines:
    if not line:
        continue

    things = line.split(", ")
    xx = [int(x.split()[-1]) for x in things]
    xs.append(xx[:-1])

# print(xs)

ans = None
for x in get_combs(100, len(xs)):
    sco = calc_score(x, xs)
    if ans is None:
        ans = sco
    elif ans < sco:
        ans = sco

    # print(x, sco)

print(ans)
