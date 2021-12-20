import fileinput as fi
import re
import itertools as it
import functools as ft
import string
import collections as cs
import math
import sys
import heapq

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
grid = [[c for c in line] for line in lines]
gsz = (len(grid), len(grid[0]))

def op_addr(regs, a, b, c):
    regs[c] = regs[a] + regs[b]

def op_addi(regs, a, b, c):
    regs[c] = regs[a] + b

def op_mulr(regs, a, b, c):
    regs[c] = regs[a] * regs[b]

def op_muli(regs, a, b, c):
    regs[c] = regs[a] * b

def op_banr(regs, a, b, c):
    regs[c] = regs[a] & regs[b]

def op_bani(regs, a, b, c):
    regs[c] = regs[a] & b

def op_borr(regs, a, b, c):
    regs[c] = regs[a] | regs[b]

def op_bori(regs, a, b, c):
    regs[c] = regs[a] | b

def op_setr(regs, a, b, c):
    regs[c] = regs[a]

def op_seti(regs, a, b, c):
    regs[c] = a

def op_gtir(regs, a, b, c):
    regs[c] = int(regs[b] < a)

def op_gtri(regs, a, b, c):
    regs[c] = int(b < regs[a])

def op_gtrr(regs, a, b, c):
    regs[c] = int(regs[b] < regs[a])

def op_eqir(regs, a, b, c):
    regs[c] = int(a == regs[b])

def op_eqri(regs, a, b, c):
    regs[c] = int(regs[a] == b)

def op_eqrr(regs, a, b, c):
    regs[c] = int(regs[a] == regs[b])

all_ops = {
    "addr": op_addr,
    "addi": op_addi,
    "mulr": op_mulr,
    "muli": op_muli,
    "banr": op_banr,
    "bani": op_bani,
    "borr": op_borr,
    "bori": op_bori,
    "setr": op_setr,
    "seti": op_seti,
    "gtir": op_gtir,
    "gtri": op_gtri,
    "gtrr": op_gtrr,
    "eqir": op_eqir,
    "eqri": op_eqri,
    "eqrr": op_eqrr
}

assert(len(all_ops) == 16)

def pos_ops(case):
    lines = case.splitlines()
    ireg = eval(lines[0].split(": ")[-1])
    code, a, b, c = map(int, lines[1].split())
    oreg = eval(lines[2].split(":  ")[-1])

    pos = set()
    for nm, op in all_ops.items():
        regs = [x for x in ireg]
        op(regs, a, b, c)
        if regs == oreg:
            pos.add(nm)



    return (code, pos)


def solve():
    # regs = {k: 0 for k in range(4)}
    # opcode, two values, outputo
    #       , A and B,  C

    mm = [set(all_ops.keys()) for _ in range(16)]

    for group in groups[:-2]:
        code, pos = pos_ops(group)
        print(code, pos)
        mm[code] &= pos

    print(mm)
    known = {}
    while len(known) < 16:
        # First remove all we know
        for i in range(len(mm)):
            if i in known:
                continue

            mm[i] -= set(known.values())

            if len(mm[i]) == 1:
                known[i] = list(mm[i])[0]

    print(known)

    regs = [0, 0, 0, 0]
    for line in groups[-1].splitlines():
        code, a, b, c = map(int, line.split())
        all_ops[known[code]](regs, a, b, c)

    return regs[0]



            



print(solve())
