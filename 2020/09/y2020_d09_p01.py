import fileinput
import functools as ft
import itertools as it


import more_itertools as mit

# findall
# search
# parse
from parse import *

lines = []
for line in fileinput.input():
    if line.rstrip():
        lines.append(int(line.rstrip()))


for (i, num) in enumerate(lines):
    if i < 25:
        continue
    seen = False
    for j in range(max(0,i-25),i):
        for k in range(j+1,i):
            if lines[j] + lines[k] == num:
                seen = True

    if not seen:
        print(num)
