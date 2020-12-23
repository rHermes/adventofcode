import fileinput as fi
import itertools as it
from collections import defaultdict

mem = defaultdict(int) 
for line in fi.input():
    parts = line.rstrip().split(" ")
    ids = int(parts[0][1:])
    x, y = [int(k) for k in parts[2][:-1].split(",")]
    w, h = [int(k) for k in parts[3].split("x")]

    for p in it.product(range(x,x+w),range(y,y+h)):
        mem[p] += 1

print(sum(1 for v in mem.values() if v > 1))
