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
    reps[o].add(i)

# print(reps)

final_atom = "e"
start_atom = groups[1]
# print(atom)


def newpos_rep(atom):
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

    return pos

lens = {start_atom: 0}
pos = set([start_atom])

# max_len = -1
max_len = 100000000000000000

while len(pos) > 0:
    # we find the pos with the smallest current length.
    min_key = None
    min_val = 10000000000000000000000
    for k in pos:
        # val = lens[k]
        val = len(k)
        if val < min_val:
            min_key = k
            min_val = val


    # if min_val > max_len:
    if min_val < max_len:
        max_len = min_val
        print("new max depth: {}: {}".format(max_len, min_key))

    pos.remove(min_key)
    # Remove from the heap
    # if max_len < 25:
    #     print("we are doing {} with len {}".format(min_key, min_val))

    new_pos = newpos_rep(min_key)
    for pp in new_pos:
        if pp == final_atom:
            print(lens[min_key] + 1)
            pos.clear()
            break
        if pp in lens:
            continue
        else:
            lens[pp] = lens[min_key] + 1
            pos.add(pp)
