import fileinput as fi

import re
import itertools as it
import functools as ft

import more_itertools as mit

import math

import collections

import z3

import numpy as np

# findall
# search
# parse
from parse import *


INPUT = "".join(fi.input())

groups = INPUT.split("\n\n")
lines = list(INPUT.splitlines())


VV = None
ss = {}
for grp in groups:
    # print(grp)
    lins = list(grp.splitlines())
    tid = int(lins[0][5:-1])
    img = [[x == '#' for x in line] for line in lins[1:]]
    if VV == None:
        VV = len(img[0])
    ss[tid] = img


N = int(len(ss)**(0.5))

ids = list(ss.keys())

JJ = {}
for I in range(len(ids)):
    a = ss[ids[I]]
    an = [a[0][i] for i in range(VV)]
    ae = [a[i][VV-1] for i in range(VV)]
    ass = [a[VV-1][i] for i in range(VV)]
    aw = [a[i][0] for i in range(VV)]
    JJ[ids[I]] = 0


    for ax in [an, ae, ass, aw]:
        matches = 0
        for J in range(len(ids)):
            if I == J:
                continue

            b = ss[ids[J]]

            bn = [b[0][i] for i in range(VV)]
            be = [b[i][VV-1] for i in range(VV)]
            bss = [b[VV-1][i] for i in range(VV)]
            bw = [b[i][0] for i in range(VV)]

            # Check if any can match with any
            for y in [bn, be, bss, bw]:
                if ax == y or ax == list(reversed(y)):

                    matches += 1

        if matches == 0:
            JJ[ids[I]] += 1

ans = 1
for k, v in JJ.items():
    if v == 2:
        ans *= k
    
print(ans)
