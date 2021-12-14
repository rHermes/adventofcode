import fileinput as fi
import itertools as it
import collections as cs

inp = map(str.rstrip, fi.input())
goal = next(inp)

# Skip the blank line
next(inp)

rules = {}
for line in inp:
    a, b = line.split(" -> ")
    rules[a] = b

pairs = cs.Counter(x+y for x, y in zip(goal,goal[1:]))
counts = cs.Counter(goal)

for _ in range(10):
    ng = cs.Counter()
    for pair, times in pairs.items():
        c = rules[pair]
        ng[pair[0] + c] += times
        ng[c + pair[1]] += times

        counts[c] += times

    pairs = ng

print(max(counts.values())-min(counts.values()))
