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

for line in lines[i:]:
    if line == "":
        i += 2
        break
    i += 1

valid = []
ans = 0
for line in lines[i:-1]:
    nums = [int(x) for x in line.split(",")]
    for num in nums:
        for (x1,x2), (y1,y2) in fields.values():
            if (x1 <= num <= x2 or y1 <= num <= y2):
                break
        else:
            ans += num

    # print(line)

print(ans)
