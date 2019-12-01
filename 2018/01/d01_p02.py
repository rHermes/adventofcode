import fileinput

xs = [int(line.rstrip()) for line in fileinput.input()]
seen = set()

cur = 0
i = 0
while cur not in seen:
    seen.add(cur)
    cur += xs[i]
    i = (i+1) % len(xs)
print(cur)
