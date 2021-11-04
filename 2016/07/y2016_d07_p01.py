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

for line in lines:
    # gprint(line)

    for match in re.findall(r"([a-z])([a-z])\2\1", line):
        a, b = match
        if a != b:
            break
    else:
        continue


    for match in re.findall(r"\[[^]]*([a-z])([a-z])\2\1[^]]*\]", line):
        a, b = match
        if a != b:
            break
    else:
        print(line)
    
    # print(line)
