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

    idx = np.s_[pb:jb, pa:ja]

    if line.startswith("toggle "):
        a[idx] += 2
    elif line.startswith("turn on"):
        a[idx] += 1
    elif line.startswith("turn off"):
        a[idx] -= 1
        a[idx] = a[idx].clip(min=0)

print(a.sum())
