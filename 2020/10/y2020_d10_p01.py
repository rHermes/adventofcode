import fileinput as fi

nums = frozenset([int(x) for x in fi.input() if x.rstrip()] + [0,])

diffs = {1: 0, 2: 0, 3: 1}
for x in nums:
    for y in range(1,4):
        if x+y in nums:
            diffs[y] += 1
            break

print(diffs[1]*diffs[3])
