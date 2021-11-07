import fileinput as fi

import numpy as np

a = np.full((1000,1000), 0)

for line in map(str.rstrip, fi.input()):
    if line == "":
        continue

    w = line.split(" ")
    p1, p2 = w[-3], w[-1]
    pa, pb = map(int, p1.split(","))
    ja, jb = map(lambda x: int(x) + 1, p2.split(","))

    if line.startswith("toggle "):
        a[pb:jb, pa:ja] += 2
    elif line.startswith("turn on"):
        a[pb:jb, pa:ja] += 1
    elif line.startswith("turn off"):
        a[pb:jb, pa:ja] -= 1
        a[pb:jb, pa:ja] = a[pb:jb, pa:ja].clip(min=0)

print(a.sum())
