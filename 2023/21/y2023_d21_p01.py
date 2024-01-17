import fileinput as fi
import itertools as it
import collections as cs


# Input parsing
INPUT = "".join(fi.input()).rstrip()
lines = list(INPUT.splitlines())
grid = [[c for c in line] for line in lines]
gsz = (len(grid), len(grid[0]))
Y, X = gsz

# Return a map
def calcCost(open: set[tuple[int,int]], start: tuple[int,int]):
    cost = {}
    Q = cs.deque([(start, int(0))])
    while Q:
        pos, co = Q.popleft()
        if pos in cost:
            continue

        cost[pos] = co

        py, px = pos
        for np in [(py+1,px), (py-1,px), (py,px+1), (py,px-1)]:
            if np in open and np not in cost:
                Q.append((np, co+1))
    
    return cost

def numSteppedOn(cost: dict[tuple[int,int], int], remainingSteps: int, wantEvens: bool):
    ans = 0
    for (py,px), co in cost.items():
        if co <= remainingSteps and (py + px + wantEvens) % 2 != 0:
            ans += 1

    return ans

open = set()
start = (0, 0)
for y in range(Y):
    for x in range(X):
        c = grid[y][x]
        if c == "S":
            start = (y, x)
            open.add((y,x))
        elif c == ".":
            open.add((y,x))

blockC = (Y//2, X//2)
costC = calcCost(open, start)
print(numSteppedOn(costC, 64, True))
