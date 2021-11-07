import fileinput as fi

import numpy as np

W = 50
H = 6

screen = np.full((H, W), False)

for line in fi.input():
    if line.startswith("rect "):
        col, row = map(int, line[5:].split("x"))
        screen[:row,:col] = True

    elif line.startswith("rotate column "):
        first, sec = line[14:].split(" by ")
        col = int(first[2:])
        shift = int(sec)

        screen[:,col] = np.roll(screen[:,col], shift)

    elif line.startswith("rotate row "):
        first, sec = line[11:].split(" by ")
        row = int(first[2:])
        shift = int(sec)

        screen[row] = np.roll(screen[row], shift)

print(screen.sum())
