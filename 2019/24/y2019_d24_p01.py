import fileinput


def hh(bugs):
    return tuple(bugs)

def evo(bugs):
    nbugs = set()
    for y in range(5):
        for x in range(5):
            d = [(0,-1), (1,0), (0, 1), (-1,0)]
            count = 0
            for dx, dy in d:
                if (x+dx, y+dy) in bugs:
                    count += 1

            if (count == 1 or count == 2) and (x,y) not in bugs:
                nbugs.add((x,y))
            elif (count == 1) and (x,y) in bugs:
                nbugs.add((x,y))

    return nbugs
                

def score(bugs):
    ans = 0
    pows = 0
    for y in range(5):
        for x in range(5):
            if (x,y) in bugs:
                ans += pow(2,pows)
            
            pows += 1

    return ans


def solve(board):
    bugs = set()
    for y in range(5):
        for x in range(5):
            if board[y][x] == "#":
                bugs.add((x,y))


    seen = set()
    seen.add(hh(bugs))

    while True:
        bugs = evo(bugs)

        h = hh(bugs)

        if h in seen:
            return score(bugs)
        else:
            seen.add(h)





board = [line.strip() for line in fileinput.input()]
print(solve(board))
