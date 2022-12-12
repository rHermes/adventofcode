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
    for y in range(my):
        for x in range(mx):
            if grid[y][x] == "S":
                start = (y, x)
                grid[y][x] = "a"
            if grid[y][x] == "E":
                end = (y, x)
                grid[y][x] = "z"

            grid[y][x] = ord(grid[y][x]) - ord("a")
    
    # The number of levels we have to go before we are at z
    # or how far away from the end we are.
    h = lambda y,x,c: max(25 - c, abs(y - end[0]) + abs(x -end[1]))

    start_positions = [start]
    Q = [(h(y, x, grid[y][x]), 0, (y,x)) for y,x in start_positions]
    heapq.heapify(Q)
    seen = set(start_positions)

    while Q:
        _, score, path = heapq.heappop(Q)
        py,px = path

        if path == end:
            return score

        c = grid[py][px]

        for (ly,lx) in ortho(py,px,gsz):
            pc = grid[ly][lx]
            if pc - c <= 1 and (ly,lx) not in seen:
                seen.add((ly,lx))
                heapq.heappush(Q, (score + 1 + h(ly,lx,pc), score + 1, (ly,lx)))

print(solve())
