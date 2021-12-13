import fileinput as fi
import itertools as it

inp = map(str.rstrip, fi.input())

dots = frozenset(tuple(map(int, line.split(","))) for line in it.takewhile(bool, inp))

for line in inp:
    d, w = line.split()[-1].split("=")
    w = int(w)

    newdots = set()
    for x,y in dots:
        nx, ny = x, y
        if d == 'y' and w < y:
            ny = w - (y - w)
        elif d == 'x' and w < x:
            nx = w - (x - w)

        newdots.add((nx,ny))

    dots = frozenset(newdots)

maxx = max(x for x,y in dots)
maxy = max(y for x,y in dots)

for y in range(maxy+1):
    print("".join(" █"[(x,y) in dots] for x in range(maxx+1)))
