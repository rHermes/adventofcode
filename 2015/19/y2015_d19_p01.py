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

reps = collections.defaultdict(set)
for line in groups[0].splitlines():
    i, o = line.split(" => ")
    reps[i].add(o)

# print(reps)

atom = groups[1]
# print(atom)
pos = set()
for i in range(len(atom)):
    # print("before: [{}], cur: [{}], after: [{}]".format(atom[:i], atom[i:], atom[i+1:]))
    before = atom[:i]
    cur = atom[i:]

    for k, repss in reps.items():
        if cur.startswith(k):
            after = atom[i+len(k):]
            for rep in repss:
                pos.add(before + rep + after)


print(len(pos))
