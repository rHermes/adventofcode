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


def find_start(lines):
    x, y = 0, 0
    while lines[y][x] != '|':
        x += 1

    return (x,y)

dirs = {
    "n": (0, -1),
    "e": (1, 0),
    "s": (0, 1),
    "w": (-1, 0)
}

anti = {"n": "s", "e": "w", "s": "n", "w": "e"}

def solve(lines, pt):
    x, y = pt
    d = 's'
    ans = []
    steps = 0
    while lines[y][x] != ' ':
        if lines[y][x] not in "-|+":
            ans.append(lines[y][x])
            print("We reached {}".format(lines[y][x]))

        if lines[y][x] == '+':
            for nd in "nesw":
                if nd == anti[d]:
                    continue

                gx, gy = dirs[nd]
                tx, ty = x + gx, y + gy

                if lines[ty][tx] != ' ':
                    print("We have a new direction: {}".format(nd))
                    d = nd
                    break
            else:
                print("WTF")

        dx, dy = dirs[d]
        x, y = x + dx, y + dy
        steps += 1

    return ("".join(ans), steps)






# Input parsing
lines = list("".join(fi.input()).rstrip("\n").splitlines())

x, y = find_start(lines)
print(solve(lines, (x,y)))
