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
def step(modules, state):
    cur = [("button", "broadcaster", "low")]
    newState = deepcopy(state)

    pulses = {"low": 0, "high": 0}

    while cur:
        src, dst, signal = cur.pop(0)
        assert(signal in ["low", "high"])
        pulses[signal] += 1
        # print(dst, signal)
        if dst == "output":
            continue

        if dst not in modules:
            continue

        tp, outputs = modules[dst]
        if tp == "broadcaster":
            for out in outputs:
                cur.append((dst, out, signal))
        elif tp == "flip":
            if signal == "high":
                continue

            on = newState[dst] == "on"
            if newState[dst] == "on":
                newState[dst] = "off"
                for out in outputs:
                    cur.append((dst, out, "low"))
            else:
                newState[dst] = "on"
                for out in outputs:
                    cur.append((dst, out, "high"))

        elif tp == "conj":
            newState[dst][src] = signal

            allHigh = all(signal == "high" for _, signal in newState[dst].items())
            if allHigh:
                for out in outputs:
                    cur.append((dst, out, "low"))
            else:
                for out in outputs:
                    cur.append((dst, out, "high"))
        else:
            print("BIG ERROR")

    return (newState, pulses["low"], pulses["high"])

# print(state)
# print(modules)

def cycle(modules, state):
    le, low, high = 0, 0, 0
    while True:
        state, nl, lh = step(modules, state)
        low += nl
        high += lh
        le += 1

        # Check if state is back to intial
        default = True
        for name, (tp, outs) in modules.items():
            if tp == "broadcaster":
                continue
            elif tp == "flip":
                if state[name] == "on":
                    default = False
                    break
            elif tp == "conj":
                if not all(signal == "low" for _, signal in state[name].items()):
                    default = False
                    break

        if default:
            break

    return le, low, high

# le, low, high = cycle(modules, state)
# print(le, low, high)

# def cycle(modules, state):
le, low, high = 0, 0, 0
for _ in range(1000):
    state, nl, lh = step(modules, state)
    low += nl
    high += lh
    le += 1

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
print(le, low, high)
print(low * high)

