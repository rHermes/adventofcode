import fileinput as fi

import re
import itertools as it
import functools as ft

import more_itertools as mit
import collections
import math

import z3

# findall
# search
# parse
from parse import *

# grps = "".join(fi.input()).rstrip().split("\n\n")
# print(grps)

lines = []

for line in fi.input():
    if line.rstrip():
        lines.append(line.rstrip())

def eval_expr(expr):
    # print(expr)
    prts = expr.split(" ")
    i = 0
    # / we try to find it
    grps = []
    while i < len(prts):
        prt = prts[i]
        if '(' not in prts[i]:
            grps.append((False,prts[i]))
            i += 1
            continue
        
        subexpr = []
        # We have a paranthasis
        j = i
        first = True
        level = 0
        while first or level != 0:
            first = False
            for k in prts[j]:
                if k == '(':
                    level += 1
                if k == ')':
                    level -= 1
            j += 1

        subexpr = prts[i:j]

        grps.append((True,subexpr))
        
        i = j
    # print(grps) 
    l = grps[0]
    if l[0] == True:
        l = eval_expr(" ".join(l[1])[1:-1])
    else:
        l = int(l[1])

    i = 1
    while i < len(grps)-1:
        (_, op), r = grps[i], grps[i+1]
        if r[0] == True:
            r = eval_expr(" ".join(r[1])[1:-1])
        else:
            r = int(r[1])
        
        if op == '+':
            l += r
        elif op == '*':
            l *= r
        else:
            print(op)
            raise "WTF"

        i += 2
 
    return l
    # print(grps)

s = 0
for line in lines:
    # print(line)
    s += eval_expr(line)

print(s)



