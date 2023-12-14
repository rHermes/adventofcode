import fileinput as fi
import itertools as it

grid = [[c for c in line.rstrip()] for line in fi.input()]
Y, X = (len(grid), len(grid[0]))

rocks = set()
stones = set()
for y, x in it.product(range(Y), range(X)):
    c = grid[y][x]
    if c == "O":
        stones.add((y,x))
    elif c == "#":
        rocks.add((y,x))


def north(rocks, stones):
    final_stones = set()
    for y, x in sorted(stones):
        while 0 < y and (y-1, x) not in final_stones and (y-1, x) not in rocks:
            y -= 1

        final_stones.add((y,x))

    return final_stones

def south(rocks, stones):
    final_stones = set()
    for y, x in sorted(stones, reverse=True):
        while y < Y-1 and (y+1, x) not in final_stones and (y+1, x) not in rocks:
            y += 1

        final_stones.add((y,x))

    return final_stones

def east(rocks, stones):
    final_stones = set()
    for x, y in sorted(((x,y) for y,x in stones), reverse=True):
        while x < X-1 and (y, x+1) not in final_stones and (y, x+1) not in rocks:
            x += 1

        final_stones.add((y,x))

    return final_stones

def west(rocks, stones):
    final_stones = set()
    for x, y in sorted((x,y) for y,x in stones):
        while 0 < x and (y, x-1) not in final_stones and (y, x-1) not in rocks:
            x -= 1

        final_stones.add((y,x))

    return final_stones

def get_sig(stones):
    sig = tuple(sorted(stones))
    sig = hash(sig)
    return sig

G = {}
def cycle(rocks, stones):
    sig = get_sig(stones)
    if sig in G:
        return G[sig]

    stones = north(rocks, stones)
    stones = west(rocks, stones)
    stones = south(rocks, stones)
    stones = east(rocks, stones)

    G[sig] = stones
    return stones


N = 1000000000
i = 0
skipped = False

seen = {}
while i < N:
    if not skipped:
        sig = get_sig(stones)
        if sig in seen:
            rest = N - i
            loop_size = i - seen[sig]
            i = N - (rest % loop_size)
            skipped = True
            continue
        else:
            seen[sig] = i

    stones = cycle(rocks, stones)
    i += 1

ans = 0
for y, _ in stones:
    ans += (Y - y)

print(ans)
