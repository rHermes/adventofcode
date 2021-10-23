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

INPUT = "".join(fi.input()).rstrip()

groups = INPUT.split("\n\n")
# print(groups[-1])
lines = list(INPUT.splitlines())

nums = [int(x) for x in lines]

ans = 0
for i in range(len(nums)):
    for co in it.combinations(nums, r=i):
        if sum(co) == 150:
            ans += 1
print(ans)
