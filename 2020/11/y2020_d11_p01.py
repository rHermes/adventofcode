import fileinput

lines = [line.rstrip() for line in fileinput.input() if line.rstrip()]

def around(lines, x, y):
    arounds = 0
    for (dy, dx) in [(-1,-1), (-1, 0), (-1, 1), (0,-1), (0, 1), (1,-1), (1,0), (1,1)]:
        zx = x - dx
        zy = y - dy
        if 0 <= zx < len(lines[0]) and 0 <= zy < len(lines) and lines[zy][zx] == '#':
            arounds += 1

    return arounds

def step(lines):
    nn = []
    for y in range(len(lines)):
        thi = []
        for x in range(len(lines[y])):
            if lines[y][x] == 'L':
                a = around(lines, x, y)
                if a == 0:
                    thi.append("#")
                else:
                    thi.append("L")
            elif lines[y][x] == '#':
                a = around(lines, x, y)
                if a >= 4:
                    thi.append("L")
                else:
                    thi.append("#")
            else:
                thi.append(lines[y][x])

        nn.append(thi)

    return nn

first = lines
two = step(lines)
while first != two:
    first = two
    two = step(two)

ans = 0
for l in two:
    for x in l:
        if x == '#':
            ans += 1

print(ans)
