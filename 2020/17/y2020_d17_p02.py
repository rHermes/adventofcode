import fileinput as fi

import itertools as it

import collections

# findall
# search
# parse
# from parse import *

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

grid = collections.defaultdict(lambda: collections.defaultdict(lambda: collections.defaultdict(lambda: collections.defaultdict(bool))))

y = 0
gx = 0
for line in lines:
    for i,x in enumerate(line):
        grid[0][y][i][0] = (x == '#')
    gx = len(line)
    y += 1

# print(gx, y)


def around(x, y, z, w):
    a = set()
    for i in range(-1,2):
        for j in range(-1,2):
            for k in range(-1,2):
                for m in range(-1,2):
                    a.add((x+i,y+j,z+k,w+m))

    
    a.remove((x,y,z,w))
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

def step(g, gx, gy, gz, gw):
    changes = []
    for z in range(-(gz),(gz+1)):
        for y in range(-gy,gy):
            for x in range(-gx,gx):
                for w in range(-gw,gw):
                    arr = sum(g[az][ay][ax][aw] for (ax,ay,az,aw) in around(x,y,z,w))
                    ll = g[z][y][x][w]
                    if ll:
                        if arr not in [2,3]:
                            changes.append((x,y,z,w,False))
                    else:
                        if arr == 3:
                            changes.append((x,y,z,w,True))

    for x,y,z,w,n in changes:
        g[z][y][x][w] = n

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
    step(grid,gx+i,y+i,i,i+1)
    # print("====")

ans = 0
for v in grid.values():
    for vv in v.values():
        for vvv in vv.values():
            for vvvv in vvv.values():
                if vvvv == True:
                    ans += 1
print(ans)

