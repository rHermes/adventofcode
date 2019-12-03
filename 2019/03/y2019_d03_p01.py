import fileinput

def solve(lines):
    places1 = set()
    places2 = set()

    trans = {
            "U": (0, 1),
            "R": (1, 0),
            "D": (0, -1),
            "L": (-1, 0)
            }
    for p, line in zip([places1, places2], lines):
        x, y = 0, 0

        for k in line.split(","):
            d = k[:1]
            num = int(k[1:])

            dx, dy = trans[d]
            for i in range(num):
                x += dx
                y += dy
                p.add((x,y))

    sames = places1 & places2 - set([(0,0)])
    return min(abs(x) + abs(y) for x,y in sames)


lines = [line.rstrip() for line in fileinput.input()]
print(solve(lines))
