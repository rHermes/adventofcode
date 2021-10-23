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
"children": 3,
"cats": 7,
"samoyeds": 2,
"pomeranians": 3,
"akitas": 0,
"vizslas": 0,
"goldfish": 5,
"trees": 3,
"cars": 2,
"perfumes": 1,
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
        if kk in ind and ind[kk] != vv:
            break
    else:
        print(pnum)
        print(ind)


    # print(ind)
