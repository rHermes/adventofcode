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
numbers = [list(map(int, re.findall("-?[0-9]+", line))) for line in lines]

carts = []
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c in "^v<>":
            carts.append((y,x,0,c))

print(carts)

for y,x, _, c in carts:
    wl = list(lines[y])
    wl[x] = {"<": "-", ">": "-", "v": "|", "^": "|"}[c]
    lines[y] = "".join(wl)


def print_track(lines, carts):
    nl = [x for x in lines]
    for y,x, _, c in carts:
        wl = list(nl[y])
        wl[x] = c
        nl[y] = "".join(wl)

    print("\n".join(nl))

DIR = {"^": (-1,0), "v": (1,0), ">": (0,1), "<": (0,-1)}
ts = 0
# print("\n".join(lines))

done = False
while len(carts) > 1:
    seen = set()
    for y, x, _, _ in carts:
        seen.add((y,x))

    # print(ts)
    # print_track(lines, carts)
    # print(ts, carts)
    to_remove = set()
    carts = sorted(carts)
    for i in range(len(carts)):
        y, x, gen, c = carts[i]

        if c == 'v' and lines[y][x] == '\\':
            c = ">"
        elif c == '<' and lines[y][x] == '\\':
            c = "^"
        elif c == '>' and lines[y][x] == '\\':
            c = "v"
        elif c == '^' and lines[y][x] == '\\':
            c = "<"
        elif c == ">" and lines[y][x] == '/':
            c = "^"
        elif c == "v" and lines[y][x] == '/':
            c = '<'
        elif c == "<" and lines[y][x] == '/':
            c = 'v'
        elif c == "^" and lines[y][x] == '/':
            c = '>'
        elif lines[y][x] == "+":
            if gen == 0:
                if c == "^":
                    c = "<"
                elif c == ">":
                    c = "^"
                elif c == "v":
                    c = ">"
                else:
                    c = "v"
            elif gen == 2:
                if c == "^":
                    c = ">"
                elif c == ">":
                    c = "v"
                elif c == "v":
                    c = "<"
                else:
                    c = "^"

            gen = (gen+1) % 3

        seen.remove((y,x))
        dy, dx = DIR[c]
        y += dy
        x += dx

        if (y,x) in seen:
            print("We have a crash at {} at: {},{}".format(ts, x,y))
            to_remove.add(i)
            for j, (py,px, _, _) in enumerate(carts):
                if py == y and px == x:
                    to_remove.add(j)
        else:
            seen.add((y,x))

        carts[i] = (y,x,gen,c)

    for j in reversed(sorted(to_remove)):
        print("We deleted {} at {}".format(j, ts))
        del carts[j]

    ts += 1

print("{},{}".format(carts[0][1],carts[0][0]))
