import fileinput as fi
import re
import itertools as it

lines = fi.input()

# Parse description
desc = list(it.takewhile(lambda x: x != "\n", lines))
stacks = []
for i, c in enumerate(desc[-1]):
    if c not in "123456789":
        continue
    
    stacks.append([])
    for line in desc[:-1]:
        if i < len(line) and line[i] not in "[ ]":
            stacks[-1].append(line[i])

# Find all remaining matches, and apply int to them.
exps = (re.fullmatch(r"move (\d+) from (\d+) to (\d+)", line.strip()) for line in lines)
matches = filter(bool, exps)
nums = (map(int, m.groups()) for m in matches)

for amount, src, dst in nums:
    orig = stacks[src-1]
    our, left = orig[:amount], orig[amount:]
    stacks[src-1] = left
    stacks[dst-1] = list(reversed(our)) + stacks[dst-1]

print("".join(stack[0] for stack in stacks)) 
