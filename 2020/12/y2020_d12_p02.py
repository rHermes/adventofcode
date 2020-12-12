import fileinput as fi


lookup = {
    "N": (0, 1),
    "E": (1, 0),
    "S": (0, -1),
    "W": (-1, 0)
}

# First is left, second rigth
lookup_turn = {
    "N": ["W", "E"],
    "E": ["N", "S"],
    "S": ["E", "W"],
    "W": ["S", "N"]
}


lookup_rotate = [lambda x,y: (-y, x), lambda x,y: (y, -x)]


def solve(insts):
    d = 'E'
    wx, wy = 10, 1
    x, y = 0, 0

    # print(x, y)
    for nd, amt in insts:
        # print(nd, amt)
        if nd == "F":
            x += wx*amt
            y += wy*amt
        elif nd in lookup:
            dx, dy = lookup[nd]
            wx += dx*amt
            wy += dy*amt
        elif nd in "LR":
            while amt > 0:
                d = lookup_turn[d][nd != "L"]
                wx, wy = lookup_rotate[nd != "L"](wx, wy)
                amt -= 90
        else:
            raise Error("WTF!")

        # print(x, y, d)

    return abs(x) + abs(y)

insts = []
for line in fi.input():
    if not line.rstrip():
        continue

    d, xr = line[0], int(line[1:])
    insts.append((d, xr))


print(solve(insts))
