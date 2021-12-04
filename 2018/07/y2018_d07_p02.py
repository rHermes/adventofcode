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
numbers = [list(map(int, re.findall("[0-9]+", line))) for line in lines]

G = collections.defaultdict(set)
F = collections.defaultdict(set)

for line in reversed(sorted(lines, key=lambda x: x.split(" ")[-3])):
    pr = line.split(" ")
    a, b = pr[1], pr[-3]
    G[b].add(a)
    F[a].add(b)
    if a not in G:
        G[a] = set()

# import graphlib

# ts = graphlib.TopologicalSorter(G)
# print("".join(reversed(list(ts.static_order()))))

# print(G)

N_WORKERS = 5
extra = 60

workers = [[None, 0] for _ in range(N_WORKERS)]
step = 0
seen = set()
inprog = set()
while len(G) > len(seen):
    # We skip this step for the first one
    for worker in workers:
        if worker[0] is None:
            continue

        worker[1] -= 1

        if worker[1] == 0:
            print("At {} seconds we finished {}".format(step, worker[0]))
            seen.add(worker[0])
            worker[0] = None
        elif worker[1] < 0:
            raise Exception("Not popssible!")

    aworkers = [w for w in workers if w[0] is None]


    cands = []
    for k, v in G.items():
        if k in seen|inprog:
            continue
        
        left = v - seen
        if len(left) == 0:
            cands.append(k)

    for w, c in zip(aworkers, sorted(cands)):
        print("At {} seconds we started work on {}".format(step, c))
        w[0] = c
        w[1] = ord(c) - ord('A') + 1 + extra
        inprog.add(c)

    step += 1

print(step-1)

# print("".join(reversed(order)))
# print("".join(order))
