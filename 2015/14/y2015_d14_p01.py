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

def calc(speed, act, rest, n=2503):
    dist = 0
    sec = 0
    while sec < n:
        i = 0
        while i < act and sec < n:
            dist += speed
            i += 1
            sec += 1
        
        sec += rest

    return dist

print("Comet: {}".format(calc(14, 10, 127, n=10)))
print("Comet: {}".format(calc(14, 10, 127, n=1000)))
print("Dancer: {}".format(calc(16, 11, 162, n=10)))
print("Dancer: {}".format(calc(16, 11, 162, n=1000)))

dists = []
for line in lines:
    # print(line)
    # print(parse("{} can fly {:d} km/s for {:d} seconds, but then must rest for {:d} seconds.", line))
    name, speed, act, rest = parse("{} can fly {:d} km/s for {:d} seconds, but then must rest for {:d} seconds.", line)
    # print("{}: {}", name, calc(speed, act, rest))
    dists.append((calc(speed, act, rest), name))

print(dists)
print(max(dists))


