import fileinput as fi
import itertools as it

def parse_input():
    INPUT = "".join(fi.input()).rstrip()
    groups = INPUT.split("\n\n")

    order = [int(x) for x in groups[0].split(",")]

    boards = []
    for st in groups[1:]:
        boards.append([[int(x) for x in line.split(" ") if x] for line in st.splitlines()])

    return (order, boards)


def check_done(board, got):
    for row in board:
        if all(x in got for x in row):
            return True

    for x in range(len(board[1])):
        if all(row[x] in got for row in board):
            return True

    return False


def solve(order, boards):
    got = set()
    for x in order:
        got.add(x)

        for board in boards:
            if check_done(board, got):
                a = sum(set(it.chain.from_iterable(board)) - got)
                return a * x


order, boards = parse_input()
print(solve(order, boards))
