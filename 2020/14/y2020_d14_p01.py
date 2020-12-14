import fileinput as fi
import itertools as it
import collections
import functools as ft


import more_itertools as mit

# findall
# search
# parse
from parse import *


lines = []
for l in fi.input():
    if l.rstrip():
        lines.append(l.rstrip())

mem = {}

mask_and = 0
mask_or = 0

for line in lines:
    if line.startswith("mask = "):
        k = parse("mask = {}", line)[0]
        mask_and = 0
        mask_or = 0
        for i, c in enumerate(reversed(k)):
            if c == '1':
                mask_or |= 1 << i
                mask_and |= 1 << i
            elif c == 'X':
                mask_and |= (1 << i)
    else:
        k, y = list(parse("mem[{:d}] = {:d}", line))
        mem[k] = (y & mask_and) | mask_or

print(sum(mem.values()))
