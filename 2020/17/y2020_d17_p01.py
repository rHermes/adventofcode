import fileinput as fi
from collections import defaultdict

def around(x, y, z):
    a = set()
    for i in range(-1,2):
        for j in range(-1,2):
            for k in range(-1,2):
                a.add((x+i,y+j,z+k))

    a.remove((x,y,z))
    return a

def step(G):
    heat = defaultdict(int)
    for l in G:
        # This is to make sure we evaluate nodes even if they have no one around them
        heat[l] += 0
        for p in around(*l):
            heat[p] += 1

    add = set()
    remove = set()
    for l, v in heat.items():
        if l in G:
            if v not in [2,3]:
                remove.add(l)
        else:
            if v == 3:
                add.add(l)

    # Update in place, to avoid allocating more memory
    G -= remove
    G |= add



G = set()
for y, line in enumerate(map(str.rstrip, fi.input())):
    for x, c in enumerate(line):
        if c == '#':
            G.add((x,y,0))

for _ in range(6):
    step(G)

print(len(G))
