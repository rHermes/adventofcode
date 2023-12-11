import fileinput as fi

grid = [list(line.rstrip()) for line in fi.input()]
Y,X = len(grid), len(grid[0])

# These sets store which rows and columns need to be expanded
dys = set(range(Y))
dxs = set(range(X))
pos = []

for y in range(Y):
    for x in range(X):
        if grid[y][x] == "#":
            pos.append((y,x))
            dys.discard(y)
            dxs.discard(x)

# We update the positions
DIFF = 2
for i in range(len(pos)):
    ty,tx = pos[i]
    add_x = sum((DIFF - 1) for dx in dxs if dx < tx)
    add_y = sum((DIFF - 1) for dy in dys if dy < ty)

    pos[i] = (ty+add_y, tx+add_x)


ans = 0
for x in range(len(pos)):
    (ty,tx) = pos[x]
    for y in range(x+1,len(pos)):
        (sy,sx) = pos[y]
        ans += abs(tx-sx) + abs(ty-sy)

print(ans)
