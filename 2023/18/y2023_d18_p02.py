import fileinput as fi
import itertools as it

ext = 0
places = [(0,0)]
for line in fi.input():
    y,x = places[-1]
    dir, me, _ = line.split(" ")
    me = int(me)

    _, _, h = line.split(" ")
    h = h[2:-1]
    me = int(h[:5], base=16)
    dir = h[-1]

    ext += me

    if dir == "3":
        places.append((y+me, x))
    elif dir == "1":
        places.append((y-me, x))
    elif dir == "2":
        places.append((y, x-me))
    elif dir == "0":
        places.append((y, x+me))

AREA = 0
for (sy,sx), (dy,dx) in it.pairwise(reversed(places[:-1])):
    AREA += (sy+dy)*(sx-dx)

AREA = AREA // 2
inter = AREA - ext//2 + 1

print(inter + ext)
