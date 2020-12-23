import fileinput as fi
import itertools as it
from collections import defaultdict

mem = defaultdict(set)
for line in fi.input():
    parts = line.rstrip().split(" ")
    ids = int(parts[0][1:])
    x, y = [int(k) for k in parts[2][:-1].split(",")]
    w, h = [int(k) for k in parts[3].split("x")]

    for p in it.product(range(x,x+w),range(y,y+h)):
        mem[p].add(ids)

all_ids = set()
over_ids = set()
for k, v in mem.items():
    all_ids |= v

    if len(v) > 1:
        over_ids |= v

print(next(iter(all_ids - over_ids)))
