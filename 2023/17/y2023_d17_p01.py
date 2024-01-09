import fileinput as fi
import heapq

# Input parsing
grid = [[c for c in line.rstrip()] for line in fi.input()]
gsz = (len(grid), len(grid[0]))
Y, X = gsz

cost = {}

Q = [ (0, 0,0,0,1,0), (0, 0,0,1,0,0) ]

for p in Q:
    cost[p[1:]] = 0

heapq.heapify(Q)

taken = set()
while Q:
    kst, y, x, dy, dx, steps = heapq.heappop(Q)
    sig = hash((y, x, dy, dx, steps))
    if sig in taken:
        continue
    else:
        taken.add(sig)

    if (y,x) == (Y-1,X-1):
        print(kst)
        break

    pos = []
    if steps < 3:
        pos.append((y+dy, x+dx, dy,dx, steps+1))

    # Left and right
    pos.append((y-dx, x+dy, -dx, dy, 1))
    pos.append((y+dx, x-dy, dx, -dy, 1))

    for ty, tx, tdy, tdx, tsteps in pos:
        newsig = (ty,tx,tdy,tdx,tsteps)

        if 0 <= ty < Y and 0 <= tx < X and newsig not in taken:
            wk = kst + int(grid[ty][tx])
            if wk < cost.get(newsig, 1000000000000000000):
                cost[newsig] = wk
                heapq.heappush(Q, (wk, *newsig))
