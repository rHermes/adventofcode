import fileinput as fi

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

ans = 0

Q = [((1,STARTX), START, 1)]
while Q:
    (cy,cx), prev, steps = Q.pop()
    if (cy,cx) == END:
        if ans < steps:
            ans = steps

        continue

    west = (cy, cx-1)
    if prev != west and grid[cy][cx-1] in ".<":
        Q.append((west, (cy,cx), steps+1))

    east = (cy, cx+1)
    if prev != east and grid[cy][cx+1] in ".>":
        Q.append((east, (cy,cx), steps+1))

    north = (cy-1, cx)
    if prev != north and grid[cy-1][cx] in ".^":
        Q.append((north, (cy,cx), steps+1))

    south = (cy+1, cx)
    if prev != south and grid[cy+1][cx] in ".v":
        Q.append((south, (cy,cx), steps+1))

print(ans)
