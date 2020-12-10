import fileinput as fi
import itertools as it

# findall, parse, search, with_pattern
from parse import *

import more_itertools as mit


ins = []
for line in fi.input():
    if line.rstrip():
        ins.append(line.rstrip())

nums = [int(x) for x in ins]

input_device = 3 + max(nums)
nums.append(0)
nums.append(3 + max(nums))

def can_connect(nums, x):
    for y in range(1,4):
        if x+y in nums:
            return y
    return None

diffs = {1: 0, 2: 0, 3: 0}
for x in nums:
    for y in range(1,4):
        if x+y in nums:
            diffs[y] += 1
            break

print(diffs[1]*diffs[3])
