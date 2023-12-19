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

workflows = {}
for line in groups[0].splitlines():
    line = line.rstrip()
    # print(line)
    name, rr = line.split("{")
    #                      }
    rr = rr[:-1]
    # print(name)
    chain = []
    for rv in rr.split(","):
        chain.append(rv)

    workflows[name] = chain

# print(workflows)
def valid(workflows, vals):
    beg = "in"
    # print(beg)

    while True:
        # print(beg, vals)
        chain = workflows[beg]
        for line in chain:
            if ":" not in line:
                beg = line
                break
            
            cond, dest = line.split(":")
            if "<" in cond:
                reg, val = cond.split("<")
                bv = {"x": 0, "m": 1, "a": 2, "s": 3}
                ourval = vals[bv[reg]]
                if ourval < int(val):
                    beg = dest
                    break
            elif ">" in cond:
                reg, val = cond.split(">")
                bv = {"x": 0, "m": 1, "a": 2, "s": 3}
                ourval = vals[bv[reg]]
                if ourval > int(val):
                    beg = dest
                    break



                


        if beg == "R":
            return False
        elif beg == "A":
            return True


def evalt(workflows, rest, beg="in"):
    # print(beg, rest)
    minx, maxx, minm, maxm, mina, maxa, mins, maxs = rest
    
    # If any of these overlap, we are not good
    if maxx <= minx or maxm <= minm or maxa <= mina or maxs <= mins:
        print("We hot")
        return []

    if beg == "R":
        return []

    if beg == "A":
        return [rest]

    rst = {
            "x": (minx, maxx),
            "m": (minm, maxm),
            "a": (mina, maxa),
            "s": (mins, maxs)
        }

    # print(beg)
    pos = []

    chain = workflows[beg]

    for line in chain:
        if ":" not in line:
            gvs = (*rst["x"], *rst["m"], *rst["a"], *rst["s"])
            pos.extend(evalt(workflows, gvs, beg=line))
            continue


        cond, dest = line.split(":")
        if "<" in cond:
            reg, val = cond.split("<")
            val = int(val)

            gmin, gmax = rst[reg]
            rst[reg] = (gmin, min(gmax, val))
            gvs = (*rst["x"], *rst["m"], *rst["a"], *rst["s"])
            pos.extend(evalt(workflows, gvs, beg=dest))

            rst[reg] = (max(gmin,val-1), gmax)
        elif ">" in cond:
            reg, val = cond.split(">")
            val = int(val)

            gmin, gmax = rst[reg]
            rst[reg] = (max(gmin, val), gmax)
            gvs = (*rst["x"], *rst["m"], *rst["a"], *rst["s"])
            pos.extend(evalt(workflows, gvs, beg=dest))

            rst[reg] = (gmin, min(gmax, val+1))



    return pos                


NG = 4000
# NG = 40
goods = evalt(workflows, (0, NG+1, 0, NG+1, 0, NG+1, 0, NG+1))
ans = 0
for minx, maxx, minm, maxm, mina, maxa, mins, maxs in goods:
    # print("WOW")
    # print(minx, maxx, minm, maxm, mina, maxa, mins, maxs)
    ans += (maxx - minx - 1) * (maxm - minm - 1) * (maxa - mina - 1) * (maxs - mins - 1)
    # for x in range(minx+1, maxx):
    #     for m in range(minm+1, maxm):
    #         for a in range(mina+1, maxa):
    #             for s in range(mins+1, maxs):
    #                 if not valid(workflows, (x, m, a, s)):
    #                     print(x, m, a, s)

print(ans)
