import fileinput as fi
import itertools as it

ext = 0
places = [(0,0)]
for line in fi.input():
    y,x = places[-1]
    dir, me, _ = line.split(" ")
    me = int(me)

    ext += me

    if dir == "U":
        places.append((y+me, x))
    elif dir == "D":
        places.append((y-me, x))
    elif dir == "L":
        places.append((y, x-me))
    elif dir == "R":
        places.append((y, x+me))

AREA = 0
for (sy,sx), (dy,dx) in it.pairwise(reversed(places[:-1])):
    AREA += (sy+dy)*(sx-dx)

AREA = AREA // 2
inter = AREA - ext//2 + 1
print(inter + ext)
