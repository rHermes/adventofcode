import fileinput as fi
import itertools as it

def get_boards():
    groups = "".join(fi.input()).split("\n\n")
    for group in groups:
        lines = group.splitlines()
        tid = int(lines[0][5:-1])
        img = [[x == '#' for x in line] for line in lines[1:]]
        yield (tid,img)

def get_int_borders(board):
    BN = len(board)
    n = sum(board[0][i] << (BN-1-i) for i in range(BN))
    e = sum(board[i][BN-1] << (BN-1-i) for i in range(BN))
    s = sum(board[BN-1][i] << (BN-1-i) for i in range(BN))
    w = sum(board[i][0]  << (BN-1-i) for i in range(BN))
    return [n, e, s, w]

def reverse_bits(n, no_of_bits):
    result = 0
    for i in range(no_of_bits):
        result <<= 1
        result |= n & 1
        n >>= 1
    return result

boards = dict(get_boards())
borders = {tid: get_int_borders(board) for tid, board in boards.items()}
ids = list(borders.keys())

BN = len(boards[ids[0]])


matches = {i: 0 for i in boards.keys()}
for i, aid in enumerate(ids):
    ab = borders[aid]
    ar = [reverse_bits(x,BN) for x in ab]
    pls = set(ab + ar)

    # Not need to check onces with 4 matches pieces around it
    if matches[aid] == 4:
        continue

    for j, bid in enumerate(ids[i+1:]):
        if matches[bid] == 4:
            continue

        for bx in borders[bid]:
            if bx in pls:
                break
        else:
            continue
        matches[aid] += 1
        matches[bid] += 1

ans = 1
for k, v in matches.items():
    if v == 2:
        ans *= k

print(ans)
