import fileinput
import itertools as it


def solve(cmds):
    x1, y1 = 0,0
    x2, y2 = 0,0

    hs = {(0,0): 1}

    trans = {
            "^": (0, 1),
            "<": (-1, 0),
            ">": (1, 0),
            "v": (0, -1)
    }
    
    # I use cycle here because I can.
    for n, c in zip(it.cycle([False,True]), cmds):
        dx, dy = trans[c]
        if n:
            x1 += dx
            y1 += dy
            hs[(x1,y1)] = 1 + hs.get((x1,y1), 0)
        else:
            x2 += dx
            y2 += dy
            hs[(x2,y2)] = 1 + hs.get((x2,y2), 0)


    
    return len(hs.keys())


for line in fileinput.input():
    print(solve(line.rstrip()))
