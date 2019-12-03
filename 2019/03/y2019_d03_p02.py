import fileinput

def solve(lines):
    places1 = set()
    places2 = set()
    steps1 = {}
    steps2 = {}

    trans = {
            "U": (0, 1),
            "R": (1, 0),
            "D": (0, -1),
            "L": (-1, 0)
            }
    for p, s, line in zip([places1, places2], [steps1, steps2], lines):
        x, y, j = 0, 0, 0

        for k in line.split(","):
            d = k[:1]
            num = int(k[1:])

            dx, dy = trans[d]
            for i in range(num):
                x += dx
                y += dy
                p.add((x,y))

                j += 1
                if (x,y) not in s:
                    s[(x,y)] = j

    sames = places1 & places2 - set([(0,0)])
    return min(steps1[p] + steps2[p] for p in sames)


lines = [line.rstrip() for line in fileinput.input()]
print(solve(lines))
