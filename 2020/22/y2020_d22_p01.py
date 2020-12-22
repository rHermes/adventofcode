import fileinput as fi

import re
import itertools as it
import functools as ft

import more_itertools as mit

import math

import collections

import z3

import numpy as np

# findall
# search
# parse
from parse import *

INPUT = "".join(fi.input())

groups = INPUT.split("\n\n")
# print(groups[-1])
lines = list(INPUT.splitlines())



def zround(a, b):
    aa = a.popleft()
    bb = b.popleft()

    if aa < bb:
        b.append(bb)
        b.append(aa)
    elif bb < aa:
        a.append(aa)
        a.append(bb)

    return (a, b)

def zscore(a):
    ans = 0
    for i,x in enumerate(reversed(a),1):
        ans += i*x
    return ans


# print(groups)

p1d = collections.deque()
for line in groups[0].splitlines()[1:]:
    p1d.append(int(line))

p2d = collections.deque()
for line in groups[1].splitlines()[1:]:
    p2d.append(int(line))



while p1d and p2d:
    # print("P1", p1d)
    # print("P2", p2d)
    p1d, p2d = zround(p1d, p2d)
print(max([zscore(p1d), zscore(p2d)]))
# print("p1d", zscore(p1d))
# print("p2d", zscore(p2d))
