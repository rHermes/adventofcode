import fileinput as fi
import itertools as it
import collections as cs
import collections.abc as abc

positionT = tuple[int,int]
def adj(y: int, x: int, shape: positionT) -> abc.Iterator[positionT]:
    """Returns all points around a point, given the shape of the array"""
    sy, sx = shape
    for dy,dx in it.product([-1,0,1], [-1,0,1]):
        if dy == 0 and dx == 0:
            continue

        py = y + dy
        px = x + dx

        if 0 <= px < sx and 0 <= py < sy:
            yield (py,px)


grid = [list(line.rstrip()) for line in fi.input()]
gsz = (len(grid), len(grid[0]))

Y, X = gsz



# The idea here is to store all numbers that are adjecent to a gear into a
# single list and then only considering the lists with exactly 2 items.
# The number detection logic is the same as in part one
gears = cs.defaultdict(list)

current_number = 0
current_gears = set()
for j in range(Y):
    for i in range(X):
        c = grid[j][i]

        if not c.isdigit():
            if current_number != 0:
                for sy,sx in current_gears:
                    gears[(sy,sx)].append(current_number)

            current_number = 0
            current_gears.clear()
            continue

        current_number = current_number * 10 + int(c)

        for ty,tx in adj(j, i, gsz):
            tc = grid[ty][tx]
            if tc == "*":
                current_gears.add((ty,tx))


    # put test here
    if current_number != 0:
        for sy,sx in current_gears:
            gears[(sy,sx)].append(current_number)

    current_number = 0
    current_gears.clear()

ans = 0
for numbers in gears.values():
    if len(numbers) != 2:
        continue

    ans += numbers[0] * numbers[1]

print(ans)
