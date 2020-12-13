import fileinput as fi
import itertools as it
import functools as ft
import collections

import sys

# findall, search, parse with pattern
from parse import *

import more_itertools as mit


lines = [x.rstrip() for x in fi.input() if x.rstrip()]

# nums = [int(x) for x in lines]

erl = int(lines[0])
busses = [int(x) for x in lines[1].split(",") if x != "x"]
# print(lines)
# print(busses)


bbus = 0
k = erl
while True:
    for bus in busses:
        if k % bus == 0:
            bbus = bus     
            print(bus * (k - erl))
            break
    else:
        k += 1
        continue
    
    break



