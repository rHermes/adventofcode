import fileinput as fi
import itertools as it
import re

lines = map(str.rstrip, fi.input())
dirs = next(lines)

# We skip a line, as it will be blank
next(lines)

nodes = {}
for line in lines:
    m = re.match(r"(\w+) = \((\w+), (\w+)\)", line)
    if not m:
        continue
    n, b, a = m.groups()
    nodes[n] = (b, a)

current = "AAA"
    
steps = 0
for c in it.cycle(dirs):
    if current == "ZZZ":
        break
    
    current = nodes[current][c == "R"]
    steps += 1



print(steps)
