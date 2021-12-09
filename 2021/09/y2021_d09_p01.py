import fileinput as fi
import itertools as it

def ortho(y, x, shape):
    sy, sx = shape
    if 0 < x: yield (y, x-1)
    if x < sx-1: yield (y, x+1)
    if 0 < y: yield (y-1, x)
    if y < sy-1: yield (y+1, x)


def solve(lines):
    board = [[int(c) for c in line] for line in lines]
    shape = (len(board), len(board[0]))

    ans = 0
    for (y,x) in it.product(range(shape[0]), range(shape[1])):
        if all(board[y][x] < board[ay][ax] for (ay,ax) in ortho(y, x, shape)):
            ans += board[y][x] + 1

    return ans


lines = map(str.rstrip, fi.input())
print(solve(lines))
