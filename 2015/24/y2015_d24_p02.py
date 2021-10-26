import fileinput as fi
import re
import itertools as it
import functools as ft
import string
import collections
import math
import sys

# findall, search, parse
from parse import *
import more_itertools as mit
import z3
import numpy as np
import lark
import regex

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

packs = set(int(x) for x in lines)

N = sum(packs) // 4

ans = 1e100
for i in range(len(packs)//4 + 2):
    for a in it.combinations(packs, i):
        k = sum(a)
        if k != N:
            continue

        # We prune candidates that will never win
        if math.prod(a) > ans:
            continue


        rest = packs - set(a)
        for j in range(i+1,len(rest)):
            for b in it.combinations(rest, j):
                if sum(b) != N:
                    continue

                rest2 = rest - set(b)

                for c, d in mit.set_partitions(rest2, k=2):
                    if sum(c) != N:
                        continue

                    assert(sum(d) == N)
                    qe = math.prod(a)
                    if ans > qe:
                        ans = qe
                        break
                else:
                    continue

                break
            else:
                continue

            break

    if ans != 1e100:
        break

print(ans)


# for a in mit.powerset(packs:
#     if sum(a) != N:
#         continue

#     print(a)

# for a, b, c in mit.set_partitions(packs, k=3):
#     if sum(a) != sum(b) != sum(c):
#         continue

#     print([a, b, c])
