import fileinput as fi
import itertools as it

dxs = set()
dys = set()

for y, row in enumerate(fi.input()):
    for x, c in enumerate(row.rstrip()):
        if c == '>':
            dxs.add((y,x))
        elif c == 'v':
            dys.add((y,x))

my, mx = y+1, x+1

for i in it.count(1):
    ndxs, ndys = set(),set()
    moved = False

    for y,x in dxs:
        np = (y,(x+1)%mx)
        if np not in dxs and np not in dys:
            ndxs.add(np)
            moved = True
        else:
            ndxs.add((y,x))

    for y,x in dys:
        np = ((y+1)%my,x)
        if np not in ndxs and np not in dys:
            ndys.add(np)
            moved = True
        else:
            ndys.add((y,x))

    dxs, dys = ndxs, ndys
    if not moved:
        break

print(i)
