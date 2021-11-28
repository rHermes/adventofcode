import fileinput as fi
import re
import itertools as it
import functools as ft
import string
import collections
import math
import sys
import heapq

# findall, search, parse
# from parse import *
import more_itertools as mit
# import z3
# import numpy as np
# import lark
# import regex
# import intervaltree as itree

# print(sys.getrecursionlimit())
sys.setrecursionlimit(6500)

# Debug logging
DEBUG = True
def gprint(*args, **kwargs):
    if DEBUG: print(*args, **kwargs)

# Input parsing
INPUT = "".join(fi.input()).rstrip()
groups = INPUT.split("\n\n")
lines = list(INPUT.splitlines())

def step(par):
    p, v, a = par
    px, py, pz = p
    vx, vy, vz = v
    ax, ay, az = a
    
    vx += ax
    vy += ay
    vz += az

    px += vx
    py += vy
    vz += vz

    return ((px, py, pz), (vx, vy, vz), (ax, ay, az))

def dist(par):
    return abs(par[0][0]) + abs(par[0][1]) + abs(par[0][2])

pars = []
for line in lines:
    p, v, a = line.split(", ")
    px, py, pz = map(int, p[3:-1].split(","))
    vx, vy, vz = map(int, v[3:-1].split(","))
    ax, ay, az = map(int, a[3:-1].split(","))
    p = (px, py, pz)
    v = (vx, vy, vz)
    a = (ax, ay, az)
    par = (p ,v, a)
    pars.append(par)


for i, par in enumerate(pars):
    p, v, a = par

    ax, ay, az = a

    score = abs(ax) + abs(ay) + abs(az)

    print("{} scores: {}".format(i, score))

    



# import tqdm
# prev_best = None
# for i in tqdm.trange(1000000):
#     pars = [step(par) for par in pars]
#     best_par = None
#     min_distance = 1000000000000000000000000000000000
#     for j, par in enumerate(pars):
#         dp = dist(par)
#         if dp < min_distance:
#             min_distance = dp
#             best_par = j

#     if prev_best != best_par:
#         tqdm.write("Iteration {} gives best {} for par {}".format(i, min_distance, best_par))
#         prev_best = best_par



