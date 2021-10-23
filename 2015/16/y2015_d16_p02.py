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

know = {
    "children": lambda x: x == 3,
    "cats": lambda x: x > 7,
    "samoyeds": lambda x: x == 2,
    "pomeranians": lambda x: x < 3,
    "akitas": lambda x: x == 0,
    "vizslas": lambda x: x == 0,
    "goldfish": lambda x: x < 5,
    "trees": lambda x: x > 3,
    "cars": lambda x: x == 2,
    "perfumes": lambda x: x == 1,
}



for line in lines:
    if not line:
        continue

    pname, things = line.split(":", maxsplit=1)
    pnum = int(pname[4:])
    # print(pname, pnum)

    idents = [x.split(": ") for x in things.strip().split(", ")]
    ind = {k: int(v) for (k, v) in idents if int(v)}

    for kk, vv in know.items():
        if kk in ind and not vv(ind[kk]):
            break
    else:
        print(pnum)
        print(ind)


    # print(ind)
