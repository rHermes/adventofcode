import fileinput as fi

import re
import itertools as it
import functools as ft

import more_itertools as mit

import math

import collections

import z3

import numpy as np

import string

# findall
# search
# parse
from parse import *

import lark
import regex

INPUT = "".join(fi.input()).rstrip()

groups = INPUT.split("\n\n")
# print(groups[-1])
lines = list(INPUT.splitlines())

def goodstring(s):
    for i in range(len(s)-2):
        if s[i] == s[i+2]:
            break
    else:
        return False

    for i in range(len(s)-3):
        for j in range(i+2, len(s)-1):
            if s[i] == s[j] and s[i+1] == s[j+1]:
                break
        else:
            continue

        break
    else:
        return False

    return True

ans = 0
for line in lines:
    good = goodstring(line)
    if good:
        ans += 1

print(ans)
