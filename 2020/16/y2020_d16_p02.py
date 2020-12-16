import fileinput as fi

import re
import itertools as it
import functools as ft

import more_itertools as mit

import math

# findall
# search
# parse
from parse import *

lines = []

for line in fi.input():
    lines.append(line.rstrip())


i = 0
fields = {}
for line in lines:
    if line == "":
        i += 2
        break
    name, one_x, two_x, one_y, two_y = parse("{}: {:d}-{:d} or {:d}-{:d}", line).fixed
    fields[name] = ((one_x, two_x), (one_y, two_y))
    i += 1

# print(fields)

valid = []
for line in lines[i:]:
    if line == "":
        i += 2
        break
    nums = [int(x) for x in line.split(",")]
    for num in nums:
        for name, ((x1,x2), (y1,y2)) in fields.items():
            if (x1 <= num <= x2 or y1 <= num <= y2):
                break
        else:
            break
    else:
        # print(nums)
        valid.append(nums)
    i += 1

ans = 0
valid_fields = {k: 0 for k in fields.keys()}
for line in lines[i:]:
    if line == "":
        break
    nums = [int(x) for x in line.split(",")]
    for num in nums:
        for name, ((x1,x2), (y1,y2)) in fields.items():
            if (x1 <= num <= x2 or y1 <= num <= y2):
                break
        else:
            break
    else:
        # print(nums)
        valid.append(nums)

    # print(line)

vf = {}
for k in fields.keys():
    vf[k] = [True for _ in range(len(valid[0]))]


for nums in valid:
    for (i,num) in enumerate(nums):
        for name, ((x1,x2), (y1,y2)) in fields.items():
            if not (x1 <= num <= x2 or y1 <= num <= y2):
                vf[name][i] = False

# print(vf)
field_pos = {}
taken = set()
while len(field_pos) != len(fields):
    for k, v in vf.items():
        if sum(v) == 1:
            for i, l in enumerate(v):
                if l:
                    field_pos[k] = i

    for k, v in vf.items():
        for l in field_pos.values():
            v[l] = False

    # break

# print(field_pos)
# for nums in valid:

ans = 1
for k, v in field_pos.items():
    if k.startswith("departure"):
        ans *= valid[0][v]

print(ans)
