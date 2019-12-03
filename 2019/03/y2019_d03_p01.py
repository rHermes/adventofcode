import fileinput

def solve(ss):
    x1, y1 = 0, 0
    x2, y2 = 0, 0

    places1 = set()
    places2 = set()

    trans = {
            "L": (-1, 0),
            "U": (0, 1),
            "R": (1, 0),
            "D": (0, -1)
            }

    for k in ss[0].split(","):
        d = k[:1]
        num = int(k[1:])

        dx, dy = trans[d]

        for i in range(num):
            x1, y1 = x1 + dx, y1 + dy
            places1.add((x1,y1))


    for k in ss[1].split(","):
        d = k[:1]
        num = int(k[1:])

        dx, dy = trans[d]


        for i in range(num):
            x2, y2 = x2 + dx, y2 + dy
            places2.add((x2,y2))

    
    sames = []
    for p1 in places1 & places2:
        if not (p1[0] == 0 and p1[1] == 0):
            sames.append(abs(p1[0]) + abs(p1[1]))

    return min(sames)

         



lines = [line.rstrip() for line in fileinput.input()]

print(solve(lines))
