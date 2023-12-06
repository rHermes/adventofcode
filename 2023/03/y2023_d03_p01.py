import fileinput as fi
import itertools as it
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


# Input parsing
grid = [list(line.rstrip()) for line in fi.input()]
gsz = (len(grid), len(grid[0]))

Y, X = gsz

current_number = 0
has_symbol = False

ans = 0
for j in range(Y):
    for i in range(X):
        c = grid[j][i]

        if not c.isdigit():
            if has_symbol:
                ans += current_number

            current_number = 0
            has_symbol = False
            continue

        current_number = current_number * 10 + int(c)

        # We don't need to look for symbols if we already have one.
        if not has_symbol:
            for ty,tx in adj(j, i, gsz):
                tc = grid[ty][tx]
                if (not tc.isdigit()) and tc != ".":
                    has_symbol = True

    if has_symbol:
        ans += current_number

    current_number = 0
    has_symbol = False

print(ans)
