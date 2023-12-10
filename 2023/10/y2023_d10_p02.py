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

            G[(y,x)].update(parts)
            sy, sx = y, x
            
            # We have to S, for the ray casting algorithm to work.
            if north in parts:
                if south in parts:
                    grid[y][x] = "|"
                elif east in parts:
                    grid[y][x] = "L"
                else:
                    grid[y][x] = "J"
            else:
                # We must have south here
                if east in parts:
                    grid[y][x] = "F"
                elif west in parts:
                    grid[y][x] = "7"
                else:
                    grid[y][x] = "-"



# We perform a depth first search here.
seen = set()
cur = cs.deque([(sy,sx)])
while cur:
    sy, sx = cur.pop()
    if (sy,sx) in seen:
        continue
    seen.add((sy,sx))

    for (ty,tx) in G[(sy,sx)] - seen:
        cur.append((ty,tx))

# Now we check each row with the even odd rule. The reason we just count L, | and J
# is that we imagine that the ray is being cast a 3/4 of the way up the cell. These are
# the only cells which have an upper part. This makes it easier to determine if we are
# inside or not
ans = 0
for y in range(Y):
    inside = False
    for x in range(X):
        c = grid[y][x]
        if (y,x) in seen and c in "L|J":
            inside = not inside

        ans += inside and (y,x) not in seen

print(ans)
