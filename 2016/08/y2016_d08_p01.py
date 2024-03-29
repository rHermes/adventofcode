import fileinput as fi

W = 50
H = 6

screen = [[False for _ in range(W)] for _ in range(H)]

for line in fi.input():
    if line.startswith("rect "):
        a, b = map(int, line[5:].split("x"))
        for row in range(b):
            for col in range(a):
                screen[row][col] = True

    elif line.startswith("rotate column "):
        first, sec = line[14:].split(" by ")
        col = int(first[2:])
        shift = int(sec)

        oldy = [screen[row][col] for row in range(H)]
        for row in range(H):
            screen[(row+shift) % H][col] = oldy[row]

    elif line.startswith("rotate row "):
        first, sec = line[11:].split(" by ")
        row = int(first[2:])
        shift = int(sec)

        oldx = [screen[row][col] for col in range(W)]
        for col in range(W):
            screen[row][(col + shift) % W] = oldx[col]


print(sum(sum(row) for row in screen))
