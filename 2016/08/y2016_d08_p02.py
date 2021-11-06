import fileinput as fi

def print_screen(screen):
    for row in screen:
        for c in row:
            if c:
                print("█", end="")
            else:
                print(" ", end="")
        print("")

W = 50
H = 6

screen = [[False for _ in range(W)] for _ in range(H)]

for line in fi.input():
    if line.startswith("rect "):
        a, b = map(int,line[5:].split("x"))
        for row in range(b):
            for col in range(a):
                screen[row][col] = True

    elif line.startswith("rotate column "):
        rest = line[14:]
        first, sec = rest.split(" by ")
        col = int(first[2:])
        shift = int(sec)

        oldy = [screen[row][col] for row in range(H)]
        for row in range(H):
            screen[(row+shift) % H][col] = oldy[row]

    elif line.startswith("rotate row "):
        rest = line[11:]
        first, sec = rest.split(" by ")
        row = int(first[2:])
        shift = int(sec)

        oldx = [screen[row][col] for col in range(W)]
        for col in range(W):
            screen[row][(col + shift) % W] = oldx[col]


print_screen(screen)
