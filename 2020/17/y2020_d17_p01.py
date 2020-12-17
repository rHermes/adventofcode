import fileinput as fi
import collections

# findall
# search
# parse

lines = []

for line in fi.input():
    if line.rstrip():
        lines.append(line.rstrip())

# lines = "".join(fi.input()).rstrip().split("\n\n")
# lines = "".join(fi.input()).rstrip().split("\n")
# for line in fi.input():
#     if line.rstrip():
#     else:
#         cur.append()

grid = collections.defaultdict(lambda: collections.defaultdict(lambda: collections.defaultdict(bool)))

y = 0
gx = 0
for line in lines:
    for i,x in enumerate(line):
        grid[0][y][i] = (x == '#')
    gx = len(line)
    y += 1

# print(gx, y)


def around(x, y, z):
    a = set()
    for i in range(-1,2):
        for j in range(-1,2):
            for k in range(-1,2):
                a.add((x+i,y+j,z+k))

    
    a.remove((x,y,z))
    return a

def print_board(g, gx, gy, gz):
    for z in range(-(gz),(gz+1)):
        print("z={}".format(z))
        for y in range(gy):
            for x in range(gx):
                if g[z][y][x]:
                    print("#", end="")
                else:
                    print(".", end="")
            print()
        print()

def step(g, gx, gy, gz):
    changes = []
    for z in range(-(gz),(gz+1)):
        for y in range(-gy,gy):
            for x in range(-gx,gx):
                arr = sum(g[az][ay][ax] for (ax,ay,az) in around(x,y,z))
                ll = g[z][y][x]
                if ll:
                    if arr not in [2,3]:
                        changes.append((x,y,z,False))
                else:
                    if arr == 3:
                        changes.append((x,y,z,True))

    for x,y,z,n in changes:
        g[z][y][x] = n

# print(lines)
# print(len(around(0,0,0)))
# print(around(0,0,0))

# print(grid)
# step(grid, gx, y, 1)

# print(grid)

for i in range(1,7):
    # print("STEP: {}".format(i))
    # print_board(grid, 10000,10000,i-1)
    # print("====")
    # step(grid,gx,y,i)
    step(grid,100,100,i)
    # print("====")

ans = 0
for v in grid.values():
    for vv in v.values():
        for vvv in vv.values():
            if vvv == True:
                ans += 1
print(ans)

