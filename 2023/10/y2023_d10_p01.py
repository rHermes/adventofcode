import fileinput as fi
import typing
import collections as cs

grid = [list(line.rstrip()) for line in fi.input()]
gsz = (len(grid), len(grid[0]))

# Create grid
G: typing.DefaultDict[tuple[int,int],set[tuple[int,int]]] = cs.defaultdict(set)
Y, X = gsz
sy, sx = 0, 0
for y in range(Y):
    for x in range(X):
        c = grid[y][x]

        east = (y,x+1)
        north = (y-1, x)
        west = (y, x-1)
        south = (y+1,x)

        if c == ".":
            continue
        elif c == "F":
            G[(y,x)].update((south, east))
        elif c == "|":
            G[(y,x)].update((north, south))
        elif c == "-":
            G[(y,x)].update((east, west))
        elif c == "L":
            G[(y,x)].update((east, north))
        elif c == "J":
            G[(y,x)].update((west, north))
        elif c == "7":
            G[(y,x)].update((west, south))
        elif c == "S":
            parts = set()
            if 0 < y and grid[y-1][x] in "F|7":
                    parts.add(north)
            if y < Y-1 and grid[y+1][x] in "|LJ":
                    parts.add(south)
            if 0 < x and grid[y][x-1] in "-LF":
                    parts.add(west)
            if x < X-1 and grid[y][x+1] in "-J7":
                    parts.add(east)

            # From my input
            G[(y,x)].update(parts)
            sy, sx = y, x

seen = set()
cur = cs.deque([(sy,sx,int(0))])
maxdepth = 0
while cur:
    sy, sx, depth = cur.popleft()
    if (sy,sx) in seen:
        continue

    maxdepth = max(depth, maxdepth)

    seen.add((sy,sx))

    for (ty,tx) in G[(sy,sx)] - seen:
        cur.append((ty,tx,depth+1))

print(maxdepth)
