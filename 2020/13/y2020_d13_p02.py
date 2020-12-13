import fileinput as fi
import itertools as it
import functools as ft
import collections

import sys

# findall, search, parse with pattern
from parse import *

import more_itertools as mit

import z3


def print_works(i,a,j,b,N=20):
    t = 0
    x = 0
    ans = []
    while N > 0:
        if (t + i) % a == 0 and (t+j) % b == 0:
            # print("{}: {}".format(x, t))
            ans.append(t)
            x += 1
            N -= 1

        t += 1

    return ans

def period(i,a,j,b):
    t = 0
    dfs = []
    while (t + i) % a != 0 or (t+j) % b != 0:
        t += 1

    return t

# start and period
def real_period(i,a,j,b):
    x, y = print_works(i,a,j,b,N=2)
    return (x,y-x)



def check_works(i,a,j,b,offset,period):
    t = offset
    for x in range(100):
        if (t + i) % a != 0 or (t+j) % b != 0:
            # print(x)
            # print(t)
            return False
        t += period

    return True




lines = [x.rstrip() for x in fi.input() if x.rstrip()]

# nums = [int(x) for x in lines]

erl = int(lines[0])
busses = [(i, int(x)) for (i,x) in enumerate(lines[1].split(",")) if x != "x"]
# print(lines)
# print(busses)


# kv = print_works(0, 19, 13, 37, N=2)
# print(kv)
# (p1s, p1p) = real_period(0, 19, 13, 37)

# import math

def merge_periods(periods):
    nper = []
    i, a = periods[0]
    for (j,b) in periods[1:]:
        nper.append(real_period(i,a,j,b))

    return nper



# periods = merge_periods(busses)
# print(periods)
# periods2 = merge_periods(periods)
# print(periods2)
# periods3 = merge_periods(periods2)
# print(periods3)
# periods4 = merge_periods(periods3)
# print(periods4)
# periods2 = []
# i, a = periods[0]
# for (j,b) in periods[1:]:
#     periods2.append(real_period(i,a,j,b))

# print(periods2)
# # print(p1s, p1p)

# o1 = periods[0][0]
# t = o1
# df = periods[0][1]

def find_first_n_periods(busses, N, t=0, df=1):
    x1 = None
    x2 = None
    while True:
        # print(t)
        for (i,b) in busses[:N]:
            if (t + i) % b != 0:
                break
        else:
            if x1 == None:
                x1 = t
            elif x2 == None:
                x2 = t
                break

        t += df

    return (x1,x2-x1)


t = 0
df = 1
for n in range(0,len(busses)+1):
    t, df = find_first_n_periods(busses, n, t, df)

print(t)
