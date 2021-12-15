import fileinput as fi
import itertools as it
import heapq

def ortho(y, x, shape):
    """Returns all orthagonaly adjacent points, respecting boundary conditions"""
    sy, sx = shape
    if 0 < x: yield (y, x-1)
    if x < sx-1: yield (y, x+1)
    if 0 < y: yield (y-1, x)
    if y < sy-1: yield (y+1, x)

def solve(grid):
    gsz = (len(grid), len(grid[0]))
    dst = (gsz[0]-1, gsz[1]-1)
    Q = [(0, 0, 0)]

    seen = set()
    while len(Q) > 0:
        risk, y, x = heapq.heappop(Q)
        if (y,x) == dst:
            return risk

        if (y,x) in seen:
            continue
        else:
            seen.add((y,x))

        for ny,nx in ortho(y, x, gsz):
            if (ny,nx) in seen:
                continue

            heapq.heappush(Q, (grid[ny][nx] + risk, ny, nx))


    raise Exception("Should not be possible")

grid = [[int(c) for c in line] for line in map(str.rstrip, fi.input())]

print(solve(grid))
