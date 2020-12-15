import math
import re

import z3

import fileinput as fi
import itertools as it
import functools as ft

import more_itertools as mit

import collections

# findall
# search
# parse
from parse import *

lines = []

for line in fi.input():
    # w = parse()
    lines.append(line.rstrip())

numbers = [int(x) for x in lines[0].split(",")]

spoken = collections.defaultdict(lambda x: 0)
# spoken2 = collections.defaultdict(lambda x: 0)


i = 1
last = 0
for x in numbers: 
    print(i, x)
    spoken[x] = i
    last = x
    i += 1

while i <= 30000000:
    if last in spoken:
        df = i-1 - spoken[last]
        spoken[last] = i-1
    else:
        spoken[last] = i-1
        df = 0

    # print(i, df)
    last = df
    i += 1

print(last)


