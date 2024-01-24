import fileinput as fi
import collections as cs

# Input parsing
grid = [[c for c in line.rstrip()] for line in fi.input()]
gsz = (len(grid), len(grid[0]))
Y,X = gsz

START = (0,0)
STARTX = 0
END = (Y,0)
for x in range(X):
    if grid[0][x] == ".":
        STARTX = x
        START = (0, x)
    if grid[Y-1][x] == ".":
        END = (Y-1,x)


# Let's find all intersections
intersections = set([START, END])
for y in range(1,Y-1):
    for x in range(1,X-1):
        if grid[y][x] == "#":
            continue

        good = 0
        good += grid[y-1][x] != "#"
        good += grid[y+1][x] != "#"
        good += grid[y][x-1] != "#"
        good += grid[y][x+1] != "#"

        if 3 <= good:
            intersections.add((y,x))

# Now we calculate the distance between all intersections
G = {}
for ST in intersections:
    G[ST] = {}
    seen = set()
    Q = cs.deque([(ST,0)])
    while Q:
        (cy, cx), steps = Q.popleft()
        if (cy,cx) in seen:
            continue
        else:
            seen.add((cy,cx))

        if (cy,cx) != ST and (cy,cx) in intersections:
            if (cy,cx) in G[ST]:
                print("WTF")

            G[ST][(cy,cx)] = steps
            continue

        west = (cy, cx-1)
        if 0 < cx and grid[cy][cx-1] != "#":
            Q.append((west, steps+1))

        east = (cy, cx+1)
        if cx < X-1 and grid[cy][cx+1] != "#":
            Q.append((east, steps+1))

        north = (cy-1, cx)
        if 0 < cy and grid[cy-1][cx] != "#":
            Q.append((north, steps+1))

        south = (cy+1, cx)
        if cy < Y-1 and  grid[cy+1][cx] != "#":
            Q.append((south, steps+1))


Q = [(START, frozenset(), 0)]
ans = 0
while Q:
    (cy,cx), prev, steps = Q.pop()
    if (cy,cx) == END:
        if ans < steps:
            ans = steps
            print("New best: ", ans)

        continue

    gv = prev | frozenset([(cy,cx)])

    for dst, cost in G[(cy,cx)].items():
        if dst not in gv:
            Q.append((dst, gv, steps + cost))

print(ans)
