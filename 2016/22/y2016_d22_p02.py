import fileinput as fi
import collections as cs

# Input parsing
INPUT = "".join(fi.input()).rstrip()
lines = list(INPUT.splitlines())

target_x = 0
max_y = 0
nodes = {}
for line in lines[2:]:
    nam, sz, used, avail, use = [x for x in line.split(" ") if x]
    _, x, y = nam.split("-")
    x = int(x[1:])
    y = int(y[1:])
    sz = int(sz[:-1])
    used = int(used[:-1])

    target_x = max(target_x, x)
    max_y = max(max_y, y)
    nodes[(x,y)] = (sz, used) 

Y = max_y
X = target_x

# We need to convert this node field, into something we can use.
# we will begin with removing all nodes, that could never be moved
# around
open_spot = (0,0)
blocked = set()
for y in range(0, Y+1):
    for x in range(0, X+1):
        sz, used = nodes[(x,y)]
        if 100 < sz:
            blocked.add((x,y))
        elif used == 0:
            open_spot = (x,y)

def bfs(blocked, start, stop, X, Y):
    seen = set()
    Q = cs.deque([(start, int(0))])
    while Q:
        pos, steps = Q.popleft()
        if pos in seen:
            continue
        else:
            seen.add(pos)

        if pos == stop:
            return steps

        px, py = pos
        for (dx, dy) in [(0,1), (0,-1), (1,0), (-1,0)]:
            gx, gy = px + dx, py + dy
            if not (0 <= gx <= X and 0 <= gy <= Y):
                continue
            if (gx,gy) in blocked:
                continue

            Q.append(((gx, gy), steps + 1))
            # if (gx, gy) not in nodes:


# There are 2 stages here.
# how much it costs to get the solution into the step before.
ans = bfs(blocked, open_spot, (target_x-1, 0), X, Y)

# we move the target one closer
ans += 1

# We now need to move it (target_x-1) turns to the right,
# which takes 5 steps for each move to the right we make.
ans += 5*(target_x-1)

print(ans)
