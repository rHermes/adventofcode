import fileinput as fi
import re
import itertools as it
import functools as ft
import string
import collections as cs
import collections.abc as abc
import math
import sys
import heapq

import typing

# findall, search, parse
from parse import *
import more_itertools as mit
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

positionT = tuple[int,int]
def ortho(y: int, x: int, shape: positionT) -> abc.Iterator[positionT]:
    """Returns all orthagonaly adjacent points, respecting boundary conditions"""
    sy, sx = shape
    if 0 < x: yield (y, x-1)
    if x < sx-1: yield (y, x+1)
    if 0 < y: yield (y-1, x)
    if y < sy-1: yield (y+1, x)

def adj(y: int, x: int, shape: positionT) -> abc.Iterator[positionT]:
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


modules = {}
# modules["output"] = ("output", [])
state = {}
# state["output"] = 0
conj = set()
for line in lines:
    name, we = line.split(" -> ")
    we = we .split(", ")
    if name == "broadcaster":
        modules[name] = ("broadcaster", we)
    elif name[0] == "%":
        modules[name[1:]] = ("flip", we)
        state[name[1:]] = "off"
    elif name[0] == "&":
        modules[name[1:]] = ("conj", we)
        state[name[1:]] = {}
        conj.add(name[1:])
    else:
        print("BIG ERROR")
        print(line)

for c in conj:
    for name, (tp, outputs) in modules.items():
        if c in outputs:
            state[c][name] = "low"

from copy import deepcopy
def step(modules, state, le=0):
    cur = cs.deque([("button", "broadcaster", "low")])
    while cur:
        src, dst, signal = cur.popleft()
        # print(dst, signal)
        if dst == "output":
            continue

        if dst not in modules:
            if dst == "rx":
                if signal == "low":
                    print("WE DID IT IN: {}".format(le))
                    return True

            continue

        tp, outputs = modules[dst]
        if tp == "broadcaster":
            for out in outputs:
                cur.append((dst, out, signal))
        elif tp == "flip":
            if signal == "high":
                continue

            on = state[dst] == "on"
            if state[dst] == "on":
                state[dst] = "off"
                for out in outputs:
                    cur.append((dst, out, "low"))
            else:
                state[dst] = "on"
                for out in outputs:
                    cur.append((dst, out, "high"))

        elif tp == "conj":
            state[dst][src] = signal
            if signal == "low":
                for out in outputs:
                    cur.append((dst, out, "high"))
            else:
                allHigh = all(signal == "high" for _, signal in state[dst].items())
                if dst == "ks" and allHigh:
                    print("It's all high after: {}".format(le))

                if allHigh:
                    for out in outputs:
                        cur.append((dst, out, "low"))
                else:
                    for out in outputs:
                        cur.append((dst, out, "high"))
        else:
            print("BIG ERROR")
    
    return False

# print(state)
# print(modules)

def cycle(modules, state):
    cur = 0
    firstOk = 0
    lastVal = "off"
    lastChange = 0
    nn = "fl"
    while True:
        step(modules, state, cur+1)
        cur += 1

        # if firstOk == 0:
        #     print(state["ms"])
        #     allHigh = all(signal == "high" for _, signal in state["ms"].items())
        #     if allHigh:
        #         print("It t urned on after {} steps".format(firstOk))


        # if firstOk == 0 and state["cm"]["ks"] == "low":
        # if firstOk == 0 and state["xf"]["tc"] == "low":
        # if firstOk == 0 and state["sz"]["ms"] == "low":
        #     firstOk = cur
        #     print("It turned on after {} steps".format(firstOk))
        # if state[nn] != lastVal:
        #     diff = cur - lastChange
        #     lastChange = cur
        #     lastVal = state[nn]
        #     print(nn, "changed to", state[nn], "at", cur, "with diff of", diff)

        # Check if state is back to intial
        # default = True
        # for name, (tp, outs) in modules.items():
        #     if tp == "broadcaster":
        #         continue
        #     elif tp == "flip":
        #         if state[name] == "on":
        #             default = False
        #             break
        #     elif tp == "conj":
        #         if not all(signal == "low" for _, signal in state[name].items()):
        #             default = False
        #             break

        # if default:
        #     break
    
    return 0


# for name, (tp, outs) in modules.items():
#     if tp == "conj":
#         print("{}[label=\"&{}\"]".format(name, name))
#     elif tp == "flip":
#         print("{}[label=\"%{}\"]".format(name, name))
#     for out in outs:
#         print("{} -> {}".format(name, out))
print(cycle(modules, state))

# # def cycle(modules, state):
# le, low, high = 0, 0, 0
# from tqdm import trange
# for i in trange(10000000000):
#     # print(state)
#     w =  step(modules, state, i+1)
#     # print(state)
#     if w:
#         print(i+1)

