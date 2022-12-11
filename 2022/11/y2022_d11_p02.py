import fileinput as fi
import re
import itertools as it
import functools as ft
import string
import collections as cs
import math
import sys
import heapq

import tqdm
# findall, search, parse
# from parse import *
# import more_itertools as mit
# import z3
# import numpy as np
# import lark
# import regex
# import intervaltree as itree
# from bidict import bidict

# print(sys.getrecursionlimit())
sys.setrecursionlimit(6500)

# Debug logging
DEBUG = True
def gprint(*args, **kwargs):
    if DEBUG: print(*args, **kwargs)

def ortho(y, x, shape):
    """Returns all orthagonaly adjacent points, respecting boundary conditions"""
    sy, sx = shape
    if 0 < x: yield (y, x-1)
    if x < sx-1: yield (y, x+1)
    if 0 < y: yield (y-1, x)
    if y < sy-1: yield (y+1, x)

def adj(y, x, shape):
    """Returns all points around a point, given the shape of the array"""
    sy, sx = shape
    for dy,dx in it.product([-1,0,1], [-1,0,1]):
        if dy == 0 and dx == 0:
            continue

        py = y + dy
        px = x + dx

        if 0 <= px < sx and 0 <= py < sy:
            yield (py,px)


# Input parsing
INPUT = "".join(fi.input()).rstrip()
groups = INPUT.split("\n\n")
lines = list(INPUT.splitlines())
numbers = [list(map(int, re.findall("-?[0-9]+", line))) for line in lines]
pos_numbers = [list(map(int, re.findall("[0-9]+", line))) for line in lines]
grid = [[c for c in line] for line in lines]
gsz = (len(grid), len(grid[0]))

def one_round(inspects,monkeys, maxm):
    for i in range(len(monkeys)):
       # print("Monkey {}".format(i))
       items, op_str, divt, true_monkey, false_monkey = monkeys[i]
       for item in items:
           inspects[i] += 1
           # print("  Monkey inspects an item with a worry level of {}.".format(item))
           old = item
           neww = eval(op_str) % maxm
           if neww % divt == 0:
               monkeys[true_monkey][0].append(neww)
           else:
               monkeys[false_monkey][0].append(neww)

       monkeys[i][0].clear()
       # monkeys[i] = ([], op_str, divt, true_monkey, false_monkey)

        


def solve():
    monkeys = []
    for group in groups:
        lines = group.splitlines()
        # id = int(parse("Monkey {:d}:", lines[0])[0]
        start_items = [int(x) for x in lines[1][len("  Starting items: "):].split(",")]
        op_str = lines[2][len("  Operation: new = "):]
        divt = int(lines[3].split()[-1])
        true_monkey = int(lines[4].split()[-1])
        false_monkey = int(lines[5].split()[-1])
        monkeys.append((start_items, op_str, divt, true_monkey, false_monkey))
        # print(id)
        # print(start_items)
        # print(op_str)
        # print(divt)
        # print(lines[1].split())
        # print(id)

    maxm = 1
    for monkey in monkeys:
        maxm *= monkey[2]
  
    for i in range(len(monkeys)):
        print("Monkey {}: {}".format(i, ",".join([str(x) for x in monkeys[i][0]])))

    inspects = [0 for _ in monkeys]

    for _ in tqdm.trange(10000):
        one_round(inspects, monkeys, maxm)

    ww = list(sorted(inspects))
    a, b = ww[-2:]
    return a * b

    print(inspects)

    for i in range(len(monkeys)):
        print("Monkey {}: {}".format(i, ",".join([str(x) for x in monkeys[i][0]])))


print(solve())
