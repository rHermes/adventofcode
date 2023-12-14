import fileinput as fi
import itertools as it

grid = [[c for c in line.rstrip()] for line in fi.input()]
Y, X = (len(grid), len(grid[0]))

rocks = set()
stones = set()
for y, x in it.product(range(Y), range(X)):
    c = grid[y][x]
    if c == "O":
        stones.add((y,x))
    elif c == "#":
        rocks.add((y,x))

final_stones = set()
for y,x in sorted(stones):
    while 0 < y and (y-1, x) not in final_stones and (y-1, x) not in rocks:
        y -= 1

    final_stones.add((y,x))
ans = 0
for y, x in final_stones:
    ans += (Y - y)

print(ans)
