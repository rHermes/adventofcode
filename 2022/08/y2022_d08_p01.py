import fileinput as fi

# Input parsing
lines = filter(bool,map(str.rstrip,fi.input()))
grid = [[int(c) for c in line] for line in lines]
gsz = (len(grid), len(grid[0]))

my, mx = gsz

visible = set()

for y in range(my):
    max_v = -1
    for x in range(mx):
        v = grid[y][x]
        if max_v < v:
            visible.add((y,x))
            max_v = v
    
for y in range(my):
    max_v = -1
    for x in reversed(range(mx)):
        v = grid[y][x]
        if max_v < v:
            visible.add((y,x))
            max_v = v

for x in range(mx):
    max_v = -1
    for y in range(my):
        v = grid[y][x]
        if max_v < v:
            visible.add((y,x))
            max_v = v


for x in range(mx):
    max_v = -1
    for y in reversed(range(my)):
        v = grid[y][x]
        if max_v < v:
            visible.add((y,x))
            max_v = v

print(len(visible))  
