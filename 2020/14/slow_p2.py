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
    else:
        break

mem = {}


mask_or = 0
mask_float = []

for line in lines:
    if line.startswith("mask = "):
        k = parse("mask = {}", line)[0]
        mask_or = 0
        mask_float = []
        floating = []
        for i, c in enumerate(reversed(k)):
            if c == '1':
                mask_or |= 1 << i
            elif c == 'X':
                floating.append(i)

        full = (1 << 36) - 1

        if floating:
            for i in range(2**(len(floating))):
                mand = full
                mor = 0
                for j in range(len(floating)):
                    if i & (1 << j):
                        mor |= 1 << floating[j]
                    else:
                        mand ^= 1 << floating[j]

                mask_float.append((mand, mor))
 
        # print()
        # print("{:>036b}".format(full))
        # print(k, k)
        # for mand, mor in mask_float:
        #     print("{:>036b} {:>036b}".format(mand, mor))

    else:
        k, y = list(parse("mem[{:d}] = {:d}", line))
        mm = k | mask_or
        if mask_float:
            for mand, mor in mask_float:
                mom = (mm & mand) | mor
                mem[mom] = y
        else:
            print("yey")
            mem[mm] = y

print(sum(mem.values()))
# for k, v in mem.items():
#     print(k, v)
