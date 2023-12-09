import fileinput as fi
import itertools as it
import re
import math

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

starts = [x for x in nodes.keys() if x[-1] == "A"]
loop_steps = []


steps = 0
for c in it.cycle(dirs):
    if not starts:
        break

    new_starts = []
    for current in starts:
        if current[-1] == "Z":
            loop_steps.append(steps)
        else:
            new_starts.append(nodes[current][c == "R"])

    steps += 1

    starts = new_starts



print(math.lcm(*loop_steps))
