import fileinput as fi
import itertools as it
import heapq
import collections

def ortho(y, x, shape):
    sy, sx = shape
    if 0 < x: yield (y, x-1)
    if x < sx-1: yield (y, x+1)
    if 0 < y: yield (y-1, x)
    if y < sy-1: yield (y+1, x)


def solve(lines):
    board = [[int(c) for c in line] for line in lines]
    sy, sx = (len(board), len(board[0]))
    shape = (sy, sx)

    lowpoints = []
    for y, x in it.product(range(sy), range(sx)):
        if all(board[y][x] < board[ay][ax] for (ay,ax) in ortho(y, x, shape)):
            lowpoints.append((y,x))

    ans = [0, 0, 0]
    for (y,x) in lowpoints:
        Q = collections.deque([(y,x)])
        seen = set([(y,x)])

        while len(Q) > 0:
            y, x = Q.popleft()

            for (py,px) in ortho(y, x, shape):
                if (py,px) not in seen and board[py][px] < 9:
                    seen.add((py,px))
                    Q.append((py,px))

        heapq.heappushpop(ans, len(seen))

    return ans[0] * ans[1] * ans[2]


lines = map(str.rstrip, fi.input())
print(solve(lines))
