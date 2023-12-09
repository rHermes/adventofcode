import fileinput as fi
import re

import more_itertools as mit
import z3

# Input parsing
INPUT = "".join(fi.input()).rstrip()
groups = INPUT.split("\n\n")
lines = list(INPUT.splitlines())
numbers = [list(map(int, re.findall("-?[0-9]+", line))) for line in lines]


phases = []
for g in groups[1:]:
    rgs = []
    for x in list(g.splitlines())[1:]:
        tr, sr, lr = map(int, x.split(" "))
        rgs.append((sr, tr, lr))

    phases.append(rgs)


grps_seeds = numbers[0]

s = z3.Solver()
zans = z3.Int("zans") 

goods = []
for start, l in mit.chunked(grps_seeds, 2):
    goods.append(z3.And(start <= zans, zans < (start + l)))

s.add(z3.Or(goods))

location = zans
for phase in phases:
    # We are in a phase
    temp = location
    sexpr = temp
    for sr, tr, lr in phase:
        sexpr = z3.If(
            z3.And(sr <= temp, temp < sr + lr),
            tr + (temp - sr),
            sexpr
        )

    location = sexpr

# We need to pin this one, since we want to get it's value later
fl = z3.Int("fl")
s.add(fl == location)

while s.check() == z3.sat:
    m = s.model()
    s.add(location < m[fl].as_long())

print(m[fl].as_long())
