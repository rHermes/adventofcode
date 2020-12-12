import fileinput as fi

lookup = {
    "N": (0, 1),
    "E": (1, 0),
    "S": (0, -1),
    "W": (-1, 0)
}

def solve(insts):
    wx, wy = 10, 1
    x, y = 0, 0

    for inst, amt in insts:
        if inst == "F":
            x += wx*amt
            y += wy*amt
        elif inst in lookup:
            dx, dy = lookup[inst]
            wx += dx*amt
            wy += dy*amt
        elif inst in "LR":
            # What is a right turn, but 3 left turns?
            if inst == "R":
                amt *= 3

            for _ in range((amt % 360)//90):
                wx, wy = -wy, wx
        else:
            raise Error("WTF!")

    return abs(x) + abs(y)

insts = [(x[0], int(x[1:])) for x in fi.input() if x.rstrip()]
print(solve(insts))
