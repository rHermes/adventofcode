import fileinput as fi
import itertools as it
import collections as cs


def solve(inar, start_grid, n):
    grid = cs.defaultdict(bool) # start with black
    grid.update(start_grid)

    cur = False
    for i in range(n):
        new_grid = cs.defaultdict(lambda: cur)

        to_consider = set()
        for (y,x), c in grid.items():
            for dy, dx in it.product([-1,0,1],[-1,0,1]):
                to_consider.add((y+dy, x+dx))

        for (y,x) in sorted(to_consider):
            wnam = 0
            for dy, dx in it.product([-1,0,1],[-1,0,1]):
                wnam <<= 1
                wnam += grid[(y+dy,x+dx)]

            new_grid[(y,x)] = inar[wnam]

        grid = new_grid

        # Flip the current set value.
        cur = inar[-cur]

    return sum(grid.values())

# input processing
inp = map(str.rstrip, fi.input())
inar = [x == '#' for x in next(inp)]
assert(len(inar) == 512)

# Skip one line
next(inp)

# read the rest of the board
grid = {}
for y, row in enumerate(inp):
    for x, c in enumerate(row):
        grid[(y,x)] = c == "#"

print(solve(inar, grid, 2))
