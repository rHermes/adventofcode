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
import numpy as np
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

def to_pat(desc):
    rows = desc.split("/")
    wow = np.array([[x == '#' for x in y] for y in rows])
    return wow

def from_pat(pat):
    ans = []
    for row in pat:
        ans.append("".join([".#"[bool(x)] for x in row]))

    return "/".join(ans)


def blockshaped(arr, nrows, ncols):
    """
    Return an array of shape (n, nrows, ncols) where
    n * nrows * ncols = arr.size

    If arr is a 2D array, the returned array should look like n subblocks with
    each subblock preserving the "physical" layout of arr.
    """
    h, w = arr.shape
    assert h % nrows == 0, f"{h} rows is not evenly divisible by {nrows}"
    assert w % ncols == 0, f"{w} cols is not evenly divisible by {ncols}"
    return (arr.reshape(h//nrows, nrows, -1, ncols)
               .swapaxes(1,2)
               .reshape(-1, nrows, ncols))

def variants(y):
    w = y
    yield w

    w = np.rot90(w)
    yield w

    w = np.rot90(w)
    yield w

    w = np.rot90(w)
    yield w
    
    w = np.rot90(w)
    w = np.fliplr(w)
    yield w

    w = np.rot90(w)
    yield w

    w = np.rot90(w)
    yield w

    w = np.rot90(w)
    yield w

def step(pats, cur):
    h, w = cur.shape
    if h % 2 == 0:
        nb = h // 2
        news = blockshaped(cur, 2, 2)
    else:
        nb = h // 3
        news = blockshaped(cur, 3, 3)

    gad = [[]]
    for sub in news:
        if len(gad[-1]) == nb:
            gad.append([])
        psub = from_pat(sub)
        gad[-1].append(pats[psub])
        # if psub not in pats:
        #     raise Exception("WTF WE HAVEN'T SEEN THIS")

    # print(gad)
    ged = np.block(gad)
    return ged


def solve(pats):
    cur = np.array([[False, True, False], [False, False, True], [True, True, True]])
    for i in range(18):
        cur = step(pats, cur)

    return sum(sum(cur))

pats = {}

for line in lines:
    src, dst = line.split(" => ")

    psrc = to_pat(src)
    pdst = to_pat(dst)

    for pvar in variants(psrc):
        pats[from_pat(pvar)] = pdst


print(solve(pats))
