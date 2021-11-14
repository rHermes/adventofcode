import fileinput as fi
import heapq

def is_open(x, y, c):
    w = x*x + 3*x + 2*x*y + y + y*y
    w += c
    bits = bin(w).count('1')
    return bits % 2 == 0

def pos_moves(pos):
    px, py = pos
    
    pas = [(px+1, py), (px, py+1)]
    if px > 0:
        pas.append((px-1, py))

    if py > 0:
        pas.append((px, py-1))


    return pas

def solve(c, start, stop):
    gx, gy = stop

    Q = [(0, start)]

    seen = set([start])
    while len(Q) > 0:
        depth, (px, py) = heapq.heappop(Q)

        if (px, py) == stop:
            return depth

        for nx, ny in pos_moves((px, py)):
            if (nx, ny) not in seen and is_open(nx, ny, c):
                heapq.heappush(Q, (depth+1, (nx, ny)))
                seen.add((nx, ny))

    return -1

start = (1,1)
goal = (31,39)
c = int(next(fi.input()))
print(solve(c, start, goal))
