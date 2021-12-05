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

def parse(node):
    nchild = node[0]
    nmeta = node[1]
    childs = []

    cc = 2
    for i in range(nchild):
        c = parse(node[cc:])
        childs.append(c)
        cc += c["len"]


    meta = []
    for i in range(nmeta):
        meta.append(node[cc])
        cc += 1

    return {"len": cc, "children": childs, "metas": meta}

def val(node):
    ch = node["children"]
    mt = node["metas"]
    if len(ch) == 0:
        return sum(mt)

    ans = 0
    for m in mt:
        if 0 <= m-1 < len(ch):
            ans += val(ch[m-1])

    return ans


root = parse(numbers[0])
print(val(root))
