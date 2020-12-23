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

cups = [int(x) for x in lines[0]]
# print(cups)
N = len(cups)

for i in range(100):
    # print("move {}".format(i+1))
    # print(cups)
    cc = cups[0]
    # a, b, c = cups[1], cups[2], cups[3]
    j = cc - 1
    while j not in cups or j in cups[1:4]:
        if j <= 1:
            j = N
        else:
            j -= 1

    # print("Pick up:", cups[1:4])

    dst = cups.index(j)
    # print("dst:", dst)
    # print("{} + {} + {} + {}".format(cups[4:dst+1], cups[1:4], cups[dst+1:] , [cups[0]]))
    cups = cups[4:dst+1] + cups[1:4] + cups[dst+1:] + [cups[0]]
    # print("")

dst = cups.index(1)
wow = cups[dst+1:] + cups[:dst]
print("".join(map(str,wow)))


# print(lines[:-1])
