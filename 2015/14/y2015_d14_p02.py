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
    dist = [0]
    sec = 0
    while sec < n:
        i = 0
        while i < act and sec < n:
            dist.append(dist[-1] + speed)
            i += 1
            sec += 1
        
        j = 0
        while j < rest and sec < n:
            dist.append(dist[-1])
            j += 1
            sec += 1

    return dist[1:]


def points(speeds):
    pnts = [0 for _ in speeds]
    for jj, x in enumerate(zip(*speeds)):
        mm = max(x)
        for i, y in enumerate(x):
            if y == mm:
                pnts[i] += 1
        # print("For {} we have {} with max {} and pnts {}".format(jj+1, x, mm, pnts))

    return pnts

nn = 150
speeds = [calc(14, 10, 127, n=1000), calc(16, 11, 162, n=1000)]

print(points(speeds))
# print("Comet: {}".format(calc(14, 10, 127, n=10)))
# print("Comet: {}".format(calc(14, 10, 127, n=1000)))
# print("Dancer: {}".format(calc(16, 11, 162, n=10)))
# print("Dancer: {}".format(calc(16, 11, 162, n=1000)))

dists = []

speeds = []
names = []
for line in lines:
    # print(line)
    # print(parse("{} can fly {:d} km/s for {:d} seconds, but then must rest for {:d} seconds.", line))
    name, speed, act, rest = parse("{} can fly {:d} km/s for {:d} seconds, but then must rest for {:d} seconds.", line)
    # print("{}: {}", name, calc(speed, act, rest))
    names.append(name)
    speeds.append(calc(speed, act, rest))

pts = points(speeds)
print(max(pts))
