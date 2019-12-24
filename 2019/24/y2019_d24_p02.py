import fileinput
from collections import defaultdict


def evo(ww):
    nw = {}

    for z in range(-1000,1000):
        # check if there is anything adjacent
        if not ((z in ww) or ((z+1) in ww) or (z-1 in ww)):
            continue

        ubugs = ww.get(z-1, set())
        dbugs = ww.get(z+1, set())
        bugs = ww.get(z, set())

        nbugs = set()
        for y in range(5):
            for x in range(5):
                d = [(0,-1), (1,0), (0, 1), (-1,0)]
                count = 0
                for dx, dy in d:
                    if (x+dx, y+dy) in bugs:
                        count += 1

                if (x,y) == (2,1):
                    for i in range(5):
                        if (i,0) in dbugs:
                            count += 1

                elif (x,y) == (2,3):
                    for i in range(5):
                        if (i,4) in dbugs:
                            count += 1

                elif (x,y) == (1,2):
                    for j in range(5):
                        if (0,j) in dbugs:
                            count += 1
                elif (x,y) == (3,2):
                    for j in range(5):
                        if (4,j) in dbugs:
                            count += 1

                if y == 0:
                    if (2,1) in ubugs:
                        count += 1
                if y == 4:
                    if (2,3) in ubugs:
                        count += 1

                if x == 0:
                    if (1,2) in ubugs:
                        count += 1
                if x == 4:
                    if (3,2) in ubugs:
                        count += 1
                
                if (x,y) == (2,2):
                    count = 0

                if (count == 1 or count == 2) and (x,y) not in bugs:
                    nbugs.add((x,y))
                elif (count == 1) and (x,y) in bugs:
                    nbugs.add((x,y))

        nw[z] = nbugs

    return nw

def solve(board):
    ww = {}
    bugs = set()
    for y in range(5):
        for x in range(5):
            if board[y][x] == "#":
                bugs.add((x,y))

    ww[0] = bugs

    
    for i in range(200):
        ww = evo(ww)

    ans = 0

    for bugs in ww.values():
        ans += len(bugs)

    return ans


board = [line.strip() for line in fileinput.input()]
print(solve(board))
