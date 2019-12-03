import fileinput

def solve(cmds):
    x,y = 0,0

    hs = {(0,0): 1}

    trans = {
            "^": (0, 1),
            "<": (-1, 0),
            ">": (1, 0),
            "v": (0, -1)
    }

    for c in cmds:
        dx, dy = trans[c]
        x += dx
        y += dy
        hs[(x,y)] = 1 + hs.get((x,y), 0)

    
    return len(hs.keys())


for line in fileinput.input():
    print(solve(line.rstrip()))
