import fileinput as fi
from collections import deque

lookup = {
    "N": (0, 1),
    "E": (1, 0),
    "S": (0, -1),
    "W": (-1, 0)
}

def solve(insts):
    # We use a queue, because it has easy rolling
    d = deque(lookup[x] for x in "ESWN")
    x, y = 0, 0

    for inst, amt in insts:
        if inst == "F":
            dx, dy = d[0]
            x += dx*amt
            y += dy*amt
        elif inst in lookup:
            dx, dy = lookup[inst]
            x += dx*amt
            y += dy*amt
        elif inst in "LR":
            a = amt//90
            if inst == "R":
                a = -a
            d.rotate(a)
        else:
            raise Error("WTF!")

    return abs(x) + abs(y)

insts = [(x[0], int(x[1:])) for x in fi.input() if x.rstrip()]
print(solve(insts))
