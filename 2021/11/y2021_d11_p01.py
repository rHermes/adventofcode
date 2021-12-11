import fileinput as fi
import itertools as it

# Returns a
def adj(y, x, shape):
    """Returns all points around a point, given the shape of the array"""
    sy, sx = shape
    for dy,dx in it.product([-1,0,1], [-1,0,1]):
        if dy == 0 and dx == 0:
            continue

        py = y + dy
        px = x + dx

        if 0 <= px < sx and 0 <= py < sy:
            yield (py,px)


ans = 0
octo = [[int(c) for c in line.rstrip()] for line in fi.input()]
for _ in range(100):
    flashing, flashed = set(), set()
    # First we add 1 to each number
    for y, x in it.product(range(10), range(10)):
        octo[y][x] += 1
        if octo[y][x] > 9:
            flashing.add((y,x))

    while 0 < len(flashing):
        y, x = flashing.pop()
        flashed.add((y,x))
        for (y,x) in adj(y, x, (10,10)):
            octo[y][x] += 1
            if octo[y][x] > 9 and (y,x) not in flashed:
                flashing.add((y,x))

    for y, x in flashed:
        octo[y][x] = 0

    ans += len(flashed)

print(ans)
