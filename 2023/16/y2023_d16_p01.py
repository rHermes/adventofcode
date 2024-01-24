import fileinput as fi
import re

# Debug logging
DEBUG = True
def gprint(*args, **kwargs):
    if DEBUG: print(*args, **kwargs)


grid = [[c for c in line.rstrip()] for line in fi.input()]
Y, X= (len(grid), len(grid[0]))


seen = set()
dups = set()
beams = [((0,0,0,1))]
while beams:
    y, x, dy, dx = beams.pop()
    if (y,x,dy,dx) in dups:
        continue
    else:
        dups.add((y,x,dy,dx))

    seen.add((y,x))

    c = grid[y][x]
    if c == ".":
        ty, tx = y + dy, x + dx
        if 0 <= tx < X and 0 <= ty < Y:
            beams.append((ty,tx,dy,dx))

    elif c == "/":
        if dx == 1:
            dy, dx = -1, 0
        elif dx == -1:
            dy, dx = 1, 0
        elif dy == 1:
            dy, dx = 0, -1
        elif dy == -1:
            dy, dx = 0, 1
        else:
            print("BIG PROBLEM")
        ty, tx = y + dy, x + dx
        if 0 <= tx < X and 0 <= ty < Y:
            beams.append((ty,tx,dy,dx))

    elif c == "\\":
        if dx == 1:
            dy, dx = 1, 0
        elif dx == -1:
            dy, dx = -1, 0
        elif dy == 1:
            dy, dx = 0, 1
        elif dy == -1:
            dy, dx = 0, -1
        else:
            print("BIG PROBLEM")

        ty, tx = y + dy, x + dx
        if 0 <= tx < X and 0 <= ty < Y:
            beams.append((ty,tx,dy,dx))

    elif c == "|":
        if dx == 1 or dx == -1:
            dy, dx = 1, 0
            ty, tx = y + dy, x + dx
            if 0 <= tx < X and 0 <= ty < Y:
                beams.append((ty,tx,dy,dx))

            dy, dx = -1, 0
            ty, tx = y + dy, x + dx
            if 0 <= tx < X and 0 <= ty < Y:
                beams.append((ty,tx,dy,dx))

        elif dy == 1 or dy == -1:
            ty, tx = y + dy, x + dx
            if 0 <= tx < X and 0 <= ty < Y:
                beams.append((ty,tx,dy,dx))
        else:
            print("BIG PROBLEM")

    elif c == "-":
        if dy == 1 or dy == -1:
            dy, dx = 0, 1
            ty, tx = y + dy, x + dx
            if 0 <= tx < X and 0 <= ty < Y:
                beams.append((ty,tx,dy,dx))

            dy, dx = 0, -1
            ty, tx = y + dy, x + dx
            if 0 <= tx < X and 0 <= ty < Y:
                beams.append((ty,tx,dy,dx))

        elif dx == 1 or dx == -1:
            ty, tx = y + dy, x + dx
            if 0 <= tx < X and 0 <= ty < Y:
                beams.append((ty,tx,dy,dx))
        else:
            print("BIG PROBLEM")

    else:
        print("We have a problem!")

print(len(seen))
