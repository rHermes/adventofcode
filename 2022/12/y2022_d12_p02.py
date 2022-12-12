import fileinput as fi
import heapq


def ortho(y, x, shape):
    """Returns all orthagonaly adjacent points, respecting boundary conditions"""
    sy, sx = shape
    if 0 < x: yield (y, x-1)
    if x < sx-1: yield (y, x+1)
    if 0 < y: yield (y-1, x)
    if y < sy-1: yield (y+1, x)


# Input parsing
lines = filter(bool, map(str.rstrip, fi.input()))
grid = [list(line) for line in lines]
gsz = (len(grid), len(grid[0]))

def solve():
    my, mx = gsz
    roots = []
    for y in range(my):
        for x in range(mx):
            if grid[y][x] == "S":
                grid[y][x] = "a"
            if grid[y][x] == "E":
                end = (y, x)
                grid[y][x] = "z"

            grid[y][x] = ord(grid[y][x]) - ord("a")
    
    # (est, steps, pos)
    Q = [(25, 0, end)]
    seen = set((end,))
    while Q:
        _, score, path = heapq.heappop(Q)
        py,px = path
        c = grid[py][px]

        if c == 0:
            return score

        for (ly,lx) in ortho(py,px,gsz):
            pc = grid[ly][lx]
            if c - pc <= 1 and (ly,lx) not in seen:
                seen.add((ly,lx))
                heapq.heappush(Q, (pc + score + 1, score + 1, (ly,lx)))

print(solve())
