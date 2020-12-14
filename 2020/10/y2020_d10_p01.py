import fileinput as fi

nums = frozenset([int(x) for x in fi.input()] + [0,])

d1, d3 = 0, 1
for x in nums:
    if x+1 in nums:
        d1 += 1
    elif x+3 in nums:
        d3 += 1

print(d1*d3)
