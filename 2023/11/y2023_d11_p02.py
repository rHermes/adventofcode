import fileinput as fi

grid = [list(line.rstrip()) for line in fi.input()]

dys = []
for j in range(len(grid)):
    if all(c == "." for c in grid[j]):
        dys.append(j)

dxs = []
for i in range(len(grid[0])):
    if all(row[i] == "." for row in grid):
        dxs.append(i)

pos = [] 
for j in range(len(grid)):
    for i in range(len(grid[0])):
        if grid[j][i] == "#":
            pos.append((j,i))

# We update the positions
DIFF = 1000000
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
