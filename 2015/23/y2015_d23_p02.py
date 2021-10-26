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

reg = {"a": 1, "b": 0}

i = 0
while i < len(lines):
    de = lines[i].split()

    if de[0] == "hlf":
        reg[de[1]] //= 2
        i += 1

    if de[0] == "tpl":
        reg[de[1]] *= 3
        i += 1

    if de[0] == "inc":
        reg[de[1]] += 1
        i += 1

    if de[0] == "jmp":
        i += int(de[1])

    if de[0] == "jie":
        if reg[de[1][0]] % 2 == 0:
            i += int(de[2])
        else:
            i += 1

    if de[0] == "jio":
        if reg[de[1][0]] == 1:
            i += int(de[2])
        else:
            i += 1


        
print(reg["b"])
