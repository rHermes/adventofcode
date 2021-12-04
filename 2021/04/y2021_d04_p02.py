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

for line in lines:
    print(line)

order = [int(x) for x in groups[0].split(",")]

boards = []
for st in groups[1:]:
    nams = [list(map(int, re.findall("[0-9]+", line))) for line in st.splitlines()]
    boards.append(nams)



def check_done(board, got):
    for row in board:
        if all(x in got for x in row):
            return True
    
    for x in range(len(board[1])):
        if all(row[x] in got for row in board):
            return True

    return False



def solve(order, boards):
    got = set()
    for i, x in enumerate(order):
        got.add(x)

        to_del = []
        for j, board in enumerate(boards):
            if check_done(board, got):
                if len(boards) == 1:
                    a = sum(set(it.chain.from_iterable(board)) - got)
                    return a * x
                else:
                    to_del.append(j)

        for j in reversed(to_del):
            del boards[j]

print(solve(order, boards))
