import fileinput as fi

import re
import itertools as it
import functools as ft

import more_itertools as mit

import math

import collections

import numpy as np

# import z3

# findall
# search
# parse
from parse import *

INPUT = "".join(fi.input())

groups = INPUT.split("\n\n")
lines = list(INPUT.splitlines())


rules = []
for line in lines:
    if not line:
        break
    a, b = line.split(" (contains ")
    a = a.split()
    b = b[:-1].split(", ")
    rules.append((a,b))


all_foods = set()
all_algs = set()
times = {}
for foods, algs in rules:
    for food in foods:
        times[food] = times.get(food,0) + 1
        all_foods.add(food)

    for alg in algs:
        all_algs.add(alg)

# print(rules)

# print(all_algs)
ans = {alg: None for alg in all_algs}

for alg in all_algs:
    for foods, algs in rules:
        if alg in algs:
            if not ans[alg]:
                ans[alg] = set(foods)
            else:
                ans[alg] &= set(foods)

# print(ans)

maybe_alg = all_foods.copy()
for alg, foods in ans.items():
    maybe_alg -= foods

# print(maybe_alg)
# print(len(maybe_alg))


gans = {}
taken = set()

while True:
    for alg, foods in ans.items():
        if len(foods - taken) == 1:
            gans[alg] = list(foods-taken)[0]
            taken.add(gans[alg])
            break
    else:
        break


items = [(alg,food) for alg, food in gans.items()]
items = sorted(items)
print(",".join([x[1] for x in items]))
# print(",".join(sorted(gans.keys())))
# rans = 0
# for food in maybe_alg:
#     rans += times[food]

# print(rans)
