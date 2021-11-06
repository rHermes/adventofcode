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

W = 50
H = 6

screen = [[False for _ in range(W)] for _ in range(H)]

def print_screen(screen):
    for row in screen:
        for c in row:
            if c:
                print("#", end="")
            else:
                print(".", end="")
        print("")

for line in lines:
    if line.startswith("rect "):
        a, b = map(int,line[5:].split("x"))
        for y in range(b):
            for x in range(a):
                screen[y][x] = True

    elif line.startswith("rotate column "):
        rest = line[14:]
        first, sec = rest.split(" by ")
        col = int(first[2:])
        shift = int(sec)

        newy = [False for _ in range(H)]
        for y in range(H):
            newy[(y+shift) % H] = screen[y][col]

        for y in range(H):
            screen[y][col] = newy[y]

    elif line.startswith("rotate row "):
        rest = line[len("rotate row "):]
        first, sec = rest.split(" by ")
        row = int(first[2:])
        shift = int(sec)

        newx = [False for _ in range(W)]
        for x in range(W):
            newx[(x + shift) % W] = screen[row][x]

        for x in range(W):
            screen[row][x] = newx[x]

    else:
        print("ERROR: {}".format(line))


    print(line)
    print_screen(screen)

print("final")
print_screen(screen)
ans = 0
for row in screen:
    ans += sum(row)

print(ans)
